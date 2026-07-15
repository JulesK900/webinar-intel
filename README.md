# webinar-intel

Give it a competitor's YouTube webinar URL, get back a PMM-grade competitive brief — including the veiled competitor swipes a plain summary misses.

Works on any webinar the tracked competitor uploads to YouTube — no per-video configuration. Point it at a new URL and the same pipeline produces a fresh brief: overview, speaker roster, timestamped speaker-attributed claims, and GTM response recommendations.

## How it works (hybrid mode)

```bash
webinar-intel fetch "https://youtube.com/watch?v=..." --competitor zenity
```

That one local command fetches the transcript and pushes it. GitHub Actions then runs the Claude analysis, commits the brief to `briefs/`, and appends it to a Google Doc.

Why hybrid? YouTube blocks transcript requests from datacenter IPs, so the fetch runs locally; everything else (and all secrets) stays in GitHub.

## Fully local mode

```bash
webinar-intel brief "https://youtube.com/watch?v=..." --competitor zenity
```

Requires `ANTHROPIC_API_KEY` in `.env` (plus `BRIEF_DOC_ID` and `GOOGLE_SA_JSON` for the Google Doc append).

## Setup

```bash
git clone https://github.com/JulesK900/webinar-intel
cd webinar-intel
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

GitHub secrets used by CI: `ANTHROPIC_API_KEY`, `GOOGLE_SA_JSON`, `BRIEF_DOC_ID`.

## Profiles

The analysis is anchored by two markdown files:

- `profiles/us.md` — the company you represent: pillars, differentiators, sore spots, positioning language.
- `profiles/<competitor>.md` — the competitor: aliases, pillars, known claims, veiled-attack phrases.

The richer these files, the sharper the brief — especially the indirect-mention detection, which reads the transcript through both lenses.

## Reuse for your own company

The agent is fully profile-driven — nothing about the analyzed companies lives in the code. To adapt it:

1. Clone the repo.
2. Replace `profiles/us.md` with your own company (pillars, differentiators, sore spots, positioning language).
3. Add `profiles/<competitor>.md` for each competitor you track (aliases, pillars, known claims, veiled-attack phrases).
4. Set your own secrets (`ANTHROPIC_API_KEY`, and optionally `GOOGLE_SA_JSON` + `BRIEF_DOC_ID`).

That's it — `webinar-intel fetch <url> --competitor <slug>` now analyzes through your lens. Multiple competitors coexist as separate profile files selected by the `--competitor` flag.

## Brief output

Each brief covers: overview, speakers (with search links), coverage summary, direct competitor mentions, indirect/veiled mentions with interpretation, where they touched our territory, where they contradicted us, where they left an opening, and recommended GTM response.

Every claim carries a clickable `[H:MM:SS]` timestamp linking to that moment in the video, attributed to the speaker who said it.

## Room for improvement

- **Better context recognition** — speaker attribution is inferred by the LLM from self-intros and host handoffs; true speaker diarization (pyannote / WhisperX on the audio track) would make attribution robust in messy multi-speaker segments.
- **Richer video metadata** — publish date and duration via the YouTube Data API (oEmbed only provides title/channel).
- **Non-YouTube sources** — yt-dlp + Whisper fallback for on24, BrightTALK, and vendor-hosted recordings.
- **Historical diffing** — compare briefs across a competitor's webinars over time to surface positioning shifts.
- **Profile auto-refresh** — periodically re-crawl the competitor's site to keep pillars and taglines current.
