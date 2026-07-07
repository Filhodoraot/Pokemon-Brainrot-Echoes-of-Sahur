# Starter learnsets patch V1

Target file:

`src/data/pokemon/level_up_learnsets.h`

This patch changes the starter moves by level while using existing FireRed moves.

No custom move is created yet.

## Design rule

Use old moves as placeholders for future Brainrot moves.

Later rename moves like this:

| Current move | Future Brainrot name |
|---|---|
| GROWL | Sahur Whisper |
| VINE_WHIP | Banana Whip |
| RAZOR_LEAF | Peel Cutter |
| EMBER | Espresso Shot |
| SMOKESCREEN | Cafe Smoke |
| SLASH | Assassin Slash |
| BUBBLE | Tralala Bubble |
| BITE | Meme Bite |
| RAPID_SPIN | Sneaker Spin |
| RAIN_DANCE | Tralala Rhythm |

## Chimpanzini line

Role:

- physical
- tanky
- plant brute
- slower but reliable

### Replace `sBulbasaurLevelUpLearnset`

```c
static const u16 sBulbasaurLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(6, MOVE_VINE_WHIP),
    LEVEL_UP_MOVE(9, MOVE_LEECH_SEED),
    LEVEL_UP_MOVE(13, MOVE_GROWTH),
    LEVEL_UP_MOVE(17, MOVE_RAZOR_LEAF),
    LEVEL_UP_MOVE(22, MOVE_POISON_POWDER),
    LEVEL_UP_MOVE(27, MOVE_TAKE_DOWN),
    LEVEL_UP_MOVE(34, MOVE_SYNTHESIS),
    LEVEL_UP_MOVE(42, MOVE_SOLAR_BEAM),
    LEVEL_UP_END
};
```

### Replace `sIvysaurLevelUpLearnset`

```c
static const u16 sIvysaurLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(1, MOVE_VINE_WHIP),
    LEVEL_UP_MOVE(6, MOVE_VINE_WHIP),
    LEVEL_UP_MOVE(9, MOVE_LEECH_SEED),
    LEVEL_UP_MOVE(13, MOVE_GROWTH),
    LEVEL_UP_MOVE(18, MOVE_RAZOR_LEAF),
    LEVEL_UP_MOVE(23, MOVE_POISON_POWDER),
    LEVEL_UP_MOVE(29, MOVE_TAKE_DOWN),
    LEVEL_UP_MOVE(38, MOVE_SYNTHESIS),
    LEVEL_UP_MOVE(50, MOVE_SOLAR_BEAM),
    LEVEL_UP_END
};
```

### Replace `sVenusaurLevelUpLearnset`

```c
static const u16 sVenusaurLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(1, MOVE_VINE_WHIP),
    LEVEL_UP_MOVE(1, MOVE_LEECH_SEED),
    LEVEL_UP_MOVE(6, MOVE_VINE_WHIP),
    LEVEL_UP_MOVE(9, MOVE_LEECH_SEED),
    LEVEL_UP_MOVE(13, MOVE_GROWTH),
    LEVEL_UP_MOVE(18, MOVE_RAZOR_LEAF),
    LEVEL_UP_MOVE(23, MOVE_POISON_POWDER),
    LEVEL_UP_MOVE(29, MOVE_TAKE_DOWN),
    LEVEL_UP_MOVE(41, MOVE_SYNTHESIS),
    LEVEL_UP_MOVE(55, MOVE_SOLAR_BEAM),
    LEVEL_UP_END
};
```

## Cappuccino line

Role:

- fast
- aggressive
- fragile
- fire assassin flavor

### Replace `sCharmanderLevelUpLearnset`

```c
static const u16 sCharmanderLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_SCRATCH),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(6, MOVE_EMBER),
    LEVEL_UP_MOVE(10, MOVE_SMOKESCREEN),
    LEVEL_UP_MOVE(14, MOVE_METAL_CLAW),
    LEVEL_UP_MOVE(19, MOVE_SCARY_FACE),
    LEVEL_UP_MOVE(25, MOVE_SLASH),
    LEVEL_UP_MOVE(32, MOVE_FLAMETHROWER),
    LEVEL_UP_MOVE(40, MOVE_FIRE_SPIN),
    LEVEL_UP_MOVE(49, MOVE_HEAT_WAVE),
    LEVEL_UP_END
};
```

### Replace `sCharmeleonLevelUpLearnset`

