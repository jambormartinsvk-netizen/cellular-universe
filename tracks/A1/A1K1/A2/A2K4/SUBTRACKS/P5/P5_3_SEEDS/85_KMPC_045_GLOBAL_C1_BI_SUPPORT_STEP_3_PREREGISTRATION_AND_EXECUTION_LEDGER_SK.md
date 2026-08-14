# KMPC-045 — GLOBAL_C1 BI support step 3: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI_SUPPORT_STEP_3`  
**Stav:** `KMPC045_TECHNICAL_FAILURE_PF074 / KMPC046_AUTHORITATIVE_PASS`  
**Identita:** `BI / k=0.05 Mpc^-1 / nominal`  
**Skóre a triggery:** `NONE`

## 1. Jediná otázka a immutable vstupy

KMPC-042 dokázal, že BI candidate `[0,3]` nestačí. KMPC-044 následne
uzavrel BI M1 order-7 same-matrix numerical boundary. KMPC-045 smie položiť
iba otázku:

> Je BI candidate support `[0,5]` dostatočný voči audit supportu `[0,7]`?

Immutable prerequisite výsledky:

- KMPC-042:
  `RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05.json`, SHA-256
  `E5F18DA4DE5A718C4448D095804F6D41FE88445A95FB99645EFBCCB48D48CA61`;
- KMPC-043:
  `RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json`, SHA-256
  `B02D1D16CFAE4331378B68F12258142F84A424419BB9D3A52AAEE87D0CC61EB0`;
- KMPC-044:
  `RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY.json`, SHA-256
  `C3BD732C9F3FB402E4143DA6EF149E6C2830F5F5C96D17D21D314BC5B82F1C36`.

KMPC-044 neexportuje opravený stav. Preto sa z BI KMPC-043 stavu na tej
istej BI `121×98` reduced matici zopakuje presne jedna deterministická
`np.linalg.lstsq(A_r,-r,rcond=None)` korekcia. Musí mať rank `98`, veľkosť
`<=1e-14`, reprodukovať KMPC-044 correction pri relative `1e-12` a absolute
`1e-16`, zachovať anchor/lower a uzavrieť `121/121 + 18/18`.

CDI JSON, CDI stav ani CDI korekčný vektor nie sú vstupom.

## 2. Presný support a tail kontrakt

| Rola | Support | F0 počet | M3 počet |
|---|---:|---:|---:|
| immutable regresia A | `[0,3]` | 8 | 52 |
| immutable regresia B / candidate | `[0,5]` | 12 | 78 |
| audit | `[0,7]` | 16 | 104 |

Zmrazené metriky:

- regresia `[0,3]` a `[0,5]` voči KMPC-042: relative `1e-12`, absolute
  `1e-14`;
- common bridge `[0,5]↔[0,7]`: iba powers `0…5`, relative `1e-8`, absolute
  fallback `1e-12`;
- tail baseline: powers `1…5`;
- jediný nový autoritatívny tail:
  `sum(abs(c_j)*z**j)` iba pre `j=6,7`;
- tail relative `1e-6`, absolute fallback norm/tolerance `1e-12`;
- plochy presne `z={1e-4,1e-2}`;
- signed tail je iba diagnostický a nesmie vytvoriť PASS rušením znamienok;
- actual conditional `S-C0` coefficient guard sa zopakuje pre `[0,5]↔[0,7]`;
- všetky tri supporty musia prejsť rank/driver/holdout/contract/registry/
  forbidden/production/regularity/finite core guardy.

## 3. Rozhodovací strom

1. Hash/source/registry/runtime/JSON/publish chyba →
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`.
2. BI M1 rekonštrukcia alebo `[0,3]/[0,5]` regresia FAIL →
   `REVIEW_BI_SUPPORT_STEP_3_REGRESSION_OR_M1_PROVENANCE_UNCLOSED`.
3. Core alebo `S-C0` FAIL →
   `REVIEW_BI_SUPPORT_STEP_3_CORE_GATE_UNCLOSED`.
4. Common bridge `0…5` FAIL →
   `REVIEW_BI_SUPPORT_STEP_3_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`.
5. Tail envelope `6,7` FAIL →
   `REVIEW_BI_SUPPORT_STEP_3_SUPPORT_05_REMAINDER_UNCLOSED`.
6. Všetko PASS →
   `PASS_BI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Skript nevydáva autoritatívny verdikt.

## 4. Očakávanie a STOP hranica

Predbežná hypotéza je, že common `0…5` ostane stabilný a tail `6,7` môže
prejsť podobne ako pri CDI, ale číselný BI výsledok je `NEZNÁMY` a medzi
módmi sa neprenáša.

Ak tail zlyhá, `[0,9]` sa nespustí automaticky. Nasleduje samostatný no-solve
audit rastu koeficientov, asymptotických pomerov a odhadu polomeru
konvergencie. Prah ani plochy sa po výsledku nemenia.

## 5. Prevádzkový kontrakt

