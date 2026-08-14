# Aktuálny vykonávací plán v3.18

**Aktualizované:** 2026-07-19  
**Autorita:** hlavný orchestrátor  
**Aktívna cesta:** `A1-K1 -> A2-K4 -> P5`  
**Nahrádza pre aktuálnu navigáciu:** staršie globálne akčné plány; tie zostávajú historickými dôkazmi  
**Pravidlo údržby:** tento súbor sa aktualizuje iba pri uzavretí brány, zmene aktívnej cesty, PT1/PT2 udalosti alebo release baseline

## 0. Týždenná tokenová pauza — ukončená používateľom

**Stav:** `RESUMED_BY_EXPLICIT_USER_AUTHORIZATION_2026-07-18`  
**Pôvodný predpokladaný návrat:** 2026-07-24 — už neplatí  
**Autorita zmeny:** používateľ výslovne povolil pokračovať vo výpočte.

Povolený numerical boundary audit bol dokončený cez technických nástupcov
KMPC-037→039 bez zmeny matice alebo prahov. KMPC-040 potom v samostatne
predregistrovanom step 3 uzavrel CDI candidate support `[0,5]` voči `[0,7]`
pre `k=.05 / nominal`; common `0…5` aj tail `6,7` prešli.

KMPC-044 uzavrel BI order-7 numerical boundary. KMPC-045 potom zachoval
technickú PF-074 bez fyzikálneho payloadu; KMPC-046 potvrdil BI `[0,5]`.
KMPC-047 až 053 uzavreli NID `[0,5]` po M1 depth-7 a numerical-boundary
audite. KMPC-054 až 056 samostatne uzavreli NIV: `[-1,2]` bol nedostatočný,
ale pri M1 depth 6 je `[-1,4]` dostatočný voči `[-1,6]`. PF-076 ostáva
zachovaný ako technická owner chyba bez fyzikálneho verdiktu.

KMPC-057 až 060 uzavreli tri fail-closed smoke chyby PF-077 až PF-079 a
presnú support-semantics diagnózu bez fyzikálneho atómu. KMPC-061 prešiel
preflight. KMPC-063 uzavrel prvý C2 atóm `AD/k=.005/nominal`: candidate
support `[0,6]` voči audit `[0,8]` prešiel. KMPC-065 potom otestoval
AD/k=.15; KMPC-066 uzavrel candidate support `[0,4]` voči `[0,6]`, pričom
najhorší tail na `.01` bol `9.14e-9/1.52e-8 < 1e-6`. C2 je `2/10 PASS`.
KMPC-067 až 073 potom uzavreli CDI/k=.005 na accepted `[0,7]` voči
`[0,9]`; checkpointové PF-081 až PF-084 nemenia fyziku a jediný výsledkový
candidate je KMPC-073. KMPC-074 našiel na CDI/k=.15 jediný M3 driver
boundary `3.84e-10 > 1e-10`; KMPC-075 ho na presne tej istej 104×104 matici
uzavrel tromi residual corrections na `1.11e-16`. KMPC-078 potom uzavrel
BI/k=.005 cez hashovaný checkpoint. KMPC-083 potom vyriešil tú istú
float64-zostavenú BI/k=.15 driver maticu pri 80 dps: driver klesol na
`9.82e-82`, ale nezávislý `Einstein_0i[7]` ostal `3.019756782e-9 > 1e-9`.
KMPC-086 znovu zostavil celý 16×104 holdout pri 80 dps a dostal prakticky
rovnakých `3.019756712e-9`. KMPC-087 následne zostavil aj 104×104 driver pri
80 dps: driver prešiel na `8.72e-82`, ale nezávislý `Einstein_0i[7]` ostal
`3.019756578e-9`. Solve, holdout assembly aj driver assembly roundoff sú tým
vylúčené. KMPC-092 potom úplným 73-term ledgerom zrekonštruoval holdout do
`2.30e-67` a nameral cancellation factor `8.91e8`. Dominantný otvorený blok
je fractional background × M1 (`-7.04819e-9`), kým F0 je iba
`-1.80023e-11`. KMPC-099/100 potom izolovali M1 maticu: natívna 80-dps
assembly po binary64 projekcii aj frozen rebuild majú rank `98/98`, condition
`634.52` a relatívny matrix rozdiel iba `6.09e-18`; RHS je identická. QR
výnimka bola lokalizovaná na HP solver/algoritmickú hranicu, nie na projected
rank alebo assembly. KMPC-102 potom na natívnej 80-dps matici explicitným
CPQR potvrdil rank `98/98`, relatívnu faktorizáciu `1.00e-82`, normálový
reziduál `7.85e-85` a uzavrel lokálne M1 driver/holdout riadky. HP-M1 solver
boundary je diagnosticky uzavretá. C2 je `5/10 PASS`; ďalší krok je jediný
downstream-insertion audit cez zachovaný 13-stavový register a zmrazený
F0/M3/non-fit holdout pipeline.

