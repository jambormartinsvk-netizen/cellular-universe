# Scope — KMPC-051 až 053 NID support closure

- Package ID: `EA-20260718-009-KMPC051-053-NID-SUPPORT-CLOSURE`
- Route: `A1-K1 / A2-K4 / P5.3g7 / GLOBAL_C1 / NID`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

1. Dokazuje KMPC-051, že M1 depth 7 odstráni veľký NID Einstein order-7
   holdout bez common regresie, pričom ostane iba float64 driver hranica?
2. Reprodukujú V2 aj nezávislý V3 80-dps same-matrix solve v KMPC-052
   úplný driver/holdout PASS v capoch?
3. Reprodukuje official KMPC-053 immutable regresiu, refined core, common a
   tail PASS, a teda scoped adequacy candidate supportu `[0,5]`?
4. Zostávajú tvrdenia korektne obmedzené na `NID/.05/nominal` bez `[0,9]`
   a bez prenosu na NIV?

## Poradie čítania

1. `EVIDENCE/001–002`: protokol a frozen support kontrakt.
2. `003–007`: KMPC-051 depth diagnosis.
3. `008–012`: KMPC-052 numerical boundary.
4. `013–017`: KMPC-053 official support closure.
5. `018–019`: error ledger a immutable regression prerequisite.
6. runtime mapa a official reprodukcia KMPC-053.

## Zmrazené kritériá

M1 depth `7`; supporty `[0,3]/[0,5]/[0,7]`; driver `1e-10`, holdout/common
`1e-8`, tail `1e-6`, absolute fallback a correction cap `1e-12/1e-14`;
tail iba `6,7` na `z=1e-4,1e-2`.

## Nonclaims

Nie T3. Bez NIV, iných `k`/variantov, `[0,9]`, S-M, full hierarchy, ODE,
P5.4, G8/G9 alebo dát. Official T2 vetva je KMPC-053; KMPC-051/052 sú
reference lineage, nie ďalšie povinné spustenia.

`SCORE_EFFECT=NONE`; `RELEASE_TRIGGER=NONE`; `ZENODO_TRIGGER=NONE`.
