# Custom Sprite Drop-ins

Put custom Roan and Brainrot sprites here.

The script below copies your files into the real FireRed graphics folders:

```bash
python3 tools/apply_custom_sprite_dropins.py
```

The GitHub Actions playtest build already runs this script.

Missing files are skipped, so you can add art slowly.

## Roan files

Put Roan overworld files in:

```text
custom_sprites/roan/
```

Minimum first file:

```text
custom_sprites/roan/red_normal.png
```

Optional Roan files later:

```text
custom_sprites/roan/red_item.png
custom_sprites/roan/red_surf_run.png
custom_sprites/roan/red_surf.png
custom_sprites/roan/red_bike.png
custom_sprites/roan/red_vs_seeker_bike.png
custom_sprites/roan/red_fish.png
custom_sprites/roan/player.pal
custom_sprites/roan/player_unused.pal
custom_sprites/roan/player_reflection.pal
```

These replace:

```text
graphics/object_events/pics/people/red_normal.png
graphics/object_events/palettes/player.pal
```

## Roan size notes

The current Red normal overworld source PNG is:

```text
144x32
```

So the safest first Roan sheet should also be:

```text
144x32 PNG
transparent background
indexed or clean 16-color style
```

It can still be edited later, but matching the old size avoids cursed build gremlins.

## Brainrot files

Put Brainrot sprites like this:

```text
custom_sprites/brainrots/chimpanzi/front.png
custom_sprites/brainrots/chimpanzi/back.png
custom_sprites/brainrots/chimpanzi/icon.png
custom_sprites/brainrots/chimpanzi/normal.pal
custom_sprites/brainrots/chimpanzi/shiny.pal
```

You do not need all files at once.

## First priority Brainrot folders

Starters:

```text
chimpanzi
bananini
avocador
cappucino
harpucino
capassino
tralalero
tralalito
tralalord
```

Test Zone 01:

```text
noobini
pizzanini
losnoobi
pipikiwi
pipicorni
timcheese
raccooni
```

Zone Green 01:

```text
bambini
crostini
bambilord
lirili
larila
lirilord
brrbrr
patapim
```

Early cave/checkpoint:

```text
trippi
troppilord
tungmini
tungmed
tungrock
moonini
moonlord
sleeprot
```

## Brainrot size notes

The original Pokemon battle sprites are usually:

```text
front.png 64x64
back.png 64x64
icon.png 32x64
```

Keep the same sizes when replacing.

## Important

Do not copy random sprites from the internet unless the license allows it.

Best safe route:

1. generate or draw original sprite
2. reduce to 16 colors
3. put PNG/pal here
4. run the playtest build
