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


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    pattern = r"\t@ Adds the specified item to the bag, then prints a message with fanfare\. See description of msgreceiveditem\.\n\t\.macro giveitem_msg msg:req, item:req, amount=1, fanfare=MUS_LEVEL_UP\n\tadditem \\item, \\amount\n\tmsgreceiveditem \\msg, \\item, \\amount, \\fanfare\n\t\.endm"
    text, count = re.subn(pattern, SAFE_MACRO, text, count=1)
    if count != 1:
        # Already patched or macro text drifted. Keep build alive but warn loudly.
        if "Safer playtest version" in text:
            print("Safe giveitem_msg macro already present.")
            return
        raise RuntimeError("giveitem_msg macro block not found")
    PATH.write_text(text, encoding="utf-8")
    print("Safe giveitem_msg macro applied.")


if __name__ == "__main__":
    main()
