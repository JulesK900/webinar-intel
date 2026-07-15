from __future__ import annotations

from datetime import date
from pydantic import BaseModel, Field


class TranscriptSegment(BaseModel):
    start_seconds: float
    text: str


class VideoMetadata(BaseModel):
    video_id: str
    title: str
    channel: str
    published_at: date | None = None
    duration_seconds: int | None = None
    url: str


class Transcript(BaseModel):
    metadata: VideoMetadata
    segments: list[TranscriptSegment] = Field(default_factory=list)

    @property
    def full_text(self) -> str:
        return "\n".join(seg.text for seg in self.segments)


class Profile(BaseModel):
    name: str
    body: str


class Brief(BaseModel):
    metadata: VideoMetadata
    overview: str
    coverage: list[str]
    direct_mentions: list[str]
    indirect_mentions: list[str]
    touched_our_territory: list[str]
    contradicted_us: list[str]
    left_openings: list[str]
    recommended_response: list[str]
