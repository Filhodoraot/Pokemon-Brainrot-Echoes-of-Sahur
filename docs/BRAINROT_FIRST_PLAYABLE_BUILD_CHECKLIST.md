# First playable Brainrot build checklist

This is the order to apply patches so the game starts showing Brainrot changes fast.

## Goal of first playable build

Make the first 15 minutes of the ROM feel like Brainrot: Echoes of Sahur.

No custom sprites yet.

## What should be visible in-game

- Player can use ROAN as default name.
- Rival can use KIUNIN as default name.
- Roan's house mentions Luna.
- Pallet Town becomes Training Center 01.
- Oak becomes Dr. Avelar in visible dialogue.
- Lab scene talks about Brainrots.
- Starters are described as Tralalero, Chimpanzini, and Cappuccino.
- Route 1 becomes Test Zone 01.
- Viridian becomes Viridian Safe Zone.
- Species names show early Brainrot names.

## Apply order

### 1. New game intro code

Patch source:

`docs/BRAINROT_NEW_GAME_CODE_PATCH.md`

Real file:

`src/oak_speech.c`

This gives:

- ROAN default name
- KIUNIN default rival name
- intro species changed to Squirtle slot / Tralalero placeholder

### 2. Species names

Patch source:

`docs/BRAINROT_SPECIES_NAME_PATCH_V1.md`

Real file:

`src/data/text/species_names.h`

This gives visible battle/species names:

- CHIMPANZI
- CAPPUCINO
- TRALALERO
- PIPIKIWI
- NOOBINI
- TIMCHEESE
- RACCOONI

### 3. Roan house text

Patch source:

`docs/BRAINROT_ROAN_HOUSE_TEXT_PATCH.md`

Real files:

`data/maps/PalletTown_PlayersHouse_1F/text.inc`
`data/maps/PalletTown_PlayersHouse_2F/text.inc`

This adds:

- Luna hint
- Mom forgetting Luna
- Cognia TV hint

### 4. Pallet / Training Center 01 text

Patch source:

`docs/BRAINROT_EARLY_TEXT_PATCHES.md`

Real file:

`data/maps/PalletTown/text.inc`

This adds:

- Training Center 01
- Avelar warning Roan
- Brainrot Ball
- Braindex

### 5. Avelar lab text

Patch source:

`docs/BRAINROT_LAB_TEXT_FULL_PATCH.md`

Real file:

`data/maps/PalletTown_ProfessorOaksLab/text.inc`

This adds:

- Avelar lab scene
- Brainrot starter choice dialogue
- Roan and Kiunin rivalry tone

### 6. Route 1 / Test Zone 01 text

Patch source:

`docs/BRAINROT_ROUTE1_TEST_ZONE_PATCH.md`

Real file:

`data/maps/Route1/text.inc`

This adds:

- Test Zone 01 sign
- supply desk NPC
- Brainrot Ball mention

### 7. Viridian Safe Zone text

Patch source:

`docs/BRAINROT_VIRIDIAN_SAFE_ZONE_TEXT_PATCH.md`

Real file:

`data/maps/ViridianCity/text.inc`

This adds:

- Viridian Safe Zone
- License Center
- Brainrot capture tutorial text
- Cognia hints

## First compile test

After applying only these patches, compile.

Do not touch sprites yet.

Test these moments:

1. New game intro opens.
2. ROAN appears as name option.
3. KIUNIN appears as rival name option.
4. Player starts in bedroom.
5. TV/NES text works.
6. Mom text works.
7. Avelar stops player before grass.
8. Lab starter scene works.
9. Rival battle starts.
10. Route 1 NPCs talk.
11. Viridian old man tutorial still works.

## If something breaks

Most likely causes:

- missing `$` at end of text
- typo in label name
- text line too weird for GBA charset
- accent used by accident
- copied Markdown code fence into `.inc` file

Do not paste the triple backticks into code files.

Only paste the C/text block inside the code fence.

## Not included yet

- custom sprites
- actual wild encounter table edits
- new moves
- new abilities
- new maps
- new event cutscenes

Those come after the first build compiles.
