# Externý audit QCT: identita teórie a možný prenos do Bunkového vesmíru

**Dátum:** 2026-07-15  
**Externý koncept:** *Quantum Cell Theory: Passengers in the Flow*, Andrew Gerard Lizzio  
**Zadaný record:** Zenodo 20059776, verzia 4.1  
**Kontrolovaná novšia revízia:** Zenodo 20199519, verzia v32  
**Rozsah:** identita teórie, kozmológia, tmavý sektor a použiteľnosť pre `A1-K1 / A2-K4 / K7`  
**Mimo rozsahu:** úplný audit tvrdení o hmotnostiach častíc, chémii a Yang-Millsovom mass gap

## Krátky verdikt

1. **Nie je to tá istá teória.** Správne označenie je
   `DIFFERENT_THEORY_WITH_SHARED_CELLULAR_ONTOLOGY`.
2. **Neposkytuje hotové riešenie nášho A2-K4/K7 problému.** Nemá odvodený a
   numericky integrovaný úplný lineárny Einstein-Boltzmannov systém, plnú
   fotónovú/neutrínovú hierarchiu, CMB likelihood ani predikciu `S8`.
3. **Nedáva fyzikálny dôkaz v prospech našej konkrétnej teórie.** Dáva iba
   nezávislý príklad podobnej všeobecnej intuície, že priestor môže byť bunkový.
4. **Môže pomôcť obmedzene:** ako zdroj troch auditovateľných alternatívnych
   hypotéz a ako negatívny metodický príklad pre naše G8/G9. Žiadnu z nich
   nemožno importovať do v3.18 bez samostatnej koľaje.

## 1. Prečo nejde o tú istú teóriu

| Rozhodujúca vlastnosť | Bunkový vesmír v3.17/v3.18 | QCT | Verdikt identity |
|---|---|---|---|
| Základná sieť | náhodná 3D Poisson-Voronoi/Delaunayova sieť | konečný jednoduchý graf a simpliciálny komplex | odlišné |
| Počet buniek | rastie delením, `N proportional a^3` | P1: `N` je konštantné | priamy rozpor |
| Veľkosť bunky | bunky nerastú; konštantnosť je súčasťou v3 fundamentu | P2: bunky sa izotropne zmenšujú/zväčšujú podľa vibračnej energie | priamy rozpor |
| Pôvod expanzie | delenie buniek poháňané trávením paliva | radiálny tok a zmena veľkosti buniek | iný mechanizmus |
| Jadro dynamiky | transport palivo -> hmota/popol, réžia `delta`, metabolizmus `lambda`, Bianchiho bilancia | `a = c^2 grad(ln s)` a pole veľkosti bunky `s` | iné rovnice a stavové premenné |
| Tmavá hmota | reálny gravitačný popol s konštantnou hmotnosťou | nelineárna kompresia buniek, Phase 2 a plánované vyššie Hopfove solitóny | iná ontológia aj mikrofyzika |
| Tmavá energia | účtovný tieň tvorby hmoty a riedenia paliva | pozícia v kozmologickom toku a zvyšok `Lambda(alpha)` | iný mechanizmus |
| Lineárne poruchy | explicitný A2 program s kontinuitami, Eulerom, Einsteinovými constraintmi a regulárnymi módmi | tvrdenie, že Phase 2 sa správa ako CDM, bez úplného uzavretého systému | nie je zameniteľné |
| Zmena fundamentu | deliaca sa sieť je nosná hypotéza | konštantný počet premenlivo veľkých buniek je nosná hypotéza | prípadný prechod by bol v4.0, nie oprava v3.18 |

Spoločná veta „priestor sa skladá z buniek“ preto označuje iba širokú rodinu
modelov. Identitu teórie určujú aktualizačné pravidlá. Tie sú navzájom
nekompatibilné.

