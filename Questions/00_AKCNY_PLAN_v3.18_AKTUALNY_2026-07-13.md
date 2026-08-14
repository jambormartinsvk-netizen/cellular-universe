# Autoritatívny akčný plán v3.18

**Dátum:** 2026-07-13  
**Stav:** aktívny plán  
**Najbližší krok:** A2/Q20 — kovariantné perturbácie

## 1. Účel a prednosť

Tento plán nahrádza staršie poradie krokov všade, kde sa s ním rozchádzajú dokumenty:

- `Questions/otazky_a_navrh_krokov_v3.18.md`;
- staršie doplnenia registra otázok;
- historický balík `Nespracovane/krok_D_registrovy_balik.md`;
- predbežné plány vetvy `S8/H0`.

Staršie súbory sa nemažú a zostávajú auditnou stopou. Vedecké verdikty v ich neskorších autoritatívnych erratách zostávajú platné.

## 2. Rozhodnutie o poradí

Poradie je:

1. **A2 — perturbácie a stabilita základnej A1-K1**;
2. **A3 — nezávislá Boltzmannova implementácia a nulové limity**;
3. **A4/A5 — para, exit a primordiálne perturbácie**;
4. **A8 — vopred definovaný plný dátový fit**;
5. **až potom** nové tvrdenia o `S8/H0`.

Dôvod: bez A2 nevieme, či pracovný model vôbec má fyzikálne prípustné perturbácie. Ďalšie nastavovanie `gamma` alebo `Omega_K` na požadované čísla by iba zväčšovalo post-data flexibilitu.

## 3. A2 — aktuálny pracovný balík

### A2.0 — ledger zložiek, rámca a označení

Vytvoriť:

- `Questions/A2_Q20_problem_perturbacii_a_kolaje.md`;
- `Audit/A2_00_kovariantny_ledger_zloziek_a_interakcii.md`.

Povinný obsah:

1. zoznam všetkých zložiek: palivo, CDM/popol, baryóny, fotóny, neutrína/para a prípadná doména I;
2. pre každú zložku `rho`, `p`, `w`, pokojová rýchlosť, zvuková rýchlosť a anizotropný stres;
3. presná definícia metriky, signatúry, času a Fourierovej konvencie;
4. kovariantná bilancia

   `nabla_mu T_A^(mu nu) = Q_A^nu`, pričom `sum_A Q_A^nu = 0`;

5. rozklad

   `Q_A^mu = Q_A u^mu + F_A^mu`, pričom `u_mu F_A^mu = 0`;

6. explicitné rozlíšenie A1-K1, S8-K1a a S8-K1b.

**Brána A2.0:** žiadny zdroj energie ani hybnosti nesmie zostať bez prijímateľa a protizdroja.

**Kill condition:** ak sa nedá zostaviť `sum_A Q_A^nu=0` bez dodatočného fundamentálneho objektu, pôvodná koľaj zomiera. Nový objekt sa smie skúmať iba ako nová koľaj a môže znamenať v4.

### A2.1 — základná koľaj bez dodatočného trenia

Najprv odvodiť perturbácie pre samotnú A1-K1:

- energia prechádza z paliva do CDM/popola;
- baryóny sú osobitne konzervované;
- nepridáva sa fenomenologické `gamma_drag`;
- smer `Q_A^mu` a zvolený pokojový rámec musia byť explicitné.

Odvodenie urobiť aspoň v jednej úplnej gauge a výsledné pozorovateľné veličiny prepísať gauge-invariantne. Pre kontrolu je vhodné mať Newtonovu aj synchrónnu formuláciu alebo nezávislý algebraický cross-check.

**Výstup:** návrh rovníc v `Nespracovane/A17_A2_perturbacie_A1-K1_NAVRH.md`, nie priamy zápis do hlavného dokumentu.

### A2.2 — analytické testy T0–T8

