# P5.3g7-M3-FULL/R-A — pokus 8/10, support-ladder execution ledger

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-029`  
**Stav:** `ATTEMPT_8_CLOSED / REVIEW_J8_NUMERICAL_DRIVER_RESIDUAL`  
**Counter:** `8/10`  
**K4:** `LIVE / 60/100`, bez zmeny

## Ľudský význam

Test zisťuje, aký dlhý skorý rad je potrebný, aby už ďalšie dva rády menili
seed menej než o jednu milióntinu. Najprv sa vyrieši J6 a potom J8. Ak sa
koeficienty, ranky a Einsteinove holdouty stabilizujú a J6/J8 chvost prejde,
budeme vedieť, či minimálny production support je J4 alebo J6. Test stále nič
nehovorí o finite opacity, plnej hierarchii, CMB alebo S8.

## Frozen hashe

| physics | wrapper | runner |
|---|---|---|
| `070F217...1BF2` | `934AE0...E475` | `4B44F1...1F33` |

Predregistračný dokument 43 má finálny SHA-256
`2DBEA1249A8FDB9E7713A1989AAAAB1421CC1E9FECC924C36142AAD90238A939`.

## Očakávania a vetvy

| proces | očakávanie | PASS vetva | nonzero/timeout vetva |
|---|---|---|---|
| py_compile wrapper+runner | exit 0, <10 s | help | technický fail; žiadny solve |
| `--help` | exit 0, frozen CLI | J6 | technický fail; žiadny solve |
| J6 | 14/14 F0, 91/91 M3, M1 87/87; guards/holdouts/finite PASS, <4.8 s | J8 | stop; audit J6 alebo technická chyba |
| J8 | 18/18 F0, 117/117 M3, M1 109/109; guards/holdouts/finite PASS, <4.8 s | aggregate | stop; audit J8 alebo technická chyba |
| aggregate | presne J6+J8, J4 hash, four bridges, tails/powers/monotonic | hlavný číselný audit | review bez fyzikálnej smrti |

## Procesný ledger

| fáza | stav | dôkaz |
|---|---|---|
| static physics audit | PASS_SCOPE_ONLY | žiadna rovnica kopírovaná; iba shape guard mutácia/restoration |
| static math audit | PASS_STATIC_ONLY | M1 order6/8, finite, exact powers a tail schema overené |
| static documentation audit | PASS_AFTER_FIXES | názvy, poradie a release hranica uzavreté |
| py_compile | PASS | exit 0, wall 0.7 s; bez fyzikálneho významu |
| help | PASS | exit 0, wall 0.8 s; `support 6/8` a aggregate potvrdené |
| J6 | PASS | M1 87/87; F0 14/14; M3 91/91; 0 false checks; payload 1.172 s; SHA `658495...C4636A` |
| J8 | REVIEW | M1/F0/rank/holdout/guards PASS; iba M3 driver `1.5577e-10 > 1e-10`; SHA `1EE3FC...D51AB8` |
| aggregate | `NOT_RUN_BY_PREREGISTERED_STOP` | J8 exit 2, agregácia zakázaná |
| orchestrator audit | `REVIEW_NUMERICAL_RESIDUAL_PROVENANCE_REQUIRED` | nie formulačný ani fyzikálny STOP |

`NEXT_PROCESS = NONE_IN_ATTEMPT_8`  
`J6_SHA256 = 658495A11A3C72262CDCBEC9B9515794E506A6C7F14F40865704AA26E6C4636A`  
`J8_SHA256 = 1EE3FCDF3B77C6C7E4C26317A3F39AA45D4CFA5BA6B559E312E598BC3ED51AB8`
`EXTERNAL_LIMIT = 10 s`

## Release

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```
