# A2-K4.2 — high-k a subhorizontový audit a rozsudok

**Dátum auditu:** 2026-07-14  
**Koľaj:** A1-K1 / A2-K4  
**Rozsudok brány:** **`PREŠLA K4.2 V DEKLAROVANOM PERFECT-RADIATION ROZSAHU`**  
**Stav koľaje:** **`PREŽÍVA K4.2 — 59/100`**  
**Nový dôvod smrti:** nevydaný  
**Bezprostredný krok:** **K4.3 — úplná Einstein–Boltzmannova realizácia a
CMB-normalizovaná rastová brána**

## 1. Čo tento rozsudok znamená

K4 po prvýkrát prešla súčasne:

1. úplným trojrozmerným regulárnym superhorizontovým priestorom K4.1;
2. analytickým vysokofrekvenčným hlavným symbolom;
3. testom efektívnych kinetických a gradientových znamienok;
4. presným algebraickým a numerickým nulovým limitom;
5. subhorizontovou integráciou všetkých troch regulárnych módov na
   `q=30,300,1000`;
6. bodovým Einsteinovým `00` constraintom;
7. konvergenciou riešiča, kroku pozadia a počiatočného času.

Nenašiel sa nový K4-špecifický gradientový, ghostový ani exponenciálny
high-`k` mód. K4 preto nezomiera v K4.2.

