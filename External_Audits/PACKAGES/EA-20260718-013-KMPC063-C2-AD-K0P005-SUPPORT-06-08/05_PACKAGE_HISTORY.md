# História balíka EA-013

## 2026-07-18 — DRAFT_NOT_DELIVERED

Samostatný balík jedného uceleného support-ladder PASS výsledku. Theory
author: Martin Jambor. Script creator: Codex (OpenAI). Obsahuje 11 evidence
kópií a minimálny úplný REPRO closure. Do seal-u sa smie meniť iba po
strojovom a behaviorálnom preflighte.

## 2026-07-18 — PREFLIGHT_FORMAT_REJECTED / DRAFT_REPAIRED

Prvý strojový preflight odmietol všetkých 39 manifestových riadkov, lebo
TSV hlavička obsahovala doslovné `` `t `` namiesto tabulátorov. Runtime
mapa, súbory a hashe prešli. Opravená bola iba hlavička; nevznikol Python
proces ani fyzikálny výsledok.

## 2026-07-18 — PREFLIGHT_PASSED / SEALED_READY_FOR_AUDIT

Strojový preflight `271/271`. Fresh-copy compile/help/smoke/official audit
prešli a generated SHA
`7E0931BDAD03686AEBE0AFF685F1997382EA38ACED9D357BF07913A927C0ADD0`
reprodukoval M1/core/common/background/tail PASS, F0 `.01`
`1.8269976120859345e-9` a M3 `.01` `5.074642949718514e-9`. Missing
KMPC-062 prerequisite aj mutated KMPC-063 base skončili fail-closed exitom
`2`. Tri zahoditeľné kópie boli odstránené. Balík je immutable.
