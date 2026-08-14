# KMPC-118 — C2 NIV/k=.005 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / TAIL_ONLY_REVIEW_CONSUMED_BY_KMPC_119_120`  
**Vstupný stav:** C2 `8/10 PASS`, K4 `LIVE / 60/100`, technický counter `0/10`

## Presná otázka

Prejde frozen C2 atóm `NIV/k=.005/nominal` s accepted supportom `[-1,4]`,
auditom `[-1,6]` a M1 depth `6` všetkými M1, combined-`R_fs`, F0/M3 core,
common, tail, S-C0 a background bránami pri už zmrazených prahoch?

## Zmrazený kontrakt

- znovupoužije sa byteovo nezmenený `c2_single_atom_adapter.py` a
  `c2_fourier_coverage.py`; nový base modul nevzniká;
- ordering-only prerequisite je KMPC-117 raw SHA
  `F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4`
  s candidate
  `PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`;
- C1 NIV prerequisite ostáva KMPC-056 SHA
  `9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332`;
- `k=0.005 Mpc^-1` je Fourierov perturbatívny mód, nie background parameter;
- prahy: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`,
  absolute fallback a background `1e-12`;
- tail/background povrchy `z=1e-4,1e-2` a 13-state order ostávajú frozen.

## Predregistrované rozhodovanie

1. M1 false → `REVIEW_C2_M1_NUMERICAL_BOUNDARY`;
2. iný core false → `REVIEW_C2_CORE_GATE_UNCLOSED`;
3. common false → `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. netail PASS a tail false →
   `REVIEW_C2_NIV_K0p005_SUPPORT_06_08_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NIV_K0p005_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. Autoritatívna zmena C2 na `9/10` je dovolená
až po internom audite raw. REVIEW ani technická chyba nemenia skóre a nie sú
fyzikálnym STOP A2-K4 bez invariantného dôkazu.

## Scope a exekúcia

- iba NIV/k=.005/nominal; NIV/.15, širší support, S-M, ODE/P5.4, G8/G9 a
  dáta sú zakázané;
- compile → help → smoke → presne jeden official atom;
- interný runtime presne `4.8 s`, vonkajší procesný limit `30 s`;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 362:
  `scripts/362_script_KMPC_118_P5_3g7_C2_NIV_k0p005_nominal.py`;
- runner SHA-256:
  `1A6F758BCC6B21EA75DED86030D7F2A8FE3BAB494A027912428E215A3C4FFD4D`;
- source contract `17` položiek, prerequisite contract `6` položiek;
- stabilný harness SHA-256
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_118_P5_3G7_C2_NIV_K0p005_NOMINAL.json`;
- canonical output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 362 spustený cez Python.
Od tohto bodu je runner 362 immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke/official exit 0; raw SHA `FDB2DF9C0AA1620F2ABF76F1704735DD1848F8C8D861BD959B5F81EC6873B78F` | `IMMUTABLE_RESULT` |
| 2026-07-19 | všetky netail brány PASS; `.01` tail F0 `1.54255e-5`, M3 `2.18311e-5` | `REVIEW_SUPPORT_06_08_REQUIRED` |
| 2026-07-19 | checkpoint/resume KMPC-119/120 uzavrel support bez zmeny prahu | `REVIEW_CONSUMED / HISTORY_PRESERVED` |
