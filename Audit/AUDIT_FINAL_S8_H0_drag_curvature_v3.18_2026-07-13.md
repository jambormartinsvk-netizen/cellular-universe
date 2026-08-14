# Konečný audit hypotéz S8–H0: trenie, krivosť a kombinácia

**Dátum:** 2026-07-13  
**Status dokumentu:** AUTORITATÍVNY PRE DODANÉ TABUĽKY  
**Nahrádza:** predbežný fixno-hustotný screening K1/K4 v `Questions/S8_H0_styri_nove_kolaje_prvotny_audit_2026-07-13.md` a interpretácie zo skriptu 16  
**Cieľ auditu:** rozhodnúť dodané hypotézy bez toho, aby sa k rovnakým tabuľkám musel opakovať audit.

## 1. Konečný verdikt

| ID | Hypotéza | Verdikt |
|---|---|---|
| H1 | Dodaný grid trenia je numericky výsledkom deklarovanej rozšírenej pipeline 09 | **PREŽÍVA — 100/100 na úrovni reprodukcie** |
| H2 | Grid trenia je „exaktná fyzikálna kalibrácia“ modelu | **MŔTVA** — chýbajú konzistentné perturbácie interakcie a plná likelihood |
| H3 | `γdrag = 0,03` znamená približne 3 % brzdenia popola za e-fold | **MŔTVA** — ide o koeficient pri derivácii rastu jednej celkovej hmotnej tekutiny, nie priamo percentuálnu stratu rýchlosti popola |
| K1a | Konštantné trenie aplikované na jedinú premennú celkovej hmoty od `z=1000` | **MŔTVA AKO FYZIKÁLNA IMPLEMENTÁCIA** |
| K1b | Covariantný prenos hybnosti iba medzi popolom a dynamickou sieťovou/tmavou zložkou | **PREŽÍVA — 35/100** |
| H4 | Pokles `χ²_3front` z 29,99 na 8,99 dokazuje zlepšenie o 21 bodov voči ΛCDM | **MŔTVA** — `χ²_3front` nie je likelihood a ignoruje kľúčové kovariancie a veličiny |
| H5 | Dodaný grid krivosti je numericky výsledkom FLRW krivosti a samosúladnej CMB kotvy | **PREŽÍVA — 100/100 na úrovni reprodukcie** |
| K4a | Fenomenologická otvorená FLRW krivosť môže posunúť H0 nahor a S8 nadol | **PREŽÍVA — 63/100** |
| K4b | Náhodná topológia bunkovej siete vnútorne odvodzuje `ΩK ≈ +0,005` | **PREŽÍVA — 20/100** — nie je v rozpore so zákonom, ale zatiaľ nemá odvodenie ani meranie zo siete |
| H6 | Bod `ΩK=0,005` už dokázal dvojité vyriešenie napätí | **MŔTVA AKO DÔKAZ** — je to reprodukovateľný toy bod, nie modelová likelihood |
| H7 | Príklad `ΩK=0,002`, `γ=0,015` trafí cieľ `H0≈68`, `S8≈0,82` | **MŔTVA** — dáva `H0=67,2672`, `S8=0,82515` |
| K5 | Kombinácia covariantného trenia a odvodenej krivosti | **PREŽÍVA — 35/100** |
| H8 | Dva voľné parametre sa dajú v toy pipeline nastaviť presne na `H0=68`, `S8=0,82` | **PREŽÍVA ARITMETICKY**, ale má nulovú prediktívnu váhu, lebo dva parametre boli kalibrované na dva ciele |

Verdikty „MŔTVA“ sa vzťahujú na presne uvedené tvrdenie alebo implementáciu. Nezabíjajú automaticky fyzikálne širšiu K1b, K4a/K4b alebo K5.

## 2. Nezávislá reprodukcia gridov

Použitý skript: `scripts/17_script_S8_H0_drag_curvature_grid_audit.py`.

Skript samostatne implementuje:

