#!/usr/bin/env python3
"""Phase 2 story pass for Brainrot: Echoes of Sahur.

This patch makes the early game less like vanilla FireRed:
- The rival battle becomes an emergency license evaluation.
- The BRAINDEX and Brainrot Balls are given immediately after the first duel.
- The parcel loop is skipped for the playtest.
- A best-effort Roan palette recolor is attempted if matching palette files exist.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def p(path: str) -> Path:
    return ROOT / path


def read(path: str) -> str:
    return p(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    p(path).write_text(text, encoding="utf-8")


def replace_between_labels(text: str, start_label: str, next_label: str, new_block: str) -> str:
    start_token = f"{start_label}::"
    next_token = f"{next_label}::"
    start = text.find(start_token)
    if start == -1:
        raise RuntimeError(f"start label not found: {start_label}")
    end = text.find(next_token, start)
    if end == -1:
        raise RuntimeError(f"next label not found after {start_label}: {next_label}")
    return text[:start] + new_block.rstrip() + "\n\n" + text[end:]


def replace_label_block(text: str, label: str, new_block: str) -> str:
    start_token = f"{label}::"
    start = text.find(start_token)
    if start == -1:
        raise RuntimeError(f"label not found: {label}")
    end = text.find("\n\n", start)
    if end == -1:
        end = len(text)
    return text[:start] + new_block.rstrip() + text[end:]


def ensure_text_label(text: str, label: str, block: str) -> str:
    if f"{label}::" in text:
        return text
    if not text.endswith("\n"):
        text += "\n"
    return text + "\n" + block.rstrip() + "\n"


def patch_training_center_script() -> None:
    path = "data/maps/PalletTown_ProfessorOaksLab/scripts.inc"
    text = read(path)

    new_end_rival_battle = """PalletTown_ProfessorOaksLab_EventScript_EndRivalBattle::