Presné QCT postuláty sú v [QCT Postulates v8](https://zenodo.org/records/20199519/files/QCT-Supp-1-Postulates-v8.pdf):
konštantný počet buniek, izotropná zmena ich veľkosti a jeden časový kvant na
propagačný krok. Náš fundament je zapísaný v lokálnych súboroch
`theory/README.md`, `theory/SK/01_Introduction_and_Philosophy_SK.md` a
`theory/SK/04_Main_Document_Theory_Equations_Values_v3.17_SK.md`.

## 2. Sú všetky predpovede rovnaké?

Nie. Prekryv je čiastočný a pri rozhodujúcich kozmologických veličinách sa modely
rozchádzajú.

| Veličina alebo tvrdenie | Bunkový vesmír | QCT v auditovaných dokumentoch | Význam |
|---|---:|---:|---|
| `n_s` | približne `0.9656` | približne `0.9640` | podobné číslo, odlišné odvodenie |
| prvotné `r` | `< 10^-10` | `< 10^-10` | podobný smer, nie spoločný mechanizmus |
| `H0` | približne `66.4 km/s/Mpc` | približne `69.6 km/s/Mpc` | odlišná predikcia |
| `S8` | približne `0.86-0.87`, otvorené riziko | nenájdená predikcia ani likelihood | QCT nerieši náš hlavný cieľ |
| `Delta N_eff` | `0.0535`, teda `N_eff` približne `3.10` | QCT pri rovnosti používa Phase 2 `g*=2` a iba fotóny | fyzikálne odlišné a v QCT neuzavreté |
| `w0, wa` | približne `(-0.92, -0.61)` | bez ekvivalentnej validovanej CPL predikcie | nie je rovnaká tabuľka |
| tmavá hmota | popol, iba gravitačný | kompresia/Phase 2/Hopfove solitóny | odlišné |
| prvý CMB vrchol | musí vyjsť z `r_s/D_M` v kalibrovanej pipeline | v zadanom v4.1 balíku sa objavilo `220` aj `243`; v32 dodatok uvádza `220` | v4.1 vnútorná nekonzistentnosť |

Podobnosť `n_s` a horného limitu `r` je zaujímavá na evidenciu konvergentných
hypotéz, ale nie je potvrdením. Obe čísla sú blízko známeho observačného cieľa a
QCT ešte nepredložila kompletnú mapu z vlastných perturbácií na CMB likelihood.

## 3. Rieši QCT náš problém A2-K4/K7?

**Nie. Verdikt: `NO_DIRECT_A2_TRANSFER`.**

Na uzavretie nášho A2/K7 potrebujeme najmenej:

1. kovariantný stres-energetický tenzor a jednoznačné prenosy energie a hybnosti;
2. úplné linearizované kontinuity a Eulerove rovnice všetkých zložiek;
3. Einsteinove constrainty a dynamické rovnice v určenej gauge;
4. regulárne AD/CDI/BI/NID/NIV superhorizontové počiatočné módy;
5. plnú fotónovú a neutrínovú Boltzmannovu hierarchiu;
6. výpočet CMB, rastu a `S8` na jednej konzistentnej kalibrácii;
7. likelihood s počtom parametrov a datasetmi.

Ani v novšom [QCT Cosmology v7](https://zenodo.org/records/20199519/files/QCT-Supp-5-Cosmology-v7.pdf)
tieto kroky nie sú hotové. Dokument sám označuje CMB výkonové spektrum z Phase 2
a rast štruktúr za najdôležitejšie nevypočítané testy a na konci žiada budúci
beh CLASS alebo CAMB. CLASS je práve kód na riešenie lineárnej Einstein-Boltzmannovej
sústavy, nie iba kalkulačka z dvoch hustôt
([CLASS overview](https://arxiv.org/abs/1104.2932)).

Tvrdenie QCT, že podobné `Omega_b h^2` a `Omega_c h^2` automaticky dávajú
rovnaký pomer CMB vrcholov, nestačí. QCT súčasne mení radiačnú históriu,
mikrofyziku tmavej zložky, počiatočné podmienky a kauzálnu štruktúru Phase 2.
Rovnaké dve hustoty preto nie sú rovnakým vstupom do celej Boltzmannovej sústavy.

## 4. Fyzikálne varovania z relevantnej časti QCT

Tieto body nepredstavujú úplný audit QCT. Sú to dôvody, prečo jej kozmologické
výsledky nemožno preniesť do nášho modelu bez nového dôkazu.

### 4.1 Rast porúch je tvrdený, nie odvodený v úplnej sústave

QCT uvádza `delta_2 proportional ln(a)` počas radiačnej éry a
`delta_2 proportional a` po rovnosti a nazýva identitu Phase 2 s CDM presnou na
lineárnom ráde. Chýba však explicitná úplná sústava, gauge, constrainty a
hierarchia, ktoré by túto identitu dokázali. V staršom Postulates v1 bolo navyše
výslovne uvedené, že rast vyžaduje samostatný Jeansov test.

### 4.2 Neutrína a radiačná hustota

QCT Cosmology v7 pri rovnosti používa po prechode iba fotóny, `g*=2`, a tým
posúva rovnosť na `z` približne `5660`. Štandardné reliktné neutrína však nesú
nenulovú radiačnú hustotu; presný výpočet dáva `N_eff` približne `3.046`
([Mangano et al.](https://arxiv.org/abs/hep-ph/0506164)). Dokument pritom mieša
entropické `g_*s` a energetické `g_*eff`. Kým QCT neukáže konzistentnú neutrínovú
históriu a hierarchiu, odvodené skoršie `z_eq` a 68-percentný rastový náskok
nemajú rozhodovaciu váhu.

### 4.3 Zvuková rýchlosť nestačí na polohu CMB vrcholu

Z `c_s` a baryónového zaťaženia nemožno samostatne odvodiť `ell_1`. Treba
integrovať zvukový horizont, vzdialenosť k poslednému rozptylu, rekombináciu a
poruchy. Planck meria uhlovú akustickú škálu s vysokou presnosťou a jeho
šesťparametrový fit zahŕňa aj `A_s` a `tau`, ktoré QCT označuje ako neadresované
([Planck 2018 VI](https://doi.org/10.1051/0004-6361/201833910)).

### 4.4 Supersonický tok automaticky nemení stavovú rovnicu

To, že prúd je supersonický, samo osebe nemení lokálny pomer `p/rho` z `1/3` na
`0`. Rovnako zachovanie počtu buniek samo nedokazuje nulovú objemovú viskozitu a
najbližšie-susedská interakcia sama nedokazuje nulovú šmykovú viskozitu. Na tieto
závery treba mikroskopický collision kernel alebo kovariantný efektívny tenzor.

### 4.5 Otvorené normalizačné kruhy

QCT Cosmology v7 sama uvádza, že nezávislý vzorec pre `omega_D5` nie je
definovaný a vstupuje do reťazca vedúceho k `H0=69.6`. Phase 2 navyše pri tvorbe
prestreľuje požadovaný pomer k baryónom asi o osem rádov a frakcia približne
`10^-8` zostáva otvorenou termodynamikou. To nie je hotová alternatíva k našej
mikrofyzike popola.

## 5. Čo nám QCT môže reálne priniesť

### Prenositeľné ako otázka alebo test, nie ako výsledok

| Kandidát | Možný prínos | Podmienka použitia | Priorita |
|---|---|---|---|
| Dipól lokálneho `H0` korelovaný s veľkoškálovou štruktúrou | kontrola, či lokálny rebrík nesie smerovú systematiku | preregistrovať mapu, dataset a nulový model | nízka až stredná; neblokuje K7 |
| `a0 = c H0/(2 pi)` | samostatný test väzby galaktickej dynamiky na kozmologické pozadie | audit rotácií, lensingu, zhlukov a časového vývoja | parkovať mimo A2 |
| `delta rho_cell = g^2/(2 G c^2)` | alternatívna nelineárna efektívna hustota na galaktických škálach | odvodiť z akcie/Tmunu a preveriť solar-system, Bullet Cluster, CMB | samostatná A1 alternatíva, nie oprava K7 |
| Pole veľkosti bunky `s` | úplne iný fundamentálny smer, ak deliaca sa sieť raz definitívne zomrie | test driftu konštánt, Lorentza, GR, stability a plného CMB | iba budúca v4.0 koľaj |
| QCT proof-map štýl | dokumentačný vzor: oddeliť tvrdenie, závislosti a otvorenú medzeru | bez preberania fyzikálneho verdiktu | použiteľné priebežne |

### Neprenositeľné do aktuálnej K7

- `g*=2` po Phase 2;
- tvrdenie `Phase 2 = CDM` bez perturbatívnej sústavy;
- CMB výstup odvodený iba z podobnosti dvoch hustôt;
- hodnota `H0=69.6` bez uzavretia jej vlastného kritického reťazca;
- označenie širokých tvrdení za „proved“ v registri bez nezávislej kontroly dôkazu.

## 6. Dáva QCT našej teórii za pravdu?

Iba v najslabšom filozofickom zmysle: ďalší autor nezávisle skúma diskrétny
bunkový priestor, emergentnú gravitáciu, veľmi malé tenzory a kozmológiu bez
štandardného inflatónu. To je **prior art a tematická konvergencia**, nie
experimentálne ani matematické potvrdenie nášho delenia, `delta`, `lambda`,
paliva, pary, popola alebo relácie `n_s <-> w(z)`.

Pri publikovaní je vhodné QCT uviesť v prehľade príbuzných bunkových modelov a
výslovne vysvetliť rozdiel „konštantný počet meniacich sa buniek“ verzus
„rast počtu konštantných buniek“. Tým sa zároveň chráni naša priorita na vlastný
mechanizmus bez prehnaného tvrdenia, že všeobecná myšlienka bunkového priestoru
je unikátna.

## 7. Dopad na stav našej práce

- `A2-K4/K7`: bez zmeny fyzikálneho verdiktu a bez zmeny hĺbky `66.5/100`.
- G8: stále treba našu vlastnú plnú fotónovú/neutrínovú hierarchiu.
- G9: stále treba našu vlastnú CMB/S8 likelihood.
- Nevzniká nová živá podkoľaj K7.
- QCT kandidáty sa parkujú mimo A2. Pole premenlivej veľkosti bunky môže vzniknúť
  iba ako fundamentálne nová A1 vetva a podľa našich pravidiel by patrilo do v4.0.

## 8. Auditná hranica

Zadaný hlavný PDF má rovnaký SHA-256 ako kópia načítaná priamo zo Zenodo
recordu 20059776. Textová extrakcia všetkých rozhodujúcich dokumentov prešla.
Hromadný vizuálny render deviatich strán bol po prekročení 60 s ukončený a
nebol použitý ako dôkaz. Číselné tvrdenia v tomto audite sú preto založené na
textovej extrakcii s explicitnými hranicami strán a na verejných zdrojových PDF.

Audit v4.1 bol následne skontrolovaný proti trom rozhodujúcim dokumentom v32.
Záver o identite a nepoužiteľnosti pre K7 sa nezmenil. Nešlo o úplný audit
všetkých pätnástich súborov v32.

## 9. Primárne zdroje

- [Zenodo record 20059776, v4.1](https://zenodo.org/records/20059776)
- [Zenodo record 20199519, v32](https://zenodo.org/records/20199519)
- [QCT Main v101](https://zenodo.org/records/20059776/files/QCT-Main-v101.pdf)
- [QCT Postulates v8](https://zenodo.org/records/20199519/files/QCT-Supp-1-Postulates-v8.pdf)
- [QCT Cosmology v7](https://zenodo.org/records/20199519/files/QCT-Supp-5-Cosmology-v7.pdf)
- [QCT Proof Registry v12](https://zenodo.org/records/20199519/files/QCT-Supp-0b-ProofRegistry-v12.pdf)
- [Planck 2018 VI, cosmological parameters](https://doi.org/10.1051/0004-6361/201833910)
- [CLASS I, primary code paper](https://arxiv.org/abs/1104.2932)
- [Relic neutrino decoupling, primary calculation](https://arxiv.org/abs/hep-ph/0506164)
