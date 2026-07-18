"""LLM calls, split by job so tokens go where judgment is needed.

Three calls instead of one monolith:

1. ``analyze_coverage``  — FAST model. Overview, speakers, coverage from the
   full transcript. Mechanical summarization; cheap tokens.
2. ``analyze_competitive`` — SMART model. The judgment call: only the
   detect-stage candidate windows plus focused vault files.
3. ``extract_learnings`` — FAST model. Distills new recurring claims and
   veiled phrasings so the vault gets smarter with every run.

Model names are env-overridable so forks can pick their own price point.
"""

from __future__ import annotations

import json
import os

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

COMPETITIVE_PROMPT = """You are a senior PMM analyzing excerpts from a competitor webinar.
A keyword scanner already extracted only the transcript moments that mention
competitors (directly or in veiled terms) or touch our territory. Excerpts are
separated by [...] markers; each line keeps its [H:MM:SS] timestamp.

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


def _ask_json(model: str, prompt: str, max_tokens: int = 4096) -> dict:
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(
        block.text for block in resp.content if isinstance(block, TextBlock)
    )
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Model returned non-JSON output: {text[:200]}") from exc


def analyze_coverage(transcript: Transcript) -> dict:
    """FAST model: overview, speakers, and coverage from the full transcript."""
    prompt = COVERAGE_PROMPT.format(transcript=transcript.timestamped_text)
    return _ask_json(FAST_MODEL, prompt, max_tokens=2048)


def analyze_competitive(
    candidates_text: str, us: UsContext, competitor: CompetitorContext
) -> dict:
    """SMART model: competitive judgment over candidate windows only."""
    prompt = COMPETITIVE_PROMPT.format(
        messaging=us.messaging,
        counters=us.counters,
        profile=competitor.profile,
        talk_tracks=competitor.talk_tracks,
        candidates=candidates_text,
        attribution_rule=ATTRIBUTION_RULE,
    )
    return _ask_json(SMART_MODEL, prompt, max_tokens=4096)


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
) -> Brief:
    """Run the split pipeline and assemble the brief."""
    coverage = analyze_coverage(transcript)
    competitive = analyze_competitive(
        candidates_text or transcript.timestamped_text, us, competitor
    )
    return Brief(metadata=transcript.metadata, **coverage, **competitive)
