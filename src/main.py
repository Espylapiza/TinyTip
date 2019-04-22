#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
from translators.Bing import Bing
from gui import show_tip
from pymouse import PyMouse
from textwrap import wrap


def translate(text):
    print(bing.get_translation(text))


if __name__ == "__main__":
    bing = Bing()
    retry_times = 3

    text = subprocess.check_output(["xclip", "-o"])
    text = text.strip()

    for _ in range(retry_times):
        translation = bing.translate(text)
        if translation is not None:
            break

    if translation is None:
        translation = str(text, "utf-8")

    translation = "\n".join(wrap(translation, 25))

    show_time = max(3, len(translation) // 6) * 1000
    x, y = PyMouse().position()
    show_tip(translation, x, y, show_time)
