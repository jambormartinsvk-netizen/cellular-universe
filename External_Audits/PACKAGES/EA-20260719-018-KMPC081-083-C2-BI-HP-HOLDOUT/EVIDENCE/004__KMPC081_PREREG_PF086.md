# KMPC-081 — C2 BI/k=.15 high-precision holdout boundary: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_PF086 / NO_PHYSICS_VERDICT`  
**Prerequisite:** KMPC-080 SHA
`028BE28F8111FE6F775ACFC68A46FF51156DE0F1BD753D5A9C9CEA1CDF83DD1F`

Atóm ostáva `BI/k=.15`, accepted `[0,5]`, audit `[0,7]`, M1 depth 7.
KMPC-081 vykoná presne jeden `mpmath` LU solve auditnej 104×104 driver
matice pri `80 dps`. Každý float64 vstup sa prevedie exact pomerom celých
čísel. Holdout `Einstein_00/0i` sa zostaví pôvodným kódom a vyhodnotí v 80 dps
na tomto riešení; jeho riadky sa nikdy nepridajú do solve.

Zmrazené prahy: driver `1e-10`, holdout `1e-9`, absolute fallback `1e-12`.
Runtime official `45 s`, jeden high-precision solve, žiadne opakovanie ani
precision sweep. Smoke používa malú exact 3×3 maticu a overí owner restore,
canonical identitu, exact float bridge a odmietnutie cudzieho atómu.

PASS candidate je
`PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY` iba ak:

- high-precision driver aj nezávislý holdout PASS;
- jediná float64 false check bola holdout;
- M1, rank, forbidden guards, S-C0, common, tail a background ostali PASS.

High-precision FAIL zostáva `REVIEW_EXACT_ASSEMBLY_REQUIRED`, nie fyzikálny
STOP. Bez skóre, agregácie, release alebo Zenodo triggera.

Zmrazené SHA-256:

- module `c2_bi_k0p15_high_precision_holdout.py`:
  `5B7A4740428DEB891A4C5892FE8E4412E914EF10FAD58EF6D423549F93032DB4`;
- runner 325:
  `3C34EDD4B2A0E48107E6A34E112087444FD6210CA9753CA68CB6B1962698CB7B`;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | interný audit, 80 dps, jeden solve, nezávislý holdout, prahy a vetvenie zmrazené | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | module, runner a lineage hashovo zmrazené; success/failure raw neprítomné | `FROZEN / NOT_RUN` |
| 2026-07-19 | official zastal vo vonkajšom 4.8 s argument garde pred importom/solve | `PF-086 / NO_PHYSICS_VERDICT` |
