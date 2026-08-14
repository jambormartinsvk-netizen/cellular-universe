# KMPC-076 — C2 BI/k=.005 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / REVIEW_TAIL_SUPPORT_EXTENSION`  
**Poradový prerequisite:** KMPC-075 SHA
`19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9`

Jediný atóm je `BI/k=.005/nominal`. Candidate/audit support je pôvodný C1
rozsah `[0,5]→[0,7]`, M1 depth 7, common `0…5`, tail `6,7`. Výsledok CDI
sa fyzikálne neprenáša; KMPC-075 je iba nemenný poradový prerequisite.

Plochy a prahy ostávajú `z=1e-4,.01`, common `1e-8`, tail `1e-6`, absolute
fallback/background `1e-12`, M1 driver `1e-10`, holdout `1e-9`. Bez zmeny
rovníc, supportu, prahov, `rcond`, korekčného vektora alebo agregácie.

PASS candidate:
`PASS_C2_BI_K0p005_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`. Tail-only FAIL
otvorí `[0,7]→[0,9]`; M1 driver-only numerická hranica smie otvoriť iba
samostatne predregistrovaný same-matrix refinement; ostatný REVIEW sa vetví
podľa zmrazeného C2 stromu. Bez zmeny K4 skóre, release alebo Zenodo triggera.

Použije sa nezmenený adapter `c2_single_atom_adapter.py` SHA
`C018ACB17311A8CB522FB612AB0EDD1DD5B9C47E16DC5D915A5F6DAF4204BAF8`
a nový tenký runner 320. Raw:
`RUN_KMPC_076_P5_3G7_C2_BI_K0p005_NOMINAL.json`.

Zmrazený SHA-256 runnera 320:
`5410B74F3B6D0E87A82D8DAB9C723B67307E7459B2A0A578E4F560EEF6982159`.
Harness SHA-256:
`735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | identita, support, hĺbka, prahy, prerequisite a vetvenie zmrazené pred vytvorením runnera | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | runner a source chain hashovo zmrazené; cieľ aj failure raw neprítomné | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile/help/smoke PASS; official M1/core/common/background PASS, M3 tail FAIL pri `z=.01`; raw SHA `B053B523...4FCA00` | `IMMUTABLE / REVIEW_SUPPORT_07_09_REQUIRED` |
