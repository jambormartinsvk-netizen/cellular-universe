# KMPC-123 — C2 NIV/k=.15 support `[-1,6]` checkpoint: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / CHECKPOINT_INCOMPLETE_NO_VERDICT`  
**Prerequisite:** KMPC-122 SHA
`BAC68E1D85802852EEBF4B1AC2E277EC15FD32264E166F673D486FD747869419`

## Dôvod a presná otázka

KMPC-122 uzavrel jedinú KMPC-121 core hranicu na presne tej istej matici:
M3 driver `1.62542e-10→1.51686e-16`, holdout `4.25308e-12 <1e-9`.
Ostal iba tail na `z=.01`: F0 `1.80841e-6`, M3 `2.25323e-6`.

KMPC-123 smie iba vytvoriť hashovaný verdict-free checkpoint accepted
`[-1,6]`, audit `[-1,8]`, M1 depth `8`, ktorý umožní samostatný resume
audit bez opätovného accepted solve.

## Zmrazený checkpoint kontrakt

- znovupoužije sa immutable support-generic successor SHA
  `70D8E55DD59FF7C1C23F9BD4C3615063C017D9639D497381AE803C4ED0EDBB0E`;
- `mode=NIV`, `k=.15`, accepted `[-1,6]`, audit `[-1,8]`, M1 depth `8`;
- ordering prerequisite je KMPC-122 candidate
  `REVIEW_C2_NIV_K0p15_SUPPORT_06_08_REQUIRED` s exact SHA vyššie;
- output:
  `RUN_KMPC_123_P5_3G7_C2_NIV_K0p15_SUPPORT_06_ACCEPTED_CHECKPOINT.json`;
- status musí byť `TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT` a
  candidate `CHECKPOINT_ONLY_NO_PHYSICS_VERDICT`;
- všetky checkpoint preconditions, source hashes, support/depth identity a
  owner restoration musia byť true;
- rovnice, solver, prahy, povrchy a equation builder sa nemenia;
- checkpoint sám nemení C2, K4 ani fyzikálny verdikt.

## Scope a exekúcia

- compile → help → smoke → presne jeden checkpoint atom;
- interný runtime `4.8 s`, vonkajší procesný limit `30 s`;
- žiadny resume audit, tail interpretácia ani score update v tomto kroku;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 367:
  `scripts/367_script_KMPC_123_P5_3g7_C2_NIV_k0p15_support_06_checkpoint.py`;
- runner SHA-256:
  `95B4100D7DA19552EF6EA6E6571426D64E683F3BE0AF234F05F97947396D26DF`;
- source contract `20` položiek, prerequisite contract `6` položiek;
- stabilný harness SHA-256
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- canonical output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 367 spustený cez Python.
Od tohto bodu je immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke/official exit 0; raw SHA `D3B31093D84156D05BF4EE8EC707D53B5D653DE5700289E6EA68627674898DC8` | `IMMUTABLE_CHECKPOINT_ATTEMPT` |
| 2026-07-19 | M1 a 8/9 preconditions PASS; accepted M3 driver `fuel_Euler[6]=1.48191e-10 >1e-10` | `CHECKPOINT_INCOMPLETE_NO_VERDICT` |
| 2026-07-19 | KMPC-124 smoke fail-closed; priamy widened-support same-matrix nástupca vyžadovaný | `HISTORY_PRESERVED` |
