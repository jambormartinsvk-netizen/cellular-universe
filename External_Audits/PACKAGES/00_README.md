# Dôkazové balíky pre externý audit

Tento adresár obsahuje iba hotové, nemenné balíky vytvorené na požiadanie.
Každý priečinok `EA-...` je samostatný problém a obsahuje manifest SHA-256.

Nový balík sa považuje za hotový až po stave `PREFLIGHT_PASSED`, kontrole
`01_MANIFEST_SHA256.tsv` a `04_RUNTIME_DEPENDENCY_MAP.tsv` nástrojom
`External_Audits/TOOLS/Test-ExternalAuditPackage.ps1`. Importy samy osebe
nie sú dependency closure; povinné sú aj runtime-opened JSON/config/data
vstupy v presnej ceste `REPRO/`.

Nevkladajte sem voľné poznámky ani odpovede auditora. Tie patria do
`External_Audits/RESPONSES/` s rovnakým ID balíka.

Pravidlá: [protokol balíkov](../00_AUDITOR_PACKAGE_PROTOCOL_SK.md).
