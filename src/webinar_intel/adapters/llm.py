from __future__ import annotations

import json
import os

from anthropic import Anthropic

from webinar_intel.core.models import Brief, Profile, Transcript


MODEL = "claude-opus-4-7"


PROMPT_TEMPLATE = """You are a senior PMM analyzing a competitor webinar transcript.

# Us (the company we represent)
{us}

# Competitor
{competitor}

# Transcript
{transcript}

Return a JSON object with exactly these keys (all values are lists of strings unless noted):
- overview: string, 2-3 sentences describing what the webinar was
- coverage: 5-8 bullets summarizing what was covered
- direct_mentions: quotes where a competitor is named directly (include timestamp if useful)
- indirect_mentions: veiled references ("legacy vendors", "point solutions", etc.) with your interpretation of who they mean and why
- touched_our_territory: moments where their claims overlap our pillars
- contradicted_us: claims that undermine our positioning
- left_openings: gaps or things they didn't say we could exploit
- recommended_response: 2-3 concrete GTM moves (blog, battle card update, sales talking point)

Return ONLY the JSON object, no prose."""


def analyze(transcript: Transcript, us: Profile, competitor: Profile) -> Brief:
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt = PROMPT_TEMPLATE.format(
        us=us.body,
        competitor=competitor.body,
        transcript=transcript.full_text,
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text
    data = json.loads(text)
    return Brief(metadata=transcript.metadata, **data)
