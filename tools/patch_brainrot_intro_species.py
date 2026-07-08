#!/usr/bin/env python3
"""Use a Brainrot starter in the new game intro creature reveal."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "src/oak_speech.c"

text = PATH.read_text(encoding="utf-8")
old = "#define INTRO_SPECIES SPECIES_NIDORAN_F"
new = "#define INTRO_SPECIES SPECIES_SQUIRTLE"
if old not in text and new not in text:
    raise SystemExit("INTRO_SPECIES line not found")
text = text.replace(old, new)
PATH.write_text(text, encoding="utf-8")
print("Brainrot intro species set to TRALALERO/SQUIRTLE slot.")
