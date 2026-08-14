# KMPC-121 — C2 NIV/k=.15 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / CORE_AND_TAIL_REVIEW_CONSUMED`  
**Vstupný stav:** C2 `9/10 PASS`, K4 `LIVE / 60/100`, technický counter `0/10`

## Presná otázka

Prejde frozen C2 atóm `NIV/k=.15/nominal` s accepted supportom `[-1,4]`,
auditom `[-1,6]` a M1 depth `6` všetkými M1, combined-`R_fs`, F0/M3 core,
common, tail, S-C0 a background bránami pri už zmrazených prahoch?

## Zmrazený kontrakt

- znovupoužije sa byteovo nezmenený `c2_single_atom_adapter.py` a
  `c2_fourier_coverage.py`; nový base modul nevzniká;
- ordering-only prerequisite je KMPC-120 raw SHA
  `D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136`
  s candidate
  `PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`;
- C1 NIV prerequisite ostáva KMPC-056 SHA
  `9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332`;
- `k=0.15 Mpc^-1` je Fourierov perturbatívny mód, nie background parameter;
- prahy: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`,
  absolute fallback a background `1e-12`;
- tail/background povrchy `z=1e-4,1e-2` a 13-state order ostávajú frozen.

## Predregistrované rozhodovanie

1. M1 false → `REVIEW_C2_M1_NUMERICAL_BOUNDARY`;
2. iný core false → `REVIEW_C2_CORE_GATE_UNCLOSED`;
3. common false → `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. netail PASS a tail false →
   `REVIEW_C2_NIV_K0p15_SUPPORT_06_08_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NIV_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. Autoritatívna zmena C2 na `10/10` a uzavretie
NIV módu sú dovolené až po internom audite raw. REVIEW ani technická chyba
nemenia skóre a nie sú fyzikálnym STOP A2-K4 bez invariantného dôkazu.

## Scope a exekúcia

- iba NIV/k=.15/nominal; širší support, S-M, ODE/P5.4, G8/G9 a dáta sú
  zakázané;
- compile → help → smoke → presne jeden official atom;
- interný runtime presne `4.8 s`, vonkajší procesný limit `30 s`;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 365:
  `scripts/365_script_KMPC_121_P5_3g7_C2_NIV_k0p15_nominal.py`;
- runner SHA-256:
  `9B0C7903B2CD5B484307B93F745C829310D7B69A0A2E48E9654FCAE5B5237400`;
- source contract `17` položiek, prerequisite contract `6` položiek;
- stabilný harness SHA-256
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_121_P5_3G7_C2_NIV_K0p15_NOMINAL.json`;
- canonical output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 365 spustený cez Python.
Od tohto bodu je immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke/official exit 0; raw SHA `8E5E8107833C9F2858BA180F9DBC3DFA4037566CCC2F7D30AF819B1FC94C0BEE` | `IMMUTABLE_RESULT` |
| 2026-07-19 | audit false iba M3 driver `1.62542e-10`; tail `.01` F0/M3 `1.80841e-6/2.25684e-6` | `REVIEW_CORE_AND_SUPPORT` |
| 2026-07-19 | KMPC-122 uzavrel core; KMPC-126 uzavrel widened support | `REVIEW_CONSUMED / HISTORY_PRESERVED` |
