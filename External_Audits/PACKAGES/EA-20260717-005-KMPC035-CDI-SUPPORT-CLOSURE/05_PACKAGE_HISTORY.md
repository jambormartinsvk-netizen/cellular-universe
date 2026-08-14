# História balíka EA-005

## 2026-07-17 — DRAFT_NOT_DELIVERED

Balík vznikol ako nový follow-up po prijatí externého auditu 003. Pôvodný
balík ani jeho odpoveď sa nemenia. Scope je technická reprodukčná closure;
fyzika, supporty a projektové prahy KMPC-035 zostávajú zmrazené.

Zapracované nálezy:

- F1: priložený KMPC-034 runtime prerequisite;
- F2: oddelená cross-platform diagnostika bez verdict effect;
- F3: would-be relative diagnostika absolute vetvy;
- F4: šesťbodový z-scan s explicitným nonclaimom;
- F5: collision-safe publish a negatívny fixture;
- F6: environment a BLAS/LAPACK metadata;
- F7: výslovný zákaz tvrdenia T3 pri spoločnom equation engine.

Python nebol pri zostavení balíka spustený. Pred sealom musí prejsť iba
read-only PowerShell package preflight; vedecký smoke/audit vykoná externý
auditor.

## 2026-07-17 — PREFLIGHT_PASSED / SEALED_READY_FOR_AUDIT

Read-only `Test-ExternalAuditPackage.ps1` skončil:

```text
checks=168
failed=0
passed=true
```

Overil 24 source/copy evidence položiek, 14 runtime ciest, povinné control
súbory, response template, scope/instruction markery a nulové temp alebo
pending-hash artefakty. Po tomto bode sa balík nemení; každá ďalšia oprava
musí dostať nové `NNN`.
