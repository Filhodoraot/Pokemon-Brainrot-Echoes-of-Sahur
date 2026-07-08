#!/usr/bin/env python3
"""Copy optional custom PNG/palette drop-ins into the FireRed graphics tree.

This lets the project accept new Roan and Brainrot sprites without manually
hunting every destination path.

Accepted layouts:

    custom_sprites/brainrots/noobini/front.png
    custom_sprites/custom_sprites/brainrots/noobini/front.png
    BrainrotImages/brainrots/noobini/front.png
    BrainrotImages/custom_sprites/brainrots/noobini/front.png

Missing files are skipped, so the playtest can still build while art is WIP.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Any of these roots can contain brainrots/ or roan/.
CUSTOM_CANDIDATES = (
    ROOT / "custom_sprites",
    ROOT / "custom_sprites" / "custom_sprites",
    ROOT / "BrainrotImages",
    ROOT / "BrainrotImages" / "custom_sprites",
)


def copy_if_exists(src: Path, dst: Path, copied_dests: set[Path]) -> bool:
    if not src.exists():
        return False
    # If the same destination was already filled by a higher-priority root,
    # do not overwrite it with a duplicate from another extracted folder.
    if dst in copied_dests:
        print(f"skipped duplicate {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    copied_dests.add(dst)
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


def existing_custom_roots() -> list[Path]:
    roots: list[Path] = []
    for root in CUSTOM_CANDIDATES:
        if (root / "brainrots").exists() or (root / "roan").exists():
            roots.append(root)
    return roots


def apply_roan(copied_dests: set[Path]) -> int:
    copied = 0
    for custom_root in existing_custom_roots():
        for src_rel, dst_rel in ROAN_FILES.items():
            if copy_if_exists(custom_root / src_rel, ROOT / dst_rel, copied_dests):
                copied += 1
    return copied


def apply_brainrots(copied_dests: set[Path]) -> int:
    copied = 0
    for custom_root in existing_custom_roots():
        for brainrot, folder in BRAINROT_FOLDERS.items():
            for filename in SPRITE_KINDS:
                src = custom_root / "brainrots" / brainrot / filename
                dst = ROOT / "graphics" / "pokemon" / folder / filename
                if copy_if_exists(src, dst, copied_dests):
                    copied += 1
    return copied


def main() -> None:
    roots = existing_custom_roots()
    if not roots:
        print("No custom sprite drop-in roots found; vanilla/placeholder graphics remain.")
        print("Expected one of these layouts:")
        for root in CUSTOM_CANDIDATES:
            print(f"  - {root.relative_to(ROOT)}/brainrots/<name>/front.png")
        return

    print("Sprite drop-in roots:")
    for root in roots:
        print(f"  - {root.relative_to(ROOT)}")

    copied_dests: set[Path] = set()
    copied = apply_roan(copied_dests) + apply_brainrots(copied_dests)
    if copied == 0:
        print("No custom sprite drop-in files matched known Brainrot slots yet.")
    else:
        print(f"Applied {copied} custom sprite drop-in file(s).")


if __name__ == "__main__":
    main()
