# Pokyny externému auditorovi — EA-028

Najprv over `01_MANIFEST_SHA256.tsv`, source/copy paritu a úplnosť
`04_RUNTIME_DEPENDENCY_MAP.tsv`. Pracuj iba v čerstvých kópiách `REPRO`.

Over najmä:

- NIV/.005: KMPC-118 tail-only REVIEW, KMPC-119 verdict-free checkpoint a
  KMPC-120 PASS s `.01` tail `3.66649e-9/7.69530e-9`;
- NIV/.15: KMPC-121 core+tail REVIEW a KMPC-122 same-matrix core closure;
- KMPC-123 `checkpoint_complete=false`, accepted M3 driver
  `1.4819148859e-10`, a KMPC-124 fail-closed smoke bez fyziky;
- KMPC-125 technický post-processing failure pre chýbajúcu rank-130
  provenance, nie fyzikálny výsledok;
- KMPC-126 rank-104 accepted a rank-130 audit provenance, driver after
  `1.72471e-16/2.13943e-16`, holdout `9.60602e-11`, tail
  `2.80666e-12/3.40284e-12` a background `3.45586e-16`;
- že dopad je NIV mód closed a C2 atoms `10/10`, aggregate NOT_RUN a K4
  `60/100`.

Vykonaj negatívny guard a fresh-copy vetvy podľa dokumentu 03. Pre každý
príkaz zapíš presný príkaz, exit code, wall time a SHA-256 každého
generated JSON, ako aj každú odchýlku. Field-level porovnanie smie odrátať
iba polia `runtime_seconds` a normalizovať iba absolútny root prefix
`frozen_algebra_source`; relatívny suffix musí zostať zhodný. Zapečatený
balík ani Evidence súbory nemeň.
