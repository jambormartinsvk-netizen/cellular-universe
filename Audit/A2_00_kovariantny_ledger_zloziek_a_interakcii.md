# A2.0 — kovariantný ledger zložiek a interakcií

**Dátum:** 2026-07-13  
**Aktívna koľaj:** A2-K1  
**Rozsah:** efektívna všeobecne-relativistická formulácia; nie mikroskopická akcia bunkovej siete  
**Verdikt A2.0:** **PREŽÍVA 48/100; bilančná brána prešla, perturbačná stabilita nebola rozhodnutá**

## 1. Konvencie

- signatúra metriky: `(-,+,+,+)`;
- normalizácia: `g_mu_nu u_A^mu u_A^nu = -1`;
- projektor: `h_A^(mu nu)=g^(mu nu)+u_A^mu u_A^nu`;
- Einsteinove rovnice sa v A2 používajú ako efektívna makroskopická gravitácia;
- `nabla_mu G^(mu nu)=0` vyžaduje `nabla_mu T_tot^(mu nu)=0`.

Pre všeobecnú zložku:

```text
T_A^(mu nu) = (rho_A+p_A)u_A^mu u_A^nu
              + p_A g^(mu nu) + pi_A^(mu nu).
```

Pre fotóny, neutrína a voľne prúdiacu paru je `pi_A^(mu nu)` vo všeobecnosti nenulové a v A3 sa musí získať z Boltzmannovej hierarchie.

## 2. Zložky aktívneho kozmologického ledgeru

| ID | Zložka | Background | Perturbačná uzávera A2-K1 | Bunkový zdroj |
|---|---|---|---|---|
| `f` | palivo | `w_f=-1+delta=-0.97703` | `c_s,f^2=1`, `pi_f=0` ako efektívny postulát | `-Q^mu` |
| `c` | CDM/popol | `w_c=0` | `c_s,c^2=0`, `pi_c=0` | `+Q^mu` |
| `b` | baryóny | po rekombinácii približne prach; predtým termálny tlak podľa štandardnej fyziky | štandardná baryónová kontinuita/Euler + Thomson | `0` |
| `gamma` | fotóny | `w=1/3` | Boltzmannova hierarchia, Thomson s baryónmi | `0` |
| `nu` | štandardné neutrína | relativistická alebo hmotná história podľa zvolenej bázy | štandardná Boltzmannova hierarchia | `0` |
| `s` | para/gravitónový relikt | v tomto kroku iba nezávisle zachovaná relativistická zložka | voľné prúdenie alebo tekutinová uzávera sa musí určiť v A4 | `0` po jej vzniku |

### Doména I

Doména I sa v A2-K1 **nezapočítava ako samostatný tenzor energie a hybnosti**, pretože teória zatiaľ neurčila jej lokálnu hustotu, tlak, štvorrýchlosť ani prenos. Je evidovaná ako otvorená Q8.

Ak doména I fyzicky nesie energiu alebo hybnosť, musí dostať `T_I^(mu nu)` a `Q_I^mu`; inak by bola skrytým rezervoárom a A2-K1 by neprešla bilanciou.

### Para

Ledger A2 opisuje obdobie po zadanom vzniku/decouplingu pary. Q18/Q23 musia neskôr odvodiť jej zdrojovú históriu. Ak sa para tvorí z paliva počas kozmologického vývoja, musí sa zaviesť dvojica `-S_s^mu` v palive a `+S_s^mu` v pare. Súčasný background tento kanál neobsahuje.

## 3. Kovariantný bunkový prenos

Definujeme lokálny skalár hustoty paliva

`rho_f = T_f^(mu nu) u_f,mu u_f,nu`

a konštantnú efektívnu mieru `Gamma` s rozmerom inverzného času. Aktívna koľaj volí

```text
Q^mu = Gamma rho_f u_c^mu,
Q_f^mu = -Q^mu,
Q_c^mu = +Q^mu.
```

Zápis je kovariantný, ak `Gamma` je konštantný skalár parametra efektívnej teórie.

### Dôležité obmedzenie `Gamma=lambda H0`

Fyzikálna definícia musí byť `Gamma = constant`. Vzťah

`lambda = Gamma/H0`

je potom iba bezrozmerná parametrizácia voči dnešnej referenčnej hodnote. Ak by `H0` v lokálnom zákone znamenalo ne-lokálne nameranú vlastnosť celého vesmíru, mikrofyzikálny zákon by nebol lokálne odvodený. Ak by sa namiesto toho použila lokálna expanzia `Theta/3`, vznikol by iný model `Q proportional H rho_f`, ktorý nereprodukuje presne V1 a musí dostať novú koľaj.

## 4. Úplné bilančné rovnice

```text
nabla_mu T_f^(mu nu)     = -Q^nu
nabla_mu T_c^(mu nu)     = +Q^nu
nabla_mu T_b^(mu nu)     = +C_bg^nu
nabla_mu T_gamma^(mu nu) = -C_bg^nu
nabla_mu T_nu^(mu nu)    = 0
nabla_mu T_s^(mu nu)     = 0
```

Tu `C_bg^nu` označuje štandardnú baryónovo-fotónovú kolíznu výmenu. Presné štandardné neutrínové kolízne členy sa pred decouplingom pridajú v pároch so súčtom nula.

Súčet dáva identicky:

```text
sum_A nabla_mu T_A^(mu nu)
= -Q^nu + Q^nu + C_bg^nu - C_bg^nu
= 0.
```

Brána celkového zachovania energie a hybnosti teda prešla konštrukciou.

## 5. Energia a hybnosť v jednotlivých rámcoch

Pre ľubovoľný referenčný rámec `u^mu`:

