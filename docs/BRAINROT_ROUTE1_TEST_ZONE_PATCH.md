# Route 1 / Test Zone 01 patch

Target file:

`data/maps/Route1/text.inc`

Replace the whole file with this:

```c
Route1_Text_WorkAtPokeMartTakeSample::
    .string "Hi!\n"
    .string "I work for the supply desk at\n"
    .string "Training Center 01.\p"
    .string "This road is now a test zone\n"
    .string "for new Brainrot trainers.\p"
    .string "If your partner gets hurt, do not\n"
    .string "panic. Use this sample.\p"
    .string "Here you go!$"

Route1_Text_ComeSeeUsIfYouNeedPokeBalls::
    .string "Come see us in Viridian if you\n"
    .string "need BRAINROT BALLS.\p"
    .string "And do not stare too long at\n"
    .string "wild Brainrots. Trust me.$"

Route1_Text_PutPotionAway::
    .string "{PLAYER} put the POTION away in\n"
    .string "the BAG's ITEMS POCKET.$"

Route1_Text_CanJumpFromLedges::
    .string "See those ledges along the road?\p"
    .string "Trainers use them to retreat\n"
    .string "fast from unstable Brainrots.\p"
    .string "It looks dumb, but it works.\p"
    .string "You can return to Training Center\n"
    .string "01 quicker that way.$"

Route1_Text_RouteSign::
    .string "TEST ZONE 01\n"
    .string "TRAINING CENTER 01 - VIRIDIAN SAFE ZONE$"
```

## Story purpose

Route 1 becomes the first controlled outdoor test for new Brainrot trainers.

Roan is still uncomfortable around Brainrots here. Other people act like the situation is normal, which supports the cognitive fall lore.

## First wild Brainrots for this zone

Use these as the first encounter replacements later:

| Original early slot idea | Brainrot replacement | Role |
|---|---|---|
| Rattata | Pipi Kiwi | easy first catch |
| Pidgey | Noobini Pizzanini | basic meme enemy |
| extra common slot | Tim Cheese | fast annoying enemy |
| extra rare slot | Raccooni Jandelini | rare item-thief style Brainrot |

## Recommended encounter levels

| Brainrot | Level range | Rarity |
|---|---:|---|
| Pipi Kiwi | 2-4 | common |
| Noobini Pizzanini | 2-4 | common |
| Tim Cheese | 3-5 | uncommon |
| Raccooni Jandelini | 4-5 | rare |

## Important

For the first playable build, do not add new species yet.

Safer temporary mapping:

- Rattata slot becomes Pipi Kiwi by name/data.
- Pidgey slot becomes Noobini Pizzanini by name/data.
- Add Tim Cheese and Raccooni later after the first build compiles.

This keeps the ROM stable while the first test zone is being built.
