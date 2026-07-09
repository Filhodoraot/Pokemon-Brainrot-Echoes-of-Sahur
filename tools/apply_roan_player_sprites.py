#!/usr/bin/env python3
"""Import Roan player sprites from a ZIP/folder when present.

Accepted upload options:
- roan_sprites_rgba.zip with sprite_01.png ... sprite_18.png
- roan_sprite_pack.zip with large_sprite_01.png ... large_sprite_18.png
- roan_sprites_rgba/ or roan_sprite_pack/ folders

This importer is best-effort and build-safe.
"""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZIP_CANDIDATES = [
    ROOT / "roan_sprite_pack.zip",
    ROOT / "roan_sprites_rgba.zip",
    ROOT / "custom_player_sprites" / "roan_sprite_pack.zip",
    ROOT / "custom_player_sprites" / "roan_sprites_rgba.zip",
]
DIR_CANDIDATES = [
    ROOT / "roan_sprite_pack",
    ROOT / "roan_sprites_rgba",
    ROOT / "custom_player_sprites" / "roan_sprite_pack",
    ROOT / "custom_player_sprites" / "roan_sprites_rgba",
]
PREPARED = ROOT / "custom_player_sprites" / "roan_prepared"

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Pillow is required for Roan sprite import.") from exc


def folder_has_sprites(folder: Path) -> bool:
    return any(folder.glob("sprite_*.png")) or any(folder.glob("large_sprite_*.png"))


def find_source_dir() -> Path | None:
    for folder in DIR_CANDIDATES:
        if folder.exists() and folder_has_sprites(folder):
            return folder

    for zip_path in ZIP_CANDIDATES:
        if zip_path.exists():
            out = ROOT / "generated_roan_sprites_from_zip"
            if out.exists():
                shutil.rmtree(out)
            out.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(out)
            if folder_has_sprites(out):
                return out
            for folder in out.rglob("*"):
                if folder.is_dir() and folder_has_sprites(folder):
                    return folder
    return None


def rgba_without_checkerboard(path: Path) -> Image.Image:
    img = Image.open(path).convert("RGBA")
    pix = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pix[x, y]
            if a == 0:
                continue
            mx = max(r, g, b)
            mn = min(r, g, b)
            mean = (r + g + b) / 3
            if mx - mn <= 18 and mean >= 205:
                pix[x, y] = (0, 0, 0, 0)
    return img


def fit_canvas(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    alpha = img.getchannel("A")
    bbox = alpha.getbbox()
    if bbox:
        img = img.crop(bbox)
    if img.width == 0 or img.height == 0:
        return Image.new("RGBA", size, (0, 0, 0, 0))
    scale = min(target_w / img.width, target_h / img.height)
    new_w = max(1, min(target_w, int(round(img.width * scale))))
    new_h = max(1, min(target_h, int(round(img.height * scale))))
    img = img.resize((new_w, new_h), Image.Resampling.NEAREST)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.alpha_composite(img, ((target_w - new_w) // 2, target_h - new_h))
    return out


def save_indexed(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rgba = img.convert("RGBA")
    flat = Image.new("RGB", rgba.size, (255, 0, 255))
    flat.paste(rgba, mask=rgba.getchannel("A"))
    indexed = flat.quantize(colors=16, method=Image.Quantize.MEDIANCUT)
    indexed.save(path)


def sprite_path(source: Path, num: int) -> Path:
    options = [
        source / f"sprite_{num:02d}.png",
        source / f"large_sprite_{num:02d}.png",
    ]
    for path in options:
        if path.exists():
            return path
    raise FileNotFoundError(f"missing Roan sprite #{num:02d} in {source}")


def load_sprite(source: Path, num: int) -> Image.Image:
    return rgba_without_checkerboard(sprite_path(source, num))


def build_overworld_sheet(source: Path) -> Image.Image:
    # Current generated pack order:
    # 01-04 = back/up, 05-08 = front/down, 09-12 = side A, 13-16 = side B.
    # 17/18 = trainer front/back in many packs, but old packs may use 05/14.
    rows = [
        [5, 6, 7, 8],       # down/front
        [1, 2, 3, 4],       # up/back
        [9, 10, 11, 12],    # side
        [13, 14, 15, 16],   # opposite side
    ]
    sheet = Image.new("RGBA", (32 * 4, 32 * 4), (0, 0, 0, 0))
    for row_i, row in enumerate(rows):
        for col_i, sprite_num in enumerate(row):
            frame = fit_canvas(load_sprite(source, sprite_num), (32, 32))
            sheet.alpha_composite(frame, (col_i * 32, row_i * 32))
    return sheet


def pick_existing_sprite(source: Path, preferred: list[int]) -> int:
    for num in preferred:
        try:
            sprite_path(source, num)
            return num
        except FileNotFoundError:
            pass
    raise FileNotFoundError(f"none of these Roan sprites exist: {preferred}")


def build_battle_sprite(source: Path, preferred_nums: list[int], size: tuple[int, int]) -> Image.Image:
    num = pick_existing_sprite(source, preferred_nums)
    return fit_canvas(load_sprite(source, num), size)


def copy_if_path_exists(src: Path, candidates: list[str]) -> list[str]:
    changed: list[str] = []
    for candidate in candidates:
        dest = ROOT / candidate
        if dest.exists():
            shutil.copyfile(src, dest)
            changed.append(candidate)
    return changed


def main() -> None:
    source = find_source_dir()
    if source is None:
        print("Roan sprite ZIP/folder not found. Skipping Roan sprite import.")
        return

    PREPARED.mkdir(parents=True, exist_ok=True)

    overworld = build_overworld_sheet(source)
    trainer_front = build_battle_sprite(source, [17, 5], (64, 64))
    trainer_back = build_battle_sprite(source, [18, 14], (64, 64))

    prepared_overworld = PREPARED / "roan_overworld.png"
    prepared_front = PREPARED / "roan_trainer_front.png"
    prepared_back = PREPARED / "roan_trainer_back.png"

    save_indexed(overworld, prepared_overworld)
    save_indexed(trainer_front, prepared_front)
    save_indexed(trainer_back, prepared_back)

    changed: list[str] = []
    changed += copy_if_path_exists(prepared_overworld, [
        "graphics/object_events/pics/people/red/normal.png",
        "graphics/object_events/pics/people/boy/normal.png",
        "graphics/object_events/pics/people/player/normal.png",
        "graphics/object_events/pics/field_player/boy/normal.png",
        "graphics/object_events/pics/field_player/red/normal.png",
    ])
    changed += copy_if_path_exists(prepared_front, [
        "graphics/trainers/front_pics/red.png",
        "graphics/trainers/front_pics/boy.png",
        "graphics/trainers/front_pics/player.png",
    ])
    changed += copy_if_path_exists(prepared_back, [
        "graphics/trainers/back_pics/red.png",
        "graphics/trainers/back_pics/boy.png",
        "graphics/trainers/back_pics/player.png",
    ])

    print(f"Roan sprite import source: {source.relative_to(ROOT)}")
    print(f"Prepared files written to: {PREPARED.relative_to(ROOT)}")
    if changed:
        print("Applied Roan sprites to existing game paths:")
        for path in changed:
            print(f"  - {path}")
    else:
        print("No known player graphic paths existed, so prepared files were saved only.")
        print("Build will continue; map these prepared files after we confirm repo paths.")


if __name__ == "__main__":
    main()
