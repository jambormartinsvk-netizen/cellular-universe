# A2-K7.0 — reprodukovateľný numerický výstup prvej brány

**Dátum:** 2026-07-13  
**Generátor:** `scripts/50_script_A2_K7_0_mediator_ledger_collision_gate.py`  
**Stav behu:** `PASS`  
**Rozsah:** presný backgroundový ledger a znamienko lokálneho collision
operátora; nie úplné kozmologické perturbácie

Predregistrovaný grid bol
`epsilon/delta={0.01,0.05,0.10,0.25,0.50,0.90}`. Mediátor bol v prvej
realizácii tlakovo spriemerovaný masívny kanonický skalár s `w_M=0`.

| `epsilon/delta` | `epsilon` | `Omega_M0` | `w_phi` | `alpha1(rec)` | `alpha1(0)` | `alpha2(0)` | `log10 D_Mphi` | `log10 D_cM` | `tau_M` [Gyr] | stav |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| 0.01 | 0.00022970 | 0.00014889 | -0.97725448 | 2.958761 | 655.806776 | 0.323115 | -274.047361 | -0.040953 | 0.022560 | PASS |
| 0.05 | 0.00114850 | 0.00074446 | -0.97815341 | 2.936619 | 133.386227 | 0.323115 | -61.883955 | -0.040953 | 0.112802 | PASS |
| 0.10 | 0.00229700 | 0.00148893 | -0.97927940 | 2.933851 | 68.083659 | 0.323115 | -35.363529 | -0.040953 | 0.225605 | PASS |
| 0.25 | 0.00574250 | 0.00372231 | -0.98267300 | 2.932191 | 28.902117 | 0.323115 | -19.451274 | -0.040953 | 0.564012 | PASS |
| 0.50 | 0.01148500 | 0.00744463 | -0.98838156 | 2.931637 | 15.841604 | 0.323115 | -14.147189 | -0.040953 | 1.128023 | PASS |
| 0.90 | 0.02067300 | 0.01340033 | -0.99765451 | 2.931391 | 10.036931 | 0.323115 | -11.789818 | -0.040953 | 2.030441 | PASS |

## Rezíduá a konvergencia

```text
maximálne absolútne ledgerové rezíduum       = 2.220e-16
max relatívny rozdiel alpha1(0), kroky
5e-4 vs 2.5e-4                              = 0.000e+00
collision eigenhodnoty                       < 0 na celom intervale
```

`D_Mphi` a `D_cM` sú collision-only tlmiace faktory od rekombinácie po
dnešok. Hodnota `log10 D_cM=-0.040953` znamená
`D_cM=0.9100`: priame relaxovanie rýchlosti celého existujúceho popola je
len približne deväťpercentné. Nejde ešte o výsledný rast hustotných porúch.

## Strojový rozsudok

```text
presný A1 ledger                       PASS
kladná entalpia phi aj M               PASS
kladné donorové zdroje                 PASS
interaction-only anti-damping          NEZISTENÝ
úplná gauge-invariantná stabilita      NEOVERENÁ
mikrofyzické odvodenie Q1,Q2           NEOVERENÉ
A2-K7.0                                PREŽÍVA 30/100
```

