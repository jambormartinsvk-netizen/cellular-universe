# A2-K5.0 — kanonická skalárna akcia, rekonštrukcia a rastové riziko

**Dátum:** 2026-07-13  
**Koľaj:** A2-K5/K1  
**Verdikt:** `PREŽÍVA IBA K5.0 — 45/100; RASTOVÁ BRÁNA ČERVENÁ`  
**Nie je to:** potvrdená mikrofyzika bunkovej siete ani plná predikcia `S8`

## 1. Rozsah rozsudku

Koľaj K5/K1 prešla konštrukciou lokálnej akcie, znamienkami, presnou
backgroundovou rekonštrukciou, ghost/gradient bránou a backgroundovým testom
efektívnej hmotnosti. Prvý subhorizontový test však ukázal, že povinná piata
sila preváži nad prídavným trením a zvýši rast hmoty. Konečný observačný
rozsudok sa odkladá iba preto, že zatiaľ chýba úplný relativistický
Boltzmannov výpočet s CMB normalizáciou.

Skóre `45/100` vyjadruje zrelosť dôkazu, nie 45-percentnú pravdepodobnosť.

## 2. Hypotéza a konvencie

Použitá Einstein-frame akcia je

```text
S = integral d^4x sqrt(-g) [Mpl^2 R/2 - (partial phi)^2/2 - V(phi)]
    + S_c[A(phi)^2 g_mu_nu, psi_c]
    + S_b[g_mu_nu, psi_b] + S_r[g_mu_nu, psi_r].
```

Definujeme

```text
varphi = phi/Mpl,
beta(varphi) = d ln A/d varphi,
T_c = -rho_c.
```

Potom

```text
nabla_mu T_c^(mu nu) = (beta/Mpl) T_c nabla^nu phi,
rho_c,dot + 3 H rho_c = + beta varphi,dot rho_c,
phi,ddot + 3 H phi,dot + V_,phi = - (beta/Mpl) rho_c.
```

Súčet skalárneho a CDM tenzora je zachovaný. Znamienko znamená, že pri
`beta varphi,dot>0` rastie hmotnosť CDM a energia tečie z paliva do popola.

Literatúra často používa opačné znamienko parametra. V konvencii Barros et
al. je presné mapovanie `beta_Barros = -beta_tu`; bez tohto mapovania by sa
obrátili backgroundový zdroj aj trecí člen.

## 3. Presná rekonštrukcia A1-K1

Nech `x=ln a`, `E=H/H0`, `X_i=rho_i/(3 H0^2 Mpl^2)`, `w_f=-1+delta` a
`Gamma=lambda H0`. Kanonický skalár dáva

```text
varphi_x = sqrt(3 delta X_f)/E,
beta = lambda sqrt(X_f)/(X_c sqrt(3 delta)),
V/(3 H0^2 Mpl^2) = (1-w_f) X_f/2.
```

Tým sa identicky obnoví

```text
beta H rho_c varphi_x = lambda H0 rho_f = Gamma rho_f.
```

Nezávislá identita meniacej sa hmotnosti je

```text
A(a)/A0 = X_c(a) a^3/X_c0,
d ln A/dx = lambda X_f/(E X_c).
```

Skript 32 našiel maximálnu relatívnu chybu zdroja `6.66e-16` a maximálnu
chybu identity `ln A` `5.06e-9`.

## 4. Nulové a hraničné limity

### 4.1 Regulárny nulový limit

Pri `lambda -> 0` a pevnom `delta>0` platí `beta->0`, `A->konštanta` a
`Q->0`. Zostane minimálne viazané CDM a kanonické kvintesenciálne pole.

### 4.2 Singulárny limit, ktorý sa nesmie zamlčať

Pri `delta -> 0` a pevnom nenulovom `lambda` platí

```text
varphi_x -> 0,
beta proportional lambda/sqrt(delta) -> infinity.
```

Kanonické pole teda nemôže mať presne vákuový stav `w_f=-1` a súčasne
konečný tok `Gamma rho_f` s konečnou konformnou väzbou. Regulárny spoločný
limit vyžaduje aspoň `lambda/sqrt(delta)->0`. Toto obmedzuje staršie slovné
formulácie, v ktorých sa `w=-1` a nenulové trávenie mohli uvádzať súčasne.

## 5. Lokálne stabilitné brány

- kanonický kinetický člen má správne znamienko;
- `rho_f+p_f=delta rho_f>0` pre registrované `delta=0.02297`;
- hlavný skalárny mód má `c_s^2=1`;
- konformná väzba nepridáva vyššiu časovú deriváciu;
- rekonštruované funkcie sú konečné od `z*=1089.9` po dnešok;
- skript 35 našiel minimum `m_phi^2/H0^2=2.6624256` a minimum
  `m_eff^2/H0^2=21.5384259`, obe dnes a obe kladné;
- kroková konvergencia týchto miním je lepšia než `1.84e-7`.

Tieto body sú backgroundová a hlavnosymbolová kontrola. Nenahrádzajú úplnú
kvadratickú akciu so všetkými gravitačnými a hmotovými módmi.

## 6. Neodstrániteľná väzba trenia a piatej sily

Rekonštrukcia dáva

