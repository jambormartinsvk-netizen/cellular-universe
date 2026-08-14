# BUNKOVÝ VESMÍR — PRAVIDLÁ A REGISTER OTÁZOK: DODATOK v3.18

**Dátum:** 13. júl 2026  
**Jazyková autorita:** slovenská verzia  
**Základný register:** `theory/SK/05_Methodology_Rules_and_Question_Register_SK.md`

## 0. Vzťah k základnému registru

Tento súbor je záväzným pokračovaním súboru 05 pre v3.18. Časti 1–10 základného registra a ich pravidlá sa **nemenia ani nemažú**. Dodatok pridáva iba pravidlá, ktoré v základnom registri chýbali, nové otázky a zdôvodnené obmedzenia starších formulácií.

Pri rozpore o stave otázky platí neskorší, užší verdikt v tomto dodatku. Historická formulácia zostáva zachovaná ako auditná stopa.

## 1. Kontrola, že nové pravidlá neduplikujú staré

| Nové pravidlo | Najbližšie staršie pravidlo | Čo sa pridáva a nebolo pokryté |
|---|---|---|
| AR1 | Časť 2: NÁVRH → PREKLAD → SÚD → ŠKRT | Formálny status každého vstupu autora ako hypotézy a povinný výsledok auditu. |
| AR2 | Časť 3: K-ZROD | Postup pri viacerých možnostiach a presná podmienka smrti celej vetvy. |
| AR3 | Časť 2: falzifikácia; Časť 6: cintorín | Povinný dôkazový balík, zákaz mazania a podmienka založenia novej koľaje. |
| AR4 | P1–P5 | Povinné uchovanie skriptu, vstupu, výstupu, prostredia, verzie a opráv. |
| AR5 | Bez priameho ekvivalentu | Nemennosť publikovaných verzií, changelog, manifest a hashe. |
| AR6 | P5 | Rozlíšenie smoke testu, toy citlivosti, aproximácie, predikcie a fitu; rozsah verdiktu. |
| AR7 | Bez priameho ekvivalentu | Povinná obsahová synchronizácia SK/EN registra. |
| AR8 | AR4 (artefakty) a AR6 (rozsah) | Povinný audit prenosu fyzikálnej formulácie do každého downstream skriptu; staršie pravidlá nekontrolujú úplnosť stavu a koeficientov v implementácii. |
| AR9 | AR6 (rozsah) a AR8 (physics contract) | Zákaz zameniť efektívny/coarse-grained ledger za odvodený mikroskopický kauzálny graf. |

## 2. Nové auditné pravidlá AR1–AR9

### AR1 — Každý vstup autora je hypotéza

Každé nové fyzikálne alebo numerické tvrdenie dodané autorom vstupuje do práce ako **HYPOTÉZA**, nie ako výsledok. Audit mu pridelí stav:

- **PREŽÍVA N/100**, ak v testovanom rozsahu nenarazilo na potvrdený fyzikálny rozpor; alebo
- **MŔTVA**, ak presne definovaná formulácia neprešla fyzikálnou, matematickou, numerickou alebo štatistickou bránou.

Reprodukcia autorovej tabuľky potvrdzuje reprodukovateľnosť čísel, nie automaticky ich fyzikálny mechanizmus.

### AR2 — Vetvenie do koľají a smrť vetvy

Ak má problém viac konzistentných možností, vytvoria sa koľaje K1 až Kn. Najprv sa testuje koľaj s najväčšou predbežnou šancou na úspech. Každá koľaj má vlastnú hypotézu, testy, výstupy a kill conditions.

Koľaj prežije brány alebo narazí na zdokumentovanú stenu. Vetva zomiera až vtedy, keď zomrú všetky jej koľaje. Toto pravidlo dopĺňa K-ZROD; nemení jeho podmienky pre vznik novej koľaje.

### AR3 — Mŕtve koľaje sa nemažú

