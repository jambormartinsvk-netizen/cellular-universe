# KMPC-037 — M1 order-7 numerical refinement and boundary closure: predregistrácia

**Dátum:** 2026-07-18  
**Identita:** `GLOBAL_C1 / M1_ORDER7_NUMERICAL_REFINEMENT_AND_BOUNDARY_CLOSURE_AUDIT`  
**Stav:** `FROZEN / EXECUTED_TECHNICAL_FAILURE_PF072 / SUPERSEDED_BY_KMPC039`  
**Predchodca:** KMPC-036 JSON SHA-256
`39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497`

## 1. Jediná otázka

Možno na presne tej istej KMPC-036 float64 sústave a nezmenených prahoch
preukázať, že tri terminal power-7 driver odchýlky sú float64 solver/rounding
floor, a nie invariantný rozpor už zostavenej sústavy?

KMPC-037 nemení rovnice, parametre, state/power registry, hard anchor ani
support. Nevykonáva CDI support step 3 a nevytvára `[0,9]`.

## 2. Zmrazený kontrakt a prahy

- `CDI / k=0.05 Mpc^-1 / nominal / order=7`;
- full matrix `121×99`, reduced matrix `121×98`, rank `98/98`;
- exact hard anchor `h[1]`;
- 121 driver+initial riadkov a 18 nezávislých `00/0i` holdoutov;
- relative residual `<=1e-10` pri term norm `>1e-12`;
- absolute residual `<=1e-12` pri menšom term norme;
- lower state regression `abs(diff)<=max(1e-14,1e-12*scale)`;
- anchor difference `<=1e-14`;
- bounded correction `max(abs(delta_x))<=1e-14`;
- najviac jeden float64 refinement a jeden high-precision solve;
- high precision: `mpmath`, presne `80` decimal digits, vstupné float64 čísla
  prenesené exaktne cez `float.as_integer_ratio()`;
- high-precision least squares: QR solve tej istej reduced float64 matice;
- interný limit `4.8 s` pre compile/help/smoke a V0–V2; high-precision audit
  má samostatný interný cap `45 s` a externý cap `60 s` podľa segmentačného
  pravidla AR29.

Ak dependency/API smoke ukáže, že QR solve nie je v tomto limite technicky
uskutočniteľný, fyzika sa nespustí a vznikne iba technický incident. Metóda
sa po výsledku nesmie potichu zmeniť na normal equations.

## 3. Povinné vetvy jedného runu

### V0 — immutable reference regression

Načítať KMPC-036 JSON, overiť jeho SHA, znovu zostaviť rovnakú affine sústavu
a potvrdiť shapes, rank, anchor, state/power/row parity, lower coefficients,
121 residualov a 18 holdoutov. V0 fail zastaví run pred refinementom.

### V1 — float64 diagnostics

Pre reduced systém `A_r x_r=b_r` exportovať:

- `r=A_r x_r-b_r`;
- `||A_r^T r||_inf`;
- normwise backward error
  `||r||_2/(||A_r||_2||x_r||_2+||b_r||_2)`;
- invariant `metric×term_norm=abs(residual)` pre každý riadok.

V1 je diagnostic-only.

### V2 — presne jeden bounded refinement

Vypočítať jedinú least-squares korekciu `delta_x` z `A_r delta_x=-r`.
Zostaviť celý full vector s nezmeneným anchorom a znovu vyhodnotiť 121+18
riadkov. Druhý refinement je zakázaný.

### V3 — presne jeden independent high-precision solve

Rovnaké už zostavené float64 `A_r,b_r` preniesť exaktne do mpmath 80 dps a
vykonať jeden QR least-squares solve. Vyhodnotiť residualy v 80 dps a tiež po
jednom spätnom projekte riešenia do float64. V3 nie je native high-precision
rebuild a nesmie sa tak označiť.

## 4. PASS/REVIEW strom

