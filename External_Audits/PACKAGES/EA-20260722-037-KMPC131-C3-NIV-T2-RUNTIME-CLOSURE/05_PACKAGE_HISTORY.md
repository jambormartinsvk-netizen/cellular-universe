# História balíka EA-037

## 2026-07-22 — SEALED_READY_FOR_EXTERNAL_T2_AUDIT

- nový ID; EA-036 zostáva immutable;
- opravný scope je iba EA-036 F-001 až F-003;
- pridané dve exact-hash runtime závislosti, ktoré chýbali v EA-036;
- field parity vopred menuje šesť runtime polí a jednu path-root
  normalizáciu so suffix/hash guardom;
- frozen runner, `20` importov, dva JSON vstupy a reference raw sú byteovo
  nezmenené;
- manifest `30`, runtime mapa `25`, package `37` + response `1`, spolu
  `38 < 40`;
- lokálny orchestrátor nespúšťa Python; fresh T2 patrí externému agentovi;
- R6 preflight prešiel `249/249`, failed `0`;
- source/copy parita `30/30`, runtime mapa `25/25`, exact REPRO coverage
  `25/25`, hardcoded dependency checks `3/3`;
- package files `37`, response `1`, duplicate hash groups `0`, temp files
  `0`, placeholdery `0`;
- lokálny Python nebol spustený; po tomto zápise je package immutable.
