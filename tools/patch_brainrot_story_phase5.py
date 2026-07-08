#!/usr/bin/env python3
"""Phase 5 story pass for Brainrot: Echoes of Sahur.

This pass converts the Vermilion/S.S. Anne arc into:
- SOUND PORT, a coastal signal hub.
- The S.S. Anne as a Cognia signal vessel with strange audio cargo.
- Kiunin's ship battle as a stronger rivalry/status scene.
- Lt. Surge as the License B Examiner using electricity and sound locks.
- Early foreshadowing for the Skibidy Zone.
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


def patch_vermilion_city() -> None:
    path = "data/maps/VermilionCity/text.inc"
    text = read(path)
    replacements = {
        "VermilionCity_Text_GrimerMultipliesInSludge": '''VermilionCity_Text_GrimerMultipliesInSludge::
    .string "We monitor signal pollution here.\p"
    .string "When audio trash builds up,\n"
    .string "wild BRAINROTS gather fast.$"''',
        "VermilionCity_Text_DidYouSeeSSAnneInHarbor": '''VermilionCity_Text_DidYouSeeSSAnneInHarbor::
    .string "Did you see the S.S. ANNE\n"
    .string "moored in the harbor?\p"
    .string "COGNIA says it carries clean\n"
    .string "research data.\p"
    .string "But I heard flushing sounds\n"
    .string "coming from the cargo deck.$"''',
        "VermilionCity_Text_SSAnneHasDepartedForYear": '''VermilionCity_Text_SSAnneHasDepartedForYear::
    .string "So, the S.S. ANNE departed?\p"
    .string "Then the port should get\n"
    .string "quieter.\p"
    .string "Unless something stayed behind.$"''',
        "VermilionCity_Text_BuildingOnThisLand": '''VermilionCity_Text_BuildingOnThisLand::
    .string "I am building a signal tower\n"
    .string "on this plot.\p"
    .string "My partner is flattening the\n"
    .string "ground for the foundation.$"''',
        "VermilionCity_Text_Machop": '''VermilionCity_Text_Machop::
    .string "BRAINROT: Guh! Guhguhguh!$"''',
        "VermilionCity_Text_MachopStompingLandFlat": '''VermilionCity_Text_MachopStompingLandFlat::
    .string "A BRAINROT is stomping the\n"
    .string "land flat.$"''',
        "VermilionCity_Text_SSAnneVisitsOnceAYear": '''VermilionCity_Text_SSAnneVisitsOnceAYear::
    .string "The S.S. ANNE is a famous\n"
    .string "COGNIA signal vessel.\p"
    .string "Once a year, it gathers\n"
    .string "trainers, candidates, and data.$"''',
        "VermilionCity_Text_CitySign": '''VermilionCity_Text_CitySign::
    .string "SOUND PORT\n"
    .string "Where Kanto's signals meet the sea$"''',
        "VermilionCity_Text_SnorlaxBlockingRoute12": '''VermilionCity_Text_SnorlaxBlockingRoute12::
    .string "NOTICE!\p"
    .string "ROUTE 12 may be blocked by\n"
    .string "a sleeping BRAINROT.\p"
    .string "If the road hums, do not\n"
    .string "try to wake it by force.\p"
    .string "Detour through ECHO TUNNEL\n"
    .string "toward MEMORY TOWN.\p"
    .string "SOUND PORT POLICE$"''',
        "VermilionCity_Text_PokemonFanClubSign": '''VermilionCity_Text_PokemonFanClubSign::
    .string "BRAINROT FAN CLUB\n"
    .string "Fans, collectors, and weirdos welcome!$"''',
        "VermilionCity_Text_GymSign": '''VermilionCity_Text_GymSign::
    .string "SOUND PORT EXAM HALL\n"
    .string "EXAMINER: LT. SURGE\l"
    .string "License B electric focus test$"''',
        "VermilionCity_Text_VermilionHarbor": '''VermilionCity_Text_VermilionHarbor::
    .string "SOUND PORT HARBOR$"''',
        "VermilionCity_Text_WelcomeToTheSSAnne": '''VermilionCity_Text_WelcomeToTheSSAnne::
    .string "Welcome to the S.S. ANNE\n"
    .string "COGNIA signal vessel!$"''',
        "VermilionCity_Text_DoYouHaveATicket": '''VermilionCity_Text_DoYouHaveATicket::
    .string "Welcome to the S.S. ANNE!\p"
    .string "Excuse me, do you have a\n"
    .string "signal boarding ticket?$"''',
        "VermilionCity_Text_FlashedSSTicket": '''VermilionCity_Text_FlashedSSTicket::
    .string "{FONT_NORMAL}{PLAYER} flashed the S.S. TICKET!\p"
    .string "{FONT_MALE}Great!\n"
    .string "Welcome aboard the S.S. ANNE!$"''',
        "VermilionCity_Text_DontHaveNeededSSTicket": '''VermilionCity_Text_DontHaveNeededSSTicket::
    .string "{FONT_NORMAL}{PLAYER} does not have the needed\n"
    .string "S.S. TICKET.\p"
    .string "{FONT_MALE}Sorry!\p"
    .string "Only cleared candidates may\n"
    .string "board this vessel.$"''',
        "VermilionCity_Text_TheShipSetSail": '''VermilionCity_Text_TheShipSetSail::
    .string "The S.S. ANNE set sail.\p"
    .string "For a second, the harbor\n"
    .string "sounds like a flushing echo.$"''',
        "VermilionCity_Text_Route2AideHasPackageForYou": '''VermilionCity_Text_Route2AideHasPackageForYou::
    .string "Oh, hello, {PLAYER}!\n"
    .string "It is me, one of DR. AVELAR's\n"
    .string "aides.\p"
    .string "Another aide had a package\n"
    .string "for you near ROUTE 2.\p"
    .string "Avelar says your BRAINDEX\n"
    .string "reacts strangely to old routes.\p"
    .string "Please check on it when\n"
    .string "you can.$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_vermilion_gym() -> None:
    path = "data/maps/VermilionCity_Gym/text.inc"
    text = read(path)
    replacements = {
        "VermilionCity_Gym_Text_LtSurgeIntro": '''VermilionCity_Gym_Text_LtSurgeIntro::
    .string "Hey, kid!\n"
    .string "You know where you are?\p"
    .string "This is the License B exam.\n"
    .string "Weak focus gets fried here.\p"
    .string "Electric BRAINROTS saved me\n"
    .string "when the old signals broke.\p"
    .string "They shock noise into silence.\p"
    .string "Same thing I will do to you!{PLAY_BGM}{MUS_ENCOUNTER_GYM_LEADER}$"''',
        "VermilionCity_Gym_Text_LtSurgePostBattle": '''VermilionCity_Gym_Text_LtSurgePostBattle::
    .string "A word of advice, kid!\p"
    .string "Electric power is brutal.\p"
    .string "But Ground-type BRAINROTS\n"
    .string "can shut the circuit down.$"''',
        "VermilionCity_Gym_Text_ExplainThunderBadgeTakeThis": '''VermilionCity_Gym_Text_ExplainThunderBadgeTakeThis::
    .string "The THUNDERBADGE marks you\n"
    .string "as License B level!\p"
    .string "Your team will move faster\n"
    .string "under pressure.\p"
    .string "It also lets you use FLY\n"
    .string "outside battle, kid!\p"
    .string "You are weirdly steady.\n"
    .string "Take this!$"''',
        "VermilionCity_Gym_Text_ReceivedTM34FromLtSurge": '''VermilionCity_Gym_Text_ReceivedTM34FromLtSurge::
    .string "{PLAYER} received TM34\n"
    .string "from LT. SURGE.$"''',
        "VermilionCity_Gym_Text_ExplainTM34": '''VermilionCity_Gym_Text_ExplainTM34::
    .string "TM34 contains SHOCK WAVE!\p"
    .string "It never misses because the\n"
    .string "signal locks onto noise.\p"
    .string "Teach it to an ELECTRIC\n"
    .string "BRAINROT!$"''',
        "VermilionCity_Gym_Text_LtSurgeDefeat": '''VermilionCity_Gym_Text_LtSurgeDefeat::
    .string "Now that is a shocker!\p"
    .string "You passed the License B test,\n"
    .string "kid!\p"
    .string "Fine, take the THUNDERBADGE!$"''',
        "VermilionCity_Gym_Text_TuckerIntro": '''VermilionCity_Gym_Text_TuckerIntro::
    .string "SURGE trained me to handle\n"
    .string "panic signals.\p"
    .string "He is a hard examiner.$"''',
        "VermilionCity_Gym_Text_TuckerDefeat": '''VermilionCity_Gym_Text_TuckerDefeat::
    .string "Stop!\n"
    .string "Your focus is good!$"''',
        "VermilionCity_Gym_Text_TuckerPostBattle": '''VermilionCity_Gym_Text_TuckerPostBattle::
    .string "Those locks are not just\n"
    .string "electric.\p"
    .string "They reset when the room\n"
    .string "hears messy movement.$"''',
        "VermilionCity_Gym_Text_BailyIntro": '''VermilionCity_Gym_Text_BailyIntro::
    .string "I am lightweight, but I\n"
    .string "control electricity well!\p"
    .string "That is why I passed B prep.$"''',
        "VermilionCity_Gym_Text_BailyDefeat": '''VermilionCity_Gym_Text_BailyDefeat::
    .string "Fried!$"''',
        "VermilionCity_Gym_Text_BailyPostBattle": '''VermilionCity_Gym_Text_BailyPostBattle::
    .string "SURGE hid switches inside\n"
    .string "the trash bins.\p"
    .string "Gross? Yes. Effective? Also yes.$"''',
        "VermilionCity_Gym_Text_DwayneIntro": '''VermilionCity_Gym_Text_DwayneIntro::
    .string "This is no place for soft\n"
    .string "candidates!\p"
    .string "Even good ones get zapped!$"''',
        "VermilionCity_Gym_Text_DwayneDefeat": '''VermilionCity_Gym_Text_DwayneDefeat::
    .string "Wow!\n"
    .string "You surprised me!$"''',
        "VermilionCity_Gym_Text_DwaynePostBattle": '''VermilionCity_Gym_Text_DwaynePostBattle::
    .string "When you open the first lock,\n"
    .string "the second is nearby.\p"
    .string "Think clean. Move clean.\n"
    .string "Do not let the room bait you.$"''',
        "VermilionCity_Gym_Text_GymGuyAdvice": '''VermilionCity_Gym_Text_GymGuyAdvice::
    .string "Yo!\n"
    .string "Class S candidate in the making!\p"
    .string "SURGE uses ELECTRIC BRAINROTS.\p"
    .string "WATER and FLYING partners\n"
    .string "hate this room.\p"
    .string "GROUND partners can cut\n"
    .string "the current.\p"
    .string "Also, the locks punish panic.$"''',
        "VermilionCity_Gym_Text_GymGuyPostVictory": '''VermilionCity_Gym_Text_GymGuyPostVictory::
    .string "Whew!\n"
    .string "That match had voltage!$"''',
        "VermilionCity_Gym_Text_GymStatue": '''VermilionCity_Gym_Text_GymStatue::
    .string "LICENSE B EXAM HALL\n"
    .string "EXAMINER: LT. SURGE\p"
    .string "PASSED CANDIDATES:\n"
    .string "{RIVAL}$"''',
        "VermilionCity_Gym_Text_GymStatuePlayerWon": '''VermilionCity_Gym_Text_GymStatuePlayerWon::
    .string "LICENSE B EXAM HALL\n"
    .string "EXAMINER: LT. SURGE\p"
    .string "PASSED CANDIDATES:\n"
    .string "{RIVAL}, {PLAYER}$"''',
        "VermilionCity_Gym_Text_NopeOnlyTrashHere": '''VermilionCity_Gym_Text_NopeOnlyTrashHere::
    .string "Nope!\n"
    .string "Only signal trash here.$"''',
        "VermilionCity_Gym_Text_SwitchUnderTrashFirstLockOpened": '''VermilionCity_Gym_Text_SwitchUnderTrashFirstLockOpened::
    .string "Hey! A switch is under\n"
    .string "the signal trash!\p"
    .string "The first electric lock opened!$"''',
        "VermilionCity_Gym_Text_SecondLockOpened": '''VermilionCity_Gym_Text_SecondLockOpened::
    .string "The second electric lock opened!\n"
    .string "The motorized door opened!$"''',
        "VermilionCity_Gym_Text_OnlyTrashLocksWereReset": '''VermilionCity_Gym_Text_OnlyTrashLocksWereReset::
    .string "Nope!\n"
    .string "Only signal trash here.\p"
    .string "Hey!\n"
    .string "The electric locks reset!$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_ss_anne() -> None:
    corridor_path = "data/maps/SSAnne_2F_Corridor/text.inc"
    text = read(corridor_path)
    replacements = {
        "SSAnne_2F_Corridor_Text_ThisShipIsLuxuryLiner": '''SSAnne_2F_Corridor_Text_ThisShipIsLuxuryLiner::
    .string "This ship is a luxury liner\n"
    .string "and a COGNIA signal vessel!\p"
    .string "At every port, we host parties\n"
    .string "and collect field data.$"''',
        "SSAnne_2F_Corridor_Text_RivalIntro": '''SSAnne_2F_Corridor_Text_RivalIntro::
    .string "{RIVAL}: Bonjour, {PLAYER}!\p"
    .string "You got invited too?\n"
    .string "That is hilarious.\p"
    .string "I already logged a ton of\n"
    .string "BRAINROT data.\p"
    .string "The ship's cargo deck has\n"
    .string "a weird bathroom signal.\p"
    .string "Skibidy, flushing, static...\n"
    .string "whatever.\p"
    .string "My dad says I should ignore it,\n"
    .string "so I will beat you instead!$"''',
        "SSAnne_2F_Corridor_Text_RivalDefeat": '''SSAnne_2F_Corridor_Text_RivalDefeat::
    .string "Humph!\p"
    .string "You are raising your BRAINROTS\n"
    .string "better than I expected.$"''',
        "SSAnne_2F_Corridor_Text_RivalVictory": '''SSAnne_2F_Corridor_Text_RivalVictory::
    .string "{RIVAL}: Maybe the sea is\n"
    .string "making you dizzy!\p"
    .string "Train harder, {PLAYER}!$"''',
        "SSAnne_2F_Corridor_Text_RivalPostBattle": '''SSAnne_2F_Corridor_Text_RivalPostBattle::
    .string "{RIVAL}: I heard the captain\n"
    .string "has the CUT clearance.\p"
    .string "He also heard the cargo signal\n"
    .string "and got sick.\p"
    .string "Go see him if you want.\p"
    .string "I am heading for License B.\n"
    .string "Try not to drown in my shadow.$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(corridor_path, text)

    captain_path = "data/maps/SSAnne_CaptainsOffice/text.inc"
    text = read(captain_path)
    replacements = {
        "SSAnne_CaptainsOffice_Text_CaptainIFeelSeasick": '''SSAnne_CaptainsOffice_Text_CaptainIFeelSeasick::
    .string "CAPTAIN: Ooargh...\n"
    .string "I feel hideous...\p"
    .string "It is not the sea.\n"
    .string "It is that repeating flush...$"''',
        "SSAnne_CaptainsOffice_Text_RubbedCaptainsBack": '''SSAnne_CaptainsOffice_Text_RubbedCaptainsBack::
    .string "{PLAYER} helped the CAPTAIN\n"
    .string "steady his breathing!\p"
    .string "In... out...\n"
    .string "The noise fades.$"''',
        "SSAnne_CaptainsOffice_Text_ThankYouHaveHMForCut": '''SSAnne_CaptainsOffice_Text_ThankYouHaveHMForCut::
    .string "CAPTAIN: Whew! Thank you!\p"
    .string "The cargo signal got into\n"
    .string "my head for a moment.\p"
    .string "You want CUT clearance?\p"
    .string "Take this HIDDEN MACHINE.\p"
    .string "Teach CUT to a BRAINROT,\n"
    .string "and it can clear small trees.$"''',
        "SSAnne_CaptainsOffice_Text_ObtainedHM01FromCaptain": '''SSAnne_CaptainsOffice_Text_ObtainedHM01FromCaptain::
    .string "{PLAYER} obtained HM01\n"
    .string "from the CAPTAIN!$"''',
        "SSAnne_CaptainsOffice_Text_ExplainCut": '''SSAnne_CaptainsOffice_Text_ExplainCut::
    .string "Using CUT, you can clear\n"
    .string "small trees.\p"
    .string "Try it near SOUND PORT\n"
    .string "after earning License C.$"''',
        "SSAnne_CaptainsOffice_Text_SSAnneWillSetSailSoon": '''SSAnne_CaptainsOffice_Text_SSAnneWillSetSailSoon::
    .string "CAPTAIN: ...Whew!\p"
    .string "Now that I am steady again,\n"
    .string "we must depart.\p"
    .string "If that cargo signal spreads,\n"
    .string "SOUND PORT will hear it first.\p"
    .string "Farewell, candidate.\n"
    .string "Guard your thoughts.$"''',
        "SSAnne_CaptainsOffice_Text_YuckShouldntHaveLooked": '''SSAnne_CaptainsOffice_Text_YuckShouldntHaveLooked::
    .string "Yuck!\n"
    .string "The trash smells like static.$"''',
        "SSAnne_CaptainsOffice_Text_HowToConquerSeasickness": '''SSAnne_CaptainsOffice_Text_HowToConquerSeasickness::
    .string "How to Resist Signal Sickness...\n"
    .string "The CAPTAIN was reading this!$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(captain_path, text)


def main() -> None:
    patch_vermilion_city()
    patch_vermilion_gym()
    patch_ss_anne()
    print("Brainrot phase 5 Sound Port and License B story patch applied.")


if __name__ == "__main__":
    main()
