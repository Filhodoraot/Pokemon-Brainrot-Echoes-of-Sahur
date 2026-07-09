#!/usr/bin/env python3
"""Progression locks and text cleanup for Brainrot playtests.

This patch is build-safe. If a target label changes, it prints a warning and
continues instead of killing the whole playtest build.
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


def ensure_once(text: str, marker: str, block: str) -> str:
    if marker in text:
        return text
    if not text.endswith("\n"):
        text += "\n"
    return text + "\n" + block.rstrip() + "\n"


def replace_label_block(text: str, label: str, new_block: str) -> tuple[str, bool]:
    start = text.find(f"{label}::")
    if start == -1:
        print(f"warning: label not found, skipped: {label}")
        return text, False
    end = text.find("\n\n", start)
    if end == -1:
        end = len(text)
    return text[:start] + new_block.rstrip() + text[end:], True


def safe_regex_replace(text: str, pattern: str, replacement: str, name: str) -> str:
    new_text, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        print(f"warning: regex target not found, skipped: {name}")
        return text
    return new_text


def patch_pallet_route_lock() -> None:
    map_path = "data/maps/PalletTown/map.json"
    try:
        data = json.loads(read(map_path))
    except Exception as exc:
        print(f"warning: could not read {map_path}: {exc}")
        return

    coord_events = data.setdefault("coord_events", [])
    needed = [
        {
            "type": "trigger",
            "x": 12,
            "y": 1,
            "elevation": 3,
            "var": "VAR_MAP_SCENE_PALLET_TOWN_OAK",
            "var_value": "1",
            "script": "PalletTown_EventScript_BlockRouteUntilRivalBattle",
        },
        {
            "type": "trigger",
            "x": 13,
            "y": 1,
            "elevation": 3,
            "var": "VAR_MAP_SCENE_PALLET_TOWN_OAK",
            "var_value": "1",
            "script": "PalletTown_EventScript_BlockRouteUntilRivalBattle",
        },
    ]
    for event in needed:
        if not any(e.get("x") == event["x"] and e.get("y") == event["y"] and e.get("script") == event["script"] for e in coord_events):
            coord_events.append(event)
    write(map_path, json.dumps(data, indent=2) + "\n")

    script_path = "data/maps/PalletTown/scripts.inc"
    text = read(script_path)
    block = '''PalletTown_EventScript_BlockRouteUntilRivalBattle::
	lockall
	goto_if_set FLAG_BEAT_RIVAL_IN_OAKS_LAB, PalletTown_EventScript_BlockRouteUntilRivalBattle_Pass
	msgbox PalletTown_Text_RivalBattleRequired
	closemessage
	applymovement LOCALID_PLAYER, PalletTown_Movement_PlayerStepBackFromRoute
	waitmovement 0
	releaseall
	end

PalletTown_EventScript_BlockRouteUntilRivalBattle_Pass::
	releaseall
	end

PalletTown_Movement_PlayerStepBackFromRoute::
	walk_down
	step_end'''
    text = ensure_once(text, "PalletTown_EventScript_BlockRouteUntilRivalBattle::", block)
    write(script_path, text)

    text_path = "data/maps/PalletTown/text.inc"
    text = read(text_path)
    text = ensure_once(text, "PalletTown_Text_RivalBattleRequired::", '''PalletTown_Text_RivalBattleRequired::
    .string "AVELAR: Not yet, {PLAYER}.\p"
    .string "Your first License E check is\n"
    .string "inside the lab.\p"
    .string "Face KIUNIN first.\n"
    .string "Then TEST ZONE 01 opens.$"''')
    write(text_path, text)


def patch_pewter_gym_lock() -> None:
    path = "data/maps/PewterCity_Gym/scripts.inc"
    text = read(path)

    brock = '''PewterCity_Gym_EventScript_Brock::
	goto_if_unset FLAG_BEAT_RIVAL_IN_OAKS_LAB, PewterCity_Gym_EventScript_TooEarly
	famechecker FAMECHECKER_BROCK, FCPICKSTATE_COLORED, UpdatePickStateFromSpecialVar8005
	trainerbattle_single TRAINER_LEADER_BROCK, PewterCity_Gym_Text_BrockIntro, PewterCity_Gym_Text_BrockDefeat, PewterCity_Gym_EventScript_DefeatedBrock, NO_MUSIC
	goto_if_unset FLAG_GOT_TM39_FROM_BROCK, PewterCity_Gym_EventScript_GiveTM39
	msgbox PewterCity_Gym_Text_BrockPostBattle
	release
	end'''
    text, _ = replace_label_block(text, "PewterCity_Gym_EventScript_Brock", brock)

    liam = '''PewterCity_Gym_EventScript_Liam::
	goto_if_unset FLAG_BEAT_RIVAL_IN_OAKS_LAB, PewterCity_Gym_EventScript_TooEarly
	trainerbattle_single TRAINER_CAMPER_LIAM, PewterCity_Gym_Text_LiamIntro, PewterCity_Gym_Text_LiamDefeat
	msgbox PewterCity_Gym_Text_LiamPostBattle, MSGBOX_AUTOCLOSE
	end'''
    text, _ = replace_label_block(text, "PewterCity_Gym_EventScript_Liam", liam)

    block = '''PewterCity_Gym_EventScript_TooEarly::
	msgbox PewterCity_Gym_Text_TooEarly
	release
	end'''
    text = ensure_once(text, "PewterCity_Gym_EventScript_TooEarly::", block)
    write(path, text)

    text_path = "data/maps/PewterCity_Gym/text.inc"
    text = read(text_path)
    text = ensure_once(text, "PewterCity_Gym_Text_TooEarly::", '''PewterCity_Gym_Text_TooEarly::
    .string "BROCK: This exam is locked.\p"
    .string "You skipped the first lab\n"
    .string "pressure test.\p"
    .string "Go back to TRAINING CENTER 01\n"
    .string "and battle KIUNIN first.$"''')
    write(text_path, text)


def patch_no_tung_mini_line() -> None:
    path = "src/data/text/species_names.h"
    text = read(path)
    replacements = {
        "SPECIES_GEODUDE": "TALPINI",
        "SPECIES_GRAVELER": "TALPADI",
        "SPECIES_GOLEM": "TALPAFERO",
    }
    for species, name in replacements.items():
        pattern = rf'^(\s*\[{re.escape(species)}\]\s*=\s*_\(")[^"]*("\),)$'
        text = safe_regex_replace(text, pattern, rf'\1{name}\2', f"rename {species}")
    write(path, text)

    path = "src/data/pokemon/evolution.h"
    text = read(path)
    lines = {
        "SPECIES_GEODUDE": "    [SPECIES_GEODUDE] = {{EVO_LEVEL, 25, SPECIES_GRAVELER}},",
        "SPECIES_GRAVELER": "    [SPECIES_GRAVELER] = {{EVO_LEVEL, 38, SPECIES_GOLEM}},",
        "SPECIES_GOLEM": "    [SPECIES_GOLEM] = {{0}},",
    }
    for species, line in lines.items():
        pattern = rf"^\s*\[{re.escape(species)}\]\s*=\s*.*,$"
        text = safe_regex_replace(text, pattern, line, f"evolution {species}")
    write(path, text)


def cleanup_string_line(line: str) -> str:
    if ".string" not in line:
        return line
    replacements = {
        "POKéMON": "BRAINROT",
        "Pokémon": "Brainrot",
        "POKEMON": "BRAINROT",
        "Pokemon": "Brainrot",
        "pokemon": "brainrot",
        "POKé BALL": "BRAINROT BALL",
        "POKé Ball": "Brainrot Ball",
        "POKE BALL": "BRAINROT BALL",
        "Poke Ball": "Brainrot Ball",
        "POKéDEX": "BRAINDEX",
        "Pokédex": "Braindex",
        "Pokedex": "Braindex",
        "TUNGMINI": "TALPINI",
        "TUNGMED": "TALPADI",
        "TUNGROCK": "TALPAFERO",
        "Tung Mini": "Talpini",
        "Tung Med": "Talpadi",
        "Tung Rock": "Talpafero",
    }
    for old, new in replacements.items():
        line = line.replace(old, new)
    return line


def patch_text_terms() -> None:
    changed_files = 0
    for base in (ROOT / "data" / "maps", ROOT / "data" / "text"):
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.inc")):
            text = path.read_text(encoding="utf-8")
            cleaned = "\n".join(cleanup_string_line(line) for line in text.splitlines())
            if text.endswith("\n"):
                cleaned += "\n"
            if cleaned != text:
                path.write_text(cleaned, encoding="utf-8")
                changed_files += 1
    print(f"Cleaned vanilla text terms in {changed_files} file(s).")


def main() -> None:
    patch_pallet_route_lock()
    patch_pewter_gym_lock()
    patch_no_tung_mini_line()
    patch_text_terms()
    print("Brainrot progression/text cleanup applied safely.")


if __name__ == "__main__":
    main()
