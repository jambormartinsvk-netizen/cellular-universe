# KMPC-044 — BI M1 order-7 numerical boundary closure: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI_M1_ORDER7_NUMERICAL_BOUNDARY`  
**Stav:** `EXECUTED_IMMUTABLE / AUTHORITATIVE_PASS`  
**Identita:** `BI / k=0.05 Mpc^-1 / nominal / order=7`  
**Skóre a triggery:** `NONE`

## 1. Jediná otázka

Možno na presne tej istej už zostavenej BI float64 sústave a pri nezmenených
prahoch preukázať, že KMPC-043 otvorených 5 driver/initial riadkov a jeden
holdout sú solver/rounding floor, nie invariantný rozpor BI order-7
recurrence?

Immutable prerequisite je
`RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json`, SHA-256
`B02D1D16CFAE4331378B68F12258142F84A424419BB9D3A52AAEE87D0CC61EB0`.

CDI KMPC-036/039 je iba metodický precedens. KMPC-044 nesmie načítať CDI
JSON, CDI stav ani CDI correction vector. BI systém sa znovu zostaví z
frozen BI constraints a musí reprodukovať KMPC-043 pred každou korekciou.

## 2. Zmrazený kontrakt

- full matica `121×99`, reduced matica `121×98`, rank `98/98`;
- hard anchor presne `h[1]`;
- powers presne `-1…7`, stavy presne v poradí frozen `VARS`;
- driver+initial `121`, holdouty `18` (`Einstein_00/0i`);
- relative residual `<=1e-10` pri term norm `>1e-12`;
- absolute residual `<=1e-12` pri menšej norme;
- lower regresia `abs(diff)<=max(1e-14,1e-12*scale)`;
- anchor difference `<=1e-14`;
- correction cap `max(abs(delta_x))<=1e-14`;
- presne jeden float64 refinement a jeden high-precision solve;
- high precision presne `80 dps`, exact transfer cez `float.as_integer_ratio()`;
- rovnaká reduced float64 matica a RHS, bez native high-precision rebuild;
- Householder QR používa už auditovaný `sign(0)→+1` tie a správneho
  `mpmath.mp` context ownera z KMPC-039.

V0 musí presne reprodukovať tieto otvorené množiny:

- driver/initial: `gamma_Euler[7]`, `fs_Euler[6]`, `fs_Euler[7]`,
  `cdm_continuity[7]`, `tight_coupling[7]`;
- holdout: `Einstein_0i[7]`.

## 3. Povinné vetvy jediného auditu

1. **V0 immutable regresia:** hash, identita, shapes, rank, state/powers,
   anchor, všetkých 121+18 riadkov a presný 5+1 REVIEW pattern.
2. **V1 diagnostika:** `Aᵀr`, normwise backward error a residual invarianty;
   bez zmeny stavu.
3. **V2 jediná korekcia:** vyriešiť `A_r delta_x=-r`, presne raz; znovu
   overiť 121+18, lower `-1…5`, anchor a cap korekcie.
4. **V3 jediný 80-dps QR solve:** tá istá float64 matica/RHS prenesená
   exaktne; overiť 121+18 v 80 dps aj po jednom projekte späť do float64,
   lower regresiu a anchor.

Keďže smoke povinne vykoná lifecycle test na presnej `121×98` matici,
jeho interný limit je presne `12 s` a externý najviac `15 s`; starý malý
API smoke s limitom `4.8 s` by nezachytil PF-072. Audit má interný limit
presne `45 s` a externý limit najviac `60 s`. Druhá korekcia, druhý
high-precision solve v auditnej vetve,
SVD, normal equations, pivotovanie, zmena poradia alebo native rebuild sú
zakázané.

## 4. Rozhodovací strom

