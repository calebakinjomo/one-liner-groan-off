"""Write one original one-line dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "I named our robot vacuum 'Dad' — now every time it bumps into a wall, "
    "the kids yell 'Dad's home!' and honestly, they're not wrong."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