## 1. Aktuálny stav

| Oblasť | Autoritatívny stav | Čo z toho vyplýva |
|---|---|---|
| A2-K4 | **ŽIVÁ / ARCH_A COMPLETED / HISTORICAL 10 / ACTIVE TECH 0/10 / J4 SENTINEL SUPPORT PASS** | koľaj nemá fyzikálny STOP; hĺbka zostáva 60/100 |
| fyzikálna hĺbka K4 | `60/100` | historických `66.5/100` z redukovanej K7 RHS sa neprenáša |
| P5 | `3.5/6` oporných bodov | M1 anchor prešiel; úplný palivový coefficient/row kontrakt nie |
| P5.3 | B1 PASS; `.05/nominal` support uzavretý; C2 `5/10 PASS` | AD/CDI a BI/k=.005 uzavreté; BI/k=.15 natívny HP-M1 CPQR rank `98/98` prešiel, čaká jediný downstream F0/M3/non-fit holdout insertion audit |
| P5.4 | NOT RUN | nesmie sa spustiť pred plným seedom |
| G8/G9 | BLOCKED | plná hierarchia ani likelihood ešte nesmú bežať |
| R7 mŕtvych A2 koľají | `CONFIRMED_SCOPE` pre K1,K2,K3,K5,K6 | nájdené chyby nespôsobili ich falošnú smrť; rozsudky sa nesmú rozširovať mimo mechanizmu |
| živé zálohy K7/K8/K9/K11/K12 | `R8 BLOCKER MAPPED` | rodičia žijú, ale bez konkrétneho kernelu sa nesmú umelo tlačiť ku G5 |
| existenčná brána záloh | `FS-GATE-01 K8/K9/K11/K12 CLOSED AT MOMENT SCOPE` | momentové prieniky sú zmapované; body sa nepridali, ale presné mŕtve podtriedy a zostávajúca mikrofyzika sú oddelené |
| Git | pracovná vetva existuje, baseline commit chýba | `16` tracked rozdielov a `1 331` neignorovaných untracked súborov sa nesmú stageovať hromadne |
| release | PT1 evidence vznikla, PT2 nevznikol | staré podmienené predpovede treba scope-obmedziť bez vymýšľania náhradných čísel |

Fyzikálny verdikt sa týmto plánom nemení. R-A a R-B nižšie sú dve
matematické implementácie toho istého K4 mechanizmu, nie nové fyzikálne
koľaje.

## 2. Bezprostredné poradie práce

### FS-A2 — ohraničený behaviorálny audit živých záloh

Tento analytický program môže bežať popri K4-B1, pretože nemení aktívnu
fyziku ani nespúšťa solver. Používa
`tracks/A1/A1K1/A2/00_CONSTRAINT_FEASIBILITY_LEDGER.md`.

1. pre každú koľaj zmraziť priestor dovolených vstupov a výstupov;
2. doplniť nulové body, znamienka, monotónne trendy, energetické maxima a
   regularitu známe bez mikrofyziky;
