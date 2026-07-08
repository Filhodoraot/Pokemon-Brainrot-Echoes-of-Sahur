#!/usr/bin/env python3
"""Copy optional custom PNG/palette drop-ins into the FireRed graphics tree.

This lets the project accept new Roan and Brainrot sprites without manually
hunting every destination path.

Put files under custom_sprites/ and run this script before make.
Missing files are skipped, so the playtest can still build while art is WIP.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUSTOM = ROOT / "custom_sprites"


def copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"copied {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
    return True


ROAN_FILES = {
    "roan/red_normal.png": "graphics/object_events/pics/people/red_normal.png",
    "roan/red_item.png": "graphics/object_events/pics/people/red_item.png",
    "roan/red_surf_run.png": "graphics/object_events/pics/people/red_surf_run.png",
    "roan/red_surf.png": "graphics/object_events/pics/people/red_surf.png",
    "roan/red_bike.png": "graphics/object_events/pics/people/red_bike.png",
    "roan/red_vs_seeker_bike.png": "graphics/object_events/pics/people/red_vs_seeker_bike.png",
    "roan/red_fish.png": "graphics/object_events/pics/people/red_fish.png",
    "roan/player.pal": "graphics/object_events/palettes/player.pal",
    "roan/player_unused.pal": "graphics/object_events/palettes/player_unused.pal",
    "roan/player_reflection.pal": "graphics/object_events/palettes/player_reflection.pal",
}

# Brainrot name -> original Pokemon graphics folder.
BRAINROT_FOLDERS = {
    # Starters
    "chimpanzi": "bulbasaur",
    "bananini": "ivysaur",
    "avocador": "venusaur",
    "cappucino": "charmander",
    "harpucino": "charmeleon",
    "capassino": "charizard",
    "tralalero": "squirtle",
    "tralalito": "wartortle",
    "tralalord": "blastoise",

    # Test Zone 01
    "noobini": "pidgey",
    "pizzanini": "pidgeotto",
    "losnoobi": "pidgeot",
    "pipikiwi": "rattata",
    "pipicorni": "raticate",
    "timcheese": "spearow",
    "raccooni": "fearow",

    # Zone Green 01
    "bambini": "caterpie",
    "crostini": "metapod",
    "bambilord": "butterfree",
    "lirili": "weedle",
    "larila": "kakuna",
    "lirilord": "beedrill",
    "brrbrr": "pikachu",
    "patapim": "raichu",

    # Early cave/checkpoint placeholders
    "trippi": "zubat",
    "troppilord": "golbat",
    "tungmini": "geodude",
    "tungmed": "graveler",
    "tungrock": "golem",
    "moonini": "clefairy",
    "moonlord": "clefable",
    "sleeprot": "snorlax",
}

SPRITE_KINDS = ("front.png", "back.png", "icon.png", "normal.pal", "shiny.pal")


def apply_roan() -> int:
    copied = 0
    for src_rel, dst_rel in ROAN_FILES.items():
        if copy_if_exists(CUSTOM / src_rel, ROOT / dst_rel):
            copied += 1
    return copied


def apply_brainrots() -> int:
    copied = 0
    for brainrot, folder in BRAINROT_FOLDERS.items():
        for filename in SPRITE_KINDS:
            src = CUSTOM / "brainrots" / brainrot / filename
            dst = ROOT / "graphics" / "pokemon" / folder / filename
            if copy_if_exists(src, dst):
                copied += 1
    return copied


def main() -> None:
    if not CUSTOM.exists():
        print("custom_sprites folder not found; skipping custom sprite drop-ins.")
        return

    copied = apply_roan() + apply_brainrots()
    if copied == 0:
        print("No custom sprite drop-ins found yet; vanilla/placeholder graphics remain.")
    else:
        print(f"Applied {copied} custom sprite drop-in file(s).")


if __name__ == "__main__":
    main()
