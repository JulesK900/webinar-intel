from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/documents"]


def _client():
    raw = os.environ["GOOGLE_SA_JSON"]
    info = json.loads(raw)
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return build("docs", "v1", credentials=creds, cache_discovery=False)


def append_brief(doc_id: str, title: str, url: str, body_markdown: str) -> None:
    """Prepend a new brief section to the top of the doc so newest is first."""
    docs = _client()
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = f"\n\n=== {title} — {stamp} ===\n{url}\n\n"
    payload = header + body_markdown + "\n\n"

    docs.documents().batchUpdate(
        documentId=doc_id,
        body={"requests": [{"insertText": {"location": {"index": 1}, "text": payload}}]},
    ).execute()
