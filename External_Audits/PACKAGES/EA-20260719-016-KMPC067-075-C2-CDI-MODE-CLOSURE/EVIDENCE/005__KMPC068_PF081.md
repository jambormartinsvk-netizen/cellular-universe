# KMPC-068 — C2 CDI/k=.005 support [0,7]→[0,9]: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PF-081 / TECHNICAL_FAILURE_NO_PHYSICS_VERDICT / DO_NOT_RUN`  
**Poradový prerequisite:** KMPC-067 SHA
`DC11201E7301831153F4D3D5450A95FC1D5F311E5EE3E9176BDE6E471F657F8F`

Jediný atóm je `CDI/k=.005/support_07_09`. Candidate/audit support
`[0,7]→[0,9]`, M1 depth 9, common `0…7`, tail `8,9`. Zachovávajú sa plochy
`z=1e-4,.01` a všetky prahy KMPC-067: common `1e-8`, tail `1e-6`, absolute
fallback/background `1e-12`, M1 driver `1e-10`, holdout `1e-9`. Bez
correction vectora a bez automatickej opravy M1 numerical boundary.

PASS candidate:
`PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`. Tail FAIL pri
core/common PASS otvorí iba `[0,9]→[0,11]`; iný REVIEW sa vetví podľa
zmrazeného C2 stromu. Bez agregácie, skóre alebo triggera.

Použije sa nezmenený adaptér `c2_single_atom_adapter.py`, SHA-256
`C018ACB17311A8CB522FB612AB0EDD1DD5B9C47E16DC5D915A5F6DAF4204BAF8`.
Konfiguráciu a jej poradový prerequisite zmrazí nový tenký runner 312.
Raw: `RUN_KMPC_068_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09.json`.

## Frozen implementation

- adapter SHA-256:
  `C018ACB17311A8CB522FB612AB0EDD1DD5B9C47E16DC5D915A5F6DAF4204BAF8`;
- runner `312_script_KMPC_068_P5_3g7_C2_CDI_k0p005_support_07_09.py`
  SHA-256: `818303B4270A618826076C06C616FF1BA0CB4268F362AD3A6E48525D4CFBF28E`;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

Po zmrazení sa kód nemení; technická chyba je DNR a patrí do Python error
ledgeru.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | identita, support/depth, prahy, prerequisite a vetvenie zmrazené | `PREREGISTERED` |
| 2026-07-19 | runner a zdrojový reťazec hashovo zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile/help/smoke PASS; official atóm prekročil interných 4.8 s; failure SHA `5F7A23E6...57823`; bez canonical raw | `PF-081 / DO_NOT_RUN` |
