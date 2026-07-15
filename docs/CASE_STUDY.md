# Case study — webinar-intel

## The PMM problem

Competitor webinars are one of the richest, least-processed sources of competitive intelligence. Positioning language, product bets, customer name-drops, and swipes at rivals all leak out in an hour of unscripted talk. But watching a competitor webinar end-to-end costs a PMM a working morning, and most of it isn't relevant.

## What this agent does

Feed it a YouTube URL for a competitor webinar. It returns a brief that answers the questions a PMM actually asks:

1. **What did they say?** (short coverage summary)
2. **Who did they name?** (direct competitor mentions with quotes)
3. **Who did they *imply*?** (indirect swipes: "legacy vendors", "point solutions", "vault-centric" — with an interpretation of who they mean)
4. **Where did they touch our territory?** (moments overlapping our positioning pillars)
5. **Where did they contradict us?** (claims that undermine our story)
6. **Where did they leave an opening?** (things they didn't say we could exploit)
7. **What should we do about it?** (2-3 concrete GTM moves)

## Why the indirect-mention detection matters

That's the part a human PMM does today and no off-the-shelf summarizer does well. It requires context about *both* sides: the competitor's known positioning language *and* your own pillars and sore spots. The agent is prompted with both profiles, so the model isn't just spotting keywords — it's reading swipes through the lens of your positioning.

## Architecture

Hexagonal Python (core / adapters / pipeline / render). YouTube captions API for transcript, Claude Opus for analysis, Markdown for output. No cron, no queue, no database — one URL in, one file out.

## What's next (documented, not built)

- yt-dlp + Whisper fallback for non-YouTube URLs (on24, vendor-hosted MP4).
- Batch mode for a competitor's full channel.
- Historical diffing: "how has their positioning shifted across five webinars?"
