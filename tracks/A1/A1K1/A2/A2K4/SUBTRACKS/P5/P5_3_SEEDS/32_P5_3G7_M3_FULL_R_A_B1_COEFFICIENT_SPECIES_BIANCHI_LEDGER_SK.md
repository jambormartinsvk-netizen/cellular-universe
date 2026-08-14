# P5.3g7-M3-FULL/R-A — B1 coefficient/species/Bianchi ledger

**Dátum:** 2026-07-16  
**Route:** `A1-K1 -> A2-K4 -> P5 -> P5.3g7-M3-FULL/R-A`  
**Rozsah:** analytická predimplementačná brána; bez Pythonu a bez ODE  
**Autoritatívny stav:** `REVIEW_B1_NOT_YET_CLOSED`  
**Dopad na hĺbku/skóre:** žiadny; K4 zostáva `60/100 = G6`  
**Technický counter:** zostáva `3/10`; pokus 4 nebol spustený

> **Neskorší autoritatívny snapshot:** dokumenty 34–36 uzavreli B1 ako
> `PASS_CONTRACT_PREFLIGHT_ONLY`; counter je `5/10` a seed pokus 6 je
> `NOT_RUN`. Pôvodný stav vyššie zostáva historickým stavom pri vzniku ledgeru.

## 1. Čo má B1 rozhodnúť

B1 má pred kódom určiť jediný úplný kontrakt prvého K4 metrického rádu:

1. ktoré mocniny amplitúdy palivového backgroundu a `z` sa násobia;
2. ktoré palivové koeficienty sú na tomto ráde naozaj potrebné;
3. presné synchronné fuel/ash species rows a tlak;
4. presnú paritu stavov a určujúcich rovníc;
5. total-energy, total-momentum a Bianchi left-null identity;
6. čo zostane nezávislým holdoutom.

Kým nie sú uzavreté všetky položky, nový runner ani solve nie je povolený.

## 2. Zmrazené konvencie

```text
x = ln a,
Hc = a H,
h_c = d ln(Hc)/dx,
z = k a/(H0 sqrt(Omega_r0)),
s2 = k^2/Hc^2,
U_A = Hc theta_A/k^2,
gamma = Gamma/H = lambda/E,
r = rho_f/rho_c,
beta = delta rho_f/(rho_c+delta rho_f),
U_d = (1-beta)U_c + beta U_f,
w_f = -1+delta,
c_s,f^2 = 1.
```

Background:

```text
rho_c,x = -3 rho_c + gamma rho_f,
rho_f,x = -(3 delta+gamma)rho_f.
```

Fourierovo `k` smie vstupovať do porúch cez `z` alebo `s2`; nesmie byť
holým parametrom `gamma`, `r`, `beta` ani homogénneho backgroundu.

## 3. B1.1 — dvojitá expanzia

Používa sa

```text
X(z,Phi) = sum_e X[0,e] z^e
         + Phi z^p sum_j X[1,j] z^j + O(Phi^2),
p = 4-3 delta,
Phi(k) = A_f [H0 sqrt(Omega_r0)/k]^p.
```

Takto `Phi z^p=A_f a^p` a background je módovo nezávislý. Pre fuel platí
`Omega_f[0]=0`, preto na prvom metrickom ráde

```text
[Omega_f delta_f]_[1,j] = sum_m Omega_f[1,m] delta_f[0,j-m],
[Omega_f U_f]_[1,j]     = sum_m Omega_f[1,m] U_f[0,j-m].
```

`delta_f[1]` a `U_f[1]` vstúpia do Einsteinových zdrojov až pri
`O(Phi^2)`. Toto obmedzuje staršiu skratku PF-058: chyba nebola iba v tom,
že frakčný gravitačný blok mal 11 namiesto 13 neznámych. Chýbala najmä
úplná a overená `Phi^0` fuel veža a jej dve coefficient rows.

**Stav B1.1:** `PASS_FORMULA_SCOPE`; ešte nie implementačný PASS.

## 4. Povinná `Phi^0` palivová veža

Ak `n` je vedúca mocnina `h_x`, regular leading pár je

```text
D_n = (n-1)(n+6-3 delta)+9(2-delta),
U_f[0,n] = -h_x[n]/(2 D_n),
delta_f[0,n] = delta(n-1)U_f[0,n].
```

