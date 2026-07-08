# Roan Character Model Plan

This file defines the first real visual identity pass for **Roan**, replacing the vanilla Red look.

## Why this exists

The current playtest still looks too close to FireRed because the protagonist still uses Red's silhouette.

Roan needs a new silhouette, not only renamed dialogue.

## Roan final direction

Roan is not a normal trainer.

He is a 16-year-old who remembers Luna when everyone else forgot her.
He studies Brainrots because he hates and fears them, not because he dreams of being champion.

### Visual identity

- no cap
- visible dark messy hair
- dark hoodie or dark short jacket
- black or navy pants
- small blue or orange detail
- serious/tired eyes
- street researcher vibe
- should look practical, not sporty

### Palette idea

- hair: very dark brown / black
- jacket: navy / black
- shirt detail: pale blue or orange
- pants: dark gray
- shoes: muted blue or gray

## Main no-cap overworld model

The overworld sprite should be based on this idea:

```text
A 16-year-old boy protagonist for a GBA Pokémon FireRed-style ROM hack.
No cap. Messy dark hair visible from all directions.
Dark navy hoodie or short jacket, dark pants, small orange or cyan accent.
Serious expression, cautious posture, street researcher vibe.
Readable 16-color pixel art, top-down RPG overworld sprite sheet, 4 directions walking.
Transparent background.
```

## Needed Roan files

### Overworld/object event files

The FireRed decomp uses Red object-event graphics here:

```text
graphics/object_events/pics/people/red_normal.4bpp
graphics/object_events/pics/people/red_surf_run.4bpp
graphics/object_events/pics/people/red_item.4bpp
graphics/object_events/pics/people/red_surf.4bpp
graphics/object_events/pics/people/red_bike.4bpp
graphics/object_events/pics/people/red_vs_seeker_bike.4bpp
graphics/object_events/pics/people/red_fish.4bpp
graphics/object_events/palettes/player.gbapal
graphics/object_events/palettes/player_reflection.gbapal
```

Minimum for first visual pass:

1. `red_normal`
2. `player.gbapal`
3. `player_reflection.gbapal`

Later pass:

1. item pose
2. surf/run
3. bike
4. fishing
5. VS seeker bike

## Battle and menu files still needed

Roan also needs:

- trainer back sprite
- trainer front/card sprite
- intro/name select sprite if used
- palette for each if separate

These are separate from the overworld sheet.

## Brainrot tool/reference search

### Useful GitHub tool found: Porypal

Porypal is made for Pokémon Gen 3 ROM hacking and supports pokeemerald, pokefirered, and pokeemerald-expansion.

Why it matters:

- GBA sprites need 16 colors per palette.
- Porypal can extract palettes, reduce sprite colors, and apply palettes.
- This is useful after we draw Roan/Brainrots, before inserting into the game.

Repo:

```text
Loxed/porypal
```

### Useful generation workflow found: SpriteBrew

SpriteBrew is not a direct FireRed model, but it can generate and animate pixel sprite sheets from text descriptions. It can export game-ready sheets for engines, and has tools like slicing and pixel-perfect resizing.

Repo found:

```text
mrudinal/spritebrew-2d-assets
```

Use as a workflow/reference only. Do not copy random sprites without checking license.

## Best workflow for Roan

1. Generate or draw a 64x64 concept of Roan.
2. Turn that into a 4-direction overworld walking sheet.
3. Limit it to 16 colors with Porypal or another palette tool.
4. Convert it into GBA format.
5. Replace only `red_normal` first.
6. Test in-game.
7. Then replace surf/bike/item versions.

## Important note

A palette edit can make Red darker, but it cannot remove the cap.

To actually remove the cap, we need a new sprite sheet.
