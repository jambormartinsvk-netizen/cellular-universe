# KMPC-049 — NID order-7 M3 provenance: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID / ORDER7_PROVENANCE`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `KMPC049_TECHNICAL_FAILURE_PF075 / KMPC050_PREREGISTERED`  
**K4/P5:** `LIVE 60/100 / 3.5/6`; skóre a triggery `NONE`

## 1. Jediná otázka

KMPC-048 má regression/common/tail/combined-`R_fs` PASS, ale support `[0,7]`
M3 driver a holdout neprešli. KMPC-049 nemení solve ani koeficienty. Pomocou
identity-guarded capture vrstvy nad tou istou `_solve_equilibrated` a
`_holdout_metrics` cestou zistí:

> Je zlyhanie order-7 M3 bloku dôsledkom rank/formula/registry driftu, alebo
> je lokalizované na numerickej relative-scale hranici plnohodnostnej
> zmrazenej matice?

Immutable prerequisite: KMPC-048 JSON SHA
`B4F320F5D850DCF78FD9EC2A5BDDEBDA87D590DA2988CF505FA7D5B25B49BF32`.

## 2. Zmrazený rozsah

- mód `NID`, `k=.05`, nominal, support iba `[0,7]`, leading `j=0`;
- tá istá M1 order-5 štandardná kotva a rovnaká 104×104 M3 matica;
- bez zmeny rovníc, scalingu, `rcond=1e-12`, tolerancií alebo výsledkového
  stavu;
- capture musí overiť owner/callable identity, presne jeden driver a jeden
  holdout call a obnovu oboch ownerov vo `finally` aj po vyvolanej výnimke;
- exportovať hash C-contiguous matrix/constant/holdout bytes, shape, labels,
  raw a equilibrated rank/singular ratios;
- pre každý driver[7] a holdout[7] exportovať raw residual, scale,
  relative/absolute branch a PASS podľa pôvodných prahov;
- vypočítať normovaný backward error a diagnostickú jednu same-matrix
  least-squares korekciu, ale nepublikovať opravený stav a nemeníť KMPC-048.

Numerical-boundary kandidát navyše vyžaduje, aby jediná correction mala
`max_abs <= 1e-12` aj `Linf/max(Linf(x),1) <= 1e-12` a aby po nej pôvodné
driver/holdout prahy prešli. Tieto limity sú zmrazené pred behom.

## 3. Rozhodovací strom

1. owner/hash/capture/runtime/JSON chyba → technický FAIL, bez fyziky;
2. matica/labels/shape/rank/contract alebo immutable regresia FAIL →
   `REVIEW_NID_ORDER7_PROVENANCE_OR_FORMULA_DRIFT`;
3. nefinite alebo veľký absolútny/backward error →
   `REVIEW_NID_ORDER7_NONNUMERICAL_CORE_UNCLOSED`;
4. full rank, immutable regresia a lokalizované precision-sensitive rezíduá
   → `PASS_NID_ORDER7_PROVENANCE_NUMERICAL_BOUNDARY_CANDIDATE_ONLY`.

Tento PASS by iba povolil samostatný same-matrix numerical boundary audit.
Neudeľuje support adequacy ani fyzikálny bod. `[0,9]` je zakázaný.

## 4. Prevádzka

Compile base, compile runner, help, smoke, output guard a jediný audit;
interný limit `4.8 s`, externý `10 s`. Smoke musí pokryť wrong owner,
double capture, exception restore, missing prerequisite, JSON a publish.

- base: `nid_order7_m3_provenance.py`;
- runner: `293_script_KMPC_049_P5_3g7_NID_order7_M3_provenance.py`;
- output: `RUN_KMPC_049_P5_3G7_NID_ORDER7_M3_PROVENANCE.json`.

## 5. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | KMPC-048 a externý balík EA-007 uzavreli tail PASS a order-7 core REVIEW | `PREREQUISITE_CLOSED` |
| 2026-07-18 | capture-only otázka, owner guardy, matica, diagnostiky a rozhodovací strom zmrazené | `PREREGISTERED` |
| 2026-07-18 | base SHA `DC7C178B8A73DC97B5FC6CCAB97FE88F3E95F59F0EDBF05985451DD6572319C3`; runner SHA `BA3C88F96CD450CE4E78A1F4C010C2D43C461C764F1319E6FBD8655D7D6BB6D3` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile, help a smoke prešli; jediný audit zastal na druhom shared-owner solve calle | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT / PF-075` |
| 2026-07-18 | immutable failure JSON SHA `EB5EA48145CB52C95826A3111ABBD2DF0C05AC531B8471DF704E2032FA0B6E35`; canonical/temp absent | `PRESERVED` |

## 6. KMPC-050 úzky technický nástupca — predregistrácia

KMPC-049 sa neopakuje. KMPC-050 zachová jeho fyziku, prerequisite, matrix
otázku, korekčné limity, prahy, output payload a owner restore. Jediná
dovolená zmena capture vrstvy:

- call s `expected_rank != 104` sa eviduje ako passthrough a ide priamo do
  pôvodného solvera bez capture;
- presne jeden call s `expected_rank == 104` a shape `(104,104)` sa zachytí;
- druhý cieľový 104 call je fail-closed;
- smoke overí syntetický passthrough 2×2, cieľový 104 signature guard a
  obnovu ownerov po výnimke.

Povinný prerequisite je aj PF-075 failure JSON. Žiadna zmena rovníc,
supportu, matice, prahov alebo correction diagnostiky.

Prevádzka KMPC-050 zostáva rovnaká: samostatne compile base, compile runner,
help, smoke, output guard a práve jeden audit; interný limit `4.8 s`, externý
`10 s`.

- base V2: `nid_order7_m3_provenance_v2_rank_filter.py`;
- runner: `294_script_KMPC_050_P5_3g7_NID_order7_M3_provenance_rank_filter.py`;
- canonical output:
  `RUN_KMPC_050_P5_3G7_NID_ORDER7_M3_PROVENANCE_RANK_FILTER.json`.

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | base V2 SHA `D583209F7B1CCB2648EFF3DD1D59F3F4382C9E1FDB66F7854404F3BE4B9AA025`; runner 294 SHA `F6A30366769597044EDD37C7ECF67782A6B3D526810959CAFFBCC4F62077628A` | `KMPC050_FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base/runner, help, behaviorálny smoke a output guard prešli; jediný audit exit `0`, runtime `1.188 s` | `TECHNICAL_COMPLETE` |
| 2026-07-18 | raw SHA `8D527E822959D861EB33994233D22BDF752C368025AC66F28C6F820DEF479F65`; provenance/rank/regression PASS, correction driver PASS, holdout na order 7 ostal FAIL | `REVIEW_NID_ORDER7_CONSTRAINT_COMPATIBILITY_UNCLOSED` |
