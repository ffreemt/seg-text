"""Test test-en.txt."""
# pylint: disable=invalid-name
from pathlib import Path

from seg_text import seg_text

file_en = "tests/test-en.txt"
text_en = Path(file_en).read_text(encoding="utf8")
list_en = [elm for elm in text_en.splitlines() if elm.strip()]

file_zh = "tests/test-zh.txt"
text_zh = Path(file_zh).read_text(encoding="utf8")
list_zh = [elm for elm in text_zh.splitlines() if elm.strip()]


def test_en_text():
    """Test test-en text."""
    _ = seg_text(text_en)
    assert (len(_)) == 59
    _ = seg_text(text_en, lang="en")
    assert (len(_)) == 59

    _ = seg_text(list_en)
    assert (len(_)) == 59
    _ = seg_text(list_en, lang="en")
    assert (len(_)) == 59


def test_zh_text():
    """Test test-zh text."""
    _ = seg_text(text_zh)
    assert (len(_)) == 84
    _ = seg_text(text_zh, lang="zh")
    assert (len(_)) == 84

    _ = seg_text(list_zh)
    assert (len(_)) == 84
    _ = seg_text(list_zh, lang="zh")
    assert (len(_)) == 84
