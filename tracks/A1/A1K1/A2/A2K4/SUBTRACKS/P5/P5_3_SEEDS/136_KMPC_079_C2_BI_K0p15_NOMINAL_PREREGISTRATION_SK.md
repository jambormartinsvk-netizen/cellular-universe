# KMPC-079 — C2 BI/k=.15 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / REVIEW_CORE_M3_DRIVER`  
**Poradový prerequisite:** KMPC-078 SHA
`F24894A043B531825DD36A424637D1E70244F89B66678AF945EA6C135918A359`

Jediný atóm je `BI/k=.15/nominal`. Candidate/audit support je nezávislý C1
rozsah `[0,5]→[0,7]`, M1 depth 7, common `0…5`, tail `6,7`. Support ani
checkpoint z k=.005 sa neprenášajú.

Plochy a prahy ostávajú `z=1e-4,.01`, common `1e-8`, tail `1e-6`, absolute
fallback/background `1e-12`, M1 driver `1e-10`, holdout `1e-9`. Bez zmeny
rovníc, `rcond`, korekčného vektora alebo agregácie.

PASS candidate:
`PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`. Tail-only FAIL
otvorí `[0,7]→[0,9]`; M1 driver-only hranica iba samostatný same-matrix
refinement; ostatný REVIEW podľa frozen C2 stromu. Bez zmeny skóre alebo
release triggera.

Použije sa nezmenený adapter SHA
`C018ACB17311A8CB522FB612AB0EDD1DD5B9C47E16DC5D915A5F6DAF4204BAF8`
a nový runner 323. Raw:
`RUN_KMPC_079_P5_3G7_C2_BI_K0p15_NOMINAL.json`.

Zmrazený SHA-256 runnera 323:
`9AD3F44FA14EEB6688568FB101ABE925DF385A807FB99EBC022D0DD60AC9F7E5`.
Harness SHA-256:
`735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | identita, nezávislý support, prahy, prerequisite a vetvenie zmrazené | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | runner a lineage hashovo zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile/smoke PASS; official tail/common/M1/background PASS, audit M3 driver FAIL; raw SHA `014B3F7E...D4A5E5` | `IMMUTABLE / REVIEW_CORE` |
