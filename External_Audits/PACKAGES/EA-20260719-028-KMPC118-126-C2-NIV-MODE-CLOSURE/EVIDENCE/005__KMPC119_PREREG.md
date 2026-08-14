# KMPC-119 — C2 NIV/k=.005 support `[-1,6]` checkpoint: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / CHECKPOINT_ONLY / CONSUMED_BY_KMPC_120`  
**Prerequisite:** KMPC-118 SHA
`FDB2DF9C0AA1620F2ABF76F1704735DD1848F8C8D861BD959B5F81EC6873B78F`

## Dôvod a presná otázka

KMPC-118 prešiel všetky netail brány, ale tail na `z=.01` prekročil
`1e-6`: F0 worst `delta_f=1.54255e-5`, M3 worst
`delta_f=2.18311e-5`. KMPC-119 smie iba vytvoriť hashovaný verdict-free
checkpoint accepted `[-1,6]`, audit `[-1,8]`, M1 depth `8`, ktorý umožní
samostatný resume audit bez opätovného accepted solve.

## Zmrazený implementačný successor

Pôvodný `c2_configurable_checkpoint.py` síce prijímal konfiguračné hodnoty,
ale jeho `support_exact`, `atom_id` a resume candidate zostali explicitne
NID `[0,7]→[0,9]`. Nesmie sa preto potichu použiť pre NIV.

Vzniká jediný versioned successor
`c2_configurable_checkpoint_v2_support_generic.py`, ktorý:

- povoľuje iba explicitný frozen NIV tuple
  `(NIV, [-1,6], [-1,8], depth 8)`;
- nemení rovnice, solver, rcond, povrchy ani rozhodovacie prahy;
- deleguje numeriku byteovo nezmenenému predchodcovi;
- opravuje iba support guard, atom label a resume PASS/REVIEW label;
- musí po smoke aj official obnoviť všetkých verejných ownerov.

Base successor SHA-256:
`70D8E55DD59FF7C1C23F9BD4C3615063C017D9639D497381AE803C4ED0EDBB0E`.

## Zmrazený checkpoint kontrakt

- `mode=NIV`, `k=.005`, accepted `[-1,6]`, audit `[-1,8]`, M1 depth `8`;
- ordering prerequisite je KMPC-118 candidate
  `REVIEW_C2_NIV_K0p005_SUPPORT_06_08_REQUIRED` s exact SHA vyššie;
- output:
  `RUN_KMPC_119_P5_3G7_C2_NIV_K0p005_SUPPORT_06_ACCEPTED_CHECKPOINT.json`;
- checkpoint status musí byť
  `TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT` a candidate
  `CHECKPOINT_ONLY_NO_PHYSICS_VERDICT`;
- všetky checkpoint preconditions, source hashes, support/depth identity a
  owner restoration musia byť true;
- checkpoint sám nemení C2, K4 ani fyzikálny verdikt.

## Scope a exekúcia

- compile → help → smoke → presne jeden checkpoint atom;
- interný runtime `4.8 s`, vonkajší procesný limit `30 s`;
- žiadny resume audit, tail interpretácia ani score update v tomto kroku;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 363:
  `scripts/363_script_KMPC_119_P5_3g7_C2_NIV_k0p005_support_06_checkpoint.py`;
- runner SHA-256:
  `C19B31EEF351F21E5B69C79A706511D9D0094F1B0396F2075496B93AC412BFFC`;
- source contract `20` položiek, prerequisite contract `6` položiek;
- stabilný harness SHA-256
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- canonical output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 363 ani nový base
successor spustený cez Python. Od tohto bodu sú oba immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke/official exit 0; 9/9 preconditions PASS | `CHECKPOINT_COMPLETE_NO_VERDICT` |
| 2026-07-19 | raw SHA `0E87C19C706D2D8AE9FA1FF2771B46FEEF308327C5B459024175566BAF4ECEE9`; M1 depth 8 PASS | `IMMUTABLE_CHECKPOINT` |
| 2026-07-19 | KMPC-120 exact-hash resume checkpoint spotreboval | `CONSUMED / HISTORY_PRESERVED` |
