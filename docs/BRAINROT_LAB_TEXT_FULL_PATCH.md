# Full lab text patch

Target file:

`data/maps/PalletTown_ProfessorOaksLab/text.inc`

Replace the whole file with the block below.

This keeps every original label name, so the existing scripts should still find the text.

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

PalletTown_ProfessorOaksLab_Text_RivalGoToughenMyMon::
    .string "{RIVAL}: I am going to train\n"
    .string "my BRAINROT until it is wild!\p"
    .string "Roan! Avelar!\n"
    .string "Do not fall behind!$"

PalletTown_ProfessorOaksLab_Text_RivalGramps::
    .string "{RIVAL}: Avelar!$"

PalletTown_ProfessorOaksLab_Text_RivalWhatDidYouCallMeFor::
    .string "{RIVAL}: I almost forgot!\n"
    .string "Why did you call me here?$"

PalletTown_ProfessorOaksLab_Text_RivalLeaveItToMeGramps::
    .string "{RIVAL}: All right, Avelar!\n"
    .string "Leave the field work to me!$"

PalletTown_ProfessorOaksLab_Text_RivalTellSisNotToGiveYouMap::
    .string "Roan, I hate to say it, but you\n"
    .string "are not ready for this.\p"
    .string "I will borrow a TOWN MAP\n"
    .string "from my sis.\p"
    .string "I might even tell her not to\n"
    .string "lend you one. Hahaha!$"

PalletTown_ProfessorOaksLab_Text_OakThreeMonsChooseOne::
    .string "AVELAR: {RIVAL}?\n"
    .string "Good. You are both here.\p"
    .string "Roan, listen carefully.\p"
    .string "There are three BRAINROTS here.\p"
    .string "They are not toys.\n"
    .string "They are not normal animals.\p"
    .string "They are inside these\n"
    .string "BRAINROT BALLS.\p"
    .string "If you want a License, you need\n"
    .string "a partner.\p"
    .string "Choose one.\n"
    .string "Your first test starts now.$"

PalletTown_ProfessorOaksLab_Text_OakBePatientRival::
    .string "AVELAR: Be patient, {RIVAL}.\n"
    .string "You will receive one too.$"

PalletTown_ProfessorOaksLab_Text_OakWhichOneWillYouChoose::
    .string "AVELAR: Now, Roan.\p"
    .string "Inside those three BRAINROT BALLS\n"
    .string "are prototype partners.\p"
    .string "Which one will you choose?$"

PalletTown_ProfessorOaksLab_Text_OakHeyDontGoAwayYet::
    .string "AVELAR: Hey!\n"
    .string "Do not walk away from the test.$"

PalletTown_ProfessorOaksLab_Text_OakChoosingCharmander::
    .string "Ah! CAPPUCCINO ASSASSINO.\p"
    .string "Fast, sharp, and hard to control.\p"
    .string "So, Roan, you choose the\n"
    .string "FIRE SHADOW BRAINROT?$"

PalletTown_ProfessorOaksLab_Text_OakChoosingSquirtle::
    .string "Hm! TRALALERO TRALALA.\p"
    .string "Balanced, loud, and stubborn.\p"
    .string "So, Roan, you choose the\n"
    .string "WATER MEME BRAINROT?$"

PalletTown_ProfessorOaksLab_Text_OakChoosingBulbasaur::
    .string "I see! CHIMPANZINI BANANINI.\p"
    .string "Strong body, simple mind,\n"
    .string "dangerous rhythm.\p"
    .string "So, Roan, you choose the\n"
    .string "PLANT BRUTE BRAINROT?$"

PalletTown_ProfessorOaksLab_Text_OakThisMonIsEnergetic::
    .string "This BRAINROT is reacting\n"
    .string "strongly to you.$"

PalletTown_ProfessorOaksLab_Text_ReceivedMonFromOak::
    .string "{PLAYER} received {STR_VAR_1}\n"
    .string "from DR. AVELAR!$"

PalletTown_ProfessorOaksLab_Text_OakCanReachNextTownWithMon::
    .string "AVELAR: If a wild BRAINROT\n"
    .string "appears, your partner can battle.\p"
    .string "With it at your side, you should\n"
    .string "reach the next safe zone.$"

PalletTown_ProfessorOaksLab_Text_OakBattleMonForItToGrow::
    .string "AVELAR: Roan, a BRAINROT grows\n"
    .string "through battle and exposure.\p"
    .string "Do not just fear it.\n"
    .string "Learn how it thinks.$"

