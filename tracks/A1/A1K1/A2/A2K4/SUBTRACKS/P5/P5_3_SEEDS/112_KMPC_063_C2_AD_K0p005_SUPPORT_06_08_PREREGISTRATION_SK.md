# KMPC-063 — C2 AD/k=.005 support `[0,6]→[0,8]`: predregistrácia

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / PASS_CANDIDATE_ONLY`  
**Prerequisite:** KMPC-062 SHA `640057CB6AC3F059988D6BD6C0CBE65ABAC1712F18961A2FEAFA5E1341EA6760`

Jediný atóm je `AD/k=.005/nominal`. Candidate/audit `[0,6]→[0,8]`, M1
depth 8, common `0…6`, tail iba `7,8`. Prahy a plochy ostávajú common
`1e-8`, tail `1e-6`, absolute fallback/background `1e-12`,
`z=1e-4,.01`. Prenos correction vectora je zakázaný.

Raw M1 numerical boundary sa neopraví automaticky. Core/common/tail alebo
background sa vetvia rovnako ako KMPC-062. Úplný PASS má candidate
`PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`; tail FAIL otvorí
iba ďalší predregistrovaný `[0,8]→[0,10]` krok. Bez iných C2 atómov a bez
zmeny skóre/triggers.

Artefakty: base `c2_ad_k0p005_support_06_08.py`, runner 307, raw
`RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json`.

Zmrazený SHA-256 base:
`BA940220B1CDFCF155FF5ABE274B48391477EB6C6F255A7DCAC706F9DF55193E`.
Zmrazený SHA-256 runnera 307:
`1FC34ADD98947B9290CA3002910CAB4B6B6F0684CE54428428E7EB88ACA3A658`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | support/depth, prahy, prerequisite a rozhodovací strom zmrazené | `PREREGISTERED` |
| 2026-07-18 | compile, help a smoke prešli; smoke nevytvoril raw | `PREFLIGHT_PASS` |
| 2026-07-18 | jediný AD/k=.005 atóm skončil PASS; raw SHA `CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD` | `IMMUTABLE` |
