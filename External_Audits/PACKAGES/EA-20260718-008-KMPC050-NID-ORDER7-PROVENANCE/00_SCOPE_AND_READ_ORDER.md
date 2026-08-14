# Scope — KMPC-050 NID order-7 provenance

- Package ID: `EA-20260718-008-KMPC050-NID-ORDER7-PROVENANCE`
- Route: `A1-K1 / A2-K4 / P5.3g7 / GLOBAL_C1 / NID`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

1. Opravuje KMPC-050 iba PF-075 rank/shape capture routing a zachováva
   rovnice, support, prahy a immutable KMPC-048 výsledok?
2. Reprodukuje official runner plnú hodnosť `104/104`, provenance/regression
   PASS a same-matrix correction približne `2.29e-16`?
3. Zostávajú po korekcii nezávislé `Einstein_00[7]` a `Einstein_0i[7]`
   holdouty výrazne neuzavreté, takže obyčajný roundoff nie je dostatočné
   vysvetlenie?
4. Je depth-mismatch M1 order `5` proti M3 order `7` korektne označený iba
   ako ďalšia testovateľná hypotéza, nie ako už dokázaná príčina?

## Poradie čítania

1. `EVIDENCE/001–004`: protokol, kontrakt, prereg/ledger a výsledkový audit.
2. `005–010`: reference, PF-075 stopa, oba runnery a oba priame base moduly.
3. `011–013`: error ledger a immutable KMPC-048 kontext.
4. `014–026`: úplný import closure.
5. runtime mapa a official reprodukčné príkazy.

## Zmrazené kritériá

`NID/.05/nominal`, M3 support `[0,7]`, M1 depth `5`, driver `1e-10`, holdout
`1e-8`, absolute fallback `1e-12`, correction absolute aj relative limit
`1e-12`; presne jeden 16×16 passthrough a jeden 104×104 capture.

## Nonclaims

Nie T3. Bez dôkazu M1 depth-mismatch, zmeny rovníc, `[0,9]`, NIV, iných
`k`/variantov, S-M, ODE, G8/G9 alebo dát. KMPC-049 je iba immutable
technická stopa a nesmie sa znovu spúšťať ako official vetva.

`SCORE_EFFECT=NONE`; `RELEASE_TRIGGER=NONE`; `ZENODO_TRIGGER=NONE`.
