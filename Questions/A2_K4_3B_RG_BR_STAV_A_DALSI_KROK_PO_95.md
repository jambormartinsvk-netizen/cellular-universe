# A2-K4.3b-RG-BR — stav a ďalší krok po skripte 95

**Stav:** `BR1 PASS; BR2 PASS; BR3A PASS; K4.3b NEUZAVRETÁ`  
**Kanonická maximálna hĺbka:** `60/100 = G6`  
**Aktívny krok:** `BR3B`

## Stav podkrokov

| Krok | Stav | Poznámka |
|---|---|---|
| BR1 — metric/transfer ledger | **PASS** | 19/19 identít |
| BR2 — skorá spätná reakcia | **PASS s explicitnou condition hranicou** | sedem módov, dve hĺbky, šesť ledgerov |
| BR3A — frakčné zdroje | **PASS** | 40/40 módových kontrol |
| BR3B — indukované frakčné koeficienty | **AKTÍVNY** | metric + všetky gravitačne viazané species |
| plná photon/polarization/recombination hierarchia | **ČAKÁ** | leading tight coupling nestačí na G7 |
| finálny rozsudok K4.3b/G7 | **ČAKÁ** | skóre sa zatiaľ nemení |

## Aktuálne fyzikálne čísla

Backgroundové prefaktory:

- `Omega_f ~ a^3.93109`;
- `(Gamma/H)(rho_f/rho_c) ~ a^4.93109`.

Úplné módové tlakové exponenty:

- AD `5.93109`;
- CDI `4.93109`;
- BI `4.93109`;
- NID `6.93109`;
- NIV `5.93109`.

Úplné ash-transfer exponenty:

- AD `6.93109`;
- CDI `4.93109`;
- BI `5.93109`;
- NID `7.93109`;
- NIV `6.93109`.

## BR3B akceptačné kritériá

1. jedna deklarovaná synchronous konvencia;
2. módovo správny frakčný exponent, bez zaokrúhlenia na integer;
3. plná hodnosť koeficientového systému po odstránení gauge módu;
4. konečné fyzikálne koeficienty bez negatívnej kinetickej normy;
5. koeficientové rezíduá `00`, `0i`, trace a traceless `ij`;
6. energy/momentum ledger;
7. dve štartové hĺbky alebo ekvivalentný asymptotický residual-scaling test;
8. TIMEOUT zostáva `NEUZAVRETÁ`, nie smrť.

## Dôvody, ktoré nie sú smrťou

- zle podmienená druhá numerická derivácia;
- catastrophic cancellation v surových `X_A`;
- round-off kompenzovaného velocity módu pod vopred odvodenou hranicou;
- JSON serializačná chyba;
- chýbajúci plný backend alebo timeout.

