# KMPC-145 — C3 NID/.15 read-only parity-scope correction

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.15`  
**Stav:** `PREREGISTERED / INPUT_AND_SOURCE_HASH_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Technický predchodca:** `KMPC-144 / PF-128 / interný audit 229`  
**Východiskový register:** NID `8/9`, globálne C3 `38/45`, K4 `60/100`.

## 1. Presný problém

KMPC-144 úspešne znížil af0 audit M3 driver z `4.1866e-10` na
`1.3514e-16`; oba varianty majú všetky fyzikálne brány true. Pair ostal
REVIEW iba pre dve false parent parity checks:

- `af0_accepted_exact_predecessor_parity` — in-memory integer power keys
  boli porovnané s JSON string keys, hoci JSON-semantické subtrees sú exact;
- `gamma0_variant_exact_predecessor_parity` — celý objekt zahŕňal runtime a
  nový pravdivý provenance check, hoci vedecká projekcia je exact.

Source raw je
`RUN_KMPC_144_P5_3G7_C3_NID_K0p15_AF0_AUDIT_SAME_MATRIX_REFINEMENT.json`,
SHA `7288ADE2BBC876D5F26677186ACF37BD3FE6B6DC439458C90A640B1C8FD103EB`.
Fyzikálny predchodca KMPC-131 má SHA
`3850A3D951E5A8A3E21C93A6DAE7F1A08CBE6430E7100BD01B75F573F21AF71B`.

## 2. Jediná povolená read-only transformácia

KMPC-145 nesmie volať worker, solver, CPQR, maticový builder ani fyzikálnu
funkciu. Smie iba:

1. hashovo načítať oba immutable rawy;
2. vyžadovať source run KMPC-144, pair/refinement false a presnú false
   množinu dvoch vyššie uvedených parity checks;
3. vyžadovať všetky ostatné refinement checks a všetky fyzikálne brány true;
4. porovnať af0 accepted ako dva už JSON-kanonizované objekty;
5. pri gamma0 odstrániť z oboch projekcií iba runtime a z nového rawu iba
   `af0_audit_refinement_contract=true`, potom vyžadovať exact equality;
6. nastaviť iba dve parity checks a odvodené
   `same_matrix_refinement_audit.pass`, `same_matrix_refinement_pass`,
   `pair_pass`, candidate, run/test identitu;
7. publikovať protected-snapshot SHA pred/po a `0` worker/solver/CPQR calls.

Protected snapshot zahŕňa celé varianty, coefficienty, residualy, holdout,
common, tail, null, bridge, support, M1, prahy, source hashe a refinement
provenance. Vylúčené sú iba explicitne menené odvodené polia a nový
read-only audit blok.

## 3. Rozhodovacie vetvy

- všetky input/parity/protected checks true a pair true:
  `PASS_C3_NID_K0P15_PARITY_SCOPE_CORRECTION_CANDIDATE_ONLY`;
- presná false množina, semantic parity alebo protected snapshot fail:
  žiadny PASS, NID ostáva `8/9`;
- hash/schema/runtime/write chyba: technical failure bez fyzikálneho
  verdiktu.

Skriptový candidate nie je verdikt. Interný audit musí osobitne overiť
output hash, operation counts, protected snapshot a aktívne brány. Až potom
sa smie NID uzavrieť `9/9` a globálne C3 `39/45`.

## 4. Predregistrovaný postup a output

`compile → help → read-only smoke → read-only official → interný audit`.

Smoke nesmie zapisovať raw a musí mať `physics_executed=false` a
`workers=solvers=cpqr=0`. Official smie vytvoriť iba:

`scripts/results/k_mpc_005/RUN_KMPC_145_P5_3G7_C3_NID_K0p15_PARITY_SCOPE_CORRECTION.json`

alebo príslušný `_TECHNICAL_FAILURE.json`. Ani jeden pred source freeze
neexistoval.

## 5. Source freeze pred prvým KMPC-145 Python behom

| artefakt | SHA-256 |
|---|---|
| KMPC-144 source raw | `7288ADE2BBC876D5F26677186ACF37BD3FE6B6DC439458C90A640B1C8FD103EB` |
| KMPC-131 predecessor raw | `3850A3D951E5A8A3E21C93A6DAE7F1A08CBE6430E7100BD01B75F573F21AF71B` |
| runner `389/KMPC-145` | `871B24D48239A6E860722AAC701F048F3E7717FD45B03EB3A572F9939F55AEDA` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal. Runner sa odteraz nemení.
Po internom PASS sa vytvorí externý auditný balík za celý NID C3 mód.
