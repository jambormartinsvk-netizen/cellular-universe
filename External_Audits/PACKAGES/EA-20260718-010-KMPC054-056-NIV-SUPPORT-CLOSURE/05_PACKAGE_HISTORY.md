# História balíka EA-010

## 2026-07-18 — DRAFT_NOT_DELIVERED

Balík vznikol po ucelenom NIV fail-fast/support/owner closure. Theory author:
Martin Jambor. Script creator: Codex (OpenAI). Obsahuje immutable KMPC-054,
PF-076 failure KMPC-055, official KMPC-056 a úplný runtime closure. Po
behaviorálnom preflighte bude zapečatený; ďalšia oprava dostane nové ID.

Behaviorálny draft preflight odhalil dve runtime-opened formula závislosti,
ktoré neboli v pôvodnej import mape: script 88 a document 26. Official
reprodukcia fail-closed zastala pred fyzikálnym payloadom. Pred sealom boli
obe pravé hashované kópie doplnené do `REPRO/`, manifestu a runtime mapy;
nejde o zmenu auditovaných zdrojov ani verdiktu.

## 2026-07-18 — PREFLIGHT_PASSED / SEALED_READY_FOR_AUDIT

`Test-ExternalAuditPackage.ps1`: `checks=153`, `failed=0`, `passed=true`.
Fresh-copy compile/help/smoke/official audit prešli; generated candidate,
owner restore, regression, M1 depth 6, core, common a tail boli PASS.
Missing-prerequisite aj mutated-source fixtures skončili fail-closed exitom
`2`. Balík je odteraz immutable.
