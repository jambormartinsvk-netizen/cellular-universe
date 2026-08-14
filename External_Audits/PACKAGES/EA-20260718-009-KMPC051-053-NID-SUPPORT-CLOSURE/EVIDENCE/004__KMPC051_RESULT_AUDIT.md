# KMPC-051 — výsledok NID M1 depth 5→7

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny stav:** `REVIEW_NID_M1_DEPTH7_CONSTRAINT_CLOSED_NUMERICAL_DRIVER_BOUNDARY`  
**K4/P5:** `LIVE 60/100 / 3.5/6`; score a triggery `NONE`

## Dôkaz

Raw `RUN_KMPC_051_P5_3G7_NID_M1_DEPTH_5_7.json`, SHA
`AF088030BA709F08D40D825B9477C9A84BA330705CDDFB1C12C52B0DD3FC1E5E`.
Baseline depth 5 presne reprodukoval všetky štyri KMPC-050 matrix/constant
hashe. Depth-7 M1 solve mal reduced rank `98/98`, full vector `99`, nulový
hard-anchor rozdiel a full-depth driver/holdout scaled residualy
`9.80e-15 / 5.72e-15`.

Spoločné koeficienty ostali stabilné:

| Vrstva | max relatívny rozdiel oproti depth 5 |
|---|---:|
| M1 `-1…5` | `2.60e-15` |
| F0 `0…5` | `7.32e-17` |
| M3 `0…5` | `3.51e-16` |

Všetky sú hlboko pod zmrazeným `1e-8`.

## Rozhodujúca zmena

M1 depth 7 zmenil najmä affine konštanty, nie operátor:

- driver matrix max rozdiel `1.42e-14`, driver constant `8.69e-5`;
- holdout matrix max rozdiel `8.88e-16`, holdout constant `3.59e-5`.

Pôvodný veľký KMPC-050 holdout `Einstein_00[7] ≈ 0.23` po konzistentnej
M1 depth-7 zostave zmizol. Oba Einstein holdouty prešli; maximum bolo iba
`3.60e-11` na `Einstein_0i[7]`, teda pod `1e-8`.

Ostal jeden tesný driver boundary: `fuel_Euler[7] = 1.3994e-10` proti
prahu `1e-10`. Jediná same-matrix korekcia `3.3227e-16` potom uzavrela
všetky driver aj holdout riadky.

## Interpretácia kandidáta a autoritatívneho stavu

Machine kandidát podľa vopred zmrazeného stromu je
`REVIEW_NID_M1_DEPTH_MISMATCH_REJECTED_CONSTRAINT_AUDIT_REQUIRED`, pretože
vyžadoval PASS už pred korekciou. Toto sa zachováva a spätne nemení.

Výsledné dáta však **zamietajú iba plný nekorigovaný PASS**, nie samotnú
depth-mismatch príčinu veľkého constraint problému. M1 depth 7 odstránil
holdout chybu o približne desať rádov bez common regresie a zostávajúci
driver fail je na `1e-10` hranici s korekciou `3e-16`. Preto hlavný audit
presnejšie drží REVIEW s uzavretým constraintom a otvorenou numerickou
driver hranicou.

## Ďalší predregistrovaný krok

KMPC-052 má na presne tej istej depth-7 M1 + M3 `[0,7]` matici vykonať
numerical-boundary closure podľa už auditovanej BI metodiky:

- V0 reprodukcia KMPC-051 depth-7 matice, ranku a presného otvoreného
  `fuel_Euler[7]` patternu;
- V1 backward/residual invarianty;
- presne jedna bounded float64 refinement s capom `1e-14`;
- presne jeden 80-dps same-matrix QR solve s exact float transferom;
- driver, holdout, common `0…5`, hard anchor a spätná float64 projekcia;
- bez native rebuild, zmeny prahov, `[0,9]` alebo NIV.

Ak V2 aj V3 prejdú, NID depth-7 numerical boundary sa môže autoritatívne
uzavrieť a až potom sa rozhodne support adequacy. Ak nie, nasleduje
Bianchi/rovnicový audit.