- rovnice pozadia pipeline 09 s `λ=0,15`, `δ=0,02297`, `ΔNeff=0,0535`;
- kladný trecí člen pri `D'`;
- krivostný člen `ΩK a^-2` v `E²`;
- otvorenú/uzavretú FLRW priečnu vzdialenosť `S_K(χ)`;
- opätovné ukotvenie na CMB uhlovú škálu pri každom `ΩK`;
- presnú lokálnu definíciu `χ²_3front` zo skriptu 09.

### 2.1 Referenčný bod

| Veličina | Nezávislý výpočet | Dodaná hodnota |
|---|---:|---:|
| H0 | 66,36575 | 66,373 |
| Ωm | 0,3517487 | približne 0,3517 |
| w0 | −0,9191668 | −0,919 |
| wa | −0,6119564 | −0,612 |
| S8 | 0,8746489 | 0,8745 |
| `χ²_3front` | 18,7896 | 18,75 |

Rozdiely zodpovedajú zaokrúhleniu a redšej auditnej integračnej mriežke.

### 2.2 Grid trenia

| γdrag | H0 | S8 — audit | S8 — dodané | `χ²_3front` — audit |
|---:|---:|---:|---:|---:|
| 0,00 | 66,3658 | 0,87465 | 0,8745 | 18,7896 |
| 0,01 | 66,3658 | 0,85272 | 0,8526 | 12,8741 |
| 0,02 | 66,3658 | 0,83143 | 0,8313 | 9,6818 |
| 0,03 | 66,3658 | 0,81078 | 0,8107 | 8,9830 |
| 0,04 | 66,3658 | 0,79073 | 0,7906 | 10,5650 |
| 0,05 | 66,3658 | 0,77127 | 0,7712 | 14,2300 |
| 0,06 | 66,3658 | 0,75238 | 0,7523 | 19,7946 |

Maximálny rozdiel S8 je menší než `1,5×10^-4`. Grid je aritmeticky reprodukovaný.

### 2.3 Grid krivosti

| ΩK | H0 — audit | H0 — dodané | S8 — audit | S8 — dodané |
|---:|---:|---:|---:|---:|
| −0,005 | 64,28698 | 64,293 | 0,91744 | 0,9173 |
| −0,003 | 65,09055 | 65,097 | 0,90049 | 0,9004 |
| −0,001 | 65,93085 | 65,938 | 0,88332 | 0,8832 |
| 0 | 66,36575 | 66,373 | 0,87465 | 0,8745 |
| +0,001 | 66,81106 | 66,818 | 0,86592 | 0,8658 |
| +0,002 | 67,26723 | 67,275 | 0,85712 | 0,8570 |
| +0,003 | 67,73476 | 67,742 | 0,84826 | 0,8481 |
| +0,005 | 68,70603 | 68,714 | 0,83034 | 0,8302 |

Maximálny rozdiel H0 je menší než `0,008 km s^-1 Mpc^-1`; maximálny rozdiel S8 je menší než `1,7×10^-4`. Grid je aritmeticky reprodukovaný.

Tým sa opravuje skorší fixno-hustotný screening v skripte 16. Ten nezahŕňal opätovné riešenie dnešnej `Ωm` a CMB kotvy. Pre rozhodovanie K4 sa odteraz používa iba skript 17.

## 3. Prečo je tvrdenie o χ² mŕtve

Lokálne skóre je

$$
\chi^2_{3\rm front}=
\left(\frac{w_0+0,75}{0,06}\right)^2+
\left(\frac{w_a+0,86}{0,25}\right)^2+
\left(\frac{S_8-0,815}{0,019}\right)^2.
$$

### 3.1 Nie je to likelihood dát

Skóre nevyhodnocuje CMB spektrá, DESI BAO body, supernovy, RSD ani weak-lensing dátový vektor. Používa tri odvodené čísla ako nezávislé Gaussove kotvy.

Správny kvadratický tvar používa úplnú kovariančnú maticu,

$$
\Delta\mathbf p^T C^{-1}\Delta\mathbf p,
$$

