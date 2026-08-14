# KMPC-082 — BI/k=.15 high-precision harness successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_PF087 / NO_PHYSICS_VERDICT`

PF-086 zastavil KMPC-081 pred importom a bez fyziky, pretože atomic harness
pozná iba 4.8 s. KMPC-082 zachováva bez jedinej zmeny auditný modul SHA
`5B7A4740428DEB891A4C5892FE8E4412E914EF10FAD58EF6D423549F93032DB4`,
80 dps, jeden 104×104 solve, nezávislý holdout, support aj všetky prahy.

Jediná zmena je hashovaný runtime wrapper: smoke vyžaduje presne 4.8 s,
official atom presne 45 s a aggregate odmieta. Wrapper po dobehnutí obnoví
stabilný argument guard. Prerequisite zostáva KMPC-080 SHA
`028BE28F8111FE6F775ACFC68A46FF51156DE0F1BD753D5A9C9CEA1CDF83DD1F`.

Výstup:
`RUN_KMPC_082_P5_3G7_C2_BI_K0p15_HIGH_PRECISION_HOLDOUT_BOUNDARY.json`.
Kandidáty a nonclaims sú identické s KMPC-081; PF-086 nesmie ovplyvniť
fyzikálny verdict.

Zmrazené SHA-256:

- high-precision harness:
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- runner 326:
  `84D780A54C7E00FE549E99458705556B18E41AEB61D09B73A54EBCF4DC80DF7A`;
- stabilný publish harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | PF-086 izolovaná na runtime guard; jediná povolená zmena zmrazená | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | oba harness hashe, runner a auditný modul zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
| 2026-07-19 | CLI 45 s prešiel; vnútorný KMPC-057 deadline zastal pred maticou/solve; failure SHA `8B557EC2...3041DD` | `PF-087 / NO_PHYSICS_VERDICT` |
