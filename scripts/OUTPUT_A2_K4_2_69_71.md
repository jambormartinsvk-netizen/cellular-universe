# Výstup skriptov 69–71 — A2-K4.2

**Dátum:** 2026-07-14  
**Rozsah:** analytický high-`k` symbol, kompletná regulárna subhorizontová báza,
nulový limit a numerická konvergencia  
**Pravidlo času:** analytika `10 s` interne/`15 s` externe; každý samostatný
numerický beh `50 s` interne/`60 s` externe; spoločný konvergenčný beh
`50 s` interne/`60 s` externe. Nijaký beh neskončil timeoutom.

## 1. Reprodukovateľné skripty

- `69_script_A2_K4_2_high_k_principal_symbol.py`;
- `70_script_A2_K4_2_subhorizon_regular_basis.py`;
- `71_script_A2_K4_2_q300_convergence_gates.py`.

Skript 70 importuje rovnice, tri regulárne módy a auditnú normu priamo zo
skriptu 66. K4.2 preto nemení systém po výsledku K4.1 a nepridáva priaznivo
zvolený počiatočný mód.

## 2. Analytický výsledok skriptu 69

Pre premenné

```text
z = [delta_c, v_c, delta_f, v_f, delta_b, v_b, delta_r, v_r],
v_A = theta_A/k,
z_eta = k P z + O(k^0)
```

vyšiel charakteristický polynóm

```text
det(mu I-P) = mu^4 (mu^2+1) (mu^2+1/3).
```

Charakteristické rýchlosti sú

```text
0, 0, 0, 0, -1/sqrt(3), +1/sqrt(3), -1, +1.
```

Všetky propagujúce sa rýchlosti sú reálne a kauzálne. Palivový a radiačný
blok sú diagonalizovateľné. Koeficient interakcie `lambda` sa nachádza iba v
ráde `k^0`, nemení hlavný symbol a pri `lambda=0` algebraicky zmizne.

Plný symbol nie je silne hyperbolický kvôli dvom nulovým Jordanovým blokom
beztlakového CDM a baryónov: nulová vlastná hodnota má algebraickú násobnosť
4 a geometrickú násobnosť 2. Rovnaký defekt je prítomný aj pri `lambda=0`;
ide o štandardné obmedzenie efektívneho prachu, nie o novú nestabilitu K4.

Efektívna kinetická váha paliva je `delta rho_f/c_s^2>0` pre
`delta=0.02297`, `rho_f>0`, `c_s^2=1`. Toto je iba test efektívnej tekutiny;
bez mikroskopickej akcie nejde o fundamentálnu UV no-ghost vetu.

**Výstup:** `PASS_ANALYTIC_K4_2`, čas `0.25 s`.

## 3. Úplná regulárna subhorizontová báza — lambda=0.15

Základné nastavenie: `x_start=-20`, krok pozadia `1.25e-4`, DOP853,
`rtol=1e-9`, `atol=1e-12`, 1601 výstupných bodov. Aproximácia fyzikálnej
škály používa `k[h/Mpc] ~= q/2997.9`.

| `q=k/H0` | približné `k [h/Mpc]` | `q/(aE)` na štarte | `nfev` | max. singulárny transfer | `1e-5 T_max` | max. aktívne bodové rel. `00` rezíduum | čas |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 0.0100 | `6.32732e-6` | 2 978 | 428.708871 | 0.00428709 | `3.35198e-8` | 3.844 s |
| 300 | 0.1001 | `6.32732e-5` | 16 019 | 9 922.028740 | 0.0992203 | `9.98911e-9` | 4.469 s |
| 1000 | 0.3336 | `2.10911e-4` | 47 222 | 24 001.695397 | 0.240017 | `4.41484e-8` | 6.219 s |

Všetky tri módy — adiabatic, CDM-density isocurvature a baryon-density
isocurvature — boli integrované súčasne. Všetky hodnoty boli konečné.
Počiatočné relatívne rezíduá constraintu boli najviac `2.32e-16`.

Aktívny bod je definovaný podmienkou
`term_norm > 1e-12 * global_max_term_norm`; až na týchto bodoch sa počíta
`abs(residual)/term_norm`. Tým sa nevyhlasuje delenie numerického šumu
numerickým šumom za úspech.

## 4. Nulový limit — lambda=0

| `q` | `T_max`, K4 (`lambda=0.15`) | `T_max`, nulový limit | pomer K4/nulový limit | interpretácia |
|---:|---:|---:|---:|---|
| 30 | 428.708871 | 431.240185 | 0.9941 | K4 nepridáva rast |
| 300 | 9 922.028740 | 10 631.990904 | 0.9332 | K4 rast mierne tlmí |
| 1000 | 24 001.695397 | 26 457.831457 | 0.9072 | K4 rast mierne tlmí |

Veľké absolútne transfery sú teda hlavne štandardným rastom prachových
hustôt na subhorizontových škálach. Nie sú novou interakčnou explóziou:
pri vypnutí K4 sú väčšie. Toto porovnanie nie je tvrdenie o zhode s CMB alebo
`S8`; na to treba fyzikálnu primordiálnu normalizáciu a Boltzmannovu hierarchiu.

## 5. Konvergenčné brány skriptu 71 pri q=300

| zmena | relatívna zmena finálnej observabilnej matice | limit | výsledok |
|---|---:|---:|---|
| `rtol 1e-9 -> 3e-10`, `atol 1e-12 -> 3e-13` | `2.10624e-8` | `<1e-5` | PASS |
| krok pozadia `1.25e-4 -> 2.5e-4` | `7.02159e-8` | `<1e-4` | PASS |
| štart `x=-20 -> -22` | `1.99290e-6` | `<1e-4` | PASS |

Celý štvorbeh skončil za `20.844 s`. Najhoršie aktívne bodové relatívne
rezíduum v štvorbehu bolo `4.11699e-8`.

## 6. Strojový rozsudok a auditná interpretácia

```text
script 69: PASS_ANALYTIC_K4_2
script 70: všetkých 6 deklarovaných K4/null behov dokončených
script 71: PASS_K4_2_CONVERGENCE
audit: PREŠLA K4.2 V PERFECT-RADIATION ROZSAHU
stav: PREŽÍVA K4.2 — 59/100
```

Skóre 59/100 nie je plný A2 ani observačný úspech. Otvorenou bránou je
K4.3: plná fotónová a neutrínová Boltzmannova hierarchia, anizotropný stres,
baryón-fotónová väzba, rekombinácia, gauge krížová kontrola a až potom
CMB-normalizovaný rast/`S8`.

