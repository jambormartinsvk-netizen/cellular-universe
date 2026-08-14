# KMPC-074 — C2 CDI/k=.15 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / REVIEW_CORE_M3_DRIVER`  
**Poradový prerequisite:** KMPC-073 SHA
`B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498`

Jediný atóm je `CDI/k=.15/nominal`. Candidate/audit support je pôvodný C1
rozsah `[0,5]→[0,7]`, M1 depth 7, common `0…5`, tail `6,7`. Support `[0,7]`
z k=.005 sa neprenáša; oba k-body sa testujú nezávisle.

Plochy a prahy ostávajú `z=1e-4,.01`, common `1e-8`, tail `1e-6`, absolute
fallback/background `1e-12`, M1 driver `1e-10`, holdout `1e-9`. Bez
correction vectora a bez automatickej opravy M1 boundary.

PASS candidate:
`PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`. Tail-only FAIL
otvorí `[0,7]→[0,9]`; iný REVIEW sa vetví podľa frozen C2 stromu. Bez
agregácie, skóre alebo triggera.

Použije sa nezmenený adapter `c2_single_atom_adapter.py` SHA
`C018ACB17311A8CB522FB612AB0EDD1DD5B9C47E16DC5D915A5F6DAF4204BAF8`
a nový tenký runner 318. Raw:
`RUN_KMPC_074_P5_3G7_C2_CDI_K0p15_NOMINAL.json`.

Zmrazený SHA-256 runnera 318:
`80DD26260AC5A6F1F53F45B5280AEDD4597BA645A09B8D1A87328FC8FBB0FB67`.
Harness SHA-256:
`735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | identita, nezávislý support, prahy, prerequisite a vetvenie zmrazené | `PREREGISTERED` |
| 2026-07-19 | runner a source chain hashovo zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile/help/smoke PASS; official M1/common/tail/background PASS, audit M3 driver FAIL; raw SHA `7771610F...BB1A0` | `IMMUTABLE / REVIEW_CORE` |
