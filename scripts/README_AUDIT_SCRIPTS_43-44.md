# Reprodukcia singulárneho limitu A2-K5/K1 — skripty 43 a 44

**Dátum:** 2026-07-13

- `43_script_A2_K5_1_delta_zero_singular_limit.py` — zachovaný neúspešný beh;
  zastavil sa pred výpočtom na neexportovanom API;
- `44_script_A2_K5_1_delta_zero_singular_limit_fixed.py` — finálny nástupca
  cez validované `initial_state`;
- `ERRATUM_43_44_A2_K5_1_DELTA_LIMIT_API.md` — presný opis opravy.

Očakávané návratové kódy:

```text
script 43 -> 1
script 44 -> 0
```

Skript 44 potvrdzuje pri každom zmenšení `delta` faktorom 100:

```text
beta sa zväčší faktorom 10,
varphi_x sa zmenší faktorom 10,
beta varphi_x zostane konštantné.
```

Tým numericky reprodukuje presné analytické škálovanie
`beta proportional delta^(-1/2)` pri pevnom nenulovom backgroundovom toku.
