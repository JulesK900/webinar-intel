from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi

from webinar_intel.core.models import Transcript, TranscriptSegment, VideoMetadata


VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def extract_video_id(url: str) -> str:
    if VIDEO_ID_RE.match(url):
        return url
    parsed = urlparse(url)
    if parsed.hostname in ("youtu.be",):
        return parsed.path.lstrip("/")
    if parsed.hostname and "youtube.com" in parsed.hostname:
        qs = parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0]
        parts = parsed.path.split("/")
        if "shorts" in parts or "embed" in parts:
            return parts[-1]
    raise ValueError(f"Could not extract YouTube video ID from: {url}")


def fetch_transcript(url: str) -> Transcript:
    video_id = extract_video_id(url)
    raw = YouTubeTranscriptApi.get_transcript(video_id)
    segments = [
        TranscriptSegment(start_seconds=item["start"], text=item["text"])
        for item in raw
    ]
    metadata = VideoMetadata(
        video_id=video_id,
        title="",
        channel="",
        url=f"https://www.youtube.com/watch?v={video_id}",
    )
    return Transcript(metadata=metadata, segments=segments)
