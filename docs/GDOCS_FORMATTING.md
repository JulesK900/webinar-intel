# Writing formatted content to Google Docs from an agent

A reusable pattern for any agent that outputs markdown and needs it to land in a Google Doc as clean native formatting — real headings, real bullets, bold text — instead of raw `##` and `**` symbols.

Reference implementation: [`src/webinar_intel/render/gdocs.py`](../src/webinar_intel/render/gdocs.py)

## The problem

The Docs API `insertText` request inserts *plain text*. If you push markdown through it, the reader sees the markdown syntax literally. There is no "insert markdown" endpoint.

## The pattern

One `batchUpdate` call with requests in this exact order:

1. **Parse** the markdown into blocks: `h1` / `h2` / `bullet` / `p`, stripping the `#`, `-`, and `**` markers. Record the offsets of bold spans while stripping.
2. **Insert once**: a single `insertText` with the entire plain text (paragraphs joined by `\n`). Compute each block's `startIndex`/`endIndex` from cumulative lengths — you know them in advance because there is only one insertion.
3. **Reset styles** over the full inserted range before applying anything. Text inserted at an index *inherits the style at that index* — if the doc previously started with a heading or bullet list, your inserted text joins it. Three reset requests:
   - `updateParagraphStyle` → `namedStyleType: NORMAL_TEXT`
   - `deleteParagraphBullets`
   - `updateTextStyle` → `bold: false`
4. **Apply styles** per block:
   - Headings: `updateParagraphStyle` with `HEADING_1` / `HEADING_2`.
   - Bullets: group *consecutive* bullet blocks into one `createParagraphBullets` request with `bulletPreset: BULLET_DISC_CIRCLE_SQUARE`. One request per run of bullets, not per bullet.
   - Bold spans: `updateTextStyle` with `bold: true` over the recorded offsets.

## Gotchas learned the hard way

- **Insert at index 1 to prepend** (newest-first docs). Index 0 is the document start marker and is invalid.
- **Style requests don't shift indexes** — `updateParagraphStyle`, `createParagraphBullets` (when there are no leading tabs), and `updateTextStyle` don't insert characters, so offsets computed against the single `insertText` stay valid.
- **Strip markdown markers *before* computing offsets.** Bold offsets must be relative to the stripped text, not the raw markdown.
- **`createParagraphBullets` on a range that spans multiple paragraphs** bullets each paragraph in the range — that's why grouping consecutive bullets into one range works.
- **Skip blank lines when parsing.** Every `\n` in the inserted text creates a paragraph; empty paragraphs give the doc a ragged look and waste style requests.
- **Requests execute sequentially inside one `batchUpdate`**, so reset-then-style ordering within a single call is safe.

## Auth (service account pattern)

- Create a GCP service account, enable the **Google Docs API**, download the JSON key.
- Share the target Doc with the service account's email as **Editor**.
- Ship the key as an env var (`GOOGLE_SA_JSON`, the full JSON on one line) — never in the repo.
- Scope needed: `https://www.googleapis.com/auth/documents`.

```python
creds = service_account.Credentials.from_service_account_info(
    json.loads(os.environ["GOOGLE_SA_JSON"]),
    scopes=["https://www.googleapis.com/auth/documents"],
)
docs = build("docs", "v1", credentials=creds, cache_discovery=False)
docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
```

## Extending the parser

The reference parser handles `#`, `##`, `-`, `**bold**`. If your agent emits more:

- `###` → `HEADING_3` (same pattern).
- Numbered lists → `createParagraphBullets` with `NUMBERED_DECIMAL_ALPHA_ROMAN`.
- Italic `*text*` → `updateTextStyle` with `italic: true` (parse after bold to avoid `**` collisions).
- Links `[text](url)` → strip to `text`, then `updateTextStyle` with a `link.url` over the span.
- Tables → hard. `insertTable` + per-cell insertion requires index gymnastics; consider rendering tables as indented text instead.
