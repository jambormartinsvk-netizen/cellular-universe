# História balíka EA-038

## 2026-07-22 — SEALED_READY_FOR_EXTERNAL_MIXED_TIER_AUDIT

- nový immutable package ID; EA-037 zostáva nezmenený;
- KMPC-146 scope je explicitne T1 source/raw delta nad EA-037 T2 základom;
- KMPC-147 scope je standalone T2 s úplnou trojsúborovou runtime closure;
- full KMPC-131 runtime sa zámerne neduplikuje;
- manifest `15`, runtime mapa `3`, package `22`, response `1`, spolu
  `23 < 40`;
- R6 preflight cez PowerShell 7+ prešiel `105/105`, failed `0`;
- source/copy parita `15/15`, runtime mapa `3/3` a exact REPRO coverage
  `3/3` prešli;
- oba exact JSON vstupy runnera sú v runtime mape; KMPC-146 `SOURCE_NAME`
  je v Pythone zložený z dvoch susedných string literálov, preto jednoduchý
  full-path regex ho nehlási ako jeden token, no výsledné meno, source SHA,
  copy SHA aj runtime hash sú exact overené;
- package files `22`, response `1`, duplicate hash groups `0`, temp files
  `0`, placeholdery `0`;
- lokálny orchestrátor v package nespúšťa Python; fresh T2 patrí externému
  auditorovi;
- po tomto zápise je package immutable.
