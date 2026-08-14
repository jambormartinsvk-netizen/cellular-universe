# KMPC-064 — C2 AD/k=.15 nominal: predregistrácia

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT / DO_NOT_RUN`  
**Poradový prerequisite:** KMPC-063 SHA `CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD`

Jediný atóm je `AD/k=.15/nominal`. Atom-local candidate/audit support je
pôvodný C1 rozsah `[0,2]→[0,4]`, M1 depth 5, common `0…2`, tail iba `3,4`.
Support `[0,6]` z k=.005 ani žiadny correction vector sa neprenáša.

Zmrazené plochy sú `z=1e-4,.01`; prahy common `1e-8`, tail `1e-6`,
absolute fallback/background `1e-12`, M1 driver `1e-10` a holdout `1e-9`.
Raw M1 numerical boundary sa neopraví automaticky.

Úplný PASS má candidate
`PASS_C2_AD_K0p15_SUPPORT_02_ADEQUATE_CANDIDATE_ONLY`. Tail FAIL pri
core/common PASS otvorí iba nový `[0,4]→[0,6]` support krok. Iný core alebo
M1 REVIEW sa spracuje podľa frozen C2 stromu. Bez iných atómov, agregácie,
zmeny skóre alebo release triggera.

Artefakty: base `c2_ad_k0p15_nominal.py`, runner 308, raw
`RUN_KMPC_064_P5_3G7_C2_AD_K0p15_NOMINAL.json`.

Zmrazený SHA-256 base:
`3B2AA532B3EC77D89EE45C4831A287A4F8D50D5AE58736AD37EFF321045379F0`.
Zmrazený SHA-256 runnera 308:
`0D81CD77B80CC5684395C43BACEF132B17945F12CED67FC6DF68DBEEAFD20DD8`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | identita, support/depth, prahy, prerequisite a rozhodovací strom zmrazené | `PREREGISTERED` |
| 2026-07-18 | compile/help PASS; smoke odmietol restricted atom name počas legacy 10-name fixture; PF-080; bez raw | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` |
