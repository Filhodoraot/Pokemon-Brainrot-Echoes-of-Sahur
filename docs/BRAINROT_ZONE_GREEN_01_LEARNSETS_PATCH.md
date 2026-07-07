# Zone Green 01 learnsets patch

Target file:

`src/data/pokemon/level_up_learnsets.h`

This patch gives the first forest Brainrots better early-game identity.

## Confirmed source blocks

The real file has these blocks:

```txt
sCaterpieLevelUpLearnset
sMetapodLevelUpLearnset
sButterfreeLevelUpLearnset
sWeedleLevelUpLearnset
sKakunaLevelUpLearnset
sBeedrillLevelUpLearnset
sPikachuLevelUpLearnset
sRaichuLevelUpLearnset
```

## Design goal

Zone Green 01 should feel different from Test Zone 01.

Test Zone 01 has simple wild Brainrots.

Zone Green 01 should introduce:

- status moves
- confusion
- forest danger
- early fast evolutions
- first rare electric/noise Brainrot

## BAMBINI line

Original slots:

```txt
Caterpie -> Metapod -> Butterfree
```

Brainrot line:

```txt
BAMBINI -> CROSTINI -> BAMBILORD
```

Role:

- weird forest support line
- uses string, sleep, confusion, powder

### Replace `sCaterpieLevelUpLearnset`

```c
static const u16 sCaterpieLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_TACKLE),
    LEVEL_UP_MOVE(1, MOVE_STRING_SHOT),
    LEVEL_UP_MOVE(5, MOVE_STUN_SPORE),
    LEVEL_UP_END
};
```

### Replace `sMetapodLevelUpLearnset`

```c
static const u16 sMetapodLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_HARDEN),
    LEVEL_UP_MOVE(1, MOVE_STRING_SHOT),
    LEVEL_UP_MOVE(7, MOVE_HARDEN),
    LEVEL_UP_MOVE(10, MOVE_STUN_SPORE),
    LEVEL_UP_END
};
```

### Replace `sButterfreeLevelUpLearnset`

```c
static const u16 sButterfreeLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_CONFUSION),
    LEVEL_UP_MOVE(1, MOVE_GUST),
    LEVEL_UP_MOVE(10, MOVE_CONFUSION),
    LEVEL_UP_MOVE(13, MOVE_POISON_POWDER),
    LEVEL_UP_MOVE(14, MOVE_STUN_SPORE),
    LEVEL_UP_MOVE(15, MOVE_SLEEP_POWDER),
    LEVEL_UP_MOVE(18, MOVE_SUPERSONIC),
    LEVEL_UP_MOVE(23, MOVE_WHIRLWIND),
    LEVEL_UP_MOVE(28, MOVE_GUST),
    LEVEL_UP_MOVE(34, MOVE_PSYBEAM),
    LEVEL_UP_MOVE(40, MOVE_SAFEGUARD),
    LEVEL_UP_MOVE(47, MOVE_SILVER_WIND),
    LEVEL_UP_END
};
```

## LIRILI line

Original slots:

```txt
Weedle -> Kakuna -> Beedrill
```

Brainrot line:

```txt
LIRILI -> LARILA -> LIRILORD
```

Role:

- sharper forest attacker
- poison, fury, pursuit
- more aggressive than BAMBINI line

### Replace `sWeedleLevelUpLearnset`

```c
static const u16 sWeedleLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_POISON_STING),
    LEVEL_UP_MOVE(1, MOVE_STRING_SHOT),
    LEVEL_UP_MOVE(6, MOVE_FURY_ATTACK),
    LEVEL_UP_END
};
```

### Replace `sKakunaLevelUpLearnset`

```c
static const u16 sKakunaLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_HARDEN),
    LEVEL_UP_MOVE(1, MOVE_POISON_STING),
    LEVEL_UP_MOVE(7, MOVE_HARDEN),
    LEVEL_UP_MOVE(10, MOVE_FURY_ATTACK),
    LEVEL_UP_END
};
```

### Replace `sBeedrillLevelUpLearnset`

```c
static const u16 sBeedrillLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(1, MOVE_POISON_STING),
    LEVEL_UP_MOVE(10, MOVE_FURY_ATTACK),
    LEVEL_UP_MOVE(15, MOVE_FOCUS_ENERGY),
    LEVEL_UP_MOVE(20, MOVE_TWINEEDLE),
    LEVEL_UP_MOVE(25, MOVE_RAGE),
    LEVEL_UP_MOVE(30, MOVE_PURSUIT),
    LEVEL_UP_MOVE(35, MOVE_PIN_MISSILE),
    LEVEL_UP_MOVE(40, MOVE_AGILITY),
    LEVEL_UP_MOVE(45, MOVE_ENDEAVOR),
    LEVEL_UP_END
};
```

## BRRBRR line

Original slots:

```txt
Pikachu -> Raichu
```

Brainrot line for first build:

```txt
BRRBRR -> PATAPIM
```

Role:

- rare forest shock/noise Brainrot
- fast
- annoying status
- dangerous if found early

### Replace `sPikachuLevelUpLearnset`

```c
static const u16 sPikachuLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_THUNDER_SHOCK),
    LEVEL_UP_MOVE(1, MOVE_GROWL),
    LEVEL_UP_MOVE(6, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(8, MOVE_THUNDER_WAVE),
    LEVEL_UP_MOVE(11, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(15, MOVE_DOUBLE_TEAM),
    LEVEL_UP_MOVE(20, MOVE_SLAM),
    LEVEL_UP_MOVE(26, MOVE_THUNDERBOLT),
    LEVEL_UP_MOVE(33, MOVE_AGILITY),
    LEVEL_UP_MOVE(41, MOVE_THUNDER),
    LEVEL_UP_MOVE(50, MOVE_LIGHT_SCREEN),
    LEVEL_UP_END
};
```

For now this can stay almost the same because it already fits BRRBRR well.

### Replace `sRaichuLevelUpLearnset`

```c
static const u16 sRaichuLevelUpLearnset[] = {
    LEVEL_UP_MOVE(1, MOVE_THUNDER_SHOCK),
    LEVEL_UP_MOVE(1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE(1, MOVE_QUICK_ATTACK),
    LEVEL_UP_MOVE(1, MOVE_THUNDERBOLT),
    LEVEL_UP_MOVE(1, MOVE_THUNDER_WAVE),
    LEVEL_UP_MOVE(1, MOVE_DOUBLE_TEAM),
    LEVEL_UP_END
};
```

## Future custom move names

These are flavor names only for later.

| Current move | Future Brainrot name |
|---|---|
| STRING_SHOT | Crostini Thread |
| STUN_SPORE | Forest Freeze |
| CONFUSION | Bambi Dizzy |
| POISON_STING | Larila Sting |
| FURY_ATTACK | Lirili Rush |
| THUNDER_SHOCK | Brr Shock |
| THUNDER_WAVE | Patapim Pulse |
| DOUBLE_TEAM | Brr Clone |

## Balance note

BAMBINI gets early STUN_SPORE so it is useful.

LIRILI gets early FURY_ATTACK so it feels aggressive.

BRRBRR stays rare, so it can be strong.

## First playable result

Zone Green 01 now has clear battle roles:

```txt
BAMBINI line = support/status/confusion
LIRILI line = poison/aggressive hits
BRRBRR line = rare speed/electric/noise
```
