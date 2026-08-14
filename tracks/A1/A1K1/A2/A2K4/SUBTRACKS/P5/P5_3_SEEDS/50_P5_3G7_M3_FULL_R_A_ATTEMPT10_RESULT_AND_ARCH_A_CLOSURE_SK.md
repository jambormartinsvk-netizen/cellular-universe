# P5.3g7-M3-FULL/R-A — výsledok pokusu 10 a uzavretie ARCH-A

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-031`  
**Výsledok SHA-256:**
`C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6`  
**K4:** `LIVE / 60/100`  
**P5:** `3.5/6`

## Autoritatívny rozsudok

```text
PASS_SUPPORT_TRUNCATION_J4_SENTINEL_SCOPE
ARCH_A_COMPLETED_AT_10_OF_10
SCORE_EFFECT = NONE
RELEASE_TRIGGER = NONE
```

Token `10_OF_10` je historický názov uzavretia balíka podľa vtedajšej
metodiky. Po neskoršom používateľskom spresnení sa aktívny cap číta ako počet
po sebe idúcich technických zlyhaní: KMPC-031 bol vecne úspešný, preto
`historical_packages_total=10` a `consecutive_technical_failures=0/10`.
Výsledok ani história sa tým nemenia.

J4 je numericky dostatočný minimálny support iba pre conditional
`Phi1 M3-TCA0 AD/k=0.05/nominal` sentinel na `z=1e-4` a `z=1e-2`.

## Dôkaz

| bridge | z | max relative | max absolute fallback | stav |
|---|---:|---:|---:|---|
| J4→J6 added powers 5–6 | `1e-4` | `4.6644839165e-14` | `4.7511156284e-38` | PASS |
| J4→J6 added powers 5–6 | `1e-2` | `4.6685727393e-8` | `4.8456467923e-28` | PASS |
| J6→J8 added powers 7–8 | `1e-4` | `5.1651467416e-24` | `3.2840920655e-46` | PASS |
| J6→J8 added powers 7–8 | `1e-2` | `5.1791626207e-14` | `3.3047508260e-32` | PASS |

Všetkých 25 kontrol je true. Decimal reconstruction je presne nula vo
všetkých 52 riadkoch; no-solve, F0/M3 bridge, exact state/power, forbidden a
`U_c` regularity guardy prešli. J8 tail je na oboch plochách menší než J6.

## Raw FAIL sa zachováva

KMPC-030 raw independent-solve tail `1.2308e-5` a `3.3632e-6` ostáva FAIL.
Audit dokázal, že táto veličina mieša drift spoločných, formálne nulových
koeficientov s novými powers. Preto sa používa iba ako
`MIXED_COMMON_DRIFT_PLUS_ADDED_TAIL_DIAGNOSTIC`; nejde o čistý truncation
gate a nesmie sa spätne premenovať na PASS.

## Čo výsledok nedokazuje

- nie je to celý P5.3/P5.3g7 ani K4 PASS;
- nie sú overené CDI, BI, NID, NIV ani iné `k` a varianty;
- nie je overená S1 para, finite opacity, Phi2 recoil ani boundary limity;
- nie je to P5.4 ODE, G8 hierarchy, CMB alebo S8 test.

## Ďalší fyzikálny krok

Nevznikne technický pokus 11 tej istej ARCH-A. Najprv sa vytvorí S1 branch
contract a support-transfer passport. Potom sa fail-fast overia štyri chýbajúce
módy pri `k=.05`, nominal, s vlastným leading power a vlastným J/J+2 tailom.
Až po ich PASS má zmysel `k=.005,.15` a null variant coverage.

## Release

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```
