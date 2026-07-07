# Viridian Safe Zone text patch

This patch turns Viridian City into the first safe zone after Test Zone 01.

Target file:

`data/maps/ViridianCity/text.inc`

Replace the whole file with this:

```c
ViridianCity_Text_CanCarryMonsAnywhere::
    .string "Those BRAINROT BALLS at your\n"
    .string "waist...\p"
    .string "You passed the first partner test,\n"
    .string "didn't you?\p"
    .string "It is strange, right?\n"
    .string "Carrying a Brainrot like gear.$"

ViridianCity_Text_GymClosedWonderWhoLeaderIs::
    .string "This License Center is always\n"
    .string "closed.\p"
    .string "People say the final examiner\n"
    .string "works for Cognia.$"

ViridianCity_Text_ViridiansGymLeaderReturned::
    .string "The VIRIDIAN License Examiner\n"
    .string "has returned!$"

ViridianCity_Text_WantToKnowAboutCaterpillarMons::
    .string "You want to know about the two\n"
    .string "Brainrots in Zone Green 01?$"

ViridianCity_Text_OhOkayThen::
    .string "Oh, okay then!$"

ViridianCity_Text_ExplainCaterpieWeedle::
    .string "Some look harmless, but they\n"
    .string "mess with your attention.\p"
    .string "Others use poison or sound.\p"
    .string "Do not judge a Brainrot by\n"
    .string "how dumb it looks.$"

ViridianCity_Text_GrandpaHasntHadCoffeeYet::
    .string "Oh, Grandpa!\n"
    .string "Don't block the road again!\p"
    .string "I'm sorry.\n"
    .string "He has not had his coffee yet.$"

ViridianCity_Text_GoShoppingInPewterOccasionally::
    .string "I go to Pewter sometimes.\p"
    .string "The trail through Zone Green 01\n"
    .string "used to be a normal forest.\p"
    .string "Now it keeps making weird sounds\n"
    .string "at night.$"

ViridianCity_Text_ThisIsPrivateProperty::
    .string "I forbid you from going through!\p"
    .string "This is a restricted route!\p"
    .string "...Or private property.\n"
    .string "I forgot which.$"

ViridianCity_Text_ShowYouHowToCatchMons::
    .string "Well now, I had my coffee, and\n"
    .string "that clears the fog!\p"
    .string "Hm?\n"
    .string "What is that red device?\p"
    .string "Ah, a BRAINDEX.\p"
    .string "So Avelar finally sent another\n"
    .string "kid into the zones.\p"
    .string "You do not know how to catch\n"
    .string "a Brainrot?\p"
    .string "Then watch closely.\n"
    .string "And do not blink too much.$"

ViridianCity_Text_ThatWasEducationalTakeThis::
    .string "There!\n"
    .string "Educational, was it not?\p"
    .string "Here, take this too.\p"
    .string "It is old, but it still teaches\n"
    .string "the basics.$"

ViridianCity_Text_WatchThatToLearnBasics::
    .string "If you do not understand\n"
    .string "Brainrot battles, watch that.\p"
    .string "It teaches the basics of being\n"
    .string "a licensed Brainrot trainer.$"

ViridianCity_Text_WeakenMonsFirstToCatch::
    .string "Well now, I had my coffee, and\n"
    .string "that clears the fog!\p"
    .string "But I made it too strong.\n"
    .string "Now I hear numbers.\p"
    .string "If you are filling the BRAINDEX,\n"
    .string "remember this:\p"
    .string "weaken a Brainrot before trying\n"
    .string "to catch it.$"

ViridianCity_Text_HowsTeachyTVHelping::
    .string "Well now, I had my coffee, and\n"
    .string "that clears the fog!\p"
    .string "But I made it too strong.\n"
    .string "Now I hear numbers.\p"
    .string "Is my old TEACHY TV helping you?$"

ViridianCity_Text_MyGrandsonOnTheShow::
    .string "Wahaha!\n"
    .string "That is my grandson on the show!\p"
    .string "He explains Brainrots without\n"
    .string "screaming, which is rare.$"

ViridianCity_Text_TooBusyForTeachyTV::
    .string "Hm... Too busy for TEACHY TV?\p"
    .string "Then learn fast in the grass.\p"
    .string "Brainrots do not wait for you\n"
    .string "to understand the rules.$"

ViridianCity_Text_CitySign::
    .string "VIRIDIAN SAFE ZONE\n"
    .string "Where the forest whispers too close$"

ViridianCity_Text_CatchMonsForEasierBattles::
    .string "TRAINER TIPS\p"
    .string "Catch Brainrots and expand your\n"
    .string "field options.\p"
    .string "But remember: more Brainrots means\n"
    .string "more noise in your head.$"

ViridianCity_Text_MovesLimitedByPP::
    .string "TRAINER TIPS\p"
    .string "Brainrot moves are limited by PP.\p"
    .string "If your partner is tired, rest at\n"
    .string "a recovery center.$"

ViridianCity_Text_GymSign::
    .string "VIRIDIAN LICENSE CENTER\n"
    .string "FINAL EXAM LOCKED$"

ViridianCity_Text_GymDoorsAreLocked::
    .string "The License Center doors are\n"
    .string "locked...\p"
    .string "A small Cognia symbol is carved\n"
    .string "near the handle.$"
```

## Story purpose

Viridian becomes the first safe zone where the player sees how normal people talk about Brainrots now.

The old man tutorial becomes creepier but still useful.

The closed Gym becomes a locked License Center tied to Cognia.
