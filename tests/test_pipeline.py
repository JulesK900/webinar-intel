"""Tests for the ICM-lite pipeline: vault, detect, learn, briefs log."""

from __future__ import annotations

from pathlib import Path

from webinar_intel.core.models import Brief, Transcript, TranscriptSegment, VideoMetadata
from webinar_intel.core.vault import CompetitorContext, parse_patterns
from webinar_intel.pipeline import detect, learn
from webinar_intel.render import briefs_log

VAULT = Path(__file__).resolve().parents[1] / "context-vault"


def _transcript(texts: list[str]) -> Transcript:
    return Transcript(
        metadata=VideoMetadata(
            video_id="vid1", title="Test Webinar", channel="chan", url="https://youtu.be/vid1"
        ),
        segments=[
            TranscriptSegment(start_seconds=i * 10, text=t) for i, t in enumerate(texts)
        ],
    )


def _brief(transcript: Transcript) -> Brief:
    return Brief(
        metadata=transcript.metadata,
        overview="An overview.",
        speakers=["Ada Example — CTO, ExampleCo"],
        coverage=["Topic one"],
        direct_mentions=["[0:20] Ada Example: 'legacy API security tools'"],
        indirect_mentions=[],
        touched_our_territory=[],
        contradicted_us=[],
        left_openings=[],
        recommended_response=[],
    )


def test_parse_patterns_extracts_bullets_and_dedupes() -> None:
    md = "# T\n\n## A\n\n- Zenity\n- zenity\n- intent-based detection\n\n## B\n\n- legacy vendors\n"
    assert parse_patterns(md) == ["Zenity", "intent-based detection", "legacy vendors"]


def test_detect_finds_and_merges_windows() -> None:
    t = _transcript(
        [
            "welcome to the webinar",
            "legacy API security tools cannot keep up",
            "more filler",
            "filler again",
            "even more filler",
            "closing remarks",
        ]
    )
    result = detect.find_candidates(t, ["legacy API security"], context=1)
    assert result.hit_count == 1
    assert result.window_count == 1
    assert "legacy API security tools" in result.candidates_text
    assert "[0:10]" in result.candidates_text
    assert "closing remarks" not in result.candidates_text


def test_detect_no_hits_returns_empty() -> None:
    t = _transcript(["nothing relevant here"])
    result = detect.find_candidates(t, ["Zenity"])
    assert result.candidates_text == ""
    assert result.window_count == 0


def test_briefs_log_prepends_newest_first(tmp_path: Path) -> None:
    log = tmp_path / "BRIEFS.md"
    briefs_log.prepend(log, "# First\n\n## Overview\nfoo\n", "zenity", "First")
    briefs_log.prepend(log, "# Second\n\n## Overview\nbar\n", "zenity", "Second")
    content = log.read_text()
    assert content.startswith("# Webinar briefs")
    assert content.index("Second") < content.index("First")
    # brief headings demoted so the log keeps a single H1
    assert "\n### Overview" in content
    assert content.count("\n# ") == 0


def test_record_learnings_appends_without_duplicates(tmp_path: Path) -> None:
    tt = tmp_path / "talk-tracks.md"
    tt.write_text("# X\n\n## Learned from webinars\n\n*No webinar learnings recorded yet.*\n")
    pat = tmp_path / "patterns.md"
    pat.write_text("# P\n\n## Veiled reference patterns\n\n- AISPM\n\n## Learned patterns\n")
    hist = tmp_path / "history.md"
    hist.write_text("# H\n\n<!-- runs -->\n")

    comp = CompetitorContext(
        slug="zenity",
        profile="profile",
        talk_tracks=tt.read_text(),
        patterns=parse_patterns(pat.read_text()),
        talk_tracks_path=tt,
        patterns_path=pat,
        history_path=hist,
    )
    t = _transcript(["x"])
    touched = learn.record_learnings(
        comp,
        {
            "talk_track_learnings": ["New recurring attack line"],
            "new_patterns": ["security theater", "AISPM"],
        },
        _brief(t),
    )
    assert {p.name for p in touched} == {"talk-tracks.md", "patterns.md", "history.md"}
    tt_text = tt.read_text()
    assert "New recurring attack line" in tt_text
    assert "No webinar learnings recorded yet" not in tt_text
    pat_text = pat.read_text()
    assert "security theater" in pat_text
    assert pat_text.count("AISPM") == 1  # existing pattern not duplicated
    assert "1 direct" in hist.read_text()


def test_vault_pattern_files_parse() -> None:
    us_terms = parse_patterns((VAULT / "us" / "patterns.md").read_text())
    zen_terms = parse_patterns(
        (VAULT / "competitors" / "zenity" / "patterns.md").read_text()
    )
    assert len(us_terms) > 10
    assert len(zen_terms) > 20
    assert "Zenity" in zen_terms
