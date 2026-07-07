# Early game dialogue patches

These are safe text replacements to copy into the real game files.

Important: keep text without accents to avoid character issues in the GBA text system.

## File 1

Target file:

`data/maps/PalletTown/text.inc`

Replace the whole file with this:

```c
PalletTown_Text_OakDontGoOut::
    .string "AVELAR: Roan! Wait!\n"
    .string "Do not enter the grass!$"

PalletTown_Text_OakGrassUnsafeNeedMon::
    .string "AVELAR: It is not safe!\p"
    .string "Wild BRAINROTS have been seen\n"
    .string "near the training zone.\p"
    .string "You still do not have a partner\n"
    .string "or a BRAINROT BALL.\p"
    .string "Come with me.\n"
    .string "Your test starts now.$"

PalletTown_Text_RaisingMonsToo::
    .string "I train BRAINROTS, too.\p"
    .string "People say they are normal now,\n"
    .string "but I still do not trust them.$"

PalletTown_Text_CanStoreItemsAndMonsInPC::
    .string "Technology is incredible!\p"
    .string "The PC can store items and\n"
    .string "BRAINROT data.\p"
    .string "The Cognia Institute says it is\n"
    .string "perfectly safe. Weird, right?$"

PalletTown_Text_OakPokemonResearchLab::
    .string "AVELAR BRAINROT RESEARCH LAB$"

PalletTown_Text_PlayersHouse::
    .string "ROAN's house$"

PalletTown_Text_RivalsHouse::
    .string "{RIVAL}'s house$"

PalletTown_Text_TownSign::
    .string "TRAINING CENTER 01\n"
    .string "Where Kanto pretends this is normal.$"

PalletTown_Text_OakLetMeSeePokedex::
    .string "AVELAR: Ah, {PLAYER}.\n"
    .string "You came back alive. Good.\p"
    .string "How much data is inside your\n"
    .string "BRAINDEX now?\p"
    .string "Let me check it.$"

PalletTown_Text_CaughtXPuttingInHonestEffort::
    .string "You registered {STR_VAR_2}...\p"
    .string "Not bad.\p"
    .string "But the zones ahead are worse.\n"
    .string "Keep gathering data.$"

PalletTown_Text_CaughtXImpressiveFollowMe::
    .string "You registered... {STR_VAR_2}!?\p"
    .string "That is strong field work.\p"
    .string "{PLAYER}, I need to show you\n"
    .string "something in the lab.\p"
    .string "Come.\n"
    .string "Follow me.$"

PalletTown_Text_OakYouEnjoyingTraveling::
    .string "AVELAR: You keep going farther\n"
    .string "from the safe zones.\p"
    .string "That is dangerous...\n"
    .string "but also necessary.\p"
    .string "Kanto still hides too much.$"
```

## File 2

Target file:

`data/maps/PalletTown_ProfessorOaksLab/text.inc`

First pass goal:
- Avelar replaces Oak in visible text.
- Pokemon becomes Brainrot in visible text.
- Poke Ball becomes Brainrot Ball in visible text.
- Pokedex becomes Braindex in visible text.
- The first partner scene becomes Roan's first Brainrot License test.

Replacement notes:

- Replace rival waiting text with Brainrot training dialogue.
- Replace starter choice text with the three prototype Brainrots.
- Keep labels exactly the same so scripts do not break.

Suggested key replacements:

```c
PalletTown_ProfessorOaksLab_Text_RivalGrampsIsntAround::
    .string "{RIVAL}: What, only you?\n"
    .string "Dr. Avelar is not here yet.$"

PalletTown_ProfessorOaksLab_Text_RivalFedUpWithWaiting::
    .string "{RIVAL}: Avelar!\n"
    .string "I am done waiting!$"

PalletTown_ProfessorOaksLab_Text_RivalNoFairWhatAboutMe::
    .string "{RIVAL}: Hey! No fair!\n"
    .string "What about my test?$"

PalletTown_ProfessorOaksLab_Text_RivalGoChoosePlayer::
    .string "{RIVAL}: Go on, Roan.\p"
    .string "Pick one.\n"
    .string "I already know mine will win.$"

PalletTown_ProfessorOaksLab_Text_RivalIllTakeThisOneThen::
    .string "{RIVAL}: Then I will take this one!$"

PalletTown_ProfessorOaksLab_Text_RivalReceivedMonFromOak::
    .string "{RIVAL} received {STR_VAR_1}\n"
    .string "from DR. AVELAR!$"

PalletTown_ProfessorOaksLab_Text_RivalMyMonLooksTougher::
    .string "{RIVAL}: My BRAINROT looks way\n"
    .string "tougher than yours.$"

PalletTown_ProfessorOaksLab_Text_RivalLetsCheckOutMons::
    .string "{RIVAL}: Wait, Roan!\p"
    .string "This is your first real test.\n"
    .string "Battle me!$"

PalletTown_ProfessorOaksLab_Text_RivalDefeat::
    .string "WHAT?\n"
    .string "No way!\l"
    .string "You barely even like Brainrots!$"

Text_RivalVictory::
    .string "{RIVAL}: See?\n"
    .string "Brainrot battles are instinct!$"
```

More lab text will be written in the next patch pass.
