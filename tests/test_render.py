from webinar_intel.core.models import Brief, VideoMetadata
from webinar_intel.render.markdown import render


def _brief() -> Brief:
    return Brief(
        metadata=VideoMetadata(
            video_id="abc12345678",
            title="Securing AI Agents",
            channel="Zenity",
            url="https://www.youtube.com/watch?v=abc12345678",
        ),
        overview="A Zenity webinar on agentic AI security.",
        coverage=["Point A", "Point B"],
        direct_mentions=["'CyberArk' at 12:30"],
        indirect_mentions=["'legacy vault vendors' likely refers to Entro/SailPoint"],
        touched_our_territory=["Discussed agent identity governance"],
        contradicted_us=[],
        left_openings=["Did not mention secret scanning across code"],
        recommended_response=["Ship a blog on NHI vs agent-behavior security"],
    )


def test_render_contains_all_sections():
    out = render(_brief())
    for heading in [
        "## Overview",
        "## What was covered",
        "## Direct competitor mentions",
        "## Indirect mentions",
        "## Where they touched our territory",
        "## Where they contradicted us",
        "## Where they left an opening",
        "## Recommended response",
    ]:
        assert heading in out


def test_render_handles_empty_section():
    out = render(_brief())
    assert "_None._" in out