| Stav | Machine kandidát | Autoritatívny význam |
|---|---|---|
| V0 alebo parity fail | `REVIEW_BI_M1_ORDER7_REFERENCE_OR_REGRESSION_UNCLOSED` | V1–V3 neinterpretovať; BI support ostáva blokovaný |
| correction/difference cap, lower alebo anchor fail | `REVIEW_BI_M1_ORDER7_REFINEMENT_OUT_OF_BOUNDS` | žiadny provenance PASS |
| V2 aj V3 uzavrú 121+18 vrátane projekcie | `PASS_BI_M1_ORDER7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY` | hlavný audit smie uzavrieť BI numerical boundary |
| V2 nie, ale V3 aj projekcia áno | `PASS_BI_M1_ORDER7_FLOAT64_ROUNDING_FLOOR_CANDIDATE_ONLY` | hlavný audit smie uzavrieť BI numerical boundary |
| V3 same-matrix zostane nad prahom | `REVIEW_BI_M1_ORDER7_SAME_MATRIX_BOUNDARY_UNCLOSED` | formula/native-rebuild nástupca, nie zmena prahu |
| exception/timeout/dependency/JSON/publish | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` | zapísať PF; KMPC-043 verdict bez zmeny |

Skript neprideľuje autoritatívny verdikt.

## 5. Očakávania bez predprideleného výsledku

- V0 má presne reprodukovať 5+1 otvorených riadkov;
- correction sa očakáva rádovo `1e-15`, ale jediný záväzný cap je `1e-14`;
- hypotéza je, že V2 a V3 uzavrú všetkých 139 riadkov bez lower/anchor
  regresie;
- ak hypotéza neprejde, prahy, dps a metóda sa spätne nemenia.

## 6. Python a publish preflight

Povinné poradie: compile base, compile runner, `--help`, behaviorálny
`--smoke`, jediný `--audit`, hash a nezávislé čítanie JSON. Smoke musí
odmietnuť wrong BI prerequisite hash/identity, CDI mode, zmenu prahu,
reordered state/powers/rows, missing anchor, druhý refinement/solve,
nesprávne dps, nefinite JSON a publish collision. Presná zmrazená matica
musí prejsť QR lifecycle smoke, nie iba malá API matica.

Canonical success, failure a temp cesta sú exkluzívne a publikujú sa
atomicky. Existujúci výsledok sa nikdy neprepisuje.

## 7. Artefakty a nonclaims

- plánovaný base:
  `scripts/baseScripts/p5_general_synchronous/bi_m1_order7_numerical_boundary.py`;
- plánovaný runner:
  `scripts/288_script_KMPC_044_P5_3g7_BI_M1_order7_numerical_boundary.py`;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY.json`.

Bez BI support `[0,7]`, tail metriky, `[0,9]`, NID/NIV, iných `k`/variantov,
S-M, ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 8. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ prikázal pokračovať | `AUTHORIZED` |
| 2026-07-18 | BI identita, prerequisite, 5+1 pattern, metóda, prahy, limity a rozhodovací strom zmrazené pred novým Python procesom | `PREREGISTERED` |
| 2026-07-18 | ešte pred Python procesom opravený iba smoke runtime `4.8→12 s`, pretože povinný exact-matrix 80-dps lifecycle potrebuje viac než starý API smoke; external cap `15 s` | `PREREGISTRATION_RUNTIME_ERRATUM / PHYSICS_UNCHANGED` |
| 2026-07-18 | base SHA `FBB920976CAF5FAF2DDA87D1286573E91155A0688C23EB8E2A5AB0EE3B70BFAD`; runner SHA `AE319BB51D7C0BCE8DCE739E69E40A5E082BE1AB3F30E9C040C5379FA00DF37A` | `FROZEN` |
| 2026-07-18 | compile base; compile runner; `--help` | `PASS / PASS / PASS` |
| 2026-07-18 | behaviorálny smoke vrátane exact BI `121×98` 80-dps QR lifecycle, 11 base a 5 publish/runtime fixtures | `PASS`, internal `4.313 s` |
| 2026-07-18 | canonical/failure/temp output guard pred auditom | `ABSENT / READY_FOR_ONE_AUDIT` |
| 2026-07-18 | jediný `--audit`, internal `5.109 s`, external exit `0`; canonical JSON publikovaný atomicky | `TECHNICAL_PASS` |
| 2026-07-18 | nezávislá kontrola SHA, source parity, V0 5+1, V1 invariants, V2/V3 121+18, lower, capov, operation counts a publish guardov | `PASS_AUDIT` |
| 2026-07-18 | autoritatívny rozsudok v dokumente 84; BI support step 3 iba odblokovaný pre samostatnú predregistráciu | `PASS_SAME_MATRIX_ONLY` |
