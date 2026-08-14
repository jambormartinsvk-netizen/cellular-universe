# História balíka EA-022

## 2026-07-19 — DRAFT_NOT_DELIVERED

Balík zhromažďuje jednu ucelenú časť KMPC-093 až 100: technické HP-M1
successory, standalone matrix-provenance raw, read-only publication receipt
a interný audit. Theory author: Martin Jambor. Script creator/internal
auditor: Codex (OpenAI).

Runtime closure vychádza zo sealed EA-021 a je doplnená iba o runnery
337–344, moduly HP-M1 V1–V8 a nové raws. Balík sa nezapečatí pred dvoma
izolovanými fresh-copy vetvami, field-level kontrolou a úplným preflightom.

Prvý draft fresh-copy pokus fail-closed odhalil, že EA-021 nemal v `REPRO`
raw KMPC-092, pretože pre jeho vlastný runner bol generated target. V EA-022
je však KMPC-092 immutable prerequisite runnerov 343/344. Pred sealom sa
doplní presne tento jeden runtime vstup, regenerujú oba manifesty a obe
fresh-copy vetvy sa spustia odznova. Nevykonal sa matrix ani fyzikálny beh.

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

Po doplnení immutable KMPC-092 vstupu prešli obe izolované fresh-copy vetvy:

- KMPC-099 compile/help/smoke exit `0`; official exit `2` až po exclusive
  publish, wall time `3.806 s`, generated SHA
  `36C39560E094B868D457288757938ED4EAADC0F68B5B16128BDFCCFD27C9E545`;
  field-level obsah je zhodný s referenciou po odrátaní iba
  `runtime_seconds`;
- KMPC-100 compile/help/smoke/official exit `0`, official wall time
  `1.394 s`; generated SHA
  `2581BC157F0CBA08D91654A9BCE9976D93429D9DB6AA0FA2AE4765F05AD9CC1A`
  je byteovo zhodný s referenciou.

Manifest má `135` source/copy riadkov, runtime mapa `96` riadkov a draft
preflight po reprodukcii prešiel `887/887`. Po zmene iba package state a
history sa vykoná finálny preflight; evidence a runtime manifesty sa nemenia.