| Test | Požiadavka | Kill condition |
|---|---|---|
| **T0 Notácia** | Jednotky, znamienka a rámec sú jednoznačné. | Dve časti dokumentu používajú nekompatibilné definície. |
| **T1 Celková bilancia** | `sum_A Q_A^nu=0` na pozadí aj v perturbáciách. | Energia alebo hybnosť vzniká bez protizdroja. |
| **T2 Nulový limit** | Pri `lambda -> 0` alebo `Q_A^mu -> 0` sa obnoví štandardný CDM+baryónový systém. | Zostane nový člen alebo nesprávny rast. |
| **T3 Gauge kontrola** | Pozorovateľné výsledky nezávisia od voľby gauge. | Rozdiel gauge mení fyzikálnu predikciu. |
| **T4 Superhorizont** | Správanie `k/(aH) -> 0` je regulárne; vývoj `zeta` je odvodený vrátane neadiabatických módov. | Divergencia alebo nevysvetlený rast skorého módu. |
| **T5 Subhorizont** | Správny limit rastu pri `k/(aH) >> 1`. | Nesprávny gravitačný zdroj, znamienko alebo limit bez interakcie. |
| **T6 Stabilita** | Bez ghostov, gradientovej nestability a nekontrolovanej skorej nestability. | Ľubovoľná z nich v oblasti parametrov používanej teóriou. |
| **T7 Pozitivita/regularita** | Hustoty, efektívne zvukové rýchlosti a menovatele zostávajú fyzikálne. | Záporná fyzikálna hustota alebo singularita pred dneškom. |
| **T8 Počiatočné podmienky** | Adiabatické/izokurvatúrne módy sú úplne špecifikované. | Výsledok závisí od skrytého alebo ľubovoľného počiatočného módu. |

**Rozhodnutie:** A1-K1 prejde do A3 iba ak prejde T0–T8 vo svojom deklarovanom rozsahu.

### A2.3 — numerická validačná vrstva

Po odvodení rovníc vytvoriť samostatný reprodukovateľný skript, predbežne:

- `scripts/21_script_A2_perturbation_limit_and_stability_tests.py`;
- `scripts/README_AUDIT_SCRIPT_21.md`;
- strojovo čitateľný výstup s parametrami, toleranciami a stavom každého testu.

Skript musí obsahovať minimálne:

1. nulový limit;
2. test zmeny gauge alebo nezávislého ekvivalentného zápisu;
3. sken skorých časov, `k` a parametrov na singularity;
4. test konvergencie kroku/tolerancie;
5. bilanciu energie a hybnosti;
6. oddelenie baryónov a CDM.

Výpočtový skript sa uloží do `scripts` ešte pred použitím jeho výsledku v audite.

### A2.4 — voliteľná koľaj S8-K1b

Otvoriť ju iba ak základná A1-K1 prejde A2.0–A2.3.

S8-K1b musí zaviesť fyzikálnu výmenu hybnosti, nie násobiteľ rastovej rovnice. Dokument musí určiť:

- ktoré dve zložky si hybnosť vymieňajú;
- lokálny kovariantný tvar `F_A^mu`;
- protihybnosť;
- či sa zachováva ekvivalenčný princíp pre baryóny;
- časovú a škálovú závislosť odvodenú z mechanizmu;
- limity z CMB, BAO, RSD, lensingu, halo a dark-sector scattering.

**Kill conditions:** nevybilancovaná hybnosť, priamy drag baryónov bez dovoleného mechanizmu, gauge artefakt, skorá nestabilita alebo parameter zavedený iba na trafenie `S8`.

### A2.5 — rozhodovací protokol

Po testoch vydať jediný stavový dokument:

- `Audit/A2_FINAL_Q20_perturbacie_a_stabilita.md`.

Možné výsledky:

- A1-K1 **PREŽÍVA** a postupuje do A3;
- A1-K1 **MŔTVA**, otvorí sa A1-K2 alebo ďalšia pôvodná koľaj;
- základná A1-K1 prežíva, ale S8-K1b je **MŔTVA**;
- obe prežívajú, no hodnotenie ostáva podmienené A3/A8.

