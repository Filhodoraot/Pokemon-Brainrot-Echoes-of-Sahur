#!/usr/bin/env python3
"""Guarantee the starter Brainrots begin in their first forms.

The starter choice must be:
- CHIMPANZI  -> BANANINI  -> AVOCADOR
- CAPPUCINO  -> HARPUCINO -> CAPASSINO
- TRALALERO  -> TRALALITO -> TRALALORD

This script is intentionally small and safe. It only patches the starter species
array, starter choice text, and the evolution links for those three lines.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_block(text: str, pattern: str, replacement: str, name: str) -> str:
    new_text, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"could not patch {name}")
    return new_text


def patch_starter_species_array() -> None:
    path = "src/field_specials.c"
    text = read(path)
    replacement = """static const u16 sStarterSpecies[] = {
    SPECIES_BULBASAUR,   // CHIMPANZI, first form
    SPECIES_SQUIRTLE,   // TRALALERO, first form
    SPECIES_CHARMANDER  // CAPPUCINO, first form
};"""
    text = replace_block(
        text,
        r"static const u16 sStarterSpecies\[\] = \{.*?\};",
        replacement,
        "starter species array",
    )
    write(path, text)


def patch_evolution_line(text: str, species: str, line: str) -> str:
    pattern = rf"^\s*\[{re.escape(species)}\]\s*=\s*.*,$"
    new_text, count = re.subn(pattern, line, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"could not patch evolution for {species}")
    return new_text


def patch_starter_evolutions() -> None:
    path = "src/data/pokemon/evolution.h"
    text = read(path)
    lines = {
        "SPECIES_BULBASAUR": "    [SPECIES_BULBASAUR] = {{EVO_LEVEL, 16, SPECIES_IVYSAUR}},",
        "SPECIES_IVYSAUR": "    [SPECIES_IVYSAUR] = {{EVO_LEVEL, 32, SPECIES_VENUSAUR}},",
        "SPECIES_CHARMANDER": "    [SPECIES_CHARMANDER] = {{EVO_LEVEL, 16, SPECIES_CHARMELEON}},",
        "SPECIES_CHARMELEON": "    [SPECIES_CHARMELEON] = {{EVO_LEVEL, 32, SPECIES_CHARIZARD}},",
        "SPECIES_SQUIRTLE": "    [SPECIES_SQUIRTLE] = {{EVO_LEVEL, 16, SPECIES_WARTORTLE}},",
        "SPECIES_WARTORTLE": "    [SPECIES_WARTORTLE] = {{EVO_LEVEL, 32, SPECIES_BLASTOISE}},",
    }
    for species, line in lines.items():
        text = patch_evolution_line(text, species, line)
    write(path, text)


def patch_lab_text() -> None:
    path = "data/maps/PalletTown_ProfessorOaksLab/text.inc"
    text = read(path)

    replacements = {
        "PalletTown_ProfessorOaksLab_Text_OakChoosingCharmander": '''PalletTown_ProfessorOaksLab_Text_OakChoosingCharmander::
    .string "Ah! CAPPUCINO is your choice.\n"
    .string "This is its first form.\p"
    .string "It evolves into HARPUCINO\n"
    .string "and then CAPASSINO.\p"
    .string "So, {PLAYER}, you choose\n"
    .string "the FIRE BRAINROT CAPPUCINO?$"''',
        "PalletTown_ProfessorOaksLab_Text_OakChoosingSquirtle": '''PalletTown_ProfessorOaksLab_Text_OakChoosingSquirtle::
    .string "Hm! TRALALERO is your choice.\n"
    .string "This is its first form.\p"
    .string "It evolves into TRALALITO\n"
    .string "and then TRALALORD.\p"
    .string "So, {PLAYER}, you choose\n"
    .string "the WATER BRAINROT TRALALERO?$"''',
        "PalletTown_ProfessorOaksLab_Text_OakChoosingBulbasaur": '''PalletTown_ProfessorOaksLab_Text_OakChoosingBulbasaur::
    .string "I see! CHIMPANZI is your choice.\n"
    .string "This is its first form.\p"
    .string "It evolves into BANANINI\n"
    .string "and then AVOCADOR.\p"
    .string "So, {PLAYER}, you choose\n"
    .string "the GRASS BRAINROT CHIMPANZI?$"''',
    }

    for label, block in replacements.items():
        start = text.find(f"{label}::")
        if start == -1:
            raise RuntimeError(f"could not find lab text label {label}")
        end = text.find("\n\n", start)
        if end == -1:
            end = len(text)
        text = text[:start] + block + text[end:]

    write(path, text)


def main() -> None:
    patch_starter_species_array()
    patch_starter_evolutions()
    patch_lab_text()
    print("Starter Brainrots locked to first forms with normal evolution lines.")


if __name__ == "__main__":
    main()
