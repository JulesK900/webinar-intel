from webinar_intel.render.gdocs import _build_requests, _parse_blocks


SAMPLE = """# Title
## Section one
Intro paragraph with **bold part** inside.
- **Channel:** Zenity
- second bullet
## Section two
- [12:30](https://youtube.com/watch?v=x&t=750s) a timestamped claim
"""


def test_parse_blocks_kinds():
    blocks = _parse_blocks(SAMPLE)
    kinds = [b[0] for b in blocks]
    assert kinds == ["h1", "h2", "p", "bullet", "bullet", "h2", "bullet"]


def test_parse_blocks_strips_bold_markers():
    blocks = _parse_blocks(SAMPLE)
    para = blocks[2]
    assert "**" not in para[1]
    assert para[2] == [(21, 30)]
    assert para[1][21:30] == "bold part"


def test_build_requests_starts_with_single_insert():
    requests = _build_requests(_parse_blocks(SAMPLE))
    assert "insertText" in requests[0]
    inserted = requests[0]["insertText"]["text"]
    assert "##" not in inserted
    assert "**" not in inserted
    assert "- " not in inserted


def test_build_requests_bullets_grouped():
    requests = _build_requests(_parse_blocks(SAMPLE))
    bullet_reqs = [r for r in requests if "createParagraphBullets" in r]
    assert len(bullet_reqs) == 2


def test_parse_blocks_links():
    blocks = _parse_blocks(SAMPLE)
    last = blocks[-1]
    assert last[1].startswith("12:30 a timestamped")
    assert last[3] == [(0, 5, "https://youtube.com/watch?v=x&t=750s")]


def test_build_requests_link_style():
    requests = _build_requests(_parse_blocks(SAMPLE))
    link_reqs = [
        r
        for r in requests
        if "updateTextStyle" in r and "link" in r["updateTextStyle"]["textStyle"]
    ]
    assert len(link_reqs) == 1
    assert link_reqs[0]["updateTextStyle"]["textStyle"]["link"]["url"].endswith("t=750s")


def test_build_requests_heading_styles():
    requests = _build_requests(_parse_blocks(SAMPLE))
    styles = [
        r["updateParagraphStyle"]["paragraphStyle"]["namedStyleType"]
        for r in requests
        if "updateParagraphStyle" in r
    ]
    assert styles.count("HEADING_1") == 1
    assert styles.count("HEADING_2") == 2
