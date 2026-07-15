from __future__ import annotations

from webinar_intel.core.models import Brief


def render(brief: Brief) -> str:
    m = brief.metadata
    parts: list[str] = []
    parts.append(f"# {m.title or m.video_id}")
    parts.append("")
    parts.append(f"- **Channel:** {m.channel}")
    parts.append(f"- **URL:** {m.url}")
    if m.published_at:
        parts.append(f"- **Published:** {m.published_at.isoformat()}")
    parts.append("")
    parts.append("## Overview")
    parts.append(brief.overview)
    parts.append("")
    _bullets(parts, "What was covered", brief.coverage)
    _bullets(parts, "Direct competitor mentions", brief.direct_mentions)
    _bullets(parts, "Indirect mentions", brief.indirect_mentions)
    _bullets(parts, "Where they touched our territory", brief.touched_our_territory)
    _bullets(parts, "Where they contradicted us", brief.contradicted_us)
    _bullets(parts, "Where they left an opening", brief.left_openings)
    _bullets(parts, "Recommended response", brief.recommended_response)
    return "\n".join(parts).rstrip() + "\n"


def _bullets(parts: list[str], heading: str, items: list[str]) -> None:
    parts.append(f"## {heading}")
    if not items:
        parts.append("_None._")
    else:
        for item in items:
            parts.append(f"- {item}")
    parts.append("")
