# História balíka EA-012

## 2026-07-18 — DRAFT_NOT_DELIVERED

Samostatný balík jedného uceleného support-ladder výsledku. Theory author:
Martin Jambor. Script creator: Codex (OpenAI). Obsahuje 10 evidence kópií a
minimálny úplný REPRO closure. Do seal-u sa smie meniť iba po preflighte.

## 2026-07-18 — PREFLIGHT_PASSED / SEALED_READY_FOR_AUDIT

Strojový preflight `259/259`. Fresh-copy compile/help/smoke/official audit
prešli a generated SHA
`28A3B43548C6B27202AB1AA28615A416A6A233840386EB72666CD3F5D01E5E2A`
reprodukoval M1/core/common/background PASS, tail PASS iba na `z=1e-4` a
overall REVIEW. Missing KMPC-061 prerequisite aj mutated base skončili
fail-closed exitom `2`. Tri zahoditeľné kópie odstránené. Balík je immutable.
