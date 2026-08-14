# História balíka EA-017

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

Jeden balík pokrýva súvislý BI reťazec od nominal tail REVIEW cez nový
konfigurovateľný checkpoint až po k=.15 independent-holdout boundary.
Theory author Martin Jambor; script creator Codex (OpenAI).

Prvý sekvenčný fresh-copy pokus správne fail-closed odhalil PF-085: generated
runtime-bearing raw nemôže nahradiť exact-hash prerequisite ďalšieho runnera.
Balík sa preto pred sealom mení na izolované per-run reprodukcie s dodanými
immutable raw 075–080. Fyzikálny stav sa tým nemení.

Opravená isolated fresh-copy vetva KMPC-077 prešla exit code 0 a vytvorila
iba complete `NO_PHYSICS_VERDICT` checkpoint. Projektové compile/smoke/official
behy KMPC-076 až 080 prešli technicky a reprodukovali deklarovaný PASS/REVIEW
profil. Finálny manifest preflight: `457/457 PASS`.
