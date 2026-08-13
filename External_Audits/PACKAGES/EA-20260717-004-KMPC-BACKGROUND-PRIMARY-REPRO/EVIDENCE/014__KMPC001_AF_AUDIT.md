# K-N2/P2a — výsledok: `A_f` zo zmrazeného A1-K1 backgroundu

**Dátum:** 2026-07-15  
**Autoritatívny strojový záznam:** `scripts/results/k_mpc_005/RUN_KMPC_001_A1_AF_FROZEN_BACKGROUND.json`  
**Skript:** `scripts/234_script_KMPC_001_A1_frozen_background_Af_audit.py`  
**Limity:** vnútorný 5 s na rozlíšenie; vonkajší 10 s.

## Ľudský význam

Nemusíme do opravenej ranej formulácie pridávať nové voľné číslo `A_f`.
Ak sa prijmú už zmrazené súčasné A1 hodnoty a jeho plochá uzávierka, spätná
integrácia jednoznačne určí skorý pomer paliva ku radiácii.

To je **parameter-bookkeeping PASS**, nie odvodenie celej A1 fyziky z buniek:
`Omega_m0`, `lambda`, `delta` a plochá uzávierka sú stále predpoklady
prechádzajúce z A1.

## Výsledok

Pre `p=4-3delta=3.93109` vyšiel limit

```text
A_f = 7809.270101963506  (najjemnejší RK4 krok dx=0.000125).
```

| Krok RK4 | `A_f` pri `x=-18` | Beh | Stav |
|---:|---:|---:|---|
| `0.0005` | `7809.270102038179` | `0.281 s` | konečný a kladný |
| `0.00025` | `7809.270101967679` | `0.531 s` | konečný a kladný |
| `0.000125` | `7809.270101963506` | `1.172 s` | konečný a kladný |

Relatívny rozdiel medium/fine je `5.343344047845171e-13`, teda hlboko pod
predregistrovaným limitom `1e-5`. Všetky hustoty a `E^2` boli kladné;
skript nemal žiaden vstup `K_MPC` ani Fourierovo `k`.

## Rozsudok

**PASS-P2a — `A_f` je odvodený zo zmrazeného A1-K1 closure, nie nový fit.**

Tým je opravený koeficient `Phi(k)=A_f(H0 sqrt(Omega_r0)/k)^p` numericky
určený bez zmrazenia ľubovoľného poruchového módu `k=0.05`.

## Čo výsledok nedokazuje

- Neodvodzuje mikrofyzikálny pôvod A1 vstupov ani flatness (**P2b ostáva
  otvorená**).
- Neoprávňuje použiť skrátený K7 rad ako plný pozdný background.
- Neudeľuje žiadne skóre A2-K4 ani neodomyká CLASS adapter.

## Ďalší krok

P3 musí oddeliť dve veci: (1) presný pozitívny A1 background a (2) oblasť,
kde je jeho skorý K7 rad po normalizácii `A_f` kvantitatívne použiteľný.
Ak je rad pri neskorom `a` nekladný, zomrie iba tvrdenie, že tento skrátený
rad je plný background; K-N2 ako normalizácia sa tým automaticky nezabije.
