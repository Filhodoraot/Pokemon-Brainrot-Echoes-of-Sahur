# Starter stats patch V1

Target file:

`src/data/pokemon/species_info.h`

This patch changes the starter slots into Brainrot-style roles while keeping old sprites and engine systems.

## Design goal

- Chimpanzini line: physical tank / plant brute
- Cappuccino line: fast attacker / fire shadow flavor
- Tralalero line: balanced bulky water meme

Custom types are not added yet.

For now, use existing FireRed types:

- Chimpanzini: GRASS / POISON for now
- Cappuccino: FIRE / FIRE for now
- Tralalero: WATER / WATER for now

## Safe rule

Do not add new abilities yet.

Reuse:

- OVERGROW for Chimpanzini line
- BLAZE for Cappuccino line
- TORRENT for Tralalero line

Later we rename or replace abilities.

## Bulbasaur slot -> CHIMPANZI

Replace the `SPECIES_BULBASAUR` block with:

```c
[SPECIES_BULBASAUR] =
{
    .baseHP = 50,
    .baseAttack = 65,
    .baseDefense = 55,
    .baseSpeed = 35,
    .baseSpAttack = 45,
    .baseSpDefense = 55,
    .types = {TYPE_GRASS, TYPE_POISON},
    .catchRate = 45,
    .expYield = 64,
    .evYield_HP = 0,
    .evYield_Attack = 1,
    .evYield_Defense = 0,
    .evYield_Speed = 0,
    .evYield_SpAttack = 0,
    .evYield_SpDefense = 0,
    .itemCommon = ITEM_NONE,
    .itemRare = ITEM_NONE,
    .genderRatio = PERCENT_FEMALE(12.5),
    .eggCycles = 20,
    .friendship = 70,
    .growthRate = GROWTH_MEDIUM_SLOW,
    .eggGroups = {EGG_GROUP_MONSTER, EGG_GROUP_GRASS},
    .abilities = {ABILITY_OVERGROW, ABILITY_NONE},
    .safariZoneFleeRate = 0,
    .bodyColor = BODY_COLOR_GREEN,
    .noFlip = FALSE,
},
```

## Ivysaur slot -> BANANINI

```c
[SPECIES_IVYSAUR] =
{
    .baseHP = 68,
    .baseAttack = 82,
    .baseDefense = 73,
    .baseSpeed = 50,
    .baseSpAttack = 58,
    .baseSpDefense = 72,
    .types = {TYPE_GRASS, TYPE_POISON},
    .catchRate = 45,
    .expYield = 141,
    .evYield_HP = 0,
    .evYield_Attack = 1,
    .evYield_Defense = 1,
    .evYield_Speed = 0,
    .evYield_SpAttack = 0,
    .evYield_SpDefense = 0,
    .itemCommon = ITEM_NONE,
    .itemRare = ITEM_NONE,
    .genderRatio = PERCENT_FEMALE(12.5),
    .eggCycles = 20,
    .friendship = 70,
    .growthRate = GROWTH_MEDIUM_SLOW,
    .eggGroups = {EGG_GROUP_MONSTER, EGG_GROUP_GRASS},
    .abilities = {ABILITY_OVERGROW, ABILITY_NONE},
    .safariZoneFleeRate = 0,
    .bodyColor = BODY_COLOR_GREEN,
    .noFlip = FALSE,
},
```

## Venusaur slot -> AVOCADOR

```c
[SPECIES_VENUSAUR] =
{
    .baseHP = 88,
    .baseAttack = 105,
    .baseDefense = 95,
    .baseSpeed = 68,
    .baseSpAttack = 72,
    .baseSpDefense = 92,
    .types = {TYPE_GRASS, TYPE_POISON},
    .catchRate = 45,
    .expYield = 208,
    .evYield_HP = 0,
    .evYield_Attack = 2,
    .evYield_Defense = 1,
    .evYield_Speed = 0,
    .evYield_SpAttack = 0,
    .evYield_SpDefense = 0,
    .itemCommon = ITEM_NONE,
    .itemRare = ITEM_NONE,
    .genderRatio = PERCENT_FEMALE(12.5),
    .eggCycles = 20,
    .friendship = 70,
    .growthRate = GROWTH_MEDIUM_SLOW,
    .eggGroups = {EGG_GROUP_MONSTER, EGG_GROUP_GRASS},
    .abilities = {ABILITY_OVERGROW, ABILITY_NONE},
    .safariZoneFleeRate = 0,
    .bodyColor = BODY_COLOR_GREEN,
    .noFlip = FALSE,
},
```

## Charmander slot -> CAPPUCINO

```c
[SPECIES_CHARMANDER] =
{
    .baseHP = 39,
    .baseAttack = 64,
    .baseDefense = 38,
    .baseSpeed = 72,
    .baseSpAttack = 60,
    .baseSpDefense = 45,
    .types = {TYPE_FIRE, TYPE_FIRE},
    .catchRate = 45,
    .expYield = 65,
    .evYield_HP = 0,
    .evYield_Attack = 0,
    .evYield_Defense = 0,
    .evYield_Speed = 1,
    .evYield_SpAttack = 0,
    .evYield_SpDefense = 0,
    .itemCommon = ITEM_NONE,
    .itemRare = ITEM_NONE,
    .genderRatio = PERCENT_FEMALE(12.5),
    .eggCycles = 20,
    .friendship = 70,
    .growthRate = GROWTH_MEDIUM_SLOW,
    .eggGroups = {EGG_GROUP_MONSTER, EGG_GROUP_DRAGON},
    .abilities = {ABILITY_BLAZE, ABILITY_NONE},
    .safariZoneFleeRate = 0,
    .bodyColor = BODY_COLOR_RED,
    .noFlip = FALSE,
},
```

## Squirtle slot -> TRALALERO

```c
[SPECIES_SQUIRTLE] =
{
    .baseHP = 48,
    .baseAttack = 52,
    .baseDefense = 58,
    .baseSpeed = 52,
    .baseSpAttack = 55,
    .baseSpDefense = 58,
    .types = {TYPE_WATER, TYPE_WATER},
    .catchRate = 45,
    .expYield = 66,
    .evYield_HP = 0,
    .evYield_Attack = 0,
    .evYield_Defense = 1,
    .evYield_Speed = 0,
    .evYield_SpAttack = 0,
    .evYield_SpDefense = 0,
    .itemCommon = ITEM_NONE,
    .itemRare = ITEM_NONE,
    .genderRatio = PERCENT_FEMALE(12.5),
    .eggCycles = 20,
    .friendship = 70,
    .growthRate = GROWTH_MEDIUM_SLOW,
    .eggGroups = {EGG_GROUP_MONSTER, EGG_GROUP_WATER_1},
    .abilities = {ABILITY_TORRENT, ABILITY_NONE},
    .safariZoneFleeRate = 0,
    .bodyColor = BODY_COLOR_BLUE,
    .noFlip = FALSE,
},
```

## Balance notes

- Chimpanzini is slower but hits hard.
- Cappuccino is fastest and most aggressive.
- Tralalero is safest and most balanced.

This matches Roan's early choice theme:

- Chimpanzini: strength and survival
- Cappuccino: risk and aggression
- Tralalero: stability and investigation
