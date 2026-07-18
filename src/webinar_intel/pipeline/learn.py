"""Vault learning: deterministic writes of LLM-distilled learnings.

The model only proposes learnings (see adapters.llm.extract_learnings);
this module appends them to the vault files with plain string operations,
so the files stay human-curated edit surfaces and nothing gets rewritten.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from webinar_intel.core.models import Brief
from webinar_intel.core.vault import CompetitorContext

TALK_TRACKS_HEADING = "## Learned from webinars"
PATTERNS_HEADING = "## Learned patterns"
HISTORY_MARKER = "<!-- runs -->"
# Both emphasis spellings: markdown formatters rewrite _text_ to *text*.
PLACEHOLDERS = (
    "_No webinar learnings recorded yet._",
    "*No webinar learnings recorded yet.*",
)


def _append_under_heading(text: str, heading: str, bullets: list[str]) -> str:
    """Append bullets at the end of the section that starts at ``heading``."""
    if heading not in text:
        return text.rstrip() + f"\n\n{heading}\n\n" + "\n".join(bullets) + "\n"
    head, _, tail = text.partition(heading)
    # Find where the section ends (next '## ' heading or end of file).
    lines = tail.splitlines()
    end = len(lines)
    for i, line in enumerate(lines[1:], start=1):
        if line.startswith("## "):
            end = i
            break
    section = "\n".join(lines[:end]).rstrip()
    rest = "\n".join(lines[end:])
    section += "\n" + "\n".join(bullets) + "\n"
    result = head + heading + section
    if rest:
        result += "\n" + rest
    for placeholder in PLACEHOLDERS:
        result = result.replace(placeholder, "")
    return result.rstrip() + "\n"


def record_learnings(
    competitor: CompetitorContext,
    learnings: dict,
    brief: Brief,
) -> list[Path]:
    """Write learnings + history into the vault. Returns the touched paths."""
    today = date.today().isoformat()
    title = brief.metadata.title or brief.metadata.video_id
    touched: list[Path] = []

    talk_lines = [
        f"- ({today}, [{title}]({brief.metadata.url})) {item}"
        for item in learnings.get("talk_track_learnings", [])
    ]
    if talk_lines:
        updated = _append_under_heading(
            competitor.talk_tracks_path.read_text(), TALK_TRACKS_HEADING, talk_lines
        )
        competitor.talk_tracks_path.write_text(updated)
        touched.append(competitor.talk_tracks_path)

    existing = {t.lower() for t in competitor.patterns}
    pattern_lines = [
        f"- {p}"
        for p in learnings.get("new_patterns", [])
        if p.strip() and p.strip().lower() not in existing
    ]
    if pattern_lines:
        updated = _append_under_heading(
            competitor.patterns_path.read_text(), PATTERNS_HEADING, pattern_lines
        )
        competitor.patterns_path.write_text(updated)
        touched.append(competitor.patterns_path)

    history_line = (
        f"- {today} — [{title}]({brief.metadata.url}): "
        f"{len(brief.direct_mentions)} direct, "
        f"{len(brief.indirect_mentions)} veiled, "
        f"{len(brief.contradicted_us)} contradictions"
    )
    history = competitor.history_path.read_text()
    if HISTORY_MARKER in history:
        history = history.replace(HISTORY_MARKER, f"{HISTORY_MARKER}\n{history_line}", 1)
    else:
        history = history.rstrip() + "\n" + history_line + "\n"
    competitor.history_path.write_text(history)
    touched.append(competitor.history_path)

    return touched