rovnako ako samotná DESI analýza pri porovnaní dátových posteriorov. Parametre `w0` a `wa` sú silno korelované.

Skript 17 ukazuje citlivosť: ak by bola korelácia `ρ(w0,wa)=-0,9`, príspevok dvojice by bol

- bunkový bod: `20,52`;
- ΛCDM: `17,87`.

Pri nulovej korelácii lokálny skript dáva opačné poradie `8,93` a `29,19`. Hodnota korelácie `−0,9` tu nie je použitá ako nameraná hodnota; je to dôkaz, že bez skutočnej kovariancie sa môže znamienko údajného zlepšenia obrátiť.

### 3.2 H0 a Ωm v skóre chýbajú

Krivostný grid tvrdí dvojité zlepšenie H0 a S8, ale `χ²_3front` neobsahuje žiadny člen H0 ani Ωm. Pokles skóre pri zmene ΩK pochádza prevažne z posunu S8; H0 sa v ňom vôbec netestuje.

### 3.3 Chýba penalizácia nových parametrov

Trenie pridáva parameter `γdrag`, krivosť pridáva `ΩK` a kombinácia dva parametre. Optimum sa vyberalo po prezretí dát. Bez plnej likelihood, profilu/posterioru a penalizácie parametrov nemožno deklarovať `Δχ²` voči ΛCDM.

**Konečný verdikt H4:** čísla `8,99`, `9,50` a `29,99` môžu zostať iba pod názvom **interné pseudo-skóre troch kotiev**. Nesmú byť v novej verzii označené ako celkové χ² alebo dôkaz zlepšenia o 20–21 bodov.

## 4. Fyzikálny audit K1

### 4.1 Čo implementácia skutočne robí

Skript používa jednu premennú `D` pre všetku hmotu a rieši