3. hľadať priamy rozpor, PSD/dual certificate alebo endpointový no-go;
4. pri neprázdnom behaviorálnom obale skonštruovať jeden najjednoduchší
   fyzický svedok bez fitu na `S8/H0`;
5. zlyhanie svedka zabije iba dcéru; rodič až po certifikáte prázdnosti
   celého vopred definovaného priestoru.

Poradie: K8-Fkin, K9 iba ak ten istý proces dá rozptyl, K11-R, K12-K3.1 a
K7. Pozorovania smú behaviorálny obal vylúčiť; nesmú sa použiť na spätné
nakreslenie ľubovoľnej funkcie.

#### Výsledok FS-GATE-01 pre prvé štyri rodiče

| Koľaj | Dokázane neprázdny rozsah | Certifikovane prázdny alebo zliaty rozsah | Ďalšia rozhodujúca brána |
|---|---|---|---|
| K8 | pozitívny okamžitý on-shell momentový kužeľ | warm source-only + exact pressureless A1 je prázdny; cold source-only sa zlieva s K1/M-009 | iba nový relaxačný proces; spoločný production/scattering patrí K9 |
| K9 | cold Markovský momentový generátor môže mať produkciu aj lineárny drag s nulovým FLRW ohrevom | smooth 1->2 exact-cold finite-rate prah je prázdny; voľný druhý `kappa` nie je K9 | jedna akcia/kernel odvodzujúci production/transport pomer, fuel reakciu a noise |
| K11 | regular constitutive drag existuje; CS1 early indicial limit je GR-like; CS2 source-AST contract prešiel `55/55`, register `25/33/41` | uniform regular exact-pole, passive Hurwitz cure a univerzálna exact finite-L CAMB-E closure sú prázdne | ARCH-A 5/10; ďalší je full thermal/TCA/DAE balík 6/10, potom povinná `lmax`/closure konvergencia |
| K12 | cold neutral pair moment s korelovaným PSD noise existuje | opposite charge neruší pressure; symmetric internal force nemení COM/K1; smooth exact-cold 1->2 finite-rate prah je prázdny | coherent/cold finite-rate kernel, externý total momentum/field ledger a stabilný separation mód |

Žiadny z týchto momentových výsledkov nie je G2/G3 PASS, preto hĺbka
K8/K9/K11/K12 zostáva `10/100`. Sú však informačne rozhodujúce: už sa
nesmie vracať k warm source-only K8, k voľnému K9 drag parametru, k starému
K11 operátoru ani k predstave, že opačné náboje K12 bez tlaku priamo tlmia
total mód.

#### Najbližší FS-A2 krok

`K11-CS1` je uzavretá ako `UNDETERMINED_REVIEW`: dark rovnice a constrainty
sú známe, early indicial limit je GR-like, ale fyzický fixed-delta symbol je
viacdruhová časovo závislá DAE. `K11-CS2` má route-local predregistráciu a
S0 formula ledger prešiel, ale PF-062 zrušil v001 state-register PASS pre
nadbytočné `E_0,E_1`; správny count je `4*lmax+9`. S0 base je zmrazená ako
formula-regression/STOP-state dôkaz. Najbližší krok je nový versioned full
base s exact-A1 backgroundom,
regular basis, všetkými species/shear, constraint holdoutmi a jedným
ohraničeným propagátorom. Očakávanie `ln` relatívneho transferu ostáva
`10–13` pre absolútny K1-like rast, kým očakávaný samotný účinok K11-R
`ln(A_full/A_drag_null)` je iba približne `-0.14`; tieto dve čísla sa
nesmú zlúčiť. Full v002 je rovnaký fyzický suffix; ARCH-A použila `5/10`
poradových miest a nevytvára v003, kým sa nemení fyzika. Ak desiaty balík
vetvu neuzavrie, zastaví sa iba ARCH-A s presným dôvodom. Pred full DAE
spustením musí mať exact-A1 `x_e/opacity/T_b`, TCA mapu a deklarovaný
numerický horný rez s konvergenčným plánom; štandardná ΛCDM opacity alebo neoverený
handoff by skončili iba `REVIEW_BLOCKED_IMPLEMENTATION`.

