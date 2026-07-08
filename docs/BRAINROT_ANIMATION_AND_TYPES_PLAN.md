# Brainrot animation and type plan

This file explains how sprites, animations, and battle types should work for **Pokemon Brainrot: Echoes of Sahur**.

## 1. Sprite animation plan

FireRed/GBA does not need huge frame-by-frame monster animations like modern games. The safest pipeline is:

1. Add clean static sprites first.
2. Give each Brainrot a simple battle entrance animation.
3. Add icon/menu motion later.
4. Only create special overworld animations for rare story Brainrots.

## 2. Sprite files needed first

Every Brainrot form needs:

```text
front.png  - 64x64 battle front sprite
back.png   - 64x64 battle back sprite
icon.png   - 32x64 menu icon sheet
```

Rules:

- Transparent background.
- GBA-friendly colors.
- Readable silhouette.
- Not too much detail.
- Final evolutions should look stronger and more threatening.
- Legendaries get one form only.

## 3. Animation categories

Use these categories when choosing later animations:

### Bounce

For funny, small, goofy Brainrots.

Examples:

- NOOBINI
- PIPIKIWI
- TIMCHEESE

Motion idea:

- little hop
- squash/stretch feeling
- quick idle wobble

### Slash / Dash

For fast, aggressive, assassin-like Brainrots.

Examples:

- CAPPUCINO
- HARPUCINO
- CAPASSINO
- LIRILORD

Motion idea:

- quick shake
- tiny forward lunge
- sharp impact frame

### Wave / Swim

For aquatic Brainrots.

Examples:

- TRALALERO
- TRALALITO
- TRALALORD

Motion idea:

- up/down bob
- water-like sway
- attack lean upward

### Stomp / Heavy

For strong or stone-like Brainrots.

Examples:

- TUNGMINI
- TUNGMED
- TUNGROCK
- SLEEPROT

Motion idea:

- heavy shake
- small dust/impact feeling
- slow aggressive entrance

### Glitch / Echo

For story, memory, Sahur, or 67-related Brainrots.

Examples:

- TUNG TUNG TUNG SAHUR
- 67
- TRUE 67
- SAHUR CORE

Motion idea:

- flicker
- palette pulse
- tiny repeated shake
- slow ominous entrance

## 4. When to add animations

Do not animate before the sprites are final.

Correct order:

```text
1. Finish sprite PNGs
2. Import front/back/icon sprites
3. Test battle display
4. Assign simple animation category
5. Polish animation after seeing it in-game
```

## 5. Type system plan

For the first playable build, the game keeps the original FireRed type engine.

That means no brand-new battle types yet, because adding new types touches:

- type chart
- battle UI
- move data
- text graphics
- type icons
- compatibility with tools

Instead, Brainrots use existing Pokemon types in new combinations.

Later, type names can be visually reflavored if needed.

## 6. Current early Brainrot type identities

### Starters

| Brainrot line | Type |
|---|---|
| CHIMPANZI -> BANANINI -> AVOCADOR | Grass / Fighting |
| CAPPUCINO -> HARPUCINO -> CAPASSINO | Fire / Dark |
| TRALALERO -> TRALALITO -> TRALALORD | Water / Dark |

### Test Zone 01

| Brainrot line | Type |
|---|---|
| NOOBINI -> PIZZANINI -> LOSNOOBI | Normal / Flying |
| PIPIKIWI -> PIPICORNI | Normal / Grass |
| TIMCHEESE | Normal |
| RACCOONI | Dark / Normal |

### Zone Green 01

| Brainrot line | Type |
|---|---|
| BAMBINI -> CROSTINI -> BAMBILORD | Bug / Grass |
| LIRILI -> LARILA -> LIRILORD | Bug / Poison |
| BRRBRR -> PATAPIM | Electric / Grass |

### Cave/checkpoint

| Brainrot line | Type |
|---|---|
| TRIPPI -> TROPPILORD | Ghost / Flying |
| TUNGMINI -> TUNGMED -> TUNGROCK | Rock / Fighting |
| MOONINI -> MOONLORD | Psychic / Normal |
| SLEEPROT | Normal / Psychic |

## 7. Later type ideas

If we decide to fully reskin type names later, possible flavor names:

| Current type | Brainrot flavor idea |
|---|---|
| Normal | Meme |
| Fire | Caffeine |
| Water | Wave |
| Grass | Field |
| Electric | Signal |
| Psychic | Mind |
| Ghost | Echo |
| Dark | Rot |
| Fighting | Rage |
| Rock | Core |
| Poison | Toxic |
| Bug | Swarm |
| Flying | Air |

This should only be done after the first playable build is stable.
