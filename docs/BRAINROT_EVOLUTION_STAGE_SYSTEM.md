# Brainrot evolution stage system

This is the official evolution system for Brainrot: Echoes of Sahur.

## Core idea

Every Brainrot can have three growth stages:

1. Baby
2. Teen
3. Adult

These stages are part of the species data and lore, but they do not need to appear in the visible Pokemon name.

Example:

- Visible name: TRALALERO
- Internal/lore stage: Baby
- Later visible name can still be TRALALERO or use a short evolution name if needed.

## Why this works

Pokemon FireRed has short species names.

If every species name included Baby, Teen, and Adult, the names would become ugly and too long.

So the clean system is:

```txt
Name shown in battle: clean Brainrot name
Stage info: stored in data, docs, Pokedex text, stats, and evolution line
```

## Stage meanings

### Baby stage

Baby Brainrots are unstable and simple.

Traits:
- low stats
- easy to catch
- weird behavior but not fully dangerous
- learn simple moves
- common in early routes

Story meaning:
- the world treats them as normal pets
- Roan feels something wrong even with weak ones

### Teen stage

Teen Brainrots are more aggressive and identity-driven.

Traits:
- medium stats
- stronger moves
- more chaotic behavior
- start showing their real theme

Story meaning:
- Teen Brainrots reveal that the species are not just jokes
- their sounds and habits affect human memory more clearly

### Adult stage

Adult Brainrots are complete forms.

Traits:
- high stats
- signature moves
- stronger abilities later
- more stable identity
- usually used by stronger trainers

Story meaning:
- Adult Brainrots are dangerous enough to shape zones
- some can become alpha bosses or legendary-linked forms

## In-game implementation

The game does not need a new field named `stage` at first.

For the first build, the stage can be represented through:

- species slot
- stats
- evolution line
- Pokedex description
- move learnset
- encounter level

Later, if needed, custom code can add an actual `brainrotStage` field.

## First build implementation

Use existing evolution slots.

Example with starter lines:

| Slot | Visible name | Stage | Full lore name |
|---|---|---|---|
| Bulbasaur | CHIMPANZI | Baby | Chimpanzini Bananini Baby |
| Ivysaur | BANANINI | Teen | Chimpanzini Bananini Teen |
| Venusaur | AVOCADOR | Adult | Avocadorilla Adult |
| Charmander | CAPPUCINO | Baby | Cappuccino Assassino Baby |
| Charmeleon | HARPUCINO | Teen | Harpuccino Teen |
| Charizard | CAPASSINO | Adult | Cappuccino Assassino Adult |
| Squirtle | TRALALERO | Baby | Tralalero Tralala Baby |
| Wartortle | TRALALITO | Teen | Los Tralaleritos Teen |
| Blastoise | TRALALORD | Adult | Tralalero Tralala Adult |

## Early Route 1 examples

| Slot | Visible name | Stage | Full lore name |
|---|---|---|---|
| Rattata | PIPIKIWI | Baby | Pipi Kiwi Baby |
| Raticate | PIPICORNI | Adult | Pipi Corni Adult |
| Pidgey | NOOBINI | Baby | Noobini Pizzanini Baby |
| Pidgeotto | PIZZANINI | Teen | Noobini Pizzanini Teen |
| Pidgeot | LOSNOOBI | Adult | Los Noobinis Adult |
| Spearow | TIMCHEESE | Baby/Teen | Tim Cheese |
| Fearow | RACCOONI | Adult | Raccooni Jandelini |

## Stage-based stat pattern

### Baby stat range

- BST around 250 to 330
- low HP or low defenses
- simple moves
- common encounters

### Teen stat range

- BST around 350 to 430
- stronger identity
- can carry route bosses
- learns first signature move

### Adult stat range

- BST around 480 to 540
- complete battle role
- stronger ability later
- used in license tests and late routes

### Legendary / God forms

Legendary Brainrots do not always follow Baby/Teen/Adult.

They can have:

- Echo Form
- Guard Form
- True Form
- God Form
- Supreme Form

Examples:

| Brainrot | Form system |
|---|---|
| 67 | Echo -> True 67 |
| Skibidy Toilet | Corrupted -> True Guard |
| Strawberry Helefanto | Memory Guardian -> Tung Guard -> Liberated |
| Tung Tung Sahur | God Form -> Supreme Tung Tung |

## Pokedex stage writing

Pokedex entries should mention the stage without making the battle name huge.

Example:

```txt
TRALALERO
Baby Brainrot stage.
It repeats harmless melodies, but the rhythm can make nearby children forget small details.
```

Teen example:

```txt
TRALALITO
Teen Brainrot stage.
Its group calls create waves of noise that confuse weak minds.
```

Adult example:

```txt
TRALALORD
Adult Brainrot stage.
Its full call can overwrite memories for a few seconds.
```

## Lore rule

A Brainrot does not only evolve physically.

It evolves cognitively.

That means evolution is tied to:

- battle experience
- exposure to Sahur noise
- emotional bond
- memory pressure
- zone corruption

This explains why some Brainrots evolve differently around Roan.

## Roan connection

Because Roan has IQ 150 and Cognitive Resistance, some Brainrots react strangely to him.

They may:

- evolve earlier
- resist Sahur influence
- show hidden memory behavior
- unlock cleaner forms

This can become a special mechanic later.

## Kiunin connection

Kiunin starts trapped by Sahur noise.

His Brainrots may evolve normally at first, chasing strength and fame.

After his lock begins breaking, his Brainrots can start developing more honest or resistant forms.

This mirrors Kiunin maturing from spoiled rival into real ally.

## Development rule

For now, do not add new Baby/Teen/Adult code.

Use existing species slots and evolution chains.

After the first playable build works, then consider custom stage code.

Safe order:

1. Names
2. Stats
3. Pokedex text
4. Evolutions
5. Learnsets
6. Custom stage metadata later
7. Sprites last
