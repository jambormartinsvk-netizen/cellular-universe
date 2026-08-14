# História balíka EA-011

## 2026-07-18 — DRAFT_NOT_DELIVERED

Balík vznikol po ucelenom C2 guard-closure a prvom AD/`.005` atóme. Theory
author: Martin Jambor. Script creator: Codex (OpenAI). Obsahuje iba 21
plochých evidence kópií a minimálny úplný `REPRO` runtime closure; žiadne
ďalšie projektové dokumenty sa kvôli balíku nemenili. Po strojovom a
behaviorálnom preflighte sa buď zapečatí, alebo dostane nový package ID.

Draft preflight najprv odhalil iba chybnú TSV hlavičku s doslovným `` `t ``;
všetkých 28 runtime riadkov už v tom behu prešlo. Hlavička bola pred sealom
opravená na skutočné tabulátory; zdroje, kópie ani verdikt sa nemenili.

## 2026-07-18 — PREFLIGHT_PASSED / SEALED_READY_FOR_AUDIT

`Test-ExternalAuditPackage.ps1`: `checks=321`, `failed=0`, `passed=true`.
Fresh-copy compile/help/smoke/official audit prešli. Generated JSON SHA
`E12A6E744B4B081F41ACA9A61098786A62FB2175D370132538B48E5ECB68CA54`
reprodukoval candidate `REVIEW_C2_SUPPORT_EXTENSION_REQUIRED`, M1/core/common/
background PASS, tail FAIL a owner restore PASS. Missing-prerequisite aj
mutated-source fixtures skončili fail-closed `TECHNICAL_FAILURE` exitom `2`.
Všetky tri zahoditeľné preflight kópie boli odstránené. Balík je odteraz
immutable; oprava vyžaduje nový Package ID.
