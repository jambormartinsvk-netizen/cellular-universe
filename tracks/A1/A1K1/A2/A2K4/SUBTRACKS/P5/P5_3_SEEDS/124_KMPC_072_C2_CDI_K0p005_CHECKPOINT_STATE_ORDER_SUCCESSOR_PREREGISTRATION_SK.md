# KMPC-072 — C2 CDI/k=.005 checkpoint state-order successor

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PF-084 / TECHNICAL_SMOKE_FAILURE / DO_NOT_RUN`  
**Nástupca:** PF-083 / KMPC-071 raw sa nepoužíva fyzikálne  

Jediná povolená zmena je pri načítaní checkpointu rekonštruovať top-level
`standard_state` presne v poradí `full_ra_contract.AUTHORITATIVE_STATE` a
fail-closed overiť rovnosť celého tuple v smoke. Vnútorné power keys sa naďalej
obnovujú na integer. Všetky hodnoty ostávajú nezmenené.

Použije sa rovnaký immutable checkpoint KMPC-070 SHA
`AD8CD12F5E6CBABE28C512DFDA6D3867C3E713F5582E152F6289CD78540A7D00`,
rovnaký ordering prerequisite KMPC-067, rovnaký single-thread backend a presný
limit `4.8 s`. Fyzika, `[0,7]→[0,9]`, M1 depth 9, plochy, prahy a vetvenie sa
nemenia.

PASS candidate:
`PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`. Tail-only FAIL
otvorí iba `[0,9]→[0,11]`. Bez agregácie, skóre alebo triggera.

Artefakty: versioned overlay `c2_checkpointed_single_atom_v2_state_order.py`,
runner 316 a raw
`RUN_KMPC_072_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_STATE_ORDER_SUCCESSOR.json`.

Zmrazené SHA-256:

- V1 checkpoint base:
  `76B707973FA285733AFF61A8A931A51D4C09D249D1F6CB983758C09F0F0D05CF`;
- V2 state-order overlay:
  `7B41EC182ED87597A7719CC3AF9632CEC92BA9E7AC411C6EE5A724EC1A02F3D7`;
- runner 316:
  `AE9EEDE711DA85558591A0D1C01BFB8633D63904BB771C3213E02BD90BE8169C`;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | jediná order-provenance delta a nezmenená fyzika zmrazené | `PREREGISTERED` |
| 2026-07-19 | overlay, runner a zdrojový reťazec hashovo zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile/help PASS; smoke odhalil chybný 13-state očakávaný rozsah pre 11-state checkpoint; bez auditu/raw | `PF-084 / DO_NOT_RUN` |
