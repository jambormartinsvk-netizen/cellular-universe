# História balíka EA-039

## 2026-07-22 — DRAFT_NOT_DELIVERED

- nový immutable package ID; EA-038 zostáva nezmenený;
- scope je samostatná T2 reprodukcia read-only KMPC-148 agregátu;
- single-copy closure obsahuje runner, base, 15 pair rawov a 5 mode
  autorít; reference raw je iba v `EVIDENCE/`;
- plánovaný manifest `25`, runtime mapa `22`, package `32`, response `1`,
  spolu `33 < 40`;
- povolená field normalizácia je iba top-level `runtime_seconds`;
- pripravené sú dva odlišné fail-closed guardy: missing pair a missing mode
  authority;
- lokálny orchestrátor v package nespúšťa Python; fresh T2 patrí externému
  auditorovi.

## 2026-07-22 — SEALED_READY_FOR_EXTERNAL_T2_AUDIT

- prvý R6 draft preflight prešiel `211/212`; jediný fail bol chýbajúci
  doslovný control marker `Autorita` v dokumente 00;
- marker bol doplnený bez zmeny manifestu, runtime closure alebo dôkazov;
- opravný R6 preflight cez PowerShell 7+ prešiel `212/212`, failed `0`;
- source/copy parita `25/25`, runtime mapa `22/22` a exact REPRO coverage
  `22/22` prešli;
- package files `32`, response `1`, spolu `33 < 40`; duplicate hash groups
  `0`, temp files `0`, pending hash markers `0`;
- po finálnom kontrolnom preflighte je package immutable.
