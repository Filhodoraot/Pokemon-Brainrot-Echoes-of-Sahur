# Evolution patch V2 standalone fix

Target file:

`src/data/pokemon/evolution.h`

This fixes the temporary evolution mistake:

```txt
TIMCHEESE should not evolve into RACCOONI.
```

## Current original line

The original FireRed line is:

```c
[SPECIES_SPEAROW]    = {{EVO_LEVEL, 20, SPECIES_FEAROW}},
```

In Brainrot mapping:

```txt
SPEAROW = TIMCHEESE
FEAROW = RACCOONI
```

So if this line stays, TIMCHEESE evolves into RACCOONI, which is wrong.

## Correct design

```txt
TIMCHEESE = standalone Brainrot
RACCOONI = standalone Brainrot
```

## Patch

Remove or comment out this line:

```c
[SPECIES_SPEAROW]    = {{EVO_LEVEL, 20, SPECIES_FEAROW}},
```

Final result should have no Spearow evolution entry.

## Starter lines still evolve

Keep these edited lines:

```c
[SPECIES_BULBASAUR]  = {{EVO_LEVEL, 14, SPECIES_IVYSAUR}},
[SPECIES_IVYSAUR]    = {{EVO_LEVEL, 30, SPECIES_VENUSAUR}},
[SPECIES_CHARMANDER] = {{EVO_LEVEL, 14, SPECIES_CHARMELEON}},
[SPECIES_CHARMELEON] = {{EVO_LEVEL, 30, SPECIES_CHARIZARD}},
[SPECIES_SQUIRTLE]   = {{EVO_LEVEL, 14, SPECIES_WARTORTLE}},
[SPECIES_WARTORTLE]  = {{EVO_LEVEL, 30, SPECIES_BLASTOISE}},
```

## Route 1 lines

Keep Noobini and Pipi evolution:

```c
[SPECIES_PIDGEY]     = {{EVO_LEVEL, 12, SPECIES_PIDGEOTTO}},
[SPECIES_PIDGEOTTO]  = {{EVO_LEVEL, 25, SPECIES_PIDGEOT}},
[SPECIES_RATTATA]    = {{EVO_LEVEL, 16, SPECIES_RATICATE}},
```

Do not keep Tim Cheese evolution:

```c
// No evolution for SPECIES_SPEAROW / TIMCHEESE.
```

## First playable result

- CHIMPANZI evolves.
- CAPPUCINO evolves.
- TRALALERO evolves.
- NOOBINI evolves.
- PIPIKIWI evolves.
- TIMCHEESE does not evolve.
- RACCOONI does not evolve.

## Notes

RACCOONI can still appear as a rare standalone wild Brainrot later.

It should not be obtained through TIMCHEESE evolution.
