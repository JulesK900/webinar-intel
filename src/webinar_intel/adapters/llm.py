from __future__ import annotations

import json
import os

from anthropic import Anthropic
from anthropic.types import TextBlock

from webinar_intel.core.models import Brief, Profile, Transcript


MODEL = "claude-opus-4-7"


PROMPT_TEMPLATE = """You are a senior PMM analyzing a competitor webinar transcript.

# Us (the company we represent)
{us}

# Competitor
{competitor}

# Transcript
Each line is prefixed with its [H:MM:SS] timestamp in the video.
{transcript}

Return a JSON object with exactly these keys (all values are lists of strings unless noted):
- overview: string, 2-3 sentences describing what the webinar was
- speakers: one entry per speaker, formatted exactly as "Name — Title, Company"
  (use what they say when introducing themselves; if title or company is unknown, omit that part)
- coverage: 5-8 bullets summarizing what was covered
- direct_mentions: quotes where a competitor is named directly
- indirect_mentions: veiled references ("legacy vendors", "point solutions", etc.) with your interpretation of who they mean and why
- touched_our_territory: moments where their claims overlap our pillars
- contradicted_us: claims that undermine our positioning
- left_openings: gaps or things they didn't say we could exploit
- recommended_response: 2-3 concrete GTM moves (blog, battle card update, sales talking point)

Timestamp rule: every item in direct_mentions, indirect_mentions, touched_our_territory,
and contradicted_us MUST start with the [H:MM:SS] timestamp of the moment in the video
where the claim was made, taken from the transcript line prefixes. Example:
"[0:14:32] 'Buildtime inventory describes a system that stopped existing...' — undercuts our Salt Code story."

Return ONLY the JSON object, no prose."""


def analyze(transcript: Transcript, us: Profile, competitor: Profile) -> Brief:
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt = PROMPT_TEMPLATE.format(
        us=us.body,
        competitor=competitor.body,
        transcript=transcript.timestamped_text,
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in resp.content if isinstance(block, TextBlock))
    data = json.loads(text)
    return Brief(metadata=transcript.metadata, **data)
