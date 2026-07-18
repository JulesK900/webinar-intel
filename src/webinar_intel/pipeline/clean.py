"""Clean stage: apply vault ASR corrections to a transcript (zero tokens).

YouTube auto-captions mishear brand names and acronyms ("OASP" for "OWASP",
"Lamros" for "Lambros"). Left uncorrected, these break both the keyword
detect stage and the quality of quotes in the brief. Corrections live in
the vault as plain markdown (`corrections.md`) so anyone can extend them.
"""

from __future__ import annotations

import re

from webinar_intel.core.models import Transcript, TranscriptSegment


def apply_corrections(
    transcript: Transcript, pairs: list[tuple[str, str]]
) -> tuple[Transcript, int]:
    """Return a corrected copy of the transcript and the replacement count.

    Matching is case-insensitive on whole words; replacements keep the
    casing given in the vault file.
    """
    if not pairs:
        return transcript, 0

    compiled = [
        (re.compile(rf"\b{re.escape(wrong)}\b", flags=re.IGNORECASE), right)
        for wrong, right in pairs
    ]
    total = 0
    segments: list[TranscriptSegment] = []
    for seg in transcript.segments:
        text = seg.text
        for pattern, right in compiled:
            text, n = pattern.subn(right, text)
            total += n
        if text is seg.text or text == seg.text:
            segments.append(seg)
        else:
            segments.append(
                TranscriptSegment(start_seconds=seg.start_seconds, text=text)
            )
    if not total:
        return transcript, 0
    return Transcript(metadata=transcript.metadata, segments=segments), total
