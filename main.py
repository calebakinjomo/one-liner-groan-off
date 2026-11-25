"""One-liner groan-off entry: write one original dad joke to entry.txt.

Writes the single-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), creating the output directory if needed. The entry
text is fixed; this module performs no I/O besides that one write.
"""

import os

LINE = (
    "I named our robot vacuum 'Dad' — now every time it bumps into a wall, "
    "the kids yell 'Dad's home!' and honestly, they're not wrong."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

if not LINE.strip() or "\n" in LINE or "\r" in LINE:
    raise ValueError("entry must be a single non-empty line")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
