# Early map implementation patch V1

This file turns the first playable Kanto area into Brainrot Kanto using safe map edits.

## Goal

Make the beginning of the game feel custom without redrawing the entire world yet.

Use existing FireRed maps as the skeleton.

## Confirmed real files

### Training Center 01

Original map:

`data/maps/PalletTown/map.json`

Important fields:

```json
"id": "MAP_PALLET_TOWN",
"name": "PalletTown",
"layout": "LAYOUT_PALLET_TOWN",
"music": "MUS_PALLET",
"region_map_section": "MAPSEC_PALLET_TOWN",
"show_map_name": true
```

### Test Zone 01

Original map:

`data/maps/Route1/map.json`

Important fields:

```json
"id": "MAP_ROUTE1",
"name": "Route1",
"layout": "LAYOUT_ROUTE1",
"music": "MUS_ROUTE1",
"region_map_section": "MAPSEC_ROUTE_1",
"show_map_name": true
```

### Safe Zone 01

Original map:

`data/maps/ViridianCity/map.json`

Important fields:

```json
"id": "MAP_VIRIDIAN_CITY",
"name": "ViridianCity",
"layout": "LAYOUT_VIRIDIAN_CITY",
"music": "MUS_PEWTER",
"region_map_section": "MAPSEC_VIRIDIAN_CITY",
"show_map_name": true
```

## Safe naming plan

Do not change map ids yet.

Keep:

```txt
MAP_PALLET_TOWN
MAP_ROUTE1
MAP_VIRIDIAN_CITY
```

Why:

Changing ids can break scripts, warps, and constants.

Instead, change text, signs, NPC dialogue, region map names, and story labels first.

## Story names for early maps

| Original | Story name | Role |
|---|---|---|
| Pallet Town | Training Center 01 | start, Roan home, Avelar lab |
| Route 1 | Test Zone 01 | first wild Brainrots |
| Viridian City | Safe Zone 01 | first hub and safety rules |
| Viridian Forest | Zone Green 01 | first true dungeon |

## Early game flow

```txt
Roan wakes up
-> talks to Mom
-> leaves home
-> tries to enter Test Zone 01
-> Dr. Avelar stops him
-> goes to lab
-> chooses starter
-> Kiunin picks his starter
-> first Kiunin battle
-> Roan enters Test Zone 01
-> catches first wild Brainrot
-> reaches Safe Zone 01
-> learns Brainrot safety rules
-> enters Zone Green 01
-> finds first Sahur Fragment
```

## Pallet Town / Training Center 01 tasks

### Keep map structure

Do not edit layout yet.

Use the existing houses and lab.

### Rename through dialogue

Change NPCs and signs to call it:

```txt
Training Center 01
```

### Player house role

Roan's house.

Mom should talk about:

- Roan still searching for Luna
- people saying Luna never existed
- Roan going to Avelar's lab
- warning about Brainrots

### Rival house role

Kiunin's temporary residence or Cognia guest house.

Possible story use:

```txt
Kiunin is staying near Training Center 01 because his father has Cognia connections.
```

### Lab role

Dr. Avelar's Brainrot lab.

Starter scene:

- CHIMPANZI
- CAPPUCINO
- TRALALERO

## Route 1 / Test Zone 01 tasks

### Keep route shape

Use existing Route 1.

### Change wild encounters

Main Brainrots:

```txt
NOOBINI
PIPIKIWI
TIMCHEESE
RACCOONI rare
```

### NPC 1: Mart Clerk replacement

Original object:

```txt
Route1_EventScript_MartClerk
```

New role:

```txt
Training assistant
```

Gives Potion, but calls it test kit support.

Possible text:

```txt
You are entering Test Zone 01.
Keep your Brainrot calm.
Here, take this POTION.
```

### NPC 2: Boy replacement

Original object:

```txt
Route1_EventScript_Boy
```

New role:

```txt
young candidate
```

Possible text:

```txt
Noobini copies voices.
If it repeats you too much,
walk away slowly.
```

### Sign text

Original object:

```txt
Route1_EventScript_RouteSign
```

New sign:

```txt
TEST ZONE 01
Wild Brainrot behavior area.
License E candidates only.
```

## Viridian City / Safe Zone 01 tasks

### Keep map shape

Use the existing city.

### Rename through signs and NPCs

Call it:

```txt
Safe Zone 01
```

### Old Man tutorial role

Original object:

```txt
ViridianCity_EventScript_OldMan
```

New role:

```txt
retired Brainrot handler
```

Purpose:

- teaches capture
- explains Brainrot Balls
- says weak minds should not stare at wild Brainrots too long

### Tutorial Man role

Original object:

```txt
ViridianCity_EventScript_TutorialOldMan
```

New role:

```txt
Safe Zone guide
```

Purpose:

- teaches basic license system
- tells Roan about Zone Green 01

## Region map names

Later, find the region map section text file and change displayed names:

```txt
PALLET TOWN -> TRAINING 01
ROUTE 1 -> TEST ZONE 01
VIRIDIAN CITY -> SAFE ZONE 01
VIRIDIAN FOREST -> ZONE GREEN 01
```

If the name limit is small, use short versions:

```txt
TRAINING 01
TEST ZONE 01
SAFE ZONE 01
GREEN 01
```

## Music plan

For first build, keep music unchanged.

Later:

| Area | Music idea |
|---|---|
| Training Center 01 | calm but weird |
| Test Zone 01 | route theme with tension |
| Safe Zone 01 | safe city theme |
| Zone Green 01 | forest + low Sahur pulse |

## Visual plan

Do not redraw early.

Small visual edits later:

### Training Center 01

- add warning signs
- make lab feel more research-like
- add test-center objects

### Test Zone 01

- add fences
- warning signs
- maybe broken observation devices

### Safe Zone 01

- add safety posters
- guards near exits
- Cognia notices

### Zone Green 01

- darker forest
- cult signs
- Sahur sound markers

## First playable patch order

1. Dialogue/text changes.
2. Starter names/stats/learnsets.
3. Route 1 wild encounters.
4. Route 1 NPC text.
5. Viridian/Safe Zone NPC text.
6. Forest/Zone Green text.
7. Region map names.
8. Visual map edits later.

## Build safety note

Do not change these yet:

```txt
map id
layout id
connection map ids
warp destination ids
```

Changing those early can break the game.

For now, change story through text and encounters.
