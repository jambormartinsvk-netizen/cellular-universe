# Scope — KMPC-062 C2 AD/k=.005 support `[0,4]→[0,6]`

- Package ID: `EA-20260718-012-KMPC062-C2-AD-K0P005-SUPPORT-04-06`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

Reprodukuje KMPC-062 pri nezmenených prahoch M1/core/common/S-C0/background
PASS, tail `5,6` PASS na `z=1e-4`, ale FAIL na `z=.01`, takže `[0,4]` ešte
nie je adequate a oprávnený je iba ďalší REVIEW `[0,6]→[0,8]`?

## Poradie čítania

1. `EVIDENCE/001–002` protokol a frozen kontrakt.
2. `003–005` predregistrácia, ľudský audit a immutable raw.
3. `006–008` official runner, base a stabilný harness.
4. `009–010` KMPC-061 kontext a runtime prerequisite.
5. Dokument 03 a official reprodukcia iba runnera 306.

## Zmrazené kritériá

AD/`.005` nominal; candidate/audit `[0,4]→[0,6]`; M1 depth 6; common
`0…4`; tail `5,6`; `z=1e-4,.01`; common `1e-8`, tail `1e-6`, absolute
fallback `1e-12`, background `1e-12`.

## Nonclaims

Nie T3. Bez `[0,6]→[0,8]`, ostatných C2/C3 atómov, S-M, hierarchy, ODE
alebo dát. Bez score/release/Zenodo/prediction triggera.
