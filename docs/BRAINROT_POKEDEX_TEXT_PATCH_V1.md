# Braindex / Pokedex text patch V1

This patch changes early Pokedex text into Brainrot/Braindex lore.

## Confirmed files

Entry table:

`src/data/pokemon/pokedex_entries.h`

Pokedex text include:

`src/data/pokemon/pokedex_text.h`

FireRed text file:

`src/data/pokemon/pokedex_text_fr.h`

For FireRed, edit `pokedex_text_fr.h`.

## Design rule

The visible species name stays short.

The stage appears in the Braindex description:

- Baby Brainrot stage
- Teen Brainrot stage
- Adult Brainrot stage

## Patch 1: category names

Target file:

`src/data/pokemon/pokedex_entries.h`

Change these category names only.

### Starter line categories

```c
[NATIONAL_DEX_BULBASAUR] =
{
    .categoryName = _("BABY"),
```

```c
[NATIONAL_DEX_IVYSAUR] =
{
    .categoryName = _("TEEN"),
```

```c
[NATIONAL_DEX_VENUSAUR] =
{
    .categoryName = _("ADULT"),
```

```c
[NATIONAL_DEX_CHARMANDER] =
{
    .categoryName = _("BABY"),
```

```c
[NATIONAL_DEX_CHARMELEON] =
{
    .categoryName = _("TEEN"),
```

```c
[NATIONAL_DEX_CHARIZARD] =
{
    .categoryName = _("ADULT"),
```

```c
[NATIONAL_DEX_SQUIRTLE] =
{
    .categoryName = _("BABY"),
```

```c
[NATIONAL_DEX_WARTORTLE] =
{
    .categoryName = _("TEEN"),
```

```c
[NATIONAL_DEX_BLASTOISE] =
{
    .categoryName = _("ADULT"),
```

### Route 1 categories

```c
[NATIONAL_DEX_PIDGEY] =
{
    .categoryName = _("BABY"),
```

```c
[NATIONAL_DEX_PIDGEOTTO] =
{
    .categoryName = _("TEEN"),
```

```c
[NATIONAL_DEX_PIDGEOT] =
{
    .categoryName = _("ADULT"),
```

```c
[NATIONAL_DEX_RATTATA] =
{
    .categoryName = _("BABY"),
```

```c
[NATIONAL_DEX_RATICATE] =
{
    .categoryName = _("ADULT"),
```

```c
[NATIONAL_DEX_SPEAROW] =
{
    .categoryName = _("TEEN"),
```

```c
[NATIONAL_DEX_FEAROW] =
{
    .categoryName = _("ADULT"),
```

## Patch 2: starter Braindex text

Target file:

`src/data/pokemon/pokedex_text_fr.h`

Replace the following text constants.

### CHIMPANZI / Bulbasaur slot

```c
const u8 gBulbasaurPokedexText[] = _(
    "Baby Brainrot stage. It beats its\n"
    "hands on the ground when it senses\n"
    "Sahur noise nearby.");
```

### BANANINI / Ivysaur slot

```c
const u8 gIvysaurPokedexText[] = _(
    "Teen Brainrot stage. Its body grows\n"
    "stronger when people repeat nonsense\n"
    "without questioning it.");
```

### AVOCADOR / Venusaur slot

```c
const u8 gVenusaurPokedexText[] = _(
    "Adult Brainrot stage. It protects its\n"
    "trainer with brute force, but reacts\n"
    "badly to memory attacks.");
```

### CAPPUCINO / Charmander slot

```c
const u8 gCharmanderPokedexText[] = _(
    "Baby Brainrot stage. It moves too\n"
    "fast for its own mind and attacks\n"
    "before it understands danger.");
```

### HARPUCINO / Charmeleon slot

```c
const u8 gCharmeleonPokedexText[] = _(
    "Teen Brainrot stage. Its sharp rushes\n"
    "leave hot traces in the air like\n"
    "burnt coffee and panic.");
```

### CAPASSINO / Charizard slot

```c
const u8 gCharizardPokedexText[] = _(
    "Adult Brainrot stage. It hunts sound\n"
    "patterns and strikes before the enemy\n"
    "can finish a thought.");
```

### TRALALERO / Squirtle slot

```c
const u8 gSquirtlePokedexText[] = _(
    "Baby Brainrot stage. Its simple song\n"
    "sounds harmless, but weak minds may\n"
    "forget small details.");
```

### TRALALITO / Wartortle slot

```c
const u8 gWartortlePokedexText[] = _(
    "Teen Brainrot stage. Groups of them\n"
    "create waves of rhythm that confuse\n"
    "nearby children.");
```

### TRALALORD / Blastoise slot

```c
const u8 gBlastoisePokedexText[] = _(
    "Adult Brainrot stage. Its full call\n"
    "can shake memories loose for a few\n"
    "seconds.");
```

## Patch 3: Route 1 Braindex text

### NOOBINI / Pidgey slot

```c
const u8 gPidgeyPokedexText[] = _(
    "Baby Brainrot stage. It mimics every\n"
    "word it hears and slowly turns those\n"
    "words into nonsense.");
```

### PIZZANINI / Pidgeotto slot

```c
const u8 gPidgeottoPokedexText[] = _(
    "Teen Brainrot stage. It becomes loud\n"
    "and competitive, copying stronger\n"
    "voices to feel important.");
```

### LOSNOOBI / Pidgeot slot

```c
const u8 gPidgeotPokedexText[] = _(
    "Adult Brainrot stage. It gathers weak\n"
    "minds into a group rhythm that spreads\n"
    "fast through towns.");
```

### PIPIKIWI / Rattata slot

```c
const u8 gRattataPokedexText[] = _(
    "Baby Brainrot stage. It looks harmless\n"
    "and small, but it steals attention by\n"
    "chirping the same note.");
```

### PIPICORNI / Raticate slot

```c
const u8 gRaticatePokedexText[] = _(
    "Adult Brainrot stage. Its horn grows\n"
    "after long exposure to Sahur noise\n"
    "near test zones.");
```

### TIMCHEESE / Spearow slot

```c
const u8 gSpearowPokedexText[] = _(
    "Teen Brainrot stage. It moves quickly\n"
    "and annoys enemies until they make\n"
    "careless mistakes.");
```

### RACCOONI / Fearow slot

```c
const u8 gFearowPokedexText[] = _(
    "Adult Brainrot stage. It steals small\n"
    "objects and hides them in places that\n"
    "make no logical sense.");
```

## Important charset rule

Do not use accents.

Use:

- Brainrot
- Sahur
- memory
- stage

Avoid:

- memória
- estágio
- cérebro

The GBA text system may not like random accented text.

## First build goal

After this patch, the Braindex will already explain Baby/Teen/Adult without any new sprite work.
