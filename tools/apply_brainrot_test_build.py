#!/usr/bin/env python3
"""Apply Brainrot systems for a first playable test build.

Run from repo root:
    python3 tools/apply_brainrot_test_build.py
    make

This is intentionally sprite-free. Sprites come later.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def p(path: str) -> Path:
    return ROOT / path


def read(path: str) -> str:
    return p(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    p(path).write_text(text, encoding="utf-8")


def set_species_name(text: str, species: str, name: str) -> str:
    pattern = rf'^(\s*\[{re.escape(species)}\]\s*=\s*_\(")[^"]*("\),)$'
    repl = rf'\1{name}\2'
    new_text, count = re.subn(pattern, repl, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"species name not found: {species}")
    return new_text


def patch_species_names() -> None:
    path = "src/data/text/species_names.h"
    text = read(path)
    names = {
        # Starters
        "SPECIES_BULBASAUR": "CHIMPANZI",
        "SPECIES_IVYSAUR": "BANANINI",
        "SPECIES_VENUSAUR": "AVOCADOR",
        "SPECIES_CHARMANDER": "CAPPUCINO",
        "SPECIES_CHARMELEON": "HARPUCINO",
        "SPECIES_CHARIZARD": "CAPASSINO",
        "SPECIES_SQUIRTLE": "TRALALERO",
        "SPECIES_WARTORTLE": "TRALALITO",
        "SPECIES_BLASTOISE": "TRALALORD",

        # Test Zone 01
        "SPECIES_PIDGEY": "NOOBINI",
        "SPECIES_PIDGEOTTO": "PIZZANINI",
        "SPECIES_PIDGEOT": "LOSNOOBI",
        "SPECIES_RATTATA": "PIPIKIWI",
        "SPECIES_RATICATE": "PIPICORNI",
        "SPECIES_SPEAROW": "TIMCHEESE",
        "SPECIES_FEAROW": "RACCOONI",

        # Zone Green 01
        "SPECIES_CATERPIE": "BAMBINI",
        "SPECIES_METAPOD": "CROSTINI",
        "SPECIES_BUTTERFREE": "BAMBILORD",
        "SPECIES_WEEDLE": "LIRILI",
        "SPECIES_KAKUNA": "LARILA",
        "SPECIES_BEEDRILL": "LIRILORD",
        "SPECIES_PIKACHU": "BRRBRR",
        "SPECIES_RAICHU": "PATAPIM",

        # First cave/checkpoint placeholders
        "SPECIES_ZUBAT": "TRIPPI",
        "SPECIES_GOLBAT": "TROPPILORD",
        "SPECIES_GEODUDE": "TUNGMINI",
        "SPECIES_GRAVELER": "TUNGMED",
        "SPECIES_GOLEM": "TUNGROCK",
        "SPECIES_CLEFAIRY": "MOONINI",
        "SPECIES_CLEFABLE": "MOONLORD",
        "SPECIES_SNORLAX": "SLEEPROT",
    }
    for species, name in names.items():
        text = set_species_name(text, species, name)
    write(path, text)


def set_evolution_line(text: str, species: str, line: str) -> str:
    pattern = rf'^\s*\[{re.escape(species)}\]\s*=\s*.*,$'
    new_text, count = re.subn(pattern, line, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"evolution line not found: {species}")
    return new_text


def patch_evolutions() -> None:
    path = "src/data/pokemon/evolution.h"
    text = read(path)
    lines = {
        "SPECIES_BULBASAUR": "    [SPECIES_BULBASAUR] = {{EVO_LEVEL, 16, SPECIES_IVYSAUR}},",
        "SPECIES_IVYSAUR": "    [SPECIES_IVYSAUR] = {{EVO_LEVEL, 32, SPECIES_VENUSAUR}},",
        "SPECIES_CHARMANDER": "    [SPECIES_CHARMANDER] = {{EVO_LEVEL, 16, SPECIES_CHARMELEON}},",
        "SPECIES_CHARMELEON": "    [SPECIES_CHARMELEON] = {{EVO_LEVEL, 32, SPECIES_CHARIZARD}},",
        "SPECIES_SQUIRTLE": "    [SPECIES_SQUIRTLE] = {{EVO_LEVEL, 16, SPECIES_WARTORTLE}},",
        "SPECIES_WARTORTLE": "    [SPECIES_WARTORTLE] = {{EVO_LEVEL, 32, SPECIES_BLASTOISE}},",
        "SPECIES_PIDGEY": "    [SPECIES_PIDGEY] = {{EVO_LEVEL, 16, SPECIES_PIDGEOTTO}},",
        "SPECIES_PIDGEOTTO": "    [SPECIES_PIDGEOTTO] = {{EVO_LEVEL, 32, SPECIES_PIDGEOT}},",
        "SPECIES_RATTATA": "    [SPECIES_RATTATA] = {{EVO_LEVEL, 18, SPECIES_RATICATE}},",
        "SPECIES_CATERPIE": "    [SPECIES_CATERPIE] = {{EVO_LEVEL, 7, SPECIES_METAPOD}},",
        "SPECIES_METAPOD": "    [SPECIES_METAPOD] = {{EVO_LEVEL, 12, SPECIES_BUTTERFREE}},",
        "SPECIES_WEEDLE": "    [SPECIES_WEEDLE] = {{EVO_LEVEL, 7, SPECIES_KAKUNA}},",
        "SPECIES_KAKUNA": "    [SPECIES_KAKUNA] = {{EVO_LEVEL, 12, SPECIES_BEEDRILL}},",
        "SPECIES_PIKACHU": "    [SPECIES_PIKACHU] = {{EVO_ITEM, ITEM_THUNDER_STONE, SPECIES_RAICHU}},",
        # Tim Cheese and Raccooni are separate Brainrots, no normal evo.
        "SPECIES_SPEAROW": "    [SPECIES_SPEAROW] = {{0}},",
    }
    for species, line in lines.items():
        text = set_evolution_line(text, species, line)
    write(path, text)


def replace_c_array(text: str, name: str, new_block: str) -> str:
    start = text.find(f"static const u16 {name}[] = {{")
    if start == -1:
        raise RuntimeError(f"learnset not found: {name}")
    end = text.find("};", start)
    if end == -1:
        raise RuntimeError(f"learnset end not found: {name}")
    return text[:start] + new_block + text[end + 2:]


def patch_learnsets() -> None:
    path = "src/data/pokemon/level_up_learnsets.h"
    text = read(path)
    blocks = {
        "sBulbasaurLevelUpLearnset": '''static const u16 sBulbasaurLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(3, MOVE_GROWL),
    LEVEL_UP_MOVE(7, MOVE_VINE_WHIP),
    LEVEL_UP_MOVE(10, MOVE_LEECH_SEED),
    LEVEL_UP_MOVE(15, MOVE_RAZOR_LEAF),
    LEVEL_UP_MOVE(20, MOVE_TAKE_DOWN),
    LEVEL_UP_MOVE(25, MOVE_SLEEP_POWDER),
    LEVEL_UP_MOVE(32, MOVE_SLAM),
    LEVEL_UP_END
};''',
        "sCharmanderLevelUpLearnset": '''static const u16 sCharmanderLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_SCRATCH),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(7, MOVE_EMBER),
    LEVEL_UP_MOVE(10, MOVE_SMOKESCREEN),
    LEVEL_UP_MOVE(16, MOVE_METAL_CLAW),
    LEVEL_UP_MOVE(22, MOVE_SCARY_FACE),
    LEVEL_UP_MOVE(28, MOVE_FLAMETHROWER),
    LEVEL_UP_MOVE(36, MOVE_SLASH),
    LEVEL_UP_END
};''',
        "sSquirtleLevelUpLearnset": '''static const u16 sSquirtleLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(4, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(7, MOVE_BUBBLE),
    LEVEL_UP_MOVE(10, MOVE_WITHDRAW),
    LEVEL_UP_MOVE(15, MOVE_WATER_GUN),
    LEVEL_UP_MOVE(20, MOVE_BITE),
    LEVEL_UP_MOVE(26, MOVE_PROTECT),
    LEVEL_UP_MOVE(34, MOVE_SURF),
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
        "sPidgeottoLevelUpLearnset": '''static const u16 sPidgeottoLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(5, MOVE_SAND_ATTACK),
    LEVEL_UP_MOVE(9, MOVE_GUST),
    LEVEL_UP_MOVE(13, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(17, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(22, MOVE_WING_ATTACK),
    LEVEL_UP_MOVE(31, MOVE_AGILITY),
    LEVEL_UP_MOVE(40, MOVE_MIRROR_MOVE),
    LEVEL_UP_END
};''',
        "sPidgeotLevelUpLearnset": '''static const u16 sPidgeotLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(5, MOVE_SAND_ATTACK),
    LEVEL_UP_MOVE(9, MOVE_GUST),
    LEVEL_UP_MOVE(13, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(17, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(22, MOVE_WING_ATTACK),
    LEVEL_UP_MOVE(33, MOVE_AGILITY),
    LEVEL_UP_MOVE(44, MOVE_MIRROR_MOVE),
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
        "sRaticateLevelUpLearnset": '''static const u16 sRaticateLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(7, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(13, MOVE_FOCUS_ENERGY),
    LEVEL_UP_MOVE(20, MOVE_HYPER_FANG),
    LEVEL_UP_MOVE(30, MOVE_PURSUIT),
    LEVEL_UP_MOVE(40, MOVE_SUPER_FANG),
    LEVEL_UP_MOVE(50, MOVE_ENDEAVOR),
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
    }
    for name, block in blocks.items():
        text = replace_c_array(text, name, block)
    write(path, text)


def find_species_block(text: str, species: str) -> tuple[int, int, str]:
    start = text.find(f"    [{species}] =")
    if start == -1:
        raise RuntimeError(f"species info not found: {species}")
    end = text.find("    },", start)
    if end == -1:
        raise RuntimeError(f"species info end not found: {species}")
    end += len("    },")
    return start, end, text[start:end]


def patch_stat_block(block: str, stats: dict[str, int]) -> str:
    for field, value in stats.items():
        pattern = rf'(\.{field}\s*=\s*)\d+'
        block, count = re.subn(pattern, rf'\g<1>{value}', block, count=1)
        if count != 1:
            raise RuntimeError(f"stat field not found: {field}")
    return block


def patch_species_stats() -> None:
    path = "src/data/pokemon/species_info.h"
    text = read(path)
    stats = {
        "SPECIES_BULBASAUR": dict(baseHP=48, baseAttack=65, baseDefense=55, baseSpeed=42, baseSpAttack=45, baseSpDefense=50),
        "SPECIES_IVYSAUR": dict(baseHP=65, baseAttack=85, baseDefense=75, baseSpeed=55, baseSpAttack=58, baseSpDefense=70),
        "SPECIES_VENUSAUR": dict(baseHP=88, baseAttack=110, baseDefense=95, baseSpeed=70, baseSpAttack=75, baseSpDefense=90),
        "SPECIES_CHARMANDER": dict(baseHP=39, baseAttack=58, baseDefense=38, baseSpeed=72, baseSpAttack=65, baseSpDefense=45),
        "SPECIES_CHARMELEON": dict(baseHP=58, baseAttack=75, baseDefense=52, baseSpeed=92, baseSpAttack=88, baseSpDefense=58),
        "SPECIES_CHARIZARD": dict(baseHP=78, baseAttack=98, baseDefense=72, baseSpeed=118, baseSpAttack=112, baseSpDefense=76),
        "SPECIES_SQUIRTLE": dict(baseHP=50, baseAttack=52, baseDefense=58, baseSpeed=48, baseSpAttack=58, baseSpDefense=58),
        "SPECIES_WARTORTLE": dict(baseHP=68, baseAttack=70, baseDefense=82, baseSpeed=62, baseSpAttack=76, baseSpDefense=78),
        "SPECIES_BLASTOISE": dict(baseHP=88, baseAttack=90, baseDefense=102, baseSpeed=80, baseSpAttack=95, baseSpDefense=104),
        "SPECIES_PIDGEY": dict(baseHP=38, baseAttack=48, baseDefense=36, baseSpeed=58, baseSpAttack=35, baseSpDefense=35),
        "SPECIES_RATTATA": dict(baseHP=35, baseAttack=58, baseDefense=35, baseSpeed=72, baseSpAttack=25, baseSpDefense=35),
        "SPECIES_SPEAROW": dict(baseHP=42, baseAttack=66, baseDefense=35, baseSpeed=72, baseSpAttack=31, baseSpDefense=31),
        "SPECIES_FEAROW": dict(baseHP=55, baseAttack=80, baseDefense=55, baseSpeed=78, baseSpAttack=45, baseSpDefense=45),
        "SPECIES_CATERPIE": dict(baseHP=45, baseAttack=35, baseDefense=40, baseSpeed=45, baseSpAttack=30, baseSpDefense=30),
        "SPECIES_WEEDLE": dict(baseHP=40, baseAttack=40, baseDefense=35, baseSpeed=50, baseSpAttack=25, baseSpDefense=30),
        "SPECIES_PIKACHU": dict(baseHP=35, baseAttack=55, baseDefense=35, baseSpeed=90, baseSpAttack=50, baseSpDefense=40),
    }
    for species, values in stats.items():
        start, end, block = find_species_block(text, species)
        text = text[:start] + patch_stat_block(block, values) + text[end:]
    write(path, text)


def patch_wild_encounters() -> None:
    path = "src/data/wild_encounters.json"
    data = json.loads(read(path))
    route1 = [
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
    forest = [
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
    done = {"route1": False, "forest": False}
    for group in data.get("wild_encounter_groups", []):
        for enc in group.get("encounters", []):
            if enc.get("map") == "MAP_ROUTE1" and enc.get("base_label") == "sRoute1_FireRed":
                enc["land_mons"]["mons"] = route1
                done["route1"] = True
            if enc.get("map") == "MAP_VIRIDIAN_FOREST" and enc.get("base_label") == "sViridianForest_FireRed":
                enc["land_mons"]["mons"] = forest
                done["forest"] = True
    missing = [k for k, v in done.items() if not v]
    if missing:
        raise RuntimeError(f"missing encounter patch: {missing}")
    write(path, json.dumps(data, indent=2) + "\n")


def patch_battle_terms() -> None:
    # Battle text still says POKeMON by default. For the test build, make battle UI speak Brainrot.
    paths = ["src/battle_message.c", "src/strings.c"]
    for path in paths:
        text = read(path)
        text = text.replace("POKéMON", "BRAINROT")
        text = text.replace("Pokémon", "Brainrot")
        text = text.replace("pokemon", "brainrot")
        text = text.replace("POKé BALL", "BRAINROT BALL")
        text = text.replace("POKé Ball", "Brainrot Ball")
        write(path, text)


def main() -> None:
    patch_species_names()
    patch_evolutions()
    patch_learnsets()
    patch_species_stats()
    patch_wild_encounters()
    patch_battle_terms()
    print("Brainrot test build patch applied.")
    print("Now run: make")


if __name__ == "__main__":
    main()