| Mód | `n` | Povinné fuel rády v aktuálnom okne | Vedúci nenulový pár |
|---|---:|---|---|
| AD | 2 | `e=0,1,2` | `delta_f[0,2], U_f[0,2]` |
| CDI | 1 | `e=0,1` | `U_f[0,1]`; `delta_f[0,1]=0` |
| BI | 1 | `e=0,1` | `U_f[0,1]`; `delta_f[0,1]=0` |
| NID | 3 | `e=0,1,2,3` | `delta_f[0,3], U_f[0,3]` |
| NIV | 2 | `e=-1,0,1,2` | `delta_f[0,2], U_f[0,2]` |

Registrované `Phi^1` okná zostávajú AD `0..2`, CDI `0..1`, BI `0..1`,
NID `0..3`, NIV `-1..2`. Background convolution support musí siahať po
`m_max=2,1,1,3,3` v rovnakom poradí módov. NIV potrebuje `m=3`, lebo jeho
štandardná rýchlosť obsahuje vrstvu `e=-1`.

Rozšírenie cieľového okna automaticky vyžaduje predĺžiť fuel vežu; leading
pár sa nesmie zmraziť ako celá funkcia.

**Stav:** presný minimálny manifest je odvodený; coefficient extractor a
truncation-negative fixture ešte neexistujú.

## 5. B1.2 — presné synchronné fuel/ash rows

Zo zmrazeného

```text
Q_f^mu=-Gamma rho_f u_d^mu,
Q_c^mu=-Q_f^mu
```

vychádza v uvedenej konvencii:

```text
delta_c,x = -s2 U_c - h_x/2 + gamma r(delta_f-delta_c),
U_c,x = (h_c-1)U_c + gamma r beta(U_f-U_c),

delta_f,x = -3(2-delta)delta_f
            -delta(s2 U_f+h_x/2)
            -9delta(2-delta)U_f
            -3gamma(2-delta)U_f,

U_f,x = (h_c+2)U_f + delta_f/delta
        +(gamma/delta)(2U_f-U_d).
```

Povinná tlaková porucha je

```text
delta p_f/rho_f
 = delta_f +(2-delta)(3delta+gamma)U_f.
```

Je odvodená a term-by-term konzervačne overená v skripte 88 pri rovnakej
konvencii `U_A=Hc theta_A/k^2`; zhoduje sa so skriptom 95. Nie je dovolené
nahradiť ju iba `delta_f` ani trojnásobkom neadiabatickej časti.

**Stav B1.2:** `PASS_FORMULA_MAP` v scope zmrazeného efektívneho fluidu.
Uzávera `c_s,f^2=1`, nulový shear a `delta Gamma=0` zostávajú pracovnými
predpokladmi, nie mikrofyzikálnym odvodením.

## 6. PF-063 — nová chyba legacy M3 V1/V2

`mode_resolved_puiseux.py` zostavil

```text
delta_f +9delta(2-delta)U_f +3gamma(2-delta)U_f,
```

čiže trojnásobok správnej neadiabatickej časti tlaku. Ide o prenesenie
koeficientu z fuel continuity do pressure source. Následný Einstein trace
ho ešte legitímne násobí celkovým trace faktorom 9; problém je už vo vnútri
`fuel_pf`.

Dôsledok:

- V1/V2 ostávajú použiteľné pre k-cancel a M1 anchor v už obmedzenom scope;
- frakčné trace/holdout výsledky nie sú autoritatívne;
- chyba mohla prispieť k ich 21 FAIL, ale jej oprava sama negarantuje PASS;
- legacy JSON a skripty sa nemažú ani neprepisujú.

## 7. B1.3 — total species left-null identity

Definuj

```text
Delta_rho = sum_A rho_A delta_A,
W = sum_A (rho_A+p_A),
Momentum = sum_A (rho_A+p_A)U_A,
Delta_p = sum_A delta p_A,
Shear = total anisotropic-stress source.
```

Pri dosadení species rows a backgroundových product rules musí platiť

```text
Delta_rho,x = -3(Delta_rho+Delta_p)
              -s2 Momentum -(h_x/2)W,

Momentum_x = (h_c-4)Momentum+Delta_p-Shear.
```

Fuel loss a ash gain sa rušia až v absolútnych produktoch, nie porovnaním
samotných fractional rows. Tlakový `gamma(2-delta)U_f` člen je presne
potrebný na total-momentum kanceláciu.

Skript 88 dokazuje tieto dve plné symbolické identity. Nový R-A preflight ich
musí znovu extrahovať coefficient-by-coefficient na každom `(Phi^r,z^j)` a
exportovať explicitný convolution support.

## 8. Bianchi constraint-propagation left-null

Nech

