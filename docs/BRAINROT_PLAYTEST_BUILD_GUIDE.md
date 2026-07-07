# Brainrot playtest build guide

This guide explains how to download and test the game.

## Important status

Right now, many Brainrot changes are still saved as design docs and patch docs.

That means:

```txt
If you build the repo right now, most of the game may still look like normal FireRed.
```

To make the Brainrot version playable, the patches need to be applied into the real source files.

## Easy download

Go to the GitHub repo:

```txt
Filhodoraot/Pokemon-Brainrot-Echoes-of-Sahur
```

Then:

```txt
Code -> Download ZIP
```

This only downloads the project files.

It does not automatically give you a playable GBA ROM.

## Better download with Git

Open terminal in the folder where you want the project and run:

```bash
git clone https://github.com/Filhodoraot/Pokemon-Brainrot-Echoes-of-Sahur.git
cd Pokemon-Brainrot-Echoes-of-Sahur
```

## Build tools needed

This project is based on pret/pokefirered.

To build the ROM, you need the build tools listed in `INSTALL.md`.

On Windows, the recommended option is WSL1/Ubuntu.

Install packages in Ubuntu/WSL:

```bash
sudo apt update && sudo apt upgrade
sudo apt install build-essential binutils-arm-none-eabi git libpng-dev
```

## agbcc setup

The project needs agbcc.

Go to the folder that contains the Brainrot repo and run:

```bash
git clone https://github.com/pret/agbcc
cd agbcc
./build.sh
./install.sh ../Pokemon-Brainrot-Echoes-of-Sahur
cd ../Pokemon-Brainrot-Echoes-of-Sahur
```

## Build the ROM

Inside the repo folder, run:

```bash
make
```

If it works, the output should be:

```txt
pokefirered.gba
```

## Test the ROM

Open `pokefirered.gba` in a GBA emulator.

Recommended easy emulators:

```txt
mGBA
VisualBoyAdvance-M
```

## What to test first

When Brainrot patches start being applied to real source files, test in this order:

1. New game starts.
2. ROAN name appears.
3. KIUNIN rival appears.
4. Starter names are changed.
5. Route 1 becomes Test Zone 01.
6. Wild encounters show NOOBINI/PIPIKIWI/TIMCHEESE/RACCOONI.
7. Viridian Forest text becomes Zone Green 01.
8. Game does not crash when entering forest.

## Current priority

Before serious playtesting, apply these real patches:

```txt
src/oak_speech.c
src/data/text/species_names.h
src/data/pokemon/evolution.h
src/data/pokemon/level_up_learnsets.h
src/data/wild_encounters.json
data/maps/PalletTown/text.inc
data/maps/Route1/text.inc
data/maps/ViridianForest/text.inc
```

## Safe rule

Do not change map ids yet.

Keep:

```txt
MAP_PALLET_TOWN
MAP_ROUTE1
MAP_VIRIDIAN_CITY
MAP_VIRIDIAN_FOREST
```

Only change text, names, encounters, evolutions, and learnsets first.
