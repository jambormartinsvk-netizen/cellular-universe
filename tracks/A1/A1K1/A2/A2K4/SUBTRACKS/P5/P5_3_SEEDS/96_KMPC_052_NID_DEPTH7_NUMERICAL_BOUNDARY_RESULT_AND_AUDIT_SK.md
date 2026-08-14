# KMPC-052 — výsledok NID depth-7 numerical boundary

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny rozsudok:** `PASS_NID_DEPTH7_PROVENANCE_NUMERICAL_BOUNDARY_CLOSED_SAME_MATRIX_ONLY`  
**K4/P5:** `LIVE 60/100 / 3.5/6`; score a triggery `NONE`

Raw `RUN_KMPC_052_P5_3G7_NID_DEPTH7_NUMERICAL_BOUNDARY.json`, SHA
`FDEE962EED16EDF459D7D8504833AB1206AEF1BFC8178A356A88A121CF196C4C`.

## Rozhodujúce výsledky

| Vetva | Výsledok |
|---|---|
| V0 parity | presná KMPC-051 depth-7 matica; jediný fail `fuel_Euler[7] = 1.3994e-10`; holdout PASS |
| V1 | normwise backward error `1.2199e-16` |
| V2 | jedna correction `3.3227e-16`, rank `104`; driver max `1.6157e-16`, holdout max `2.6216e-11`; PASS |
| V3 80 dps | QR residual `4.1078e-84`; driver max `1.2467e-16`, holdout max `2.6215e-11`; PASS |
| V3→float64 | driver max `1.1523e-16`, holdout max `2.6215e-11`; PASS |
| common `0…5` | V2 aj V3 max rozdiel `3.3227e-16 < 1e-8` |

V2 correction aj V3 rozdiel od V0 sú viac než rád pod capom `1e-14`.
Householder owner sa obnovil; operation counts sú presne `1/1/1/1`, native
rebuild `0`.

## Interpretácia

Na rovnakej depth-7 M1 + NID M3 `[0,7]` matici dva nezávislé numerické
postupy uzavreli všetkých 104 driver a 16 holdout riadkov bez zmeny rovníc,
prahov alebo common koeficientov. Posledný KMPC-051 driver fail je preto v
same-matrix scope uzavretý ako float64 solver/rounding floor.

Tento PASS neznamená support adequacy. Samostatný KMPC-053 musí ešte
znovu vyhodnotiť candidate `[0,5]` proti refined audit `[0,7]`, common
`0…5`, cancellation-safe tail `6,7`, S-C0, combined-`R_fs` a immutable
regresiu. `[0,9]` zostáva zakázaný.
