# Route 1 wild encounters patch V2

Target file:

`src/data/wild_encounters.json`

This patch changes Route 1 into Test Zone 01.

## Confirmed real block

The real FireRed block uses:

```json
"map": "MAP_ROUTE1",
"base_label": "sRoute1_FireRed"
```

Original Route 1 only uses:

```txt
SPECIES_PIDGEY
SPECIES_RATTATA
```

In Brainrot mapping:

```txt
SPECIES_PIDGEY = NOOBINI
SPECIES_RATTATA = PIPIKIWI
SPECIES_SPEAROW = TIMCHEESE
SPECIES_FEAROW = RACCOONI
```

## Design goal

Test Zone 01 should feel like the player's first Brainrot behavior area.

Encounter identity:

- NOOBINI: common annoying copycat
- PIPIKIWI: common simple fast attacker
- TIMCHEESE: uncommon fast pest
- RACCOONI: rare standalone trickster

## Replace Route 1 land_mons block

Find this block in `src/data/wild_encounters.json`:

```json
{
  "map": "MAP_ROUTE1",
  "base_label": "sRoute1_FireRed",
  "land_mons": {
    "encounter_rate": 21,
    "mons": [
      ...
    ]
  }
}
```

Replace only the `mons` list with this:

```json
"mons": [
  {
    "min_level": 2,
    "max_level": 2,
    "species": "SPECIES_PIDGEY"
  },
  {
    "min_level": 2,
    "max_level": 2,
    "species": "SPECIES_RATTATA"
  },
  {
    "min_level": 3,
    "max_level": 3,
    "species": "SPECIES_PIDGEY"
  },
  {
    "min_level": 3,
    "max_level": 3,
    "species": "SPECIES_RATTATA"
  },
  {
    "min_level": 3,
    "max_level": 3,
    "species": "SPECIES_PIDGEY"
  },
  {
    "min_level": 3,
    "max_level": 3,
    "species": "SPECIES_RATTATA"
  },
  {
    "min_level": 4,
    "max_level": 4,
    "species": "SPECIES_PIDGEY"
  },
  {
    "min_level": 4,
    "max_level": 4,
    "species": "SPECIES_RATTATA"
  },
  {
    "min_level": 4,
    "max_level": 4,
    "species": "SPECIES_SPEAROW"
  },
  {
    "min_level": 5,
    "max_level": 5,
    "species": "SPECIES_SPEAROW"
  },
  {
    "min_level": 5,
    "max_level": 5,
    "species": "SPECIES_FEAROW"
  },
  {
    "min_level": 5,
    "max_level": 5,
    "species": "SPECIES_RATTATA"
  }
]
```

## Encounter rate meaning

The encounter rate stays:

```json
"encounter_rate": 21
```

This is safe because it keeps the same route density.

## Slot logic

The global land encounter rates are:

```txt
20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1
```

So the new feel is roughly:

```txt
NOOBINI / Pidgey slots: common
PIPIKIWI / Rattata slots: common
TIMCHEESE / Spearow slots: uncommon
RACCOONI / Fearow slot: very rare
```

## Why Raccooni is level 5

Raccooni is standalone and rare.

It should feel like a small secret in the first route.

It should not evolve from Tim Cheese.

## Optional safer version

If level 5 Raccooni feels too strong, replace the rare slot with level 4:

```json
{
  "min_level": 4,
  "max_level": 4,
  "species": "SPECIES_FEAROW"
}
```

But V1 should test level 5 first.

## Important evolution rule

Also make sure `src/data/pokemon/evolution.h` has no Spearow -> Fearow evolution.

TIMCHEESE and RACCOONI must stay separate.

## First playable result

Route 1 / Test Zone 01 becomes:

```txt
NOOBINI common
PIPIKIWI common
TIMCHEESE uncommon
RACCOONI rare
```
