# Route 1 Brainrot learnsets patch V1

Target file:

`src/data/pokemon/level_up_learnsets.h`

This patch gives early Route 1 Brainrots their first gameplay identity.

No custom moves yet.

## Brainrots covered

| Original slot | Brainrot | Evolution status |
|---|---|---|
| Pidgey | NOOBINI | evolves |
| Pidgeotto | PIZZANINI | evolves |
| Pidgeot | LOSNOOBI | final form |
| Rattata | PIPIKIWI | evolves |
| Raticate | PIPICORNI | final form |
| Spearow | TIMCHEESE | does not evolve |
| Fearow | RACCOONI | does not evolve |

## Important correction

TIMCHEESE does not evolve into RACCOONI.

RACCOONI is standalone.

So the evolution file should not keep Spearow -> Fearow as a real final design.

## NOOBINI line

Role:

- annoying common route Brainrot
- fast enough to bother the player
- learns accuracy/control moves

### Replace `sPidgeyLevelUpLearnset`

```c
static const u16 sPidgeyLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_SAND_ATTACK),
    LEVEL_UP_MOVE(5, MOVE_GUST),
    LEVEL_UP_MOVE(9, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(13, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(18, MOVE_WING_ATTACK),
    LEVEL_UP_MOVE(25, MOVE_FEATHER_DANCE),
    LEVEL_UP_MOVE(34, MOVE_AGILITY),
    LEVEL_UP_MOVE(43, MOVE_MIRROR_MOVE),
    LEVEL_UP_END
};
```

### Replace `sPidgeottoLevelUpLearnset`

```c
static const u16 sPidgeottoLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_SAND_ATTACK),
    LEVEL_UP_MOVE(1, MOVE_GUST),
    LEVEL_UP_MOVE(5, MOVE_GUST),
    LEVEL_UP_MOVE(9, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(13, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(19, MOVE_WING_ATTACK),
    LEVEL_UP_MOVE(27, MOVE_FEATHER_DANCE),
    LEVEL_UP_MOVE(36, MOVE_AGILITY),
    LEVEL_UP_MOVE(48, MOVE_MIRROR_MOVE),
    LEVEL_UP_END
};
```

### Replace `sPidgeotLevelUpLearnset`

```c
static const u16 sPidgeotLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_SAND_ATTACK),
    LEVEL_UP_MOVE(1, MOVE_GUST),
    LEVEL_UP_MOVE(1, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(5, MOVE_GUST),
    LEVEL_UP_MOVE(9, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(13, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(19, MOVE_WING_ATTACK),
    LEVEL_UP_MOVE(27, MOVE_FEATHER_DANCE),
    LEVEL_UP_MOVE(38, MOVE_AGILITY),
    LEVEL_UP_MOVE(52, MOVE_MIRROR_MOVE),
    LEVEL_UP_END
};
```

## PIPI KIWI line

Role:

- simple fast attacker
- easy first catch
- learns bite-style pressure

### Replace `sRattataLevelUpLearnset`

```c
static const u16 sRattataLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(5, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(10, MOVE_FOCUS_ENERGY),
    LEVEL_UP_MOVE(14, MOVE_HYPER_FANG),
    LEVEL_UP_MOVE(21, MOVE_PURSUIT),
    LEVEL_UP_MOVE(29, MOVE_SUPER_FANG),
    LEVEL_UP_MOVE(38, MOVE_ENDEAVOR),
    LEVEL_UP_END
};
```

### Replace `sRaticateLevelUpLearnset`

```c
static const u16 sRaticateLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(1, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(5, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(10, MOVE_FOCUS_ENERGY),
    LEVEL_UP_MOVE(14, MOVE_HYPER_FANG),
    LEVEL_UP_MOVE(20, MOVE_SCARY_FACE),
    LEVEL_UP_MOVE(28, MOVE_PURSUIT),
    LEVEL_UP_MOVE(38, MOVE_SUPER_FANG),
    LEVEL_UP_MOVE(48, MOVE_ENDEAVOR),
    LEVEL_UP_END
};
```

## TIMCHEESE standalone

Role:

- fast pest
- fragile
- annoying early wild Brainrot
- no evolution

### Replace `sSpearowLevelUpLearnset`

```c
static const u16 sSpearowLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_PECK),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(5, MOVE_LEER),
    LEVEL_UP_MOVE(10, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(16, MOVE_PURSUIT),
    LEVEL_UP_MOVE(23, MOVE_AERIAL_ACE),
    LEVEL_UP_MOVE(31, MOVE_AGILITY),
    LEVEL_UP_MOVE(40, MOVE_DRILL_PECK),
    LEVEL_UP_END
};
```

## RACCOONI standalone

Role:

- rare trickster
- annoying item/thief style
- no evolution

### Replace `sFearowLevelUpLearnset`

```c
static const u16 sFearowLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_PECK),
    LEVEL_UP_MOVE(1, MOVE_LEER),
    LEVEL_UP_MOVE(1, MOVE_PURSUIT),
    LEVEL_UP_MOVE(7, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(13, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(20, MOVE_THIEF),
    LEVEL_UP_MOVE(28, MOVE_AGILITY),
    LEVEL_UP_MOVE(37, MOVE_AERIAL_ACE),
    LEVEL_UP_MOVE(47, MOVE_DRILL_PECK),
    LEVEL_UP_END
};
```

## Evolution note

In `src/data/pokemon/evolution.h`, remove or disable the Spearow evolution line:

```c
[SPECIES_SPEAROW] = {{EVO_LEVEL, 20, SPECIES_FEAROW}},
```

TIMCHEESE and RACCOONI should be separate single-stage Brainrots.

## First build goal

The player should feel early Route 1 has different Brainrot personalities:

- NOOBINI: common and annoying
- PIPIKIWI: simple and useful
- TIMCHEESE: fast pest
- RACCOONI: rare trickster
