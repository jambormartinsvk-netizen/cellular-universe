# Pokyny externému auditorovi — EA-024

Najprv over `01_MANIFEST_SHA256.tsv`, source/copy paritu a úplnosť
`04_RUNTIME_DEPENDENCY_MAP.tsv`. Pracuj iba v čerstvých kópiách `REPRO`.

Over najmä:

- že dokumenty 168–174 vznikli pred príslušnými Python behmi;
- že PF-107…PF-110 sú oddelené od fyzikálnych verdiktov;
- raw KMPC-108 SHA `683D867D...9D995` a vnútorný register SHA
  `402B42E1...5EBF40`;
- 11 M1 stavov v decimal90, dva fuel stavy vo float-hex a autoritatívne
  kombinované poradie 13 stavov;
- presne šesť `mpf` konverzií a ich deklarované payload cesty;
- jediný audit false check `M3_driver`, worst
  `tight_coupling[7]=2.7715917114e-10 > 1e-10`;
- audit M3 independent holdout PASS, worst
  `Einstein_0i[7]=1.1636663777e-10 < 1e-9`;
- že KMPC-109 je read-only, prepočítava fingerprint bez solve a povoľuje iba
  exact resume;
- že C2/P5/K4 skóre ani verdikt nie sú zmenené.

Vykonaj dve izolované reprodukcie podľa dokumentu 03. Pre každý príkaz
zapíš exit code, wall time, SHA generated JSON a všetky odchýlky. Field-level
porovnanie smie odrátať iba `runtime_seconds`; každú ďalšiu odchýlku označ
osobitne. Zapečatený balík ani referenčné raw nemeň.
