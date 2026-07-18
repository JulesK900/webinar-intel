# webinar-intel

Give it a competitor's YouTube webinar URL, get back a PMM-grade competitive brief — including the veiled competitor swipes a plain summary misses.

Works on any webinar the tracked competitor uploads to YouTube — no per-video configuration. Point it at a new URL and the same pipeline produces a fresh brief: overview, speaker roster, timestamped speaker-attributed claims, and GTM response recommendations. And it gets smarter: every analyzed webinar feeds new competitor talk tracks and phrasings back into the knowledge base.

## 5-minute setup

```bash
git clone https://github.com/JulesK900/webinar-intel
cd webinar-intel
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

Then edit two folders in `context-vault/` (see below) and run:

```bash
webinar-intel brief "https://youtube.com/watch?v=..." --competitor zenity
```

That's the whole setup: one API key, two markdown folders. The brief lands in `briefs/` and is appended in full to `BRIEFS.md` — a single running log of every analysis, newest first. No Google account, no cloud config required.

## How it works (ICM-lite pipeline)

The pipeline follows the [Interpreted Context Methodology](https://github.com/RinDig/Interpreted-Context-Methdology) idea: small context files loaded per stage instead of one monolithic prompt — and the mechanical work is plain Python, so paid tokens only go where judgment is needed.

```
transcript
   |
   v
1. DETECT (pure Python, zero tokens)
   Keyword scan against the vault's pattern files finds every moment that
   names the competitor, uses a veiled swipe, or touches our territory.
   Only these candidate windows move forward (saved to briefs/candidates/
   for inspection).
   |
   v
2. COVERAGE (fast model, cheap tokens)
   Overview, speakers, and topic summary from the full transcript.
   |
   v
3. JUDGMENT (smart model, focused tokens)
   The candidate windows + our messaging + our counters + the competitor's
   known talk tracks -> mentions, territory overlaps, contradictions,
   openings, recommended response.
   |
   v
4. RENDER + LEARN
   Brief written to briefs/ and BRIEFS.md (and optionally a Google Doc).
   A final cheap call distills NEW recurring claims and veiled phrasings,
   which are appended to the competitor's vault files - so the next run
   detects more and knows more.
```

Compared to a single full-transcript prompt to the top model, this cuts token cost roughly 70% while giving the expensive model a cleaner, more focused task.

## The context vault

All company knowledge lives in `context-vault/` as small markdown files — nothing about the analyzed companies is in the code:

```
context-vault/
  us/
    identity.md      # who we are
    messaging.md     # pillars, positioning language, proof points
    counters.md      # differentiators + where competitors attack us
    patterns.md      # our-territory terms for the detect stage
  competitors/<slug>/
    profile.md       # who they are, pillars, head-to-head
    talk-tracks.md   # framing, attack angles, learned claims  <- grows per run
    patterns.md      # names, aliases, veiled phrases           <- grows per run
    history.md       # log of analyzed webinars                 <- grows per run
```

Every file is a plain-text edit surface: curate, correct, or extend anything by hand and the next run picks it up. The richer the vault, the sharper the brief.

## Hybrid mode (how this repo runs in production)

```bash
webinar-intel fetch "https://youtube.com/watch?v=..." --competitor zenity
```

That one local command fetches the transcript and pushes it. GitHub Actions then runs the analysis, commits the brief + BRIEFS.md + vault learnings, and (if configured) appends to a Google Doc.

Why hybrid? YouTube blocks transcript requests from datacenter IPs, so the fetch runs locally; everything else (and all secrets) stays in GitHub. CI secrets: `ANTHROPIC_API_KEY` (required), `GOOGLE_SA_JSON` + `BRIEF_DOC_ID` (optional).

## Optional: Google Docs delivery

For distributing briefs to sales/marketing in a shared running doc:

1. Create a Google Cloud service account with the Docs API enabled.
2. Share the target doc with the service account (Editor).
3. Set `GOOGLE_SA_JSON` (the key JSON) and `BRIEF_DOC_ID` as env vars or CI secrets.

When these are absent the pipeline just skips this step — markdown outputs always work.

## Reuse for your own company

1. Clone the repo.
2. Rewrite `context-vault/us/` for your company.
3. Add `context-vault/competitors/<slug>/` for each competitor (copy the zenity folder as a template).
4. Set `ANTHROPIC_API_KEY`.

`webinar-intel fetch <url> --competitor <slug>` now analyzes through your lens. Model choice is env-overridable (`WEBINAR_INTEL_SMART_MODEL`, `WEBINAR_INTEL_FAST_MODEL`) if you want a different cost/quality point.

## Brief output

Each brief covers: overview, speakers (with search links), coverage summary, direct competitor mentions, indirect/veiled mentions with interpretation, where they touched our territory, where they contradicted us, where they left an opening, and recommended GTM response.

Every claim carries a clickable `[H:MM:SS]` timestamp linking to that moment in the video, attributed to the speaker who said it.

## Room for improvement

- **Better context recognition** — speaker attribution is inferred by the LLM from self-intros and host handoffs; true speaker diarization (pyannote / WhisperX on the audio track) would make attribution robust in messy multi-speaker segments.
- **Semantic detect fallback** — the detect stage is keyword-based; a cheap-model sweep over the full transcript could catch truly novel veiled references that match no known pattern (the learning loop narrows this gap over time).
- **Richer video metadata** — publish date and duration via the YouTube Data API (oEmbed only provides title/channel).
- **Non-YouTube sources** — yt-dlp + Whisper fallback for on24, BrightTALK, and vendor-hosted recordings.
- **Historical diffing** — compare briefs across a competitor's webinars over time to surface positioning shifts (history.md is the seed for this).
