#!/usr/bin/env python3
"""Normalize custom Brainrot sprite PNG sizes before the GBA build.

The GBA menu icon format is strict:
- front.png: 64x64
- back.png: 64x64
- icon.png: 32x64, made of two 32x32 frames stacked vertically

If an uploaded icon is larger or malformed, it can overflow/corrupt VRAM and show
huge glitchy icons in battle or party menus. This script repairs the copied PNGs
inside graphics/pokemon after custom sprite drop-ins run.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POKEMON_DIR = ROOT / "graphics" / "pokemon"

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - build workflow installs pillow
    raise SystemExit("Pillow is required. Install python3-pil before running this script.") from exc


def alpha_bbox(img: Image.Image):
    rgba = img.convert("RGBA")
    alpha = rgba.getchannel("A")
    return alpha.getbbox()


def fit_nearest(src: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Fit visible pixels into a transparent canvas without smoothing."""
    target_w, target_h = size
    rgba = src.convert("RGBA")
    bbox = alpha_bbox(rgba)
    if bbox:
        rgba = rgba.crop(bbox)

    if rgba.width == 0 or rgba.height == 0:
        return Image.new("RGBA", size, (0, 0, 0, 0))

    scale = min(target_w / rgba.width, target_h / rgba.height)
    new_w = max(1, min(target_w, int(round(rgba.width * scale))))
    new_h = max(1, min(target_h, int(round(rgba.height * scale))))
    resized = rgba.resize((new_w, new_h), Image.Resampling.NEAREST)

    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.alpha_composite(resized, ((target_w - new_w) // 2, (target_h - new_h) // 2))
    return out


def sanitize_front_back(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        img = Image.open(path)
    except Exception as exc:
        print(f"warning: could not read {path.relative_to(ROOT)}: {exc}")
        return False

    fixed = fit_nearest(img, (64, 64))
    if img.size != (64, 64) or img.mode != "RGBA":
        fixed.save(path)
        print(f"fixed battle sprite size: {path.relative_to(ROOT)} -> 64x64")
        return True
    return False


def sanitize_icon(path: Path, front_fallback: Path | None = None) -> bool:
    if path.exists():
        try:
            img = Image.open(path).convert("RGBA")
        except Exception as exc:
            print(f"warning: could not read icon {path.relative_to(ROOT)}: {exc}")
            img = None
    else:
        img = None

    changed = False
    if img is None and front_fallback is not None and front_fallback.exists():
        img = Image.open(front_fallback).convert("RGBA")
        changed = True

    if img is None:
        return False

    if img.size == (32, 64):
        frame1 = img.crop((0, 0, 32, 32))
        frame2 = img.crop((0, 32, 32, 64))
        # Re-save as clean RGBA to remove odd metadata/modes.
        fixed = Image.new("RGBA", (32, 64), (0, 0, 0, 0))
        fixed.alpha_composite(frame1, (0, 0))
        fixed.alpha_composite(frame2, (0, 32))
        if img.mode != "RGBA" or changed:
            fixed.save(path)
            print(f"cleaned icon sprite: {path.relative_to(ROOT)}")
            return True
        return False

    if img.size == (32, 32):
        frame = img
    else:
        frame = fit_nearest(img, (32, 32))

    fixed = Image.new("RGBA", (32, 64), (0, 0, 0, 0))
    fixed.alpha_composite(frame, (0, 0))
    fixed.alpha_composite(frame, (0, 32))
    fixed.save(path)
    print(f"fixed menu icon size: {path.relative_to(ROOT)} -> 32x64")
    return True


def main() -> None:
    changed = 0
    scanned = 0
    if not POKEMON_DIR.exists():
        raise SystemExit("graphics/pokemon was not found")

    for species_dir in sorted(p for p in POKEMON_DIR.iterdir() if p.is_dir()):
        scanned += 1
        front = species_dir / "front.png"
        back = species_dir / "back.png"
        icon = species_dir / "icon.png"
        changed += int(sanitize_front_back(front))
        changed += int(sanitize_front_back(back))
        changed += int(sanitize_icon(icon, front))

    print(f"Brainrot sprite size sanitizer complete: {changed} file(s) fixed across {scanned} species folder(s).")


if __name__ == "__main__":
    main()
