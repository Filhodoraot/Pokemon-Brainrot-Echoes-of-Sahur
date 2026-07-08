#!/usr/bin/env python3
"""Phase 1 type identity pass for Brainrot: Echoes of Sahur.

This keeps the normal FireRed type engine, but gives the early Brainrot
species explicit type identities instead of relying only on their original
Pokemon slots.

This patch is intentionally safe: if a species block or type line is not found,
it prints a warning and keeps building instead of breaking the playtest.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def p(path: str) -> Path:
    return ROOT / path


def read(path: str) -> str:
    return p(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    p(path).write_text(text, encoding="utf-8")


def find_species_block(text: str, species: str) -> tuple[int, int, str] | None:
    start = text.find(f"    [{species}] =")
    if start == -1:
        print(f"warning: species info not found, skipping {species}")
        return None
    end = text.find("    },", start)
    if end == -1:
        print(f"warning: species info end not found, skipping {species}")
        return None
    end += len("    },")
    return start, end, text[start:end]


def patch_types(block: str, type1: str, type2: str) -> str | None:
    # Keep the original indentation. Only replace the two type constants.
    pattern = r"(\.types\s*=\s*\{)\s*TYPE_[A-Z_]+\s*,\s*TYPE_[A-Z_]+\s*(\}\s*,?)"
    repl = rf"\g<1>{type1}, {type2}\2"
    patched, count = re.subn(pattern, repl, block, count=1)
    if count != 1:
        print("warning: type field not found in species block, skipping one entry")
        return None
    return patched


def main() -> None:
    path = "src/data/pokemon/species_info.h"
    text = read(path)

    type_map = {
        # Starters
        "SPECIES_BULBASAUR": ("TYPE_GRASS", "TYPE_FIGHTING"),      # CHIMPANZI
        "SPECIES_IVYSAUR": ("TYPE_GRASS", "TYPE_FIGHTING"),        # BANANINI
        "SPECIES_VENUSAUR": ("TYPE_GRASS", "TYPE_FIGHTING"),       # AVOCADOR
        "SPECIES_CHARMANDER": ("TYPE_FIRE", "TYPE_DARK"),          # CAPPUCINO
        "SPECIES_CHARMELEON": ("TYPE_FIRE", "TYPE_DARK"),          # HARPUCINO
        "SPECIES_CHARIZARD": ("TYPE_FIRE", "TYPE_DARK"),           # CAPASSINO
        "SPECIES_SQUIRTLE": ("TYPE_WATER", "TYPE_DARK"),           # TRALALERO
        "SPECIES_WARTORTLE": ("TYPE_WATER", "TYPE_DARK"),          # TRALALITO
        "SPECIES_BLASTOISE": ("TYPE_WATER", "TYPE_DARK"),          # TRALALORD

        # Test Zone 01
        "SPECIES_PIDGEY": ("TYPE_NORMAL", "TYPE_FLYING"),          # NOOBINI
        "SPECIES_PIDGEOTTO": ("TYPE_NORMAL", "TYPE_FLYING"),       # PIZZANINI
        "SPECIES_PIDGEOT": ("TYPE_NORMAL", "TYPE_FLYING"),         # LOSNOOBI
        "SPECIES_RATTATA": ("TYPE_NORMAL", "TYPE_GRASS"),          # PIPIKIWI
        "SPECIES_RATICATE": ("TYPE_NORMAL", "TYPE_GRASS"),         # PIPICORNI
        "SPECIES_SPEAROW": ("TYPE_NORMAL", "TYPE_NORMAL"),         # TIMCHEESE
        "SPECIES_FEAROW": ("TYPE_DARK", "TYPE_NORMAL"),            # RACCOONI

        # Zone Green 01
        "SPECIES_CATERPIE": ("TYPE_BUG", "TYPE_GRASS"),            # BAMBINI
        "SPECIES_METAPOD": ("TYPE_BUG", "TYPE_GRASS"),             # CROSTINI
        "SPECIES_BUTTERFREE": ("TYPE_BUG", "TYPE_GRASS"),          # BAMBILORD
        "SPECIES_WEEDLE": ("TYPE_BUG", "TYPE_POISON"),             # LIRILI
        "SPECIES_KAKUNA": ("TYPE_BUG", "TYPE_POISON"),             # LARILA
        "SPECIES_BEEDRILL": ("TYPE_BUG", "TYPE_POISON"),           # LIRILORD
        "SPECIES_PIKACHU": ("TYPE_ELECTRIC", "TYPE_GRASS"),        # BRRBRR
        "SPECIES_RAICHU": ("TYPE_ELECTRIC", "TYPE_GRASS"),         # PATAPIM

        # Cave/checkpoint
        "SPECIES_ZUBAT": ("TYPE_GHOST", "TYPE_FLYING"),            # TRIPPI
        "SPECIES_GOLBAT": ("TYPE_GHOST", "TYPE_FLYING"),           # TROPPILORD
        "SPECIES_GEODUDE": ("TYPE_ROCK", "TYPE_FIGHTING"),         # TUNGMINI
        "SPECIES_GRAVELER": ("TYPE_ROCK", "TYPE_FIGHTING"),        # TUNGMED
        "SPECIES_GOLEM": ("TYPE_ROCK", "TYPE_FIGHTING"),           # TUNGROCK
        "SPECIES_CLEFAIRY": ("TYPE_PSYCHIC", "TYPE_NORMAL"),       # MOONINI
        "SPECIES_CLEFABLE": ("TYPE_PSYCHIC", "TYPE_NORMAL"),       # MOONLORD
        "SPECIES_SNORLAX": ("TYPE_NORMAL", "TYPE_PSYCHIC"),        # SLEEPROT
    }

    patched_count = 0
    for species, (type1, type2) in type_map.items():
        found = find_species_block(text, species)
        if found is None:
            continue
        start, end, block = found
        patched = patch_types(block, type1, type2)
        if patched is None:
            continue
        text = text[:start] + patched + text[end:]
        patched_count += 1

    write(path, text)
    print(f"Brainrot phase 1 type identities applied: {patched_count} species patched.")


if __name__ == "__main__":
    main()
