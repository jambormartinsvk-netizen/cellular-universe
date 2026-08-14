# Preflight checklist externého auditného balíka

## Lifecycle

- [ ] Balík má nový, nikdy nepoužitý Package ID.
- [ ] R6 preflight sa spúšťa cez `pwsh` 7+, nie cez legacy Windows PowerShell 5.1.
- [ ] Stav je `DRAFT`; pred preflightom sa neoznačuje `SEALED` ani `READY`.
- [ ] Po odovzdaní sa balík už nemení; oprava dostane nové `NNN`.
- [ ] Po seal sa v aktívnom scope/instructions nenachádza stale `DRAFT_NOT_DELIVERED`, `NOT_SEALED`, `AWAITING_*` ani budúci čas o review/seale; historické výskyty sú iba v označenej package history.

## Scope a autorita

- [ ] Jedna presná otázka, explicitné nonclaims a target evidence tier.
- [ ] Oddelený package verdict, technický výsledok a fyzikálny verdict.
- [ ] Zmrazené rozhodovacie prahy sú oddelené od nových diagnostických prahov.

## Úplnosť dôkazov

- [ ] `01_MANIFEST_SHA256.tsv` má source/copy path, rolu a oba hashe.
- [ ] Každé errátum alebo rozhodovací dokument citovaný ako opora účtovania či verdiktu je priložený; ak je redundantný, scope obsahuje explicitnú coverage poznámku s pôvodnou cestou, SHA-256 a dôvodom vynechania.
- [ ] Každý importovaný projektový modul má podľa single-copy pravidla jednu fyzickú kópiu v `REPRO/` a manifest mu pridelí všetky potrebné roly.
- [ ] Každý runtime-opened JSON/config/data súbor je v runtime dependency mape.
- [ ] Každá lokálna cesta z `EXPECTED_HASHES` alebo obdobnej source-hash mapy je v `REPRO/`, manifeste a runtime mape.
- [ ] Runtime mapa má exact coverage všetkých fyzických súborov pod `REPRO/`; nemá chýbajúce ani navyše deklarované riadky.
- [ ] Negatívne a nulové fixtures potrebné pre scope sú priložené alebo opísané.
- [ ] Output adresár rozlišuje runtime vstupy od generated outputs.

## Reprodukcia

- [ ] Presné smoke a audit príkazy, interný aj externý timeout.
- [ ] Očakávaný exit code vrátane zámerného nonzero exit.
- [ ] Referenčný raw výsledok a očakávané polia/tolerancie.
- [ ] Field-parity pravidlo vopred menuje všetky top-level aj vnorené runtime polia a pri absolútnej ceste zachováva relatívny suffix + source SHA-256.
- [ ] Oficiálna vetva a každá odchýlka sú vyhodnotené oddelene.
- [ ] Cross-platform diagnostika nemôže prepísať zmrazený projektový prah.

## Hygiena a odpoveď

- [ ] Nulové operation counts sú označené `RUNTIME_INSTRUMENTED` alebo `STATICALLY_DEMONSTRATED`; pri statickom tvrdení pokyny vyžadujú nezávislý source/import/call scan auditora.
- [ ] Atomic-publish collision fixture nezmení cieľ a nenechá temp súbor.
- [ ] Runner exportuje Python, knižnice, BLAS/LAPACK, OS a architektúru.
- [ ] Response template vyžaduje príkaz, exit code, wall time a output SHA-256.
- [ ] `Test-ExternalAuditPackage.ps1` skončí `passed=true`.
- [ ] Live `Test-ExternalAuditPackage.ps1` je označený ako pre-seal kontrola kurátora/reviewera/orchestrátora, nie ako package-only príkaz externého auditora.
- [ ] Každý povinný auditorský príkaz je realizovateľný iba z `ALLOWED_READS`; sealed-only allowlist neodkazuje na nepribalený live tool.
- [ ] Ak sa checker prikladá, je manifestovaný, self-contained a nečíta live `source_path`; inak pokyny vyžadujú explicitnú package-local hash/inventory kontrolu.
