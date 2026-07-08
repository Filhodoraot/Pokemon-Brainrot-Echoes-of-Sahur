#!/usr/bin/env python3
"""Phase 6 story pass for Brainrot: Echoes of Sahur.

This pass converts Lavender and Pokemon Tower into:
- MEMORY TOWN, a place where missing memories collect.
- MEMORY TOWER, where echoes of erased people and BRAINROTS remain.
- Stronger Luna hints.
- Stronger 67 possession foreshadowing.
- Echo Masks replacing Rocket grunts on the tower peak.
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


def patch_lavender_town() -> None:
    path = "data/maps/LavenderTown/text.inc"
    text = read(path)
    replacements = {
        "LavenderTown_Text_DoYouBelieveInGhosts": '''LavenderTown_Text_DoYouBelieveInGhosts::
    .string "Do you believe memories can\n"
    .string "walk after being erased?$"''',
        "LavenderTown_Text_SoThereAreBelievers": '''LavenderTown_Text_SoThereAreBelievers::
    .string "Really?\p"
    .string "Then you may hear the tower\n"
    .string "calling back.$"''',
        "LavenderTown_Text_JustImaginingWhiteHand": '''LavenderTown_Text_JustImaginingWhiteHand::
    .string "Hahaha, I guess not.\p"
    .string "That small hand on your\n"
    .string "shoulder...\p"
    .string "I am just imagining it.$"''',
        "LavenderTown_Text_TownKnownAsMonGraveSite": '''LavenderTown_Text_TownKnownAsMonGraveSite::
    .string "This town is known as\n"
    .string "MEMORY TOWN.\p"
    .string "People come here to mourn\n"
    .string "things they cannot prove\n"
    .string "they lost.$"''',
        "LavenderTown_Text_GhostsAppearedInTower": '''LavenderTown_Text_GhostsAppearedInTower::
    .string "Echoes appeared in MEMORY TOWER.\p"
    .string "Some say they are BRAINROTS.\p"
    .string "Some say they are children\n"
    .string "COGNIA forgot on purpose.$"''',
        "LavenderTown_Text_TownSign": '''LavenderTown_Text_TownSign::
    .string "MEMORY TOWN\n"
    .string "Where forgotten names still echo$"''',
        "LavenderTown_Text_SilphScopeNotice": '''LavenderTown_Text_SilphScopeNotice::
    .string "New SILPH SCOPE!\n"
    .string "Make hidden echoes visible!\p"
    .string "COGNIA / SILPH RESEARCH$"''',
        "LavenderTown_Text_VolunteerPokemonHouse": '''LavenderTown_Text_VolunteerPokemonHouse::
    .string "MEMORY HOUSE\n"
    .string "For lost partners and lost people$"''',
        "LavenderTown_Text_PokemonTowerSign": '''LavenderTown_Text_PokemonTowerSign::
    .string "MEMORY TOWER\n"
    .string "Do not repeat what repeats you$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_tower_1f() -> None:
    path = "data/maps/PokemonTower_1F/text.inc"
    text = read(path)
    replacements = {
        "PokemonTower_1F_Text_ErectedInMemoryOfDeadMons": '''PokemonTower_1F_Text_ErectedInMemoryOfDeadMons::
    .string "MEMORY TOWER was built for\n"
    .string "lost BRAINROTS, missing people,\n"
    .string "and names no record keeps.$"''',
        "PokemonTower_1F_Text_ComeToPayRespectsSon": '''PokemonTower_1F_Text_ComeToPayRespectsSon::
    .string "Did you come to pay respects?\p"
    .string "Bless your steady heart, son.\p"
    .string "The tower is loud today.$"''',
        "PokemonTower_1F_Text_ComeToPayRespectsGirl": '''PokemonTower_1F_Text_ComeToPayRespectsGirl::
    .string "Did you come to pay respects?\p"
    .string "Bless your steady heart, girl.\p"
    .string "The tower is loud today.$"''',
        "PokemonTower_1F_Text_CameToPrayForDepartedClefairy": '''PokemonTower_1F_Text_CameToPrayForDepartedClefairy::
    .string "I came to pray for my\n"
    .string "departed partner.\p"
    .string "When I close my eyes, I hear\n"
    .string "a child counting... six... seven...$"''',
        "PokemonTower_1F_Text_GrowlitheWhyDidYouDie": '''PokemonTower_1F_Text_GrowlitheWhyDidYouDie::
    .string "My partner...\p"
    .string "Why does everyone remember\n"
    .string "you, but Roan remembers a girl\n"
    .string "no one else does?$"''',
        "PokemonTower_1F_Text_SenseSpiritsUpToMischief": '''PokemonTower_1F_Text_SenseSpiritsUpToMischief::
    .string "I am a CHANNELER.\p"
    .string "There are echoes above.\n"
    .string "They are not all dead.\p"
    .string "Some are trapped memories.$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_tower_2f() -> None:
    path = "data/maps/PokemonTower_2F/text.inc"
    text = read(path)
    replacements = {
        "PokemonTower_2F_Text_RivalIntro": '''PokemonTower_2F_Text_RivalIntro::
    .string "{RIVAL}: Hey, {PLAYER}!\p"
    .string "Why are you here?\n"
    .string "Looking for your fake sister?\p"
    .string "...Why did I say that?\p"
    .string "Whatever. This place is making\n"
    .string "my head itch.\p"
    .string "Battle me before the tower\n"
    .string "starts talking again!$"''',
        "PokemonTower_2F_Text_RivalDefeat": '''PokemonTower_2F_Text_RivalDefeat::
    .string "What?\n"
    .string "No way!\p"
    .string "The tower messed with me!$"''',
        "PokemonTower_2F_Text_RivalVictory": '''PokemonTower_2F_Text_RivalVictory::
    .string "{RIVAL}: See?\p"
    .string "You cannot save memories\n"
    .string "with a weak team.$"''',
        "PokemonTower_2F_Text_RivalPostBattle": '''PokemonTower_2F_Text_RivalPostBattle::
    .string "{RIVAL}: I logged a rare\n"
    .string "BRAINROT here, but the page\n"
    .string "erased itself.\p"
    .string "It left only two numbers:\n"
    .string "six and seven.\p"
    .string "My dad says not to chase\n"
    .string "old tower signals.\p"
    .string "So obviously I am leaving.\n"
    .string "You can get haunted alone.$"''',
        "PokemonTower_2F_Text_SilphScopeCouldUnmaskGhosts": '''PokemonTower_2F_Text_SilphScopeCouldUnmaskGhosts::
    .string "Even we cannot identify\n"
    .string "these memory echoes.\p"
    .string "A SILPH SCOPE may reveal\n"
    .string "what they really are.$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_tower_3f_to_6f() -> None:
    replacements_by_file = {
        "data/maps/PokemonTower_3F/text.inc": {
            "PokemonTower_3F_Text_HopeIntro": '''PokemonTower_3F_Text_HopeIntro::
    .string "Lu...na...\n"
    .string "Do not forget...$"''',
            "PokemonTower_3F_Text_HopeDefeat": '''PokemonTower_3F_Text_HopeDefeat::
    .string "Hwa!\n"
    .string "I can think again!$"''',
            "PokemonTower_3F_Text_HopePostBattle": '''PokemonTower_3F_Text_HopePostBattle::
    .string "The tower spoke through me.\p"
    .string "It said one name.\n"
    .string "LUNA.$"''',
            "PokemonTower_3F_Text_CarlyIntro": '''PokemonTower_3F_Text_CarlyIntro::
    .string "Six...\n"
    .string "Seven...$"''',
            "PokemonTower_3F_Text_CarlyDefeat": '''PokemonTower_3F_Text_CarlyDefeat::
    .string "Hmm?\n"
    .string "What was I counting?$"''',
            "PokemonTower_3F_Text_CarlyPostBattle": '''PokemonTower_3F_Text_CarlyPostBattle::
    .string "Sorry!\p"
    .string "A number got stuck in\n"
    .string "my mouth.$"''',
            "PokemonTower_3F_Text_PatriciaIntro": '''PokemonTower_3F_Text_PatriciaIntro::
    .string "Be gone!\n"
    .string "False memory!$"''',
            "PokemonTower_3F_Text_PatriciaDefeat": '''PokemonTower_3F_Text_PatriciaDefeat::
    .string "Whew!\n"
    .string "The echo left!$"''',
            "PokemonTower_3F_Text_PatriciaPostBattle": '''PokemonTower_3F_Text_PatriciaPostBattle::
    .string "The others above are caught\n"
    .string "inside repeated sounds.$"''',
        },
        "data/maps/PokemonTower_4F/text.inc": {
            "PokemonTower_4F_Text_PaulaIntro": '''PokemonTower_4F_Text_PaulaIntro::
    .string "Hospital lights! No!\n"
    .string "White flash!$"''',
            "PokemonTower_4F_Text_PaulaDefeat": '''PokemonTower_4F_Text_PaulaDefeat::
    .string "Where is the light?$"''',
            "PokemonTower_4F_Text_PaulaPostBattle": '''PokemonTower_4F_Text_PaulaPostBattle::
    .string "I saw a hospital hallway.\p"
    .string "But I have never been there.$"''',
            "PokemonTower_4F_Text_LaurelIntro": '''PokemonTower_4F_Text_LaurelIntro::
    .string "Repeat with me!\n"
    .string "Tung... tung...$"''',
            "PokemonTower_4F_Text_LaurelDefeat": '''PokemonTower_4F_Text_LaurelDefeat::
    .string "What!$"''',
            "PokemonTower_4F_Text_LaurelPostBattle": '''PokemonTower_4F_Text_LaurelPostBattle::
    .string "We cannot determine the\n"
    .string "identity of the echoes...$"''',
            "PokemonTower_4F_Text_JodyIntro": '''PokemonTower_4F_Text_JodyIntro::
    .string "Do not remember!\n"
    .string "Remembering hurts!$"''',
            "PokemonTower_4F_Text_JodyDefeat": '''PokemonTower_4F_Text_JodyDefeat::
    .string "Huh?\n"
    .string "Who? What?$"''',
            "PokemonTower_4F_Text_JodyPostBattle": '''PokemonTower_4F_Text_JodyPostBattle::
    .string "May lost BRAINROTS and\n"
    .string "lost people rest in peace...$"''',
        },
        "data/maps/PokemonTower_5F/text.inc": {
            "PokemonTower_5F_Text_RestHereInPurifiedSpace": '''PokemonTower_5F_Text_RestHereInPurifiedSpace::
    .string "Come, child!\n"
    .string "This floor is protected.\p"
    .string "Rest here before the tower\n"
    .string "puts words in your mouth.$"''',
            "PokemonTower_5F_Text_TammyIntro": '''PokemonTower_5F_Text_TammyIntro::
    .string "Give... me...\n"
    .string "your... name...$"''',
            "PokemonTower_5F_Text_TammyDefeat": '''PokemonTower_5F_Text_TammyDefeat::
    .string "Gasp!$"''',
            "PokemonTower_5F_Text_TammyPostBattle": '''PokemonTower_5F_Text_TammyPostBattle::
    .string "I was under a memory echo.$"''',
            "PokemonTower_5F_Text_RuthIntro": '''PokemonTower_5F_Text_RuthIntro::
    .string "You... shall...\n"
    .string "forget... her...$"''',
            "PokemonTower_5F_Text_RuthDefeat": '''PokemonTower_5F_Text_RuthDefeat::
    .string "What a nightmare!$"''',
            "PokemonTower_5F_Text_RuthPostBattle": '''PokemonTower_5F_Text_RuthPostBattle::
    .string "I was trapped in someone\n"
    .string "else's forgotten fear.$"''',
            "PokemonTower_5F_Text_KarinaIntro": '''PokemonTower_5F_Text_KarinaIntro::
    .string "Static children!$"''',
            "PokemonTower_5F_Text_KarinaDefeat": '''PokemonTower_5F_Text_KarinaDefeat::
    .string "Ha?$"''',
            "PokemonTower_5F_Text_KarinaPostBattle": '''PokemonTower_5F_Text_KarinaPostBattle::
    .string "I regained my senses.$"''',
            "PokemonTower_5F_Text_JanaeIntro": '''PokemonTower_5F_Text_JanaeIntro::
    .string "Urgah...\n"
    .string "Six... seven...$"''',
            "PokemonTower_5F_Text_JanaeDefeat": '''PokemonTower_5F_Text_JanaeDefeat::
    .string "Whoo!$"''',
            "PokemonTower_5F_Text_JanaePostBattle": '''PokemonTower_5F_Text_JanaePostBattle::
    .string "I trained in the mountains,\n"
    .string "but the number still found me.$"''',
            "PokemonTower_5F_Text_PurifiedZoneMonsFullyHealed": '''PokemonTower_5F_Text_PurifiedZoneMonsFullyHealed::
    .string "Entered the protected memory zone.\p"
    .string "{PLAYER}'s BRAINROTS were fully\n"
    .string "healed.$"''',
        },
        "data/maps/PokemonTower_6F/text.inc": {
            "PokemonTower_6F_Text_AngelicaIntro": '''PokemonTower_6F_Text_AngelicaIntro::
    .string "Give... me...\n"
    .string "your... focus...$"''',
            "PokemonTower_6F_Text_AngelicaDefeat": '''PokemonTower_6F_Text_AngelicaDefeat::
    .string "Groan!$"''',
            "PokemonTower_6F_Text_AngelicaPostBattle": '''PokemonTower_6F_Text_AngelicaPostBattle::
    .string "My head feels empty...\n"
    .string "like someone skimmed thoughts off.$"''',
            "PokemonTower_6F_Text_EmiliaIntro": '''PokemonTower_6F_Text_EmiliaIntro::
    .string "LUNA is not real!\n"
    .string "LUNA is not real!$"''',
            "PokemonTower_6F_Text_EmiliaDefeat": '''PokemonTower_6F_Text_EmiliaDefeat::
    .string "Something fell silent!$"''',
            "PokemonTower_6F_Text_EmiliaPostBattle": '''PokemonTower_6F_Text_EmiliaPostBattle::
    .string "Why did I say that name?\p"
    .string "I do not know any Luna.$"''',
            "PokemonTower_6F_Text_JenniferIntro": '''PokemonTower_6F_Text_JenniferIntro::
    .string "Ke... ke... ke...\n"
    .string "67... 67...$"''',
            "PokemonTower_6F_Text_JenniferDefeat": '''PokemonTower_6F_Text_JenniferDefeat::
    .string "Keee!$"''',
            "PokemonTower_6F_Text_JenniferPostBattle": '''PokemonTower_6F_Text_JenniferPostBattle::
    .string "What is going on here?$"''',
            "PokemonTower_6F_Text_BeGoneIntruders": '''PokemonTower_6F_Text_BeGoneIntruders::
    .string "Be gone...\n"
    .string "Name thieves...$"''',
            "PokemonTower_6F_Text_GhostWasCubonesMother": '''PokemonTower_6F_Text_GhostWasCubonesMother::
    .string "The echo was not just a ghost.\p"
    .string "It was a memory knot formed\n"
    .string "around a lost BRAINROT.$"''',
            "PokemonTower_6F_Text_MothersSpiritWasCalmed": '''PokemonTower_6F_Text_MothersSpiritWasCalmed::
    .string "The memory knot was calmed.\p"
    .string "Before fading, it whispered:\n"
    .string "LUNA REMEMBERS YOU.$"''',
        },
    }

    for path, replacements in replacements_by_file.items():
        text = read(path)
        for label, block in replacements.items():
            text = replace_label_block(text, label, block)
        write(path, text)


def patch_tower_7f() -> None:
    path = "data/maps/PokemonTower_7F/text.inc"
    text = read(path)
    replacements = {
        "PokemonTower_7F_Text_Grunt1Intro": '''PokemonTower_7F_Text_Grunt1Intro::
    .string "What do you want?\n"
    .string "Why are you here?\p"
    .string "The Echo Masks collect\n"
    .string "names before COGNIA buries them.$"''',
        "PokemonTower_7F_Text_Grunt1Defeat": '''PokemonTower_7F_Text_Grunt1Defeat::
    .string "I give up!$"''',
        "PokemonTower_7F_Text_Grunt1PostBattle": '''PokemonTower_7F_Text_Grunt1PostBattle::
    .string "DANTE will remember this.\p"
    .string "Even if Kanto does not.$"''',
        "PokemonTower_7F_Text_Grunt2Intro": '''PokemonTower_7F_Text_Grunt2Intro::
    .string "This old man marched right\n"
    .string "up to our tower post.\p"
    .string "He kept saying the dead\n"
    .string "are not the problem.\p"
    .string "The erased are.$"''',
        "PokemonTower_7F_Text_Grunt2Defeat": '''PokemonTower_7F_Text_Grunt2Defeat::
    .string "Please!\n"
    .string "No more!$"''',
        "PokemonTower_7F_Text_Grunt2PostBattle": '''PokemonTower_7F_Text_Grunt2PostBattle::
    .string "BRAINROTS are power.\p"
    .string "Names are power.\p"
    .string "Why should we leave either\n"
    .string "unused?$"''',
        "PokemonTower_7F_Text_Grunt3Intro": '''PokemonTower_7F_Text_Grunt3Intro::
    .string "You are not saving anyone, kid!\p"
    .string "Some people are happier\n"
    .string "when they stop thinking.$"''',
        "PokemonTower_7F_Text_Grunt3Defeat": '''PokemonTower_7F_Text_Grunt3Defeat::
    .string "Do not fight the Echo Masks!$"''',
        "PokemonTower_7F_Text_Grunt3PostBattle": '''PokemonTower_7F_Text_Grunt3PostBattle::
    .string "You are not getting away\n"
    .string "with this!$"''',
        "PokemonTower_7F_Text_MrFujiThankYouFollowMe": '''PokemonTower_7F_Text_MrFujiThankYouFollowMe::
    .string "MR. FUJI: Heh?\n"
    .string "You came to save me?\p"
    .string "Thank you. But I came here\n"
    .string "of my own free will.\p"
    .string "This tower holds memories\n"
    .string "that COGNIA calls errors.\p"
    .string "I heard a girl's name here.\n"
    .string "LUNA.\p"
    .string "If you remember her, Roan,\n"
    .string "then she is not gone.\p"
    .string "Follow me to MEMORY HOUSE,\n"
    .string "at the foot of this tower.$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def patch_memory_house() -> None:
    path = "data/maps/LavenderTown_VolunteerPokemonHouse/text.inc"
    text = read(path)
    replacements = {
        "LavenderTown_PokemonCenter_1F_Text_HearMrFujiNotFromAroundHere": '''LavenderTown_PokemonCenter_1F_Text_HearMrFujiNotFromAroundHere::
    .string "I recently moved here.\p"
    .string "MR. FUJI is not from\n"
    .string "MEMORY TOWN either.\p"
    .string "He says erased people leave\n"
    .string "heavier echoes than ghosts.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_WhereDidMrFujiGo": '''LavenderTown_VolunteerPokemonHouse_Text_WhereDidMrFujiGo::
    .string "That is odd, MR. FUJI\n"
    .string "is not here.\p"
    .string "He went to the tower after\n"
    .string "he heard a child singing.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_MrFujiWasPrayingForCubonesMother": '''LavenderTown_VolunteerPokemonHouse_Text_MrFujiWasPrayingForCubonesMother::
    .string "MR. FUJI had been praying\n"
    .string "for a trapped memory knot\n"
    .string "inside the tower.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_MrFujiLooksAfterOrphanedMons": '''LavenderTown_VolunteerPokemonHouse_Text_MrFujiLooksAfterOrphanedMons::
    .string "This is MR. FUJI's house.\p"
    .string "He looks after abandoned\n"
    .string "BRAINROTS and people who\n"
    .string "lost pieces of themselves.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_MonsNiceToHug": '''LavenderTown_VolunteerPokemonHouse_Text_MonsNiceToHug::
    .string "It is warm!\n"
    .string "Some BRAINROTS calm down\n"
    .string "when hugged.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_Nidorino": '''LavenderTown_VolunteerPokemonHouse_Text_Nidorino::
    .string "BRAINROT: Grrr...$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_Psyduck": '''LavenderTown_VolunteerPokemonHouse_Text_Psyduck::
    .string "BRAINROT: Gwappa!$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_IdLikeYouToHaveThis": '''LavenderTown_VolunteerPokemonHouse_Text_IdLikeYouToHaveThis::
    .string "MR. FUJI: {PLAYER}...\p"
    .string "Your BRAINDEX quest needs\n"
    .string "more than courage.\p"
    .string "It needs love for what\n"
    .string "Kanto wants to forget.\p"
    .string "This may help you wake\n"
    .string "sleeping BRAINROTS and\n"
    .string "sleeping memories.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_ReceivedPokeFluteFromMrFuji": '''LavenderTown_VolunteerPokemonHouse_Text_ReceivedPokeFluteFromMrFuji::
    .string "{PLAYER} received the\n"
    .string "MEMORY FLUTE from MR. FUJI.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_ExplainPokeFlute": '''LavenderTown_VolunteerPokemonHouse_Text_ExplainPokeFlute::
    .string "Upon hearing the MEMORY FLUTE,\n"
    .string "sleeping BRAINROTS may wake.\p"
    .string "Try using it on BRAINROTS\n"
    .string "blocking silent roads.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_HasPokeFluteHelpedYou": '''LavenderTown_VolunteerPokemonHouse_Text_HasPokeFluteHelpedYou::
    .string "MR. FUJI: Has the MEMORY FLUTE\n"
    .string "helped you?$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_GrandPrizeDrawingClipped": '''LavenderTown_VolunteerPokemonHouse_Text_GrandPrizeDrawingClipped::
    .string "BRAINROT FIELD MAGAZINE\p"
    .string "Monthly report form...\p"
    .string "Gone!\p"
    .string "Someone clipped out the page\n"
    .string "about missing children.$"''',
        "LavenderTown_VolunteerPokemonHouse_Text_PokemonMagazinesLineShelf": '''LavenderTown_VolunteerPokemonHouse_Text_PokemonMagazinesLineShelf::
    .string "BRAINROT magazines line\n"
    .string "the shelf.\p"
    .string "BRAINROT INSIDER...\p"
    .string "COGNIA SAFE HANDLING...$"''',
    }
    for label, block in replacements.items():
        text = replace_label_block(text, label, block)
    write(path, text)


def main() -> None:
    patch_lavender_town()
    patch_tower_1f()
    patch_tower_2f()
    patch_tower_3f_to_6f()
    patch_tower_7f()
    patch_memory_house()
    print("Brainrot phase 6 Memory Town story patch applied.")


if __name__ == "__main__":
    main()
