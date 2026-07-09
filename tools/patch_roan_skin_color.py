#!/usr/bin/env python3
"""Force Roan/player skin colors away from accidental blue palettes.

Some player palettes are separate from the outfit palette, so changing Red's
clothes is not enough. This pass only touches likely player/Roan assets and
turns common accidental blue/cyan skin tones into natural GBA skin shades.
It is best-effort and build-safe.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LIKELY_PLAYER_PATH_WORDS = (
    "red",
    "player",
    "hero",
    "boy",
    "brendan",
    "roan",
    "back_pic",
    "backpic",
    "trainer_red",
)

# Blue/cyan rows that came from earlier recolor attempts or palette drift.
# They are mapped to simple FireRed/GBA skin ramps.
PAL_SWAPS = {
    "16 24 56": "88 48 32",
    "24 32 64": "120 72 48",
    "32 48 88": "160 96 64",
    "40 56 104": "192 128 88",
    "48 72 128": "224 160 112",
    "64 96 160": "240 184 136",
    "88 120 184": "248 200 152",
    "104 144 216": "248 216 176",
    "120 160 224": "248 224 192",
    "128 184 248": "248 224 192",
    "64 160 224": "240 184 136",
    "80 176 240": "248 200 152",
}


def is_likely_player_asset(path: Path) -> bool:
    low = path.as_posix().lower()
    return any(word in low for word in LIKELY_PLAYER_PATH_WORDS)


def patch_pal_file(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False

    original = text
    for old, new in PAL_SWAPS.items():
        text = text.replace(old, new)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"fixed Roan skin palette rows: {path.relative_to(ROOT)}")
        return True
    return False


def nearest_skin_for_blue(r: int, g: int, b: int) -> tuple[int, int, int] | None:
    # Only obvious accidental blue/cyan colors. Do not touch dark outlines,
    # normal black/gray, or tiny blue UI details.
    if b < 80:
        return None
    if b <= r + 35 or b <= g + 20:
        return None
    if r < 20 and g < 20 and b < 90:
        return None

    brightness = (r + g + b) // 3
    if brightness < 70:
        return (88, 48, 32)
    if brightness < 105:
        return (144, 88, 56)
    if brightness < 145:
        return (192, 128, 88)
    if brightness < 185:
        return (224, 160, 112)
    return (248, 200, 152)


def patch_png_file(path: Path) -> bool:
    try:
        from PIL import Image
    except ImportError:
        print("warning: Pillow missing; PNG Roan skin fix skipped.")
        return False

    try:
        img = Image.open(path)
    except Exception:
        return False

    rgba = img.convert("RGBA")
    pixels = rgba.load()
    changed = 0

    for y in range(rgba.height):
        for x in range(rgba.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            skin = nearest_skin_for_blue(r, g, b)
            if skin is None:
                continue
            pixels[x, y] = (*skin, a)
            changed += 1

    if changed == 0:
        return False

    # Preserve indexed PNGs when possible because gbagfx prefers paletted input.
    if img.mode == "P":
        indexed = rgba.convert("RGB").quantize(colors=16, method=Image.Quantize.MEDIANCUT)
        indexed.save(path)
    else:
        rgba.save(path)

    print(f"fixed Roan blue skin pixels: {path.relative_to(ROOT)} ({changed} px)")
    return True


def main() -> None:
    changed = 0
    scanned = 0

    for path in ROOT.glob("graphics/**/*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".pal", ".png"}:
            continue
        if not is_likely_player_asset(path):
            continue
        scanned += 1
        if path.suffix.lower() == ".pal":
            changed += int(patch_pal_file(path))
        else:
            changed += int(patch_png_file(path))

    print(f"Roan skin color pass complete: {changed} file(s) changed, {scanned} likely player asset(s) scanned.")


if __name__ == "__main__":
    main()
