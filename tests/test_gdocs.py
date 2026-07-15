from webinar_intel.render.gdocs import _build_requests, _parse_blocks


SAMPLE = """# Title
## Section one
Intro paragraph with **bold part** inside.
- **Channel:** Zenity
- second bullet
## Section two
_None._
"""


def test_parse_blocks_kinds():
    blocks = _parse_blocks(SAMPLE)
    kinds = [b[0] for b in blocks]
    assert kinds == ["h1", "h2", "p", "bullet", "bullet", "h2", "p"]


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
    assert len(bullet_reqs) == 1


def test_build_requests_heading_styles():
    requests = _build_requests(_parse_blocks(SAMPLE))
    styles = [
        r["updateParagraphStyle"]["paragraphStyle"]["namedStyleType"]
        for r in requests
        if "updateParagraphStyle" in r
    ]
    assert styles.count("HEADING_1") == 1
    assert styles.count("HEADING_2") == 2
