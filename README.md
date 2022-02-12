# seg-text
[![pytest](https://github.com/ffreemt/seg-text/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/seg-text/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/seg_text.svg)](https://badge.fury.io/py/seg_text)

Segment multilingual text to sentences

## Prerequisite for Windows without a C compiler

`seg-text` depends on `polyglot` which in turn depengs on `pyicu`, `pycld2` and `Morfessor`. For windows without a C compiler (such as visiaul C or mingw C), these cannot be installed via pip directly.

However, readily available `whl` packages can be downloaded from [https://www.lfd.uci.edu/~gohlke/pythonlibs/](https://www.lfd.uci.edu/~gohlke/pythonlibs/). After that, install (for example for python 3.8 amd64) them via
```bash
pip install PyICU-2.8-cp38-cp38-win_amd64.whl pycld2-0.41-cp38-cp38-win_amd64.whl Morfessor-2.0.6-py3-none-any.whl
```

## Install `seg-text`

```shell
pip install seg-text
# or poetry add seg-text
# pip install git+https://github.com/ffreemt/seg-text
# poetry add git+https://github.com/ffreemt/seg-text

# To upgrade
pip install seg-text -U
# or poetry add seg-text@latest
```

## Use `seg-text`
```python
from seg_text import seg_text

prin(seg_text(" text 1\n test 2. Test 3"))
# ["text 1", "test 2.", "Test 3"]

text = """ “元宇宙”，英文為“Metaverse”。該詞出自1992年；的科幻小說《雪崩》。 """
print(seg_text(text))
# ["“元宇宙”，英文為“Metaverse”。", "該詞出自1992年；的科幻小說《雪崩》。"]

print(seg_text(text, extra="[;:]"))
# ["“元宇宙”，英文為“Metaverse”。", "該詞出自1992年；", "的科幻小說《雪崩》。"]

```

Refer to the source file `seg_text.py` for more details.