# ERRATUM skriptov 43/44 — API dnešných hustôt

**Dátum:** 2026-07-13

Skript 43 sa zastavil pred výpočtom s `AttributeError`, pretože volal
neexportovanú pomocnú funkciu `omega_radiation_today`. Nevyprodukoval fyzikálny
výsledok.

Skript 44 používa validované rozhranie

```text
state0, X_b0 = initial_state(parameters)
X_f0 = state0[0]
X_c0 = Omega_m0-X_b0.
```

Rovnice škálovania, mriežka hodnôt `delta` a prahy sa nemenia. Skript 43 sa
zachováva ako auditná stopa neúspešného API volania.
