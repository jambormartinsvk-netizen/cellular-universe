# A2/Q20 — výber koľaje bez povinnej piatej sily K5/K1

**Dátum:** 2026-07-13  
**Otázka:** Máme koľaj bez pretrvávajúceho rizika `S8 -> približne 0.92`
spôsobeného povinnou konformnou piatou silou?  
**Krátka odpoveď:** áno, ale zatiaľ žiadna neprešla vlastným auditom

## 1. Najlepší kandidát — A2-K5/K3a

`A2-K5/K3a` používa všeobecnú derivatívnu akciu

```text
f(n_c, phi, X, Z),
Z=u_c^mu partial_mu phi.
```

Prenos hybnosti vzniká zo `Z`-závislosti a nie iba z gradientu meniacej sa
hmotnosti CDM. Preto neplatí povinná väzba K5/K1

```text
backgroundový tok -> beta -> G_eff/G=1+2 beta^2 F >1.
```

V známych zdravých podtriedach môže momentum transfer viesť k
`G_eff,c<G` v neskorom vesmíre. To je presne vlastnosť, ktorú potrebujeme na
zníženie rastu namiesto jeho zvýšenia.

**Aktuálny stav:** `HYPOTÉZA — ČAKÁ, ZRELOSŤ 25/100`.

Hodnotenie neznamená pravdepodobnosť pravdivosti. Znamená iba, že existuje
publikovaná akčná trieda a žiadaný mechanizmus, ale ešte neexistuje konkrétna
funkcia `f` odvodená z bunkovej teórie ani jej backgroundový a stabilitný test.

## 2. Ďalšie koľaje bez povinnej konformnej sily

| Koľaj | Prečo nemá povinnú silu K5/K1 | Nové riziko | Stav |
|---|---|---|---|
| **K5/K2a** | popol vzniká produkciou počtu častíc s konštantnou hmotnosťou; po vzniku nemá skalárny náboj | creation pressure, šum, spätná reakcia a správny profil `Q` | `ČAKÁ 18/100` |
| **K5/K4a** | energiu a hybnosť nesie konečno-entalpický mediátor; popol môže byť skalárne neutrálny | mediátor môže vytvoriť vlastnú silu alebo meniť background | `ČAKÁ 15/100` |
| **K5/K6** | elastický momentum transfer môže pôsobiť ako fyzikálne trenie bez backgroundovej piatej sily | neprípustné, ak produkcia a trenie vyžadujú dva nezávislé post-data parametre | `ČAKÁ 12/100` |
| **A1-K2/A2-K6a** | prahový tok sa vypne pred neskorým rastom; dnešná veľká väzba nevznikne | mení A1-K1 background a pravdepodobne fundament | `ČAKÁ 10/100; v4 kandidát` |

## 3. Dôležité rozlíšenie

Tieto koľaje zatiaľ **nemajú potvrdený problém** `S8->0.92`, pretože neobsahujú
konkrétny konformný mechanizmus K5/K1. To však ešte neznamená, že predpovedajú
správne `S8`.

- K5/K3a ako jediná už má v primárnej literatúre explicitný precedens
  `G_eff<G`.
- K5/K2a a K5/K4a iba konštrukčne odstraňujú povinný skalárny náboj; ich rast
  zatiaľ nebol vypočítaný.
- K5/K6 má literárny precedens slabšieho zhlukovania cez elastický momentum
  transfer, ale musí byť mikrofyzicky zviazaná s produkciou popola.
- A1-K2/A2-K6a nie je čistá náhrada A2: musí znovu prejsť backgroundom.

## 4. Rozhodnutie o poradí

1. dokončiť A3 pre K5/K1, aby sa korektne rozhodlo M-012;
2. ako prvú alternatívu začať K5/K3a;
3. prvá brána K5/K3a musí ešte pred integráciou dokázať:
   - kladnú kinetickú maticu;
   - nulový tlak CDM;
   - žiadny pól `1/(1+w_f)`;
   - reprodukciu A1-K1 alebo presne priznanú odchýlku;
   - `G_eff,c<=G` bez rušenia dvoch nezávisle fitovaných veľkých členov.

Ak posledná podmienka neprejde, K5/K3a zomrie ešte pred CLASS/CAMB a pokračuje
sa K5/K2a alebo K5/K4a.

## 5. Primárne opory

- [Kase a Tsujikawa — všeobecné `f(n_c,phi,X,Z)` interakcie a prípady `G_eff,c<G`](https://arxiv.org/abs/2005.13809).
- [Amendola a Tsujikawa — energy+momentum coupling so slabšou gravitáciou](https://arxiv.org/abs/2003.02686).
- [Pourtsidou, Skordis a Copeland — akčné triedy skalár–CDM couplingov](https://arxiv.org/abs/1307.0458).
- [Beltrán Jiménez et al. — elastický momentum transfer a slabšie zhlukovanie](https://arxiv.org/abs/2106.11222).
