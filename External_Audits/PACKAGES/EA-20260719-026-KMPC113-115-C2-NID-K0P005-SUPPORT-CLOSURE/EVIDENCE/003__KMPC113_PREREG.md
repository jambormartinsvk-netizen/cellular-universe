# KMPC-113 — C2 NID/k=.005 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / TAIL_ONLY_REVIEW_CONSUMED_BY_KMPC_114_115`  
**Vstupný stav:** C2 `6/10 PASS`, K4 `LIVE / 60/100`, technický counter `0/10`

## Presná otázka

Prejde frozen C2 atóm `NID/k=.005/nominal` s accepted supportom `[0,5]`,
auditom `[0,7]` a M1 depth `7` všetkými M1, combined-`R_fs`, F0/M3 core,
common, tail, S-C0 a background bránami pri už zmrazených prahoch?

## Zmrazený kontrakt

- znovupoužije sa byteovo nezmenený `c2_single_atom_adapter.py` a
  `c2_fourier_coverage.py`; nový base modul nevzniká;
- ordering-only prerequisite je KMPC-112 raw SHA
  `FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1`
  s candidate
  `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY`;
- C1 NID prerequisite je KMPC-053 SHA
  `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`;
- `k` je Fourierov perturbatívny mód, nie background parameter;
- prahy: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`,
  absolute fallback a background `1e-12`;
- povrchy tail/background ostávajú `z=1e-4,1e-2`.

## Predregistrované rozhodovanie

1. M1 false → `REVIEW_C2_M1_NUMERICAL_BOUNDARY`;
2. iný core false → `REVIEW_C2_CORE_GATE_UNCLOSED`;
3. common false → `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. netail PASS a tail false →
   `REVIEW_C2_NID_K0p005_SUPPORT_07_09_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NID_K0p005_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. Autoritatívna zmena C2 na `7/10` je dovolená
až po internom audite raw. REVIEW ani technická chyba nemenia skóre a nie sú
fyzikálnym STOP A2-K4 bez príslušného invariantného dôkazu.

## Scope a exekúcia

- iba NID/k=.005/nominal; iné atómy, support `[0,9]`, S-M, ODE, P5.4,
  G8/G9 a dáta sú zakázané;
- compile → help → smoke → presne jeden official atom;
- interný runtime presne `4.8 s`, vonkajší procesný limit `30 s`;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 357:
  `scripts/357_script_KMPC_113_P5_3g7_C2_NID_k0p005_nominal.py`;
- runner SHA:
  `5B214095903EA0ABC1FFB8559EF191D7A1A7E10FE9B489A9F02C7815F6E19ECB`;
- source contract `17` položiek, prerequisite contract `6` položiek;
- stabilný harness SHA
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_113_P5_3G7_C2_NID_K0p005_NOMINAL.json`.

Pred vytvorením tejto predregistrácie nebol runner 357 spustený cez Python.
Od tohto bodu je runner 357 immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke PASS; official exit 0 za `3.406 s` | `IMMUTABLE_RESULT` |
| 2026-07-19 | M1/core/common/background PASS; tail `.01` F0 `1.1184e-5`, M3 `2.4037e-5` | `REVIEW_SUPPORT_07_09_REQUIRED` |
| 2026-07-19 | raw SHA `DD5B3075AB7581C4DC590CFE668952217B58C969B07FEC1CCDE5FA02C7B3B533`; následníci 114/115 uzavreli `[0,7]` | `REVIEW_CONSUMED / HISTORY_PRESERVED` |
