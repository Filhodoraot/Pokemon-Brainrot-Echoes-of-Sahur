#!/usr/bin/env python3
"""Import Roan player sprites from a ZIP/folder when present.

Accepted upload options:
- roan_sprites_rgba.zip with sprite_01.png ... sprite_18.png
- roan_sprite_pack.zip with large_sprite_01.png ... large_sprite_18.png
- roan_sprites_rgba/ or roan_sprite_pack/ folders

This importer is best-effort and build-safe.
"""

from __future__ import annotations

import math
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


def quantized_colors_for_opaque_pixels(rgba: Image.Image, max_colors: int = 15) -> list[tuple[int, int, int]]:
    colors: list[tuple[int, int, int]] = []
    pix = rgba.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = pix[x, y]
            if a == 0:
                continue
            colors.append((r, g, b))

    if not colors:
        return []

    strip = Image.new("RGB", (len(colors), 1))
    strip.putdata(colors)
    q = strip.quantize(colors=max_colors, method=Image.Quantize.MEDIANCUT)
    palette = q.getpalette() or []
    used = sorted(set(q.getdata()))
    out: list[tuple[int, int, int]] = []
    for idx in used[:max_colors]:
        base = idx * 3
        out.append((palette[base], palette[base + 1], palette[base + 2]))
    return out


def nearest_palette_index(rgb: tuple[int, int, int], palette: list[tuple[int, int, int]]) -> int:
    r, g, b = rgb
    best_i = 1
    best_dist = 10**9
    for i, (pr, pg, pb) in enumerate(palette, start=1):
        dist = (r - pr) ** 2 + (g - pg) ** 2 + (b - pb) ** 2
        if dist < best_dist:
            best_dist = dist
            best_i = i
    return best_i


def save_indexed(img: Image.Image, path: Path) -> None:
    """Save GBA-safe indexed PNG with transparent/background pixels at palette index 0.

    The old version let PIL choose palette slot 0. In FireRed/GBA that slot is
    treated as transparent, so if PIL made blue index 0 the whole sprite got a
    blue rectangle. This version reserves slot 0 on purpose.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    rgba = img.convert("RGBA")
    colors = quantized_colors_for_opaque_pixels(rgba, 15)

    paletted = Image.new("P", rgba.size, 0)
    palette_values: list[int] = [255, 0, 255]  # transparent key color at index 0
    for r, g, b in colors:
        palette_values.extend([r, g, b])
    while len(palette_values) < 256 * 3:
        palette_values.extend([0, 0, 0])
    paletted.putpalette(palette_values[: 256 * 3])

    src = rgba.load()
    dst = paletted.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = src[x, y]
            if a == 0:
                dst[x, y] = 0
            elif colors:
                dst[x, y] = nearest_palette_index((r, g, b), colors)
            else:
                dst[x, y] = 0

    paletted.save(path)


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
