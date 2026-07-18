from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class TranscriptSegment(BaseModel):
    start_seconds: float
    text: str


class VideoMetadata(BaseModel):
    video_id: str
    title: str
    channel: str
    published_at: Optional[date] = None
    duration_seconds: Optional[int] = None
    url: str


class Transcript(BaseModel):
    metadata: VideoMetadata
    segments: list[TranscriptSegment] = Field(default_factory=list)

    @property
    def full_text(self) -> str:
        return "\n".join(seg.text for seg in self.segments)

    @property
    def timestamped_text(self) -> str:
        lines = []
        for seg in self.segments:
            total = int(seg.start_seconds)
            h, rem = divmod(total, 3600)
            m, s = divmod(rem, 60)
            stamp = f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
            lines.append(f"[{stamp}] {seg.text}")
        return "\n".join(lines)


class Profile(BaseModel):
    name: str
    body: str


class Brief(BaseModel):
    metadata: VideoMetadata
    # "own": the competitor hosted the webinar (their claims are the signal).
    # "third-party": someone else hosted and the competitor came up.
    mode: str = "third-party"
    overview: str
    speakers: list[str] = Field(default_factory=list)
    coverage: list[str]
    direct_mentions: list[str]
    indirect_mentions: list[str]
    touched_our_territory: list[str]
    contradicted_us: list[str]
    left_openings: list[str]
    recommended_response: list[str]
