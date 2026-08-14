# História balíka EA-025

## 2026-07-19 — DRAFT_NOT_DELIVERED

Balík zhromažďuje ucelené uzavretie BI módu v C2: checkpoint/receipt z
KMPC-108/109, exact-resume predregistrácie KMPC-110–112, technické
PF-111/PF-112, úspešný raw KMPC-112 a interný audit dokument 179. Theory
author: Martin Jambor. Script creator/internal auditor: Codex (OpenAI).

Runtime closure vychádza zo sealed EA-024 a pridáva iba V17–V19, runnery
354–356 a hashovaný PF-112 prerequisite. Pred sealom musí prejsť package
preflight, negatívny missing-prerequisite guard a izolovaná field-level
reprodukcia KMPC-112.

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

Balík má `156` source/copy manifest riadkov a `126` runtime-map riadkov.
Draft preflight prešiel `1052/1052`.

Izolované behaviorálne kontroly prešli:

- negatívna vetva bez PF-112 prerequisite skončila podľa kontraktu v
  `static_hash_guard`, exit `2`, bez success raw;
- čistá KMPC-112 vetva: compile exit `0` (`0.184 s`), help exit `0`
  (`1.716 s`), smoke exit `0` (`1.407 s`) a official exit `0`
  (`37.288 s` wall; raw runtime `35.718 s`);
- generated raw SHA
  `A004DF7D0D7D53943D5544279049323A1F1927015936AA948C39FF72D5D81624`;
- field-level obsah je zhodný s Evidence 018 po odrátaní iba všetkých polí
  `runtime_seconds`; technical/physics false množiny sú prázdne, pôvodná
  audit false množina je presne `M3_driver`;
- driver `8.6147582237e-82`, holdout `7.0711904227e-15`,
  `Einstein_0i[7]=3.3965448411e-15` a fitted holdout rows `0`.

Obe dočasné fresh-copy vetvy boli po kontrole bezpečne odstránené. Final
package preflight prešiel `1052/1052`. Od tohto seal bodu sú evidence,
runtime strom, manifesty, control docs a response template immutable;
oprava vyžaduje nový package ID.
