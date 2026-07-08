#!/usr/bin/env python3
"""Copy optional custom PNG/palette drop-ins into the FireRed graphics tree.

This lets the project accept new Roan and Brainrot sprites without manually
hunting every destination path.

Recommended layout:

    custom_sprites/brainrots/noobini/front.png

But the script also auto-detects nested or renamed upload folders, like:

    custom_sprites/custom_sprites/brainrots/noobini/front.png
    BrainrotImages/brainrots/noobini/front.png
    anything_else/brainrots/noobini/front.png

It also accepts sprite ZIP uploads committed into the repo, like:

    brainrot_lote1_custom_sprites_gba_ready.zip
    custom_sprite_zips/brainrot_lote2.zip
    custom_sprites/brainrot_lote3.zip

Missing files are skipped, so the playtest can still build while art is WIP.
"""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED_ZIP_ROOT = ROOT / "generated_custom_sprites_from_zips"

# Do not scan heavy/source folders when looking for uploaded art folders.
SKIP_DIRS = {
    ".git",
    ".github",
    "agbcc",
    "asm",
    "build",
    "charmap.txt",
    "constants",
    "data",
    "docs",
    "graphics",
    "include",
    "sound",
    "src",
    "sym_bss.txt",
    "sym_common.txt",
    "tools",
}

ZIP_NAME_HINTS = ("brainrot", "sprite", "sprites", "custom", "lote", "gba")


def normalize_name(name: str) -> str:
    """Normalize folder names so Noobini, noobini, noobini_front all match better."""
    lowered = name.lower()
    return "".join(ch for ch in lowered if ch.isalnum())


def is_relevant_zip(path: Path) -> bool:
    lowered = path.name.lower()
    return path.suffix.lower() == ".zip" and any(hint in lowered for hint in ZIP_NAME_HINTS)


def is_safe_zip_member(name: str) -> bool:
    target = Path(name)
    if target.is_absolute():
        return False
    return ".." not in target.parts


def discover_sprite_zips() -> list[Path]:
    """Find likely sprite ZIPs without walking the full source tree."""
    candidates: list[Path] = []

    for item in ROOT.iterdir():
        if item.is_file() and is_relevant_zip(item):
            candidates.append(item)
        elif item.is_dir() and not should_skip_dir(item):
            for child in item.iterdir():
                if child.is_file() and is_relevant_zip(child):
                    candidates.append(child)

    return sorted(set(candidates), key=lambda p: str(p).lower())


def extract_sprite_zips() -> int:
    zips = discover_sprite_zips()
    if not zips:
        return 0

    if GENERATED_ZIP_ROOT.exists():
        shutil.rmtree(GENERATED_ZIP_ROOT)
    GENERATED_ZIP_ROOT.mkdir(parents=True, exist_ok=True)

    extracted = 0
    print("Sprite ZIPs found:")
    for zip_path in zips:
        out_dir = GENERATED_ZIP_ROOT / zip_path.stem
        out_dir.mkdir(parents=True, exist_ok=True)
        print(f"  - {zip_path.relative_to(ROOT)}")

        with zipfile.ZipFile(zip_path) as zf:
            for member in zf.infolist():
                if member.is_dir():
                    continue
                if not is_safe_zip_member(member.filename):
                    print(f"skipped unsafe zip member: {member.filename}")
                    continue

                target = out_dir / member.filename
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(member) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
                extracted += 1

    print(f"Extracted {extracted} file(s) from sprite ZIP(s).")
    return extracted


def copy_if_exists(src: Path, dst: Path, copied_dests: set[Path]) -> bool:
    if not src.exists():
        return False
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

# Brainrot folder name -> original Pokemon graphics folder.
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

NORMALIZED_BRAINROT_FOLDERS = {
    normalize_name(name): folder for name, folder in BRAINROT_FOLDERS.items()
}

SPRITE_KINDS = ("front.png", "back.png", "icon.png", "normal.pal", "shiny.pal")


def should_skip_dir(path: Path) -> bool:
    return path.name in SKIP_DIRS or path.name.startswith(".")


def discover_named_dirs(target_name: str) -> list[Path]:
    """Find dirs named target_name, without walking source/build folders."""
    found: list[Path] = []
    stack = [p for p in ROOT.iterdir() if p.is_dir() and not should_skip_dir(p)]

    while stack:
        current = stack.pop()
        if current.name == target_name:
            found.append(current)
            # Do not need to scan inside brainrots/roan dirs.
            continue
        try:
            children = list(current.iterdir())
        except OSError:
            continue
        for child in children:
            if child.is_dir() and not should_skip_dir(child):
                stack.append(child)
    return sorted(found, key=lambda p: len(p.parts))


def discover_roan_roots() -> list[Path]:
    return [path.parent for path in discover_named_dirs("roan")]


def discover_brainrots_dirs() -> list[Path]:
    return discover_named_dirs("brainrots")


def apply_roan(copied_dests: set[Path]) -> int:
    copied = 0
    roan_roots = discover_roan_roots()
    for custom_root in roan_roots:
        for src_rel, dst_rel in ROAN_FILES.items():
            if copy_if_exists(custom_root / src_rel, ROOT / dst_rel, copied_dests):
                copied += 1
    return copied


def apply_brainrots(copied_dests: set[Path]) -> int:
    copied = 0
    brainrots_dirs = discover_brainrots_dirs()

    for brainrots_dir in brainrots_dirs:
        for brainrot_dir in sorted(p for p in brainrots_dir.iterdir() if p.is_dir()):
            key = normalize_name(brainrot_dir.name)
            pokemon_folder = NORMALIZED_BRAINROT_FOLDERS.get(key)
            if pokemon_folder is None:
                print(f"skipped unknown brainrot folder: {brainrot_dir.relative_to(ROOT)}")
                continue

            for filename in SPRITE_KINDS:
                src = brainrot_dir / filename
                dst = ROOT / "graphics" / "pokemon" / pokemon_folder / filename
                if copy_if_exists(src, dst, copied_dests):
                    copied += 1

    return copied


def main() -> None:
    extract_sprite_zips()

    brainrots_dirs = discover_brainrots_dirs()
    roan_roots = discover_roan_roots()

    if not brainrots_dirs and not roan_roots:
        print("No custom sprite drop-in folders found; vanilla/placeholder graphics remain.")
        print("Expected a folder like: custom_sprites/brainrots/<name>/front.png")
        print("Or a ZIP like: brainrot_lote1_custom_sprites_gba_ready.zip")
        return

    if brainrots_dirs:
        print("Brainrot sprite folders found:")
        for path in brainrots_dirs:
            print(f"  - {path.relative_to(ROOT)}")

    if roan_roots:
        print("Roan sprite roots found:")
        for path in roan_roots:
            print(f"  - {path.relative_to(ROOT)}")

    copied_dests: set[Path] = set()
    copied = apply_roan(copied_dests) + apply_brainrots(copied_dests)

    if copied == 0:
        print("No custom sprite drop-in files matched known Brainrot slots yet.")
    else:
        print(f"Applied {copied} custom sprite drop-in file(s).")


if __name__ == "__main__":
    main()
