# Erratum skriptu 66 — JSON serializácia `numpy.int64`

**Dátum:** 2026-07-14  
**Pôvodný SHA-256:**
`35FD4590344B321A17DE1F92A45DDB8A756C79629F2F3AF08838D330278940CF`

Prvý beh dokončil symbolickú aj numerickú časť, ale zlyhal pred výpisom JSON:

```text
TypeError: Object of type int64 is not JSON serializable
```

Príčinou bol iba typ premennej `regular_count`, ktorý vznikol sčítaním
booleovských hodnôt NumPy. Oprava mení

```text
regular_count = sum(...)
```

na

```text
regular_count = int(sum(...))
```

Rovnice, parametre, počiatočné módy, integrátor, tolerancie, prahy ani
fyzikálna interpretácia sa nemenia. Po oprave sa musí celý výpočet spustiť
od začiatku; prvý beh nevydal verdikt.

