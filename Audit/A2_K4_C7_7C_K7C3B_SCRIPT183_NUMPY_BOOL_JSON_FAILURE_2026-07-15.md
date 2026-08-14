# A2-K4 / C7.7c / K7c.3b — technická smrť exportu skriptu 183

Dátum: 2026-07-15  
Stav skriptu 183: **MŔTVA TECHNICKÁ PODKOĽAJ**

Skript 183 prešiel cez seed aj pevné RK4 slučky, ale pri tvorbe JSON skončil s `TypeError('Object of type bool is not JSON serializable')`. Aspoň jedna kontrola niesla NumPy skalárny boolean namiesto vstavaného Python `bool`.

Keďže nevznikol úplný JSON s endpointmi a checkmi, výsledok sa nesmie spätne interpretovať ako PASS ani FAIL. Povolená oprava 184 pred `json.dumps` prevedie `checks = {key: bool(value) ...}`. Rovnice, kroky, počet krokov, seed, prahy a limity sa nemenia.