```text
Q_A^mu = Q_A u^mu + F_A^mu,
u_mu F_A^mu = 0.
```

V CDM rámci:

```text
Q_c = +Gamma rho_f,
F_c^mu = 0.
```

CDM preto z tohto prenosu nedostáva dodatočnú silu vo svojej Eulerovej rovnici. To neznamená, že jeho kontinuitná rovnica zostane štandardná.

V rámci paliva, do prvého rádu v relatívnej rýchlosti:

```text
Q_f approximately -Gamma rho_f,
F_f^mu = -Gamma rho_f h_f^mu_nu u_c^nu.
```

Palivo teda všeobecne cíti hybnostnú výmenu, keď `u_f^mu != u_c^mu`. Tvrdenie „prenos hybnosti je nulový“ platí iba pre projekciu do CDM rámca.

## 6. Porucha skalára prenosu

Pre konštantné `Gamma` a lokálne `Q=Gamma rho_f` je v konkrétnej gauge

`delta Q = Gamma delta rho_f`.

Samotné `delta rho_f` je gauge-dependentné; fyzikálny výpočet musí použiť celý perturbovaný štvorvektor alebo gauge-invariantnú kombináciu. Nesmie sa dosadiť `delta Q=0` iba preto, že backgroundová `Gamma` je konštantná.

## 7. Obnova FRW backgroundu

V homogénnej limite, pre `x=ln a`:

```text
rho_f' = -3 delta rho_f - (Gamma/H)rho_f
rho_c' = -3 rho_c + (Gamma/H)rho_f
rho_b' = -3 rho_b
rho_r' = -4 rho_r.
```

Po `Gamma=lambda H0` ide presne o A1-K1/V1 background. Tým je splnená požiadavka, že A2 nemení už overený background potichu.

## 8. Palivová uzávera a koľaje

Background `p_f=w_f rho_f` neurčuje pokojovú fyzikálnu zvukovú rýchlosť. Preto vznikli samostatné koľaje:

- **A2-K1:** `c_s,f^2=1`, `pi_f=0`; aktívny efektívny scalar-like kandidát;
- **A2-K2:** `c_s,f^2=w_f=-0.97703`; mŕtva gradientovou nestabilitou;
- A2-K3/K4 menia smer prenosového štvorvektora;
- A2-K5 vyžaduje mikroskopickú akciu.

Voľba `c_s,f^2=1` nevytvára ghost automaticky, ale ani nedokazuje jeho neprítomnosť. Ghost test vyžaduje kvadratickú akciu alebo ekvivalentnú kontrolu kinetickej matice; tá v A2.0 ešte neexistuje.

## 9. Auditné brány A2.0

| Test | Výsledok | Stav |
|---|---|---|
| L0 — komponenty | Palivo, CDM, baryóny, fotóny, neutrína a para sú oddelené. Doména I je explicitne vylúčená, kým nemá `T_I`. | **PREŠIEL V DEKLAROVANOM ROZSAHU** |
| L1 — celková bilancia | Bunkový aj štandardný kolízny prenos sa párovo vyrušujú. | **PREŠIEL** |
| L2 — lokálna kovariancia | `rho_f` je skalár, `u_c^mu` vektor, `Gamma` konštantný skalár. | **PREŠIEL EFEKTÍVNE** |
| L3 — rámec hybnosti | `F_c^mu=0` iba v CDM rámci; palivová protihybnosť je evidovaná. | **PREŠIEL** |
| L4 — baryóny | Bunkový zdroj baryónov je nula; Thomsonova výmena zostáva štandardná. | **PREŠIEL** |
| L5 — FRW limita | Presne obnovuje A1-K1/V1. | **PREŠIEL** |
| L6 — uzávera paliva | A2-K1 je definovaná; barotropická A2-K2 bola zabitá. Mikrofyzický pôvod `c_s^2=1` chýba. | **ČIASTOČNE** |
| L7 — para | Po vzniku zachovaná; história zdroja čaká Q18/Q23. | **ČIASTOČNE** |
| L8 — doména I | Žiadne dvojité započítanie; fyzikálny `T_I` čaká Q8. | **OTVORENÉ MIMO ROZSAHU A2-K1** |

## 10. Verdikt

Kovariantný ledger A2-K1 je bilančne životaschopný a **postupuje do A2.1**. Nie je potvrdená jeho stabilita.

Najväčšie riziko je známe z triedy interagujúcich konštantných-`w` tekutín: na superhorizontových škálach môžu vzniknúť neadiabatické rastové módy, ktoré background vôbec neukáže. Výsledky literatúry nemožno automaticky preniesť, pretože konkrétny skalár prenosu a znamienko sa líšia; treba odvodiť vlastný dominantný mód A2-K1.

## 11. Zdroje a rozsah ich použitia

- [Malik a Wands](https://arxiv.org/abs/astro-ph/0411703): všeobecný gauge-invariantný formalizmus viacerých interagujúcich tekutín.
- [Valiviita, Majerotto a Maartens](https://arxiv.org/abs/0804.0232): dôkaz, že backgroundová konzistencia jednoduchého interagujúceho constant-`w` modelu nezaručuje stabilné poruchy. Ich model nie je totožný s A2-K1.
- [Clemson et al.](https://arxiv.org/abs/1109.6234): fyzikálne rozdiely medzi voľbami smeru prenosového štvorvektora.
- [Yang a Xu](https://arxiv.org/abs/1409.5533): príklad, že perturbovanie skalára použitého v interakcii musí byť špecifikované.
- [Interacting Dark Sectors in light of DESI DR2](https://arxiv.org/abs/2503.21652): moderný príklad, v ktorom sa interakcia testuje v backgrounde aj perturbáciách.

