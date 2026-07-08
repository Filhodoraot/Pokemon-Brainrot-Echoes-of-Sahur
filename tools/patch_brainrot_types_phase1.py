#!/usr/bin/env python3
"""Phase 1 type identity pass for Brainrot: Echoes of Sahur.

This keeps the normal FireRed type engine, but gives the early Brainrot
species explicit type identities instead of relying only on their original
Pokemon slots.

Adding brand-new type slots is much riskier because it touches the battle UI,
type chart, move data, text graphics, and save-facing data. For the playable
build, we reuse the existing type chart and make each Brainrot feel correct
through type combinations.
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


def find_species_block(text: str, species: str) -> tuple[int, int, str]:
    start = text.find(f"    [{species}] =")
    if start == -1:
        raise RuntimeError(f"species info not found: {species}")
    end = text.find("    },", start)
    if end == -1:
        raise RuntimeError(f"species info end not found: {species}")
    end += len("    },")
    return start, end, text[start:end]


def patch_types(block: str, type1: str, type2: str) -> str:
    new_line = f".types = {{{type1}, {type2}}}"
    block, count = re.subn(r"\.types\s*=\s*\{TYPE_[A-Z_]+,\s*TYPE_[A-Z_]+\}", new_line, block, count=1)
    if count != 1:
        raise RuntimeError("type field not found in species block")
    return block


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

    for species, (type1, type2) in type_map.items():
        start, end, block = find_species_block(text, species)
        text = text[:start] + patch_types(block, type1, type2) + text[end:]

    write(path, text)
    print("Brainrot phase 1 type identities applied.")


if __name__ == "__main__":
    main()