Read-only source audit už pripol `external/CLASS` commit
`e85808324f51fc694d12e3ed7439552a3c3f9540`: CLASS odovzdáva exact
background `H(z)` priamo HyRec, takže architektúra je uskutočniteľná.
Full v002 však nie je úzky adapter. Pred implementáciou treba coupled
present-day-normalized fuel/ash background, custom K11 species/mode ledger,
nezávislú steam hierarchy, exact CAMB-E/CLASS polarization mapu a
netautologické holdouty. Stav ostáva `REVIEW_BLOCKED_IMPLEMENTATION`, bez
Python behu a bez zmeny hĺbky.

K9/K12 zostávajú za mikrofyzickou bránou. K7 sa znovu otvorí až po dodaní
nového spektrálneho kernelu mimo už mŕtvych M-014 podtried; opakovanie
starých bath ansatzov nemá informačnú hodnotu. K4 zostáva hlavnou cestou na
`60/100`.

### B0 — bezpečný Git control-plane baseline

**Cieľ:** najprv zachovať auditnú stopu, aby následné presuny a opravy boli
vratné a porovnateľné.

Povinné výstupy:

1. úplný WB-0 manifest tracked, untracked, ignored a veľkých súborov;
2. secret scan bez vypisovania nájdených tajomstiev do logu;
3. desaťriadková migračná mapa `theory/theory -> theory` s Git blobom a
   SHA-256, bez vykonania presunu;
4. explicitný staging manifest prvého commitu;
5. WB-1 control-plane commit iba na
   `work/v3.18-audit-2026-07-16` a push na túto pracovnú vetvu.

Do WB-1 sa nesmú potichu dostať deletions koreňového `LICENSE`, `README.md`,
EN README, starých `theory/theory` ciest, hlavné teoretické dokumenty,
vedecké skripty ani externé PDF. Nepoužiť `git add .`.

**STOP B0:** nejasná licencia, nájdené tajomstvo, nejednoznačná migračná
parita alebo staging mimo manifestu.  
**PASS B0:** auditovateľný malý commit a zhodný vzdialený pracovný branch;
`main` aj `D:\Teoria-main` zostanú nedotknuté.

### R0 — PT1 trigger ledger, časovo citlivý

Po potvrdení PT1 dátumom 2026-07-16 treba zapísať pracovný Git záznam
najneskôr do troch pracovných dní a cieľ úzkeho Zenodo DOC/ERRATUM vydania je
2026-07-30. Zatiaľ sa nič nepublikuje a v3.17 sa neprepisuje.

| Verejný riadok | Pracovný stav pre ledger | Náhrada |
|---|---|---|
| `N_eff = 3.09–3.10`, resp. `Delta N_eff=0.0535` | `SUPERSEDED IN SCOPE / CONDITIONAL ESTIMATE` | `NOT YET AVAILABLE` |
| tepelné pozadie `0.90 K / 53 GHz` | `SUPERSEDED IN SCOPE / RECALCULATION OPEN` | `NOT YET AVAILABLE` |
| `H0 = 66.4 km/s/Mpc` | `MATERIAL IMPACT AUDIT REQUIRED` | až po citlivosti `Delta N_eff: 0.0535 -> 0` |

PT1 sa musí premietnuť do SK/EN CSV, PDF, README, Zenodo popisu a relevantnej
časti hlavného dokumentu. PT2 nevznikne, kým náhradný výsledok neprejde
odvodením, reprodukciou, nulovým/konvergenčným testom a nezávislým auditom.

### K4-B1 — uzavreté ako contract preflight; bez fyzikálnych bodov

Najprv sa použije rádovo konzistentná formulácia **R-A**. Pred ďalším kódom
treba uzavrieť jeden analytický balík so štyrmi položkami:

