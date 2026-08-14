# Scope — KMPC-048 NID support step 2

- Package ID: `EA-20260718-007-KMPC048-NID-SUPPORT-STEP2`
- Route: `A1-K1 / A2-K4 / P5.3g7 / GLOBAL_C1 / NID`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

1. Reprodukuje official runner regresiu `[0,3]/[0,5]`, common `0…5`, tail
   `6,7` a combined-`R_fs` PASS, ale order-7 core FAIL?
2. Je zlyhanie lokalizované na M3 driver `fuel_continuity[7]` a nezávislý
   holdout `Einstein_00[7]`, nie na rank, tail alebo support regresiu?
3. Je `REVIEW_NID_SUPPORT_STEP_2_ORDER7_CORE_BOUNDARY` primeraný bez
   fyzikálneho STOP a bez automatického `[0,9]`?

## Poradie čítania

1. `EVIDENCE/001–002`: protokol a frozen support kontrakt.
2. `003–005`: predregistrácia, výsledkový audit a raw reference.
3. `006–007`: official runner a direct base.
4. `008–021`: error ledger a úplný import closure.
5. runtime mapa a reprodukčné príkazy.

## Zmrazené kritériá

`NID/.05/nominal`; regression `[0,3]/[0,5]`; candidate `[0,5]`; audit
`[0,7]`; leading `j=0`; common `0…5` s `1e-8`; envelope tail `6,7` s
`1e-6`; absolute fallback `1e-12`; surfaces `1e-4,1e-2`.

## Nonclaims

Nie T3. Bez `[0,9]`, uzavretia order-7 precision/provenance, NIV, iných
`k`/variantov, S-M, full hierarchy, P5.4, G8/G9 alebo dát.

`SCORE_EFFECT=NONE`; `RELEASE_TRIGGER=NONE`; `ZENODO_TRIGGER=NONE`.

