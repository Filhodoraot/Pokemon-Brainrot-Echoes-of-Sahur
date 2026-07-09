#!/usr/bin/env python3
"""Harder playtest tuning plus simple Brainrot license test minigames.

This keeps the build safe and uses only existing FireRed script commands.
The minigames are text/event based:
- Brock asks a focus test before the battle.
- Wrong answers do not softlock, but they waste time and force retry.
- Trainer and wild levels get a small difficulty bump.
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


def replace_label_block(text: str, label: str, new_block: str) -> str:
    start = text.find(f"{label}::")
    if start == -1:
        print(f"warning: label not found, skipped: {label}")
        return text
    end = text.find("\n\n", start)
    if end == -1:
        end = len(text)
    return text[:start] + new_block.rstrip() + text[end:]


def ensure_once(text: str, marker: str, block: str) -> str:
    if marker in text:
        return text
    if not text.endswith("\n"):
        text += "\n"
    return text + "\n" + block.rstrip() + "\n"


def harder_level(level: int) -> int:
    if level <= 5:
        return level + 1
    if level <= 12:
        return level + 2
    if level <= 24:
        return level + 3
    if level <= 40:
        return level + 4
    return min(level + 5, 75)


def harder_iv(level: int, current: int) -> int:
    target = 20
    if level >= 12:
        target = 40
    if level >= 24:
        target = 70
    if level >= 40:
        target = 100
    return max(current, target)


def patch_trainer_difficulty() -> None:
    path = "src/data/trainer_parties.h"
    text = read(path)

    def level_repl(match: re.Match[str]) -> str:
        old = int(match.group(1))
        return f".lvl = {harder_level(old)}"

    text = re.sub(r"\.lvl\s*=\s*(\d+)", level_repl, text)

    # Give trainers less cardboard IVs. This is light but noticeable.
    current_level = 5
    out: list[str] = []
    for line in text.splitlines():
        lvl_match = re.search(r"\.lvl\s*=\s*(\d+)", line)
        if lvl_match:
            current_level = int(lvl_match.group(1))
        iv_match = re.search(r"(\.iv\s*=\s*)(\d+)", line)
        if iv_match:
            old = int(iv_match.group(2))
            new = harder_iv(current_level, old)
            line = line[:iv_match.start(2)] + str(new) + line[iv_match.end(2):]
        out.append(line)

    write(path, "\n".join(out) + "\n")
    print("Trainer difficulty bumped: levels and IVs increased.")


def patch_wild_difficulty() -> None:
    path = "src/data/wild_encounters.json"
    try:
        data = json.loads(read(path))
    except Exception as exc:
        print(f"warning: wild encounters not patched: {exc}")
        return

    changed = 0
    for group in data.get("wild_encounter_groups", []):
        for encounter in group.get("encounters", []):
            for section_name in ("land_mons", "water_mons", "rock_smash_mons", "fishing_mons"):
                section = encounter.get(section_name)
                if not section:
                    continue
                for mon in section.get("mons", []):
                    for key in ("min_level", "max_level"):
                        if key in mon and isinstance(mon[key], int):
                            old = mon[key]
                            if old <= 20:
                                mon[key] = old + 1
                            elif old <= 40:
                                mon[key] = old + 2
                            else:
                                mon[key] = min(old + 3, 70)
                            changed += int(mon[key] != old)
    write(path, json.dumps(data, indent=2) + "\n")
    print(f"Wild difficulty bumped: {changed} level value(s) changed.")


def patch_brock_license_tests() -> None:
    path = "data/maps/PewterCity_Gym/scripts.inc"
    text = read(path)

    brock = '''PewterCity_Gym_EventScript_Brock::
	goto_if_unset FLAG_BEAT_RIVAL_IN_OAKS_LAB, PewterCity_Gym_EventScript_TooEarly
	goto_if_set FLAG_TEMP_1, PewterCity_Gym_EventScript_BrockBattleReady
	msgbox PewterCity_Gym_Text_FocusTestIntro
	msgbox PewterCity_Gym_Text_FocusTestQuestion1, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, PewterCity_Gym_EventScript_FocusTestWrong
	msgbox PewterCity_Gym_Text_FocusTestQuestion2, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, PewterCity_Gym_EventScript_FocusTestWrong
	msgbox PewterCity_Gym_Text_FocusTestQuestion3, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, PewterCity_Gym_EventScript_FocusTestWrong
	setflag FLAG_TEMP_1
	msgbox PewterCity_Gym_Text_FocusTestPass
	goto PewterCity_Gym_EventScript_BrockBattleReady

PewterCity_Gym_EventScript_BrockBattleReady::
	famechecker FAMECHECKER_BROCK, FCPICKSTATE_COLORED, UpdatePickStateFromSpecialVar8005
	trainerbattle_single TRAINER_LEADER_BROCK, PewterCity_Gym_Text_BrockIntro, PewterCity_Gym_Text_BrockDefeat, PewterCity_Gym_EventScript_DefeatedBrock, NO_MUSIC
	goto_if_unset FLAG_GOT_TM39_FROM_BROCK, PewterCity_Gym_EventScript_GiveTM39
	msgbox PewterCity_Gym_Text_BrockPostBattle
	release
	end

PewterCity_Gym_EventScript_FocusTestWrong::
	msgbox PewterCity_Gym_Text_FocusTestWrong
	closemessage
	delay 20
	release
	end'''
    text = replace_label_block(text, "PewterCity_Gym_EventScript_Brock", brock)
    write(path, text)

    text_path = "data/maps/PewterCity_Gym/text.inc"
    text = read(text_path)
    text = ensure_once(text, "PewterCity_Gym_Text_FocusTestIntro::", '''PewterCity_Gym_Text_FocusTestIntro::
    .string "BROCK: License D is not\n"
    .string "only a battle.\p"
    .string "First comes a focus test.\n"
    .string "Answer without letting the\l"
    .string "brainrot noise bait you.$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_FocusTestQuestion1::", '''PewterCity_Gym_Text_FocusTestQuestion1::
    .string "Question 1.\p"
    .string "Is TUNG TUNG SAHUR a normal\n"
    .string "evolution line with a mini form?$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_FocusTestQuestion2::", '''PewterCity_Gym_Text_FocusTestQuestion2::
    .string "Question 2.\p"
    .string "Should a trainer catch evidence\n"
    .string "instead of chasing noise?$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_FocusTestQuestion3::", '''PewterCity_Gym_Text_FocusTestQuestion3::
    .string "Question 3.\p"
    .string "If a mirror writes 67, should\n"
    .string "you repeat it out loud?$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_FocusTestPass::", '''PewterCity_Gym_Text_FocusTestPass::
    .string "BROCK: Good.\p"
    .string "Your focus did not wobble.\n"
    .string "Now comes the pressure duel.$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_FocusTestWrong::", '''PewterCity_Gym_Text_FocusTestWrong::
    .string "BROCK: Wrong.\p"
    .string "That answer lets the noise\n"
    .string "steer you.\p"
    .string "Step back, breathe, and try\n"
    .string "the test again.$"''')
    write(text_path, text)
    print("Brock focus-test minigame added.")


def main() -> None:
    patch_trainer_difficulty()
    patch_wild_difficulty()
    patch_brock_license_tests()
    print("Brainrot difficulty and test patch applied.")


if __name__ == "__main__":
    main()
