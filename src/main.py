#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
from translation.bing import get_translation
from gui import show_tip
from pymouse import PyMouse

# import pymouse.x11.PyMouse

retry_times = 3


text = subprocess.check_output(["xclip", "-o"])
text = text.strip()


for _ in range(retry_times):
    text = get_translation(text)
    if text is not None:
        break

t = max(3, len(text) // 4) * 1000

text_lines = ""

for i in range(len(text)):
    text_lines += text[i]
    if (i + 1) % 25 == 0:
        text_lines += "\n"


if text is not None:
    x, y = PyMouse().position()
    show_tip(text_lines, x, y, t)