```c
static const u16 sCharmeleonLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_SCRATCH),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(1, MOVE_EMBER),
    LEVEL_UP_MOVE(6, MOVE_EMBER),
    LEVEL_UP_MOVE(10, MOVE_SMOKESCREEN),
    LEVEL_UP_MOVE(14, MOVE_METAL_CLAW),
    LEVEL_UP_MOVE(20, MOVE_SCARY_FACE),
    LEVEL_UP_MOVE(27, MOVE_SLASH),
    LEVEL_UP_MOVE(36, MOVE_FLAMETHROWER),
    LEVEL_UP_MOVE(45, MOVE_FIRE_SPIN),
    LEVEL_UP_MOVE(56, MOVE_HEAT_WAVE),
    LEVEL_UP_END
};
```

### Replace `sCharizardLevelUpLearnset`

```c
static const u16 sCharizardLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_HEAT_WAVE),
    LEVEL_UP_MOVE(1, MOVE_SCRATCH),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(1, MOVE_EMBER),
    LEVEL_UP_MOVE(1, MOVE_METAL_CLAW),
    LEVEL_UP_MOVE(6, MOVE_EMBER),
    LEVEL_UP_MOVE(10, MOVE_SMOKESCREEN),
    LEVEL_UP_MOVE(14, MOVE_METAL_CLAW),
    LEVEL_UP_MOVE(20, MOVE_SCARY_FACE),
    LEVEL_UP_MOVE(27, MOVE_SLASH),
    LEVEL_UP_MOVE(36, MOVE_WING_ATTACK),
    LEVEL_UP_MOVE(44, MOVE_FLAMETHROWER),
    LEVEL_UP_MOVE(55, MOVE_FIRE_SPIN),
    LEVEL_UP_MOVE(66, MOVE_HEAT_WAVE),
    LEVEL_UP_END
};
```

## Tralalero line

Role:

- balanced
- safe starter
- water rhythm/meme flavor
- good for Roan's investigation path

### Replace `sSquirtleLevelUpLearnset`

```c
static const u16 sSquirtleLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(6, MOVE_BUBBLE),
    LEVEL_UP_MOVE(9, MOVE_WITHDRAW),
    LEVEL_UP_MOVE(13, MOVE_WATER_GUN),
    LEVEL_UP_MOVE(17, MOVE_BITE),
    LEVEL_UP_MOVE(22, MOVE_RAPID_SPIN),
    LEVEL_UP_MOVE(27, MOVE_PROTECT),
    LEVEL_UP_MOVE(33, MOVE_RAIN_DANCE),
    LEVEL_UP_MOVE(41, MOVE_SKULL_BASH),
    LEVEL_UP_MOVE(50, MOVE_HYDRO_PUMP),
    LEVEL_UP_END
};
```

### Replace `sWartortleLevelUpLearnset`

```c
static const u16 sWartortleLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(1, MOVE_BUBBLE),
    LEVEL_UP_MOVE(6, MOVE_BUBBLE),
    LEVEL_UP_MOVE(9, MOVE_WITHDRAW),
    LEVEL_UP_MOVE(13, MOVE_WATER_GUN),
    LEVEL_UP_MOVE(18, MOVE_BITE),
    LEVEL_UP_MOVE(24, MOVE_RAPID_SPIN),
    LEVEL_UP_MOVE(30, MOVE_PROTECT),
    LEVEL_UP_MOVE(38, MOVE_RAIN_DANCE),
    LEVEL_UP_MOVE(47, MOVE_SKULL_BASH),
    LEVEL_UP_MOVE(58, MOVE_HYDRO_PUMP),
    LEVEL_UP_END
};
```

### Replace `sBlastoiseLevelUpLearnset`

```c
static const u16 sBlastoiseLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(1, MOVE_BUBBLE),
    LEVEL_UP_MOVE(1, MOVE_WITHDRAW),
    LEVEL_UP_MOVE(6, MOVE_BUBBLE),
    LEVEL_UP_MOVE(9, MOVE_WITHDRAW),
    LEVEL_UP_MOVE(13, MOVE_WATER_GUN),
    LEVEL_UP_MOVE(18, MOVE_BITE),
    LEVEL_UP_MOVE(24, MOVE_RAPID_SPIN),
    LEVEL_UP_MOVE(30, MOVE_PROTECT),
    LEVEL_UP_MOVE(42, MOVE_RAIN_DANCE),
    LEVEL_UP_MOVE(55, MOVE_SKULL_BASH),
    LEVEL_UP_MOVE(68, MOVE_HYDRO_PUMP),
    LEVEL_UP_END
};
```

## Why this patch matters

This gives each starter a different feel immediately:

- Chimpanzini hits harder and survives.
- Cappuccino attacks fast and snowballs.
- Tralalero is reliable and safer.

## Later phase

After this works, create actual custom moves:

- Banana Bonk
- Espresso Slash
- Sneaker Wave
- Sahur Call
- Meme Bite
- IQ Drain

But for the first build, existing moves are safer.
