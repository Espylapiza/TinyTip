#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
from translators.Bing import Bing
from gui import show_tip
from pymouse import PyMouse
from textwrap import wrap
from polyglot.detect import Detector

min_time = 2
max_time = 30
lang_to = "zh"
retry_times = 5
max_width = 25
words_per_sec = 6

if __name__ == "__main__":
    text = str(subprocess.check_output(["xclip", "-o"]).strip(), "utf-8")

    if len(text) == 0:
        exit(0)

    try:
        lang_from = Detector(text).languages[0].code
    except Exception:
        exit(0)

    for _ in range(retry_times):
        bing = Bing(lang_from=lang_from, lang_to=lang_to)

        translation = bing.translate(text)
        if translation is not None:
            break

    if translation is None:
        translation = text

    translation = "\n".join(wrap(translation, max_width))

    show_time = min(max_time, max(min_time, len(translation) // words_per_sec)) * 1000
    x, y = PyMouse().position()
    show_tip(translation, x, y, show_time)
