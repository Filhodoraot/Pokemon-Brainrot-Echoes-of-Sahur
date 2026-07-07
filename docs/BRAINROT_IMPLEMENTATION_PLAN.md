# Brainrot implementation plan

This file tracks how the ROM will be changed without breaking the build.

## Rule

Do not change everything at once. Each phase should compile before moving to the next one.

## Phase 1: Story documents

Status: started.

Files:
- docs/BRAINROT_STORY.md
- docs/BRAINROT_IMPLEMENTATION_PLAN.md
- docs/BRAINROT_POKEDEX_V1.md
- docs/BRAINROT_MOVES_ABILITIES_V1.md

Goal: keep the full idea safe before editing game data.

## Phase 2: Early-game text

Goal: make the start of the game feel like Brainrot: Echoes of Sahur.

Target files:
- data/maps/PalletTown/text.inc
- data/maps/PalletTown_ProfessorOaksLab/text.inc
- data/maps/PlayersHouse_1F/text.inc
- data/maps/PlayersHouse_2F/text.inc
- data/maps/Route1/text.inc
- data/maps/ViridianCity/text.inc

Changes:
- Oak becomes Dr. Avelar.
- Pokemon become Brainrots in visible dialogue.
- Poke Balls become Brainrot Balls in visible dialogue.
- Pokedex becomes Braindex in visible dialogue.
- Pallet Town becomes Training Center 01 in signs.
- Route 1 becomes a test zone.

## Phase 3: Starters

Goal: replace the FireRed starters in name and data first, before custom sprites.

Starter set:
- Bulbasaur slot -> Chimpanzini Bananini
- Charmander slot -> Cappuccino Assassino
- Squirtle slot -> Tralalero Tralala

Why use old slots first:
- Safer for compiling.
- Less tables to expand.
- Sprites can remain temporary until custom art is ready.

Target files:
- src/data/text/species_names.h
- src/data/pokemon/species_info.h
- src/data/pokemon/pokedex_entries.h
- src/data/pokemon/level_up_learnsets.h

## Phase 4: Route encounters

Goal: replace early wild Pokemon with common Brainrots.

Route 1 early Brainrots:
- Pipi Kiwi
- Noobini Pizzanini
- Tim Cheese
- Raccooni Jandelini

Viridian Forest Brainrots:
- Brr Brr Patapim
- Bandito Bobritto
- Boneca Ambalabu
- Trippi Troppi
- Tree Tree Tree Sahur as a story boss later

Target files:
- data/wild_encounters.json

## Phase 5: License system

The original gym badge structure will stay internally at first, but visible dialogue will call it Brainrot Licenses.

Badge replacements in story:
- Boulder Badge -> License E
- Cascade Badge -> License D
- Thunder Badge -> License C
- Rainbow Badge -> License B
- Soul Badge -> License A
- Marsh Badge -> Cognition Pass
- Volcano Badge -> Null Zone Pass
- Earth Badge -> License S

This keeps the engine stable while changing the lore.

## Phase 6: Types

Start by reusing old Pokemon types with renamed flavor.

Later add custom types:
- MEME
- SOUND
- GLITCH
- MEMORY
- CHAOS
- SWEET
- COSMIC

Adding types touches battle logic and should be done after the early game is stable.

## Phase 7: Moves and abilities

Add Brainrot-themed moves after species names and starters work.

Add legendary abilities last, because unique abilities may require custom C code.

## Phase 8: Sprites

Hardest phase.

Temporary plan:
- Use original sprites as placeholders.
- Replace names, stats, text, encounters first.
- Add custom sprites one species at a time.

Sprite files to study later:
- src/data/pokemon_graphics/front_pic_table.h
- src/data/pokemon_graphics/back_pic_table.h
- src/data/pokemon_graphics/palette_table.h
- graphics/pokemon/

## Phase 9: Story events

After text and starter changes compile, add new event scenes:

Early events:
- Avelar stops Roan before Route 1.
- First Brainrot partner test.
- First mention of Luna.
- First Cognia Institute clue.

Mid-game events:
- Cult of the First Sound.
- Cave 67.
- Dante Vilar reveal.
- Skibidy corruption.
- Strawberry Helefanto memory test.

End-game events:
- Sahur Realm.
- Tung Tung God Form.
- Supreme Tung Tung.

## Build safety

After each phase:
1. Compile.
2. Test new game start.
3. Test starter choice.
4. Test Route 1 wild battle.
5. Commit only if stable.
