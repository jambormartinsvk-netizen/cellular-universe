# Scope — KMPC-063 C2 AD/k=.005 support `[0,6]→[0,8]`

- Package ID: `EA-20260718-013-KMPC063-C2-AD-K0P005-SUPPORT-06-08`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

Reprodukuje KMPC-063 pri nezmenených prahoch M1/core/common/S-C0/background
PASS a tail `7,8` PASS na `z=1e-4` aj `z=.01`, takže support `[0,6]` je
adequate candidate iba pre AD/k=.005/nominal a C2 sa posúva na `1/10 PASS`?

## Poradie čítania

1. `EVIDENCE/001–002` protokol a frozen kontrakt.
2. `003–005` predregistrácia, ľudský audit a immutable raw.
3. `006–008` official runner, base a stabilný harness.
4. `009–011` KMPC-062 kontext, runtime prerequisite a jeho base.
5. Dokument 03 a official reprodukcia iba runnera 307.

## Zmrazené kritériá

AD/`.005` nominal; candidate/audit `[0,6]→[0,8]`; M1 depth 8; common
`0…6`; tail `7,8`; `z=1e-4,.01`; common `1e-8`, tail `1e-6`, absolute
fallback `1e-12`, background `1e-12`.

## Nonclaims

Nie T3. Bez AD/`.15`, ostatných C2/C3 atómov, S-M, hierarchy, ODE alebo
dát. Bez score/release/Zenodo/prediction triggera. PASS supportu jedného
atómu nie je fyzikálny verdikt celej P5 ani A2-K4.
