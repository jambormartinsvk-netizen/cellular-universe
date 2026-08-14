# KMPC-067 — C2 CDI/k=.005 nominal: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / REVIEW_SUPPORT_07_09_REQUIRED`  
**Poradový prerequisite:** KMPC-066 SHA `81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816`

Jediný atóm je `CDI/k=.005/nominal`. Candidate/audit support `[0,5]→[0,7]`,
M1 depth 7, common `0…5`, tail `6,7`. Plochy `z=1e-4,.01`; prahy
common `1e-8`, tail `1e-6`, absolute fallback/background `1e-12`, M1
driver `1e-10`, holdout `1e-9`. Bez correction vectora a bez automatickej
opravy M1 numerical boundary.

PASS candidate: `PASS_C2_CDI_K0p005_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.
Tail FAIL pri core/common PASS otvorí iba `[0,7]→[0,9]`; iný REVIEW sa
vetví podľa frozen C2 stromu. Bez agregácie, skóre alebo triggera.

Prvýkrát sa použije stabilný, fyziku neobsahujúci konfigurovateľný adaptér
`c2_single_atom_adapter.py`. Konfigurácia je hashovaná priamo v runneri 311;
adaptér sa po každom smoke/audit behu musí obnoviť na pôvodných owneroch.
Raw: `RUN_KMPC_067_P5_3G7_C2_CDI_K0p005_NOMINAL.json`.

## Frozen implementation

- adapter: `c2_single_atom_adapter.py`, SHA-256
  `C018ACB17311A8CB522FB612AB0EDD1DD5B9C47E16DC5D915A5F6DAF4204BAF8`;
- runner: `311_script_KMPC_067_P5_3g7_C2_CDI_k0p005_nominal.py`, SHA-256
  `3D772377AAB7A3CBE711F04774188302823B05C46AAF3982420DEBF2F6BC0B94`;
- harness: `c2_atomic_runner_harness.py`, SHA-256
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

Po tomto zmrazení sa adaptér ani runner nesmú meniť. Technická chyba patrí do
Python error ledgeru a vyžaduje verziovaný successor; nesmie dostať fyzikálny
výklad.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | identita, support/depth, prahy, prerequisite a vetvenie zmrazené | `PREREGISTERED` |
| 2026-07-19 | statická kontrola, overenie prerequisite hashov a zmrazenie implementácie | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile, help a smoke vrátane owner-restore prešli | `TECHNICAL_GATE_PASS` |
| 2026-07-19 | oficiálny atóm publikovaný; M1/core/common/background PASS, tail FAIL | `REVIEW_SUPPORT_07_09_REQUIRED` |
