#!/usr/bin/env python3
"""Force Roan/player colors away from accidental blue palettes.

The previous pass only looked for obvious names like red/player/hero. Some
FireRed player graphics live under generic object-event folders, so this pass
also scans likely player object-event and trainer back-pic areas.

Goal:
- no blue skin
- no full blue outfit/body
- keep the build safe by saving edited PNGs as indexed/paletted PNGs
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAME_HINTS = (
    "red",
    "player",
    "hero",
    "boy",
    "male",
    "brendan",
    "roan",
    "back_pic",
    "backpic",
    "trainer_red",
)

PATH_HINTS = (
    "graphics/object_events/pics/people",
    "graphics/object_events/pics/field_player",
    "graphics/object_events/pics/player",
    "graphics/trainers/back_pics",
    "graphics/trainers/front_pics/red",
    "graphics/trainers/front_pics/leaf",
    "graphics/trainers/front_pics/brendan",
)

# Palette rows. Dark/mid blues become Roan's dark outfit. Bright cyan-blue that
# often came from skin drift becomes natural GBA skin highlight.
PAL_SWAPS = {
    "8 16 48": "16 16 20",
    "16 24 56": "24 24 28",
    "24 32 64": "32 32 36",
    "32 48 88": "40 40 44",
    "40 56 104": "48 48 52",
    "48 72 128": "64 64 68",
    "64 96 160": "80 80 84",
    "88 120 184": "112 112 116",
    "104 144 216": "224 160 112",
    "120 160 224": "240 184 136",
    "128 184 248": "248 200 152",
    "64 160 224": "224 160 112",
    "80 176 240": "240 184 136",
}


def is_likely_player_asset(path: Path) -> bool:
    low = path.as_posix().lower()
    if any(hint in low for hint in PATH_HINTS):
        return True
    return any(word in low for word in NAME_HINTS)


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
        print(f"fixed Roan/player blue palette rows: {path.relative_to(ROOT)}")
        return True
    return False


def replacement_for_blue(r: int, g: int, b: int) -> tuple[int, int, int] | None:
    # Only obvious accidental blue/cyan. Avoid touching black outlines, gray,
    # or normal UI-ish colors.
    if b < 70:
        return None
    if b <= r + 35 or b <= g + 15:
        return None
    if r < 18 and g < 18 and b < 90:
        return None

    brightness = (r + g + b) // 3

    # Dark/mid blues are usually the accidental blue outfit/body from the bug.
    if brightness < 75:
        return (24, 24, 28)
    if brightness < 105:
        return (40, 40, 44)
    if brightness < 135:
        return (64, 64, 68)
    if brightness < 165:
        return (96, 96, 100)

    # Very bright cyan/blue highlights are more likely the skin/highlight drift.
    if brightness < 200:
        return (224, 160, 112)
    return (248, 200, 152)


def save_indexed_png(img, path: Path) -> None:
    # gbagfx is happier with indexed PNGs than accidental RGBA files.
    rgb = img.convert("RGB")
    indexed = rgb.quantize(colors=16, method=Image.Quantize.MEDIANCUT)
    indexed.save(path)


def patch_png_file(path: Path) -> bool:
    try:
        from PIL import Image as PILImage
    except ImportError:
        print("warning: Pillow missing; PNG Roan/player color fix skipped.")
        return False

    global Image
    Image = PILImage

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
            replacement = replacement_for_blue(r, g, b)
            if replacement is None:
                continue
            pixels[x, y] = (*replacement, a)
            changed += 1

    if changed == 0:
        return False

    save_indexed_png(rgba, path)
    print(f"fixed Roan/player blue pixels: {path.relative_to(ROOT)} ({changed} px)")
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
        # Do not touch Pokemon/Brainrot sprites here.
        if "graphics/pokemon/" in path.as_posix().lower():
            continue
        scanned += 1
        if path.suffix.lower() == ".pal":
            changed += int(patch_pal_file(path))
        else:
            changed += int(patch_png_file(path))

    print(f"Roan/player blue cleanup complete: {changed} file(s) changed, {scanned} likely player asset(s) scanned.")


if __name__ == "__main__":
    main()
