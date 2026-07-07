# Brainrot Windows Build Without Ubuntu

This guide is for testing on Windows without installing Ubuntu or WSL.

This uses the modern compiler path from the Makefile, so the output name is:

```text
pokefirered_modern.gba
```

It is for playtesting, not checksum-perfect matching.

## You need

1. Python 3 installed.
2. devkitPro/devkitARM installed.
3. mGBA installed.
4. This repository downloaded or updated.

## Important

When installing Python, enable:

```text
Add Python to PATH
```

For devkitPro, use the normal Windows installer and make sure devkitARM is installed.

## Build

Open the devkitPro/MSYS2 shell if possible.

Go to the repo folder, then run:

```bat
tools\build_brainrot_windows_modern.bat
```

If double-clicking does not work, run it from the terminal.

## Output

Open this file in mGBA:

```text
pokefirered_modern.gba
```

## What this script does

It checks if these commands exist:

```text
python
make
arm-none-eabi-gcc
```

Then it runs:

```bat
python tools\apply_brainrot_test_build.py
python tools\patch_brainrot_trainers.py
make firered_modern
```

## If it fails

Copy the first error and send it back.

Common errors:

```text
python was not found
```

Install Python 3 and add it to PATH.

```text
make was not found
```

Open the devkitPro/MSYS2 shell, or install make.

```text
arm-none-eabi-gcc was not found
```

Install devkitPro/devkitARM, then reopen the terminal.

## What to test

1. Start new game.
2. Pick starter.
3. Check starter name in battle.
4. Go to Route 1.
5. Find NOOBINI, PIPIKIWI, TIMCHEESE, or RACCOONI.
6. Go to Zone Green 01.
7. Find BAMBINI, LIRILI, CROSTINI, LARILA, or BRRBRR.
8. Battle early trainers.

Sprites are not changed yet.
