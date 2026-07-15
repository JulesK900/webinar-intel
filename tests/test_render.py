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
        speakers=["Karen Katz — Director AI Security, Zenity"],
        coverage=["Point A", "Point B"],
        direct_mentions=["[12:30] 'CyberArk mentioned by name'"],
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


def test_render_linkifies_timestamps():
    out = render(_brief())
    assert "[12:30](https://www.youtube.com/watch?v=abc12345678&t=750s)" in out


def test_render_speakers_with_linkedin():
    out = render(_brief())
    assert "## Speakers" in out
    assert "linkedin.com/search/results/people" in out
    assert "Karen+Katz" in out
