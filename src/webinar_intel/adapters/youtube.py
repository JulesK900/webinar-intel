from __future__ import annotations

import json
import os
import re
from urllib.parse import parse_qs, urlparse
from urllib.request import urlopen

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

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


def _api() -> YouTubeTranscriptApi:
    user = os.environ.get("WEBSHARE_PROXY_USERNAME")
    password = os.environ.get("WEBSHARE_PROXY_PASSWORD")
    if user and password:
        return YouTubeTranscriptApi(
            proxy_config=WebshareProxyConfig(proxy_username=user, proxy_password=password)
        )
    return YouTubeTranscriptApi()


def _oembed(video_id: str) -> dict:
    """Fetch title/channel via YouTube oEmbed (no API key needed)."""
    oembed_url = (
        "https://www.youtube.com/oembed?url="
        f"https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D{video_id}&format=json"
    )
    try:
        with urlopen(oembed_url, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception:
        return {}


def fetch_transcript(url: str) -> Transcript:
    video_id = extract_video_id(url)
    fetched = _api().fetch(video_id)
    segments = [
        TranscriptSegment(start_seconds=snippet.start, text=snippet.text) for snippet in fetched
    ]
    meta = _oembed(video_id)
    metadata = VideoMetadata(
        video_id=video_id,
        title=meta.get("title", ""),
        channel=meta.get("author_name", ""),
        url=f"https://www.youtube.com/watch?v={video_id}",
    )
    return Transcript(metadata=metadata, segments=segments)
