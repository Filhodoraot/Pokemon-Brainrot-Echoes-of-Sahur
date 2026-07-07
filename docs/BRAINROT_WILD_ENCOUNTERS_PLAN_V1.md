# Wild encounters plan V1

Goal: make the first wild area feel like Brainrot: Echoes of Sahur.

## First target area

Route 1 becomes:

`TEST ZONE 01`

This is the first controlled field test for new Brainrot trainers.

## First Route 1 encounter set

| Brainrot | Level | Rarity | Original slot idea |
|---|---:|---|---|
| Pipi Kiwi | 2-4 | common | Rattata |
| Noobini Pizzanini | 2-4 | common | Pidgey |
| Tim Cheese | 3-5 | uncommon | Spearow |
| Raccooni Jandelini | 4-5 | rare | Fearow or another early slot |

## Safer temporary mapping

Use existing species slots first:

```txt
SPECIES_RATTATA  -> PIPIKIWI
SPECIES_PIDGEY   -> NOOBINI
SPECIES_SPEAROW  -> TIMCHEESE
SPECIES_FEAROW   -> RACCOONI
```

Why:
- no new species table expansion yet
- no new graphics table yet
- less chance to break compile

## Ideal Route 1 encounter table

Pseudo-table:

```c
Route1 land encounters:
- level 2 PIPIKIWI
- level 2 NOOBINI
- level 3 PIPIKIWI
- level 3 NOOBINI
- level 3 TIMCHEESE
- level 4 PIPIKIWI
- level 4 NOOBINI
- level 4 TIMCHEESE
- level 5 RACCOONI
- level 5 RACCOONI
```

## Story flavor

Route 1 is not a normal road anymore.

People call it safe, but it is only safe because Cognia controls the data and hides failed tests.

Wild Brainrots here are weak, but they still affect attention and memory.

NPC vibe:

- Adults treat this as normal.
- Kids repeat Brainrot names without thinking.
- Roan feels something is wrong.
- Avelar watches because Roan may have Cognitive Resistance.

## Next areas

### Viridian City

Role: first safe zone.

Text themes:
- people talk about Brainrot licenses
- shop sells Brainrot Balls
- old man tutorial becomes capture instructor
- first hint that kids are repeating words again

### Viridian Forest / Zone Green 01

Encounter ideas:
- Brr Brr Patapim
- Bandito Bobritto
- Boneca Ambalabu
- Trippi Troppi
- Pipi Avocado

Story boss:
- Tree Tree Tree Sahur or Brr Brr Patapim Alpha

## Need to locate exact wild encounter file

The usual file in some FireRed decomps may be one of these:

```txt
src/data/wild_encounters.h
data/wild_encounters.h
src/data/pokemon/wild_encounters.h
data/wild_encounters.json
```

In this repo, `data/wild_encounters.json` was not found, so we need to inspect the project structure more before editing real encounter data.

## Build safety

First change only text and species names.

Then change encounters.

Then compile.
