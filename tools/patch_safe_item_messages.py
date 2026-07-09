#!/usr/bin/env python3
"""Avoid fragile item reward message scripts in playtest builds.

Some edited story scenes crashed after item reward messages returned from the
standard item receive script. For the playtest, keep item rewards simple:
add the item, show the message, play the fanfare, and return normally.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "asm" / "macros" / "event.inc"

SAFE_MACRO = '''\t@ Safer playtest version: adds item and prints the provided message without STD_RECEIVED_ITEM.
\t.macro giveitem_msg msg:req, item:req, amount=1, fanfare=MUS_OBTAIN_ITEM
\tadditem \\item, \\amount
\tplayfanfare \\fanfare
\tmessage \\msg
\twaitmessage
\twaitfanfare
\t.endm'''


ORIGINAL_PATTERN = r"\t@ Adds the specified item to the bag, then prints a message with fanfare\. See description of msgreceiveditem\.\n\t\.macro giveitem_msg msg:req, item:req, amount=1, fanfare=MUS_LEVEL_UP\n\tadditem \\item, \\amount\n\tmsgreceiveditem \\msg, \\item, \\amount, \\fanfare\n\t\.endm"


def main() -> None:
    text = PATH.read_text(encoding="utf-8")

    if "Safer playtest version" in text:
        print("Safe giveitem_msg macro already present.")
        return

    # IMPORTANT: use a function replacement so Python's regex engine does not
    # interpret assembler macro args like \item as regex replacement escapes.
    text, count = re.subn(ORIGINAL_PATTERN, lambda _match: SAFE_MACRO, text, count=1)

    if count != 1:
        print("warning: original giveitem_msg macro block not found; build will continue.")
        return

    PATH.write_text(text, encoding="utf-8")
    print("Safe giveitem_msg macro applied.")


if __name__ == "__main__":
    main()