```text
A=(aE)^2,
C00=q^2 eta -(A/2)h_x +(3/2)a^2 Delta_rho,
C0i=eta_x -(3/2)Momentum/E^2,
Ctr=A[h_xx+(h_c+2)h_x]-2q^2 eta+9a^2 Delta_p,
Ctl=A[h_xx+6eta_xx+(h_c+2)(h_x+6eta_x)]
    -2q^2 eta+9a^2 Shear.
```

Z background identít a total species konzervácie vyplývajú presné
propagačné identity

```text
C00_x + C00 - q^2 C0i + Ctr/2 = 0,
C0i_x +(h_c+2)C0i -(Ctl-Ctr)/(6A) = 0.
```

V implementácii sa najprv musia zostaviť absolútne species product rules a
až potom tieto kombinácie. Rekonštrukcia constraintu z neho samého,
`Q-Q=0`, lokálny rank alebo post-fit malé rezíduum nie sú left-null dôkaz.
`C00` a `C0i` zostanú mimo driver matice ako nezávislé holdouty.

**Stav B1.3:** plná identita je odvodená; coefficient-wise R-A extractor a
negatívne fixtures ešte neboli vykonané. Preto B1 zostáva REVIEW.

## 9. B1.4 — presná state/row parita M3-TCA0

```text
STATE = (
 h, eta, delta_gamma, delta_fs, delta_b, delta_c,
 U_gamma, U_fs, sigma_fs, U_b, U_c, delta_f, U_f
)

DRIVER = (
 gamma_continuity, gamma_Euler,
 fs_continuity, fs_shear, fs_Euler,
 baryon_continuity,
 cdm_continuity, cdm_Euler,
 tight_coupling,
 fuel_continuity, fuel_Euler,
 Einstein_trace, Einstein_traceless
)

HOLDOUT = (Einstein_00, Einstein_0i).
```

Presná parita je `13/13`. Blok je trojuholníkový: 11-zložková `Phi^1`
gravitačná odozva používa úplné `fuel[0]`; dvojica `fuel[1]` je spectator na
tomto ráde a nesmie sa vložiť do `O(Phi)` Einstein source. Je však prítomná,
aby sa overili obe rows a aby sa implementácia ticho nevydávala za plný
13-stavový kontrakt.

Toto je stále M3-TCA0, nie finite-opacity systém ani plná Boltzmannova
hierarchia.

## 10. Nulové a hraničné brány

Pokus 4 musí fail-closed overiť:

1. `gamma->0`: štandardný CDM + constant-`w` fuel fluid;
2. `A_f->0`: fuel/ash vážené zdroje zmiznú a metrický blok prejde na M1;
3. tri dynamické `k` pri rovnakom `a`: rovnaký background;
4. `k->0`: konečné `U_A`, teda `theta_A=O(k^2)`;
5. `rho_f->0`: vážený fuel source zmizne;
6. `rho_c->0`: fractional ash forma je singulárna a nesmie predstierať
   regularitu; potrebovala by absolútne premenné;
7. `delta->0`: fuel Euler má fyzikálny pól `1/delta`; audit platí pre
   zmrazené `delta=0.02297`, nie ako vacuum-limit dôkaz;
8. zakázaný `Omega_f[1]*fuel[1]` príspevok v `Phi^1` strese;
9. lower regular fuel coefficients musia byť explicitné nuly, nie chýbajúce
   kľúče;
10. state/row exact-set paritu a negatívne fixtures pre vynechaný alebo extra
    stav/riadok.

## 11. Rozsudok a ďalší krok

```text
REVIEW_B1_NOT_YET_CLOSED
```

R-A nezomrela. Presná fyzika species rows, tlak, minimálny coefficient
support a left-null identity sú identifikované. Pred technickým pokusom 4
ešte treba v samostatnom Markdown prerune zmraziť:

- konkrétnu dátovú schému coefficient extractorov a všetky negatívne fixtures;
- nezávislý frozen callable/hash pre M1 helper;
- S-C steam rail a K4-viazaný `h,eta` seed v deklarovanom scope;
- očakávané presné nuly a fail-closed výstup každého preflight checku.

Potom smie vzniknúť iba preflight bez solve ako technický pokus `4/10`.

## Neskorší stav vykonania

Tento dokument zachytáva stav pred kódom. Pokus 4 neskôr prešiel algebrou,
ale PF-064 obmedzila jeho lokálny contract guard. Pokus 5 zaviedol
samostatný frozen contract a prešiel `9/9` plus deväť negatívnych fixtures.
Aktuálny stav je `PASS_CONTRACT_PREFLIGHT_ONLY`, counter `5/10`; ďalší krok
je predregistrácia seedového pokusu 6. Dôkaz je v dokumentoch 34–36.
