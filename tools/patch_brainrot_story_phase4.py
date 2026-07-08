#!/usr/bin/env python3
"""Phase 4 story pass for Brainrot: Echoes of Sahur.

This pass moves the next chunk of the game away from vanilla FireRed:
- Cerulean becomes LICENSE C CITY.
- Misty becomes the License C Examiner.
- The Rocket house theft becomes an Echo Masks/Cognia clue.
- Kiunin's rival scene hints at his pressure, status obsession, and memory lock.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def p(path: str) -> Path:
    return ROOT / path


def read(path: str) -> str:
    return p(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    p(path).write_text(text, encoding="utf-8")


def replace_label_block(text: str, label: str, new_block: str) -> str:
    start_token = f"{label}::"
    start = text.find(start_token)
    if start == -1:
        raise RuntimeError(f"label not found: {label}")
    end = text.find("\n\n", start)
    if end == -1:
        end = len(text)
    return text[:start] + new_block.rstrip() + text[end:]


def patch_cerulean_city() -> None:
    path = "data/maps/CeruleanCity/text.inc"
    text = read(path)
    replacements = {
        "CeruleanCity_Text_RivalIntro": '''CeruleanCity_Text_RivalIntro::
    .string "{RIVAL}: Yo, {PLAYER}!\p"
    .string "Still alive after MOON NOISE\n"
    .string "CAVE? Cute.\p"
    .string "I already cleared half the\n"
    .string "C test route.\p"
    .string "My BRAINROTS are getting\n"
    .string "stronger, louder, better.\p"
    .string "Let me check if you are\n"
    .string "still worth chasing!$"''',
        "CeruleanCity_Text_RivalDefeat": '''CeruleanCity_Text_RivalDefeat::
    .string "No way!\n"
    .string "That was noise luck!$"''',
        "CeruleanCity_Text_RivalPostBattle": '''CeruleanCity_Text_RivalPostBattle::
    .string "{RIVAL}: Tch... whatever.\p"
    .string "A COGNIA storage researcher\n"
    .string "north of here found rare data.\p"
    .string "He says some BRAINROTS\n"
    .string "remember places people forgot.\p"
    .string "Sounds fake, but my dad\n"
    .string "wanted that report.\p"
    .string "You should go too, if your\n"
    .string "brain can handle it.\p"
    .string "I am still ahead of you.\n"
    .string "Do not forget that.$"''',
        "CeruleanCity_Text_OhRightLittlePresentAsFavor": '''CeruleanCity_Text_OhRightLittlePresentAsFavor::
    .string "Oh, right.\p"
    .string "Avelar told me to give you\n"
    .string "this field checker.\p"
    .string "I do not need it.\n"
    .string "Everyone already watches me.$"''',
        "CeruleanCity_Text_ExplainFameCheckerSmellYa": '''CeruleanCity_Text_ExplainFameCheckerSmellYa::
    .string "It stores notes about people\n"
    .string "connected to the licenses.\p"
    .string "Names, rumors, weird behavior.\p"
    .string "Maybe it will even explain\n"
    .string "why you keep saying LUNA.\p"
    .string "...Forget I said that.\n"
    .string "Later, {PLAYER}!$"''',
        "CeruleanCity_Text_RivalVictory": '''CeruleanCity_Text_RivalVictory::
    .string "{RIVAL}: See?\n"
    .string "Class S future. Remember it.$"''',
        "CeruleanCity_Text_GruntIntro": '''CeruleanCity_Text_GruntIntro::
    .string "Hey! Stay out!\p"
    .string "This house had old COGNIA\n"
    .string "files hidden in the wall.\p"
    .string "DANTE says memory belongs\n"
    .string "to whoever can control it.\p"
    .string "...Huh?\n"
    .string "You heard nothing!{PLAY_BGM}{MUS_ENCOUNTER_ROCKET}$"''',
        "CeruleanCity_Text_GruntDefeat": '''CeruleanCity_Text_GruntDefeat::
    .string "GRUNT: Stop!\n"
    .string "The Echo Masks retreat!$"''',
        "CeruleanCity_Text_OkayIllReturnStolenTM": '''CeruleanCity_Text_OkayIllReturnStolenTM::
    .string "Fine...\n"
    .string "Take the TM back.\p"
    .string "But the copied files are\n"
    .string "already moving north.$"''',
        "CeruleanCity_Text_RecoveredTM28FromGrunt": '''CeruleanCity_Text_RecoveredTM28FromGrunt::
    .string "{PLAYER} recovered TM28\n"
    .string "from the ECHO MASK GRUNT.$"''',
        "CeruleanCity_Text_BetterGetMovingBye": '''CeruleanCity_Text_BetterGetMovingBye::
    .string "DANTE will not like this...\n"
    .string "I am gone!$"''',
        "CeruleanCity_Text_TrainerLifeIsToughIsntIt": '''CeruleanCity_Text_TrainerLifeIsToughIsntIt::
    .string "You are a candidate too?\p"
    .string "Training, catching, keeping\n"
    .string "your thoughts clear...\p"
    .string "It is a tough life, right?$"''',
        "CeruleanCity_Text_YouCanCutDownSmallTrees": '''CeruleanCity_Text_YouCanCutDownSmallTrees::
    .string "Some paths are blocked by\n"
    .string "small trees.\p"
    .string "A licensed CUT technique can\n"
    .string "open them.\p"
    .string "That is why License C matters.$"''',
        "CeruleanCity_Text_IfSlowbroWasntThereCouldCutTree": '''CeruleanCity_Text_IfSlowbroWasntThereCouldCutTree::
    .string "If that sleepy BRAINROT\n"
    .string "would move, you could reach\n"
    .string "the other side.\p"
    .string "Maybe CUT would solve it.$"''',
        "CeruleanCity_Text_PokemonEncyclopediaAmusing": '''CeruleanCity_Text_PokemonEncyclopediaAmusing::
    .string "You are making a BRAINDEX?\p"
    .string "Good. Someone should write\n"
    .string "the version COGNIA edits out.$"''',
        "CeruleanCity_Text_PeopleHereWereRobbed": '''CeruleanCity_Text_PeopleHereWereRobbed::
    .string "The people here were robbed.\p"
    .string "Not money. Old medical files.\p"
    .string "The police blame masked thieves,\n"
    .string "but COGNIA is nervous too.$"''',
        "CeruleanCity_Text_SlowbroUseSonicboom": '''CeruleanCity_Text_SlowbroUseSonicboom::
    .string "Okay! Partner!\n"
    .string "Use SONICBOOM!$"''',
        "CeruleanCity_Text_SlowbroPayAttention": '''CeruleanCity_Text_SlowbroPayAttention::
    .string "Come on, partner, focus!$"''',
        "CeruleanCity_Text_SlowbroPunch": '''CeruleanCity_Text_SlowbroPunch::
    .string "Partner, punch!$"''',
        "CeruleanCity_Text_NoYouBlewItAgain": '''CeruleanCity_Text_NoYouBlewItAgain::
    .string "No!\n"
    .string "The noise broke focus again!$"''',
        "CeruleanCity_Text_SlowbroWithdraw": '''CeruleanCity_Text_SlowbroWithdraw::
    .string "Partner, WITHDRAW!$"''',
        "CeruleanCity_Text_HardToControlMonsObedience": '''CeruleanCity_Text_HardToControlMonsObedience::
    .string "No! That is wrong!\p"
    .string "Strong BRAINROTS only obey\n"
    .string "trainers with proper license.\p"
    .string "Skill is not enough.\n"
    .string "Your mind has to stay steady.$"''',
        "CeruleanCity_Text_SlowbroTookSnooze": '''CeruleanCity_Text_SlowbroTookSnooze::
    .string "The BRAINROT took a snooze...$"''',
        "CeruleanCity_Text_SlowbroLoafingAround": '''CeruleanCity_Text_SlowbroLoafingAround::
    .string "The BRAINROT is loafing around...$"''',
        "CeruleanCity_Text_SlowbroTurnedAway": '''CeruleanCity_Text_SlowbroTurnedAway::
    .string "The BRAINROT turned away...$"''',
        "CeruleanCity_Text_SlowbroIgnoredOrders": '''CeruleanCity_Text_SlowbroIgnoredOrders::
    .string "The BRAINROT ignored orders...$"''',
        "CeruleanCity_Text_WantBrightRedBicycle": '''CeruleanCity_Text_WantBrightRedBicycle::
    .string "I want a bike for field work.\p"
    .string "Walking through noisy zones\n"
    .string "gets tiring fast.$"''',
        "CeruleanCity_Text_ThisIsCeruleanCave": '''CeruleanCity_Text_ThisIsCeruleanCave::
    .string "This is AREA NULL.\p"
    .string "Only candidates with extreme\n"
    .string "mental stability may enter.\p"
    .string "The BRAINROTS inside do not\n"
    .string "just battle.\p"
    .string "They look back into you.$"''',
        "CeruleanCity_Text_CitySign": '''CeruleanCity_Text_CitySign::
    .string "LICENSE C CITY\n"
    .string "Missing children case zone$"''',
        "CeruleanCity_Text_TrainerTipsHeldItems": '''CeruleanCity_Text_TrainerTipsHeldItems::
    .string "TRAINER TIPS\p"
    .string "A BRAINROT can hold an item.\p"
    .string "Some items activate during\n"
    .string "battle when stress rises.$"''',
        "CeruleanCity_Text_BikeShopSign": '''CeruleanCity_Text_BikeShopSign::
    .string "Fast travel for candidates!\n"
    .string "BIKE SHOP$"''',
        "CeruleanCity_Text_GymSign": '''CeruleanCity_Text_GymSign::
    .string "LICENSE C CITY EXAM HALL\n"
    .string "EXAMINER: MISTY\l"
    .string "Water pressure focus test$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_cerulean_gym() -> None:
    path = "data/maps/CeruleanCity_Gym/text.inc"
    text = read(path)
    replacements = {
        "CeruleanCity_Gym_Text_MistyIntro": '''CeruleanCity_Gym_Text_MistyIntro::
    .string "Hi, new candidate!\p"
    .string "I am MISTY, License C Examiner.\p"
    .string "C rank is where training stops\n"
    .string "being cute.\p"
    .string "Water pressure, panic, rhythm...\n"
    .string "all of it tests focus.\p"
    .string "My policy is full pressure\n"
    .string "with WATER BRAINROTS!{PLAY_BGM}{MUS_ENCOUNTER_GYM_LEADER}$"''',
        "CeruleanCity_Gym_Text_ExplainTM03": '''CeruleanCity_Gym_Text_ExplainTM03::
    .string "TM03 teaches WATER PULSE.\p"
    .string "It hits with water and sound\n"
    .string "pressure.\p"
    .string "Use it on an aquatic\n"
    .string "BRAINROT!$"''',
        "CeruleanCity_Gym_Text_ExplainCascadeBadge": '''CeruleanCity_Gym_Text_ExplainCascadeBadge::
    .string "The CASCADEBADGE marks you\n"
    .string "as License C level.\p"
    .string "BRAINROTS up to Lv. 30\n"
    .string "will obey stable commands.\p"
    .string "You can now use CUT outside\n"
    .string "battle to open blocked paths.\p"
    .string "You also earned my favorite TM.$"''',
        "CeruleanCity_Gym_Text_ReceivedTM03FromMisty": '''CeruleanCity_Gym_Text_ReceivedTM03FromMisty::
    .string "{PLAYER} received TM03\n"
    .string "from MISTY.$"''',
        "CeruleanCity_Gym_Text_MistyDefeat": '''CeruleanCity_Gym_Text_MistyDefeat::
    .string "Wow!\n"
    .string "You stayed calm under pressure!\p"
    .string "All right.\p"
    .string "You passed the License C test.\n"
    .string "Take the CASCADEBADGE.$"''',
        "CeruleanCity_Gym_Text_DianaIntro": '''CeruleanCity_Gym_Text_DianaIntro::
    .string "What? You?\p"
    .string "MISTY does not need to test\n"
    .string "every shaky candidate herself!$"''',
        "CeruleanCity_Gym_Text_DianaDefeat": '''CeruleanCity_Gym_Text_DianaDefeat::
    .string "You did not break focus!$"''',
        "CeruleanCity_Gym_Text_DianaPostBattle": '''CeruleanCity_Gym_Text_DianaPostBattle::
    .string "License C is all about pressure.\p"
    .string "If you panic, your BRAINROT\n"
    .string "panics harder.$"''',
        "CeruleanCity_Gym_Text_LuisIntro": '''CeruleanCity_Gym_Text_LuisIntro::
    .string "Splash!\p"
    .string "First pressure test!\n"
    .string "Let's do it!$"''',
        "CeruleanCity_Gym_Text_LuisDefeat": '''CeruleanCity_Gym_Text_LuisDefeat::
    .string "That cannot be!$"''',
        "CeruleanCity_Gym_Text_LuisPostBattle": '''CeruleanCity_Gym_Text_LuisPostBattle::
    .string "MISTY is calm even when\n"
    .string "the room feels like a storm.\p"
    .string "That is why she is Examiner.$"''',
        "CeruleanCity_Gym_Text_GymGuyAdvice": '''CeruleanCity_Gym_Text_GymGuyAdvice::
    .string "Yo!\n"
    .string "Future Class S candidate!\p"
    .string "MISTY uses WATER BRAINROTS.\p"
    .string "GRASS partners can drain\n"
    .string "their pressure.\p"
    .string "ELECTRIC partners can shock\n"
    .string "the rhythm apart.$"''',
        "CeruleanCity_Gym_Text_WeMakePrettyGoodTeam": '''CeruleanCity_Gym_Text_WeMakePrettyGoodTeam::
    .string "You passed MISTY'S test!\p"
    .string "See? Calm brain, clean win.$"''',
        "CeruleanCity_Gym_Text_GymStatue": '''CeruleanCity_Gym_Text_GymStatue::
    .string "LICENSE C EXAM HALL\n"
    .string "EXAMINER: MISTY\p"
    .string "PASSED CANDIDATES:\n"
    .string "{RIVAL}$"''',
        "CeruleanCity_Gym_Text_GymStatuePlayerWon": '''CeruleanCity_Gym_Text_GymStatuePlayerWon::
    .string "LICENSE C EXAM HALL\n"
    .string "EXAMINER: MISTY\p"
    .string "PASSED CANDIDATES:\n"
    .string "{RIVAL}, {PLAYER}$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def main() -> None:
    patch_cerulean_city()
    patch_cerulean_gym()
    print("Brainrot phase 4 Cerulean License C story patch applied.")


if __name__ == "__main__":
    main()
