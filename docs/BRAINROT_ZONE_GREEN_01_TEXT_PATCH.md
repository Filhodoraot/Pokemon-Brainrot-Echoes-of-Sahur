# Zone Green 01 text patch

Target file:

`data/maps/ViridianForest/text.inc`

This patch rewrites Viridian Forest into Zone Green 01.

## Goal

Zone Green 01 should be the first place where the story gets darker.

The player should feel:

- this is not just a normal forest
- Brainrots were once called field demons
- the Cult of the First Sound is nearby
- Sahur Noise can make people forget things
- Kiunin is starting to break through the mental lock

## Language rule

Actual ROM text stays English first.

PT-BR version is included here for translation planning.

Do not use accents inside ROM text until charset support is confirmed.

## Replace full file with this EN version first

```asm
ViridianForest_Text_FriendsItchingToBattle::
    .string "This is ZONE GREEN 01.\n"
    .string "Wild BRAINROTS react to sound.\p"
    .string "If one repeats your voice,\n"
    .string "do not answer it.$"

ViridianForest_Text_RickIntro::
    .string "Hey! You have a BRAINROT!\n"
    .string "Then prove your mind is stable!$"

ViridianForest_Text_RickDefeat::
    .string "No!\n"
    .string "BAMBINI froze up!$"

ViridianForest_Text_RickPostBattle::
    .string "The forest used to be normal.\p"
    .string "Then the sounds came.\n"
    .string "Tung... tung...$"

ViridianForest_Text_DougIntro::
    .string "You hear it too, right?\n"
    .string "That little knock in the trees?$"

ViridianForest_Text_DougDefeat::
    .string "Huh?\n"
    .string "The sound stopped.$"

ViridianForest_Text_DougPostBattle::
    .string "People called them field demons.\p"
    .string "Now everyone acts like\n"
    .string "they were always here.$"

ViridianForest_Text_SammyIntro::
    .string "Wait!\n"
    .string "Do not rush in this forest!$"

ViridianForest_Text_SammyDefeat::
    .string "You kept focus...\n"
    .string "That is rare.$"

ViridianForest_Text_SammyPostBattle::
    .string "I found a wood shard here.\p"
    .string "When I touched it, I forgot\n"
    .string "why I was crying.$"

ViridianForest_Text_AnthonyIntro::
    .string "Small BRAINROTS can still\n"
    .string "break your head!$"

ViridianForest_Text_AnthonyDefeat::
    .string "My head feels loud...$"

ViridianForest_Text_AnthonyPostBattle::
    .string "A man in a green mask told me:\p"
    .string "Thinking hurts.\n"
    .string "Repeating saves.$"

ViridianForest_Text_CharlieIntro::
    .string "Did you know BRAINROTS evolve?\p"
    .string "Some grow.\n"
    .string "Some only change when watched.$"

ViridianForest_Text_CharlieDefeat::
    .string "Oh!\n"
    .string "My LIRILI lost!$"

ViridianForest_Text_CharliePostBattle::
    .string "BAMBINI and LIRILI grow fast.\p"
    .string "But BRRBRR is rare.\n"
    .string "It appears when the trees knock.$"

ViridianForest_Text_RanOutOfPokeBalls::
    .string "I threw all my BRAINROT BALLS.\p"
    .string "One NOOBINI copied my voice\n"
    .string "and made me waste them.$"

ViridianForest_Text_AvoidGrassyAreasWhenWeak::
    .string "TRAINER TIPS\p"
    .string "If your mind feels noisy,\n"
    .string "leave the grass.\p"
    .string "Weak teams attract wild\n"
    .string "BRAINROTS.$"

ViridianForest_Text_UseAntidoteForPoison::
    .string "For poison, use ANTIDOTE!\p"
    .string "LIRILI stings are small,\n"
    .string "but the fever is not.$"

ViridianForest_Text_ContactOakViaPCToRatePokedex::
    .string "COGNIA NOTICE\p"
    .string "Report strange sounds,\n"
    .string "memory loss, or repeated words.\p"
    .string "Do not spread panic.$"

ViridianForest_Text_CantCatchOwnedMons::
    .string "TRAINER TIPS\p"
    .string "You cannot catch a BRAINROT\n"
    .string "that belongs to someone else.\p"
    .string "Throw BALLS only at wild\n"
    .string "BRAINROTS.$"

ViridianForest_Text_WeakenMonsBeforeCapture::
    .string "TRAINER TIPS\p"
    .string "Weaken BRAINROTS before\n"
    .string "capture.\p"
    .string "A calm target breaks fewer\n"
    .string "BALLS.$"

ViridianForest_Text_LeavingViridianForest::
    .string "LEAVING ZONE GREEN 01\n"
    .string "LICENSE D CITY AHEAD$"
```

## Extra story scene to add later

This needs a new event or script later.

Use this as the Sahur Fragment scene.

### EN scene

```asm
ZoneGreen01_Text_SahurFragmentFound::
    .string "A cold wooden shard lies\n"
    .string "under the roots.\p"
    .string "It knocks once.\n"
    .string "Tung.\p"
    .string "ROAN remembered LUNA's voice.$"

ZoneGreen01_Text_KiuninLockStart::
    .string "KIUNIN: Wait...\n"
    .string "Luna was real?\p"
    .string "No. That makes no sense.\n"
    .string "You are lying.\p"
    .string "Why do I feel like\n"
    .string "I knew that name?$"
```

### PT-BR scene planning

Do not put this in ROM yet unless PT-BR build is being made.

```asm
ZoneGreen01_Text_SahurFragmentFound_PTBR::
    .string "Um fragmento de madeira fria\n"
    .string "esta sob as raizes.\p"
    .string "Ele bate uma vez.\n"
    .string "Tung.\p"
    .string "ROAN lembrou da voz de LUNA.$"

ZoneGreen01_Text_KiuninLockStart_PTBR::
    .string "KIUNIN: Espera...\n"
    .string "Luna era real?\p"
    .string "Nao. Isso nao faz sentido.\n"
    .string "Voce esta mentindo.\p"
    .string "Por que parece que\n"
    .string "eu conhecia esse nome?$"
```

## Kiunin arc in this area

This is the first moment where Kiunin almost understands Roan.

But Cognitive Lock pulls him away.

He reacts with anger because fear is easier than truth.

## Zone Green 01 story beat

Roan should leave the forest with:

```txt
Sahur Fragment
```

Kiunin should leave with:

```txt
first crack in Cognitive Lock
```

The player should understand:

```txt
The world is lying.
Some people almost remember.
The forest knows more than the towns.
```

## PT-BR translation style later

Use simple Brazilian Portuguese:

- nao instead of não
- voce instead of você
- memoria instead of memória
- crianca instead of criança

Only use accents if the font/charset is confirmed safe.
