# Roan house text patch

This patch changes the player's house into Roan's house and adds early hints about Luna.

## File 1

Target file:

`data/maps/PalletTown_PlayersHouse_1F/text.inc`

Replace the whole file with this:

```c
PalletTown_PlayersHouse_1F_Text_AllBoysLeaveOakLookingForYou::
    .string "MOM: ...Right.\n"
    .string "You are really going.\p"
    .string "Dr. Avelar was looking for you.\p"
    .string "He said the License test starts\n"
    .string "today.\p"
    .string "Roan... please be careful.\p"
    .string "And stop asking about that girl.\n"
    .string "You never had a sister.$"

PalletTown_PlayersHouse_1F_Text_AllGirlsLeaveOakLookingForYou::
    .string "MOM: ...Right.\n"
    .string "You are really going.\p"
    .string "Dr. Avelar was looking for you.\p"
    .string "He said the License test starts\n"
    .string "today.\p"
    .string "Roan... please be careful.\p"
    .string "And stop asking about that girl.\n"
    .string "You never had a sister.$"

PalletTown_PlayersHouse_1F_Text_YouShouldTakeQuickRest::
    .string "MOM: Roan!\n"
    .string "You should take a quick rest.\p"
    .string "You keep waking up after saying\n"
    .string "the same name... Luna.$"

PalletTown_PlayersHouse_1F_Text_LookingGreatTakeCare::
    .string "MOM: Oh, good.\n"
    .string "You and your BRAINROT look fine.\p"
    .string "I still do not like this, but...\p"
    .string "Take care now.$"

PalletTown_PlayersHouse_1F_Text_MovieOnTVFourBoysOnRailroad::
    .string "There is a news program on TV.\p"
    .string "COGNIA says Brainrot activity is\n"
    .string "normal and under control.\p"
    .string "...That sounds fake.$"

PalletTown_PlayersHouse_1F_Text_MovieOnTVGirlOnBrickRoad::
    .string "There is a news program on TV.\p"
    .string "COGNIA says Brainrot activity is\n"
    .string "normal and under control.\p"
    .string "...That sounds fake.$"

PalletTown_PlayersHouse_1F_Text_OopsWrongSide::
    .string "Wrong side.\p"
    .string "For a second, you thought you\n"
    .string "heard someone laughing upstairs.$"
```

## File 2

Target file:

`data/maps/PalletTown_PlayersHouse_2F/text.inc`

Replace the whole file with this:

```c
PalletTown_PlayersHouse_2F_Text_PlayedWithNES::
    .string "There is an old console here.\p"
    .string "Two save files are listed.\p"
    .string "ROAN\n"
    .string "LUNA\p"
    .string "The second name flickers, then\n"
    .string "vanishes.\p"
    .string "...Okay.\n"
    .string "It is time to go.$"

PalletTown_PlayersHouse_2F_Text_PressLRForHelp::
    .string "It is a posted notice...\p"
    .string "If your thoughts feel foggy,\n"
    .string "ask for HELP.\p"
    .string "Press the L or R Button!$"
```

## Story purpose

This patch tells the player immediately that:

- Roan remembers Luna.
- His mom does not remember her.
- Cognia is hiding something.
- The world is treating Brainrots as normal.

This should make the opening feel creepy without needing a new cutscene yet.
