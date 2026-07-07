# New game intro code patch

Target file:

`src/oak_speech.c`

This patch makes the new game intro closer to Brainrot: Echoes of Sahur.

## Current confirmed code

The intro species is currently:

```c
#define INTRO_SPECIES SPECIES_NIDORAN_F
```

The male name list and rival name list are also inside `src/oak_speech.c`.

## Goal

- Show a starter-related Brainrot placeholder in the intro.
- Add ROAN as a default player name.
- Add KIUNIN as the default rival name.

## Step 1: change intro species

Replace:

```c
#define INTRO_SPECIES SPECIES_NIDORAN_F
```

With:

```c
#define INTRO_SPECIES SPECIES_SQUIRTLE
```

Why:

After the species name patch, Squirtle's slot becomes TRALALERO.

So the intro will use the Squirtle placeholder sprite, but the Brainrot identity will be Tralalero Tralala.

## Step 2: add custom name strings

Add this near the other static text/name declarations, before `sMaleNameChoices`:

```c
static const u8 sNameChoice_Roan[] = _("ROAN");
static const u8 sNameChoice_Kiunin[] = _("KIUNIN");
```

## Step 3: put ROAN first in male names

Find:

```c
static const u8 *const sMaleNameChoices[] =
{
#if defined(FIRERED)
    gNameChoice_Red,
    gNameChoice_Fire,
    gNameChoice_Ash,
    gNameChoice_Kene,
    gNameChoice_Geki,
```

Change it to:

```c
static const u8 *const sMaleNameChoices[] =
{
    sNameChoice_Roan,
#if defined(FIRERED)
    gNameChoice_Red,
    gNameChoice_Fire,
    gNameChoice_Ash,
    gNameChoice_Kene,
    gNameChoice_Geki,
```

This makes ROAN appear as the first suggested name.

## Step 4: put ROAN first in female names too

This project is centered on Roan, so even if the player selects the other sprite, the first suggested name can still be ROAN.

Find:

```c
static const u8 *const sFemaleNameChoices[] =
{
#if defined(FIRERED)
    gNameChoice_Red,
    gNameChoice_Fire,
```

Change it to:

```c
static const u8 *const sFemaleNameChoices[] =
{
    sNameChoice_Roan,
#if defined(FIRERED)
    gNameChoice_Red,
    gNameChoice_Fire,
```

## Step 5: replace rival choices with KIUNIN first

Find:

```c
static const u8 *const sRivalNameChoices[] =
{
#if defined(FIRERED)
    gNameChoice_Green,
    gNameChoice_Gary,
    gNameChoice_Kaz,
    gNameChoice_Toru
#elif defined(LEAFGREEN)
    gNameChoice_Red,
    gNameChoice_Ash,
    gNameChoice_Kene,
    gNameChoice_Geki
#endif
};
```

Replace with:

```c
static const u8 *const sRivalNameChoices[] =
{
    sNameChoice_Kiunin,
#if defined(FIRERED)
    gNameChoice_Green,
    gNameChoice_Gary,
    gNameChoice_Kaz,
    gNameChoice_Toru
#elif defined(LEAFGREEN)
    gNameChoice_Red,
    gNameChoice_Ash,
    gNameChoice_Kene,
    gNameChoice_Geki
#endif
};
```

## Expected in-game result

When starting a new game:

- The intro Brainrot placeholder should be based on Squirtle, later named TRALALERO.
- ROAN appears as a suggested player name.
- KIUNIN appears as a suggested rival name.

## Build safety

This is a safer code change than adding new species.

It only changes:

- one species define
- two local name strings
- name choice arrays

If the build fails, revert this file first.
