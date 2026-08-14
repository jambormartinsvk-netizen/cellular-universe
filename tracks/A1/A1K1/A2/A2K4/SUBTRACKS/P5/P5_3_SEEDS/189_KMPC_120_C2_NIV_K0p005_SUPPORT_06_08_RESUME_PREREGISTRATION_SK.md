# KMPC-120 — C2 NIV/k=.005 `[-1,6]→[-1,8]` resume: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / PASS_CANDIDATE`  
**Ordering prerequisite:** KMPC-118 SHA
`FDB2DF9C0AA1620F2ABF76F1704735DD1848F8C8D861BD959B5F81EC6873B78F`  
**Checkpoint prerequisite:** KMPC-119 SHA
`0E87C19C706D2D8AE9FA1FF2771B46FEEF308327C5B459024175566BAF4ECEE9`

## Presná otázka

Obnoví KMPC-120 immutable NIV checkpoint accepted `[-1,6]`, zachová presné
13-state poradie a dopočíta audit `[-1,8]` tak, aby M1, driver,
independent `00/0i` holdout, common, tail, S-C0 a background prešli pri
nezmenených prahoch?

## Zmrazený kontrakt

- rovnaký versioned successor SHA
  `70D8E55DD59FF7C1C23F9BD4C3615063C017D9639D497381AE803C4ED0EDBB0E`;
- `mode=NIV`, `k=.005`, accepted `[-1,6]`, audit `[-1,8]`, M1 depth `8`;
- KMPC-119 checkpoint musí mať exact hash, verdict-free status, source hash
  mapu a frozen ladder identitu;
- accepted stav sa obnoví z checkpointu; audit solve nesmie meniť accepted
  coefficients ani pridať independent holdout do driver fitu;
- prahy ostávajú driver `1e-10`, holdout `1e-9`, common `1e-8`, tail
  `1e-6`, absolute fallback/background `1e-12`;
- tail/background povrchy a equation builder ostávajú byteovo nezmenené.

## Predregistrované rozhodovanie

1. checkpoint/source/order/owner guard false → technický incident bez
   fyzikálneho verdiktu;
2. M1 alebo core false → príslušný `REVIEW_C2_*_BOUNDARY` podľa raw false
   množiny;
3. common false → `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. netail PASS a tail false →
   `REVIEW_C2_NIV_K0p005_SUPPORT_08_10_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. Autoritatívny C2 `8/10→9/10` povoľuje až
interný audit raw. K4 ostáva `60/100` do uzavretia celej fyzikálnej brány.

## Scope a exekúcia

- compile → help → smoke → presne jeden resume atom;
- interný runtime `4.8 s`, vonkajší procesný limit `30 s`;
- NIV/.15, S-M, ODE/P5.4, G8/G9 a dáta sú mimo scope;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 364:
  `scripts/364_script_KMPC_120_P5_3g7_C2_NIV_k0p005_support_06_08_checkpoint_resume.py`;
- runner SHA-256:
  `9CDA95D23A5A07EF2ACE65E74A9D1DED45BFC9B729E7CC3D03335BBD7FBBE7C8`;
- source contract `20` položiek, prerequisite contract `7` položiek;
- stabilný harness SHA-256
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_120_P5_3G7_C2_NIV_K0p005_SUPPORT_06_08_CHECKPOINT_RESUME.json`;
- output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 364 spustený cez Python.
Od tohto bodu je immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke/official exit 0; checkpoint a 13-state order PASS | `PREFLIGHT_PASS` |
| 2026-07-19 | raw SHA `D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136`; všetky brány true | `IMMUTABLE / PASS_CANDIDATE` |
| 2026-07-19 | interný audit dokument 190 prijal scoped NIV/k=.005 PASS | `AUTHORITATIVE_SCOPED_PASS` |
