# KMPC-062 — C2 AD/k=.005 support `[0,4]→[0,6]`: predregistrácia

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C2 → AD/k=.005/nominal`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Prerequisite:** KMPC-061 SHA `0952AF08B1DE291D015F71396954F70EAE2F78A962E1EE1D3A08ECA48A1F5DCD`

## Otázka

Odstráni minimálny support krok z `[0,2]` na `[0,4]` veľký tail `3,4`, ak
sa candidate `[0,4]` porovná s auditom `[0,6]` pri novom M1 depth 6?

## Zmrazený kontrakt

- iba `AD`, `k=0.005 Mpc^-1`, `nominal`;
- regression prerequisite: celý immutable KMPC-061 a jeho candidate REVIEW;
- candidate/audit support: `[0,4]→[0,6]`;
- M1 depth `6`; žiadny correction vector;
- common powers `0…4`; added tail iba `5,6`;
- `z=1e-4,1e-2`; common `1e-8`, tail `1e-6`, absolute fallback `1e-12`;
- background relative `1e-12`; všetky frozen R-A/B1/TCA0/S-C0/core brány;
- jeden official proces, internal `4.8 s`, external `10 s`, immutable JSON.

## Rozhodovací strom

- technická chyba → bez fyzikálneho verdiktu;
- M1/core/common failure → REVIEW príslušnej brány;
- tail `5,6` failure → `REVIEW_C2_AD_K0p005_FURTHER_SUPPORT_EXTENSION_REQUIRED`;
- background failure → kandidát na STOP background mapy, vyžaduje nezávislú reprodukciu;
- všetko PASS → `PASS_C2_AD_K0p005_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY` a
  až potom možno predregistrovať AD/`.15`.

Bez skóre, release a prediction triggera. Bez zvyšných deviatich C2 atómov,
C3, S-M, hierarchy alebo ODE.

## Artefakty

- base: `scripts/baseScripts/p5_general_synchronous/c2_ad_k0p005_support_04_06.py`;
- runner: `scripts/306_script_KMPC_062_P5_3g7_C2_AD_k0p005_support_04_06.py`;
- raw: `RUN_KMPC_062_P5_3G7_C2_AD_K0p005_SUPPORT_04_06.json`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | otázka, support/depth, prahy, stop strom a jediný atóm zmrazené | `PREREGISTERED` |
| 2026-07-18 | base SHA `EFE65B1BEE946EE531A6757F95CAFB103EE8D1320FB363009F624A69156EEFC8`; thin runner SHA `0A0D8379A44BC74701592BE85B62D0241AF21F36CF5ED35CB82F1DDF5AA39CF5`; stabilný harness nezmenený; žiadny KMPC-062 output | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile/help/smoke PASS; official exit `0`; raw SHA `640057CB6AC3F059988D6BD6C0CBE65ABAC1712F18961A2FEAFA5E1341EA6760`; core/common/background PASS, tail `5,6` FAIL iba na `z=.01` | `REVIEW_C2_AD_K0p005_FURTHER_SUPPORT_EXTENSION_REQUIRED` |
