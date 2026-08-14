# KMPC-065 — C2 AD/k=.15 smoke-scope successor: predregistrácia

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / REVIEW_SUPPORT_EXTENSION_REQUIRED`  
**Nástupca:** PF-080 / KMPC-064 bez fyzikálneho raw

Jediná povolená zmena je oddelenie dvoch smoke rozsahov. Parent V4 vykoná
svoj pôvodný matrix-wide 10-name smoke mimo atom-local overlaya. Nový smoke
potom osobitne overí AD/k=.15 identity, `[0,2]→[0,4]`, M1 depth 5,
prerequisite KMPC-063, restricted názov, source-hash vlastníctvo a obnovu
ownerov. Audit stále vykoná iba AD/k=.15/nominal.

Fyzika, support, M1, plochy, prahy, rozhodovací strom a nonclaims sú presne
z KMPC-064/doc114. PASS candidate ostáva
`PASS_C2_AD_K0p15_SUPPORT_02_ADEQUATE_CANDIDATE_ONLY`; tail FAIL otvára iba
`[0,4]→[0,6]`. Žiadna agregácia, korekcia ani zmena skóre.

Artefakty: V2 base `c2_ad_k0p15_nominal_v2_smoke_scope.py`, runner 309, raw
`RUN_KMPC_065_P5_3G7_C2_AD_K0p15_NOMINAL.json`.

Zmrazený SHA-256 V2 base:
`44D9F865E4E1513502C00D39F6C6389874A34067B03859B9527B17AFBB2740DC`.
Zmrazený SHA-256 runnera 309:
`882DAE356100A5C06479D64FF156C69467DA12AE0A8298DAFDB24E5AA9A5FCCE`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | jediná technická delta a nezmenený fyzikálny kontrakt zmrazené | `PREREGISTERED` |
| 2026-07-18 | compile/help/smoke PASS; jediný atóm skončil REVIEW; raw SHA `987E467EA2F36EA8F061F665A33AE1F6DC9AB6E2EFE9FB710E23CE0C50171636` | `IMMUTABLE` |
