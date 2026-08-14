# K-N2/P4b2a — kovariantný species ledger A2-K4 na presnom A1 backgrounde

**Stav:** `PASS pre Newtonovu-gauge species formuláciu.`  
**Otvorené:** transformácia do synchronnej projektovanej K7 bázy (P4b2b).

## Autorita a historické obmedzenie

`Audit/A2_00_kovariantny_ledger_zloziek_a_interakcii.md` opisuje v časti 3
vtedajšiu koľaj A2-K1 s prenosom rovnobežným s `u_c`. Pre A2-K4 sa **nesmie**
použiť ako rovnica pohybu. Autoritou pre definíciu K4 je
`Audit/A2_2_odvodenie_a_test_A2_K3_A2_K4.md`, časť 4: 

```text
Q_f^mu=-Gamma rho_f u_d^mu,   Q_c^mu=+Gamma rho_f u_d^mu,
(rho_c+delta rho_f) theta_d=rho_c theta_c+delta rho_f theta_f.
```

Starý konečný rozsudok M-011 v tomto historickom dokumente bol neskorším
auditom obmedzený; tu sa z neho používajú iba explicitne uvedené rovnice a
konvencie, nie starý finálny verdikt.

## Presná A1 energy-frame váha

Na plnom A1 backgrounde je

```text
beta_d(a) = delta X_f/[X_c+delta X_f],
theta_d = (1-beta_d) theta_c + beta_d theta_f,
gamma(a) = Gamma/H = lambda/E(a),
r(a)=X_f/X_c.
```

Tieto definície nemajú Fourierovo `k`. Pri ranej radiácii dávajú rovnaké
vedúce limity ako skorá K7 formulácia, ale ostávajú konečné aj mimo nej, ak
`X_c>0`.

## Kovariantné lineárne rovnice: znamienka a nulový limit

V Newtonovej gauge, s konformnou deriváciou, existujúci K4 ledger dáva:

```text
delta_c' + theta_c - 3 Phi'
 = a Gamma r (delta_f-delta_c+Psi),

theta_c' + Hconf theta_c - k^2 Psi
 = a Gamma r beta_d (theta_f-theta_c),

delta_f' + 3 Hconf(1-w_f)delta_f + delta theta_f
 + 9 Hconf^2(1-w_f^2) theta_f/k^2 - 3delta Phi'
 = -a Gamma[Psi+3 Hconf(1-w_f)theta_f/k^2],

theta_f' - 2 Hconf theta_f - k^2 delta_f/delta-k^2Psi
 = a Gamma/delta [(2-beta_d)theta_f-(1-beta_d)theta_c].
```

Tu `delta=1+w_f` a `delta Q=Gamma delta rho_f`. Znamienka toku sú párové:
zisk CDM je plus, strata paliva mínus. Pri `Gamma->0` všetky interakčné
členy zmiznú, zatiaľ čo neinteragujúce palivo, CDM, baryóny a radiácia
zostanú zachované. Toto je správny interaction-null limit definovaný v P4a.

Prechod na deriváciu podľa `x=ln a` nahrádza každý faktor
`a Gamma/Hconf` za `Gamma/H=gamma(a)`. To presne vysvetľuje, prečo staré
radiačné `g` musí byť v novom backgrounde `gamma=lambda/E`, nie
`lambda a^2/sqrt(Omega_r0)` pri každom `a`.

## Rozsudok

**P4b2a PREŠLA.** Zachovaný K4 operátor má úplný species-level kovariantný
ledger a jeho source termy majú na presnom A1 backgrounde jednoznačné
koeficienty a nulový limit. Neobjavil sa nový parameter ani piata sila.

To ešte **nie je** povolenie nahradiť `background()` v skripte 213. Ten je
v synchronnej, projektovanej báze `D,M`, kde sa musia nanovo odvodiť gauge
transformácie, product-rule členy a Einsteinove constrainty. Tento krok je
P4b2b/P4c a môže stále zlyhať na znamienku alebo neuzavretom constraint-e.

## Ďalší krok

Vytvoriť tabuľku jedna ku jednej: Newtonove species premenné → synchronné
species premenné → projektované `D,M`, vrátane derivácií exact-A1 váh.
Každý dodatočný product-rule člen musí mať separátnu algebraickú nulu alebo
Einsteinov constraint test pred vytvorením akéhokoľvek nového ODE runnera.
