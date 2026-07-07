#!/usr/bin/env python3
"""
Brainrot gameplay systems patcher.

Run from repo root before building:

    python3 tools/apply_brainrot_systems.py
    make

This applies first playable Brainrot systems directly to source files:

- species battle names
- early evolution lines
- starter/early stats
- early learnsets
- Route 1 and Zone Green 01 wild encounters

Sprites are intentionally not changed here.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Could not find block for {label}")
    return text.replace(old, new, 1)


def patch_species_names() -> None:
    path = "src/data/text/species_names.h"
    text = read(path)

    replacements = {
        # Starters
        '    [SPECIES_BULBASAUR] = _("BULBASAUR"),': '    [SPECIES_BULBASAUR] = _("CHIMPANZI"),',
        '    [SPECIES_IVYSAUR] = _("IVYSAUR"),': '    [SPECIES_IVYSAUR] = _("BANANINI"),',
        '    [SPECIES_VENUSAUR] = _("VENUSAUR"),': '    [SPECIES_VENUSAUR] = _("AVOCADOR"),',
        '    [SPECIES_CHARMANDER] = _("CHARMANDER"),': '    [SPECIES_CHARMANDER] = _("CAPPUCINO"),',
        '    [SPECIES_CHARMELEON] = _("CHARMELEON"),': '    [SPECIES_CHARMELEON] = _("HARPUCINO"),',
        '    [SPECIES_CHARIZARD] = _("CHARIZARD"),': '    [SPECIES_CHARIZARD] = _("CAPASSINO"),',
        '    [SPECIES_SQUIRTLE] = _("SQUIRTLE"),': '    [SPECIES_SQUIRTLE] = _("TRALALERO"),',
        '    [SPECIES_WARTORTLE] = _("WARTORTLE"),': '    [SPECIES_WARTORTLE] = _("TRALALITO"),',
        '    [SPECIES_BLASTOISE] = _("BLASTOISE"),': '    [SPECIES_BLASTOISE] = _("TRALALORD"),',

        # Zone Green 01
        '    [SPECIES_CATERPIE] = _("CATERPIE"),': '    [SPECIES_CATERPIE] = _("BAMBINI"),',
        '    [SPECIES_METAPOD] = _("METAPOD"),': '    [SPECIES_METAPOD] = _("CROSTINI"),',
        '    [SPECIES_BUTTERFREE] = _("BUTTERFREE"),': '    [SPECIES_BUTTERFREE] = _("BAMBILORD"),',
        '    [SPECIES_WEEDLE] = _("WEEDLE"),': '    [SPECIES_WEEDLE] = _("LIRILI"),',
        '    [SPECIES_KAKUNA] = _("KAKUNA"),': '    [SPECIES_KAKUNA] = _("LARILA"),',
        '    [SPECIES_BEEDRILL] = _("BEEDRILL"),': '    [SPECIES_BEEDRILL] = _("LIRILORD"),',
        '    [SPECIES_PIKACHU] = _("PIKACHU"),': '    [SPECIES_PIKACHU] = _("BRRBRR"),',
        '    [SPECIES_RAICHU] = _("RAICHU"),': '    [SPECIES_RAICHU] = _("PATAPIM"),',

        # Test Zone 01
        '    [SPECIES_PIDGEY] = _("PIDGEY"),': '    [SPECIES_PIDGEY] = _("NOOBINI"),',
        '    [SPECIES_PIDGEOTTO] = _("PIDGEOTTO"),': '    [SPECIES_PIDGEOTTO] = _("PIZZANINI"),',
        '    [SPECIES_PIDGEOT] = _("PIDGEOT"),': '    [SPECIES_PIDGEOT] = _("LOSNOOBI"),',
        '    [SPECIES_RATTATA] = _("RATTATA"),': '    [SPECIES_RATTATA] = _("PIPIKIWI"),',
        '    [SPECIES_RATICATE] = _("RATICATE"),': '    [SPECIES_RATICATE] = _("PIPICORNI"),',
        '    [SPECIES_SPEAROW] = _("SPEAROW"),': '    [SPECIES_SPEAROW] = _("TIMCHEESE"),',
        '    [SPECIES_FEAROW] = _("FEAROW"),': '    [SPECIES_FEAROW] = _("RACCOONI"),',

        # Early cave/stone placeholders
        '    [SPECIES_ZUBAT] = _("ZUBAT"),': '    [SPECIES_ZUBAT] = _("TRIPPI"),',
        '    [SPECIES_GOLBAT] = _("GOLBAT"),': '    [SPECIES_GOLBAT] = _("TROPPILORD"),',
        '    [SPECIES_GEODUDE] = _("GEODUDE"),': '    [SPECIES_GEODUDE] = _("TUNGMINI"),',
        '    [SPECIES_GRAVELER] = _("GRAVELER"),': '    [SPECIES_GRAVELER] = _("TUNGMED"),',
        '    [SPECIES_GOLEM] = _("GOLEM"),': '    [SPECIES_GOLEM] = _("TUNGROCK"),',
        '    [SPECIES_CLEFAIRY] = _("CLEFAIRY"),': '    [SPECIES_CLEFAIRY] = _("MOONINI"),',
        '    [SPECIES_CLEFABLE] = _("CLEFABLE"),': '    [SPECIES_CLEFABLE] = _("MOONLORD"),',
    }

    for old, new in replacements.items():
        text = replace_exact(text, old, new, old)

    write(path, text)


def patch_evolutions() -> None:
    path = "src/data/pokemon/evolution.h"
    text = read(path)

    replacements = {
        '    [SPECIES_CATERPIE] = {{EVO_LEVEL, 7, SPECIES_METAPOD}},': '    [SPECIES_CATERPIE] = {{EVO_LEVEL, 7, SPECIES_METAPOD}},',
        '    [SPECIES_METAPOD] = {{EVO_LEVEL, 10, SPECIES_BUTTERFREE}},': '    [SPECIES_METAPOD] = {{EVO_LEVEL, 12, SPECIES_BUTTERFREE}},',
        '    [SPECIES_WEEDLE] = {{EVO_LEVEL, 7, SPECIES_KAKUNA}},': '    [SPECIES_WEEDLE] = {{EVO_LEVEL, 7, SPECIES_KAKUNA}},',
        '    [SPECIES_KAKUNA] = {{EVO_LEVEL, 10, SPECIES_BEEDRILL}},': '    [SPECIES_KAKUNA] = {{EVO_LEVEL, 12, SPECIES_BEEDRILL}},',
        '    [SPECIES_PIDGEY] = {{EVO_LEVEL, 18, SPECIES_PIDGEOTTO}},': '    [SPECIES_PIDGEY] = {{EVO_LEVEL, 16, SPECIES_PIDGEOTTO}},',
        '    [SPECIES_PIDGEOTTO] = {{EVO_LEVEL, 36, SPECIES_PIDGEOT}},': '    [SPECIES_PIDGEOTTO] = {{EVO_LEVEL, 32, SPECIES_PIDGEOT}},',
        '    [SPECIES_RATTATA] = {{EVO_LEVEL, 20, SPECIES_RATICATE}},': '    [SPECIES_RATTATA] = {{EVO_LEVEL, 18, SPECIES_RATICATE}},',
        '    [SPECIES_SPEAROW] = {{EVO_LEVEL, 20, SPECIES_FEAROW}},': '    [SPECIES_SPEAROW] = {},',
    }

    for old, new in replacements.items():
        text = replace_exact(text, old, new, old)

    write(path, text)


def patch_learnsets() -> None:
    path = "src/data/pokemon/level_up_learnsets.h"
    text = read(path)

    blocks = {
        "sCaterpieLevelUpLearnset": '''static const u16 sCaterpieLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_STRING_SHOT),
    LEVEL_UP_MOVE(5, MOVE_STUN_SPORE),
    LEVEL_UP_END
};''',
        "sMetapodLevelUpLearnset": '''static const u16 sMetapodLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_HARDEN),
    LEVEL_UP_MOVE(1, MOVE_STRING_SHOT),
    LEVEL_UP_MOVE(7, MOVE_HARDEN),
    LEVEL_UP_MOVE(10, MOVE_STUN_SPORE),
    LEVEL_UP_END
};''',
        "sButterfreeLevelUpLearnset": '''static const u16 sButterfreeLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_CONFUSION),
    LEVEL_UP_MOVE(1, MOVE_GUST),
    LEVEL_UP_MOVE(10, MOVE_CONFUSION),
    LEVEL_UP_MOVE(13, MOVE_POISON_POWDER),
    LEVEL_UP_MOVE(14, MOVE_STUN_SPORE),
    LEVEL_UP_MOVE(15, MOVE_SLEEP_POWDER),
    LEVEL_UP_MOVE(18, MOVE_SUPERSONIC),
    LEVEL_UP_MOVE(23, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(28, MOVE_GUST),
    LEVEL_UP_MOVE(34, MOVE_PSYBEAM),
    LEVEL_UP_MOVE(40, MOVE_SAFEGUARD),
    LEVEL_UP_MOVE(47, MOVE_SILVER_WIND),
    LEVEL_UP_END
};''',
        "sWeedleLevelUpLearnset": '''static const u16 sWeedleLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_POISON_STING),
    LEVEL_UP_MOVE(1, MOVE_STRING_SHOT),
    LEVEL_UP_MOVE(6, MOVE_FURY_ATTACK),
    LEVEL_UP_END
};''',
        "sKakunaLevelUpLearnset": '''static const u16 sKakunaLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_HARDEN),
    LEVEL_UP_MOVE(1, MOVE_POISON_STING),
    LEVEL_UP_MOVE(7, MOVE_HARDEN),
    LEVEL_UP_MOVE(10, MOVE_FURY_ATTACK),
    LEVEL_UP_END
};''',
        "sBeedrillLevelUpLearnset": '''static const u16 sBeedrillLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(1, MOVE_POISON_STING),
    LEVEL_UP_MOVE(10, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(15, MOVE_FOCUS_ENERGY),
    LEVEL_UP_MOVE(20, MOVE_TWINEEDLE),
    LEVEL_UP_MOVE(25, MOVE_RAGE),
    LEVEL_UP_MOVE(30, MOVE_PURSUIT),
    LEVEL_UP_MOVE(35, MOVE_PIN_MISSILE),
    LEVEL_UP_MOVE(40, MOVE_AGILITY),
    LEVEL_UP_MOVE(45, MOVE_ENDEAVOR),
    LEVEL_UP_END
};''',
        "sPikachuLevelUpLearnset": '''static const u16 sPikachuLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_THUNDER_SHOCK),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(6, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(8, MOVE_THUNDER_WAVE),
    LEVEL_UP_MOVE(11, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(15, MOVE_DOUBLE_TEAM),
    LEVEL_UP_MOVE(20, MOVE_SLAM),
    LEVEL_UP_MOVE(26, MOVE_THUNDERBOLT),
    LEVEL_UP_MOVE(33, MOVE_AGILITY),
    LEVEL_UP_MOVE(41, MOVE_THUNDER),
    LEVEL_UP_MOVE(50, MOVE_LIGHT_SCREEN),
    LEVEL_UP_END
};''',
        "sRaichuLevelUpLearnset": '''static const u16 sRaichuLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_THUNDER_SHOCK),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(1, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(1, MOVE_THUNDERBOLT),
    LEVEL_UP_MOVE(1, MOVE_THUNDER_WAVE),
    LEVEL_UP_MOVE(1, MOVE_DOUBLE_TEAM),
    LEVEL_UP_END
};''',
        "sPidgeyLevelUpLearnset": '''static const u16 sPidgeyLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(5, MOVE_SAND_ATTACK),
    LEVEL_UP_MOVE(9, MOVE_GUST),
    LEVEL_UP_MOVE(13, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(17, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(21, MOVE_WING_ATTACK),
    LEVEL_UP_MOVE(29, MOVE_AGILITY),
    LEVEL_UP_MOVE(37, MOVE_MIRROR_MOVE),
    LEVEL_UP_END
};''',
        "sRattataLevelUpLearnset": '''static const u16 sRattataLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(7, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(13, MOVE_FOCUS_ENERGY),
    LEVEL_UP_MOVE(20, MOVE_HYPER_FANG),
    LEVEL_UP_MOVE(27, MOVE_PURSUIT),
    LEVEL_UP_MOVE(34, MOVE_SUPER_FANG),
    LEVEL_UP_MOVE(41, MOVE_ENDEAVOR),
    LEVEL_UP_END
};''',
        "sSpearowLevelUpLearnset": '''static const u16 sSpearowLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_PECK),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(7, MOVE_LEER),
    LEVEL_UP_MOVE(13, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(19, MOVE_PURSUIT),
    LEVEL_UP_MOVE(25, MOVE_AERIAL_ACE),
    LEVEL_UP_MOVE(31, MOVE_AGILITY),
    LEVEL_UP_MOVE(37, MOVE_DRILL_PECK),
    LEVEL_UP_END
};''',
        "sFearowLevelUpLearnset": '''static const u16 sFearowLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_PECK),
    LEVEL_UP_MOVE(1, MOVE_LEER),
    LEVEL_UP_MOVE(1, MOVE_PURSUIT),
    LEVEL_UP_MOVE(7, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(13, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(26, MOVE_AERIAL_ACE),
    LEVEL_UP_MOVE(32, MOVE_AGILITY),
    LEVEL_UP_MOVE(40, MOVE_DRILL_PECK),
    LEVEL_UP_END
};''',
    }

    for name, new_block in blocks.items():
        start = text.find(f"static const u16 {name}[] = {{")
        if start == -1:
            raise RuntimeError(f"Could not find learnset {name}")
        end = text.find("};", start)
        if end == -1:
            raise RuntimeError(f"Could not find end of learnset {name}")
        end += 2
        text = text[:start] + new_block + text[end:]

    write(path, text)


def patch_wild_encounters() -> None:
    path = "src/data/wild_encounters.json"
    data = json.loads(read(path))

    route1_mons = [
        {"min_level": 2, "max_level": 2, "species": "SPECIES_PIDGEY"},
        {"min_level": 2, "max_level": 2, "species": "SPECIES_RATTATA"},
        {"min_level": 3, "max_level": 3, "species": "SPECIES_PIDGEY"},
        {"min_level": 3, "max_level": 3, "species": "SPECIES_RATTATA"},
        {"min_level": 3, "max_level": 3, "species": "SPECIES_PIDGEY"},
        {"min_level": 3, "max_level": 3, "species": "SPECIES_RATTATA"},
        {"min_level": 4, "max_level": 4, "species": "SPECIES_PIDGEY"},
        {"min_level": 4, "max_level": 4, "species": "SPECIES_RATTATA"},
        {"min_level": 4, "max_level": 4, "species": "SPECIES_SPEAROW"},
        {"min_level": 5, "max_level": 5, "species": "SPECIES_SPEAROW"},
        {"min_level": 5, "max_level": 5, "species": "SPECIES_FEAROW"},
        {"min_level": 5, "max_level": 5, "species": "SPECIES_RATTATA"},
    ]

    forest_mons = [
        {"min_level": 3, "max_level": 3, "species": "SPECIES_CATERPIE"},
        {"min_level": 3, "max_level": 3, "species": "SPECIES_WEEDLE"},
        {"min_level": 4, "max_level": 4, "species": "SPECIES_CATERPIE"},
        {"min_level": 4, "max_level": 4, "species": "SPECIES_WEEDLE"},
        {"min_level": 5, "max_level": 5, "species": "SPECIES_CATERPIE"},
        {"min_level": 5, "max_level": 5, "species": "SPECIES_WEEDLE"},
        {"min_level": 5, "max_level": 5, "species": "SPECIES_METAPOD"},
        {"min_level": 5, "max_level": 5, "species": "SPECIES_KAKUNA"},
        {"min_level": 6, "max_level": 6, "species": "SPECIES_METAPOD"},
        {"min_level": 6, "max_level": 6, "species": "SPECIES_KAKUNA"},
        {"min_level": 4, "max_level": 4, "species": "SPECIES_PIKACHU"},
        {"min_level": 6, "max_level": 6, "species": "SPECIES_PIKACHU"},
    ]

    patched_route1 = False
    patched_forest = False

    for group in data.get("wild_encounter_groups", []):
        for encounter in group.get("encounters", []):
            if encounter.get("map") == "MAP_ROUTE1" and encounter.get("base_label") == "sRoute1_FireRed":
                encounter["land_mons"]["mons"] = route1_mons
                patched_route1 = True
            if encounter.get("map") == "MAP_VIRIDIAN_FOREST" and encounter.get("base_label") == "sViridianForest_FireRed":
                encounter["land_mons"]["mons"] = forest_mons
                patched_forest = True

    if not patched_route1:
        raise RuntimeError("Could not patch Route 1 encounters")
    if not patched_forest:
        raise RuntimeError("Could not patch Viridian Forest encounters")

    write(path, json.dumps(data, indent=2) + "\n")


def patch_species_stats() -> None:
    path = "src/data/pokemon/species_info.h"
    text = read(path)

    # Conservative first-build stat pass.
    # This keeps the original structure intact and only changes obvious starter/early values.
    replacements = {
        # Bulbasaur line -> Chimpanzini line: tanky physical grass/brute feel.
        ".baseHP        = 45,\n        .baseAttack    = 49,\n        .baseDefense   = 49,\n        .baseSpeed     = 45,\n        .baseSpAttack  = 65,\n        .baseSpDefense = 65,": ".baseHP        = 48,\n        .baseAttack    = 65,\n        .baseDefense   = 55,\n        .baseSpeed     = 42,\n        .baseSpAttack  = 45,\n        .baseSpDefense = 50,",
        ".baseHP        = 60,\n        .baseAttack    = 62,\n        .baseDefense   = 63,\n        .baseSpeed     = 60,\n        .baseSpAttack  = 80,\n        .baseSpDefense = 80,": ".baseHP        = 65,\n        .baseAttack    = 85,\n        .baseDefense   = 75,\n        .baseSpeed     = 55,\n        .baseSpAttack  = 58,\n        .baseSpDefense = 70,",
        ".baseHP        = 80,\n        .baseAttack    = 82,\n        .baseDefense   = 83,\n        .baseSpeed     = 80,\n        .baseSpAttack  = 100,\n        .baseSpDefense = 100,": ".baseHP        = 88,\n        .baseAttack    = 110,\n        .baseDefense   = 95,\n        .baseSpeed     = 70,\n        .baseSpAttack  = 75,\n        .baseSpDefense = 90,",

        # Charmander line -> Cappuccino line: fast fire/shadow attacker.
        ".baseHP        = 39,\n        .baseAttack    = 52,\n        .baseDefense   = 43,\n        .baseSpeed     = 65,\n        .baseSpAttack  = 60,\n        .baseSpDefense = 50,": ".baseHP        = 39,\n        .baseAttack    = 58,\n        .baseDefense   = 38,\n        .baseSpeed     = 72,\n        .baseSpAttack  = 65,\n        .baseSpDefense = 45,",
        ".baseHP        = 58,\n        .baseAttack    = 64,\n        .baseDefense   = 58,\n        .baseSpeed     = 80,\n        .baseSpAttack  = 80,\n        .baseSpDefense = 65,": ".baseHP        = 58,\n        .baseAttack    = 75,\n        .baseDefense   = 52,\n        .baseSpeed     = 92,\n        .baseSpAttack  = 88,\n        .baseSpDefense = 58,",
        ".baseHP        = 78,\n        .baseAttack    = 84,\n        .baseDefense   = 78,\n        .baseSpeed     = 100,\n        .baseSpAttack  = 109,\n        .baseSpDefense = 85,": ".baseHP        = 78,\n        .baseAttack    = 98,\n        .baseDefense   = 72,\n        .baseSpeed     = 118,\n        .baseSpAttack  = 112,\n        .baseSpDefense = 76,",

        # Squirtle line -> Tralalero line: balanced water/meme.
        ".baseHP        = 44,\n        .baseAttack    = 48,\n        .baseDefense   = 65,\n        .baseSpeed     = 43,\n        .baseSpAttack  = 50,\n        .baseSpDefense = 64,": ".baseHP        = 50,\n        .baseAttack    = 52,\n        .baseDefense   = 58,\n        .baseSpeed     = 48,\n        .baseSpAttack  = 58,\n        .baseSpDefense = 58,",
        ".baseHP        = 59,\n        .baseAttack    = 63,\n        .baseDefense   = 80,\n        .baseSpeed     = 58,\n        .baseSpAttack  = 65,\n        .baseSpDefense = 80,": ".baseHP        = 68,\n        .baseAttack    = 70,\n        .baseDefense   = 82,\n        .baseSpeed     = 62,\n        .baseSpAttack  = 76,\n        .baseSpDefense = 78,",
        ".baseHP        = 79,\n        .baseAttack    = 83,\n        .baseDefense   = 100,\n        .baseSpeed     = 78,\n        .baseSpAttack  = 85,\n        .baseSpDefense = 105,": ".baseHP        = 88,\n        .baseAttack    = 90,\n        .baseDefense   = 102,\n        .baseSpeed     = 80,\n        .baseSpAttack  = 95,\n        .baseSpDefense = 104,",
    }

    changed = 0
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new, 1)
            changed += 1

    if changed < 9:
        raise RuntimeError(f"Stats patch incomplete: only {changed}/9 stat blocks changed")

    write(path, text)


def main() -> None:
    patch_species_names()
    patch_evolutions()
    patch_learnsets()
    patch_wild_encounters()
    patch_species_stats()
    print("Brainrot gameplay systems applied successfully.")
    print("Now run: make")


if __name__ == "__main__":
    main()
