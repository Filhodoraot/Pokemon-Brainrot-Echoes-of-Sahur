#!/usr/bin/env python3
"""Harder playtest tuning plus Cognia mental-space license tests.

The test is not a school quiz anymore.
COGNIA uses the user's mind as the test space, making a small mental maze.
At first, COGNIA thinks this is just science. Secretly, Dante's cult research
turns these tests into a slow Tung Tung scanning system for IQ priority.
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


def patch_brock_cognia_mental_maze() -> None:
    """Replace the old quiz with a small path-choice mental maze.

    It still uses simple FireRed event commands, but the fiction is not a quiz:
    the player is walking through a mental space created by COGNIA's system.
    The wrong corridors sound normal/safe, because common people in the story
    believe Brainrots are just normal creatures.
    """
    path = "data/maps/PewterCity_Gym/scripts.inc"
    text = read(path)

    brock = '''PewterCity_Gym_EventScript_Brock::
	goto_if_unset FLAG_BEAT_RIVAL_IN_OAKS_LAB, PewterCity_Gym_EventScript_TooEarly
	goto_if_set FLAG_TEMP_1, PewterCity_Gym_EventScript_BrockBattleReady
	msgbox PewterCity_Gym_Text_MentalMazeIntro
	msgbox PewterCity_Gym_Text_MentalMazeDoorOne, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, PewterCity_Gym_EventScript_MentalMazeFail
	msgbox PewterCity_Gym_Text_MentalMazeDoorTwo, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, PewterCity_Gym_EventScript_MentalMazeFail
	msgbox PewterCity_Gym_Text_MentalMazeDoorThree, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, PewterCity_Gym_EventScript_MentalMazeFail
	setflag FLAG_TEMP_1
	msgbox PewterCity_Gym_Text_MentalMazePass
	goto PewterCity_Gym_EventScript_BrockBattleReady

PewterCity_Gym_EventScript_BrockBattleReady::
	famechecker FAMECHECKER_BROCK, FCPICKSTATE_COLORED, UpdatePickStateFromSpecialVar8005
	trainerbattle_single TRAINER_LEADER_BROCK, PewterCity_Gym_Text_BrockIntro, PewterCity_Gym_Text_BrockDefeat, PewterCity_Gym_EventScript_DefeatedBrock, NO_MUSIC
	goto_if_unset FLAG_GOT_TM39_FROM_BROCK, PewterCity_Gym_EventScript_GiveTM39
	msgbox PewterCity_Gym_Text_BrockPostBattle
	release
	end

PewterCity_Gym_EventScript_MentalMazeFail::
	msgbox PewterCity_Gym_Text_MentalMazeFail
	closemessage
	delay 20
	release
	end'''
    text = replace_label_block(text, "PewterCity_Gym_EventScript_Brock", brock)
    write(path, text)

    text_path = "data/maps/PewterCity_Gym/text.inc"
    text = read(text_path)
    text = ensure_once(text, "PewterCity_Gym_Text_MentalMazeIntro::", '''PewterCity_Gym_Text_MentalMazeIntro::
    .string "BROCK: Before the duel, COGNIA\n"
    .string "requires a mind-space scan.\p"
    .string "Most people think BRAINROTS\n"
    .string "are only normal creatures.\p"
    .string "This system tests whether your\n"
    .string "mind follows the safe crowd\l"
    .string "or notices the hidden signal.$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_MentalMazeDoorOne::", '''PewterCity_Gym_Text_MentalMazeDoorOne::
    .string "Your mind becomes a hallway.\p"
    .string "LEFT door: children laughing\n"
    .string "with harmless BRAINROTS.\p"
    .string "RIGHT door: one quiet room\n"
    .string "with no sound at all.\p"
    .string "Enter the LEFT door?$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_MentalMazeDoorTwo::", '''PewterCity_Gym_Text_MentalMazeDoorTwo::
    .string "The silent room folds inward.\p"
    .string "A COGNIA sign says:\n"
    .string "DO NOT RESIST. THIS IS SAFE.\p"
    .string "A cracked wall shows a small\n"
    .string "LUNA scratch mark.\p"
    .string "Trust the COGNIA sign?$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_MentalMazeDoorThree::", '''PewterCity_Gym_Text_MentalMazeDoorThree::
    .string "Behind the crack, a number\n"
    .string "tries to write itself: 67.\p"
    .string "The hallway asks for your\n"
    .string "thoughts, not your voice.\p"
    .string "Step through without repeating\n"
    .string "the number out loud?$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_MentalMazePass::", '''PewterCity_Gym_Text_MentalMazePass::
    .string "BROCK: You passed.\p"
    .string "You ignored the easy story.\n"
    .string "That is rare.\p"
    .string "COGNIA calls this calibration.\n"
    .string "I am not sure that is all.$"''')
    text = ensure_once(text, "PewterCity_Gym_Text_MentalMazeFail::", '''PewterCity_Gym_Text_MentalMazeFail::
    .string "The hallway smiles.\p"
    .string "For a second, you believe\n"
    .string "everything is normal.\p"
    .string "Then the test rejects you.\n"
    .string "Your thoughts were too easy\l"
    .string "to lead.$"''')
    write(text_path, text)
    print("COGNIA mental maze trial added.")


def main() -> None:
    patch_trainer_difficulty()
    patch_wild_difficulty()
    patch_brock_cognia_mental_maze()
    print("Brainrot difficulty and Cognia mental test patch applied.")


if __name__ == "__main__":
    main()
