"""BRIEFS.md accumulator: every run's full brief in one file, newest first.

This is the zero-setup output channel: no Google account needed, the whole
run history is readable in a single markdown file in the repo.
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

HEADER = (
    "# Webinar briefs\n\n"
    "Full competitive briefs from every run, newest first. "
    "Individual briefs also live in `briefs/`.\n"
)
_HEADING_RE = re.compile(r"^(#{1,5}) ", flags=re.MULTILINE)


def _demote_headings(markdown: str) -> str:
    """Push every heading one level down so briefs nest under run headers."""
    return _HEADING_RE.sub(lambda m: "#" + m.group(1) + " ", markdown)


def prepend(log_path: Path, brief_markdown: str, competitor: str, title: str) -> None:
    entry_header = f"## {date.today().isoformat()} — {title} (vs {competitor})"
    body = _demote_headings(brief_markdown).strip()
    # The demoted brief starts with its own '## title' line; drop it since the
    # run header already carries the title.
    lines = body.splitlines()
    if lines and lines[0].startswith("## "):
        lines = lines[1:]
    entry = f"{entry_header}\n\n" + "\n".join(lines).strip() + "\n"

    if log_path.exists():
        existing = log_path.read_text()
        _, _, tail = existing.partition(HEADER)
        rest = tail if tail else existing
        content = HEADER + "\n" + entry + "\n---\n" + rest.lstrip("\n")
    else:
        content = HEADER + "\n" + entry
    log_path.write_text(content.rstrip() + "\n")
