# KMPC-048 — GLOBAL_C1 NID support step 2: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID_SUPPORT_STEP_2`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_PASS / AUTHORITATIVE_REVIEW_ORDER7_CORE_BOUNDARY`  
**Identita:** `NID / k=0.05 Mpc^-1 / nominal`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; skóre a triggery `NONE`

## 1. Otázka a immutable prerequisite

KMPC-047 ukázal core/common/combined-`R_fs` PASS, ale tail `4,5` FAIL pre
candidate `[0,3]`. KMPC-048 preto testuje iba:

> Je NID candidate support `[0,5]` dostatočný voči audit supportu `[0,7]`?

Immutable prerequisite:
`RUN_KMPC_047_P5_3G7_NID_C1_PRIMARY_EXTENDED_COVERAGE.json`, SHA-256
`EED63396DB99C0818306C581413572BE647630CFD0433A8F05A1DCE704DC696A`.

## 2. Support, regresia a metriky

| Rola | Support | F0 | M3 |
|---|---:|---:|---:|
| regression A | `[0,3]` | 8 | 52 |
| regression B / candidate | `[0,5]` | 12 | 78 |
| audit | `[0,7]` | 16 | 104 |

- regresia `[0,3]` a `[0,5]` voči KMPC-047: relative `1e-12`, absolute
  `1e-14`;
- common bridge `[0,5]↔[0,7]`: powers `0…5`, relative `1e-8`, absolute
  fallback `1e-12`;
- tail baseline: powers `0…5`;
- jediný autoritatívny tail: `sum(abs(c_j) z^j)` pre `j=6,7`;
- tail relative `1e-6`, absolute norm/tolerance `1e-12/1e-12`;
- plochy presne `z={1e-4,1e-2}`;
- leading `j=0`; signed tail iba diagnostický;
- všetky tri supporty musia prejsť rank/driver/holdout/forbidden/
  production/regularity/finite core guardy;
- combined-`R_fs` M1 kompenzácia a actual S-C0 coefficient guard sa
  zopakujú bez zmeny.

Registry adapter smie dočasne zmeniť iba očakávané shape counts počas
solve a musí ich obnoviť vo `finally`; smoke vyvolá deterministickú výnimku
po mutácii a overí úplnú obnovu.

## 3. Rozhodovací strom

1. parser/hash/runtime/JSON/publish chyba →
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`;
2. immutable `[0,3]/[0,5]` regresia FAIL →
   `REVIEW_NID_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT`;
3. core, combined-`R_fs` alebo S-C0 FAIL →
   `REVIEW_NID_SUPPORT_STEP_2_CORE_GATE_UNCLOSED`;
4. common powers `0…5` FAIL →
   `REVIEW_NID_SUPPORT_STEP_2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
5. tail `6,7` FAIL →
   `REVIEW_NID_SUPPORT_STEP_2_SUPPORT_05_REMAINDER_UNCLOSED`;
6. všetko PASS →
   `PASS_NID_SUPPORT_STEP_2_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Skript nevydáva autoritatívny verdikt. Ak tail zlyhá, `[0,9]` sa nespustí
automaticky; najprv sa predregistruje order-7 provenance/numerical boundary
podľa príčiny. Prahy ani plochy sa po výsledku nemenia.

## 4. Prevádzka a artefakty

Povinné poradie: compile base, compile runner, `--help`, `--smoke`, output
guard, presne jeden `--audit`, hash a nezávislé čítanie JSON. Vnútorný limit
je `4.8 s`, vonkajší najviac `10 s` na proces. Canonical/failure/temp sú
immutable.

- base: `scripts/baseScripts/p5_general_synchronous/nid_support_step2.py`;
- runner: `scripts/292_script_KMPC_048_P5_3g7_NID_support_step2_05_07.py`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_048_P5_3G7_NID_SUPPORT_STEP_2_05_07.json`.

## 5. Nonclaims

Bez `[0,9]`, NIV, iných `k`/variantov, S-M, full hierarchy, ODE/P5.4,
G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 6. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | KMPC-047 udelil `REVIEW_SUPPORT_EXTENSION_REQUIRED`; jeho balík EA-006 prešiel `138/138` | `PREREQUISITE_CLOSED` |
| 2026-07-18 | `[0,5]→[0,7]`, regresia, prahy, plochy, combined-`R_fs` a rozhodovací strom zmrazené pred Python procesom | `PREREGISTERED` |
| 2026-07-18 | base SHA `7AFA5AD9022FA3EB8BDFB5F77D573939D60B2312A0FA29493D6505695958EE5B`; runner SHA `9FA55116BB7CFD911CCB2D8D741280C3A5AF99C9741BA2FC5AA61A5DC2068002` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base, compile runner, `--help`, smoke a output guard | `PASS / PASS / PASS / PASS / ABSENT` |
| 2026-07-18 | jediný official audit, external exit `0`, internal `3.531 s`; JSON SHA `B4F320F5D850DCF78FD9EC2A5BDDEBDA87D590DA2988CF505FA7D5B25B49BF32` | `TECHNICAL_PASS` |
| 2026-07-18 | regresia/common/tail/combined-`R_fs` PASS; support `[0,7]` M3 driver a `00/0i` holdout FAIL | `REVIEW_NID_SUPPORT_STEP_2_CORE_GATE_UNCLOSED` |
