# Pokyny externému auditorovi — EA-025

Najprv over `01_MANIFEST_SHA256.tsv`, source/copy paritu a úplnosť
`04_RUNTIME_DEPENDENCY_MAP.tsv`. Pracuj iba v čerstvej kópii `REPRO`.

Over najmä:

- že predregistrácie Evidence 006–008 predchádzali svojim Python behom;
- že PF-111/PF-112 nevydali fyzikálny payload a immutable failure SHA je
  `1ADCB30A...BD95E40`;
- checkpoint/receipt/state SHA `683D867D...9D995`,
  `21EF9A9B...28118F9`, `402B42E1...5EBF40`;
- explicitné poradie 11 M1 + 2 fuel stavov a publish-canonical parity;
- pôvodný audit false check `M3_driver`, worst
  `tight_coupling[7]=2.7715917114e-10 > 1e-10`;
- exact driver `8.6147582237e-82`, holdout `7.0711904227e-15` a
  `Einstein_0i[7]=3.3965448411e-15`;
- jeden exact solve, capture `104×104`, holdout `16×104`, zero fitted
  holdout rows, owners restored a no-CPQR-repeat;
- že projektový dopad je iba BI/.15 scoped PASS, C2 `6/10`, bez zmeny
  K4 `60/100`.

Vykonaj negatívny missing-prerequisite guard a izolovanú reprodukciu podľa
dokumentu 03. Pre každý príkaz zapíš exit code, wall time, SHA-256
generated JSON a všetky odchýlky. Field-level porovnanie smie odrátať iba všetky
`runtime_seconds`; každú ďalšiu odchýlku označ osobitne. Zapečatený balík,
Evidence 018 ani runtime vstupy nemeň.
