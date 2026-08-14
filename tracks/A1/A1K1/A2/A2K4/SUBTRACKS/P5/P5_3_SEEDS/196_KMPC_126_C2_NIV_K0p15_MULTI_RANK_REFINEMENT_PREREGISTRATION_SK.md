# KMPC-126 — C2 NIV/k=.15 multi-rank refinement: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / PASS_CANDIDATE`  
**Vstupný stav:** C2 `9/10 PASS`, K4 `LIVE / 60/100`, technický counter `2/10`

## Dôvod a presná otázka

PF-115 ukázal, že historická same-matrix vrstva refinovala iba rank 104.
Pri widened ladderi má accepted M3 rank 104 a audit M3 rank 130; audit preto
nemal provenance field a KMPC-125 fail-closed bez success raw.

KMPC-126 testuje ten istý úplný widened atóm ako KMPC-125, ale versioned
successor explicitne refinovaním pokrýva oba a iba frozen ranky `{104,130}`
a publikuje samostatnú accepted/audit provenance.

## Zmrazený versioned successor

`c2_same_matrix_refinement_v2_multi_rank.py` SHA-256:
`1E2600C366590B7FC56289D1FBC386EF24DA50DA9ED5686AE5FB5A50E0992F08`.

Successor:

- povoľuje iba accepted `[-1,6]`, audit `[-1,8]`, M1 depth 8;
- volá byteovo nezmenený original solver a rovnakú trojkrokovú residual
  correction funkciu predchodcu;
- refinovaním pokrýva iba `expected_rank=104` a `130`; iné ranky deleguje
  bez zmeny;
- nemení matrix, constant, support, equation builder, rcond, prahy ani
  holdout definíciu;
- smoke musí behaviorálne prejsť samostatný rank-104 aj rank-130 fixture;
- official musí mať exact same-matrix provenance pre accepted aj audit.

## Zmrazený fyzikálny kontrakt

- `mode=NIV`, `k=.15`, accepted `[-1,6]`, audit `[-1,8]`, M1 depth 8;
- ordering prerequisite je posledný platný fyzikálny raw KMPC-122 SHA
  `BAC68E1D85802852EEBF4B1AC2E277EC15FD32264E166F673D486FD747869419`;
- KMPC-123 incomplete checkpoint ani KMPC-125 failure raw nie sú runtime
  prerequisites;
- presne tri corrections na každom target ranku, exact same matrix/constant,
  nezhoršený absolute fallback residual a exact rank;
- driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`, absolute
  fallback/background `1e-12`; žiadne uvoľnenie;
- holdout riadky sa nesmú dostať do driver solve.

## Predregistrované rozhodovanie

1. source/prerequisite/rank fixture/owner/provenance fail → technický
   incident bez fyzikálneho verdiktu;
2. accepted alebo audit driver po corrections false →
   `REVIEW_C2_NIV_K0p15_MULTI_RANK_NUMERICAL_BOUNDARY`;
3. independent holdout false →
   `REVIEW_C2_NIV_K0p15_INDEPENDENT_HOLDOUT_BOUNDARY`;
4. core/common prejdú a tail false →
   `REVIEW_C2_NIV_K0p15_SUPPORT_08_10_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. C2 `9/10→10/10`, uzavretie NIV módu a ďalšiu
route povoľuje až interný audit.

## Scope a exekúcia

- compile → help → smoke → presne jeden official atom;
- interný runtime `4.8 s`, vonkajší procesný limit `30 s`;
- S-M, ODE/P5.4, G8/G9 a dáta sú mimo scope;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 370:
  `scripts/370_script_KMPC_126_P5_3g7_C2_NIV_k0p15_support_06_08_multi_rank_refinement.py`;
- runner SHA-256:
  `6AF0F54BD7D92E5730898A82B024BE1D6F932B879D974AB7EB47F47E5522EAF9`;
- source contract `19` položiek, prerequisite contract `6` položiek;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json`;
- output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 370 ani nový base
successor spustený cez Python. Od tohto bodu sú immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke PASS vrátane rank 104/130 fixtures | `PREFLIGHT_PASS` |
| 2026-07-19 | official exit 0, internal runtime `4.156 s`; raw SHA `1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0` | `IMMUTABLE / PASS_CANDIDATE` |
| 2026-07-19 | interný audit dokument 197 prijal scoped NIV/.15 PASS a uzavrel NIV mód | `AUTHORITATIVE_SCOPED_PASS` |
