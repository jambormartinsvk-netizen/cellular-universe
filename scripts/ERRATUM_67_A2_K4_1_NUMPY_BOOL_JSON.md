# Erratum skriptu 67 — JSON serializácia NumPy `bool`

**Dátum:** 2026-07-14  
**Pôvodný SHA-256:**
`20F54CA95515DAE9A267400C60B947534972C7B97D52D8FBC2E9BF89C5F32D67`

Prvý nezávislý fixed-RK4 beh dokončil obe integrácie, ale zlyhal pred JSON
výpisom:

```text
TypeError: Object of type bool is not JSON serializable
```

Išlo o `numpy.bool_` v slovníku kontrol. Oprava obalí výsledky kontrol
štandardným Python `bool(...)`. Rovnice, referenčná matica, integrátor,
kroky, prahy a numerické výsledky sa nemenia. Celý výpočet sa musí zopakovať;
prvý beh nevydal fyzikálny verdikt.

