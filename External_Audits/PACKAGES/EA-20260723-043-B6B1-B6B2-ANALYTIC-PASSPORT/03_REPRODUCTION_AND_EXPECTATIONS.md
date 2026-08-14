# Statický audit a očakávania EA-043

EA-043 je statický T1 analytic-envelope/perturbation/search/data-passport
capsule. Povinný je package preflight a nezávislý ručný audit; official
Python vetva neexistuje.

```powershell
pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 `
  -PackagePath External_Audits\PACKAGES\EA-20260723-043-B6B1-B6B2-ANALYTIC-PASSPORT
```

Očakávanie: exit code `0`, `96/96` kontrol PASS, source/copy parita `15/15`,
`REPRO=0`, runtime rows `0` a wall time zapísaný auditorom. Žiadny generated
JSON sa neočakáva.

## Povinné nezávislé kontroly

1. zostaviť tabuľku common a MF1–MF4 moment inequalities s predpokladmi,
   nulovými limitmi a nonclaims;
2. zostaviť tabuľku `P0–P8` s kovariantnými source/sign/source-off
   požiadavkami a rodinnými identity;
3. skontrolovať, že search record je append-only/immutable, coverage je
   explicitná a ranking nepoužíva comparator ani quasi-holdout ako leakage;
4. oddeliť E3 interval `[0.777,0.831]` od jeho E2 mapovania a od budúcej
   forward predikcie;
5. označiť DES/KiDS/HSC čísla iba `INFERRED_FROM_PROJECT_DOCS` a nevydávať
   primary-publication verification claim;
6. overiť dependency graph D03/D04–D11 a minimalitu successor balíka
   D04+D08+D10 bez tvrdenia closure ostatných blokov.

Správny audit môže potvrdiť scope, nájsť presnú medzeru alebo odmietnuť
konkrétnu časť contractu. Nemôže z tohto balíka vyhlásiť existenciu alebo
neexistenciu rodiny, vykonať kandidátny search, predikovať S8, certifikovať
holdout, dosiahnuť T2/T3 ani zmeniť projektový stav, skóre alebo hĺbku.
