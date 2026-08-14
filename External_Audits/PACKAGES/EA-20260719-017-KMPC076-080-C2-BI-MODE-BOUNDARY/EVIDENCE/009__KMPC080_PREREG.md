# KMPC-080 — C2 BI/k=.15 same-matrix refinement: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `FROZEN / NOT_RUN`  
**Prerequisite:** KMPC-079 SHA
`014B3F7E76929ED7C3DC894C8B84550AB68435BF7BC2A650788801D786D4A5E5`

KMPC-079 uzavrel všetky brány okrem auditnej M3 driver precision:
`gamma_Euler[7]` má relatívne rezíduum `3.227055158031955e-9 > 1e-10`.
KMPC-080 smie na presne tej istej 104×104 matici a konštante vykonať presne
tri residual corrections. Nesmie meniť rovnice, support `[0,5]→[0,7]`,
M1 depth 7, `rcond`, prahy ani vyberať inú maticu.

Výber refined riešenia je dovolený iba ak je konečná, zlepší maximum
relatívneho rezídua a nezhorší maximum absolute-fallback rezídua. Potom sa
všetky frozen brány prepočítajú z vybratej riešenia. PASS candidate:
`PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Použije sa už auditovaný konfigurovateľný same-matrix engine
`c2_cdi_k0p15_same_matrix_refinement.py` SHA
`EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6`.
Historické `cdi` v názve nemení scope: engine prijíma identitu z adaptera a
neobsahuje CDI špecifickú rovnicu. Nový runner 324 a raw
`RUN_KMPC_080_P5_3G7_C2_BI_K0p15_SAME_MATRIX_REFINEMENT.json`.

Zmrazený SHA-256 runnera 324:
`2B4C89AA644997EFC3566BEA6846CF1609E11F88AE3F9691C20C5FC4E3014F05`.
Harness SHA-256:
`735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | matrix/constant identity, tri corrections, selection rule, prahy a kandidát zmrazené | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | runner a lineage hashovo zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
