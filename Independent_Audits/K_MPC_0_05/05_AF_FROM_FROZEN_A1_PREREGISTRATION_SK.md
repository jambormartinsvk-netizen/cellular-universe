# K-N2/P2 — predregistrácia: určenie `A_f` zo zmrazeného A1-K1 backgroundu

**Stav pred behom:** `PRIPRAVENÉ`  
**Súvisiaci skript:** `scripts/234_script_KMPC_001_A1_frozen_background_Af_audit.py`  
**Vonkajší limit behu:** 10 s. **Vnútorný limit skriptu:** predvolene 5 s.

## Otázka

Je skorý koeficient

```text
A_f = lim_(a->0) [(rho_f/rho_r)/a^p],  p=4-3delta,
```

novým voľným parametrom, alebo je už určený zmrazeným A1-K1 backgroundom?

## Vstupy bez nového fitu

Preberajú sa presne deklarované hodnoty skriptu 11:

```text
h=0.6637, Omega_m0=0.3517, lambda=0.15, delta=0.02297,
Delta_Neff=0.0535, omega_b=0.02237.
```

Dnešné palivo nie je nová voľba: flat A1 closure určuje

```text
X_f0 = 1 - Omega_m0 - Omega_r0.
```

Skript integruje tieto už zmrazené A1 rovnice spätne z `a=1`:

```text
X_f,x = -3delta X_f - lambda X_f/E,
X_m,x = -3X_m + lambda X_f/E,
X_r,x = -4X_r,
E^2 = X_f+X_m+X_r.
```

## Očakávaný výsledok

V ranej radiačnej oblasti má `A_f(x)=(X_f/X_r)/a^p` konvergovať na konečné
kladné číslo. Tri rozlíšenia RK4 (`dx=5e-4, 2.5e-4, 1.25e-4`) musia dať
zhodné limitné hodnoty; výsledok nesmie používať `K_MPC`, Fourierovo `k` ani
nový voľný vstup.

## PASS / STOP

- **PASS-A (numerický):** všetky hustoty a `E^2` sú konečné a kladné;
  limit `A_f` je kladný; rozdiel dvoch najjemnejších krokov je pod `1e-5`.
- **STOP-A:** nekladnosť, nekonečnosť, nedokončenie v limite alebo
  nekonvergencia.
- **Interpretácia po PASS-A:** `A_f` nie je *dodatočný numerický parameter*
  nad deklarovaným A1 closure. To **nie je** mikroskopické odvodenie
  `Omega_m0`, `lambda` ani flatness zo siete; ich status zostáva oddelene
  evidovaný.

## Ďalší postup

Pri PASS-A sa výsledné `A_f` smie použiť iba ako odvodená hranicová hodnota
pre samostatný, predregistrovaný full-background test `D_univ(a)`. Pri
STOP-A sa K-N2 neuzavrie a chyba/hranica sa zdokumentuje bez prepisovania
starých behov.

## Poznámka k prvému technickému pokusu (2026-07-15)

Prvý pokus skončil pred fyzikou na `ModuleNotFoundError: No module named
'scripts.baseScripts'` (PF-036). Nevznikol numerický výsledok ani JSON a stav
brány sa tým nemení. Príčinou bol chybný importný koreň pri spustení zo
`scripts`; teraz sa opakuje identický predregistrovaný beh s opraveným
importom.