PalletTown_ProfessorOaksLab_Text_OakHaveSomethingForMe::
    .string "AVELAR: Oh, Roan!\n"
    .string "How is the prototype BRAINROT?\p"
    .string "It seems more stable than before.\p"
    .string "You may have more talent than\n"
    .string "you think.\p"
    .string "What is that?\n"
    .string "You have something for me?$"

PalletTown_ProfessorOaksLab_Text_DeliveredOaksParcel::
    .string "{PLAYER} delivered the sealed\n"
    .string "COGNIA PARCEL.$"

PalletTown_ProfessorOaksLab_Text_OakCustomBallIOrdered::
    .string "Ah!\n"
    .string "The custom BRAINROT BALL!\p"
    .string "Cognia finally sent it.\n"
    .string "Thank you.$"

PalletTown_ProfessorOaksLab_Text_OakHaveRequestForYouTwo::
    .string "AVELAR: Right.\n"
    .string "I have a request for you two.$"

PalletTown_ProfessorOaksLab_Text_OakPokedexOnDesk::
    .string "On the desk is my invention,\n"
    .string "the BRAINDEX!\p"
    .string "It records data on BRAINROTS\n"
    .string "you have seen or caught.\p"
    .string "It is our best tool against\n"
    .string "the unknown.$"

PalletTown_ProfessorOaksLab_Text_OakTakeTheseWithYou::
    .string "AVELAR: Roan and {RIVAL}.\n"
    .string "Take these with you.$"

PalletTown_ProfessorOaksLab_Text_ReceivedPokedexFromOak::
    .string "{PLAYER} received the BRAINDEX\n"
    .string "from DR. AVELAR.$"

PalletTown_ProfessorOaksLab_Text_OakCatchMonsForDataTakeThese::
    .string "AVELAR: Seeing a BRAINROT is\n"
    .string "not enough.\p"
    .string "You must catch them to gather\n"
    .string "complete field data.\p"
    .string "Here are tools for your\n"
    .string "first captures.$"

PalletTown_ProfessorOaksLab_Text_ReceivedFivePokeBalls::
    .string "{PLAYER} received five\n"
    .string "BRAINROT BALLS.$"

PalletTown_ProfessorOaksLab_Text_OakExplainCatching::
    .string "When a wild BRAINROT appears,\n"
    .string "weaken it first.\p"
    .string "Then throw a BRAINROT BALL.\p"
    .string "This will not always work.\n"
    .string "Some resist capture violently.$"

PalletTown_ProfessorOaksLab_Text_OakCompleteMonGuideWasMyDream::
    .string "A complete guide to every\n"
    .string "BRAINROT in Kanto...\p"
    .string "That was supposed to be\n"
    .string "Cognia's duty.\p"
    .string "But they hide too much.\p"
    .string "So I want you two to collect\n"
    .string "the truth in the field.\p"
    .string "This is not just research.\n"
    .string "This is Kanto's missing history.$"

PalletTown_ProfessorOaksLab_Text_OakMonsAroundWorldWait::
    .string "BRAINROTS across Kanto are\n"
    .string "waiting, Roan.$"

PalletTown_ProfessorOaksLab_Text_OakAddedNothingToPokedex::
    .string "Ah, Roan!\n"
    .string "How is your BRAINDEX?\p"
    .string "{RIVAL} has already added\n"
    .string "new field data.\p"
    .string "...Nothing?\p"
    .string "You cannot solve Luna's case\n"
    .string "by standing still.\p"
    .string "Take these and try harder.$"

PalletTown_ProfessorOaksLab_Text_OakComeSeeMeSometime::
    .string "AVELAR: Come see me sometimes.\p"
    .string "I need to know how your\n"
    .string "BRAINDEX is developing.$"

PalletTown_ProfessorOaksLab_Text_BlankEncyclopedia::
    .string "It is like an encyclopedia, but\n"
    .string "most pages are blank.$"

PalletTown_ProfessorOaksLab_Text_ThoseArePokeBalls::
    .string "Those are BRAINROT BALLS.\n"
    .string "They contain unstable partners.$"

PalletTown_ProfessorOaksLab_Text_OaksLastMon::
    .string "That is DR. AVELAR's last\n"
    .string "prototype BRAINROT.$"

PalletTown_ProfessorOaksLab_Text_PressStartToOpenMenu::
    .string "Press START to open the MENU!$"

