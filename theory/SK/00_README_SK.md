# 00 — Kvantová bunková teória priestoru: sprievodca k verzii 3.18

**Autor:** Martin Jámbor<br>
**Oficiálny názov teórie:** Kvantová bunková teória priestoru (`KBTP`)<br>
**Jazyková autorita:** slovenské súbory<br>
**Obsahový cutoff:** 9. august 2026<br>
**Plánované publikačné okno:** 11.–13. august 2026<br>
**DOI vydania:** [`10.5281/zenodo.21915608`](https://doi.org/10.5281/zenodo.21915608)<br>
**Stav teórie:** pracovná fyzikálna hypotéza s auditovanými čiastkovými
výsledkami; zatiaľ nie je experimentálne potvrdená

## Samostatnosť a rozsah vydania

Táto sada dokumentov je samostatným výkladom verzie 3.18. Na jej pochopenie
nie je potrebná verzia 3.17. Slovo „úplný“ tu znamená úplný dokumentačný
snapshot: sada obsahuje pracovnú ontológiu, fyzikálny mechanizmus, rovnice,
výsledky, predikčné skupiny, otvorené otázky aj hranice tvrdení. Neznamená,
že teória je dokončená alebo experimentálne potvrdená.

## Poradie čítania

1. [`01_Bunkovy_Vesmir_SK.md`](01_Bunkovy_Vesmir_SK.md) — úplný
   súvislý výklad teórie: problém, fyzikálna predstava, rovnice, výsledky,
   predikcie, falzifikácia a otvorené otázky.
2. [`02_Prediction_Status_Table_SK.csv`](02_Prediction_Status_Table_SK.csv)
   — strojovo čitateľný register P01–P11 s tvrdením verzie 3.18, cieľom
   prežitia, dosahom vylúčenia, významom zhody, dôkazom a povinným nonclaimom.
3. [`03_Methodology_and_Question_Register_SK.md`](03_Methodology_and_Question_Register_SK.md)
   — pravidlá auditu, logika živých a mŕtvych koľají, neznáme funkcie a
   úplný register otázok Q1–Q34.
4. [`04_Theory_Existence_Conditions_Register_SK.csv`](04_Theory_Existence_Conditions_Register_SK.csv)
   — strojovo čitateľný register EC01–EC43: exaktné zákony, otvorené
   mantinely, mechanistické a kalibračné hodnoty, väzby na P01–P11, dosah
   smrti a čísla, ktoré sa nesmú použiť ako fyzikálny STOP.

## Obsahová mapa dokumentov

### Dokument 01 — súvislý fyzikálny výklad

[`01_Bunkovy_Vesmir_SK.md`](01_Bunkovy_Vesmir_SK.md) je hlavný
čitateľský dokument. Jeho časti majú tento účel:

1. **Otázka teórie — môže jeden lokálny proces spájať viac javov?** — teória
   skúma, či spracovanie energie a delenie buniek priestoru môže byť spoločným
   fyzikálnym pôvodom zrýchlenej expanzie, vzniku hmoty, tmavej zložky
   popola, reliktných vĺn pary, jaziev a šípu času. Zároveň porovnáva svoj
   obraz vlnenia svetla a spoločného limitného $c$ s mainstreamovou fyzikou
   a ukazuje úlohu hlavnej premostovacej rovnice s $\delta$.
2. **Navrhovaný mechanizmus — čo sa môže diať pri delení bunky?** — energia
   vákua vystupuje ako palivo lokálnej udalosti, ktorá mení sieť a môže
   vytvárať hmotu, popol, paru a jazvu paralelne alebo v kauzálnom reťazci.
   Kapitola oddeľuje už odvodené a testované míľniky od poradia produktov,
   ktoré ešte musí rozhodnúť matematika a pozorovania.
3. **Triedy tvrdení** — presný rozdiel medzi `DERIVED`, `CONDITIONAL`,
   `HYPOTHESIS`, `OPEN`, `WITHDRAWN` a `STOP_SCOPE`.
4. **Od siete k fyzike** — Poissonova–Delaunayova geometria, réžia delenia,
   kapacita `C=28`, front signálu, disperzia, limitné $c$, vnútorná kapacita
   a Newtonov grafový comparator.
5. **Homogénne kozmologické pozadie** — energetický ledger, rodina $\lambda$,
   univerzálny background bez závislosti od Fourierovho módu, účtovný tieň
   a para.
6. **Lineárne poruchy a observables** — požiadavky na úplný A2 systém,
   ohraničené ciele a podmienené diagnostické body $S_8/H_0$, CMB kotva,
   skalárne spektrum a tenzorový sektor.
7. **Odpovede ľudskou rečou** — priestor, expanzia, palivo, hmota, popol,
   para, $H_0$, $S_8$, svetelný kužeľ, gravitácia, meranie a šíp času.
8. **Predikcie** — čitateľský súhrn P01–P11 a ich dnešné záväzky.
9. **Stanice a koľaje** — význam A/K označení, prijaté míľniky, živé a mŕtve
   koľaje, dôvody STOP, hĺbka `60/100`, blocker A2-K4 a úlohy do A3.
10. **Otvorené fundamentálne otázky** — fyzika, ktorú verzia 3.18 ešte
    neuzavrela.
11. **Priznania a nonclaims** — čo nemožno z výsledkov vyvodiť.
12. **Falzifikácia a ďalší postup** — čo by mechanizmus alebo teóriu
    obmedzilo či vyvrátilo a aké brány nasledujú.
13. **Citačná hranica** — čo možno citovať ako current výsledok.
14. **Register skratiek** — fyzikálne symboly, observables, jednotky,
    stanice, koľaje, brány a auditné kódy.

### Dokument 02 — presný register každej predikcie

[`02_Prediction_Status_Table_SK.csv`](02_Prediction_Status_Table_SK.csv)
je strojovo čitateľný register záväzného znenia predikcií pre verziu 3.18.
Každý riadok obsahuje
tvrdenie a cieľ prežitia verzie 3.18, dosah prípadného vylúčenia, význam
zhody, dôkazovú stopu a povinný nonclaim. Na pochopenie žiadneho riadku nie
je potrebná staršia verzia:

- `P01` — $N_{\rm eff}$ a $\Delta N_{\rm eff}$;
- `P02` — skalárny spektrálny index $n_s$;
- `P03` — pomer tenzorov ku skalárom $r$;
- `P04` — Hubbleova konštanta $H_0$;
- `P05` — zhlukovací parameter $S_8$;
- `P06` — parametre tmavej energie $w_0,w_a$;
- `P07` — priama detekcia tmavej hmoty/popola;
- `P08` — odvolaný presný vzťah $n_s-w$, ktorý v3.18 nemá cieľ prežitia;
- `P09` — možný časový drift $\delta$;
- `P10` — Lorentzova invariancia a disperzia;
- `P11` — termálne parné/vlnové pozadie; identifikácia reliktu s gravitónmi
  nie je odvodená.

CSV je správne miesto na otázku „čo dnes smieme tvrdiť o konkrétnej
predikcii?“. Fyzikálny výklad jej pôvodu patrí do dokumentu 01 a pravidlá
hodnotenia do dokumentu 03.

### Dokument 03 — pravidlá auditu a register otázok

[`03_Methodology_and_Question_Register_SK.md`](03_Methodology_and_Question_Register_SK.md)
určuje, ako sa výsledky smú vytvárať a interpretovať:

0. účel, autoritu a samostatnosť registra;
1. kotvu teórie a pracovný protokol;
2. vznik, identitu, vetvenie a archiváciu koľají;
3. povinné verifikačné pravidlá P1–P5, známe pasce M1–M9 a lineage audit;
4. dôkazové triedy, fyzikálne mantinely, neznáme funkcie a test
   neprázdnosti ich prípustnej množiny;
5. výpočtový, auditný a release workflow;
6. historický cintorín a dnešné mŕtve presne vymedzené formulácie s dôvodmi smrti;
7. úplný register otázok Q1–Q34;
8. ledger starších formulácií, ktoré neskorší audit obmedzil;
9. živé nenájdené funkcie a presné návratové body;
10. povinné release nonclaims.

### Dokument 04 — všetky podmienky existencie a ich dosah

[`04_Theory_Existence_Conditions_Register_SK.csv`](04_Theory_Existence_Conditions_Register_SK.csv)
je spoločný strojovo čitateľný index EC01–EC43. Odpovedá na otázku „akú
hodnotu, rozsah alebo exaktnú vlastnosť musí mať daná formulácia a čo presne
zomrie, ak ju nesplní?“. Oddeľuje:

- fundamentálne exaktné podmienky bez voľnej tolerancie;
- merateľné targets, ktorých tolerancia patrí datasetu a likelihood;
- otvorené podmienky bez povoleného číselného kill okna;
- mechanistické a kalibračné hodnoty bez automatického theory-level dosahu;
- procesné a numerické čísla, ktoré nikdy samy nevytvárajú fyzikálny STOP.

Dokument `04` neprepisuje autoritatívne predikčné riadky v `02`; pri EC
riadku prepojenom s P01–P11 treba čítať oba záznamy.

## Rýchle trasy čítania

| Cieľ čitateľa alebo AI | Odporúčaná trasa |
|---|---|
| prvé pochopenie teórie | dokument 01: §§1–2, potom §7, §9 a §11 |
| kontrola rovníc a symbolov | dokument 01: §§4–6 a register §14 |
| overenie jednej predikcie | dokument 01: §8, potom príslušný riadok P01–P11 v dokumente 02 vrátane jeho povinného riadkového nonclaimu a napokon globálne release nonclaims v dokumente 03 §10 |
| kontrola všetkých nutných hodnôt a mantinelov | príslušný riadok EC01–EC43 v dokumente 04; jeho zdroj v dokumente 01 alebo 03; pri väzbe na P01–P11 aj dokument 02 |
| kontrola progresu A1–A3 | dokument 01: §9; metodické pravidlá koľají v dokumente 03 §§2–3 |
| zistenie, prečo koľaj zomrela | dokument 01: §9.3; dokument 03: §§6 a 8 |
| hľadanie otvorenej funkcie alebo mantinelov | dokument 03: §§4 a 9; fyzikálny kontext v dokumente 01 §§5–6 a 10 |
| audit výpočtu alebo tvrdenia | dokument 03: §§1–5, potom dôkazová cesta uvedená pri výsledku v dokumente 01 alebo 02 |
| príprava citácie predikcie | dokument 01: §13, príslušné povolené tvrdenie aj povinný riadkový nonclaim v dokumente 02 a použiteľné globálne nonclaims v dokumente 03 §10 |
| citovanie stavu koľaje | dokument 01: §§9 a 9.3; metodika a historické obmedzenia v dokumente 03 §§2–3, 6 a 8; dokument 02 sa na koľaje nepoužíva |

> #### Technický návod čítania pre AI a audítorov
>
> *Táto poznámka slúži na správne strojové čítanie identifikátorov a hraníc
> tvrdení vydania.*
>
> - **Predikcia `P01–P11`:** prečítaj jej význam v dokumente 01 §8, presné
>   povolené tvrdenie a riadkový nonclaim v dokumente 02, globálne
>   obmedzenia v dokumente 03 §10 a súvisiace podmienky `EC` v dokumente 04.
> - **Koľaj `A…-K…`:** stav čítaj v dokumente 01 §§9 a 9.3 a pravidlá
>   koľají v dokumente 03. Dokument 02 neobsahuje riadky koľají.
> - **Jazyková autorita:** pri významovom rozdiele medzi prekladmi rozhoduje
>   slovenské vydanie.
> - **Hranica vydania:** pracovný adresár `tracks/` je auditná a vývojová
>   stopa. Nesmie nahradiť vydanie v3.18 ani rozšíriť jeho tvrdenia.

## Ako čítať tvrdenia

**Presne vymedzený rozsah** (v auditných kódoch aj `scope`) je konkrétna
kombinácia rovníc, predpokladov, vstupov, fyzikálneho režimu a testovaného
javu, na ktorú výsledok skutočne platí. Výsledok z takého rozsahu sa nesmie
automaticky preniesť na inú formuláciu ani na celú teóriu.

- `DERIVED` znamená odvodenie iba v presne uvedenom matematickom rozsahu.
- `CONDITIONAL` znamená výsledok závislý od uvedených vstupov alebo kotvy.
- `HYPOTHESIS` a `OPEN` nie sú potvrdením ani predikciou.
- `WITHDRAWN` zachováva staré tvrdenie v histórii, ale zakazuje jeho dnešné
  používanie.
- `STOP_SCOPE` zabíja presne testovaný mechanizmus, nie automaticky celú
  teóriu.

**Cieľ prežitia** je vopred zapísaná číselná alebo exaktná podmienka, ktorú
musí splniť presne označená formulácia. Zhoda ju iba ponechá živú; nepotvrdí
bunkový mechanizmus. Spoľahlivé vylúčenie zabije rozsah uvedený v danom
riadku. Celú teóriu môže zabiť až cieľ označený `THEORY_LEVEL` alebo dôkaz,
že všetky deklarované vrcholové alternatívy sú úplné a vylúčené. Dáta použité
na zostrojenie alebo normalizáciu cieľa sú kalibračné dáta a nesmú sa druhý
raz vykázať ako nezávislé potvrdenie.
Žiadny riadok P01–P11 vo v3.18 zatiaľ nemá certifikovaný dosah
`THEORY_LEVEL`. Pri každom riadku s aktívnym cieľom prežitia však musí
robustne nekompatibilný výsledok po úplnom požadovanom observable teste,
vrátane neistôt, covariance a systematík, vyvolať zapísaný STOP pomenovaného
rozsahu alebo, rozhodnutím Martina Jambora, fyzikálne odlišnú novú koľaj; cieľ
sa po výsledku nesmie potichu posunúť.

## Ako čítať mapu overovania

Teória sa preveruje ako cesta cez **kontrolné stanice**. Na každej stanici
možno skúšať viac **koľají** — fyzikálne odlišných spôsobov, ako splniť jej
požiadavky.

- **A1 — homogénne pozadie:** kontroluje expanziu vesmíru a základný účet
  energie medzi jeho zložkami bez priestorových porúch.
- **A2 — lineárne poruchy:** kontroluje, či možno pozadie rozšíriť na úplnú,
  konzervačnú, kauzálnu a stabilnú dynamiku malých porúch.
- **A3 — pozorovateľný vesmír:** vyžaduje implementáciu úplného systému v
  Einsteinovom–Boltzmannovom výpočte, napríklad v CLASS alebo CAMB, a jeho
  porovnanie s CMB, rastom štruktúr a ďalšími meraniami.
- **K — koľaj:** označuje konkrétny skúšaný mechanizmus na danej stanici.

### Čo znamenajú brány G1–G10

Brány určujú rovnakú postupnosť kontrol pre každú koľaj. Číslo pri bráne je
kanonická hĺbka, ktorú koľaj dosiahne až po prejdení tejto brány aj všetkých
predchádzajúcich brán alebo ich výslovne dokázaného ekvivalentu.

Slová **úplný** a **PASS** sa pri každej bráne vzťahujú iba na vopred
zmrazenú formuláciu, stavový priestor a fyzikálny režim uvedené v jej
kontrolnom pase. Rozšírenie stupňov voľnosti alebo fyzikálneho režimu znovu
otvára všetky dotknuté nasledujúce brány, ak prenos výsledku nezaručí
samostatný dôkaz ekvivalencie.

| Brána | Hĺbka | Čo musí koľaj preukázať |
|---|---:|---|
| `G1` | `10/100` | Je zapísaná fyzikálne odlišná hypotéza, jej mechanizmus, stupne voľnosti, parametre a rozdiel od ostatných koľají. |
| `G2` | `20/100` | Homogénne pozadie a úplný účet energie a hybnosti sú uzavreté, kladné a majú správny nulový limit. |
| `G3` | `30/100` | Existuje lokálna akcia alebo rovnocenný úplný kovariantný uzáver bez chýbajúceho operátora, zdroja alebo prenosového rámca. |
| `G4` | `40/100` | Sú odvodené úplné lineárne rovnice všetkých zložiek, perturbovaný prenos $\delta Q_A$, Einsteinove constrainty, Bianchiho identity, gauge mapa, znamienka a nulový limit. |
| `G5` | `50/100` | Existuje úplná regulárna superhorizontová báza všetkých fyzických módov s constraintmi a klasifikáciou počiatočných módov. |
| `G6` | `60/100` | V zmrazenom rozsahu prejde celá regulárna báza použiteľnými testmi efektívnych kinetických a gradientových znamienok, charakteristickej kauzality, fyzikálnych menovateľov, high-$k$/subhorizontovej stability, stiffness a konvergencie. Efektívny fluidný PASS sám nie je mikroskopickou UV no-ghost vetou ani dôkazom globálnej hyperbolicity. |
| `G7` | `70/100` | Vlastná úplná Einsteinova–Boltzmannova implementácia obsahuje fotóny, neutrína, anizotropný stres, tight coupling, rekombináciu, fyzické transfery, conservation/constraint/null testy a nezávislú implementáciu alebo gauge cross-check. |
| `G8` | `80/100` | Z úplného systému vzniknú CMB-normalizované spektrá a rastové veličiny $\sigma_8$ a $S_8$, nie iba ľubovoľne normalizovaný efektívny mód. |
| `G9` | `90/100` | Spoločná analýza CMB, BAO, lensingu a ďalších vopred určených dát zahŕňa likelihoody a covariance, priory, nuisance parametre, počet voľností, systematiky, holdout, robustnosť a vopred určené prahy vylúčenia. |
| `G10` | `100/100` | Prešli všetky brány danej verzie a povinné ďalšie predikcie; manifest, hashe, changelog, priznanie otvorených brán a úplná reprodukčná stopa umožnili nezávislé zopakovanie. |

Stanica A3 nie je druhá kópia brány G7. Najprv musí G7 uzavrieť úplný
Einsteinov–Boltzmannov most a fyzické transfery. Až potom A3 pokračuje cez G8
k CMB-normalizovaným spektrám a rastu a cez G9 k spoločnému porovnaniu s
dátami. Jedna práca sa preto nesmie započítať v dvoch bránach.

Neskorší nutný no-go test môže koľaj fyzikálne zastaviť aj vtedy, keď
niektoré medzibrány neboli vykonané. Taký test sa zachová ako **brána
smrti**, ale nezvýši kanonickú hĺbku koľaje za preskočené brány.

### Kde sa teória nachádza

Aktívna cesta je

```text
A1-K1 -> A2-K4 -> A3
```

Koľaj `A1-K1` prešla iba kontrolou homogénneho pozadia. Na stanici A2 sa
najďalej dostala koľaj `A2-K4`:

1. brána `G5` prijala regulárnu superhorizontovú bázu a stanovila hĺbku
   `50/100`;
2. brána `G6` prešla v zmrazenom deväťpremennom efektívnom fluidnom systéme
   s perfektnou radiáciou: preverila všetky tri regulárne módy, efektívne
   kinetické a gradientové znamienka, kauzálne charakteristické rýchlosti,
   nulový limit, constraint, subhorizontové body $q=30,300,1000$ a numerickú
   konvergenciu. Tým zvýšila hĺbku na `60/100`, ale nepreukázala
   mikroskopickú no-ghost vetu ani globálnu stabilitu.

Číslo `60/100` je teda **súčet váh prejdených fyzikálnych brán**. Nie je to
60 % pravdepodobnosť pravdivosti teórie, 60 % dokončenej práce ani
štatistický výsledok. Stanica A2 ešte nie je dokončená. Stále chýba najmä
úplný spoločný lokálny zákon produkcie a prenosu, dynamické zachovanie
constraintov, úplná fotónová a neutrínová hierarchia a následná brána A3.

### Čo znamená stav koľaje

- **`LIVE_ACTIVE`:** koľaj práve prechádza ďalšími kontrolami.
- **`LIVE_BACKUP / WAITING`:** pomenovaná alternatíva ešte nebola úplne
  sformulovaná alebo overená. Kladným dôkazom sa stane až po predložení
  úplných rovníc, podmienok testu a explicitného prípustného riešenia alebo
  dôkazu jeho existencie.
- **`STOP_SCOPE`:** konkrétna testovaná formulácia narazila na fyzikálny
  rozpor. Dôvod zostáva zaznamenaný, ale výsledok automaticky nezabíja inú
  koľaj ani celú teóriu.

Kým nemáme úplnú živú koľaj ani dôkaz, že všetky prípustné koľaje sú
nemožné, celkový stav zostáva **neuzavretý**
(`GLOBAL_FEASIBILITY_INCOMPLETE`). Čakajúca záložná koľaj nie je dôkazom, že
riešenie existuje; znamená iba to, že daná možnosť ešte nebola rozhodnutá.

### Kde overiť podrobnosti

- dokument `01` §9 vysvetľuje prijaté míľniky, rovnice, živé a mŕtve
  koľaje, dôvody STOP, súčasnú prekážku A2-K4 a úlohy potrebné pred A3;
- dokument `02` uvádza presné aktuálne tvrdenia a hranice predikcií;
- dokument `03` obsahuje pravidlá overovania, históriu obmedzených
  formulácií a register otvorených otázok;
- dokument `04` uvádza všetky podmienky existencie a presne hovorí, akú
  časť modelu môže nesplnenie každej podmienky vylúčiť.

Tieto štyri dokumenty tvoria samostatný stav vydania v3.18. Na jeho
pochopenie ani citovanie nie sú potrebné pracovné súbory. Odkazy na GitHub
sú iba doplnkovou auditnou stopou na kontrolu výpočtov a pôvodu výsledkov.
Význam identifikátorov podrobnejšie vysvetľuje dokument `01` §9.1 a jeho
záverečný register skratiek.