Mŕtva koľaj zostáva označená `MŔTVA — ARCHIVOVANÁ`. Musí sa uchovať:

1. presná hypotéza a jej rozsah;
2. test alebo zákon, ktorý neprešla;
3. presný dôvod smrti;
4. vstupy, jednotky, dáta, skripty a výstupy;
5. čo verdikt nezabíja;
6. podmienka, ktorá oprávňuje založiť novú koľaj.

Tá istá koľaj sa znovu neotvára iba premenovaním parametra, rozšírením gridu alebo iným optimalizátorom. Nová koľaj vyžaduje novú fyziku, opravu preukázanej chyby alebo nové nezávislé dáta a sekciu `Rozdiel oproti mŕtvej koľaji`.

Podrobný protokol: `Audit/00_PRAVIDLO_ARCHIVACIE_MRTVYCH_KOLAJI.md`.

### AR4 — Skripty a výpočty sú súčasť dôkazu

Každý výpočet použitý v audite má reprodukovateľný skript v `scripts`. Skripty a výpočty živých aj mŕtvych koľají sa uchovávajú.

Chybný skript sa ticho neprepíše. Zachová sa pôvodná verzia, vytvorí sa opravená verzia a Markdown erratum. Pri vydaní sa uloží reprodukčný príkaz, verzia prostredia, vstup, zmrazený výstup a SHA-256.

Ak je dôvod smrti výlučne analytický, záznam uvedie `výpočtový skript: NEBOL POTREBNÝ` a zachová úplnú argumentáciu. Skript sa nevytvára iba naoko.

### AR5 — Publikované verzie sú nemenné

Čísla a text už publikovanej verzie na Zenodo sa spätne neprepisujú. Každá ďalšia publikovaná verzia dostane:

- changelog voči predchádzajúcej verzii;
- manifest súborov;
- SHA-256;
- odkazy na erratá a zmenené verdikty.

Oprava vznikne ako nová verzia/záznam alebo explicitné erratum, nikdy ako tichá zmena historického výsledku.

### AR6 — Úroveň dôkazu a rozsah verdiktu

Každý numerický výsledok sa označí ako jeden z typov:

- `smoke test`;
- `toy sensitivity`;
- `aproximácia`;
- `fyzikálna predikcia`;
- `dátový fit`.

Lokálna suma rezíduí sa nesmie volať globálny likelihood. Post-data optimum nemá predikčnú váhu. Verdikt musí uviesť, či platí pre pozadie, perturbácie, mikrofyziku, numeriku alebo dátový fit. Prechod jednej brány nie je potvrdením celej teórie.

### AR7 — Povinná synchronizácia SK/EN

Dôležité pravidlo, otázka, zmena stavu, dôvod smrti a podmienka znovuotvorenia sa zapisujú do SK aj EN registra s rovnakým identifikátorom. Slovenská verzia je autoritatívna; anglická verzia je jej obsahovo verný zrkadlový záznam.

### AR8 — Audit prenosu formulácie do implementácie

Predtým, než nižší skript alebo pipeline dostane fyzikálnu váhu, musí mať
zverejnený **physics contract**: rodičovskú kovariantnú rovnicu, gauge,
stavový priestor, backgroundové koeficienty, úlohu Fourierovho módu, nulové
limity a Einsteinove constrainty. Lineage audit následne preverí, že každý
povinný prvok kontraktu je prítomný v downstream implementácii alebo je
výslovne označený ako kontrolovaná aproximácia.

Chýbajúci dynamický stupeň voľnosti, zmena smeru `Q^mu`, nahradenie
presného backgroundu radom mimo jeho platnosti alebo presun `k` do
backgroundu je **STOP implementácie**, nie iba solverová chyba. Staré
skripty a výsledky sa zachovajú, ale ich fyzikálny rozsah sa obmedzí.
Nástupca potrebuje nový stavový priestor/deriváciu a audit sa zopakuje pre
všetkých jeho potomkov. Prechod interných numerických kontrol redukovanej
RHS sám osebe nepotvrdzuje rodičovský mechanizmus.

