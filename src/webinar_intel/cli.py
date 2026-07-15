from __future__ import annotations

import re
from pathlib import Path

import typer
from dotenv import load_dotenv

from webinar_intel.adapters import llm, youtube
from webinar_intel.core.models import Profile
from webinar_intel.render.markdown import render


app = typer.Typer(add_completion=False, help="Analyze competitor webinars from YouTube.")


@app.command()
def brief(
    url: str = typer.Argument(..., help="YouTube URL or video ID"),
    competitor: str = typer.Option(
        ..., "--competitor", "-c", help="Competitor profile slug (matches profiles/<slug>.md)"
    ),
    profiles_dir: Path = typer.Option(Path("profiles"), "--profiles-dir"),
    out_dir: Path = typer.Option(Path("briefs"), "--out-dir"),
) -> None:
    """Generate a competitive brief from a YouTube webinar URL."""
    load_dotenv()

    us = _load_profile(profiles_dir / "us.md", "us")
    comp = _load_profile(profiles_dir / f"{competitor}.md", competitor)

    typer.echo(f"Fetching transcript for {url}...")
    transcript = youtube.fetch_transcript(url)

    typer.echo("Analyzing with Claude...")
    result = llm.analyze(transcript, us, comp)

    out_dir.mkdir(parents=True, exist_ok=True)
    slug = _slug(result.metadata.title or result.metadata.video_id)
    out_path = out_dir / f"{competitor}-{slug}.md"
    out_path.write_text(render(result))
    typer.echo(f"Wrote {out_path}")


def _load_profile(path: Path, name: str) -> Profile:
    if not path.exists():
        raise typer.BadParameter(f"Profile not found: {path}")
    return Profile(name=name, body=path.read_text())


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "webinar"


if __name__ == "__main__":
    app()
