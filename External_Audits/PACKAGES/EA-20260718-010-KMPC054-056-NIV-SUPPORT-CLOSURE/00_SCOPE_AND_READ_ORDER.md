# Scope — KMPC-054 až 056 NIV support closure

- Package ID: `EA-20260718-010-KMPC054-056-NIV-SUPPORT-CLOSURE`
- Route: `A1-K1 / A2-K4 / P5.3g7 / GLOBAL_C1 / NIV`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

1. Reprodukuje KMPC-054 PASS core/common/combined-`R_fs`, ale FAIL tailu
   `3,4`, takže NIV `[-1,2]` je nedostatočný?
2. Je KMPC-055 správne zachovaný ako PF-076 technický failure bez
   fyzikálneho verdiktu?
3. Mení KMPC-056 iba owner bridge, obnoví namespace a reprodukuje nezmenený
   depth-6 test `[-1,4]→[-1,6]`?
4. Prejdú regression, M1, core, common a tail `5,6`, takže `[-1,4]` je
   adequate iba v scope `NIV/.05/nominal`?

## Poradie čítania

1. `EVIDENCE/001–002`: R3 protokol a frozen support kontrakt.
2. `003–007`: KMPC-054 fail-fast otázka a výsledok.
3. `008–012`: KMPC-055/PF-076 technická história; 299 nespúšťať.
4. `013–017`: KMPC-056 owner successor a autoritatívny scoped výsledok.
5. runtime mapa a official reprodukcia iba runnera 300.

## Zmrazené kritériá

NIV leading `j=-1`; candidate/audit `[-1,4]→[-1,6]`; M1 depth `6`;
common `-1…4`; tail iba `5,6`; plochy `z=1e-4,1e-2`; common `1e-8`, tail
`1e-6`, absolute fallback `1e-12`; regresia `1e-12/1e-14`.

## Nonclaims

Nie T3. Bez iných `k`/variantov, `[-1,8]`, S-M, full hierarchy, ODE/P5.4,
G8/G9 alebo dát. Official T2 vetva je iba KMPC-056; KMPC-054 je immutable
reference a KMPC-055 je `DO_NOT_RUN_AUDIT_TECHNICAL`.

`SCORE_EFFECT=NONE`; `RELEASE_TRIGGER=NONE`; `ZENODO_TRIGGER=NONE`.
