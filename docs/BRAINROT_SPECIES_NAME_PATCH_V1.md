# Species name patch V1

Target file:

`src/data/text/species_names.h`

Important:

FireRed species names use `POKEMON_NAME_LENGTH`, which is normally 10 characters.

So long Brainrot names need short in-game names.

## Starter slots

Replace these lines:

```c
[SPECIES_BULBASAUR] = _("BULBASAUR"),
[SPECIES_IVYSAUR] = _("IVYSAUR"),
[SPECIES_VENUSAUR] = _("VENUSAUR"),
[SPECIES_CHARMANDER] = _("CHARMANDER"),
[SPECIES_CHARMELEON] = _("CHARMELEON"),
[SPECIES_CHARIZARD] = _("CHARIZARD"),
[SPECIES_SQUIRTLE] = _("SQUIRTLE"),
[SPECIES_WARTORTLE] = _("WARTORTLE"),
[SPECIES_BLASTOISE] = _("BLASTOISE"),
```

With this:

```c
[SPECIES_BULBASAUR] = _("CHIMPANZI"),
[SPECIES_IVYSAUR] = _("BANANINI"),
[SPECIES_VENUSAUR] = _("AVOCADOR"),
[SPECIES_CHARMANDER] = _("CAPPUCINO"),
[SPECIES_CHARMELEON] = _("HARPUCINO"),
[SPECIES_CHARIZARD] = _("CAPASSINO"),
[SPECIES_SQUIRTLE] = _("TRALALERO"),
[SPECIES_WARTORTLE] = _("TRALALITO"),
[SPECIES_BLASTOISE] = _("TRALALORD"),
```

## What these mean in lore

| Original slot | In-game name | Full Brainrot name |
|---|---|---|
| Bulbasaur | CHIMPANZI | Chimpanzini Bananini |
| Ivysaur | BANANINI | Chimpanzini Bananini middle form |
| Venusaur | AVOCADOR | Avocadorilla final form |
| Charmander | CAPPUCINO | Cappuccino Assassino |
| Charmeleon | HARPUCINO | Harpuccino |
| Charizard | CAPASSINO | Cappuccino Assassino final form |
| Squirtle | TRALALERO | Tralalero Tralala |
| Wartortle | TRALALITO | Los Tralaleritos middle form |
| Blastoise | TRALALORD | Tralalero final form |

## Early Route 1 slots

Replace these lines:

```c
[SPECIES_PIDGEY] = _("PIDGEY"),
[SPECIES_PIDGEOTTO] = _("PIDGEOTTO"),
[SPECIES_PIDGEOT] = _("PIDGEOT"),
[SPECIES_RATTATA] = _("RATTATA"),
[SPECIES_RATICATE] = _("RATICATE"),
[SPECIES_SPEAROW] = _("SPEAROW"),
[SPECIES_FEAROW] = _("FEAROW"),
```

With this:

```c
[SPECIES_PIDGEY] = _("NOOBINI"),
[SPECIES_PIDGEOTTO] = _("PIZZANINI"),
[SPECIES_PIDGEOT] = _("LOSNOOBI"),
[SPECIES_RATTATA] = _("PIPIKIWI"),
[SPECIES_RATICATE] = _("PIPICORNI"),
[SPECIES_SPEAROW] = _("TIMCHEESE"),
[SPECIES_FEAROW] = _("RACCOONI"),
```

## What these mean in lore

| Original slot | In-game name | Full Brainrot name |
|---|---|---|
| Pidgey | NOOBINI | Noobini Pizzanini |
| Pidgeotto | PIZZANINI | stronger Noobini line |
| Pidgeot | LOSNOOBI | Los Noobinis |
| Rattata | PIPIKIWI | Pipi Kiwi |
| Raticate | PIPICORNI | Pipi Corni |
| Spearow | TIMCHEESE | Tim Cheese |
| Fearow | RACCOONI | Raccooni Jandelini |

## Why names are shortened

The game name box is tiny.

So the game uses short names, while docs/story/Pokedex can use the full names.

Example:

- Battle name: CAPPUCINO
- Lore name: Cappuccino Assassino

## Safety rule

Only edit names first. Do not edit stats, moves, sprites, or evolution in the same commit.

After this compiles, move to species info.
