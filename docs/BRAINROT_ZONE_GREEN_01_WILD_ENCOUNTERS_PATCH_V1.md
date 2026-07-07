# Zone Green 01 wild encounters patch V1

Target file:

`src/data/wild_encounters.json`

This patch changes Viridian Forest into Zone Green 01.

## Story role

Zone Green 01 is the first real dungeon.

It is where Roan starts seeing that Brainrots are not just silly creatures.

This area introduces:

- field demon history
- first cult clues
- forest Brainrots
- early Sahur Fragment setup

## Confirmed real block style

Viridian Forest uses:

```json
"map": "MAP_VIRIDIAN_FOREST"
```

The LeafGreen block confirms the forest pattern uses these species:

```txt
SPECIES_CATERPIE
SPECIES_WEEDLE
SPECIES_KAKUNA
SPECIES_METAPOD
SPECIES_PIKACHU
```

For FireRed, use the same target map and replace the `land_mons` list.

## Brainrot mapping for first forest build

| Original slot | Brainrot role | Battle name idea |
|---|---|---|
| Caterpie | Bambini Crostini Baby | BAMBINI |
| Metapod | Bambini Crostini Teen | CROSTINI |
| Butterfree | Bambini Crostini Adult | BAMBILORD |
| Weedle | Lirili Larila Baby | LIRILI |
| Kakuna | Lirili Larila Teen | LARILA |
| Beedrill | Lirili Larila Adult | LIRILORD |
| Pikachu | Brr Brr Patapim rare echo | BRRBRR |

## Why these slots

Caterpie and Weedle already have 3-stage evolution lines.

That makes them good placeholder lines for Brainrots that evolve.

Pikachu is rare in Viridian Forest, so it becomes a rare forest Brainrot.

## Replace Viridian Forest land_mons block

Find the block:

```json
{
  "map": "MAP_VIRIDIAN_FOREST",
  "base_label": "sViridianForest_FireRed",
  "land_mons": {
    "encounter_rate": 14,
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
    "min_level": 3,
    "max_level": 3,
    "species": "SPECIES_CATERPIE"
  },
  {
    "min_level": 3,
    "max_level": 3,
    "species": "SPECIES_WEEDLE"
  },
  {
    "min_level": 4,
    "max_level": 4,
    "species": "SPECIES_CATERPIE"
  },
  {
    "min_level": 4,
    "max_level": 4,
    "species": "SPECIES_WEEDLE"
  },
  {
    "min_level": 5,
    "max_level": 5,
    "species": "SPECIES_CATERPIE"
  },
  {
    "min_level": 5,
    "max_level": 5,
    "species": "SPECIES_WEEDLE"
  },
  {
    "min_level": 5,
    "max_level": 5,
    "species": "SPECIES_METAPOD"
  },
  {
    "min_level": 5,
    "max_level": 5,
    "species": "SPECIES_KAKUNA"
  },
  {
    "min_level": 6,
    "max_level": 6,
    "species": "SPECIES_METAPOD"
  },
  {
    "min_level": 6,
    "max_level": 6,
    "species": "SPECIES_KAKUNA"
  },
  {
    "min_level": 4,
    "max_level": 4,
    "species": "SPECIES_PIKACHU"
  },
  {
    "min_level": 6,
    "max_level": 6,
    "species": "SPECIES_PIKACHU"
  }
]
```

## Encounter feel

The global land encounter slots are weighted like this:

```txt
20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1
```

So the forest becomes roughly:

```txt
BAMBINI common
LIRILI common
CROSTINI uncommon
LARILA uncommon
BRRBRR very rare
```

## Important evolution note

Because Caterpie and Weedle lines evolve early, they are good for first testing.

But update species names later:

```txt
SPECIES_CATERPIE -> BAMBINI
SPECIES_METAPOD -> CROSTINI
SPECIES_BUTTERFREE -> BAMBILORD
SPECIES_WEEDLE -> LIRILI
SPECIES_KAKUNA -> LARILA
SPECIES_BEEDRILL -> LIRILORD
SPECIES_PIKACHU -> BRRBRR
```

## Pikachu / BRRBRR note

Pikachu normally evolves with Thunder Stone.

For final design, Brr Brr Patapim should be its own evolution line or have controlled evolution.

For first build, rare BRRBRR can stay as a placeholder.

Later, either:

1. remove Pikachu's Thunder Stone evolution, or
2. use the Pikachu -> Raichu line as Brr Brr Patapim Baby -> Adult.

## First playable result

Zone Green 01 becomes:

```txt
BAMBINI common
LIRILI common
CROSTINI uncommon
LARILA uncommon
BRRBRR rare
```

This makes Viridian Forest feel like the first Brainrot dungeon.