## 4. A3 — Boltzmannova implementácia

Začať až po pozitívnom A2.

Poradie:

1. vybrať CLASS alebo CAMB a zmraziť verziu/commit;
2. bez bunkových členov reprodukovať štandardné referenčné spektrá;
3. implementovať A1-K1 bez S8-K1b;
4. porovnať dva nezávislé režimy/tolerancie;
5. až potom prípadne zapnúť S8-K1b;
6. uložiť patch, config, vstupné parametre a checksum výstupov.

Brány:

- `C_ell`, `P(k)`, background a rast sa v nulovom limite zhodujú s referenciou v stanovenej tolerancii;
- výsledok je numericky konvergentný;
- zmeny majú fyzikálne vysvetliteľný tvar, nie iba správny `S8`.

## 5. A4 a A5 — para a primordiálny sektor

### A4

Uzavrieť Q18/Q23:

- kedy para vzniká;
- s čím je v tepelnej rovnováhe;
- kedy decoupluje;
- kde je entropia pri delení;
- ako prebehne exit/reheating;
- z toho odvodiť `Delta N_eff`, nie ho vložiť ako cieľ.

### A5

Uzavrieť Q21/Q22/Q11d a status `m=1/2`, `C=28`:

- definovať, čo presne je teplota v `T proportional H`;
- odvodiť mapu mikroskopickej fluktuácie na gauge-invariantnú `zeta`;
- pred dátami odvodiť amplitúdu, sklon, running a negaussovskosť;
- kvantifikovať look-elsewhere effect pri `C=28`.

## 6. A6 — kauzálna a gravitačná brána

Táto vetva zostáva fundamentálne kritická. Musí dodať aspoň jedno:

1. emergentnú 4D Lorentzovskú kauzálnu štruktúru s kontrolovanými korekciami; alebo
2. explicitnú preferovanú foliáciu/rámec s odvodenými pozorovateľnými odchýlkami a ich limitmi.

Bez toho sa teória môže prezentovať ako efektívny kozmologický model v zvolenom rámci, nie ako hotová náhrada všeobecnej relativity.

## 7. K4b — vedľajšia koľaj krivosti

Môže bežať nezávisle, ale s nižšou prioritou než A2.

Požadované kroky:

1. definovať diskrétnu krivosť (napr. deficitné uhly/Reggeho ekvivalent);
2. simulovať viac veľkostí `N` a náhodných seedov;
3. odvodiť škálovanie pri `N -> infinity`;
4. pred pozretím na kozmologické dáta zmraziť znamienko a amplitúdu;
5. až potom porovnať s limitmi na `Omega_K`.

Ak `Omega_K` iba voľne nastavíme podľa `H0`, nejde o predikciu bunkovej siete.

## 8. A7 — dokumentácia a skripty

Priebežné pravidlá:

- každý použitý výpočet má skript v `scripts`;
- každá budúca brána G1–G9 a stanica A3/A4 má pred výpočtom mantinelový pas
  podľa `Questions/00_GATE_AND_STATION_CONSTRAINT_LEDGER_SK.md`; neuzavretý
  mantinel znamená `REVIEW_BLOCKED`, nie tichý PASS;
- každý skript má verziu, vstupy, jednotky, rozsah platnosti a test tolerancie;
- výstup sa označí ako `smoke test`, `toy sensitivity`, `approximation` alebo `physical prediction`;
- pôvodný skript sa spätne ticho nemení; oprava dostane nový skript alebo explicitné erratum;
- skript 09 zostáva pozadím/citlivostnou aproximáciou a nesmie dostať ad hoc drag ako náhradu A2/A3.

## 9. A8 — predregistrovaný dátový test

Pred spustením zapísať do Markdownu:

- presný zoznam datasetov a ich verzií;
- likelihoody, covariance a nuisance parametre;
- voľné a odvodené parametre, priory a počet stupňov voľnosti;
- nulový model a porovnávacie kritérium;
- kill thresholds;
- validačné dáta, ktoré sa nepoužijú na ladenie.