| Krok | Váha v pracovnom progress B1 | Povinný obsah |
|---|---:|---|
| B1.1 coefficient manifest | 15 % | pre každý objekt `Phi^0/Phi^1 × z^j`, zdrojová rovnica, stav kotva/neznáma/nula a vstup do `T_mu_nu` |
| B1.2 species term map | 25 % | synchronné fuel a ash continuity/Euler priamo z rovnakého `Q_A^mu`, znamienka, gauge a velocity konvencie, rozmery a nulové limity |
| B1.3 Bianchi/left-null identita | 35 % | presné zrušenie transferu v celkovej energii aj hybnosti; derivácie `00` a `0i` z nezávislých rovníc |
| B1.4 architektonické uzavretie | 25 % | z ledgeru odvodený počet stavov/riadkov; `00` a `0i` zostanú holdouty; rozhodnutie, či je R-A regulárne uzavretá |

Stav 2026-07-16: formula mapa a left-null sú v dokumente 32. Pokus 4
odhalil PF-064 po raw `15/15`; pokus 5 ju opravil samostatným contract
modulom a prešiel `9/9` plus deväť negatívnych fixtures. B1 je
`PASS_CONTRACT_PREFLIGHT_ONLY`; fyzikálna hĺbka zostáva `60/100`.

Tento jemný progress ukazuje vykonanú prácu, ale sám nezvyšuje fyzikálnu
hĺbku `60/100`. Hĺbka sa zmení až po uzavretí celej fyzikálnej brány.

Ohraničený audit všetkých A2 záloh potvrdil, že K4 je jediná živá koľaj,
ktorá už prešla G5. Výsledok a presné blockery záloh sú v
`Audit/A2_BOUNDED_BREADTH_TO_G5_50_RESULT_2026-07-16.md`.

Povinné jadro obsahuje celočíselnú test-fluid vežu
`delta_f^(0), U_f^(0)` a spätnú odozvu v prvom ráde `Phi z^p`. Premenné
`delta_f^(1), U_f^(1)` sa nesmú mechanicky pridať do každej frakčnej vrstvy;
ich potrebu musí ukázať rádová bilancia. `U_c` zostáva dynamické.

**PASS B1:** presná Bianchi identita, úplná parita stavov a rovníc, regulárne
limity `gamma -> 0`, `A_f -> 0` a background bez perturbatívneho `k`.  
**REVIEW B1:** chýbajúca rovnica, rád, gauge mapa alebo neuniformná expanzia.  
**Kandidát na STOP:** invariantný nenulový Bianchi zvyšok až po úplnom
rádovom uzávere.

Ak R-A dá invariantný rozpor alebo preukázanú neuniformnosť, povoľuje sa
jediná nezávislá formulácia **R-B**: plný species systém v `A_f` a Frobeniov
rad iba v `z`. Rovnaký invariantný rozpor v R-A aj R-B môže viesť k
autoritatívnemu STOP K4. Rozdiel medzi nimi nesmie vytvoriť K4-K8, K4-K9 ani
ďalší suffix; je to interná architektonická kontrola P5.3.

### K4-B2 — jeden ohraničený úplný seedový runner

Runner vznikne iba po PASS B1 a samostatnej Markdown predregistrácii. Nie je
to `RERUN3`; číslo `262` zostáva rezervované pre P5.4.

Musí v jednom balíku preveriť:

- presnú paritu s coefficient/row manifestom;
- päť módov `AD/CDI/BI/NID/NIV` a tri dynamické Fourierove módy;
- dynamické `U_c` a jednoznačnú gauge mapu;
- trace a traceless ako zmrazené určujúce Einsteinove rows, nezávislé `00`
  a `0i` seedové holdouty a fail-closed coefficient-wise total-energy,
  total-momentum/Bianchi krížový guard z B1;
- M1 anchor s netautologickým callable/hash guardom;
- `gamma -> 0`, `A_f -> 0`, backgroundovú k-nezávislosť a rozmerový test;
- truncation `J` verzus `J+2` a plochy zvolené podľa skutočného `z << 1`.

