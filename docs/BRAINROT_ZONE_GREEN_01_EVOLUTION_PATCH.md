# Zone Green 01 evolution patch

Target file:

`src/data/pokemon/evolution.h`

This patch sets the evolution behavior for the first forest Brainrots.

## Brainrot lines

### Bambini Crostini line

Original slots:

```txt
Caterpie -> Metapod -> Butterfree
```

Brainrot line:

```txt
BAMBINI -> CROSTINI -> BAMBILORD
Baby -> Teen -> Adult
```

Recommended evolution:

```c
[SPECIES_CATERPIE] = {{EVO_LEVEL, 7, SPECIES_METAPOD}},
[SPECIES_METAPOD]  = {{EVO_LEVEL, 12, SPECIES_BUTTERFREE}},
```

Why:

- fast evolution
- player sees Brainrot growth early
- keeps old bug-line pacing

### Lirili Larila line

Original slots:

```txt
Weedle -> Kakuna -> Beedrill
```

Brainrot line:

```txt
LIRILI -> LARILA -> LIRILORD
Baby -> Teen -> Adult
```

Recommended evolution:

```c
[SPECIES_WEEDLE] = {{EVO_LEVEL, 7, SPECIES_KAKUNA}},
[SPECIES_KAKUNA] = {{EVO_LEVEL, 12, SPECIES_BEEDRILL}},
```

Why:

- mirrors Bambini line
- gives the forest two fast evolving Brainrot families

### Brr Brr Patapim line

Original slots:

```txt
Pikachu -> Raichu
```

Brainrot line for first build:

```txt
BRRBRR -> PATAPIM
Baby -> Adult
```

Recommended evolution:

Keep Thunder Stone evolution for now:

```c
[SPECIES_PIKACHU] = {{EVO_ITEM, ITEM_THUNDER_STONE, SPECIES_RAICHU}},
```

Later, if custom evolution is added, change it to a Brainrot-specific item or level.

## First build result

Zone Green 01 has:

```txt
BAMBINI -> CROSTINI -> BAMBILORD
LIRILI -> LARILA -> LIRILORD
BRRBRR -> PATAPIM
```

## Important note

Brr Brr Patapim is planned as a 3-form Brainrot in sprite planning.

But for the first ROM build, 2 forms are safer because the Pikachu line only has 2 stages.

Later options:

1. Keep it as 2-form in game.
2. Add a new middle species slot.
3. Use Pichu if baby species are enabled/available.

For now, use the safe 2-form plan.
