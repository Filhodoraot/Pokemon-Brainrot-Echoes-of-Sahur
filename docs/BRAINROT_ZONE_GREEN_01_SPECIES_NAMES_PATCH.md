# Zone Green 01 species names patch

Target file:

`src/data/text/species_names.h`

This patch adds battle names for the Viridian Forest / Zone Green 01 Brainrots.

## Important rule

Pokemon battle names have a short limit.

So the full Brainrot name can be used in Braindex/lore, but battle names must stay short.

## Replace these species names

```c
[SPECIES_CATERPIE]   = _("BAMBINI"),
[SPECIES_METAPOD]    = _("CROSTINI"),
[SPECIES_BUTTERFREE] = _("BAMBILORD"),

[SPECIES_WEEDLE]     = _("LIRILI"),
[SPECIES_KAKUNA]     = _("LARILA"),
[SPECIES_BEEDRILL]   = _("LIRILORD"),

[SPECIES_PIKACHU]    = _("BRRBRR"),
[SPECIES_RAICHU]     = _("PATAPIM"),
```

## Full name mapping

| Original slot | Battle name | Full Brainrot name | Stage |
|---|---|---|---|
| Caterpie | BAMBINI | Bambini Crostini | Baby |
| Metapod | CROSTINI | Bambini Crostini | Teen |
| Butterfree | BAMBILORD | Bambini Crostini | Adult |
| Weedle | LIRILI | Lirili Larila | Baby |
| Kakuna | LARILA | Lirili Larila | Teen |
| Beedrill | LIRILORD | Lirili Larila | Adult |
| Pikachu | BRRBRR | Brr Brr Patapim | Baby or single-stage placeholder |
| Raichu | PATAPIM | Brr Brr Patapim | Adult placeholder |

## Notes

Brr Brr Patapim is listed as an evolving Brainrot in the sprite plan.

For the first build, use:

```txt
BRRBRR -> PATAPIM
```

This uses the existing Pikachu -> Raichu structure.

Later, if needed, make it a 3-stage line with a new middle slot.

## Safe warning

Do not use accents here.

Use:

```txt
LIRILI
LARILA
```

Not accented text.
