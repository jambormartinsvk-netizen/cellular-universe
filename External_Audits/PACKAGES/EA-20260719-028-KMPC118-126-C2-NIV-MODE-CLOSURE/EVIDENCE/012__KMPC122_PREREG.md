# KMPC-122 — C2 NIV/k=.15 same-matrix refinement: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / CORE_CLOSED_TAIL_REVIEW`  
**Prerequisite:** KMPC-121 SHA
`8E5E8107833C9F2858BA180F9DBC3DFA4037566CCC2F7D30AF819B1FC94C0BEE`

## Dôvod a jediná otázka

KMPC-121 prešiel M1, accepted solve, common, S-C0, background a independent
holdout. Audit `[-1,6]` zlyhal v core iba na `M3_driver`:
`fuel_Euler[6]=1.6254166022e-10 > 1e-10`; rank je `104/104` a holdout
maximum `2.2333405929e-12 < 1e-9`. Tail je osobitne false a v tomto kroku
sa nesmie zamiešať do core rozhodnutia.

KMPC-122 testuje, či tri predregistrované residual corrections na presne
tej istej 104×104 matici a pravej strane znížia driver pod `1e-10` bez
zmeny rovnice, supportu, `rcond`, prahu alebo holdout definície.

## Zmrazený kontrakt

- byteovo sa znovupoužije auditovaný konfigurovateľný modul
  `c2_cdi_k0p15_same_matrix_refinement.py`;
- `mode=NIV`, `k=.15`, accepted `[-1,4]`, audit `[-1,6]`, M1 depth 6;
- presne tri corrections; selection rule musí zlepšiť relative residual a
  nesmie zhoršiť absolute-fallback residual;
- matrix/constant identita musí byť `EXACT_SAME_MATRIX_AND_CONSTANT`;
- deterministic single-thread prostredie je povinné;
- driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`, absolute
  fallback/background `1e-12`; nič sa neuvoľňuje;
- žiadny holdout riadok sa nepridáva do driver solve.

## Predregistrované rozhodovanie

1. source/prerequisite/owner/provenance fail → technický incident bez
   fyzikálneho verdiktu;
2. driver ostane false →
   `REVIEW_C2_NIV_K0p15_SAME_MATRIX_NUMERICAL_BOUNDARY`;
3. driver prejde, ale independent holdout zlyhá →
   `REVIEW_C2_NIV_K0p15_INDEPENDENT_HOLDOUT_BOUNDARY`;
4. core/common prejdú a frozen tail ostane false →
   `REVIEW_C2_NIV_K0p15_SUPPORT_06_08_REQUIRED`;
5. všetky frozen brány prejdú →
   `PASS_C2_NIV_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. Ani úspešné uzavretie core samo nezvyšuje C2,
ak tail ostane false. K4 zostáva `60/100`.

## Implementácia zmrazená pred prvým Python behom

- runner 366:
  `scripts/366_script_KMPC_122_P5_3g7_C2_NIV_k0p15_same_matrix_refinement.py`;
- runner SHA-256:
  `3DCA712EDDEAB94BB21B9AEAADB61401BB5CF4B07BACF475B2F5470A87AA4F8A`;
- same-matrix base SHA-256:
  `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6`;
- source contract `18` položiek, prerequisite contract `6` položiek;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_122_P5_3G7_C2_NIV_K0p15_SAME_MATRIX_REFINEMENT.json`;
- output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 366 spustený cez Python.
Od tohto bodu je immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke/official exit 0; raw SHA `BAC68E1D85802852EEBF4B1AC2E277EC15FD32264E166F673D486FD747869419` | `IMMUTABLE_RESULT` |
| 2026-07-19 | driver `1.62542e-10→1.51686e-16`, holdout PASS; tail-only REVIEW | `CORE_CLOSED / SUPPORT_06_08_REQUIRED` |
| 2026-07-19 | KMPC-126 widened multi-rank successor uzavrel support | `REVIEW_CONSUMED / HISTORY_PRESERVED` |
