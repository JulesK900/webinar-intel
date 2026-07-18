"""LLM calls, split by job so tokens go where judgment is needed.

Two webinar modes:

- "own" (default when the channel matches the competitor): the competitor is
  hosting, so everything they say is signal. A FAST-model sweep extracts their
  positioning claims, category framing, roadmap hints, and swipes; the SMART
  model then judges those claims against our messaging.
- "third-party": someone else is hosting and the competitor merely comes up.
  The pure-Python keyword detect stage supplies candidate windows.

Shared calls: ``analyze_coverage`` (FAST: overview/speakers/topics) and
``extract_learnings`` (FAST: distills new talk tracks + scanner phrases).
Model names are env-overridable so forks can pick their own price point.
"""

from __future__ import annotations

import json
import os
from json import JSONDecodeError

from anthropic import Anthropic
from anthropic.types import TextBlock

from webinar_intel.core.models import Brief, Transcript
from webinar_intel.core.vault import CompetitorContext, UsContext

SMART_MODEL = os.environ.get("WEBINAR_INTEL_SMART_MODEL", "claude-opus-4-7")
FAST_MODEL = os.environ.get("WEBINAR_INTEL_FAST_MODEL", "claude-haiku-4-5")

ATTRIBUTION_RULE = """Timestamp + attribution rule: every item MUST start with the [H:MM:SS]
timestamp of the moment in the video where the claim was made (taken from the
transcript line prefixes), followed by the speaker's name and a colon. Infer who
is speaking from context: self-introductions, host handoffs ("over to you, Rock"),
first-person references, and topic ownership. If you cannot confidently attribute
a quote, write "Unknown speaker:". Never guess a name you are not confident about.
Example:
"[0:14:32] Rock Lambros: 'Buildtime inventory describes a system that stopped
existing...' — undercuts our Salt Code story." """

COVERAGE_PROMPT = """You are summarizing a webinar transcript for a competitive intelligence brief.

# Transcript
Each line is prefixed with its [H:MM:SS] timestamp in the video.
{transcript}

Return a JSON object with exactly these keys:
- overview: string, 2-3 sentences describing what the webinar was
- speakers: list of strings, one entry per speaker, formatted exactly as
  "Name — Title, Company" (use what they say when introducing themselves;
  if title or company is unknown, omit that part)
- coverage: list of 5-8 strings summarizing what was covered

Return ONLY the JSON object, no prose."""

CLAIMS_PROMPT = """You are scanning the transcript of a webinar HOSTED BY our competitor
{competitor}. Extract every moment where a speaker makes a claim that matters
competitively. Keep the original [H:MM:SS] timestamps.

Extract moments of these kinds:
- positioning claims: how they describe their product, platform, or category
- category framing: names/frameworks they push to define the market
- roadmap or product hints: features, launches, integrations, plans
- swipes: attacks on other vendors or approaches, direct or veiled
  ("legacy tools", "point solutions", "traditional security", etc.)
- proof points: customers, metrics, research, standards-body roles they cite

DO NOT extract: introductions and pleasantries, housekeeping, generic industry
education with no competitive angle, audience Q&A logistics.

# Transcript
{transcript}

Return a JSON object with one key:
- claims: list of strings, each formatted as "[H:MM:SS] Speaker: 'short verbatim
  quote' — kind: positioning|category|roadmap|swipe|proof"

Be generous: 15-40 claims for a typical hour-long webinar. Return ONLY the JSON
object, no prose."""

OWN_WEBINAR_PROMPT = """You are a senior PMM at the company described under "Us". Our competitor
{competitor} hosted a webinar; below are the competitively relevant claims
their speakers made (extracted from the transcript, with timestamps).
Your job: tell our sales and marketing team what {competitor} is telling the
market, and how it cuts against us.

# Us — our messaging
{messaging}

# Us — our differentiators and known attack surfaces
{counters}

# Competitor profile
{profile}

# What we already know about their talk tracks (from past webinars and research)
{talk_tracks}

# Claims made in this webinar
{candidates}

Return a JSON object with exactly these keys (all values are lists of strings):
- direct_mentions: their most important POSITIONING CLAIMS - how they framed
  their product, category, and authority. Skip bare self-introductions; a
  speaker stating their own name and employer is NOT a positioning claim.
- indirect_mentions: SWIPES at us or other vendors, direct or veiled, with your
  interpretation of who they mean and why
- touched_our_territory: claims that overlap our pillars - where they are
  competing for the same ground
- contradicted_us: claims that undermine our positioning or architecture
- left_openings: gaps, admissions, or things they didn't say that we can exploit
- recommended_response: 2-3 concrete GTM moves (blog, battle card update,
  sales talking point)

{attribution_rule}

Return ONLY the JSON object, no prose."""

COMPETITIVE_PROMPT = """You are a senior PMM analyzing excerpts from a webinar in which our
competitor comes up. A keyword scanner already extracted only the transcript
moments that mention competitors (directly or in veiled terms) or touch our
territory. Excerpts are separated by [...] markers; each line keeps its
[H:MM:SS] timestamp.

# Us — our messaging
{messaging}

# Us — our differentiators and known attack surfaces
{counters}

# Competitor profile
{profile}

# What we already know about their talk tracks (from past webinars and research)
{talk_tracks}

# Transcript excerpts (candidate moments)
{candidates}

Return a JSON object with exactly these keys (all values are lists of strings):
- direct_mentions: quotes where a competitor is named directly
- indirect_mentions: veiled references ("legacy vendors", "point solutions", etc.)
  with your interpretation of who they mean and why
- touched_our_territory: moments where their claims overlap our pillars
- contradicted_us: claims that undermine our positioning
- left_openings: gaps or things they didn't say that we could exploit
- recommended_response: 2-3 concrete GTM moves (blog, battle card update,
  sales talking point)

{attribution_rule}

Return ONLY the JSON object, no prose."""

