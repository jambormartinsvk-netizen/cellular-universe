# História balíka EA-018

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

Balík izoluje interný audit, dve technické runtime chyby bez fyziky a prvý
dokončený 80-dps solve/holdout boundary. Theory author Martin Jambor; script
creator/internal auditor Codex (OpenAI). Seal až po manifest a fresh-copy teste.

Prvý fresh-copy smoke odhalil chýbajúci transitívny import
`m1_order7_provenance.py`; balík ešte nebol zapečatený. Closure bol doplnený
a manifest regenerovaný. Potom compile, smoke aj official runner 327 prešli
exit code 0. Generated SHA `DFEDFF49...FC0CA0B`; diff voči referencii je iba
lokálna cesta a dve runtime polia, všetky fyzikálne/numerické polia sú zhodné.
Finálny preflight: `474/474 PASS`.
