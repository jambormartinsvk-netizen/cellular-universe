# Pokyny externému auditorovi — EA-027

Najprv over `01_MANIFEST_SHA256.tsv`, source/copy paritu a úplnosť
`04_RUNTIME_DEPENDENCY_MAP.tsv`. Pracuj iba v čerstvých kópiách `REPRO`.

Over najmä:

- že Evidence 003/005 predregistrovali oba Python behy pred ich rawmi;
- KMPC-116 jedinú false bránu `M3_driver`, hodnotu
  `gamma_Euler[7]=4.1865589368e-10`, rank `104/104` a independent holdout
  `6.5626998417e-11 < 1e-9`;
- že KMPC-116 tail `.01` ostal pod `1e-6`: F0 `1.2341868098e-7`, M3
  `6.8290603608e-8`;
- KMPC-117 exact same-matrix/constant identitu, tri corrections, zmenu
  drivera `4.1865589368e-10→1.3513985475e-16` a nezávislý holdout
  `1.4373221568e-11`;
- že holdout nie je súčasťou fitu a všetky frozen brány KMPC-117 sú true;
- že dopad je iba scoped NID/k=.15 PASS, uzavretie NID módu, C2 `8/10`,
  bez zmeny K4 `60/100`.

Vykonaj negatívny missing-prerequisite guard a dve čisté nezávislé
reprodukčné vetvy podľa dokumentu 03. Pre každý príkaz zapíš presný príkaz,
exit code, wall time a SHA-256 každého generated JSON, ako aj každú
odchýlku. Field-level porovnanie smie odrátať iba všetky polia
`runtime_seconds` a normalizovať iba absolútny root prefix
`frozen_algebra_source`; jeho relatívny source suffix musí zostať presne
zhodný. Každú ďalšiu odchýlku označ osobitne. Zapečatený balík ani Evidence
súbory nemeň.