Prevádzka: vnútorný limit najviac 5 s; každý compile/help/smoke/run oddelene
s vonkajším limitom najviac 10 s; immutable výsledok. Technické zlyhanie sa
zapíše, opraví v rovnakom fyzickom suffixe a nespotrebuje fyzikálny pokus.
Nový nasledovník fyzickej koľaje vznikne iba pri zmene rovníc, mechanizmu
alebo rozsahu, nie pri oprave implementácie.

### K4-B3 až B5 — cesta k rozhodnutiu A2

1. **B3 / P5.4:** krátka species-first evolúcia — dynamické constrainty,
   linearita, dva skutočné štarty, kroková konvergencia, nulový limit a
   stabilita;
2. **B4 / G8:** plná fotónová, neutrínová a parná hierarchia, recombination
   a TCA prechod, časová aj `lmax` konvergencia;
3. **B5 / G9:** CMB/S8 likelihood na už zmrazenej fyzike; dáta nesmú
   zachraňovať porušenú konzerváciu alebo neúplnú hierarchiu.

K4 môže prejsť lineárnou stanicou A2 až po B3 a B4. B5 následne rozhoduje
jej observačnú životaschopnosť pred ďalšou stanicou.

## 3. Rozhodovací strom pri stene K4

```text
R-A rádový/species/Bianchi ledger
|-- uzavretý -> jeden úplný seedový runner -> P5.4 -> G8 -> G9
`-- invariantný rozpor alebo neuniformnosť -> jediná kontrola R-B
    |-- rozpor zmizne -> pokračovať R-B; R-A označiť ako neuniformnú
    `-- rovnaký invariantný rozpor -> kandidát na STOP A2-K4
        `-- krátky analytický A2-K8 no-go ledger
            |-- samotný zdroj počtu uzavrie energiu aj hybnosť -> preveriť K8
            `-- chýba momentum/pressure/noise moment -> otvoriť A2-K9
```

Pri A2-K9 má prvá nová koľaj používať jeden lokálny production/collision
kernel: jeho nultý moment dá produkciu popola a pary, prvý prenos hybnosti a
druhý tlak, disperziu alebo šum. Tým sa odstráni konkrétna možná príčina
smrti K4; nejde o ďalšie premenovanie algebraického energy-frame.

## 4. Dokumentačný poriadok bez brzdenia fyziky

- Do fyzického presunu súborov sa nepúšťať pred WB-1 baseline.
- Starých `114` dokumentov rodiny `05` a `11` kolíznych ID sa nemaže ani
  neprepisuje. Najprv hash mapa, aliasy, supersession a SK/EN parita.
- Nové pracovné pravidlá/otázky patria do relevantnej hĺbky `tracks`, nie do
  `theory`.
- Nefunkčný skript sa označí v karanténe a presunie do history až po
  zachovaní dôvodu, vstupu a výsledku.
- Upratovanie sa robí pri uzavretí brány alebo commitu, nie po každom malom
  medzivýpočte.
- Staré navigačné dokumenty zostanú historické, ale dostanú hore odkaz na
  tento aktuálny plán.

## 5. Čo sa teraz nesmie robiť

- nespustiť legacy RERUN3, P5.4, G8 ani G9; ARCH-A balíky 4–10 sú uzavreté
  a ďalší proces musí patriť S1/mode-coverage kontraktu 51;
- nezvyšovať fyzikálnu hĺbku za textový alebo technický medzikrok;
- nezaložiť ďalší K4 suffix len kvôli tolerancii, škálovaniu alebo názvu
  runnera;
- nestageovať celý pracovný strom a necommitovať na `main`;
- nepresúvať historické `05`, `theory/theory`, mŕtve skripty ani externé
  zdroje pred baseline a link auditom;
- nepublikovať Zenodo a nevytvárať náhradné predikčné číslo bez PT2;
- nevytvárať nové globálne AR/Q ID, kým sa neuzavrie kolízna mapa.

## 6. Najbližšia konkrétna práca

