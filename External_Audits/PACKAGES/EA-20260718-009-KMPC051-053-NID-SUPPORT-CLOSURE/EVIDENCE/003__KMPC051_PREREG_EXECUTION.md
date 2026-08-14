# KMPC-051 — NID M1 depth 5→7: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID / M1_DEPTH`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED`  
**K4/P5:** `LIVE 60/100 / 3.5/6`; score a triggery `NONE`

## 1. Jediná otázka

KMPC-050 vylúčil rank loss, veľkú solve chybu aj jednoduchý roundoff, ale
M3 order-7 Einstein holdouty zostali neuzavreté. Zdroj pritom dodáva M3
supportu `[0,7]` štandardný M1 perturbation state iba do orderu `5`.

> Uzavrie rovnakú NID/.05/nominal M3 `[0,7]` sústavu konzistentné rozšírenie
> hard-anchored M1 state z depth 5 na depth 7 bez poškodenia orderov 0…5?

Immutable prerequisite je KMPC-050 JSON SHA
`8D527E822959D861EB33994233D22BDF752C368025AC66F28C6F820DEF479F65`.

## 2. Zmrazený rozsah

- iba `NID`, `k=.05`, nominal, M3 support stále `[0,7]`, leading `j=0`;
- baseline M1 depth `5`; diagnostický kandidát M1 depth `7`;
- tá istá hard M1 kotva, rovnice, background, state registry, `rcond`, driver,
  holdout, absolute fallback a correction prahy;
- bez `[0,9]`, NIV, iných `k`/variantov, S-M, ODE alebo zmeny publikovaného
  stavu;
- oba M3 behy musia používať tú istú rank-filtered capture cestu KMPC-050;
- baseline musí reprodukovať immutable matrix/constant hashe a core metriky;
- exportovať M1 rank/count, hard-anchor rozdiel, full-depth driver/holdout
  residual diagnostic, spoločné M1 koeficienty `-1…5`, M3 common `0…5`,
  matrix/constant hashe a max rozdiely;
- common regression limit ostáva `1e-8`; correction limity ostávajú `1e-12`.

## 3. Rozhodovací strom

1. source/prerequisite/capture/runtime/JSON chyba → technický FAIL;
2. depth-5 baseline nereprodukuje KMPC-050 →
   `REVIEW_NID_M1_DEPTH_BASELINE_DRIFT`;
3. depth-7 M1 nemá reduced rank `98/98`, full vector `99`, presnú kotvu alebo
   finite stav → `REVIEW_NID_M1_DEPTH7_EXTENSION_UNCLOSED`;
4. M1 alebo M3 common `0…5` prekročí `1e-8` →
   `REVIEW_NID_M1_DEPTH7_COMMON_REGRESSION`;
5. depth-7 pôvodné M3 driver aj holdout prahy prejdú →
   `PASS_NID_M1_DEPTH_MISMATCH_CANDIDATE_ONLY`;
6. inak → `REVIEW_NID_M1_DEPTH_MISMATCH_REJECTED_CONSTRAINT_AUDIT_REQUIRED`.

Ani kandidátsky PASS nepridáva fyzikálny bod. Povoľuje iba samostatné
potvrdenie M1-depth kontraktu. REVIEW vetva predregistruje Bianchi/constraint
dependence audit; nerozširuje support.

## 4. Prevádzka

Compile base, compile runner, help, smoke, output guard a jediný audit;
interný limit `4.8 s`, externý `10 s`. Pred Python sa zmrazí SHA nového base
a runnera. Smoke nevykonáva plný M1/M3 solve.

## 5. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | KMPC-050 + EA-008 lokalizovali order-7 constraint compatibility a vylúčili jednoduchý roundoff | `PREREQUISITE_CLOSED` |
| 2026-07-18 | M1 depth 5→7 otázka, prahy, rozhodovací strom a zákazy zmrazené | `PREREGISTERED` |
| 2026-07-18 | base `nid_m1_depth_5_7.py` SHA `8B4572BBA51844471782D686F4199436186491E0F8274BD5CF1CB2EAC76B8B9C`; runner 295 SHA `5506A1EFADE52EEEB626CD03F0BF5F5555B94E166A2E2CC7B863C411C142ECBF`; output `RUN_KMPC_051_P5_3G7_NID_M1_DEPTH_5_7.json` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base/runner, help, smoke a output guard prešli; jediný audit exit `0`, internal `3.281 s` | `TECHNICAL_COMPLETE` |
| 2026-07-18 | raw SHA `AF088030BA709F08D40D825B9477C9A84BA330705CDDFB1C12C52B0DD3FC1E5E`; depth-7 M1 a common regresia PASS; original M3 holdout PASS, driver tesne FAIL; jedna bounded correction uzavrela oba | `REVIEW_DEPTH7_CONSTRAINT_CLOSED_NUMERICAL_DRIVER_BOUNDARY` |