### AR9 — Efektívny ledger nerozhoduje skrytú postupnosť

Rovnice pre homogénne zdroje `Q_A` môžu zachovať energiu a správne opisovať
pozadie, ale samy nerozhodujú, či produkty jednej udalosti vznikli paralelne,
postupne alebo cez nepozorovaný medzistav. Takéto poradie smie dostať stav
fyzikálnej predikcie len po odvodení lokálneho operátora/akcie/collision
kernelu, ktorý určuje `Q_A^mu`, podiely, prípadné oneskorenia a poruchy
`delta Q_A`.

Pozorovania potom koľaje vyberajú alebo vylučujú. Hodnota podielu či času
nastavená podľa týchto dát je fit, nie odvodený mechanizmus. Pravidlo je
užšie než AR6 (rozsah výsledku) a AR8 (prenos do kódu): chráni priamo
identifikovateľnosť mikroskopického kauzálneho grafu.

## 3. Register otázok Q17–Q34

| Q | Otázka | Aktuálny stav a brána |
|---|---|---|
| Q17 | Aká je trojbodová štatistika a `f_NL` z V-termalizácie? | **OTVORENÁ.** Prvý rád je iba odhad; treba tvar, znamienko, druhý rád, gauge-invariantný prevod na `zeta` a bispektrum. |
| Q18 | Kedy vzniká gravitónová para vzhľadom na približne 1280 e-foldov? | **KRITICKÁ, OTVORENÁ; fundamentálna A4 je P1 STOP v súčasnej v3.18.** Vyriešiť `dot(rho_g)+4H rho_g=C_g` cez zrýchlenú fázu, exit a reheating; až potom určiť `Delta N_eff`. Audit existencie potvrdil, že hladký kladný skorý zdroj s konečnou podporou a párovým ledgerom je fyzikálne možná efektívna FLRW trieda. M0/P1.1 a rozšírený P1.2 audit nenašli `C_g`, lokálny clock/stav ani `T_e^(mu nu)` rezervoára; A12 dáva iba podmienenú termalizačnú hranicu, nie zdrojovú históriu. Preto nejde o odvodenú kovariantnú mikrofyziku. |
| Q19 | Ktorú hmotovú zložku vytvára prenos `Q`? | **PREŠLA BRÁNOU POZADIA.** A1-K1 vytvára CDM/popol, baryóny sú konzervované. Nie je vybraná pre perturbácie; čaká T7/A2 a T8/A8. |
| Q20 | Aký je úplný gauge-invariantný systém porúch interagujúcich zložiek? | **KRITICKÁ, OTVORENÁ; P5 je `REVIEW_BLOCKED_ARCHITECTURE`.** K7 redukovaná báza vypustila dynamické `U_c`. P5.3g4/g5/g6 uzavreli svoje formula rozsahy a KMPC-024 tvrdo ukotvil M1 štandardný seed (`76/76`, štandardné constrainty PASS). Neskorší PF-058 audit však obmedzil jeho M3 tvrdenie: frakčný solver nepreukázal úplný palivový coefficient/row kontrakt, takže 15 frakčných constraint FAIL je STOP testovaného ansatzu, nie smrť K4; 6 power FAIL je iba truncation diagnostika. Pred ďalším runnerom treba ledger `Phi^0/Phi^1 × z^j`, synchronné species rovnice a total Bianchi mapu. K4-spätne viazaný plný seed, finite opacity a odvodený S1 parný seed stále chýbajú; P5.4/G8 sú zatvorené. |
| Q21 | Čo presne je `T` vo vzťahu `T proportional H`? | **KRITICKÁ, OTVORENÁ.** Potrebná termodynamická alebo mikrodynamická definícia bez použitia nameraného `n_s`. |
| Q22 | Ako vzniká gauge-invariantná krivostná porucha `zeta` z `delta E`? | **KRITICKÁ, OTVORENÁ.** Odvodiť `P_zeta`, `A_s`, `n_s`, running, izokurvatúry a bispektrum z jedného uzavretého systému. Podbrána Q22a: energeticky náročné delenia musia určiť spoločný zdroj `S`, jeho `P_S(k)` a prípadný `k_*` bez fitu; realizované Fourierovo `k` nesmie vstúpiť do `H(a)`. Q22a-K1 je overený iba ako efektívny A1 ledger `F->C`; nie je mikroverdikt. Q22a-K2 je **MŔTVA v dodanej perzistentnej priamej voľno-relativistickej forme**: samostatný rozpočet `Delta N_eff=0.0535` nedovolí taký zdroj. Q22a-K3 má presný conservation ledger, ale priamy parný podiel prežije iba pod `f_R~3.2e-5`; `b` stále neurčuje operátor. Jediný týmto sitom nevyvrátený koridor je skorý ukončený reliktný kanál Q18/Q23 plus neskorý `F->C`; nie je ešte odvodený ani ohodnotený. Mostový audit Q4/Q72 uzavrel spoločnú vstupnú bránu Q22a-G0: dnešné `delta`, `lambda` a skalárny zdroj produkcie ešte neurčujú úplný produktový operator. Kauzálne grafy a dôkazy sú v `Questions/Q22A_DIVISION_PRODUCT_SEQUENCE_TRACKS_SK.md`. |
| Q23 | Aký mechanizmus ukončí éru paliva a reheatuje vesmír? | **KRITICKÁ, OTVORENÁ.** Určiť koniec zrýchlenia, reheatingovú teplotu, entropiu, radiačnú dominanciu a počiatočné podmienky BBN. |
| Q24 | Je fundamentálna sieť 3D priestor s globálnym tikom alebo 4D kauzálna štruktúra? | **KRITICKÁ KONCEPČNÁ VOĽBA.** Odvodiť 4D Lorentzovskú limitu alebo priznať preferovaný rámec a otestovať jeho operátory. |
| Q25 | Ako jedna kapacita zabezpečí univerzálnu väzbu všetkých polí? | **OTVORENÁ.** Potrebná spoločná efektívna metrika pre viac spinových sektorov, ekvivalenčný princíp a limity birefringencie. |
| Q26 | Je krížová V-váha skutočne entanglementová entropia? | **OTVORENÁ.** Klasické váhy nestačia; treba Hilbertove priestory, stav `rho`, kvantový kanál a von Neumannovu entropiu. |
| Q27 | Aká je lokálna réžia pri fluktuujúcom stupni `k`? | **OTVORENÁ.** Rozhodnúť meraním medzi `1/(<k>+C)` a `<1/(k+C)>` na rastúcej periodickej sieti. |
| Q28 | Aký je dynamický význam `C=28` nezávislý od `n_s`? | **OTVORENÁ.** Odvodiť `C` z lokálnej symetrie/akcie pred CMB dátami a zahrnúť look-elsewhere effect. |
| Q29 | Spĺňa bunková dynamika druhý zákon termodynamiky? | **OTVORENÁ.** Definovať entropiu všetkých zásobníkov a dokázať nezápornú celkovú produkciu pri delení a prenose `Q`. |
| Q30 | Aké sú operačné kill conditions jednotlivých predikcií? | **ČIASTOČNE VYBAVENÁ METODIKA.** AR1–AR7 a archív mŕtvych koľají platia; každej predikcii ešte treba dataset, likelihood, prah, systematiky a verziu. |
| Q31 | Aký je mikrofyzikálny model popola? | **OTVORENÁ.** Určiť spin, hmotnosť, distribúciu, stabilitu, abundanciu, voľnú dráhu, phase-space, halo a klastrové testy. |
| Q32 | Aká je kontinuálna limita gravitácie? | **OTVORENÁ.** Odvodiť Poissonovu/Einsteinovu limitu, univerzálne `G`, šošovkovanie, PPN a dve gravitačné polarizácie. |
| Q33 | Odvodzuje bunková sieť znamienko a veľkosť globálnej krivosti bez použitia `H0` dát? | **OTVORENÁ; K4b PREŽÍVA 20/100.** Potrebná diskrétna krivosť, viac `N`/seedov, limita `N->infinity` a pred-dátové zmrazenie `Omega_K`. |
| Q34 | Môže delenie buniek vytvoriť kovariantnú výmenu hybnosti iba v tmavom sektore? | **PODMIEŇENE OTVORENÁ; S8-K1b PREŽÍVA 35/100.** Otvoriť až po základnej Q20; treba `F_A^mu`, protihybnosť, stabilitu a CMB/LSS test. |