Povinné poradie: compile base, compile runner, `--help`, `--smoke`, presne
jeden `--audit`, hash a nezávislé čítanie JSON. Interný limit je presne
`4.8 s`, externý najviac `10 s` na proces. Smoke musí overiť tri prerequisite
hashe/identity, support/count/`[0,9]` rejection, BI M1 correction regresiu,
state powers `-1…7`, registry restoration po vyvolanej výnimke, JSON scalar
a atomic/exclusive publish guardy.

Canonical success/failure/temp cesta sa nikdy neprepisuje. Technická chyba
nevytvára fyzikálny verdict ani tichý rerun.

## 6. Artefakty a nonclaims

- plánovaný base:
  `scripts/baseScripts/p5_general_synchronous/bi_support_step3.py`;
- plánovaný runner:
  `scripts/289_script_KMPC_045_P5_3g7_BI_support_step3_05_07.py`;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_045_P5_3G7_BI_SUPPORT_STEP_3_05_07.json`.

Bez `[0,9]`, NID/NIV, iných `k`/variantov, S-M, full hierarchy, ODE, P5.4,
G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 7. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ prikázal pokračovať | `AUTHORIZED` |
| 2026-07-18 | BI prerequisite hashe, supporty, metriky, prahy, plochy, rozhodovací strom a `[0,9]` zákaz zmrazené | `PREREGISTERED` |
| 2026-07-18 | base SHA `1ABB16A886432C4A2B908CE802598D4970567030C2E7CCAFE6FA1A37A4C36CC8`; runner SHA `B3CCBA6068791F3DB98D60CEDC4025219AE029DF7F48D373D36925A9DB60CECB` | `FROZEN` |
| 2026-07-18 | compile base; compile runner; `--help` | `PASS / PASS / PASS` |
| 2026-07-18 | smoke: support/count/`[0,9]`, tri prerequisite, BI correction, state powers, registry exception restore, JSON a publish fixtures | `PASS` |
| 2026-07-18 | canonical/failure/temp output guard pred auditom | `ABSENT / READY_FOR_ONE_AUDIT` |
| 2026-07-18 | jediný KMPC-045 audit zastal po solve pred S-C0/core/tail payloadom: wrong helper owner; failure report následne odhalil missing `sys` import | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT / PF-074` |
| 2026-07-18 | immutable failure JSON SHA `FFFF061651A06F3FD097F5C6622C42084643F41D98C2C3B2B0C141A54C330C01`; canonical a temp absent | `PRESERVED` |

## 8. KMPC-046 úzky technický nástupca — predregistrácia

KMPC-045 sa neopakuje. KMPC-046 zachová presne jeho source hash, tri
prerequisite hashe, BI M1 correction, supporty, rovnice, metriky, prahy,
plochy, limit `4.8 s` a PASS/REVIEW strom. Povolené sú iba dve zmeny:

1. owner bridge sprístupní počas volania KMPC-045 base helper
   `bi_c1_coverage.c1._s_c0_actual_coefficient_guard` pod očakávaným menom,
   s identity guardom a odstránením bridge vo `finally`;
2. runner explicitne importuje `sys` a smoke pošle syntetickú serializovanú
   failure správu cez `sys.stderr`.

Smoke musí navyše overiť wrong owner rejection, callable identity, bridge
attach, detach a owner restore. Immutable PF-074 failure hash je nový
povinný prerequisite. Žiadna zmena support výpočtu ani výsledkové dáta z
nedokončeného KMPC-045 procesu sa nesmú použiť.

Plánované artefakty:

- base overlay `bi_support_step3_v2_owner.py`;
- runner `290_script_KMPC_046_P5_3g7_BI_support_step3_owner_successor.py`;
- output `RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json`.

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | PF-074 príčina z runtime owner mapy a runner tracebacku potvrdená | `ROOT_CAUSE_CLOSED` |
| 2026-07-18 | KMPC-046 owner/stderr-only scope zmrazený pred vytvorením alebo spustením nástupcu | `PREREGISTERED` |
| 2026-07-18 | overlay SHA `EB434319DA1E07AAE23B2CE76F6287934B941FF5A7835AF9CDE702AECA6E5EDB`; runner SHA `E20F21C1A19AA72FE6345DCFB451C55018D59CEC4A65C0C752DACB62A14D1EDB` | `FROZEN` |
| 2026-07-18 | KMPC-046 canonical/failure/temp guard | `ABSENT / READY_FOR_PREFLIGHT` |
| 2026-07-18 | compile overlay; compile runner; `--help` | `PASS / PASS / PASS` |
| 2026-07-18 | smoke: pôvodné KMPC-045 guardy + owner identity/attach/detach/restore + stderr failure route | `PASS` |
| 2026-07-18 | KMPC-046 output guard po smoke | `ABSENT / READY_FOR_ONE_AUDIT` |
| 2026-07-18 | jediný KMPC-046 audit, internal `3.0 s`, external exit `0`; canonical JSON publikovaný atomicky | `TECHNICAL_PASS` |
| 2026-07-18 | nezávislá kontrola result/source/prerequisite hashov, BI M1, regresie/core/S-C0/common/tail/cancellation, owner restore a publish guardov | `PASS_AUDIT` |
| 2026-07-18 | autoritatívny rozsudok v dokumente 86; BI `.05/nominal` support vetva uzavretá | `PASS_SUPPORT_05_ADEQUATE` |
