# KMPC-055 — GLOBAL_C1 NIV support step 2: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NIV support step 2`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT / PF-076`  
**Identita:** `NIV / k=0.05 Mpc^-1 / nominal`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; skóre a triggery `NONE`

## 1. Jediná otázka

KMPC-054 preukázal PASS jadra a common koeficientov, ale jasný FAIL čistého
tailu `3,4`. KMPC-055 preto testuje iba:

> Je NIV support `[-1,4]` postačujúci voči auditu `[-1,6]`, ak oba nové
> solve používajú M1 depth 6?

Nemenia sa rovnice, parameter, variant, prahy ani plochy. NID stav ani jeho
korekcia sa neprenášajú.

## 2. Zmrazené supporty a hĺbka

| Rola | Support | F0/M3 počet | M1 depth |
|---|---:|---:|---:|
| immutable regresia KMPC-054 | `[-1,2]`, `[-1,4]` | `8/52`, `12/78` | `5` |
| nový candidate | `[-1,4]` | `12/78` | `6` |
| nový audit | `[-1,6]` | `16/104` | `6` |

Nový common rozsah je `-1…4`; čistý added tail je iba `5,6`. M1 depth 6
je povinný, lebo musí obsahovať najvyšší auditovaný rád `6`. Predchádzajúci
depth-5 solve sa zopakuje iba na immutable regresiu KMPC-054, nie ako vstup
nového support verdictu.

Prahy zostávajú:

- regression relative/absolute `1e-12 / 1e-14`;
- common relative `1e-8`;
- tail relative `1e-6`;
- absolute fallback norm/tolerance `1e-12 / 1e-12`;
- plochy `z={1e-4,1e-2}`.

## 3. Povinné ochrany

1. immutable KMPC-054 SHA
   `0CF322A7BA5964B78BBF9180B29FA8BBBE43A646ECEB05D444B6250568ECFB1E`;
2. presná depth-5 regresia oboch pôvodných supportov;
3. M1 depth-6 rank, driver, holdout a hard anchor;
4. samostatný NIV combined-`R_fs` leading `j=-1` guard na depth-6 stave;
5. exact shape/rank/core/holdout/forbidden/production brány nových solve;
6. actual S-C0 coefficient guard pre depth-6 `[-1,4]→[-1,6]`;
7. common bridge `-1…4` a cancellation-safe tail `5,6`;
8. registry mutation sa musí obnoviť aj po vyvolanej výnimke.

## 4. Rozhodovací strom

1. technická chyba → `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`;
2. immutable depth-5 regresia FAIL →
   `REVIEW_NIV_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT`;
3. depth-6 M1, combined-`R_fs` alebo core FAIL →
   `REVIEW_NIV_SUPPORT_STEP_2_CORE_GATE_UNCLOSED`;
4. common `-1…4` FAIL →
   `REVIEW_NIV_SUPPORT_STEP_2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
5. tail `5,6` FAIL →
   `REVIEW_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_REMAINDER_UNCLOSED`;
6. všetko PASS →
   `PASS_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_ADEQUATE_CANDIDATE_ONLY`.

Skript neurčuje autoritatívny verdikt. Ďalší support sa nespustí bez nového
rozhodnutia a predregistrácie.

## 5. Plánované artefakty a prevádzka

- base: `scripts/baseScripts/p5_general_synchronous/niv_support_step2.py`;
- runner: `scripts/299_script_KMPC_055_P5_3g7_NIV_support_step2_minus1_4_minus1_6.py`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_055_P5_3G7_NIV_SUPPORT_STEP_2_MINUS1_4_MINUS1_6.json`.

Poradie: compile base, compile runner, `--help`, smoke, output guard, presne
jeden official audit, SHA a nezávislá JSON kontrola. Interný limit je presne
`4.8 s`, vonkajší najviac `10 s` na proces.

## 6. Nonclaims

Bez `[-1,8]`, iných `k`/variantov, S-M, full hierarchy, finite opacity,
ODE/P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 7. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | KMPC-054 core/common PASS a tail `3,4` FAIL autoritatívne vyhodnotený | `AUTHORIZED_SUCCESSOR` |
| 2026-07-18 | supporty, depth-5 regresia, depth-6 nové solve, prahy, plochy a rozhodovací strom zmrazené pred Python procesom | `PREREGISTERED` |
| 2026-07-18 | base SHA `2B41B11E2C27B1FB5462AF0629C0478BBFF6A1343C317D7F6E6C045C0260F680`; runner SHA `48F60E87945A2A9B2BFF37D4601B2C60A039E4D0FC09FD5A6DCD6F7F428AEBED` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base/runner, `--help`, smoke | `PASS / PASS / PASS / PASS` |
| 2026-07-18 | official audit zastal na nesprávnom ownerovi `_all_finite`; iba failure JSON SHA `93906783C433800CB9609A7D3F735F01C504840B323EA981E95BDE79CF7576EC` | `TECHNICAL_FAILURE / NO_PHYSICS_VERDICT / PF-076` |
