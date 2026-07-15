# webinar-intel

Give it a competitor's YouTube webinar URL, get back a PMM-grade competitive brief — including the veiled competitor swipes a plain summary misses.

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

## Brief output

Each brief covers: overview, coverage summary, direct competitor mentions, indirect/veiled mentions with interpretation, where they touched our territory, where they contradicted us, where they left an opening, and recommended GTM response.