LEARNING_PROMPT = """You maintain a competitive intelligence knowledge base about {competitor}.
Below are the findings from a webinar we just analyzed, followed by what we
already know. Identify only what is GENUINELY NEW and likely to recur.

# New findings from this webinar
{findings}

# What we already know (do not repeat any of this)
{talk_tracks}

# Detection phrases we already scan for (do not repeat any of these)
{patterns}

Return a JSON object with exactly these keys:
- talk_track_learnings: list of strings, each a one-line recurring claim, theme,
  or attack line the competitor used that is not already recorded (empty list if
  nothing new)
- new_patterns: list of strings, each a SHORT verbatim phrase (2-6 words) the
  competitor used as a veiled swipe that a keyword scanner should catch in
  future transcripts (empty list if nothing new)

Be strict: prefer empty lists over noise. Return ONLY the JSON object."""


def _extract_json(text: str) -> dict:
    """Parse a JSON object from model output, tolerating code fences and prose.

    Fast models often wrap JSON in ```json fences even when told not to;
    fall back to the outermost {...} span before giving up.
    """
    candidate = text.strip()
    if candidate.startswith("```"):
        candidate = candidate.split("\n", 1)[1] if "\n" in candidate else ""
        if candidate.rstrip().endswith("```"):
            candidate = candidate.rstrip()[:-3]
    try:
        return json.loads(candidate)
    except JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except JSONDecodeError:
                pass
    raise ValueError(f"Model returned non-JSON output: {text[:200]}")


MAX_OUTPUT_TOKENS = 16384


def _ask_json(model: str, prompt: str, max_tokens: int = 4096) -> dict:
    """Call the model and parse a JSON object, growing the output budget on
    truncation (stop_reason == max_tokens) instead of failing on cut-off JSON."""
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    budget = max_tokens
    while True:
        resp = client.messages.create(
            model=model,
            max_tokens=budget,
            messages=[{"role": "user", "content": prompt}],
        )
        text = "".join(
            block.text for block in resp.content if isinstance(block, TextBlock)
        )
        if resp.stop_reason == "max_tokens" and budget < MAX_OUTPUT_TOKENS:
            budget = min(budget * 2, MAX_OUTPUT_TOKENS)
            continue
        if resp.stop_reason == "max_tokens":
            raise ValueError(
                f"Model output still truncated at {budget} tokens; "
                f"response starts: {text[:200]}"
            )
        return _extract_json(text)


def analyze_coverage(transcript: Transcript) -> dict:
    """FAST model: overview, speakers, and coverage from the full transcript."""
    prompt = COVERAGE_PROMPT.format(transcript=transcript.timestamped_text)
    return _ask_json(FAST_MODEL, prompt, max_tokens=2048)


def extract_claims(transcript: Transcript, competitor: CompetitorContext) -> list[str]:
    """FAST model: sweep the competitor's own webinar for competitive claims."""
    prompt = CLAIMS_PROMPT.format(
        competitor=competitor.slug,
        transcript=transcript.timestamped_text,
    )
    data = _ask_json(FAST_MODEL, prompt, max_tokens=4096)
    claims = data.get("claims", [])
    return [c for c in claims if isinstance(c, str) and c.strip()]


def analyze_competitive(
    candidates_text: str,
    us: UsContext,
    competitor: CompetitorContext,
    mode: str = "third-party",
) -> dict:
    """SMART model: competitive judgment over the candidate material."""
    template = OWN_WEBINAR_PROMPT if mode == "own" else COMPETITIVE_PROMPT
    prompt = template.format(
        competitor=competitor.slug,
        messaging=us.messaging,
        counters=us.counters,
        profile=competitor.profile,
        talk_tracks=competitor.talk_tracks,
        candidates=candidates_text,
        attribution_rule=ATTRIBUTION_RULE,
    )
    return _ask_json(SMART_MODEL, prompt, max_tokens=8192)


def extract_learnings(brief: Brief, competitor: CompetitorContext) -> dict:
    """FAST model: distill new recurring claims + scanner phrases from a brief."""
    findings = json.dumps(
        {
            "direct_mentions": brief.direct_mentions,
            "indirect_mentions": brief.indirect_mentions,
            "touched_our_territory": brief.touched_our_territory,
            "contradicted_us": brief.contradicted_us,
        },
        indent=1,
    )
    prompt = LEARNING_PROMPT.format(
        competitor=competitor.slug,
        findings=findings,
        talk_tracks=competitor.talk_tracks,
        patterns="\n".join(f"- {t}" for t in competitor.patterns),
    )
    data = _ask_json(FAST_MODEL, prompt, max_tokens=1024)
    return {
        "talk_track_learnings": data.get("talk_track_learnings", []),
        "new_patterns": data.get("new_patterns", []),
    }


def analyze(
    transcript: Transcript,
    us: UsContext,
    competitor: CompetitorContext,
    candidates_text: str,
    mode: str = "third-party",
) -> Brief:
    """Run the split pipeline and assemble the brief."""
    coverage = analyze_coverage(transcript)
    competitive = analyze_competitive(
        candidates_text or transcript.timestamped_text, us, competitor, mode=mode
    )
    return Brief(metadata=transcript.metadata, mode=mode, **coverage, **competitive)
