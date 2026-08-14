# A2-K7 — kanonický stav podkoľají a Max. hĺbka

**Dátum:** 2026-07-13  
**Aktualizácia:** po jednotnej sekvenčnej rekalibrácii G0–G10  
**Kanonická max. prejdená hĺbka K7:** `20/100`

## Jednotná stupnica

K7 používa rovnaké G0–G10 ako všetky ostatné A2 koľaje. Rodina prešla G2:
formálny background a celkový ledger. G3 však neprešla žiadna konkrétna
mikrofyzická dcéra, pretože chýba súčasne odvodený lokálny kernel,
`delta Q`, noise/memory a pozitivita.

Staré skóre `32–42/100` sa zachováva iba ako **historický intra-G3
checkpoint**. Neznamená vyššiu kanonickú hĺbku než G3 a nesmie sa porovnávať
s G4/G5/G6 iných koľají.

`Kanonická hĺbka 20` sa dedí iba v rozsahu nezmeneného K7 backgroundu a
ledgeru. Každá dcéra musí G3 prejsť sama.

## Aktuálna tabuľka
| Podkoľaj | Stav | Kanonická max. hĺbka | Historický intra-G3 checkpoint | Dôvod/stena |
|---|---|---:|---:|---|
| K7.1a-K1 | `MŔTVA M-014a` | `20/100` | `32` | fixed-width no-go v G3 |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | `20/100` | `34` | chýba kernel/memory/noise G3 |
| K7.1a-K3.0 | `PREŽILA FORMULAČNÚ BRÁNU` | `20/100` | `36` | mikrofyzika G3 chýba |
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `20/100` | `38` | záporný Onsagerov eigenmode v G3 |
| K7.1a-K3.1-K2 | `OTVORENÁ CEZ PODKOĽAJE` | `20/100` | `42` | žiadna mikrofyzická dcéra neprešla celú G3 |
| K7.1a-K3.1-K2.1 | `PREŽÍVA IBA ROZMEROVÚ EXISTENCIU` | `20/100` | `39` | voľný bath/noise |
| K7.1a-K3.1-K2.2 | `OTVORENÁ CEZ BATH PODKOĽAJE` | `20/100` | `42` | G3 otvorená |
| K7.1a-K3.1-K2.2-K1 | `OTVORENÁ TERMÁLNA VETVA` | `20/100` | `42` | dve realizácie mŕtve; G3 neuzavretá |
| K7.1a-K3.1-K2.2-K1a | `OTVORENÁ CEZ K1a2b` | `20/100` | `42` | gravity-only G3 neuzavretá |
| K7.1a-K3.1-K2.2-K1a1 | `MŔTVA M-014d1` | `20/100` | `40` | thermal-scattering no-go v G3 |
| K7.1a-K3.1-K2.2-K1a2 | `OTVORENÁ CEZ K1a2b` | `20/100` | `42` | spectrum/matrix element neodvodené |
| K7.1a-K3.1-K2.2-K1a2a | `MŔTVA M-014d1b` | `20/100` | `42` | nekoherentný KMS rate chýba o 26–33 rádov |
| K7.1a-K3.1-K2.2-K1a2b | `OTVORENÁ KOHERENTNÁ VETVA` | `20/100` | `5` | nový G3 form factor/coherence budget |
| K7.1a-K3.1-K2.2-K1a2b-K1 | `AKTÍVNA` | `20/100` | `5` | kauzálne konečná koherentná doména; G3 otvorená |
| K7.1a-K3.1-K2.2-K1a2b-K2 | `ČAKÁ` | `20/100` | `5` | superradiant horný limit; G3 otvorená |
| K7.1a-K3.1-K2.2-K1a2b-K3 | `ČAKÁ` | `20/100` | `5` | globálna sieťová koherencia; G3 otvorená |
| K7.1a-K3.1-K2.2-K1a2c | `PRESUNUTÁ DO K2` | `20/100` | `42` | non-KMS spontaneous emission; G3 neuzavretá |
| K7.1a-K3.1-K2.2-K1b | `OTVORENÁ CEZ K1b2/K1b3` | `20/100` | `41` | soft spin-2 G3 neuzavretá |
| K7.1a-K3.1-K2.2-K1b1 | `MŔTVA M-014d2a` | `20/100` | `41` | vedúce soft zosilnenie |
| K7.1a-K3.1-K2.2-K1b2 | `ČAKÁ` | `20/100` | `5` | higher-derivative curvature operátory |
| K7.1a-K3.1-K2.2-K1b3 | `ČAKÁ` | `20/100` | `5` | ďalšie massless spin-2 pole |
| K7.1a-K3.1-K2.2-K1c | `ČAKÁ` | `20/100` | `5` | nový nespin-2 bath |
| K7.1a-K3.1-K2.2-K1d | `ČAKÁ` | `20/100` | `5` | interný tracked bath |
| K7.1a-K3.1-K2.2-K2 | `ČAKÁ + PRIJÍMA K1a2c` | `20/100` | `42` | vákuový/farebný kernel; G3 otvorená |
| K7.1a-K3.1-K2.2-K3 | `ČAKÁ` | `20/100` | `5` | netermálny farebný bath |
| K7.1a-K4 | `ČAKÁ` | `20/100` | `5` | threshold smer; G3 otvorená |

Mŕtve listy, presunuté listy, errata, skripty a historické intra-G3
checkpointy zostávajú zachované. Rodič zomrie až po smrti všetkých dcér.

