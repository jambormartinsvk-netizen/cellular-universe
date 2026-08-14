# Scope — KMPC-064/065 C2 AD/k=.15 nominal

- Package ID: `EA-20260718-014-KMPC064-065-C2-AD-K0P15-NOMINAL`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

Potvrdzuje balík, že KMPC-064 skončil iba technickým PF-080 bez fyziky a
KMPC-065 po smoke-scope oprave reprodukovateľne dáva M1/core/common/
background PASS, ale tail `3,4` FAIL na oboch plochách, takže AD/k=.15
vyžaduje iba support `[0,4]→[0,6]` REVIEW a nie STOP?

## Poradie čítania

1. `EVIDENCE/001–002` protokol a support kontrakt.
2. `003–005` obe predregistrácie a výsledkový audit.
3. `006–010` raw, runner, oba base a harness.
4. `011–012` predchádzajúci C2 kontext a ordering prerequisite.
5. Dokument 03 a official reprodukcia runnera 309.

## Zmrazené kritériá

AD/`.15` nominal; candidate/audit `[0,2]→[0,4]`; M1 depth 5; common
`0…2`; tail `3,4`; `z=1e-4,.01`; common `1e-8`, tail `1e-6`, absolute
fallback `1e-12`, background `1e-12`.

## Nonclaims

Nie T3. Bez support `[0,4]→[0,6]`, ďalších C2/C3 atómov, S-M, hierarchy,
ODE alebo dát. Bez score/release/Zenodo/prediction triggera. REVIEW
supportu nie je fyzikálny STOP P5 ani A2-K4.
