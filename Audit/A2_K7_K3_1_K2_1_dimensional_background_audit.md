# A2-K7.1a-K3.1-K2.1 — audit rozmerovej Onsagerovej a backgroundovej uzávierky

**Dátum:** 2026-07-13  
**Skript:** `scripts/59_script_A2_K7_K3_1_K2_dimensional_background_closure.py`  
**Verdikt podkoľaje:** `PREŽÍVA IBA ROZMEROVÚ BACKGROUNDOVÚ EXISTENCIU`  
**Max. hĺbka:** `39/100`  
**Akceptované skóre nadradenej K7:** `30/100`

## 1. Auditované tvrdenie

K3.1-K2 dopĺňa expanzno-reakčný cross člen o recipročný bulk stress a
diagonálne disipácie. Pri bezrozmernej chemickej afinite `A` a lokálnej
expanzii `Theta` sa použila matica

```text
 Q   = ell A + alpha Theta,
-Pi  = alpha A + zeta Theta,
alpha = epsilon (1-delta) rho_F.
```

`Q` je hustota prenášanej energie za čas a `Pi` je bulk-viskózny príspevok
k tlaku. Voľba toku `-Pi` dáva entropickú bilineárnu formu
`A Q + Theta(-Pi)`. Rozmery sú

```text
[ell] = rho/time,  [alpha] = rho,  [zeta] = rho*time.
```

Tým sa odstránila rozmerová nejednoznačnosť normalizovanej matice zo
skriptu 58. Pozitivita vyžaduje

```text
ell > 0, zeta > 0, ell*zeta-alpha^2 > 0.
```

## 2. Väzba na presný K7 background

Expanzne nezávislá časť registrovaného zdroja určuje

```text
ell A_0 = (1-epsilon) Gamma rho_F,
Gamma = lambda H_0.
```

Po zavedení

```text
ell_hat  = ell/(H rho_F),
zeta_hat = zeta H/rho_F,
c        = epsilon(1-delta)
```

platí

```text
A_0 = (1-epsilon) lambda/(ell_hat E),
ell_hat*zeta_hat > c^2,
-Pi/rho_F = c A_0 + 3 zeta_hat.
```

Celkový už overený tlak paliva sa nemení. Rovnovážna časť skalárneho tlaku
sa kompenzuje podľa

```text
p_phi,eq + Pi = p_F,
p_phi,eq = p_F-Pi.
```

Preto je entalpia skalárneho paliva

```text
(rho_phi+p_phi,eq)/rho_F = delta-epsilon-Pi/rho_F.
```

Táto kompenzácia je účtovná backgroundová identita. Zatiaľ nebola odvodená
z lokálnej akcie ani z collision integrálu.

## 3. Predregistrovaný diagnostický test

Použitý bol pôvodný K7 grid
`epsilon/delta={0.01,0.05,0.10,0.25,0.50,0.90}` a diagnostický, nie
fitovaný grid `ell_hat={0.1,1,10,100}`. Determinant dostal fixnú 1 % rezervu:

```text
zeta_hat = 1.01 c^2/ell_hat.
```

Bod prešiel iba ak súčasne platilo:

1. kladný Onsagerov determinant;
2. kladná skalárna entalpia na celom backgrounde;
3. konečná afinita a tlak;
4. `max|A_0|<1`, aby sa lineárna near-equilibrium formulácia nepoužívala
   mimo vlastného predpokladu;
5. `max(-Pi/rho_F)<0.1` ako konzervatívna diagnostická brzda.

Posledné dve hranice nie sú nové fyzikálne zákony ani observačné fitové
limity. Sú explicitné interné podmienky platnosti tohto testu.

## 4. Výsledok

| `ell_hat` | Počet PASS z 6 | `max|A_0|` dnes | Stav | Max. hĺbka |
|---:|---:|---:|---|---:|
| 0.1 | 0 | 1.469 až 1.500 | mimo lineárnej near-equilibrium oblasti | `39/100` |
| 1 | 6 | 0.1469 až 0.1500 | PASS existenčného testu | `39/100` |
| 10 | 6 | 0.01469 až 0.01500 | PASS existenčného testu | `39/100` |
| 100 | 6 | 0.001469 až 0.001500 | PASS existenčného testu | `39/100` |

Spolu prešlo 18 z 24 bodov. Vo všetkých 24 bodoch bol determinant kladný,
bulk korekcia menšia než 10 % a entalpia kladná. Šesť bodov s
`ell_hat=0.1` zlyhalo výhradne na `|A_0|<1`.

V preživších bodoch je najmenšia nájdená skalárna entalpia
`0.00230936 rho_F`, teda zostala kladná aj pri
`epsilon/delta=0.9`. Backgroundový budget preto sám osebe K3.1-K2
nevylučuje.

## 5. Čo tento výsledok nedokazuje

- `ell_hat` nebolo odvodené; grid iba dokazuje neprázdnu matematickú oblasť;
- predpoklad konštantného `ell_hat` znamená
  `ell=ell_hat H rho_F`; bez mikrofyziky nie sú určené `delta ell` ani
  `delta zeta`;
- teplota, stav a stress-energy kúpeľa nie sú určené;
- fyzikálna noise covariance nie je určená. Známa je iba formálna škála
  `N_QQ proportional to 2 T ell` v lokálnom klasickom KMS limite;
- nebol dokázaný Markovovský limit, detailná rovnováha ani spektrálna
  pozitivita;
- neboli vykonané lineárne, superhorizontové, high-k, CMB ani `S_8` testy.

Väčšie `ell_hat` zmenšuje potrebnú afinitu a minimálny bulk tlak, ale pri
pevnej teplote zväčšuje lokálnu reakčnú noise silu. Bez odvodeného kúpeľa
sa preto `ell_hat=100` nesmie označiť za fyzikálne lepšie než `ell_hat=1`.

## 6. Rozsudok a zákaz prepisu

K3.1-K2.1 **prežila iba rozmerovú backgroundovú existenčnú bránu**.
Kód smrti `M-014c` sa neaktivoval, pretože sa našli body s kladným
determinantom, kladnou entalpiou a malou afinitou. Podkoľaj však neprešla
mikrofyzickou bránou `40/100`; nadradená K7 zostáva na `30/100`.

Neskorší dokument nesmie tento výsledok skrátiť na „Onsagerov mechanizmus je
odvodený“. Presná dovolená formulácia je: „existuje rozmerovo konzistentná
pozitívna transportná matica kompatibilná s K7 backgroundom pre časť
diagnostického gridu“.

## 7. Nasledujúca vetva

Ďalším krokom je K3.1-K2.2, rozdelená na fyzikálne odlišné stavy kúpeľa:
lokálny termálny/KMS bath, vákuový kvantový farebný kernel a netermálny
farebný bath s pamäťou. Prvá sa testuje lokálna termálna realizácia, lebo
ako jediná priamo zodpovedá lokálnej white-noise aproximácii použitej v
K3.1-K2.

## 8. Primárne fyzikálne zdroje

- Crossley, Glorioso, Liu, *Effective field theory of dissipative fluids*,
  <https://arxiv.org/abs/1511.03646>.
- Glorioso, Crossley, Liu, *Effective field theory of dissipative fluids II*,
  <https://arxiv.org/abs/1701.07817>.
- Gavassino, Antonelli, Haskell, *Bulk viscosity in relativistic fluids:
  from thermodynamics to hydrodynamics*, <https://arxiv.org/abs/2003.04609>.
- Gautier, Serreau, *Langevin description of nonequilibrium quantum fields*,
  <https://arxiv.org/abs/1209.1827>.