\tspecial HealPlayerParty
\tmsgbox PalletTown_ProfessorOaksLab_Text_RivalGoToughenMyMon
\tclosemessage
\tplaybgm MUS_RIVAL_EXIT, 0
\tcall_if_eq VAR_TEMP_2, 1, PalletTown_ProfessorOaksLab_EventScript_RivalExitAfterBattleLeft
\tcall_if_eq VAR_TEMP_2, 2, PalletTown_ProfessorOaksLab_EventScript_RivalExitAfterBattleMid
\tcall_if_eq VAR_TEMP_2, 3, PalletTown_ProfessorOaksLab_EventScript_RivalExitAfterBattleRight
\tremoveobject LOCALID_OAKS_LAB_RIVAL
\tplayse SE_EXIT
\tfadedefaultbgm
\tapplymovement LOCALID_OAKS_LAB_PROF_OAK, Common_Movement_FaceDown
\twaitmovement 0
\tmsgbox PalletTown_ProfessorOaksLab_Text_AvelarLicenseShock
\ttextcolor NPC_TEXT_COLOR_NEUTRAL
\tplayfanfare MUS_OBTAIN_KEY_ITEM
\tmessage PalletTown_ProfessorOaksLab_Text_ReceivedPokedexFromOak
\twaitmessage
\twaitfanfare
\tcall EventScript_RestorePrevTextColor
\tsetflag FLAG_SYS_POKEDEX_GET
\tspecial SetUnlockedPokedexFlags
\tsetvar VAR_MAP_SCENE_POKEMON_CENTER_TEALA, 1
\tmsgbox PalletTown_ProfessorOaksLab_Text_OakCatchMonsForDataTakeThese
\tgiveitem_msg PalletTown_ProfessorOaksLab_Text_ReceivedFivePokeBalls, ITEM_POKE_BALL, 5
\tmsgbox PalletTown_ProfessorOaksLab_Text_AvelarLicenseMission
\tsetvar VAR_MAP_SCENE_PALLET_TOWN_PROFESSOR_OAKS_LAB, 6
\tsetvar VAR_MAP_SCENE_VIRIDIAN_CITY_MART, 2
\tsetvar VAR_MAP_SCENE_VIRIDIAN_CITY_OLD_MAN, 1
\tsetvar VAR_MAP_SCENE_PALLET_TOWN_RIVALS_HOUSE, 1
\tsetvar VAR_MAP_SCENE_ROUTE22, 1
\tsetflag FLAG_BEAT_RIVAL_IN_OAKS_LAB
\treleaseall
\tend"""

    text = replace_between_labels(
        text,
        "PalletTown_ProfessorOaksLab_EventScript_EndRivalBattle",
        "PalletTown_ProfessorOaksLab_EventScript_RivalExitAfterBattleLeft",
        new_end_rival_battle,
    )
    write(path, text)


def patch_training_center_text() -> None:
    path = "data/maps/PalletTown_ProfessorOaksLab/text.inc"
    text = read(path)

    replacements = {
        "PalletTown_ProfessorOaksLab_Text_RivalFedUpWithWaiting": '''PalletTown_ProfessorOaksLab_Text_RivalFedUpWithWaiting::
    .string "{RIVAL}: AVELAR!\n"
    .string "If this is about the 67 case,\l"
    .string "I already know enough!$"''',
        "PalletTown_ProfessorOaksLab_Text_OakThreeMonsChooseOne": '''PalletTown_ProfessorOaksLab_Text_OakThreeMonsChooseOne::
    .string "AVELAR: Listen carefully.\p"
    .string "This is not a normal\n"
    .string "trainer ceremony.\p"
    .string "The old license order has\n"
    .string "been broken.\p"
    .string "These three BRAINROTS are\n"
    .string "stable enough to obey.\p"
    .string "Choose one. Then we test\n"
    .string "your mind immediately.$"''',
        "PalletTown_ProfessorOaksLab_Text_RivalLetsCheckOutMons": '''PalletTown_ProfessorOaksLab_Text_RivalLetsCheckOutMons::
    .string "{RIVAL}: Good. No fake\n"
    .string "speech. No boring route.\p"
    .string "First rule of the license:\n"
    .string "prove you can stand pressure!$"''',
        "PalletTown_ProfessorOaksLab_Text_RivalGoToughenMyMon": '''PalletTown_ProfessorOaksLab_Text_RivalGoToughenMyMon::
    .string "{RIVAL}: Tch!\n"
    .string "My head rang for a second.\p"
    .string "That was not fear.\n"
    .string "It was... signal noise.\p"
    .string "Whatever. I am going ahead.$"''',
        "PalletTown_ProfessorOaksLab_Text_OakCatchMonsForDataTakeThese": '''PalletTown_ProfessorOaksLab_Text_OakCatchMonsForDataTakeThese::
    .string "AVELAR: Take these now.\p"
    .string "No parcel mission.\n"
    .string "No waiting.\p"
    .string "If you see a BRAINROT,\n"
    .string "record it or catch it.$"''',
    }

    for label, block in replacements.items():
        text = replace_label_block(text, label, block)

    text = ensure_text_label(text, "PalletTown_ProfessorOaksLab_Text_AvelarLicenseShock", '''PalletTown_ProfessorOaksLab_Text_AvelarLicenseShock::
    .string "AVELAR: Stop.\p"
    .string "That duel spiked the\n"
    .string "Sahur reading.\p"
    .string "{PLAYER}, you resisted it.\n"
    .string "Most kids cannot.\p"
    .string "That means your license path\n"
    .string "starts right now.$"''')

    text = ensure_text_label(text, "PalletTown_ProfessorOaksLab_Text_AvelarLicenseMission", '''PalletTown_ProfessorOaksLab_Text_AvelarLicenseMission::
    .string "AVELAR: Your first objective\n"
    .string "is TEST ZONE 01.\p"
    .string "Do not chase badges.\n"
    .string "Chase evidence.\p"
    .string "If the name LUNA appears\n"
    .string "anywhere, come back.\p"
    .string "And {PLAYER}... do not let\n"
    .string "the noise finish your thoughts.$"''')

    write(path, text)


def patch_training_center_town_text() -> None:
    path = "data/maps/PalletTown/text.inc"
    text = read(path)
    replacements = {
        "PalletTown_Text_OakDontGoOut": '''PalletTown_Text_OakDontGoOut::
    .string "AVELAR: Roan! Stop!\n"
    .string "The gate is not a route anymore.$"''',
        "PalletTown_Text_OakGrassUnsafeNeedMon": '''PalletTown_Text_OakGrassUnsafeNeedMon::
    .string "AVELAR: That field was sealed\n"
    .string "after the first Sahur echo.\p"
    .string "Wild BRAINROTS are not pets.\n"
    .string "They copy fear.\p"
    .string "Come with me.\n"
    .string "Your test starts early.$"''',
        "PalletTown_Text_TownSign": '''PalletTown_Text_TownSign::
    .string "TRAINING CENTER 01\n"
    .string "Built over old Pallet Town\p"
    .string "License E candidates only$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_roan_palette_best_effort() -> None:
    """Try to darken Red/Roan colors without failing the build.

    The exact player palette path differs between FireRed forks, so this scans
    likely .pal files and replaces bright red rows with darker Roan colors.
    """
    likely_names = ("red", "boy", "player", "hero", "brendan")
    changed = []
    for pal in ROOT.glob("graphics/**/*.pal"):
        low = pal.as_posix().lower()
        if not any(name in low for name in likely_names):
            continue
        try:
            text = pal.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        original = text
        # Common JASC palette red ranges used by Red's hat/shirt.
        swaps = {
            "248 0 0": "32 48 88",
            "240 0 0": "32 48 88",
            "224 0 0": "40 56 104",
            "216 0 0": "40 56 104",
            "200 0 0": "24 32 64",
            "192 0 0": "24 32 64",
            "248 64 64": "64 96 160",
            "240 64 64": "64 96 160",
            "248 120 120": "104 144 216",
            "240 120 120": "104 144 216",
        }
        for old, new in swaps.items():
            text = text.replace(old, new)
        if text != original:
            pal.write_text(text, encoding="utf-8")
            changed.append(pal.as_posix())
    if changed:
        print("Roan palette recolor applied to:")
        for path in changed:
            print(f"  - {path}")
    else:
        print("Roan palette recolor skipped: no matching palette rows found yet.")


def main() -> None:
    patch_training_center_script()
    patch_training_center_text()
    patch_training_center_town_text()
    patch_roan_palette_best_effort()
    print("Brainrot phase 2 story patch applied.")


if __name__ == "__main__":
    main()
