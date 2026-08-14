# KMPC-066 — C2 AD/k=.15 support `[0,4]→[0,6]`: predregistrácia

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / PASS_CANDIDATE_ONLY`  
**Prerequisite:** KMPC-065 SHA `987E467EA2F36EA8F061F665A33AE1F6DC9AB6E2EFE9FB710E23CE0C50171636`

Jediný atóm je AD/k=.15/nominal. Candidate/audit `[0,4]→[0,6]`, M1
depth 6, common `0…4`, tail `5,6`; prahy a plochy sa nemenia. Bez prenosu
koeficientov alebo correction vectora. Raw M1 boundary sa neopraví.

PASS candidate je `PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`;
tail FAIL pri core/common PASS otvorí iba `[0,6]→[0,8]`. Iný REVIEW sa
vetví podľa frozen C2 stromu. Bez agregácie, skóre alebo triggera.

Artefakty: base `c2_ad_k0p15_support_04_06.py`, runner 310, raw
`RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json`.

Zmrazený SHA-256 base: `7A52C7940EBCD70EC727EC4AB014620A64EC7BAE3C22FB556ED6C2C98C10D688`.
Zmrazený SHA-256 runnera 310: `713773B5E3A09B0DF3B87AA10343EE20060D8FB74548D3BFEB9A96CEBA1F1544`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | identita, support/depth, prahy a vetvenie zmrazené | `PREREGISTERED` |
| 2026-07-18 | compile/help/smoke PASS; jediný atóm PASS; raw SHA `81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816` | `IMMUTABLE` |
