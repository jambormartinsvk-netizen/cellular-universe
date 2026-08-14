# KMPC-078 — C2 BI/k=.005 support `[0,7]→[0,9]`: predregistrácia resume

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / PASS_CANDIDATE`  
**Ordering prerequisite:** KMPC-076 SHA
`B053B523C00032360F8FAFC47189C577B9B3D426778D881A2BD110DE3C4FCA00`  
**Checkpoint prerequisite:** KMPC-077 SHA
`68A7B968A0FBDC0779D983B052C00ED05D01CAE0114D40224FAC705F09F103E8`

Jediný fyzikálne interpretovateľný atóm je checkpoint-resumed
`BI/k=.005`, accepted `[0,7]`, audit `[0,9]`, M1 depth 9. Rovnice, matice,
`rcond`, prahy a metriky sa nemenia. Resume musí hashovo overiť checkpoint,
jeho `NO_PHYSICS_VERDICT` rolu, BI identitu, support/depth a source lineage.

Povinné brány: M1 driver/holdout, core/S-C0, common `0…7`, tail `8,9` na
`z=1e-4,.01`, background a phase-aware autoritatívne 13-state poradie.
PASS candidate je
`PASS_C2_BI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`. Tail-only FAIL
otvorí `[0,9]→[0,11]`; iný fail sa vetví podľa frozen C2 stromu. Bez skóre,
agregácie, release alebo Zenodo triggera.

Použije sa nezmenený wrapper SHA
`DEB7776EFE28D60978FA49ABB914B3718C7F31F111DDC4B4037DA73961798B9F`
a nový runner 322. Raw:
`RUN_KMPC_078_P5_3G7_C2_BI_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json`.

Zmrazený SHA-256 runnera 322:
`CFC5AB13EB68CF7A4023AFF3AECBF81166F2234C09F8FA4AF304A2761C30EABF`.
Harness SHA-256:
`735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | checkpoint SHA, identita, support, hĺbka, brány, kandidáty a nonclaims zmrazené | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | runner a lineage hashovo zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
| 2026-07-19 | compile/smoke/official PASS; všetky brány a 13-state order PASS; raw SHA `F24894A0...18A359` | `IMMUTABLE / PASS_CANDIDATE` |
