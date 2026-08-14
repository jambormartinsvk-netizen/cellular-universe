# KMPC-125 — C2 NIV/k=.15 wider-support same-matrix: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_NO_VERDICT / DO_NOT_RUN`  
**Ordering prerequisite:** KMPC-122 SHA
`BAC68E1D85802852EEBF4B1AC2E277EC15FD32264E166F673D486FD747869419`

## Dôvod a presná otázka

KMPC-122 uzavrel nominal audit core na tej istej matici, ale tail vyžadoval
`[-1,6]→[-1,8]`. KMPC-123 ukázal, že fresh accepted `[-1,6]` solve má
vlastnú M3 driver hranicu `fuel_Euler[6]=1.4819148859e-10`; preto checkpoint
ostal `checkpoint_complete=false`. KMPC-124 ho správne odmietol pred
fyzikou.

KMPC-125 sa nepokúša obísť checkpoint guard. Je to nový úplný fyzikálny
beh, ktorý priamo testuje widened accepted `[-1,6]`, audit `[-1,8]`, M1
depth 8 a aplikuje presne tri residual corrections na každú práve riešenú
M3 maticu bez zmeny jej entries alebo pravej strany.

## Zmrazený kontrakt

- byteovo nezmenený `c2_cdi_k0p15_same_matrix_refinement.py` SHA
  `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6`;
- `mode=NIV`, `k=.15`, accepted `[-1,6]`, audit `[-1,8]`, M1 depth 8;
- ordering prerequisite ostáva posledný platný fyzikálny raw KMPC-122;
  incomplete checkpoint KMPC-123 nie je runtime prerequisite;
- presne tri corrections, exact same matrix/constant, nezhoršený absolute
  fallback residual, rank exact a deterministic single-thread;
- holdout riadky `Einstein_00/0i` sa nesmú pridať do driver solve;
- frozen prahy: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`,
  absolute fallback/background `1e-12`;
- equation builder, surfaces, 13-state order a C1 prerequisites sa nemenia.

## Predregistrované rozhodovanie

1. source/prerequisite/owner/provenance fail → technický incident bez
   fyzikálneho verdiktu;
2. accepted alebo audit driver po troch corrections ostane false →
   `REVIEW_C2_NIV_K0p15_WIDER_SUPPORT_NUMERICAL_BOUNDARY`;
3. independent holdout false →
   `REVIEW_C2_NIV_K0p15_INDEPENDENT_HOLDOUT_BOUNDARY`;
4. core/common prejdú a tail ostane false →
   `REVIEW_C2_NIV_K0p15_SUPPORT_08_10_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. C2 `9/10→10/10`, uzavretie NIV módu a ďalšiu
route povoľuje až interný audit.

## Scope a exekúcia

- compile → help → smoke → presne jeden official atom;
- interný runtime `4.8 s`, vonkajší procesný limit `30 s`;
- žiadny checkpoint restore ani guard bypass;
- S-M, ODE/P5.4, G8/G9 a dáta sú mimo scope;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 369:
  `scripts/369_script_KMPC_125_P5_3g7_C2_NIV_k0p15_support_06_08_same_matrix_refinement.py`;
- runner SHA-256:
  `B6BA5BB416AB8E113796A8D4B6C9EC30110E1D07ED64826F9BDEB32302A5F03C`;
- source contract `18` položiek, prerequisite contract `6` položiek;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_125_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_SAME_MATRIX_REFINEMENT.json`;
- output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 369 spustený cez Python.
Od tohto bodu je immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke exit 0; official exit 2 po výpočte na post-processing `KeyError('same_matrix_refinement')` | `PF-115 / NO_VERDICT` |
| 2026-07-19 | failure raw SHA `1ED339AE9FBA7BA27C066A659926B0B822029F8BC3CF0AE4844DF4845E3A31D0`; success raw nevznikol | `IMMUTABLE_TECHNICAL_FAILURE` |
| 2026-07-19 | príčina: base refinoval iba rank 104, widened audit rank 130 nemal provenance field | `DO_NOT_RUN / VERSIONED_MULTI_RANK_SUCCESSOR_REQUIRED` |
