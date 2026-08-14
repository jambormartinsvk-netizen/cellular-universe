# KMPC-083 — BI/k=.15 internal-deadline successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / REVIEW_EXACT_ASSEMBLY_REQUIRED`

PF-087 zastavil KMPC-082 pred maticou a solve. KMPC-083 smie zmeniť iba
vnútorný `make_deadline`: smoke prijíma 4.8 s, official 45 s. Po behu sa
owner povinne obnoví. High-precision V1 SHA, 80 dps, jeden solve, support,
rovnice, matice, prahy, holdout non-fit a oba harnessy ostávajú nezmenené.

Prerequisite je KMPC-080 SHA `028BE28F...83DD1F`. Výstup:
`RUN_KMPC_083_P5_3G7_C2_BI_K0p15_HIGH_PRECISION_HOLDOUT_BOUNDARY.json`.
Kandidáty sú identické s KMPC-081/082; PF-087 nemá fyzikálny dopad.

Zmrazené SHA-256:

- V2 deadline overlay:
  `5F3850D68BD0CCD9FCCB7CCE7E31A7C68212417E6C13921B88604D14DD321F7B`;
- runner 327:
  `68D5D64A57DF7D89738E7895773B88088B8608702870BCEBA2EB2490B55BB0D2`;
- high-precision/stable harness:
  `8DBDA083...F1906D` / `735A52A6...20B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | druhá runtime vrstva izolovaná; jediná zmena a owner restore zmrazené | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | V2, runner, oba harnessy a V1 auditný modul hashovo zmrazené | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile/smoke/official dokončené; 80-dps driver PASS, holdout FAIL nezmenený; raw SHA `A8CB50F9...D729C9` | `IMMUTABLE / REVIEW_EXACT_ASSEMBLY_REQUIRED` |
