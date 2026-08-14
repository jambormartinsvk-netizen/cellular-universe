# História balíka EA-036

## 2026-07-20 — SEALED_READY_FOR_EXTERNAL_AUDIT

- koherentná jednotka: NIV/.005 PASS, NIV/.05 PASS a prvý REVIEW NIV/.15;
- interný authoritative stav: NIV `7/9`, C3 `43/45`, K4 `60/100`;
- live zmeny obmedzené na predregistráciu 236, nový audit 237, DNR register
  a aktuálny plán; Python source ani raw sa nemenili;
- single-copy manifest: `31` exact source kópií;
- runtime closure: runner + `20` lokálnych importov + `2` JSON vstupy;
- package: `38` súborov, response šablóna `1`, spolu `39 < 40`;
- lokálny Python nebol po prvom REVIEW znovu spustený;
- bez-Pythonový package preflight prešiel `221/221`, failed `0`;
- source/copy parity `31/31`, runtime mapa `23/23`, statický import closure
  `20/20`, duplicate hash groups `0`, temp files `0`;
- fresh REPRO obsahuje iba dva vstupné JSON-y a cieľový output je
  neprítomný;
- externý auditor má ako prvý vykonať fresh T2 reprodukciu a dva negatívne
  missing-input guardy;
- package po úspešnom preflighte ostáva immutable.