$$
D''+\left(2+\frac{H'}H+\gamma_{\rm drag}\right)D'
-\frac32\frac{\Omega_m(x)}{E^2(x)}D=0.
$$

Kladné znamienko je správne pre tlmenie. `γdrag=0,03` je bezrozmerný koeficient pri `D'`, ktorý pôsobí počas približne siedmich e-foldov od `z=1000`. Nie je totožný s priamou 3 % stratou rýchlosti popola za každý e-fold.

### 4.2 Rozpor s deklarovanou interpretáciou

Rovnica nerozlišuje baryóny a popol. Trenie preto numericky pôsobí na celkovú hmotnú perturbáciu vrátane baryónov, hoci hypotéza tvrdí trenie iba tmavej hmoty.

Pozadie zároveň obsahuje výmenu energie palivo → hmota. Pri perturbáciách však chýbajú:

- perturbácia zdroja `δQ`;
- samostatné hustoty a rýchlosti baryónov, starého CDM a nového popola;
- protihybnosť zložky, ktorá popol brzdí;
- perturbácie paliva/pary/siete;
- zmeny gravitačných potenciálov, ISW, CMB lensingu a RSD.

Použiť štandardnú rastovú rovnicu pre oddelene zachovanú hmotu pri nezachovanej hmotnej zložke nie je fyzikálne uzavreté.

### 4.3 Prečo širšia K1b prežíva

Čistý prenos hybnosti v tmavom sektore sa dá zapísať covariantne tak, aby na homogénnom pozadí neprenášal energiu a menil iba perturbácie. Také modely sa analyzujú s plnými perturbáciami a dátami; pozri [interacting dark sectors with DESI DR2](https://arxiv.org/abs/2503.21652) a [momentum-coupled dark energy with DESI DR2](https://arxiv.org/abs/2506.21295).

To dokazuje existenciu fyzikálne dovolenej triedy, nie správnosť bunkového `γ=0,03`.

### 4.4 Hodnotenie K1b

| Oblasť | Body |
|---|---:|
| Reprodukcia | 20/20 |
| Konzervácia a zákony | 8/25 |
| Stabilita a kauzalita | 2/20 |
| Observačná likelihood | 5/25 |
| Vnútorné odvodenie | 0/10 |
| **Spolu** | **35/100 — PREŽÍVA PODMIENEČNE** |

### 4.5 Kill conditions K1b

K1b zomrie, ak:

1. nemožno nájsť lokálny covariantný `Q_i^μ` s `Σ_iQ_i^μ=0` a trením iba popola;
2. potrebný člen vedie ku ghostu, gradientovej nestabilite, zápornej kinetickej energii alebo nadsvetelnému signalizovaniu;
3. plná CMB+BAO+SN+RSD+lensing likelihood vylúči oblasť potrebnú na `S8≈0,82`;
4. mechanizmus nevyhnutne brzdí aj baryóny v rozpore s testami geodetického pohybu.

## 5. Fyzikálny audit K4

### 5.1 Súlad so všeobecnou relativitou

Člen

$$
E^2(a)\supset\Omega_{K0}a^{-2}
$$

a otvorená vzdialenosť `sinh(√ΩK χ)/√ΩK` sú štandardná FLRW geometria. Kladné `ΩK` označuje otvorený priestor. Táto časť gridu neporušuje potvrdený zákon.

### 5.2 Aktuálny observačný rozsah

Oficiálna DESI DR2 analýza pre `ΛCDM+ΩK` a kombináciu DESI+CMB uvádza približne

$$
\Omega_K=0,0023\pm0,0011,\quad
H_0=68,50\pm0,33,\quad
\Omega_m=0,3034\pm0,0037.
$$

Pozri tabuľku V v [DESI DR2 Results II](https://journals.aps.org/prd/pdf/10.1103/tr6y-kpc6). Samotná DESI Collaboration to neoznačuje za významný dôkaz neplochosti.

Hodnota `ΩK=0,005` je približne `2,45σ` nad týmto modelovo závislým priemerom. Nie je preto bezpečne prijatá, ale ani definitívne vylúčená na úrovni, ktorá by automaticky zabila inú dynamickú kozmológiu.

Alarmom je predikované `Ωm=0,33089`. Voči uvedenému `ΛCDM+ΩK` posterioru je rozdiel približne `7,4σ`. Toto číslo nemožno vyhlásiť za modelovú významnosť bunkovej kozmológie, pretože jej pozadie je iné; jasne však ukazuje, že pseudo-skóre vynechalo veľmi obmedzujúcu veličinu.

### 5.3 Chýbajúce odvodenie zo siete

Náhodný Delaunayov graf vložený do euklidovského priestoru nie je automaticky priestor s kladným `ΩK`. Treba:

1. definovať diskrétnu metriku a krivosť;
2. zmerať lokálne deficitné uhly alebo inú fyzikálne odôvodnenú krivosť;
3. vykonať coarse-graining a limit `N→∞`;
4. odvodiť znamienko aj amplitúdu bez použitia požadovaného H0.

### 5.4 Hodnotenie K4a/K4b

| Oblasť | K4a: fenomenologická krivosť | K4b: pôvod zo siete |
|---|---:|---:|
| Reprodukcia | 20/20 | 20/20 |
| Konzervácia a zákony | 20/25 | 0/25 |
| Stabilita a kauzalita | 15/20 | 0/20 |
| Observačná likelihood | 8/25 | 0/25 |
| Vnútorné odvodenie | 0/10 | 0/10 |
| **Spolu** | **63/100 — PREŽÍVA** | **20/100 — PREŽÍVA IBA AKO NEODVODENÁ HYPOTÉZA** |

### 5.5 Kill conditions K4

K4 zomrie, ak:

1. diskrétna krivosť konverguje k nule alebo opačnému znamienku;
2. modelovo správna likelihood vylúči potrebné `ΩK` mimo vopred určenej 99 % oblasti;
3. hodnota potrebná pre H0 zničí BAO, CMB lensing, supernovy alebo rast;
4. `ΩK` zostane iba novým voľným fitom bez nezávislej sieťovej predikcie — vtedy môže prežiť iba ako fenomenologické rozšírenie, nie výsledok teórie.

## 6. Kombinácia K5

### 6.1 Dodaný príklad

Skript `scripts/18_script_S8_H0_combined_drag_curvature_point.py` dal pre

$$
\Omega_K=0,002,\qquad\gamma_{\rm drag}=0,015
$$

výsledok:

- `H0 = 67,26723 km s^-1 Mpc^-1`;
- `S8 = 0,825146`;
- `Ωm = 0,343452`;
- interné `χ²_3front = 9,1867`.

Preto dodaná veta, že tento príklad rozloží korekcie do ideálneho stavu `68/0,82`, neprešla.

### 6.2 Post-data kalibrácia presného cieľa

Skript `scripts/19_script_S8_H0_toy_target_calibration.py` ukázal, že zjednodušená pipeline vie po dátach nastaviť

$$
\Omega_K=0,0035564,\qquad
\gamma_{\rm drag}=0,0110529
$$

na

$$
H_0=68,00001,\qquad S_8=0,820000.
$$

Súčasne dáva `Ωm=0,33695` a `χ²_3front=8,9453`.

Toto nie je predikcia: dva voľné parametre boli kalibrované na dve cieľové čísla. Výsledok iba dokazuje dosiahnuteľnosť bodu v toy pipeline.

### 6.3 Hodnotenie K5

| Oblasť | Body |
|---|---:|
| Reprodukcia | 20/20 |
| Konzervácia a zákony | 8/25 |
| Stabilita a kauzalita | 2/20 |
| Observačná likelihood | 5/25 |
| Vnútorné odvodenie | 0/10 |
| **Spolu** | **35/100 — PREŽÍVA PODMIENEČNE** |

K5 nesmie ísť do predikčnej tabuľky v3.18. Môže zostať iba ako exploratívna vetva, kým K1b a K4b nezískajú nezávislé mikrofyzikálne hodnoty.

## 7. Rozhodnutie pre v3.18

Do v3.18 možno zapísať:

- numerické gridy ako **sensitivity study simplified pipeline 09**;
- K1b a K4 ako otvorené koľaje s uvedeným skóre a kill conditions;
- reprodukčné skripty 17–19.

Do v3.18 sa nesmie zapísať:

- „trenie vyriešilo S8 na 100 %“;
- „krivka vyriešila obe napätia“;
- „celkové χ² sa zlepšilo o 20–21“;
- „γ=0,03 je odvodených 3 % za e-fold“;
- „ΩK=0,005 vyplýva z Delaunayovej topológie“;
- kalibrovaný bod K5 ako predikcia.

Tieto konkrétne tvrdenia sú týmto auditom uzavreté a nemajú sa znovu otvárať bez novej fyzikálnej rovnice alebo novej plnej likelihood.

## 8. Ďalšia živá práca

Najvyššiu fyzikálnu prioritu má teraz **K1b-T1**:

1. rozdeliť baryóny, starý CDM a vytváraný popol;
2. zapísať covariantné `Q_i^μ` vrátane energie a protihybnosti;
3. odvodiť lineárne perturbácie v určenej gauge;
4. vykonať analytický test stability;
5. až potom implementovať CLASS/CAMB a fitovať dáta.

K4b môže bežať paralelne iba ako nezávislý sieťový výpočet krivosti bez použitia cieľových H0/S8.

## 9. Použité primárne zdroje

- [DESI DR2 Results II](https://arxiv.org/abs/2503.14738) — plná kozmologická analýza, kovariancie a modelové porovnanie;
- [DESI DR2 publikovaná tabuľka parametrov](https://journals.aps.org/prd/pdf/10.1103/tr6y-kpc6);
- [KiDS-Legacy weak-lensing S8](https://arxiv.org/abs/2503.19441);
- [Interacting dark sectors in light of DESI DR2](https://arxiv.org/abs/2503.21652);
- [Momentum-coupled dark energy using DESI DR2](https://arxiv.org/abs/2506.21295);
- [SH0ES distance-ladder determination](https://arxiv.org/abs/2112.04510).

