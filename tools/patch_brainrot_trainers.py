#!/usr/bin/env python3
"""Patch early trainer parties for the Brainrot test build.

Run after apply_brainrot_test_build.py and before make.
This keeps the original trainer scripts/maps, but swaps their teams to early Brainrot species.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "src/data/trainer_parties.h"


def mon(level: int, species: str, iv: int = 0) -> str:
    return f"""    {{
        .iv = {iv},
        .lvl = {level},
        .species = {species},
    }}"""


def party_default(name: str, mons: list[str]) -> str:
    body = ",\n".join(mons)
    return f"""static const struct TrainerMonNoItemDefaultMoves {name}[] = {{
{body},
}};"""


def party_custom(name: str, entries: list[tuple[int, str, str]], iv: int = 0) -> str:
    mons = []
    for level, species, moves in entries:
        mons.append(f"""    {{
        .iv = {iv},
        .lvl = {level},
        .species = {species},
        .moves = {{{moves}}},
    }}""")
    body = ",\n".join(mons)
    return f"""static const struct TrainerMonNoItemCustomMoves {name}[] = {{
{body},
}};"""


def replace_party(text: str, name: str, new_block: str) -> str:
    marker = f" {name}[] = {{"
    marker_pos = text.find(marker)
    if marker_pos == -1:
        raise RuntimeError(f"party not found: {name}")

    start = text.rfind("static const struct TrainerMon", 0, marker_pos)
    if start == -1:
        raise RuntimeError(f"party start not found: {name}")

    end = text.find("\n};", marker_pos)
    if end == -1:
        raise RuntimeError(f"party end not found: {name}")
    end += len("\n};")

    return text[:start] + new_block + text[end:]


def main() -> None:
    text = PATH.read_text(encoding="utf-8")

    default_parties = {
        # Route 3 candidates
        "sParty_YoungsterBen": [(9, "SPECIES_RATTATA"), (9, "SPECIES_PIDGEY")],
        "sParty_YoungsterCalvin": [(10, "SPECIES_SPEAROW")],
        "sParty_LassJanice": [(8, "SPECIES_PIDGEY"), (8, "SPECIES_RATTATA")],
        "sParty_LassSally": [(9, "SPECIES_RATTATA"), (9, "SPECIES_PIDGEY")],
        "sParty_BugCatcherColton": [(9, "SPECIES_CATERPIE"), (9, "SPECIES_WEEDLE"), (9, "SPECIES_PIDGEY")],
        "sParty_BugCatcherGreg": [(8, "SPECIES_WEEDLE"), (8, "SPECIES_KAKUNA"), (8, "SPECIES_CATERPIE")],
        "sParty_BugCatcherJames": [(10, "SPECIES_CATERPIE"), (10, "SPECIES_METAPOD")],
        "sParty_LassRobin": [(11, "SPECIES_PIKACHU")],

        # Zone Green 01 trainers
        "sParty_BugCatcherRick": [(6, "SPECIES_WEEDLE"), (6, "SPECIES_CATERPIE")],
        "sParty_BugCatcherDoug": [(7, "SPECIES_WEEDLE"), (7, "SPECIES_KAKUNA"), (7, "SPECIES_CATERPIE")],
        "sParty_BugCatcherSammy": [(9, "SPECIES_WEEDLE")],

        # Moon Noise Cave first floor
        "sParty_YoungsterJosh": [(10, "SPECIES_RATTATA"), (10, "SPECIES_RATTATA"), (10, "SPECIES_ZUBAT")],
        "sParty_LassMiriam": [(11, "SPECIES_CATERPIE"), (11, "SPECIES_WEEDLE")],
        "sParty_LassIris": [(14, "SPECIES_CLEFAIRY")],
        "sParty_HikerMarcos": [(10, "SPECIES_GEODUDE"), (10, "SPECIES_GEODUDE"), (10, "SPECIES_ONIX")],
        "sParty_SuperNerdJovan": [(11, "SPECIES_PIKACHU"), (11, "SPECIES_VOLTORB")],
        "sParty_BugCatcherKent": [(11, "SPECIES_WEEDLE"), (11, "SPECIES_KAKUNA")],
        "sParty_BugCatcherRobby": [(10, "SPECIES_CATERPIE"), (10, "SPECIES_METAPOD"), (10, "SPECIES_CATERPIE")],

        # Route 4 / License C bridge early flow
        "sParty_LassCrissy": [(12, "SPECIES_PARAS"), (12, "SPECIES_CATERPIE"), (13, "SPECIES_PARASECT")],
        "sParty_BugCatcherCale": [(10, "SPECIES_CATERPIE"), (10, "SPECIES_WEEDLE"), (10, "SPECIES_METAPOD"), (10, "SPECIES_KAKUNA")],
        "sParty_LassAli": [(12, "SPECIES_PIDGEY"), (12, "SPECIES_CATERPIE"), (12, "SPECIES_WEEDLE")],
        "sParty_YoungsterTimmy": [(14, "SPECIES_RATTATA"), (14, "SPECIES_SPEAROW")],
        "sParty_LassReli": [(16, "SPECIES_PIDGEY"), (16, "SPECIES_RATTATA")],
        "sParty_CamperEthan": [(18, "SPECIES_SPEAROW")],
        "sParty_CamperShane": [(14, "SPECIES_RATTATA"), (14, "SPECIES_PIDGEY")],
    }

    custom_parties = {
        # License D Exam Hall. Brock/Liam still use stone-style Brainrots.
        "sParty_CamperLiam": [
            (10, "SPECIES_GEODUDE", "MOVE_TACKLE, MOVE_DEFENSE_CURL, MOVE_NONE, MOVE_NONE"),
            (11, "SPECIES_SANDSHREW", "MOVE_SCRATCH, MOVE_DEFENSE_CURL, MOVE_SAND_ATTACK, MOVE_NONE"),
        ],
        "sParty_SuperNerdMiguel": [
            (12, "SPECIES_GRIMER", "MOVE_POUND, MOVE_DISABLE, MOVE_NONE, MOVE_NONE"),
            (12, "SPECIES_VOLTORB", "MOVE_TACKLE, MOVE_SCREECH, MOVE_NONE, MOVE_NONE"),
            (12, "SPECIES_KOFFING", "MOVE_TACKLE, MOVE_SMOG, MOVE_NONE, MOVE_NONE"),
        ],
    }

    for name, mons in default_parties.items():
        text = replace_party(text, name, party_default(name, [mon(level, species) for level, species in mons]))

    for name, entries in custom_parties.items():
        text = replace_party(text, name, party_custom(name, entries))

    PATH.write_text(text, encoding="utf-8")
    print("Brainrot early trainer parties patched.")


if __name__ == "__main__":
    main()
