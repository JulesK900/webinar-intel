from __future__ import annotations

import re
from urllib.parse import quote_plus

from webinar_intel.core.models import Brief

TIMESTAMP_RE = re.compile(r"^\[(\d+):(\d{2})(?::(\d{2}))?\]")

# Section headings per webinar mode: on a competitor's own webinar their
# positioning claims are the signal; on a third-party webinar the mentions are.
_HEADINGS = {
    "own": ("Key positioning claims", "Swipes at us / other vendors"),
    "third-party": ("Direct competitor mentions", "Indirect mentions"),
}


def render(brief: Brief) -> str:
    m = brief.metadata
    parts: list[str] = []
    parts.append(f"# {m.title or m.video_id}")
    parts.append("")
    parts.append(f"- **Channel:** {m.channel}")
    if brief.mode == "own":
        parts.append("- **Webinar type:** competitor-hosted (their claims analyzed)")
    parts.append(f"- **URL:** {m.url}")
    if m.published_at:
        parts.append(f"- **Published:** {m.published_at.isoformat()}")
    parts.append("")
    parts.append("## Overview")
    parts.append(brief.overview)
    parts.append("")
    if brief.speakers:
        parts.append("## Speakers")
        for speaker in brief.speakers:
            parts.append(f"- {speaker} ([search]({_speaker_search(speaker)}))")
        parts.append("")
    _bullets(parts, "What was covered", brief.coverage)
    mentions_heading, indirect_heading = _HEADINGS.get(
        brief.mode, _HEADINGS["third-party"]
    )
    _bullets(parts, mentions_heading, brief.direct_mentions, m.url)
    _bullets(parts, indirect_heading, brief.indirect_mentions, m.url)
    _bullets(parts, "Where they touched our territory", brief.touched_our_territory, m.url)
    _bullets(parts, "Where they contradicted us", brief.contradicted_us, m.url)
    _bullets(parts, "Where they left an opening", brief.left_openings, m.url)
    _bullets(parts, "Recommended response", brief.recommended_response, m.url)
    return "\n".join(parts).rstrip() + "\n"


def _bullets(parts: list[str], heading: str, items: list[str], video_url: str = "") -> None:
    parts.append(f"## {heading}")
    if not items:
        parts.append("_None._")
    else:
        for item in items:
            parts.append(f"- {_linkify_timestamp(item, video_url)}")
    parts.append("")


def _speaker_search(speaker: str) -> str:
    """Google search link for the speaker (more reliable than a LinkedIn people-search)."""
    # Drop parentheticals and collapse to 'Name Title Company' for a cleaner query.
    keywords = re.sub(r"\([^)]*\)", "", speaker)
    keywords = keywords.replace("\u2014", " ").replace(",", " ")
    keywords = re.sub(r"\s+", " ", keywords).strip()
    return f"https://www.google.com/search?q={quote_plus(keywords + ' linkedin')}"


def _linkify_timestamp(item: str, video_url: str) -> str:
    """Turn a leading [H:MM:SS] into a markdown link that jumps to that moment."""
    if not video_url:
        return item
    m = TIMESTAMP_RE.match(item)
    if not m:
        return item
    if m.group(3) is not None:
        h, mm, ss = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        h, mm, ss = 0, int(m.group(1)), int(m.group(2))
    seconds = h * 3600 + mm * 60 + ss
    stamp = m.group(0)[1:-1]
    sep = "&" if "?" in video_url else "?"
    return f"[{stamp}]({video_url}{sep}t={seconds}s){item[m.end() :]}"
