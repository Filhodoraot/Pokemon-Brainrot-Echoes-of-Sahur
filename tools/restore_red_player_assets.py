#!/usr/bin/env python3
"""Restore vanilla Red/player graphics from an older safe commit.

This is a build-time safety net. Some older playtest patches recolored player
palettes and produced a blue Red. This script restores likely Red/player graphic
files from a pre-Roan safe commit, without touching Pokemon/Brainrot sprites.

It requires full git history in GitHub Actions checkout.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAFE_COMMIT = "9b3c0348c8d4efe7dc2320aa9fc8d0fe669d2825"

RESTORE_EXTS = {".png", ".pal"}
TRAINER_HINTS = ("red", "player", "hero", "boy", "brendan")
OBJECT_EVENT_HINTS = ("red", "player", "hero", "field_player")
PALETTE_HINTS = ("red", "player", "hero")


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=check)


def git_exists(ref: str) -> bool:
    result = run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"], check=False)
    return result.returncode == 0


def list_files(ref: str) -> list[str]:
    result = run(["git", "ls-tree", "-r", "--name-only", ref, "graphics"], check=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def is_restore_candidate(path: str) -> bool:
    low = path.lower()
    suffix = Path(path).suffix.lower()
    if suffix not in RESTORE_EXTS:
        return False
    if "graphics/pokemon/" in low:
        return False

    if low.startswith("graphics/trainers/"):
        return any(hint in low for hint in TRAINER_HINTS)

    if low.startswith("graphics/object_events/"):
        return any(hint in low for hint in OBJECT_EVENT_HINTS)

    if low.startswith("graphics/") and "palette" in low:
        return any(hint in low for hint in PALETTE_HINTS)

    return False


def main() -> None:
    if not git_exists(SAFE_COMMIT):
        print(f"warning: safe Red restore commit not available: {SAFE_COMMIT}")
        print("Run checkout with fetch-depth: 0. Skipping Red restore.")
        return

    files = [path for path in list_files(SAFE_COMMIT) if is_restore_candidate(path)]
    if not files:
        print("warning: no Red/player asset candidates found to restore.")
        return

    restored: list[str] = []
    for path in files:
        result = run(["git", "checkout", SAFE_COMMIT, "--", path], check=False)
        if result.returncode == 0:
            restored.append(path)
        else:
            print(f"warning: could not restore {path}: {result.stderr.strip()}")

    print(f"Red/player asset restore complete: {len(restored)} file(s) restored from {SAFE_COMMIT[:7]}.")
    for path in restored[:80]:
        print(f"  - {path}")
    if len(restored) > 80:
        print(f"  ...and {len(restored) - 80} more")


if __name__ == "__main__":
    main()