Povinné výstupy majú zahŕňať posterior/predikciu pre CMB, BAO, SN, RSD, weak lensing, `H0`, `Omega_m`, `S8` a kontrolu parametrových degenerácií.

Lokálne `chi2_3front` sa už nesmie nazývať celkový fit.

## 10. Dve možné vydávacie koľaje

### R3.18-DOC — odporúčaná najbližšia verzia

Cieľ: poctivá opravná a dokumentačná verzia bez nového nároku na presnú kozmologickú predikciu.

Pred vydaním:

1. dokončiť changelog od v3.17/Zenodo v2;
2. zapracovať A1-K1 iba ako kandidáta pozadia;
3. odstrániť alebo opraviť tvrdenia, že skript 09 či gridy 17–20 dokazujú `S8/H0`;
4. priložiť register otvorených brán;
5. vytvoriť manifest súborov a SHA-256;
6. skontrolovať SK/EN zhodu;
7. publikovať ako nový nemenný záznam/verziu.

### R3.18-PHYS — verzia s novými kozmologickými predikciami

Musí počkať na A2, A3 a A8. Ak tieto kroky zmenia fundament, vydanie sa preklasifikuje na v4.

## 11. Čo sa teraz nerobí

- ďalší grid `gamma` a `Omega_K` iba na trafenie `H0=68`, `S8=0.82`;
- vyhlasovanie post-data optima za predikciu;
- pridanie nového člena priamo do rastovej rovnice bez kovariantnej bilancie;
- propagovanie A16 návrhu do hlavného dokumentu ako uzavretú fyziku perturbácií;
- plný fit pred existenciou A2/A3.

## 12. Najbližší konkrétny výstup

Nasledujúci pracovný dokument má byť:

`Questions/A2_Q20_problem_perturbacii_a_kolaje.md`

Začať koľajou s najväčšou šancou:

**A2-K1: kovariantný energetický prenos palivo -> CDM/popol v rámci A1-K1, bez dodatočného trenia.**

## 13. Aktualizácia 2026-07-14 — A2-K12, dvojzložkový popol

Nová koľaj A2-K12 skúma dva druhy popola s opačnými skalárnymi nábojmi.
Prvá analytická brána mala historický checkpoint `25/100`; jednotná sekvenčná rekalibrácia jej dáva `10/100 = G1`, pretože G2 production ledger nie je uzavretý.

- K12-K1 je `MŔTVA M-016`: presná symetria ruší čistý skalárny tok a
  lineárny celkový mód zostáva GR-like.
- K12-K2 zostáva otvorená, ale má červený kompromis medzi asymetriou, tokom
  a netienenou piatou silou.
- K12-K3 je aktívna hypotéza: palivo produkuje páry `c+ c-`, zatiaľ čo
  opačné náboje určujú následnú silovú maticu.

Nasledujúci krok `K12-K3.1`:

1. odvodiť lokálny produkčný operátor `fuel -> c+ + c-`;
2. uzavrieť celkový kovariantný ledger;
3. odvodiť celkový a nábojový lineárny mód;
4. vykonať superhorizontovú, high-k a izokurvatúrnu bránu;
5. až po ich prejdení počítať `S8`.

K12 sa nesmie propagovať do predikčnej tabuľky v3.18 na základe samotného
odpudzovania alebo publikovaných nelineárnych halo efektov.

## 14. Autoritatívna priorita — zachrániť alebo vyčerpať A1-K1

Hlavnou úlohou zostáva nájsť fyzikálne konzistentný A2 uzáver backgroundu
A1-K1. K12 je iba jedna z kandidátskych tried a nemení tento cieľ.

A1-K1 zostáva `OTVORENÁ A PODMIENENÁ`, kým existuje aspoň jedna otvorená
fyzikálne odlišná A2 koľaj alebo kým neexistuje všeobecný no-go dôkaz.
Smrť jednej dcéry sa na rodiča neprenáša automaticky.

Aktuálne poradie:

1. K4.3, pretože K4.1 a K4.2 prešli;
2. po smrti K4.3 K8.1;
3. potom K9.1, K12-K3.1 a K11.1 podľa výsledku predchádzajúcej steny;
4. zachovať a auditovať iba fyzikálne nové otvorené listy K7.

A1-K1 sa opustí až po stopping kritériu v
`Questions/A1_K1_A2_AUDITNY_PROGRAM_A_STOPPING_KRITERIUM.md`. K10 sa do
tohto vyčerpania nepočíta, pretože už mení background a patrí k ďalšej A1
koľaji.

## 15. Aktualizácia 2026-07-14 — K4.1 dokončená (historický stav pred K4.2)

K4.1 prešla úplnou constraintovo prípustnou regulárnou bázou
perfect-radiation systému aj nezávislým fixed-RK4 krížovým testom. K4 sa
mala v starom intervalovom systéme posun z `50/100` na historický checkpoint **`55/100`**; podľa jednotnej stupnice to znamená prejdenú G5=`50/100`.

Rozhodujúce zistenia:

- indiciálny systém má presne tri regulárne módy;
- historický fuel-only velocity seed má projekčné rezíduum `0.9789492202`
  a neleží v regulárnom primordiálnom priestore;
- maximálny absolútny singulárny transfer je `26.4369073223`, takže pri
  amplitúde `1e-5` zostáva auditná norma `2.64369e-4`;
- hlavný DOP853 aj nezávislý fixed-RK4 výpočet prešli constraintovou a
  krokovou konvergenciou.

V čase tejto aktualizácie bola bezprostredná úloha **K4.2**; jej výsledok je v sekcii 17:

1. odvodiť high-k hlavný symbol;
2. preveriť kinetické a gradientové znamienka;
3. overiť nulový limit a fyzické vlastné módy;
4. integrovať reprezentatívne subhorizontové škály bez ladenia na `S8`;
5. vydať nový rozsudok s dôvodom a zachovaným skriptom.

K4 zatiaľ nie je plný A2 survivor a nepostupuje priamo do likelihoodu.
Táto podmienka je uzavretá sekciou 17: K4.2 prešla; historický M-011 sa
neobnovil ako dôvod smrti.

## 16. Aktualizácia 2026-07-14 — audit externého návrhu K11/script 47

Externý skript 47 reprodukoval deklarované tlmenie, ale jeho
`PASS_RIGOROUS_S8_K1b_AUDIT` bol fyzikálne zamietnutý.

- `-(4-3 delta)` patrí barotropickému uzáveru, nie deklarovanému
  `c_s^2=1` uzáveru s tlakom `delta_f/delta`;
- proper-time sadzby sú chybne delené `aE`, čo ich pri štarte zosilňuje
  faktorom `1090.9`;
- energetický tok a drag nie sú správne oddelené;
- fuel kontinuita je neúplná;
- bodové relatívne `00` rezíduum je pri `A=1e6` a `1e8` približne `1.0`;
- amplitúdové škálovanie overuje iba numeriku homogénnej lineárnej ODE.

Skript 47 sa zachováva ako odmietnutá implementácia. Nie je novou koľajou a
M-015 sa nevydáva. Historický checkpoint K11 bol `15/100`; jednotná rekalibrácia ho vedie ako `G1=10/100`, pretože G2/G3 neprešli.

V čase auditu skriptu 47 zostával bezprostredný krok K4.2. Sekcia 17 ho
uzatvára a mení prioritu na K4.3. Pri neskoršom návrate ku K11 treba najprv odvodiť lokálny operátor a úplný
constraintovo uzavretý systém; až potom opakovať numeriku.
## 17. Aktualizácia 2026-07-14 — K4.2 dokončená

K4.2 prešla v deklarovanom perfect-radiation rozsahu a A2-K4 sa posúva na
**`PREŽÍVA K4.2 — 60/100 = G6`**. Starých 59 bol intervalový checkpoint; fyzikálny výsledok sa nemení a nový dôvod smrti sa nevydáva.

