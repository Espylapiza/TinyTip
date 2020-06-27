#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import sys
from textwrap import wrap

from polyglot.detect import Detector
from pymouse import PyMouse

from gui import show_tip

# from translators.Bing import Bing
from translators.TextBlobTranslator import TextBlobTranslator

min_time = 2
max_time = 30
lang_to = "zh-CN"
retry_times = 2
max_width = 25
words_per_sec = 8


def show(text):
    show_time = min(max_time, max(min_time, len(text) // words_per_sec)) * 1000
    text = "\n".join(wrap(text, max_width))  # wrap
    x, y = PyMouse().position()
    show_tip(text, x, y, show_time)


if __name__ == "__main__":
    text = str(subprocess.check_output(["xclip", "-o"]).strip(), "utf-8")

    if len(text) == 0:
        show("")
        sys.exit(0)

    try:
        lang_from = Detector("what " + text).languages[0].code
    except Exception:
        show("unknown error")
        sys.exit(0)

    for _ in range(retry_times):
        blob = TextBlobTranslator(lang_from=lang_from, lang_to=lang_to)

        translation = blob.translate(text)
        if translation is not None:
            break

    if translation is None:
        print(123)
        show(text)
    else:
        print(456)
        show(translation)