| Stav | Machine kandidát | Význam |
|---|---|---|
| V0 fail | `REVIEW_KMPC037_REFERENCE_OR_REGRESSION_UNCLOSED` | V1–V3 neinterpretovať |
| V2 correction `>1e-14` alebo lower/anchor/holdout regresia | `REVIEW_KMPC037_REFINEMENT_OUT_OF_BOUNDS` | žiadny provenance PASS |
| V2 uzavrie 121+18 a V3 to potvrdí | `PASS_M1_ORDER7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY` | hlavný audit smie uzavrieť order-7 provenienciu |
| V2 neuzavrie, V3 uzavrie bez regresie | `PASS_M1_ORDER7_FLOAT64_ROUNDING_FLOOR_CANDIDATE_ONLY` | hlavný audit smie uzavrieť order-7 provenienciu |
| V3 same-matrix residual invariantne ostane nad prahom | `REVIEW_M1_ORDER7_SAME_MATRIX_BOUNDARY_UNCLOSED` | nový V4 native rebuild prereg, nie ďalší solve tu |
| exception/timeout/dependency/JSON/publish | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` | error ledger, verdict bez zmeny |

Script nevydáva autoritatívny PASS/REVIEW/STOP. `SCORE_EFFECT=NONE`,
`PREDICTION_TABLE_EFFECT=NONE`, `RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`.

## 5. Očakávania podľa AR54

- V0: presná scope/parity zhoda a pôvodný KMPC-036 REVIEW pattern v
  zmrazených regresných hraniciach;
- V1: backward error kompatibilný s float64 floorom; presná hodnota
  `NEZNÁME/EXPLORATORY`;
- V2: audítorská hypotéza `max correction≈6.52e-16`, ale autoritatívny cap
  ostáva `1e-14`;
- V2/V3: hypotéza, že všetky tri otvorené riadky prejdú bez lower/holdout
  regresie; nie je to predpridelený verdict;
- ak hypotéza neprejde, prahy sa nemenia a vznikne V4/formulačný nástupca.

## 6. Python preflight a negatívne fixtures

Pred auditom musia postupne prejsť: compile base, compile runner, `--help`,
dependency/API smoke, JSON serializačný smoke a behaviorálny smoke. Smoke
musí odmietnuť wrong prerequisite hash, zmenu prahu, reordered state/power,
missing/duplicate row, missing anchor, druhý refinement, nesprávne dps,
neserializovateľný scalar, chýbajúci runtime vstup a publish kolíziu.

Runner musí:

- kontrolovať všetky zdrojové a runtime hashe pred importom;
- odmietnuť existujúci success/failure/temp output pred drahým solve;
- používať exclusive atomic publish s cleanupom vo `finally`;
- exportovať Python/NumPy/mpmath/platform/BLAS metadata;
- pri technickej chybe zapísať poslednú fázu a nevydávať fyzikálny verdict.

## 7. Nonclaims

Bez native high-precision rebuild, CDI support step 3, `[0,9]`, BI/NID/NIV,
iných `k`/variantov, S-M, ODE, finite opacity, full hierarchy, G8/G9,
CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 8. Zmrazené implementačné artefakty

- base:
  `scripts/baseScripts/p5_general_synchronous/m1_order7_numerical_refinement.py`,
  SHA-256
  `CE29222FCE45DAA99A7B8E1FFCC06E9471D648A2B61C14DA05F653DBA9E7A80C`;
- runner:
  `scripts/281_script_KMPC_037_P5_3g7_M1_order7_numerical_refinement_boundary_closure.py`,
  SHA-256
  `272071C28488B4F81D4504EAD73C46FB454BB2A950B9A77AEDDC8338A23242E9`;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_037_P5_3G7_M1_ORDER7_NUMERICAL_REFINEMENT.json`.

Používateľ 2026-07-18 explicitne zrušil odklad do 2026-07-24 a povolil
pokračovať vo výpočte. Povolenie nemení zmrazený rozsah ani PASS/REVIEW strom.
