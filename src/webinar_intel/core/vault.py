"""Context vault loading (ICM-lite layered context).

The vault separates stable "factory" context into small files so each
pipeline stage loads only what it needs:

    context-vault/
      us/
        identity.md      # who we are (cheap calls)
        messaging.md     # pillars + positioning (judgment call)
        counters.md      # differentiators + sore spots (judgment call)
        patterns.md      # our-territory detection terms (detect stage, no LLM)
      competitors/<slug>/
        profile.md       # who they are (judgment call)
        talk-tracks.md   # framing + learned claims (judgment call + learning)
        patterns.md      # names/aliases/veiled phrases (detect stage, no LLM)
        history.md       # run log (pure bookkeeping)
"""

from __future__ import annotations

import re
from pathlib import Path

from pydantic import BaseModel, Field


class UsContext(BaseModel):
    identity: str
    messaging: str
    counters: str
    patterns: list[str] = Field(default_factory=list)


class CompetitorContext(BaseModel):
    slug: str
    profile: str
    talk_tracks: str
    patterns: list[str] = Field(default_factory=list)
    talk_tracks_path: Path
    patterns_path: Path
    history_path: Path

    model_config = {"arbitrary_types_allowed": True}


def parse_patterns(markdown: str) -> list[str]:
    """Extract detection terms: every '- term' bullet under any heading."""
    terms: list[str] = []
    for line in markdown.splitlines():
        m = re.match(r"^\s*[-*]\s+(.+?)\s*$", line)
        if not m:
            continue
        term = m.group(1).strip().strip("`").strip()
        if term and not term.startswith("<!--"):
            terms.append(term)
    # de-duplicate, preserve order
    seen: set[str] = set()
    unique = []
    for t in terms:
        key = t.lower()
        if key not in seen:
            seen.add(key)
            unique.append(t)
    return unique


def _read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Vault file missing: {path}")
    return path.read_text()


def load_us(vault_dir: Path) -> UsContext:
    us = vault_dir / "us"
    return UsContext(
        identity=_read(us / "identity.md"),
        messaging=_read(us / "messaging.md"),
        counters=_read(us / "counters.md"),
        patterns=parse_patterns(_read(us / "patterns.md")),
    )


def load_competitor(vault_dir: Path, slug: str) -> CompetitorContext:
    comp = vault_dir / "competitors" / slug
    if not comp.is_dir():
        available = sorted(p.name for p in (vault_dir / "competitors").glob("*") if p.is_dir())
        raise FileNotFoundError(
            f"No competitor vault at {comp}. Available: {', '.join(available) or 'none'}"
        )
    talk_tracks_path = comp / "talk-tracks.md"
    patterns_path = comp / "patterns.md"
    history_path = comp / "history.md"
    return CompetitorContext(
        slug=slug,
        profile=_read(comp / "profile.md"),
        talk_tracks=_read(talk_tracks_path),
        patterns=parse_patterns(_read(patterns_path)),
        talk_tracks_path=talk_tracks_path,
        patterns_path=patterns_path,
        history_path=history_path,
    )