## 4. Zdôvodnené obmedzenia starších formulácií

Staré formulácie sa nemažú. Nasledujúce riadky presne uvádzajú, prečo ich neskorší audit obmedzil.

### L1 — Q11 už nemožno označovať za globálne kompletnú

**Staršia formulácia:** Q11 `KOMPLET`, vrátane spektra a amplitúdy.

**Aktuálny rozsah:** horizontové čítanie zostáva kandidátom. Nie sú však uzavreté gaussovskosť Q11d, fyzikálny význam `T proportional H` (Q21), gauge-invariantný prevod `delta E -> zeta` (Q22), exit/reheating (Q23), status `m=1/2` ani úplná normalizácia skalárnych a tenzorových módov.

**Dôvod:** bez týchto krokov nie je odvodená pozorovateľná `P_zeta(k)` z uzavretej mikrodynamiky. Zhoda jedného sklonu s dátami nemôže nahradiť chýbajúci transfer a počiatočné podmienky.

### L2 — Q15 a `Delta N_eff=0.0535` sú podmienené

**Staršia formulácia:** tepelný gravitónový relikt a presná hodnota `Delta N_eff=0.0535` sú uzavreté.

**Aktuálny rozsah:** číslo je historický výpočet pri zadanom termálnom scenári.

**Dôvod:** relikt vytvorený pred približne 1280 e-foldmi zrýchlenej expanzie sa riedi ako `a^-4`. Bez zdroja počas/po tejto fáze a bez odvodeného exitu a reheatingu nemožno dnešnú teplotu ani `Delta N_eff` považovať za predikciu. Pozri Q18 a Q23.

