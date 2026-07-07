# PT-BR / EN localization plan

Brainrot: Echoes of Sahur should support both:

- English
- Portuguese Brazilian / PT-BR

## Main rule

The first playable build should be built safely first.

Do not break the ROM trying to add a full language selector too early.

## Safe development order

### Phase 1: English playable build

Use English text in the actual source files first.

Why:

- The base FireRed decomp is English.
- Text length is safer.
- The GBA font/charset handles English more easily.
- It helps avoid broken accents and formatting bugs.

### Phase 2: PT-BR script mirror

Create Portuguese versions in docs first.

Example:

```txt
EN: This Brainrot reacts to Sahur noise.
PT-BR: Esse Brainrot reage ao ruido Sahur.
```

Do not use accents in ROM text until charset support is confirmed.

Safe PT-BR style for GBA text:

```txt
voce -> not voce with accent
memoria -> not memoria with accent
crianca -> not crianca with accent
```

### Phase 3: choose implementation

There are two possible paths:

#### Option A: two ROM builds

```txt
Brainrot Echoes of Sahur EN.gba
Brainrot Echoes of Sahur PTBR.gba
```

This is the safest.

Each build uses different text files.

#### Option B: in-game language selector

The game asks at the start:

```txt
LANGUAGE?
ENGLISH
PORTUGUES
```

This is cooler, but harder.

It needs code changes to load different text depending on a save variable.

For the first playable build, do not do this yet.

## Recommended plan

Use Option A first.

Make two builds later:

1. EN build
2. PT-BR build

After the game is stable, consider Option B.

## File naming rule

For docs and scripts, use this style:

```txt
_TEXT_EN.md
_TEXT_PTBR.md
```

Examples:

```txt
BRAINROT_ROAN_HOUSE_TEXT_EN.md
BRAINROT_ROAN_HOUSE_TEXT_PTBR.md
BRAINROT_LAB_TEXT_EN.md
BRAINROT_LAB_TEXT_PTBR.md
```

## Translation style

### English tone

- mysterious
- simple
- readable
- Pokemon-like but darker

### PT-BR tone

- natural Brazilian Portuguese
- simple words
- not too formal
- not full meme chaos all the time

Example:

EN:

```txt
Roan, that sound is not normal.
It is inside people's memories.
```

PT-BR:

```txt
Roan, esse som nao e normal.
Ele esta dentro das memorias das pessoas.
```

## Important text limit

GBA text boxes are small.

Keep lines short.

Bad:

```txt
The cognitive corruption caused by Sahur noise is becoming extremely dangerous.
```

Good:

```txt
Sahur noise is getting worse.
It is eating memories.
```

## Current project rule

From now on, story docs can have both English and PT-BR.

Actual ROM patches should stay English until the first playable build works.

After that, create PT-BR versions.

## Final goal

The final game should be playable in:

```txt
English
Portuguese Brazilian
```

But first priority is making the ROM playable.
