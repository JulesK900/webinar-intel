from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

import typer
from dotenv import load_dotenv

from webinar_intel.adapters import llm, youtube
from webinar_intel.core.models import Profile, Transcript
from webinar_intel.render import gdocs
from webinar_intel.render.markdown import render


app = typer.Typer(add_completion=False, help="Analyze competitor webinars from YouTube.")


@app.callback()
def main() -> None:
    """webinar-intel: competitor webinar analysis."""


@app.command()
def fetch(
    url: str = typer.Argument(..., help="YouTube URL or video ID"),
    competitor: str = typer.Option(
        ..., "--competitor", "-c", help="Competitor profile slug (matches profiles/<slug>.md)"
    ),
    out_dir: Path = typer.Option(Path("transcripts"), "--out-dir"),
    push: bool = typer.Option(True, "--push/--no-push", help="git commit + push the transcript"),
) -> None:
    """Fetch a transcript locally and push it so CI can analyze it (hybrid mode)."""
    typer.echo(f"Fetching transcript for {url}...")
    transcript = youtube.fetch_transcript(url)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{transcript.metadata.video_id}.json"
    payload = {"competitor": competitor, "transcript": transcript.model_dump(mode="json")}
    out_path.write_text(json.dumps(payload, indent=2))
    typer.echo(f"Wrote {out_path} ({len(transcript.segments)} segments)")

    if push:
        subprocess.run(["git", "add", str(out_path)], check=True)
        subprocess.run(
            ["git", "commit", "-m", f"transcript: {competitor} {transcript.metadata.video_id}"],
            check=True,
        )
        subprocess.run(["git", "push"], check=True)
        typer.echo("Pushed. GitHub Actions will analyze and update the Google Doc.")


@app.command()
def analyze(
    transcript_path: Path = typer.Argument(..., help="Path to transcripts/<video_id>.json"),
    profiles_dir: Path = typer.Option(Path("profiles"), "--profiles-dir"),
    out_dir: Path = typer.Option(Path("briefs"), "--out-dir"),
) -> None:
    """Analyze a previously fetched transcript (runs in CI)."""
    load_dotenv()

    payload = json.loads(transcript_path.read_text())
    competitor = payload["competitor"]
    transcript = Transcript.model_validate(payload["transcript"])

    us = _load_profile(profiles_dir / "us.md", "us")
    comp = _load_profile(profiles_dir / f"{competitor}.md", competitor)

    typer.echo("Analyzing with Claude...")
    result = llm.analyze(transcript, us, comp)

    _write_and_publish(result, competitor, out_dir)


@app.command()
def brief(
    url: str = typer.Argument(..., help="YouTube URL or video ID"),
    competitor: str = typer.Option(
        ..., "--competitor", "-c", help="Competitor profile slug (matches profiles/<slug>.md)"
    ),
    profiles_dir: Path = typer.Option(Path("profiles"), "--profiles-dir"),
    out_dir: Path = typer.Option(Path("briefs"), "--out-dir"),
) -> None:
    """Fetch + analyze in one step (fully local mode)."""
    load_dotenv()

    us = _load_profile(profiles_dir / "us.md", "us")
    comp = _load_profile(profiles_dir / f"{competitor}.md", competitor)

    typer.echo(f"Fetching transcript for {url}...")
    transcript = youtube.fetch_transcript(url)

    typer.echo("Analyzing with Claude...")
    result = llm.analyze(transcript, us, comp)

    _write_and_publish(result, competitor, out_dir)


def _write_and_publish(result, competitor: str, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = _slug(result.metadata.title or result.metadata.video_id)
    out_path = out_dir / f"{competitor}-{slug}.md"
    body = render(result)
    out_path.write_text(body)
    typer.echo(f"Wrote {out_path}")

    doc_id = os.environ.get("BRIEF_DOC_ID")
    if doc_id and os.environ.get("GOOGLE_SA_JSON"):
        title = result.metadata.title or result.metadata.video_id
        gdocs.append_brief(doc_id, title, result.metadata.url, body)
        typer.echo(f"Appended to Google Doc {doc_id}")
    else:
        typer.echo("Skipped Google Doc append (BRIEF_DOC_ID or GOOGLE_SA_JSON not set)")


def _load_profile(path: Path, name: str) -> Profile:
    if not path.exists():
        raise typer.BadParameter(f"Profile not found: {path}")
    return Profile(name=name, body=path.read_text())


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "webinar"


if __name__ == "__main__":
    app()
