# Brainrot Test Build Now

This is the quick way to test the current first playable Brainrot build.

## What is already in this test

- World dialogue changed to Brainrot lore.
- Early locations renamed in text.
- Avelar lab text.
- Roan/Kiunin style dialogue.
- Brainrot battle names for the first playable species.
- Starter stats adjusted.
- Early learnsets adjusted.
- Early evolutions adjusted.
- Route 1 wild encounters adjusted.
- Zone Green 01 wild encounters adjusted.
- Battle text changes from Pokemon wording to Brainrot wording.

Sprites are not changed yet.

## Windows

From the repo folder, run:

```bat
tools\build_brainrot_test.bat
```

If that does not work, use WSL/Ubuntu instead.

## WSL / Ubuntu

From the repo folder, run:

```bash
bash tools/build_brainrot_test.sh
```

or manually:

```bash
python3 tools/apply_brainrot_test_build.py
make
```

## Output

If the build works, open this file in mGBA:

```text
pokefirered.gba
```

## What to test first

1. Start a new game.
2. Check if early NPCs mention Brainrots, Cognia, Avelar, Kiunin, and the license system.
3. Pick a starter.
4. Enter battles and check if names like CHIMPANZI, CAPPUCINO, or TRALALERO show up.
5. Go to Route 1 and check if wild NOOBINI, PIPIKIWI, TIMCHEESE, and rare RACCOONI appear.
6. Go to Zone Green 01 and check if BAMBINI, LIRILI, CROSTINI, LARILA, and BRRBRR appear.

## What is not ready yet

- Sprites.
- Hospital prologue cutscene.
- Full Brainrot list across all routes.
- Final boss systems.
- Full custom maps.

## If the build fails

Copy the first error that appears after running the build command and send it back.