### L3 — Q16 a `C=28` nie sú nezávisle odvodenou vetou

**Staršia formulácia:** `C=g_B=28` je odvodené a alternatívy boli popravené dátami.

**Aktuálny rozsah:** `C=28` prežíva ako mechanistické čítanie.

**Dôvod:** číslo 28 bolo v teórii prítomné pred sformulovaním testu a je previazané s čítaním `n_s`; to vytvára look-elsewhere a kruhovú validačnú možnosť. Potrebné je lokálne dynamické odvodenie nezávislé od CMB dát. Pozri Q28.

### L4 — „Jediná páka pre S8 je lambda->0.10“ bol iba obmedzený screening

**Staršia formulácia:** všetky vnútromodelové brzdy boli vylúčené a zostala iba zmena `lambda`.

**Aktuálny rozsah:** boli vylúčené konkrétne testované implementácie teplej DM a porúch pary, nie všetky fyzikálne možné mechanizmy.

**Dôvod:** ad hoc konštantné trenie celej látky S8-K1a je mŕtve pre chýbajúcu kovariantnú bilanciu a nerozlíšenie baryónov. Nová kovariantná tmavosektorová koľaj S8-K1b ešte nebola otestovaná. Krivostná K4b nie je odvodená zo siete. Žiadna z nich zatiaľ nie je predikciou.

