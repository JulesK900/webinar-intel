from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

import typer
from dotenv import load_dotenv

from webinar_intel.adapters import llm, youtube
from webinar_intel.core.models import Brief, Transcript
from webinar_intel.core.vault import CompetitorContext, UsContext, load_competitor, load_us
from webinar_intel.pipeline import detect, learn
from webinar_intel.render import briefs_log, gdocs
from webinar_intel.render.markdown import render


app = typer.Typer(add_completion=False, help="Analyze competitor webinars from YouTube.")

VAULT_OPTION = typer.Option(Path("context-vault"), "--vault-dir")


@app.callback()
def main() -> None:
    """webinar-intel: competitor webinar analysis."""


@app.command()
def fetch(
    url: str = typer.Argument(..., help="YouTube URL or video ID"),
    competitor: str = typer.Option(
        ...,
        "--competitor",
        "-c",
        help="Competitor slug (matches context-vault/competitors/<slug>/)",
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
        typer.echo("Pushed. GitHub Actions will analyze and publish the brief.")


@app.command()
def analyze(
    transcript_path: Path = typer.Argument(..., help="Path to transcripts/<video_id>.json"),
    vault_dir: Path = VAULT_OPTION,
    out_dir: Path = typer.Option(Path("briefs"), "--out-dir"),
) -> None:
    """Analyze a previously fetched transcript (runs in CI)."""
    load_dotenv()

    payload = json.loads(transcript_path.read_text())
    competitor = payload["competitor"]
    transcript = Transcript.model_validate(payload["transcript"])

    us, comp = _load_vault(vault_dir, competitor)
    result = _run_pipeline(transcript, us, comp, out_dir)
    _write_and_publish(result, competitor, out_dir)
    _record_learnings(result, comp)


@app.command()
def brief(
    url: str = typer.Argument(..., help="YouTube URL or video ID"),
    competitor: str = typer.Option(
        ...,
        "--competitor",
        "-c",
        help="Competitor slug (matches context-vault/competitors/<slug>/)",
    ),
    vault_dir: Path = VAULT_OPTION,
    out_dir: Path = typer.Option(Path("briefs"), "--out-dir"),
) -> None:
    """Fetch + analyze in one step (fully local mode)."""
    load_dotenv()

    us, comp = _load_vault(vault_dir, competitor)

    typer.echo(f"Fetching transcript for {url}...")
    transcript = youtube.fetch_transcript(url)

    result = _run_pipeline(transcript, us, comp, out_dir)
    _write_and_publish(result, competitor, out_dir)
    _record_learnings(result, comp)


def _load_vault(vault_dir: Path, competitor: str) -> tuple[UsContext, CompetitorContext]:
    try:
        return load_us(vault_dir), load_competitor(vault_dir, competitor)
    except FileNotFoundError as exc:
        raise typer.BadParameter(str(exc)) from exc


def _run_pipeline(
    transcript: Transcript, us: UsContext, comp: CompetitorContext, out_dir: Path
) -> Brief:
    # Detect stage: pure Python, zero tokens.
    detection = detect.find_candidates(transcript, us.patterns + comp.patterns)
    typer.echo(
        f"Detect stage: {detection.hit_count} hits in {detection.window_count} windows "
        f"({detection.total_segments} segments total); "
        f"terms: {', '.join(detection.matched_terms) or 'none'}"
    )
    if detection.candidates_text:
        candidates_dir = out_dir / "candidates"
        candidates_dir.mkdir(parents=True, exist_ok=True)
        candidates_path = candidates_dir / f"{transcript.metadata.video_id}.md"
        candidates_path.write_text(
            f"# Candidate windows — {transcript.metadata.title}\n\n"
            f"Matched terms: {', '.join(detection.matched_terms)}\n\n"
            "```\n" + detection.candidates_text + "\n```\n"
        )
        typer.echo(f"Wrote {candidates_path}")
    else:
        typer.echo("No candidate windows found; judgment call will read the full transcript.")

    typer.echo("Analyzing with Claude (coverage on fast model, judgment on smart model)...")
    return llm.analyze(transcript, us, comp, detection.candidates_text)


def _record_learnings(result: Brief, comp: CompetitorContext) -> None:
    typer.echo("Extracting learnings for the vault...")
    try:
        learnings = llm.extract_learnings(result, comp)
    except Exception as exc:  # noqa: BLE001 - learning must never fail the run
        typer.echo(f"Skipped vault learning (non-fatal): {exc}")
        return
    touched = learn.record_learnings(comp, learnings, result)
    for path in touched:
        typer.echo(f"Updated {path}")


def _write_and_publish(result: Brief, competitor: str, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = _slug(result.metadata.title or result.metadata.video_id)
    out_path = out_dir / f"{competitor}-{slug}.md"
    body = render(result)
    out_path.write_text(body)
    typer.echo(f"Wrote {out_path}")

    title = result.metadata.title or result.metadata.video_id
    briefs_log.prepend(Path("BRIEFS.md"), body, competitor, title)
    typer.echo("Updated BRIEFS.md")

    doc_id = os.environ.get("BRIEF_DOC_ID")
    if doc_id and os.environ.get("GOOGLE_SA_JSON"):
        gdocs.append_brief(doc_id, title, result.metadata.url, body)
        typer.echo(f"Appended to Google Doc {doc_id}")
    else:
        typer.echo("Google Docs delivery not configured; skipping (markdown outputs written).")


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "webinar"


if __name__ == "__main__":
    app()
