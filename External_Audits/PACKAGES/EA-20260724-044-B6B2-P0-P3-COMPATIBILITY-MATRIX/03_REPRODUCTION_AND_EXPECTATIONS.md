# Statický audit a očakávania EA-044

EA-044 je statický T1 analytic compatibility/constraint-matrix capsule.
Povinný je package preflight a nezávislý ručný audit; official Python vetva
neexistuje.

```powershell
pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 `
  -PackagePath External_Audits\PACKAGES\EA-20260724-044-B6B2-P0-P3-COMPATIBILITY-MATRIX
```

Očakávanie: exit code `0`, všetky kontroly PASS, source/copy parita `15/15`,
`REPRO=0`, runtime rows `0` a wall time zapísaný auditorom. Žiadny generated
JSON sa neočakáva.

## Povinné nezávislé kontroly

1. zostaviť mapu všetkých osí dokumentu 249 na atomic IDs, interval alebo
   unresolved stav a residual bucket v dokumente 250;
2. skontrolovať common-base compatibility a odlíšenie fibered productu od
   neodôvodneného Cartesian enumeration;
3. rozlíšiť retarded/commutator causality od classical/initial covariance a
   overiť positivity/null contract podľa reprezentácie objektu;
4. overiť `AP-BASELINE-ALL`, AP-NOISE-C/Q, F01–F09 inheritance a MF1 memory
   completion coverage;
5. skontrolovať EC certifikáty podľa class/domain a oddeliť
   `PRECHECK_EXCLUDED_SCOPE`, unresolved, E2 mismatch a E3 guidance;
6. overiť full-`R_test` quotient, conservation/no-double-count, quantum
   bilateral nulls a recovery limity;
7. auditovať iba minimalitu bounded P4 successor, nie vytvoriť svedka.

Správny audit môže potvrdiť deklarovaný scope, nájsť presnú medzeru alebo
odmietnuť konkrétnu časť matice. Nemôže z tohto balíka vyhlásiť fyzikálnu
neprázdnosť alebo univerzálnu prázdnosť, vybrať MF rodinu, vykonať P4,
predikovať S8, dosiahnuť T2/T3 ani zmeniť projektový stav, skóre či hĺbku.
