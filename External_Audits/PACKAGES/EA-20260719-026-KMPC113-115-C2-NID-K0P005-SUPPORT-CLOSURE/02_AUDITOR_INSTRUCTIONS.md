# Pokyny externému auditorovi — EA-026

Najprv over `01_MANIFEST_SHA256.tsv`, source/copy paritu a úplnosť
`04_RUNTIME_DEPENDENCY_MAP.tsv`. Pracuj iba v čerstvých kópiách `REPRO`.

Over najmä:

- že Evidence 003/005/007 predregistrovali každý Python beh skôr, než vznikol
  jeho raw, a nezmenili rovnice ani prahy;
- KMPC-113 netail PASS a tail-only REVIEW: na `.01` F0 `1.1184032923e-5`,
  M3 `2.4036752636e-5`, oba worst state `delta_f`;
- KMPC-114 verdict-free rolu, 9/9 preconditions, M1 depth 9, accepted
  `[0,7]` a checkpoint SHA `339FD13B...B35195`;
- KMPC-115 checkpoint guards, 13-state order, ranky F0 `20/20`, M3
  `130/130`, M1 `120/120` a independent `00/0i` holdout;
- KMPC-115 `.01` tail F0 `2.7843150709e-9`, M3 `8.9418819803e-9`,
  driver M3 `1.6132606588e-11`, holdout `4.2396377958e-13` a background
  `1.1519529664e-16`;
- že dopad je iba scoped NID/k=.005 PASS, C2 `7/10`, bez zmeny K4 `60/100`.

Vykonaj negatívny missing-prerequisite guard a tri čisté nezávislé
reprodukčné vetvy podľa dokumentu 03. Pre každý príkaz zapíš presný príkaz,
exit code, wall time
a SHA-256 každého generated JSON, ako aj každú odchýlku. Field-level
porovnanie smie odrátať iba všetky polia `runtime_seconds` a normalizovať
iba absolútny root prefix `frozen_algebra_source`, pričom jeho relatívny
suffix musí zostať presne zhodný. Každú ďalšiu odchýlku označ osobitne.
Zapečatený balík ani Evidence súbory nemeň.
