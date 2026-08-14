# A2-K7 — stav a akčný plán po M-014d2a

**Dátum:** 2026-07-13  
**Kanonický stav K7:** `PREŽÍVA K7.0 — 30/100`  
**Najhlbšia podkoľaj:** mŕtva K1b1 — `41/100`  
**Aktívna podkoľaj:** K3.1-K2.2-K1b2

| Podkoľaj | Stav | Max. hĺbka | Dôvod/stena |
|---|---|---:|---|
| K7.1a-K1 | `MŔTVA M-014a` | `32/100` | fixed-width no-go |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | `34/100` | chýba odvodený kernel/noise |
| K7.1a-K3.0 | `PREŽILA FORMULAČNÚ BRÁNU` | `36/100` | chýba mikrofyzika |
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `38/100` | záporný Onsagerov eigenmode |
| K7.1a-K3.1-K2.1 | `PREŽÍVA IBA ROZMEROVÚ BACKGROUNDOVÚ EXISTENCIU` | `39/100` | voľné `ell_hat`, bath a noise |
| K7.1a-K3.1-K2.2-K1a | `MŔTVA M-014d1` | `40/100` | gravitačný rate je o 83–97 rádov slabý |
| K7.1a-K3.1-K2.2-K1b1 | `MŔTVA M-014d2a` | `41/100` | vedúci spin-2 coupling vyžaduje `~1e24` zosilnenie |
| **K7.1a-K3.1-K2.2-K1b2** | **`AKTÍVNA`** | **`5/100`** | curvature operator basis/cutoff neauditované |
| K7.1a-K3.1-K2.2-K1b3 | `ČAKÁ` | `5/100` | ďalší massless spin-2 nosič |
| K7.1a-K3.1-K2.2-K1c | `ČAKÁ` | `5/100` | nový nespin-2 bath |
| K7.1a-K3.1-K2.2-K1d | `ČAKÁ` | `5/100` | interný tracked bath |

## Ďalší krok

K1b2 dostane analytický operator-basis audit a skript 62 pre energetické
škálovanie/cutoff. Nesmie sa použiť jediný schematický člen `R O/Lambda^n`
bez kontroly, či nie je on-shell nulový alebo redundantný. Ak všetky
operátory zomrú, K1b vetva zomrie; potom sa pokračuje K1c.

## Kontrola errata

Pri každom budúcom súhrne sa musí uviesť, že M-014d2a platí iba pre K1b1.
Pôvodný preširoký skript 61 sa zachováva ako auditná stopa, ale jeho
preširoký text nemá kanonickú platnosť.

