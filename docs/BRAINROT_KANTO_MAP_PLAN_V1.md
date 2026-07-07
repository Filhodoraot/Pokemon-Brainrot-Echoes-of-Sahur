# Brainrot Kanto map plan V1

This file plans how the FireRed Kanto map becomes the world of Brainrot: Echoes of Sahur.

## Map design rule

Use Kanto as the base.

Do not rebuild everything from zero at first.

Rename and repurpose existing towns, routes, caves, and dungeons.

This keeps the ROM playable faster.

## World structure

Kanto is divided into official zones after the Sahur Incident.

The old Pokemon world names still exist in code, but in story they become:

- Training Centers
- Safe Zones
- Test Zones
- Restricted Zones
- Corruption Zones
- Memory Zones
- Sahur Zones

## Early game map

### Pallet Town -> Training Center 01

Role:

- starting town
- Roan's home
- Dr. Avelar's lab
- first Brainrot selection
- Kiunin rival intro

Story name:

```txt
Training Center 01
```

Gameplay use:

- player house
- Avelar lab
- first starter event
- first rival battle

### Route 1 -> Test Zone 01

Role:

- first wild Brainrot area
- catch test
- License E preparation

Main wild Brainrots:

```txt
NOOBINI
PIPIKIWI
TIMCHEESE
RACCOONI rare
```

Story name:

```txt
Test Zone 01
```

### Viridian City -> Safe Zone 01

Role:

- first city hub
- early shops
- Brainrot safety rules
- first signs of Sahur normalization

Story name:

```txt
Safe Zone 01
```

### Viridian Forest -> Zone Green 01

Role:

- first real dungeon
- field demon history
- Cult of the First Sound appears
- first Sahur Fragment

Story name:

```txt
Zone Green 01
```

## License path

The old gym route becomes the official license system.

| Old area | New role | License/story use |
|---|---|---|
| Pallet Town | Training Center 01 | start |
| Route 1 | Test Zone 01 | wild Brainrot tutorial |
| Viridian City | Safe Zone 01 | basic survival rules |
| Viridian Forest | Zone Green 01 | first dungeon |
| Pewter City | License D City | survival and discipline test |
| Mt. Moon | Moon Noise Cave | first deeper Sahur distortion |
| Cerulean City | License C City | child disappearance investigation |
| Vermilion City | Sound Port | Sahur sound smuggling |
| Rock Tunnel | Echo Tunnel | noise-memory dungeon |
| Lavender Town | Memory Town | ghosts, erased names, Luna clues |
| Celadon City | Skibidy Zone entry | sewer corruption arc |
| Saffron City | Cognia Core City | hospital ruins and main truth |
| Fuchsia City | Wild Reserve Zone | advanced capture/survival test |
| Cinnabar Island | Experiment Island | Dante/Cognia experiments |
| Victory Road | License S Road | final human-side trial |
| Indigo Plateau | Supreme License Center | final license gate |

## Main story zones

### Cave 67

Possible base:

- Mt. Moon side area
- Rock Tunnel hidden section
- new cave map later

Role:

- 67 Echo encounter
- gesture loop mechanics
- Roan saves Kiunin
- first strong proof that numbers/sounds can control minds

### Skibidy Sewers

Possible base:

- Celadon Rocket Hideout
- new sewer-style tiles later

Role:

- spatial corruption
- wrong doors
- looping rooms
- Skibidy cult

### Red Garden

Possible base:

- Berry Forest style later
- Fuchsia/Safari style area
- custom memory garden later

Role:

- Strawberry Helefanto
- stolen emotional memories
- Dr. Renan Veyr sacrifice
- Kiunin lock break

### Area Null

Possible base:

- Cinnabar Mansion
- glitch lab
- Silph Co. corrupted floors

Role:

- reality bugs
- NPC text breaks
- maps loop
- Dante tests extraction machines

### Sahur Realm

Possible base:

- custom endgame maps
- surreal versions of old places

Role:

- Luna rescue
- four altars
- final boss

## City identity changes

### Pewter City

New identity:

```txt
Stone Discipline Zone
```

Theme:

- first harsh license trainer
- teaches that brute strength is not enough

### Cerulean City

New identity:

```txt
Missing Children Case Zone
```

Theme:

- investigation
- children returning less curious
- License C buildup

### Vermilion City

New identity:

```txt
Sound Port
```

Theme:

- illegal Sahur recordings
- ships carrying corrupted audio

### Lavender Town

New identity:

```txt
Memory Town
```

Theme:

- names erased from graves
- forgotten people
- Luna clues

### Celadon City

New identity:

```txt
Skibidy Corruption City
```

Theme:

- normal city above
- impossible sewer below

### Saffron City

New identity:

```txt
Cognia Core City
```

Theme:

- Cognia Institute
- Central Hospital ruins
- final truth hub

### Cinnabar Island

New identity:

```txt
Experiment Island
```

Theme:

- abandoned research
- Dante's early work
- artificial Brainrot tests

## Early route encounter plan

### Test Zone 01 / Route 1

Common:

```txt
PIPIKIWI
NOOBINI
```

Uncommon:

```txt
TIMCHEESE
```

Rare:

```txt
RACCOONI
```

## Map progression V1

```txt
Training Center 01
-> Test Zone 01
-> Safe Zone 01
-> Zone Green 01
-> License D City
-> Moon Noise Cave
-> License C City
-> Sound Port
-> Echo Tunnel
-> Memory Town
-> Skibidy Zone
-> Cognia Core City
-> Wild Reserve Zone
-> Experiment Island
-> Area Null
-> Hospital Ruins
-> Sahur Realm
```

## Development order

1. Rename early maps through text only.
2. Change early NPC dialogue.
3. Change wild encounters.
4. Change trainer names.
5. Change signs and city names.
6. Add new events.
7. Edit tiles/maps later.
8. Add custom areas last.

## Important note

For the first playable build, do not redraw the entire map.

Use the FireRed map as a skeleton.

The world becomes Brainrot Kanto through text, events, encounters, and later tiles.
