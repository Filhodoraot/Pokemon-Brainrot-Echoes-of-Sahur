# Brainrot evolution canon V2

This replaces the idea that every Brainrot must evolve.

## Core rule

Every Brainrot can have a maturity stage in lore/data:

```txt
Baby
Teen
Adult
```

But only some Brainrots have real in-game evolution.

Most Brainrots do not evolve.

## Why

If every Brainrot evolves, the game becomes too bloated.

Too many evolutions means:

- too many sprites
- too many names
- too many stats to balance
- too many Pokedex entries
- too much work before the ROM is playable

So the better system is:

```txt
Stage = property/lore
Evolution = only for selected Brainrots
```

## Types of Brainrot growth

### 1. Full evolution line

Used for important Brainrots.

Example:

```txt
CHIMPANZI -> BANANINI -> AVOCADOR
Baby -> Teen -> Adult
```

### 2. Two-stage evolution line

Used for common early Brainrots.

Example:

```txt
PIPIKIWI -> PIPICORNI
Baby -> Adult
```

### 3. No evolution

Used for many iconic Brainrots.

Example:

```txt
TIMCHEESE
Stage: Teen
No evolution
```

It can still have strong moves and good stats. Not evolving does not mean weak.

### 4. Form change later

Used for legendary or story Brainrots.

Example:

```txt
Strawberry Helefanto
Memory Guardian -> Tung Guard -> Liberated
```

This is not normal evolution. It is story/form state.

## First build evolution lines

### Real 3-stage lines

| Line | Baby | Teen | Adult |
|---|---|---|---|
| Chimpanzini line | CHIMPANZI | BANANINI | AVOCADOR |
| Cappuccino line | CAPPUCINO | HARPUCINO | CAPASSINO |
| Tralalero line | TRALALERO | TRALALITO | TRALALORD |
| Noobini line | NOOBINI | PIZZANINI | LOSNOOBI |

### Real 2-stage lines

| Line | Stage 1 | Stage 2 |
|---|---|---|
| Pipi line | PIPIKIWI | PIPICORNI |

### No-evolution early Brainrots

| Brainrot | Stage | Role |
|---|---|---|
| TIMCHEESE | Teen | fast annoying route Brainrot |
| RACCOONI | Adult | rare item-thief style Brainrot |

## Important correction

Tim Cheese should NOT evolve into Raccooni in the final design.

That was only a temporary slot idea.

Updated rule:

```txt
TIMCHEESE = standalone
RACCOONI = standalone
```

If we are forced to reuse Spearow -> Fearow for first testing, treat it as placeholder only.

Better first-build option:

- Keep SPEAROW as TIMCHEESE with no evolution.
- Keep FEAROW as RACCOONI with no pre-evolution.

In `evolution.h`, this means removing or disabling:

```c
[SPECIES_SPEAROW] = {{EVO_LEVEL, 20, SPECIES_FEAROW}},
```

or changing it to no evolution by removing the line.

## Long-term rule

Only these kinds of Brainrots should evolve:

- starters
- early route families
- important recurring species
- species with obvious baby/teen/adult concept
- boss species that grow with story progression

Most meme-icon Brainrots stay single-stage.

## Single-stage Brainrots can still be strong

Single-stage Brainrots can have:

- higher base stats
- unique abilities
- rare encounter rates
- signature moves
- story relevance

Example:

```txt
RACCOONI
No evolution
Rare encounter
High speed
Steals held items later
```

## Development priority

For first playable build:

1. Starters evolve.
2. Noobini evolves.
3. Pipi Kiwi evolves.
4. Tim Cheese does not evolve.
5. Raccooni does not evolve.
6. Legendaries do not use normal evolution.

Sprites come later.
