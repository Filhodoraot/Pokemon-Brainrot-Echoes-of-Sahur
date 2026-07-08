#!/usr/bin/env python3
"""Replace remaining vanilla Pokemon in trainer parties and wild encounters.

This playtest only has a first Brainrot roster implemented, so every normal
Pokemon species in common gameplay data is remapped into one of the available
Brainrot slots. The mapping is deterministic and level-aware so early routes do
not suddenly spawn final forms.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BRAINROT_SPECIES = {
    "SPECIES_BULBASAUR", "SPECIES_IVYSAUR", "SPECIES_VENUSAUR",
    "SPECIES_CHARMANDER", "SPECIES_CHARMELEON", "SPECIES_CHARIZARD",
    "SPECIES_SQUIRTLE", "SPECIES_WARTORTLE", "SPECIES_BLASTOISE",
    "SPECIES_PIDGEY", "SPECIES_PIDGEOTTO", "SPECIES_PIDGEOT",
    "SPECIES_RATTATA", "SPECIES_RATICATE",
    "SPECIES_SPEAROW", "SPECIES_FEAROW",
    "SPECIES_CATERPIE", "SPECIES_METAPOD", "SPECIES_BUTTERFREE",
    "SPECIES_WEEDLE", "SPECIES_KAKUNA", "SPECIES_BEEDRILL",
    "SPECIES_PIKACHU", "SPECIES_RAICHU",
    "SPECIES_ZUBAT", "SPECIES_GOLBAT",
    "SPECIES_GEODUDE", "SPECIES_GRAVELER", "SPECIES_GOLEM",
    "SPECIES_CLEFAIRY", "SPECIES_CLEFABLE",
    "SPECIES_SNORLAX",
}

NEVER_REPLACE = {
    "SPECIES_NONE",
    "SPECIES_EGG",
    "SPECIES_UNOWN",  # puzzle/form systems can depend on it; keep until we make a 67/echo replacement safely.
}

LEVEL_POOLS = [
    (4, ["SPECIES_PIDGEY", "SPECIES_RATTATA", "SPECIES_CATERPIE", "SPECIES_WEEDLE"]),
    (8, ["SPECIES_PIDGEY", "SPECIES_RATTATA", "SPECIES_CATERPIE", "SPECIES_WEEDLE", "SPECIES_SPEAROW", "SPECIES_PIKACHU"]),
    (12, ["SPECIES_PIDGEY", "SPECIES_RATTATA", "SPECIES_SPEAROW", "SPECIES_CATERPIE", "SPECIES_WEEDLE", "SPECIES_ZUBAT", "SPECIES_GEODUDE", "SPECIES_CLEFAIRY"]),
    (18, ["SPECIES_PIDGEOTTO", "SPECIES_RATICATE", "SPECIES_SPEAROW", "SPECIES_FEAROW", "SPECIES_METAPOD", "SPECIES_KAKUNA", "SPECIES_PIKACHU", "SPECIES_ZUBAT", "SPECIES_GEODUDE"]),
    (31, ["SPECIES_PIDGEOTTO", "SPECIES_RATICATE", "SPECIES_FEAROW", "SPECIES_BUTTERFREE", "SPECIES_BEEDRILL", "SPECIES_RAICHU", "SPECIES_GOLBAT", "SPECIES_GRAVELER", "SPECIES_CLEFAIRY", "SPECIES_CHARMELEON", "SPECIES_IVYSAUR", "SPECIES_WARTORTLE"]),
    (999, ["SPECIES_PIDGEOT", "SPECIES_RATICATE", "SPECIES_FEAROW", "SPECIES_BUTTERFREE", "SPECIES_BEEDRILL", "SPECIES_RAICHU", "SPECIES_GOLBAT", "SPECIES_GOLEM", "SPECIES_CLEFABLE", "SPECIES_SNORLAX", "SPECIES_CHARIZARD", "SPECIES_VENUSAUR", "SPECIES_BLASTOISE"]),
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def stable_index(seed: str, size: int) -> int:
    value = 0
    for ch in seed:
        value = (value * 131 + ord(ch)) & 0xFFFFFFFF
    return value % size


def choose_brainrot(original: str, level: int, salt: str) -> str:
    if original in NEVER_REPLACE or original in BRAINROT_SPECIES:
        return original
    for max_level, pool in LEVEL_POOLS:
        if level <= max_level:
            return pool[stable_index(f"{original}:{level}:{salt}", len(pool))]
    return "SPECIES_RATTATA"


def patch_trainer_parties() -> None:
    path = "src/data/trainer_parties.h"
    text = read(path)
    out: list[str] = []
    current_level = 5
    changed = 0

    for line_no, line in enumerate(text.splitlines(), start=1):
        lvl_match = re.search(r"\.lvl\s*=\s*(\d+)", line)
        if lvl_match:
            current_level = int(lvl_match.group(1))

        species_match = re.search(r"(\.species\s*=\s*)(SPECIES_[A-Z0-9_]+)(\s*,)", line)
        if species_match:
            original = species_match.group(2)
            replacement = choose_brainrot(original, current_level, str(line_no))
            if replacement != original:
                line = line[:species_match.start(2)] + replacement + line[species_match.end(2):]
                changed += 1
        out.append(line)

    write(path, "\n".join(out) + "\n")
    print(f"Trainer party vanilla species replaced: {changed}")


def patch_wild_encounters() -> None:
    path = "src/data/wild_encounters.json"
    data = json.loads(read(path))
    changed = 0

    for group_index, group in enumerate(data.get("wild_encounter_groups", [])):
        for enc_index, encounter in enumerate(group.get("encounters", [])):
            for section_name in ("land_mons", "water_mons", "rock_smash_mons", "fishing_mons"):
                section = encounter.get(section_name)
                if not section:
                    continue
                for mon_index, mon in enumerate(section.get("mons", [])):
                    original = mon.get("species")
                    if not isinstance(original, str):
                        continue
                    level = int(mon.get("max_level", mon.get("min_level", 5)))
                    replacement = choose_brainrot(original, level, f"{group_index}:{enc_index}:{section_name}:{mon_index}")
                    if replacement != original:
                        mon["species"] = replacement
                        changed += 1

    write(path, json.dumps(data, indent=2) + "\n")
    print(f"Wild encounter vanilla species replaced: {changed}")


def main() -> None:
    patch_trainer_parties()
    patch_wild_encounters()
    print("Vanilla Pokemon replacement pass complete.")


if __name__ == "__main__":
    main()
