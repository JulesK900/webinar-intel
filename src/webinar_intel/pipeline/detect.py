"""Detect stage: pure-Python candidate finder (no LLM, no tokens).

Scans the transcript for competitor terms, veiled-reference phrases, and
our-territory keywords, then extracts each hit with surrounding context.
Only these "candidate windows" are sent to the expensive judgment model,
instead of the full transcript.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from webinar_intel.core.models import Transcript


class DetectionResult(BaseModel):
    candidates_text: str
    window_count: int = 0
    hit_count: int = 0
    matched_terms: list[str] = Field(default_factory=list)
    total_segments: int = 0

    @property
    def coverage_ratio(self) -> float:
        """Rough share of the transcript forwarded to the judgment model."""
        if not self.total_segments:
            return 0.0
        return min(1.0, self.window_count * 5 / self.total_segments)


def _stamp(seconds: float) -> str:
    try:
        total = max(0, int(seconds))
    except (TypeError, ValueError):
        total = 0
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def find_candidates(
    transcript: Transcript, terms: list[str], context: int = 2
) -> DetectionResult:
    """Return timestamped candidate windows around every term hit.

    Each hit segment is expanded by ``context`` segments on both sides;
    overlapping windows are merged so quotes keep their surrounding flow.
    """
    segments = transcript.segments
    lowered_terms = [(t, t.lower()) for t in terms if t.strip()]
    hits: list[int] = []
    matched: dict[str, None] = {}

    for i, seg in enumerate(segments):
        text = seg.text.lower()
        for original, low in lowered_terms:
            if low in text:
                hits.append(i)
                matched.setdefault(original)

    if not hits:
        return DetectionResult(
            candidates_text="", total_segments=len(segments)
        )

    # Build [start, end] windows and merge overlaps.
    windows: list[list[int]] = []
    for i in sorted(set(hits)):
        start, end = max(0, i - context), min(len(segments) - 1, i + context)
        if windows and start <= windows[-1][1] + 1:
            windows[-1][1] = max(windows[-1][1], end)
        else:
            windows.append([start, end])

    blocks: list[str] = []
    for start, end in windows:
        lines = [
            f"[{_stamp(seg.start_seconds)}] {seg.text}"
            for seg in segments[start : end + 1]
        ]
        blocks.append("\n".join(lines))

    return DetectionResult(
        candidates_text="\n\n[...]\n\n".join(blocks),
        window_count=len(windows),
        hit_count=len(set(hits)),
        matched_terms=sorted(matched),
        total_segments=len(segments),
    )
