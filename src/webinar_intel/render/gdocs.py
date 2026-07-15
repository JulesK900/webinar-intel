from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/documents"]

INLINE_RE = re.compile(r"\*\*(?P<bold>.+?)\*\*|\[(?P<ltext>[^\]]+)\]\((?P<lurl>[^)]+)\)")


def _client():
    raw = os.environ["GOOGLE_SA_JSON"]
    info = json.loads(raw)
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return build("docs", "v1", credentials=creds, cache_discovery=False)


def _parse_blocks(markdown: str) -> list[tuple[str, str, list[tuple[int, int]], list[tuple[int, int, str]]]]:
    """Parse markdown into (kind, plain_text, bold_ranges, link_ranges) blocks.

    kind is one of: h1, h2, bullet, p. Ranges are offsets into plain_text
    after stripping ** and []() markers. Link ranges carry the URL.
    """
    blocks = []
    for raw in markdown.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("## "):
            kind, text = "h2", line[3:]
        elif line.startswith("# "):
            kind, text = "h1", line[2:]
        elif line.startswith("- "):
            kind, text = "bullet", line[2:]
        else:
            kind, text = "p", line
        plain = ""
        bolds: list[tuple[int, int]] = []
        links: list[tuple[int, int, str]] = []
        pos = 0
        for m in INLINE_RE.finditer(text):
            plain += text[pos : m.start()]
            start = len(plain)
            if m.group("bold") is not None:
                plain += m.group("bold")
                bolds.append((start, len(plain)))
            else:
                plain += m.group("ltext")
                links.append((start, len(plain), m.group("lurl")))
            pos = m.end()
        plain += text[pos:]
        blocks.append((kind, plain, bolds, links))
    return blocks


def _build_requests(
    blocks: list[tuple[str, str, list[tuple[int, int]], list[tuple[int, int, str]]]],
    start: int = 1,
) -> list[dict]:
    """Build Docs API batchUpdate requests: one insertText + styling."""
    text = ""
    metas = []
    for kind, plain, bolds, links in blocks:
        s = start + len(text)
        text += plain + "\n"
        metas.append((kind, s, start + len(text), bolds, links))
    if not metas:
        return []

    full_range = {"startIndex": start, "endIndex": start + len(text)}
    requests: list[dict] = [
        {"insertText": {"location": {"index": start}, "text": text}},
        # Reset everything inherited from the insertion point first.
        {
            "updateParagraphStyle": {
                "range": full_range,
                "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"},
                "fields": "namedStyleType",
            }
        },
        {"deleteParagraphBullets": {"range": full_range}},
        {
            "updateTextStyle": {
                "range": full_range,
                "textStyle": {"bold": False},
                "fields": "bold",
            }
        },
    ]

    i = 0
    while i < len(metas):
        kind, s, e, bolds, links = metas[i]
        if kind in ("h1", "h2"):
            style = "HEADING_1" if kind == "h1" else "HEADING_2"
            requests.append(
                {
                    "updateParagraphStyle": {
                        "range": {"startIndex": s, "endIndex": e},
                        "paragraphStyle": {"namedStyleType": style},
                        "fields": "namedStyleType",
                    }
                }
            )
        elif kind == "bullet":
            j = i
            while j + 1 < len(metas) and metas[j + 1][0] == "bullet":
                j += 1
            requests.append(
                {
                    "createParagraphBullets": {
                        "range": {"startIndex": s, "endIndex": metas[j][2]},
                        "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
                    }
                }
            )
            for k in range(i, j + 1):
                _, ks, _, k_bolds, k_links = metas[k]
                for b0, b1 in k_bolds:
                    requests.append(_bold(ks + b0, ks + b1))
                for l0, l1, url in k_links:
                    requests.append(_link(ks + l0, ks + l1, url))
            i = j + 1
            continue
        for b0, b1 in bolds:
            requests.append(_bold(s + b0, s + b1))
        for l0, l1, url in links:
            requests.append(_link(s + l0, s + l1, url))
        i += 1
    return requests


def _link(start: int, end: int, url: str) -> dict:
    return {
        "updateTextStyle": {
            "range": {"startIndex": start, "endIndex": end},
            "textStyle": {"link": {"url": url}},
            "fields": "link",
        }
    }


def _bold(start: int, end: int) -> dict:
    return {
        "updateTextStyle": {
            "range": {"startIndex": start, "endIndex": end},
            "textStyle": {"bold": True},
            "fields": "bold",
        }
    }


def append_brief(doc_id: str, title: str, url: str, body_markdown: str) -> None:
    """Prepend a formatted brief to the top of the doc (newest first)."""
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header_md = f"# {title} — {stamp}\n{url}\n"
    # Drop the body's own H1 so we don't render two title lines.
    body_lines = body_markdown.splitlines()
    if body_lines and body_lines[0].startswith("# "):
        body_lines = body_lines[1:]
    blocks = _parse_blocks(header_md + "\n".join(body_lines))
    requests = _build_requests(blocks)
    if not requests:
        return
    docs = _client()
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
