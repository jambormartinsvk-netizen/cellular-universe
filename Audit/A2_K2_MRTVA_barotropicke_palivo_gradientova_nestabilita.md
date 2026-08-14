# A2-K2 — mŕtva koľaj: barotropické palivo

**Dátum verdiktu:** 2026-07-13  
**Stav:** **MŔTVA — ARCHIVOVANÁ**  
**Typ smrti:** analytická gradientová nestabilita; numericky kvantifikovaná skriptom 21

## 1. Presná hypotéza

Palivo je striktne barotropická ideálna tekutina:

```text
p_f = w_f rho_f,
w_f = -1 + delta,
delta = 0.02297,
c_s,f^2 = c_a,f^2 = dp_f/d rho_f = w_f.
```

Prenos zostáva `Q^mu=Gamma rho_f u_c^mu`.

## 2. Analytický test

Z registrovanej hodnoty:

```text
w_f = -0.97703,
c_s,f^2 = -0.97703 < 0.
```

Hlavný krátkovlnný člen lineárnej skalárnej poruchy je lokálne

```text
delta_f'' + c_s,f^2 k^2 delta_f approximately 0.
```

Pri `c_s,f^2<0` je riešenie

```text
delta_f proportional exp(+|c_s,f| k eta)
```

namiesto zvukovej oscilácie. Lokálny algebraický zdroj `Q=Gamma rho_f` obsahuje členy bez dodatočnej kladnej hlavnej derivácie rádu `k^2`; nemôže teda opraviť záporný hlavný symbol pri ľubovoľne veľkom `k`.

Toto je gradientová nestabilita. Verdikt netvrdí ghostovú nestabilitu; tá je iný test.

## 3. Reprodukčný výpočet

Skript:

`scripts/21_script_A2_barotropic_fuel_gradient_instability.py`

Príkaz:

```powershell
python scripts/21_script_A2_barotropic_fuel_gradient_instability.py
```

Vstupy:

- `delta=0.02297`;
- `H0=66.37 km/s/Mpc`;
- `h=0.6637`;
- reprezentatívne `k=0.01, 0.1, 1.0 h/Mpc`.

Výsledok pri `z=0`:

| `k [h/Mpc]` | `mu/H0` | Čas jedného e-foldu `[H0^-1]` |
|---:|---:|---:|
| 0.01 | 29.633 | `3.3746e-2` |
| 0.1 | 296.329 | `3.3746e-3` |
| 1.0 | 2963.293 | `3.3746e-4` |

Už na veľkej lineárnej škále `0.01 h/Mpc` je okamžitá vysokofrekvenčná rastová miera takmer tridsaťkrát `H0`. Menšie škály sú horšie úmerne `k`.

## 4. Dôvod smrti

Koľaj porušuje základnú požiadavku gradientovej stability lineárnych porúch. Nestabilita je vlastnosť znamienka fyzikálnej pokojovej zvukovej rýchlosti, nie numerického integrátora ani výberu datasetu.

## 5. Čo verdikt nezabíja

Verdikt nezabíja:

- background A1-K1;
- A2-K1 s nezávislou efektívnou pokojovou zvukovou rýchlosťou `c_s,f^2=1`;
- skalárne pole alebo inú mikrofyziku, pri ktorej `w_f<0` neznamená `c_s,f^2=w_f`;
- koľaje s iným odvodeným kinetickým členom.

## 6. Podmienka novej koľaje

A2-K2 sa znovu neotvára zmenou gridu alebo tlmenia. Nová koľaj vyžaduje odvodenú mikrofyziku, ktorá mení hlavný kinetický/gradientový člen a dokazuje `c_s,f^2>=0` v celom používanom rozsahu.

## 7. Primárne metodické opory

- [Malik a Wands — interagujúce tekutiny a poruchy](https://arxiv.org/abs/astro-ph/0411703).
- [Valiviita, Majerotto a Maartens — nestability, ktoré background neodhaľuje](https://arxiv.org/abs/0804.0232).

Tieto práce poskytujú formalizmus a varovanie. Samotný verdikt A2-K2 vyplýva priamo zo záporného `c_s,f^2` v registrovanej barotropickej hypotéze.

