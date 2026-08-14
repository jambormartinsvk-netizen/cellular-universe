# K-N2/P3 — výsledok: plný A1 background verzus skrátený K7 rad

**Dátum:** 2026-07-15  
**Autoritatívny výsledok:** `scripts/results/k_mpc_005/RUN_KMPC_002_P3_A1_VS_K7_TRUNCATED_BACKGROUND.json`  
**Skript:** `scripts/235_script_KMPC_002_full_A1_vs_truncated_K7_background.py`  
**Limity:** vnútorný 5 s; vonkajší 10 s; reálny čas integrácie `1.047 s`.

## Rozsudok

**A1-PASS, K7-STOP.**

Presný zmrazený A1 background je v celom testovanom intervale kladný. Jeho
skorý, po `k`-cancelácii správne normalizovaný K7 rad však **nesmie byť
extrapolovaný až do dneška**: dosiahne nulu pri

```text
a = 0.70895788  (lineárne lokalizovaná mriežková hranica),
x približne -0.344,
```

a pri `a=1` dáva `D_K7,trunc=-24131.5578`, kým plný A1 dáva
`D_A1=10470.7875`.

## Kontrolné body

| `x` | `a` | plný `D_A1` | skrátený `D_K7,trunc` |
|---:|---:|---:|---:|
| -18 | `1.5230e-8` | 1.000052 | 1.000056 |
| -12 | `6.1442e-6` | 1.020884 | 1.022627 |
| -8 | `3.3546e-4` | 2.140251 | 2.235367 |
| -4 | `1.8316e-2` | 63.256758 | 68.449888 |
| -2 | `1.3534e-1` | 463.999709 | 502.138066 |
| 0 | 1 | 10470.787534 | **-24131.557805** |

Počiatočná zhoda je očakávaná: ide o skorý rad. Neskorá zmena znamienka je
fyzikálne neprípustná pre `H^2`, nie malá numerická odchýlka. Jej zdrojom je
záporný koeficient `1/(p+1)-1/2=-0.29720508` násobený rastúcim členom
`lambda a^2/sqrt(Omega_r0)`.

## Čo presne je mŕtve a čo ostáva živé

| Tvrdenie | Stav | Dôvod |
|---|---|---|
| „Skrátený K7 rad je celý neskorý FLRW background.“ | **MŔTVE** | pri konečnom `a<1` vytvára záporné `D`, teda imaginárne `H`. |
| K-N2/P1: algebraické odstránenie Fourierovho `k` z ranej formulácie | **ŽIVÉ** | tento beh ho netestoval ani nevyvracia. |
| K-N2/P2a: `A_f=7809.27010196` je určený zmrazeným A1 closure | **ŽIVÉ** | hodnotu používal bez nového fitu; problém je neskorá extrapolácia radu. |
| Plný A1 `D_A1(a)` ako pozitívny background kandidát | **ŽIVÉ, ale neprepojené s K7 poruchami** | kladnosť bola overená; musí sa nanovo odvodiť konzistentný perturbatívny operátor. |

## Dopad na A2-K4/K7/G8

Tento výsledok **neudeľuje skóre ani neodomyká CLASS adapter**. Zastavuje
len vetvu, ktorá by do CLASS vložila skrátený K7 výraz ako `H(a)`. Ďalšia
prípustná vetva musí vychádzať z plného `D_A1(a)` a znova odvodiť zdroje
porúch, constrainty a nulový limit; nemožno iba dosadiť `D_A1` do starých
K7 koeficientov bez odvodenia.

## História technického pokusu

Prvý pokus P3 skončil bez verdiktu na checkpointovom poradí (PF-037); jeho
dôvod aj oprava sú zachované v registračnom dokumente a error ledgeri.
Autoritatívny je až tento druhý beh s immutable JSON.

## Ďalší krok

Založiť samostatnú koľaj **K-N2/P4: exact-background rederivation** s tromi
oddelenými bránami: (1) odvodiť `H(a)` a `d tau/da` z `D_A1`; (2) odvodiť
každý K7 poruchový koeficient bez skráteného radu; (3) až potom porovnať
nulový limit a CLASS rozhranie. Bez týchto troch brán je náhrada iba
nezdokumentovaný patch.
