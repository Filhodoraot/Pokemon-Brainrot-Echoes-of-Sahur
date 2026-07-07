# Brainrot evolution patch V1

Target file:

`src/data/pokemon/evolution.h`

This patch uses existing evolution mechanics to represent:

```txt
Baby -> Teen -> Adult
```

No custom stage code is needed for the first build.

## Confirmed current structure

The file already has lines like:

```c
[SPECIES_BULBASAUR]  = {{EVO_LEVEL, 16, SPECIES_IVYSAUR}},
[SPECIES_IVYSAUR]    = {{EVO_LEVEL, 32, SPECIES_VENUSAUR}},
[SPECIES_CHARMANDER] = {{EVO_LEVEL, 16, SPECIES_CHARMELEON}},
[SPECIES_CHARMELEON] = {{EVO_LEVEL, 36, SPECIES_CHARIZARD}},
[SPECIES_SQUIRTLE]   = {{EVO_LEVEL, 16, SPECIES_WARTORTLE}},
[SPECIES_WARTORTLE]  = {{EVO_LEVEL, 36, SPECIES_BLASTOISE}},
[SPECIES_PIDGEY]     = {{EVO_LEVEL, 18, SPECIES_PIDGEOTTO}},
[SPECIES_PIDGEOTTO]  = {{EVO_LEVEL, 36, SPECIES_PIDGEOT}},
[SPECIES_RATTATA]    = {{EVO_LEVEL, 20, SPECIES_RATICATE}},
[SPECIES_SPEAROW]    = {{EVO_LEVEL, 20, SPECIES_FEAROW}},
```

## Design goal

Make early Brainrots evolve a little faster, so the player sees Baby -> Teen -> Adult in the first part of the game.

This makes the ROM feel custom before sprites are ready.

## Replace these evolution lines

### Starter lines

Replace:

```c
[SPECIES_BULBASAUR]  = {{EVO_LEVEL, 16, SPECIES_IVYSAUR}},
[SPECIES_IVYSAUR]    = {{EVO_LEVEL, 32, SPECIES_VENUSAUR}},
[SPECIES_CHARMANDER] = {{EVO_LEVEL, 16, SPECIES_CHARMELEON}},
[SPECIES_CHARMELEON] = {{EVO_LEVEL, 36, SPECIES_CHARIZARD}},
[SPECIES_SQUIRTLE]   = {{EVO_LEVEL, 16, SPECIES_WARTORTLE}},
[SPECIES_WARTORTLE]  = {{EVO_LEVEL, 36, SPECIES_BLASTOISE}},
```

With:

```c
[SPECIES_BULBASAUR]  = {{EVO_LEVEL, 14, SPECIES_IVYSAUR}},
[SPECIES_IVYSAUR]    = {{EVO_LEVEL, 30, SPECIES_VENUSAUR}},
[SPECIES_CHARMANDER] = {{EVO_LEVEL, 14, SPECIES_CHARMELEON}},
[SPECIES_CHARMELEON] = {{EVO_LEVEL, 30, SPECIES_CHARIZARD}},
[SPECIES_SQUIRTLE]   = {{EVO_LEVEL, 14, SPECIES_WARTORTLE}},
[SPECIES_WARTORTLE]  = {{EVO_LEVEL, 30, SPECIES_BLASTOISE}},
```

## Meaning

```txt
Level 14 = Baby -> Teen
Level 30 = Teen -> Adult
```

This is faster than normal starters, but not too fast.

## Route 1 Brainrot lines

Replace:

```c
[SPECIES_PIDGEY]     = {{EVO_LEVEL, 18, SPECIES_PIDGEOTTO}},
[SPECIES_PIDGEOTTO]  = {{EVO_LEVEL, 36, SPECIES_PIDGEOT}},
[SPECIES_RATTATA]    = {{EVO_LEVEL, 20, SPECIES_RATICATE}},
[SPECIES_SPEAROW]    = {{EVO_LEVEL, 20, SPECIES_FEAROW}},
```

With:

```c
[SPECIES_PIDGEY]     = {{EVO_LEVEL, 12, SPECIES_PIDGEOTTO}},
[SPECIES_PIDGEOTTO]  = {{EVO_LEVEL, 25, SPECIES_PIDGEOT}},
[SPECIES_RATTATA]    = {{EVO_LEVEL, 16, SPECIES_RATICATE}},
[SPECIES_SPEAROW]    = {{EVO_LEVEL, 18, SPECIES_FEAROW}},
```

## Meaning

| Slot | Brainrot | Stage path |
|---|---|---|
| Pidgey | Noobini | Baby -> Teen at 12 -> Adult at 25 |
| Rattata | Pipi Kiwi | Baby -> Adult at 16 |
| Spearow | Tim Cheese | Teen -> Adult/Raccooni at 18 |

## Why Pipi Kiwi has two stages first

Some Brainrots do not need a full 3-stage line in the first build.

Pipi Kiwi can start with:

```txt
PIPIKIWI Baby -> PIPICORNI Adult
```

Later, when we add more species slots, we can insert a Teen form.

## Why Tim Cheese evolves into Raccooni for now

This is temporary.

Because we are reusing old slots before adding new species, Spearow -> Fearow becomes:

```txt
TIMCHEESE -> RACCOONI
```

Later, when we have more custom species slots, Tim Cheese and Raccooni should become separate lines.

## First build evolution table

| Original line | Brainrot line | Baby | Teen | Adult |
|---|---|---|---|---|
| Bulbasaur line | Chimpanzini line | CHIMPANZI | BANANINI | AVOCADOR |
| Charmander line | Cappuccino line | CAPPUCINO | HARPUCINO | CAPASSINO |
| Squirtle line | Tralalero line | TRALALERO | TRALALITO | TRALALORD |
| Pidgey line | Noobini line | NOOBINI | PIZZANINI | LOSNOOBI |
| Rattata line | Pipi line | PIPIKIWI | none yet | PIPICORNI |
| Spearow line | temporary route line | TIMCHEESE | none yet | RACCOONI |

## Build safety

This patch only changes levels and destination species already in the game.

It should be safe.

Do not add new evolution methods yet.

## Later improvement

After first build works:

- add real Tim Cheese line
- add real Raccooni line
- add Pipi Kiwi Teen
- add custom evolution conditions tied to Sahur noise, Braindex progress, or Roan's Cognitive Resistance