PalletTown_ProfessorOaksLab_Text_SaveOptionInMenu::
    .string "The SAVE option is on the MENU.\n"
    .string "Use it regularly.$"

PalletTown_ProfessorOaksLab_Text_AllMonTypesHaveStrongAndWeakPoints::
    .string "All BRAINROT types have strong\n"
    .string "and weak points against others.$"

PalletTown_ProfessorOaksLab_Text_EmailMessage::
    .string "There is an e-mail message here.\p"
    .string "...\p"
    .string "Field License exams are ready.\p"
    .string "Candidates must bring stable\n"
    .string "BRAINROT partners.\p"
    .string "Training Center 01, report to\n"
    .string "the Cognia review board.\p"
    .string "Dr. Avelar, please respond.\n"
    .string "...$"

PalletTown_ProfessorOaksLab_Text_StudyAsOaksAide::
    .string "I study BRAINROTS as one of\n"
    .string "Dr. Avelar's aides.$"

PalletTown_ProfessorOaksLab_Text_DaisyWillGroomMons::
    .string "Hi, Roan. Your BRAINROT seems\n"
    .string "less unstable than before.\p"
    .string "Some people can read how much\n"
    .string "a BRAINROT trusts its trainer.\p"
    .string "Trust matters more than most\n"
    .string "candidates think.$"

PalletTown_ProfessorOaksLab_Text_OakIsGoingToHaveRadioShow::
    .string "Dr. Avelar was invited to speak\n"
    .string "on a Cognia radio program.\p"
    .string "He refused.\p"
    .string "He says Cognia edits the truth.$"

PalletTown_ProfessorOaksLab_Text_OakIsAuthorityOnMons::
    .string "Dr. Avelar may look tired, but\n"
    .string "he knows more about BRAINROTS\p"
    .string "than most official researchers.$"

PalletTown_ProfessorOaksLab_Text_OakFavorToAskYouPlayer::
    .string "Ah, this is excellent.\p"
    .string "Roan, I have another important\n"
    .string "favor to ask.\p"
    .string "Listen closely.$"

PalletTown_ProfessorOaksLab_Text_OakSightingsOfRareMons::
    .string "Recently, rare BRAINROTS have\n"
    .string "appeared outside known zones.\p"
    .string "Some were never recorded in\n"
    .string "Kanto before.\p"
    .string "I cannot investigate alone.\p"
    .string "Roan, I want you to go in\n"
    .string "my place.$"

PalletTown_ProfessorOaksLab_Text_RivalJustLetMeHandleEverything::
    .string "{RIVAL}: Hey, I heard that!\p"
    .string "Avelar, why do you keep trusting\n"
    .string "Roan with the weird stuff?\p"
    .string "I caught more BRAINROTS and\n"
    .string "I did it faster too.\p"
    .string "You should let me handle it.$"

PalletTown_ProfessorOaksLab_Text_OakNeedYourHelpTooNeedToSeePokedexes::
    .string "AVELAR: I know.\n"
    .string "I need your help too.\p"
    .string "Now I need to see both\n"
    .string "BRAINDEX units.$"

PalletTown_ProfessorOaksLab_Text_OakTookBothPokedexUnits::
    .string "DR. AVELAR took both\n"
    .string "BRAINDEX units.$"

PalletTown_ProfessorOaksLab_Text_OakNowTheseUnitsCanRecordMoreData::
    .string "... ... ...  ... ... ...\p"
    .string "... ... ...  ... ... ...\p"
    .string "Done.\p"
    .string "Now these units can record data\n"
    .string "on stronger BRAINROTS.$"

PalletTown_ProfessorOaksLab_Text_PlayersPokedexWasUpgraded::
    .string "{PLAYER}'s BRAINDEX was upgraded!$"

PalletTown_ProfessorOaksLab_Text_OakMustReallyWorkToFillPokedex::
    .string "Now, Roan and {RIVAL}!\p"
    .string "This time, gather real field data.\p"
    .string "Do not just collect names.\n"
    .string "Find patterns, sounds, memories.\p"
    .string "This may become the most important\n"
    .string "Brainrot record in Kanto.$"

PalletTown_ProfessorOaksLab_Text_RivalIllCompleteThePokedex::
    .string "{RIVAL}: Avelar, calm down.\p"
    .string "I will complete the BRAINDEX,\n"
    .string "do not worry.\p"
    .string "I might check the islands first.\p"
    .string "Anyways, I am out!$"
```