```text
beta_0 = 1.5288332,
1 + 2 beta_0^2 = 5.6746619,
m_eff,0^2/H0^2 = 21.5384259.
```

Na škálach `k/a >> m_eff` je CDM–CDM gravitácia násobená približne
`1+2 beta^2`. To nie je voľba navyše: rovnaká funkcia `A(phi)`, ktorá vytvára
backgroundový tok, vytvára aj trenie meniacej sa hmotnosti a príťažlivú piatu
silu. Staršiu predstavu „pridať iba kladné trenie gamma≈0.03 a nechať zdroj
gravitácie nezmenený“ táto akcia nerealizuje.

## 7. Prvý subhorizontový rastový test

Skript 33 integroval diagnostické rovnice

```text
delta_c,xx + [2+E_x/E+beta varphi_x] delta_c,x
 - 3/2 [Omega_c(1+2 beta^2 F)delta_c + Omega_b delta_b] = 0,

delta_b,xx + [2+E_x/E] delta_b,x
 - 3/2 [Omega_c delta_c + Omega_b delta_b] = 0,

F = q^2/(q^2+a^2 m_eff^2/H0^2),  q=k/H0.
```

| `q` | približné `k` [`h/Mpc`] | `delta_c(K5)/delta_c(GR-like)` | vážené `delta_m(K5)/delta_m(GR-like)` |
|---:|---:|---:|---:|
| 30 | 0.010 | 1.060568 | 1.051965 |
| 100 | 0.033 | 1.061721 | 1.052954 |
| 300 | 0.100 | 1.061824 | 1.053042 |

Samotný trecí člen dáva pomer `0.988980`, teda tlmí rast asi o `1.10 %`.
Po zahrnutí povinnej piatej sily je čistý efekt opačný: CDM rastie asi o
`6.1 %` a celková hmota o `5.2–5.3 %`. Kroková konvergencia je približne
`1.5e-8`.

## 8. Diagnostika `S8`, nie nová predikcia

Ak sa iba diagnosticky vynásobí interná hodnota `S8=0.8745` váženým rastovým
pomerom, vyjde `0.91994–0.92089`. To je nesprávny smer voči cieľu `0.82` a
voči KiDS-Legacy `0.815 (+0.016/-0.021)`.

Táto operácia nie je platná plná predikcia: `0.8745` nepochádza z
CMB-normalizovaného CLASS/CAMB riešenia pre túto akciu. Ani pomery 6.56–6.62
voči hornej šírke `+0.016` sa preto nesmú citovať ako likelihoodová
signifikancia. Skript 36 opravuje iba názvoslovie asymetrických chýb skriptu
34; fyzikálne čísla nemení.

## 9. Čo starší audit obmedzil

1. A1-K1 zostáva presným backgroundovým účtovníctvom, nie potvrdenou
   perturbačnou teóriou.
2. K5/K1 neoživuje mŕtvu A2-K1 M-009. Má inú, akciou odvodenú Eulerovu a
   Kleinovu–Gordonovu dynamiku a povinnú piatu silu.
3. Staré `c_s,f^2=1` bolo efektívnym postulátom. Tu je dôsledkom kanonickej
   akcie, ale za cenu konkrétnej väzby `A(phi)`.
4. Hodnota `S8=0.8745` sa pod K5/K1 nesmie označiť ako výsledná predikcia.
5. „Popol bez interakcie po zrode“ neplatí: jeho hmotnosť závisí od `phi`.
6. Ak sa táto akcia prijme iba ako efektívne mikrofyzikálne dokončenie už
   existujúcich rolí, môže zostať kandidátnou prílohou v3.18. Ak sa vyhlási za
   nový fundament bunkovej siete bez odvodenia zo siete, vyžaduje verziu 4.

## 10. Rozsudok a ďalšia brána

`PREŽÍVA IBA K5.0 — 45/100.` Neodporuje lokálnej kovariantnosti, zachovaniu
energie a hybnosti ani základným ghost/gradientovým podmienkam v testovanom
rozsahu. Zároveň zatiaľ neplní cieľ znížiť zhlukovanie a má silný mechanický
dôvod zhlukovanie zvyšovať.

Nasleduje A2-K5.1:

1. odvodiť úplný relativistický skalár+CDM systém z akcie;
2. urobiť presný gauge a `lambda->0` cross-check;
3. odvodiť regulárne radiačné počiatočné módy;
4. zopakovať superhorizontový test a Einsteinove constrainty;
5. až potom implementovať CLASS/CAMB a rozhodnúť `PREŽÍVA` alebo `MŔTVA M-012`.

## 11. Primárne zdroje

- [Amendola — Coupled Quintessence](https://arxiv.org/abs/astro-ph/9908023).
- [Barros et al. — Coupled quintessence with a LambdaCDM background](https://arxiv.org/abs/1802.09216); ich znamienko `beta` je oproti tomuto auditu opačné.
- [KiDS-Legacy cosmic shear constraints](https://arxiv.org/abs/2503.19441).

Zdrojové rovnice určujú typ akcie a kontroly. Verdikt a čísla v tomto audite
pochádzajú z projektových skriptov 32–36 na backgrounde A1-K1.