Rozsudok **neznamená**, že je odvodená mikroskopická akcia, vypočítané CMB,
overené `S8` alebo hotová A2. Model v tejto bráne nahrádza fotóny a neutrína
jednou perfektnou radiačnou tekutinou. Presný Einstein–Boltzmannov opis
vyžaduje samostatnú fotónovú a neutrínovú hierarchiu, vyššie multipóly a
anizotropný stres; štandardnú referenciu poskytujú Ma a Bertschinger
([arXiv:astro-ph/9506072](https://arxiv.org/abs/astro-ph/9506072)).

## 2. Predregistrované brány a výsledky

| Brána | Požiadavka | Výsledok | Stav |
|---|---|---|---|
| T0 | rovnaké rovnice a tri regulárne módy ako K4.1; bez ladenia | skript 70 importuje skript 66 | PASS |
| T1 | rýchlosti `0x4`, `±1`, `±1/sqrt(3)` | presne získané z charakteristického polynómu | PASS |
| T2 | kladný propagujúci gradient a efektívna kinetická váha | `c_s,f^2=1`, `delta rho_f>0` | PASS s UV obmedzením |
| T3 | interakcia iba v `O(k^0)` a správny `lambda=0` limit | analyticky aj numericky splnené | PASS |
| T4 | všetky tri regulárne módy; štart constraint `<1e-10` | maximum `2.32e-16` | PASS |
| T5 | aktívne bodové rel. `00` rezíduum `<1e-6` | maximum `4.41e-8` v hlavnej mriežke | PASS |
| T6a | q=300 riešičová zmena matice `<1e-5` | `2.11e-8` | PASS |
| T6b | q=300 zmena kroku pozadia `<1e-4` | `7.02e-8` | PASS |
| T6c | q=300 štart `-20 -> -22`, zmena `<1e-4` | `1.99e-6` | PASS |
| T7 | konečnosť, `1e-5 T_max<1`, bez K4 high-k explózie | max. `0.240`; K4 pod nulovým limitom | PASS |

Kill kritérium nebolo splnené. Nijaký TIMEOUT nenastal.

## 3. Analytická brána vysokého k

Po eliminácii constraintovo potlačeného `Phi=O(k^-2)` má hlavný symbol
charakteristický polynóm

```text
mu^4 (mu^2+1) (mu^2+1/3).
```

Palivo sa šíri rýchlosťou 1, perfektná radiácia rýchlosťou `1/sqrt(3)` a
CDM/baryóny majú nulové zvukové rýchlosti. Interakčné členy úmerné
`Gamma=lambda H0` sú rádu `k^0`, preto nemenia charakteristiky pri
`k -> infinity`.

### 3.1 Dôležitá výhrada k prachu

Nulová vlastná hodnota má algebraickú násobnosť 4, ale geometrickú iba 2.
CDM a baryónový blok sú štandardné Jordanove bloky beztlakového prachu.
Formálne teda nemožno tvrdiť, že **celý** prvostupňový fluidný symbol je
silne hyperbolický.

Táto vlastnosť:

- je rovnaká pri `lambda=0`;
- nie je vytvorená transferom K4;
- patrí aj štandardnej lineárnej tlakovej aproximácii prachu;
- vyžaduje opatrnosť mimo lineárneho režimu, kde vznikajú caustiky.

Preto nie je férovým dôvodom zabiť K4 oproti jej nulovej referencii, ale je
zachovaná ako obmedzenie rozsahu rozsudku.

### 3.2 Kinetická brána nie je fundamentálna no-ghost veta

V efektívnom fluidnom uzávere je palivová kinetická váha úmerná
`(rho_f+p_f)/c_s^2=delta rho_f>0` a gradientová rýchlosť je
`c_s,f^2=1>0`. Propagujúci palivový blok je diagonalizovateľný a kauzálny.

Bez lokálnej mikroskopickej akcie však nemožno z fluidnej matice dokázať
pozitivitu Hamiltoniánu všetkých UV stupňov voľnosti. K4.2 preto používa
presné pomenovanie **efektívna fluidná stabilita**, nie „dokázaná
fundamentálna bezghostovosť“.

## 4. Numerická brána

Úplná regulárna báza bola normalizovaná počiatočnou observabilnou Gramovou
maticou. V žiadnom bode sa nevyberal jediný výhodný lineárny vektor.

| `q` | `T_max`, K4 | `1e-5 T_max` | `T_max`, `lambda=0` | K4/nulový limit |
|---:|---:|---:|---:|---:|
| 30 | 428.7089 | 0.004287 | 431.2402 | 0.9941 |
| 300 | 9 922.0287 | 0.099220 | 10 631.9909 | 0.9332 |
| 1000 | 24 001.6954 | 0.240017 | 26 457.8315 | 0.9072 |

Absolútne transfery rastú s `q`, ale na testovanej mriežke:

- zostávajú v predregistrovanom lineárnom rozsahu pre seed `1e-5`;
- nemajú interakčne vyvolanú exponenciálnu obálku;
- po vypnutí interakcie sú ešte väčšie.

To ukazuje, že pozorovaný rast je dominantne štandardný gravitačný rast
bez-tlakových hustôt. Nie je to dôkaz správnej amplitúdy `S8`, pretože
počiatočná auditná norma nie je náhradou za CMB-normalizované primordiálne
spektrum.

## 5. Constraint a numerická spoľahlivosť

Globálny podiel dvoch nezávislých maxím sa nepoužil ako rozhodujúca brána.
Pre každý čas, každý mód a rovnaký bod sa spočítalo

```text
R_rel = abs(t1+t2+t3)/(abs(t1)+abs(t2)+abs(t3)).
```

Body, na ktorých bola norma členov pod `1e-12` globálneho maxima, sa
nepoužili na relatívny test šum/šum. Najhorší aktívny bodový výsledok hlavnej
mriežky bol `4.41484e-8`, pod bránou `1e-6`. Sprísnenie tolerancií zmenilo
finálnu maticu iba o `2.10624e-8`.

Rovnice viaczložkových interagujúcich porúch a potreba gauge-invariantnej
kontroly majú štandardný základ v Malikovi a Wandsovi
([arXiv:0809.4944](https://arxiv.org/abs/0809.4944)). K4.2 však testuje
konkrétnu lokálnu implementáciu a nepreberá fyzikálny rozsudok z referencie.

## 6. Ako K4.1 a K4.2 obmedzili starší M-011

Historický audit M-011 tvrdil smrť K4 z veľkého zisku jedného relatívneho
rýchlostného seedu. Neskorší audit ho **nevymazal**, ale obmedzil jeho dosah:

1. K4.1 odvodila presne tri regulárne primordiálne módy;
2. starý fuel-only velocity seed má projekčné rezíduum `0.9789492202` a
   neleží v tomto regulárnom priestore;
3. starý „gain“ bol primárne pomerom voči malej referenčnej hodnote, nie
   absolútnym normovým dôkazom divergencie;
4. K4.2 preverila celý regulárny priestor na subhorizontových škálach a
   nenašla interakčný high-`k` rast; K4 transfer bol menší než `lambda=0`.

Preto sa M-011 zachováva ako historický dôkaz smrti **konkrétneho starého
seedu a interpretácie**, nie ako platný všeobecný rozsudok nad K4. Nová smrť
K4 by musela dostať nový identifikátor a nový zachovaný dôkaz.

## 7. Maximálna hĺbka a stav

**Maximálna dosiahnutá hĺbka A2-K4 je `59/100`.**

Hĺbka znamená dokončenú auditnú bránu, nie pravdepodobnosť pravdivosti ani
percento zhody s dátami. K4 zostáva otvorená a živá. A1-K1 preto naďalej
zostáva otvorená a podmienená.

## 8. Povinný ďalší krok — K4.3

K4.3 musí byť pred výpočtom `S8` predregistrovaná a musí obsahovať:

1. samostatné fotónové a neutrínové Boltzmannove hierarchie;
2. neutrínový anizotropný stres a všeobecne `Phi != Psi`;
3. baryón-fotónovú tesnú väzbu, prechod cez rekombináciu a štandardný
   baryónový zvukový sektor;
4. rovnaký lokálny K4 transfer a nulový limit bez dodatočného drag parametra;
5. krížovú kontrolu aspoň dvoch gauge alebo nezávislej implementácie;
6. CMB-normalizované transferové funkcie `delta_m(k,z)`;
7. až potom výpočet `sigma8`, `S8`, CMB/BAO/lensing likelihoodu v A3.

Ak K4.3 zlyhá na novom fyzikálnom dôvode, K4 sa označí za mŕtvu s novým
dôvodom a všetky skripty sa zachovajú. TIMEOUT alebo chýbajúca implementácia
nie sú fyzikálnou smrťou.

## 9. Dôkazový balík

- `Questions/A2_K4_2_PROBLEM_BRANY_A_KILL_KRITERIA.md`;
- `scripts/69_script_A2_K4_2_high_k_principal_symbol.py`;
- `scripts/70_script_A2_K4_2_subhorizon_regular_basis.py`;
- `scripts/71_script_A2_K4_2_q300_convergence_gates.py`;
- `scripts/OUTPUT_A2_K4_2_69_71.md`;
- `Audit/A2_K4_1_UPLNA_REGULARNA_CONSTRAINT_BAZA_A_ROZSUDOK.md`;
- `Audit/ERRATUM_M011_K4_REFERENCE_GAIN_VS_ABSOLUTE_TRANSFER.md`;
- `Audit/A2_K4_2_MANIFEST_SHA256.md`.

