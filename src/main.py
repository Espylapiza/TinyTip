#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
from translation.bing import get_translation
from gui import show_tip
from pymouse import PyMouse

retry_times = 3


text = subprocess.check_output(["xclip", "-o"])
text = text.strip()


for _ in range(retry_times):
    text = get_translation(text)
    if text is not None:
        break

if text is not None:
    x, y = PyMouse().position()
    show_tip(text, x, y)