1. kontrakt S1/doc51 a `.05/nominal` support sú scoped PASS; KMPC-063/066
   uzavreli AD, KMPC-073/075 CDI a KMPC-078 BI/.005, takže C2 je `5/10 PASS`;
   KMPC-083/086/087 vylúčili solve-roundoff a poslednú holdout/driver
   assembly, KMPC-092 lokalizoval dominantný M1×background blok a
   KMPC-099/100 potvrdili plný projected M1 rank `98/98`; ďalší krok je
   jediný rank-revealing HP audit tej istej natívnej M1 matice bez zmeny
   prahov alebo pridania holdoutu do fitovanej matice;
2. v K11 predregistrovať full thermal/TCA/DAE historický balík číslo 6 na
   už prejdenom source-AST contracte; active counter je `0/10` a fyzikálny
   `lmax`/closure sweep je až ďalšia brána;
3. po seed výsledku rozhodnúť: R-A pokračuje do P5.4, potrebuje jedinú R-B
   kontrolu, alebo vznikol invariantný kandidát na STOP K4;
4. WB/PT1 dokumentačné práce udržať, ale nesmú blokovať uvedené fyzikálne
   rozhodnutie.

Tento sled je zámerne konečný: do najbližšieho fyzikálneho rozhodnutia povoľuje
najviac dva analytické fyzikálne varianty a potom jeden stabilný seedový
runner. Jeho technické incidenty sa opravujú a evidujú bez spotrebovania
fyzikálneho pokusu. `TECHNICAL_STOP` vznikne až po 10 po sebe idúcich
technických zlyhaniach jednej implementačnej línie; každý úspešný vecný
výpočet aktívny counter vynuluje, no úplná história sa zachová. Nový fyzický
suffix vznikne iba pri zmene fyziky.

## 7. Mapa samostatných úloh a agentov

Projekt sa nebude deliť na samostatný chat pre každý suffix. Odporúčané
hranice hlavných úloh sú:

| Úloha | Rozsah | Kedy ju otvoriť |
|---|---|---|
| `ORCH-v3.18` | autoritatívne registre, verdikty, handoffy, Git/release | stále; toto je hlavný orchestrátor |
| `A2-K4-P5.3-SEEDS` | CDI/BI/NID/NIV, `k×variant` seed coverage; S-M osobitne | teraz; S-C0 lower-moment passport uzavretý bez skóre |
| `A2-K4-P5.4-EVOLUTION` | krátka species-first ODE/DAE evolúcia | až po uzavretí P5.3 |
| `A2-K4-G8-BOLTZMANN` | finite opacity, recombination, plné hierarchie a convergence | až po P5.4 |
| `A2-BACKUP-TRACKS` | ohraničené K7/K8/K9/K11/K12 blocker/no-go audity | iba keď sa aktívne obnoví konkrétna záloha |
| `DOC-GIT-RELEASE` | manifesty, odkazy, SK/EN parita, release triggers | priebežne ako podporná read-only úloha |

Každý handoff musí smerovať na jeden route-local work plan a obsahovať
aktuálny stav, rovnice/vstupy, hashes, mantinely, otvorené blockery a
`done-when`. Módy, `k`, nulové varianty, support páry a technické opravy
zostávajú v tej istej úlohe, ak nemenia fyziku.

Hlavný reasoning agent zostáva fyzikálnym auditorom a jedinou autoritou pre
PASS/REVIEW/STOP. Rýchlejší/lacnejší agent je vhodný pre hash manifesty,
kontrolu odkazov a názvov, mechanické SK/EN porovnanie, JSON/log triage a
preflight zo známeho checklistu. Ani taký agent nesmie meniť vzorce alebo
udeliť verdikt. Počet súbežných agentov sa drží malý: jeden hlavný a najviac
tri špecializované read-only roly, pokiaľ nezávislá práca naozaj beží
paralelne.

Projektové konfigurácie sú v `.codex/agents/`. Fyzikálny a matematický
auditor používajú náročnejší profil; dokumentačný steward je pripnutý na
rýchlejší profil pre mechanické read-only kontroly. Konkrétny model nikdy
nemení rozsah autority: všetky tri roly iba odporúčajú a hlavný agent zapisuje
výsledný stav.
