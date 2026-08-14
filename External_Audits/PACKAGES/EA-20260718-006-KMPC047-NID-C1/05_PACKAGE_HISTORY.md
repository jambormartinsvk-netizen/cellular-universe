# História balíka EA-006

## 2026-07-18 — DRAFT_NOT_DELIVERED

Balík vznikol po ucelenom KMPC-047 NID C1 atóme. Obsahuje iba dôkazy a
runtime closure potrebné na reprodukciu jednej otázky. Theory author je
Martin Jambor; script creator je Codex (OpenAI).

Zapracované procesné zlepšenia z auditov 003–005:

- samostatný runtime dependency TSV;
- oba runtime-opened prerequisite JSON v presnej ceste;
- source/copy parity a strojový manifest;
- official vetva oddelená od odchýlok;
- generated output nie je predvložený do `REPRO/`;
- negatívny missing-dependency test v zahoditeľnej kópii;
- explicitné nonclaims, autorita a T2/T3 hranica.

Po doplnení manifestov musí prejsť read-only package preflight. Po stave
`SEALED_READY_FOR_AUDIT` sa balík nemení.

## 2026-07-18 — PREFLIGHT_PASSED / SEALED_READY_FOR_AUDIT

Read-only `Test-ExternalAuditPackage.ps1` skončil:

```text
checks=138
failed=0
passed=true
```

Overil 18 source/copy evidence položiek, 14 runtime ciest, oba prerequisite
JSON, povinné control súbory, response template, markery a nulové temp alebo
pending-hash artefakty. Od tohto bodu je balík nemenný; oprava vyžaduje nové
package ID.