### L5 — Všeobecná negravitačná interakcia DM nie je automatická smrť modelu

**Staršia formulácia:** každá potvrdená negravitačná interakcia DM zabíja model.

**Aktuálny rozsah:** smrteľná je interakcia, ktorá odporuje zmrazenému mikromodelu alebo observačným limitom.

**Dôvod:** popol zatiaľ nemá uzavretú mikrofyziku (Q31), takže univerzálny zákaz nie je odvodený. Q34 môže skúmať lokálnu kovariantnú výmenu hybnosti. Nie je to návrat k mŕtvej Le Sageovej koľaji #8, pretože nesmie obsahovať jej drag, ohrev a aberáciu baryónov.

### L6 — Percentá pokroku v3.17 sú historické

**Staršia formulácia:** `P_global približne 70 %` a zhoda približne `79 %`.

**Aktuálny rozsah:** ide o stav podľa vtedajšieho menovateľa otázok.

**Dôvod:** audit otvoril nové kritické brány Q18–Q34 a oddelil pozadie, perturbácie, mikrofyziku a likelihood. Aktuálny stav sa preto vedie cez brány A0–A8; staré percentá sa bez nového explicitného prepočtu nepoužívajú ako dnešný pokrok.

### L7 — K7d `66.5/100` nie je fyzikálnym dôkazom energy-frame A2-K4

**Staršia formulácia:** K7d G0–G7 PASS a hĺbka `66.5/100` podporujú aktívnu
K4 fyzikálnu koľaj až po G8.

**Aktuálny rozsah:** `66.5/100` zostáva historická technická hĺbka presne
uloženej redukovanej 13-zložkovej RHS. Aktuálne fyzikálne platná hĺbka K4 je
`60/100`; pred G8 je povinná P5 úplná general-synchronous báza.

**Dôvod:** následný lineage audit našiel, že K7 stav neobsahuje dynamické
`U_c` ani CDM hybnosť v `M`, hoci deklarovaný energy-frame prenos
`Q^mu=Gamma rho_f u_d^mu` ich pri relatívnej rýchlosti vyžaduje. Navyše
starý K7 background extrapoloval rad s `K_MPC=0.05` mimo jeho platnosti.
Pozri `Independent_Audits/K_MPC_0_05/13_P4C_K7_MISSING_UC_EXACT_BACKGROUND_STOP_SK.md`.

## 5. Aktuálne poradie práce

**AR68 — mantinelové pasy:** každá budúca G1–G9 brána a stanica A3/A4 musí
mať pred výpočtom svoj ledger fyzikálnych a observačných mantinelov;
neuzavretý mantinel dáva `REVIEW_BLOCKED`, nie tichý PASS. Kanonický register:
`Questions/00_GATE_AND_STATION_CONSTRAINT_LEDGER_SK.md`.

**AR69 — vlastníctvo artefaktov:** každý skript, base modul, výsledok a audit
má jedného route-conditioned vlastníka. Manifest zapisuje úplnú reťaz
`gate → preregistrácia → runner → base+SHA → výsledok → audit → verdikt`.
Historické súbory sa nekopírujú ani fyzicky nepresúvajú bez Git baseline,
úplnej path/SHA mapy a kontroly závislostí. Plné znenie:
`theory/SK/05_AR69_Canonical_Artifact_Ownership_and_Base_Core_SK.md`.

1. A0 je vybavené: nemenné vydania, budúci changelog a kontrolné súčty.
2. Q19/A1-K1 prešla iba bránou pozadia.
3. **Q20/A2 je bezprostredný ďalší krok.**
4. A3 implementuje model v CLASS/CAMB až po prechode A2.
5. Q18/Q23 a Q21/Q22 uzatvoria paru, exit a primordiálny sektor.
6. A8 je predregistrovaný plný fit; až potom sa aktualizujú predikcie `S8/H0`.
