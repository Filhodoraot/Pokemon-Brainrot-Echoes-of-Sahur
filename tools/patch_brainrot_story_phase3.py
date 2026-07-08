#!/usr/bin/env python3
"""Phase 3 identity pass for Brainrot: Echoes of Sahur.

This pass focuses on making the start feel less like vanilla FireRed:
- Stronger Roan/Luna setup in the player's house.
- More direct TV/bedroom hints.
- A stronger best-effort Roan recolor by detecting red-heavy palette rows.

It does not replace pixel art yet. Full no-cap Roan needs new sprite sheets.
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


def replace_label_block(text: str, label: str, new_block: str) -> str:
    start_token = f"{label}::"
    start = text.find(start_token)
    if start == -1:
        raise RuntimeError(f"label not found: {label}")
    end = text.find("\n\n", start)
    if end == -1:
        end = len(text)
    return text[:start] + new_block.rstrip() + text[end:]


def patch_roan_house_text() -> None:
    path = "data/maps/PalletTown_PlayersHouse_1F/text.inc"
    text = read(path)
    replacements = {
        "PalletTown_PlayersHouse_1F_Text_AllBoysLeaveOakLookingForYou": '''PalletTown_PlayersHouse_1F_Text_AllBoysLeaveOakLookingForYou::
    .string "MOM: Roan...\p"
    .string "You woke up saying LUNA\n"
    .string "again.\p"
    .string "I checked every photo.\n"
    .string "Every record.\p"
    .string "There was never a girl\n"
    .string "with that name here.\p"
    .string "But I know your eyes.\n"
    .string "You remember something.$"''',
        "PalletTown_PlayersHouse_1F_Text_AllGirlsLeaveOakLookingForYou": '''PalletTown_PlayersHouse_1F_Text_AllGirlsLeaveOakLookingForYou::
    .string "MOM: Roan...\p"
    .string "You woke up saying LUNA\n"
    .string "again.\p"
    .string "I checked every photo.\n"
    .string "Every record.\p"
    .string "There was never a girl\n"
    .string "with that name here.\p"
    .string "But I know your eyes.\n"
    .string "You remember something.$"''',
        "PalletTown_PlayersHouse_1F_Text_YouShouldTakeQuickRest": '''PalletTown_PlayersHouse_1F_Text_YouShouldTakeQuickRest::
    .string "MOM: Rest. Please.\p"
    .string "Every time you chase that\n"
    .string "memory, your fever returns.\p"
    .string "The doctors called it\n"
    .string "Sahur echo stress.$"''',
        "PalletTown_PlayersHouse_1F_Text_LookingGreatTakeCare": '''PalletTown_PlayersHouse_1F_Text_LookingGreatTakeCare::
    .string "MOM: Your partner is calmer\n"
    .string "than I expected.\p"
    .string "Maybe it feels what you\n"
    .string "are carrying.\p"
    .string "Come back alive, Roan.$"''',
        "PalletTown_PlayersHouse_1F_Text_MovieOnTVFourBoysOnRailroad": '''PalletTown_PlayersHouse_1F_Text_MovieOnTVFourBoysOnRailroad::
    .string "The TV shows a COGNIA report.\p"
    .string "BRAINROTS are harmless when\n"
    .string "licensed, they say.\p"
    .string "For one frame, the screen\n"
    .string "cuts to a hospital hall.$"''',
        "PalletTown_PlayersHouse_1F_Text_MovieOnTVGirlOnBrickRoad": '''PalletTown_PlayersHouse_1F_Text_MovieOnTVGirlOnBrickRoad::
    .string "The TV shows a COGNIA report.\p"
    .string "Memory gaps are normal\n"
    .string "after mass stress, they say.\p"
    .string "The word LUNA flashes, then\n"
    .string "vanishes.$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_roan_room_text() -> None:
    path = "data/maps/PalletTown_PlayersHouse_2F/text.inc"
    text = read(path)
    replacements = {
        "PalletTown_PlayersHouse_2F_Text_PlayedWithNES": '''PalletTown_PlayersHouse_2F_Text_PlayedWithNES::
    .string "Roan checked the old console.\p"
    .string "The screen should be off,\n"
    .string "but blue text appears.\p"
    .string "LUNA: do not forget me.\p"
    .string "Then only static remains.$"''',
        "PalletTown_PlayersHouse_2F_Text_PressLRForHelp": '''PalletTown_PlayersHouse_2F_Text_PressLRForHelp::
    .string "A COGNIA safety notice...\p"
    .string "If repeated words remain\n"
    .string "inside your head,\l"
    .string "report to a license center.\p"
    .string "Roan wrote under it:\n"
    .string "They are hiding something.$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def recolor_palette_text(text: str) -> tuple[str, bool]:
    changed = False
    out: list[str] = []
    for line in text.splitlines():
        parts = line.strip().split()
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            r, g, b = map(int, parts)
            # Darken red/orange-heavy colors into Roan's dark blue jacket colors.
            if r >= 120 and r > g * 2 and r > b * 2:
                brightness = (r + g + b) // 3
                if brightness >= 90:
                    line = "40 58 106"
                else:
                    line = "24 32 64"
                changed = True
            # Turn very bright cap highlight red/pink into cold blue highlight.
            elif r >= 170 and g >= 40 and b >= 40 and r > g and r > b:
                line = "88 128 208"
                changed = True
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), changed


def patch_roan_palette_best_effort() -> None:
    likely_names = (
        "red",
        "boy",
        "male",
        "player",
        "hero",
        "brendan",
        "trainer_red",
        "leaf",
    )
    changed_paths: list[str] = []
    scanned_paths: list[str] = []

    for pal in ROOT.glob("graphics/**/*.pal"):
        low = pal.as_posix().lower()
        if not any(name in low for name in likely_names):
            continue
        try:
            text = pal.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        scanned_paths.append(pal.as_posix())
        new_text, changed = recolor_palette_text(text)
        if changed:
            pal.write_text(new_text, encoding="utf-8")
            changed_paths.append(pal.as_posix())

    print("Roan palette scan candidates:")
    for path in scanned_paths[:40]:
        print(f"  - {path}")
    if len(scanned_paths) > 40:
        print(f"  ...and {len(scanned_paths) - 40} more")

    if changed_paths:
        print("Roan palette recolor applied to:")
        for path in changed_paths:
            print(f"  - {path}")
    else:
        print("Roan palette recolor skipped: no red-heavy player palette rows found.")


def main() -> None:
    patch_roan_house_text()
    patch_roan_room_text()
    patch_roan_palette_best_effort()
    print("Brainrot phase 3 Roan identity patch applied.")


if __name__ == "__main__":
    main()
