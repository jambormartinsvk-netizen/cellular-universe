# KMPC-116 — C2 NID/k=.15 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / CORE_NUMERICAL_REVIEW_CONSUMED_BY_KMPC_117`  
**Vstupný stav:** C2 `7/10 PASS`, K4 `LIVE / 60/100`, technický counter `0/10`

## Presná otázka

Prejde frozen C2 atóm `NID/k=.15/nominal` s accepted supportom `[0,5]`,
auditom `[0,7]` a M1 depth `7` všetkými M1, combined-`R_fs`, F0/M3 core,
common, tail, S-C0 a background bránami pri už zmrazených prahoch?

## Zmrazený kontrakt

- znovupoužije sa byteovo nezmenený `c2_single_atom_adapter.py` a
  `c2_fourier_coverage.py`; nový base modul nevzniká;
- ordering-only prerequisite je KMPC-115 raw SHA
  `7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851`
  s candidate
  `PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`;
- C1 NID prerequisite ostáva KMPC-053 SHA
  `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`;
- `k=0.15 Mpc^-1` je Fourierov perturbatívny mód, nie background parameter;
- prahy: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`,
  absolute fallback a background `1e-12`;
- tail povrchy `z=1e-4,1e-2`, background povrchy ostávajú frozen.

## Predregistrované rozhodovanie

1. M1 false → `REVIEW_C2_M1_NUMERICAL_BOUNDARY`;
2. iný core false → `REVIEW_C2_CORE_GATE_UNCLOSED`;
3. common false → `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. netail PASS a tail false →
   `REVIEW_C2_NID_K0p15_SUPPORT_07_09_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. Autoritatívna zmena C2 na `8/10` je dovolená
až po internom audite raw. REVIEW ani technická chyba nemenia skóre a nie sú
fyzikálnym STOP A2-K4 bez invariantného dôkazu.

## Scope a exekúcia

- iba NID/k=.15/nominal; iné atómy, support `[0,9]`, S-M, ODE, P5.4,
  G8/G9 a dáta sú zakázané;
- compile → help → smoke → presne jeden official atom;
- interný runtime presne `4.8 s`, vonkajší procesný limit `30 s`;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 360:
  `scripts/360_script_KMPC_116_P5_3g7_C2_NID_k0p15_nominal.py`;
- runner SHA:
  `D386FE76F9239771F33338D3E40ADA2E9BFC5C8568E82B7E0E8FF2C04A4F31A8`;
- source contract `17` položiek, prerequisite contract `6` položiek;
- stabilný harness SHA
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_116_P5_3G7_C2_NID_K0p15_NOMINAL.json`;
- canonical output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 360 spustený cez Python.
Od tohto bodu je runner 360 immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke/official exit 0; raw SHA `0965E3D1F7726CC851B3D1B6043468169ADEBED44096B010565F768DBD8E25AB` | `IMMUTABLE_RESULT` |
| 2026-07-19 | M1/accepted/common/tail/background/holdout PASS; audit false iba `M3_driver`, worst `gamma_Euler[7]=4.18656e-10` | `REVIEW_CORE_NUMERICAL_BOUNDARY` |
| 2026-07-19 | rovnakomatricový nástupca KMPC-117 predregistrovaný bez zmeny prahu | `REVIEW_CONSUMED / HISTORY_PRESERVED` |
