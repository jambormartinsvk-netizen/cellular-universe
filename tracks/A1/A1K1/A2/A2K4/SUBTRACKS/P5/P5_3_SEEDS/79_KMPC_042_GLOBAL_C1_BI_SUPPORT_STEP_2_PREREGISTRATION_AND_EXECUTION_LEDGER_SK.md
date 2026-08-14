# KMPC-042 — GLOBAL_C1 BI support step 2: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI_SUPPORT_STEP_2`  
**Stav:** `AUTHORIZED_NOT_EXECUTED`  
**Identita:** `BI / k=0.05 Mpc^-1 / nominal`  
**Skóre a triggery:** `NONE`

## 1. Immutable vstup a účel

KMPC-041 autoritatívne ukázal, že BI primary `[0,1]` nestačí, pričom core,
holdouty, S-C0 a common `0,1` prešli. KMPC-042 nesmie tento výpočet
preinterpretovať ani meniť jeho prahy. Jeho jediná otázka je:

> Je accepted candidate `[0,3]` dostatočný voči audit supportu `[0,5]`?

Immutable prerequisite:
`RUN_KMPC_041_P5_3G7_BI_C1_PRIMARY_EXTENDED_COVERAGE.json`, SHA-256
`8BB006EF6606476D85168FBDCD913249E9EDE024C1017473376A33CF4C7AE183`.

## 2. Presný kontrakt

| Rola | Support | F0 počet | M3 počet |
|---|---:|---:|---:|
| immutable regresia | `[0,1]` | 4 | 26 |
| immutable regresia / candidate | `[0,3]` | 8 | 52 |
| audit | `[0,5]` | 12 | 78 |

Pred interpretáciou sa musia `[0,1]` a `[0,3]` koeficienty reprodukovať
voči KMPC-041 s relative `1e-12`, absolute `1e-14`. M1 zostáva order 5;
order 7 sa nepoužije.

Ďalšie brány:

- frozen a nezávislý R-A contract, B1 a TCA0;
- F0/M3 rank, driver, holdout, leading/forbidden/production/regularity a
  finite pre všetky tri supporty;
- actual S-C0 guard medzi candidate `[0,3]` a auditom `[0,5]`;
- common bridge iba powers `0…3`, osobitne F0 a M3, relative `1e-8` a
  absolute fallback `1e-12`;
- autoritatívny tail iba powers `4,5` voči baseline `1…3` na
  `z={1e-4,1e-2}`, relative `1e-6`, absolute fallback norm/tol `1e-12`;
- tail je `sum(abs(c_j)z^j)`; signed súčet je iba diagnostický.

## 3. Rozhodovací strom

1. Technická chyba → `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`.
2. Immutable regresia FAIL →
   `REVIEW_BI_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT`.
3. Core/S-C0 FAIL → `REVIEW_BI_SUPPORT_STEP_2_CORE_GATE_UNCLOSED`.
4. Common `0…3` FAIL →
   `REVIEW_BI_SUPPORT_STEP_2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`.
5. Tail `4,5` FAIL →
   `REVIEW_BI_SUPPORT_STEP_2_SUPPORT_03_REMAINDER_UNCLOSED`.
6. Všetko PASS →
   `PASS_BI_SUPPORT_STEP_2_SUPPORT_03_ADEQUATE_CANDIDATE_ONLY`.

Tail FAIL dokazuje iba nedostatočnosť `[0,3]`. Neautorizuje `[0,7]`:
nasleduje najprv samostatná BI M1 order-7 provenance/numerical boundary
brána. Tail PASS ukončí BI support ladder na `[0,3]` a `[0,7]` sa nepočíta.

## 4. Prevádzkový kontrakt a nonclaims

Poradie `compile → --help → --smoke → jeden --audit`, interný limit presne
`4.8 s`, externý najviac `10 s`, immutable atomic/exclusive output.
Zakázané sú post-hoc prahy, rerun, `[0,7]`, NID/NIV, iné `k`/varianty,
S-M, full hierarchy, ODE, P5.4, G8/G9 a release interpretácia.

## 5. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ prikázal pokračovať | `AUTHORIZED` |
| 2026-07-18 | support, regresia, metriky, prahy a rozhodovací strom zmrazené | `PREREGISTERED` |
| 2026-07-18 | `py_compile` nového base a runnera | `PASS` |
| 2026-07-18 | runner `--help` | `PASS` |
| 2026-07-18 | smoke: support/prerequisite/registry/JSON/write guardy | `PASS` |
| 2026-07-18 | jediný bounded audit, interný limit `4.8 s` | `TECHNICAL_COMPLETE` |
| 2026-07-18 | canonical JSON zapísaný exkluzívne; failure/tmp nevznikli | `PASS` |
| 2026-07-18 | nezávislý JSON, cancellation a BI/CDI routing audit | dokument 80 |