Rozhodujúce výsledky:

- high-k polynóm je `mu^4(mu^2+1)(mu^2+1/3)`; propagujúce rýchlosti sú
  `±1` a `±1/sqrt(3)`;
- interakcia je nižšieho rádu `k^0` a má správny `lambda=0` limit;
- štandardné prachové nulové Jordanove bloky sú prítomné aj pri `lambda=0`
  a nie sú novou K4 nestabilitou;
- všetky tri regulárne módy prešli na `q=30,300,1000`;
- najväčší `1e-5 T_max=0.240017` a aktívne bodové `00` rezíduum bolo najviac
  `4.41484e-8`;
- `T_max` K4 bol na každom q menší než nulový limit;
- riešičová, backgroundová a start-time konvergencia q=300 prešli.

Historický M-011 sa nemaže. K4.1 obmedzila jeho seed na neregulárny
primordiálny vektor a K4.2 ukázala, že na úplnom regulárnom subhorizontovom
priestore nevzniká deklarovaná K4 high-k explózia. Nová smrť musí mať nový
dôvod a zachované skripty.

Bezprostredná úloha je **K4.3**:

1. predregistrovať brány plnej Einstein–Boltzmannovej implementácie;
2. doplniť samostatné fotónové a neutrínové hierarchie a anizotropný stres;
3. doplniť baryón-fotónovú tesnú väzbu a rekombináciu;
4. zachovať rovnaký K4 lokálny transfer bez nového drag fitu;
5. urobiť gauge alebo nezávislý implementačný krížový test;
6. vypočítať CMB-normalizované transfery a až potom `sigma8`, `S8` a A3
   likelihood.

Ak K4.3 zomrie, nasleduje K8.1. TIMEOUT alebo nedokončená implementácia nie
sú fyzikálnou smrťou.
## 18. Jednotná sekvenčná rekalibrácia skóre

Od 2026-07-14 sa skóre udeľuje iba za najvyššiu sekvenčne prejdenú bránu
G1–G10. Najhlbší vykonaný no-go alebo kill test sa eviduje osobitne a
nezvyšuje skóre pri preskočených medzibránach.

| Koľaj | Kanonická hĺbka | Najhlbší test / otvorená brána |
|---|---:|---|
| K1 | 40 | G5 no-go |
| K2 | 30 | G6 gradientový FAIL |
| K3 | 40 | G5 no-go |
| **K4** | **60** | **G7 otvorená** |
| K5 | 40 | G6 vykonaná; G8 hybridný CMB FAIL/M-012 |
| K6 | 30 | G6 `G_ij` no-go/M-013 |
| K7 | 20 | G3 otvorená cez podkoľaje |
| K8 | 10 | G2 otvorená |
| K9 | 10 | G2 otvorená |
| K10 | 10 | iná A1 vetva |
| K11 | 10 | G2/G3 otvorená |
| K12 | 10 | G2 otvorená |

K4 je teda najďalej **sekvenčne** preverená koľaj. K5 zostáva oprávnene
mŕtva M-012, ale jej starý neskorý hybridný screen už nie je vydávaný za
sekvenčne prejdených 75 bodov.

K4.3 sa delí podľa jednotnej hranice:

1. **A2-K4.3 / G7:** vlastný Einstein–Boltzmann, úplné počiatočné módy,
   fotóny, neutrína, anizotropný stres, tight coupling, rekombinácia,
   constraint/null/gauge/convergence a fyzické transfery;
2. po prejdení celej G7 sa K4 zvýši na `70/100` a A2 ju odovzdá do A3;
3. **A3-K4 / G8:** CMB normalizácia, `sigma8`, `S8` a rastový screen;
4. **A3-K4 / G9:** plná spoločná likelihood a systematiky.

Autoritatívny audit a changelog:
`Audit/JEDNOTNA_SEKVENCNA_STUPNICA_HLBKY_A2_A_REKALIBRACIA_K1_K12.md`.

