# KMPC-040 — GLOBAL_C1 CDI support step 3: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / CDI_SUPPORT_STEP_3`  
**Stav pri predregistrácii:** `AUTHORIZED_NOT_EXECUTED`  
**Skóre a triggery:** `NONE`

## 1. Dôvod a nemenné predpoklady

KMPC-035 uzavrel core a common bridge medzi supportmi `[0,3]` a `[0,5]`,
ale tail powers `4,5` voči candidate `[0,3]` neprešiel. KMPC-039 následne
uzavrel numerickú hranicu štandardného M1 order-7 na tej istej zmrazenej
matici. Tým je povolený jediný ďalší krok: otestovať candidate `[0,5]`
proti audit supportu `[0,7]`.

Immutable prerequisite výsledky:

- KMPC-035: `RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json`,
  SHA-256 `A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`;
- KMPC-036: `RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json`,
  SHA-256 `39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497`;
- KMPC-039: `RUN_KMPC_039_P5_3G7_M1_ORDER7_CONTEXT_OWNER.json`,
  SHA-256 `BDF3317235FEDEA23EDF8C23563423014F2E98A461C6E638C474DF94471CE016`.

KMPC-039 neexportuje opravený stav ako samostatné pole. KMPC-040 preto smie
z immutable KMPC-036 stavu deterministicky zopakovať presne jednu už
auditovanú float64 least-squares korekciu na tej istej `121×98` reduced
matici. Povolené je iba `np.linalg.lstsq(A_reduced, -residual, rcond=None)`;
maximálna korekcia musí byť `<=1e-14`, rank `98`, anchor `h[1]` presný,
driver/initial `121/121`, holdout `18/18` a lower powers `-1…5` musia prejsť.
Výsledná veľkosť korekcie musí reprodukovať KMPC-039 v rámci zmrazenej
regresnej tolerancie. Nejde o nový solve, novú rovnicu ani nový fyzikálny
parameter.

## 2. Presný výpočtový kontrakt

Identita ostáva `CDI / k=0.05 Mpc^-1 / nominal`.

| Rola | Support | F0 počet | M3 počet |
|---|---:|---:|---:|
| immutable regresia A | `[0,3]` | 8 | 52 |
| immutable regresia B / candidate | `[0,5]` | 12 | 78 |
| audit | `[0,7]` | 16 | 104 |

Rozhodovacie metriky sú zmrazené pred behom:

- regresia `[0,3]` a `[0,5]` proti KMPC-035: relative `1e-12`, absolute
  `1e-14`;
- common bridge `[0,5] ↔ [0,7]`: iba powers `0…5`, relative `1e-8`,
  absolute fallback `1e-12`;
- tail baseline: powers `1…5`;
- jediný autoritatívny nový tail: obálka
  `sum(abs(c_j)*z**j)` iba pre `j=6,7`;
- tail relative `1e-6`, absolute fallback norm/tolerance `1e-12`;
- plochy presne `z={1e-4,1e-2}`;
- signed tail je iba diagnostický; rušenie znamienok nesmie vytvoriť PASS;
- skutočný `S-C0` coefficient guard sa zopakuje pre `[0,5] ↔ [0,7]`.

## 3. Predregistrovaný rozhodovací strom

1. Ak zlyhá prerequisite hash, source hash, M1 rekonštrukcia, shape/registry
   guard alebo runtime/JSON/write guard, ide o
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`.
2. Ak zlyhá immutable regresia `[0,3]` alebo `[0,5]`, kandidát je
   `REVIEW_CDI_SUPPORT_STEP_3_REGRESSION_OR_M1_PROVENANCE_UNCLOSED`.
3. Ak zlyhá core alebo `S-C0`, kandidát je
   `REVIEW_CDI_SUPPORT_STEP_3_CORE_GATE_UNCLOSED`.
4. Ak zlyhá common bridge `0…5`, kandidát je
   `REVIEW_CDI_SUPPORT_STEP_3_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`.
5. Ak common prejde, ale tail `6,7` neprejde, kandidát je
   `REVIEW_CDI_SUPPORT_STEP_3_SUPPORT_05_REMAINDER_UNCLOSED`.
6. Iba ak prejde všetko, kandidát je
   `PASS_CDI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Skript nevydáva autoritatívny verdikt. Ten vznikne až nezávislým auditom
canonical JSON orchestrátorom.

## 4. Povolený beh a zakázané rozšírenia

Pred autoritatívnym behom sú povolené iba `compile → --help → --smoke`.
Potom je povolený presne jeden bounded `--audit` s interným limitom `4.8 s`
a externým limitom `10 s`. Výstup musí byť zapísaný atomicky a exkluzívne;
existujúci success, failure alebo dočasný súbor sa nesmie prepísať.

Zakázané bez novej predregistrácie: `[0,9]`, ďalší refinement, zmena
tolerancií/plôch, zmena rovníc, post-hoc rerun a interpretácia technického
zlyhania ako fyzikálneho výsledku. Ak tail `6,7` zlyhá, nasleduje najprv
audit rastu koeficientov, asymptotického pomeru a odhadu polomeru
konvergencie; `[0,9]` nevzniká automaticky.

## 5. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ autorizoval pokračovanie na step 3 | `AUTHORIZED` |
| 2026-07-18 | kontrakt, immutable hashe a rozhodovací strom zmrazené | `PREREGISTERED` |
| 2026-07-18 | `py_compile` pre nový base a runner | `PASS` |
| 2026-07-18 | runner `--help` | `PASS` |
| 2026-07-18 | smoke: prerequisite/M1/support/registry/JSON/write guards | `PASS` |
| 2026-07-18 | jediný bounded audit, interný limit `4.8 s` | `TECHNICAL_COMPLETE` |
| 2026-07-18 | canonical JSON zapísaný exkluzívne; failure/tmp nevznikli | `PASS` |
| 2026-07-18 | nezávislý JSON audit a autoritatívna interpretácia | dokument 76 |
