# KVANTOVÁ BUNKOVÁ TEÓRIA PRIESTORU (KBTP)

## Bunkový vesmír: fyzikálny program, rovnice, predikcie a testy — verzia 3.18

**Autor teórie:** Martin Jámbor<br>
**Verzia:** 3.18<br>
**Obsahový cutoff:** 9. august 2026<br>
**Plánované publikačné okno:** 11.–13. august 2026<br>
**DOI vydania:** [`10.5281/zenodo.21915608`](https://doi.org/10.5281/zenodo.21915608)<br>
**Trieda vydania:** `R3.18-CONSOLIDATED / COMPLETE_SELF_CONTAINED_SNAPSHOT`<br>
**Jazyková autorita:** slovenská verzia<br>

---

## 1. Otázka, ktorú teória kladie

Všeobecná relativita opisuje časopriestor ako spojitú geometriu a presne
určuje, ako hmota ovplyvňuje jeho metriku. Kvantová teória polí opisuje
častice a ich interakcie. Štandardný kozmologický model opisuje kozmickú
expanziu, reliktné žiarenie a rast štruktúr pomocou všeobecnej relativity,
studenej tmavej hmoty a kozmologickej konštanty. Zahŕňa teda aj pozorované
zrýchlené rozpínanie neskorého vesmíru. Tieto teórie sú experimentálne
úspešné vo svojich overených oblastiach. Kvantová bunková teória priestoru
ich preto nesmie obísť ani nahradiť obrazným jazykom. Kladie hlbšiu otázku:

> **Môže byť pozorovaná fyzika efektívnou povrchovou stopou lokálnej,
> diskrétnej a nerovnovážnej dynamiky priestoru?**

### 1.1 Ústredný pracovný most teórie

Kvantová bunková teória priestoru ešte nemá odvodenú jedinú mikroskopickú
„rovnicu všetkého“. Jej ústredným dnes používaným mostom medzi geometriou
siete a kozmologickým opisom je efektívna réžia prestavby

$$
\boxed{
\delta=\frac{1}{\langle k\rangle+C}
}
\tag{1}
$$

a jej podmienené číselné vyhodnotenie

$$
\langle k\rangle=\frac{48\pi^2}{35}+2\simeq15.535,
\qquad
C=28,
\qquad
\boxed{\delta\simeq0.02297}.
\tag{2}
$$

**Význam symbolov:**

- $\delta$ je bezrozmerná efektívna cena alebo disipačná réžia jednej
  prestavby;
- $\langle k\rangle$ je stredný počet povrchových susedov v referenčnej
  trojrozmernej Poissonovej–Delaunayovej sieti;
- $C$ je pracovná vnútorná kapacita bunky; hodnota `28` sa číta ako počet
  bozónových stavov v obnovenej fáze Štandardného modelu.

**Vzťah k mainstreamu:** rovnica (1) nie je súčasťou všeobecnej relativity,
Štandardného modelu ani ΛCDM. Mainstream môže zadať kozmologickú
konštantu alebo stavovú rovnicu tmavej energie, ale neodvodzuje parameter
$\delta$ z konektivity diskrétneho priestoru. KBTP sa odlišuje práve pokusom
prepojiť geometriu siete s efektívnym tlakom paliva,

$$
p_f=(-1+\delta)\rho_f,
\qquad
w_f\equiv\frac{p_f}{\rho_f}=-1+\delta.
\tag{3}
$$

Tu $\rho_f$ a $p_f$ označujú hustotu a tlak paliva a $w_f$ jeho parameter
stavovej rovnice. Rovnica (3) má rovnaký fluidný tvar, aký používa moderná
kozmológia; odlišný je navrhovaný mikroskopický pôvod $w_f+1=\delta$.

**Status:** geometrický výraz pre $\langle k\rangle$ a jeho sieťové
simulácie majú obmedzenú matematickú podporu. Identifikácia $C=28$ a krok od
jednej prestavby k rovnici (3) sú `CONDITIONAL_MECHANISM_READING`, nie
dokázaná mikrodynamická veta. Preto je číselná hodnota $\delta=0.02297$
pracovným vstupom živej koľaje, nie experimentálne potvrdenou konštantou
prírody.

Priamy zapečatený externý balík, ktorý by overoval mikroskopický most
(1) ako fyzikálny zákon, zatiaľ neexistuje. Balík uvedený pri rovniciach
(20)–(22) kontroluje až jeho podmienené použitie v normalizácii skorého
backgroundu; nedokazuje pôvod $C$ ani $\delta$.

### 1.2 V čom KBTP používa rovnakú fyziku ako mainstream

KBTP nemá uspieť tým, že nahradí overené zákony novými názvami. V oblastiach,
kde sú GR, QFT, termodynamika a kozmologické dáta overené, musí prejsť
rovnakými rovnicami a limitmi.

| Oblasť | Rovnaký základ ako mainstream | Čo musí KBTP navyše preukázať |
|---|---|---|
| kozmologické pozadie | FLRW geometria, Friedmannova rovnica a celkové zachovanie energie | odvodiť zdrojové členy z lokálneho bunkového zákona bez skrytého rezervoára |
| poruchy | Einsteinove constrainty, rovnice kontinuity, Eulerove rovnice a Boltzmannova hierarchia | odvodiť celý operátor popola, paliva a pary z jedného mechanizmu |
| svetlo a gravitácia | jeden lokálny svetelný kužeľ, Lorentzova invariancia, ekvivalenčný princíp | ukázať, ako tieto symetrie vzniknú z diskrétnej siete bez lineárnej disperzie a birefringencie |
| časticová fyzika | pozorovaný obsah častíc a kalibračné symetrie Štandardného modelu ako mantinely | vysvetliť, prečo a ako sú tieto stupne voľnosti realizované bunkovým substrátom |
| dáta | CMB, BBN, BAO, lensing, rast a lokálne merania s ich chybami a kovarianciami | priniesť najmenej jednu novú predikciu bez dodatočného fitu |

Zhoda s mainstreamovou rovnicou nie je slabina. Je to povinný nulový alebo
kontinuálny limit. Rozdiel má fyzikálny obsah iba vtedy, ak KBTP odvodí
rovnaký úspešný zákon z hlbšieho mechanizmu alebo predpovie merateľnú
odchýlku.

### 1.3 V čom je návrh odlišný

Odlišnosť KBTP je zatiaľ najmä v ontológii a kauzálnej architektúre:

1. priestor nie je základné spojité javisko, ale makroskopický limit siete
   lokálnych buniek;
2. kozmologická expanzia sa skúma ako rast alebo prestavba siete, nie ako
   pohyb buniek do vonkajšieho priestoru;
3. „palivo“, „popol“ a „para“ sú rôzne účtovné výstupy jedného možného
   lokálneho procesu, nie tri ľubovoľne pridané kozmologické tekutiny;
4. svetelný kužeľ, Lorentzova symetria a gravitácia majú byť emergentnými
   vlastnosťami spoločného substrátu;
5. kvantové meranie a šíp času sa skúmajú ako vznik fyzickej jazvy v sieti,
   nie ako osobitná úloha vedomia.

**Jazva** tu nie je iný názov pre popol ani ďalšia kozmologická tekutina.
Je to kandidát na pretrvávajúcu zmenu vnútorného stavu bunky, jej väzieb
alebo lokálnej domény po fyzickej udalosti. Do programu bola zaradená preto,
že ak má KBTP vysvetliť fundamentálnu fyzickú nezvratnosť a nie iba jej
efektívny opis, musí pomenovať stavový nosič, v ktorom zostane história
udalosti. Čisto vratná bunková aktualizácia bez takého deklarovaného nosiča
by túto ambíciu ešte nerealizovala. Presný pôvod jazvy však nie je odvodený:
spúšťačom môže byť prechod, zlyhanie, absorpcia alebo prestavba bunky a zatiaľ
nevieme, či ide o jeden mechanizmus pre pamäť, objektívny kolaps a šíp času.
To sú otvorené otázky `Q4` a `Q8`, nie prijaté výsledky.

Tieto body sú výskumné hypotézy. Samy osebe nepredstavujú dôkaz, že taký
substrát existuje.

### 1.4 Čo môže teória navyše opísať a kam smeruje

Ak by sa program uzavrel, mohol by jedným kauzálnym obrazom vysvetliť nielen
**ako** sa priestor rozpína, svetlo šíri a hmota zhlukuje, ale aj **prečo**
existuje práve takýto spoločný geometrický a energetický ledger. Jeho
teoretická a filozofická ambícia zahŕňa:

- mikroskopický pôvod priestoru, expanzie a neskorého zrýchlenia;
- spoločný pôvod neviditeľnej zhlukujúcej zložky a relativistického reliktu;
- vznik jedného limitného $c$ pre svetlo, hmotu, hodiny a meradlá;
- prechod od konečnej lokálnej kapacity k plošnému zákonu a previazaniu;
- fyzickú, nie vedomím vyvolanú nezvratnosť merania;
- vysvetlenie šípu času ako rastúcej a prepisovanej siete jaziev.

Program smeruje od ontológie k matematike, od matematiky k stabilnej
Einsteinovej–Boltzmannovej dynamike a až potom k dátam. Teória neuspeje tým,
že poskytne príbeh; musí nájsť aspoň jednu úplnú koľaj, ktorá súčasne rešpektuje
konzerváciu, kauzalitu, Lorentzove a ekvivalenčné medze, stabilitu a
pozorovania.

### 1.5 Pracovný fyzikálny mechanizmus

Pracovnou odpoveďou je hypotéza, že priestor má mikroskopické lokálne stupne
voľnosti — bunky — a že makroskopická expanzia môže byť limitným prejavom
ich prestavby alebo delenia. Metastabilná energetická zložka, ktorá túto
prestavbu umožňuje, sa označuje ako **palivo**. Pretože má v pracovnom
kontinuálnom opise tlak blízky vákuu, skúma sa aj ako možný zdroj zápornej
efektívnej tlakovej zložky a tým zrýchleného rozpínania. Zatiaľ ide o
hypotézu na úrovni homogénneho kozmologického pozadia; mikroskopický pôvod
paliva ani úplný observačný fit nie sú odvodené.

Otázka vzniku hmoty sa do programu dostala ako povinnosť každej teórie
priestorového substrátu. Nestačí vysvetliť iba to, prečo sa menia kozmické
vzdialenosti. Teória musí zároveň ukázať, prečo existujú stabilné hmotné
excitácie a kam sa pri prestavbe prenesie energia a hybnosť. Súčasný model
ešte neodvodil častice Štandardného modelu ani pôvod baryónovej hmoty. Skúma
však, či časť hmoty môže byť trvalým alebo dlho žijúcim produktom lokálnej
prestavby siete.

Pracovné názvy **popol** a **para** preto nevznikli ako dve dodatočné látky
pridané iba na zlepšenie zhody s dátami. Označujú dva možné kanály úplného
energetického ledgera:

- **popol** `c` je kandidát na nerelativistický, gravitačne zhlukujúci
  zvyšok prestavby a tým na časť fyzikálnej úlohy pripisovanej tmavej hmote;
- **para** $s$ je kandidát na relativistický alebo voľne sa šíriaci podiel
  odovzdanej energie, ktorý by mohol prispieť k radiačnému či termálnemu
  pozadiu.

Zákon zachovania vyžaduje úplný účet energie a hybnosti, ale sám neurčuje,
že oba tieto kanály musia existovať, aký majú podiel ani v akom poradí
vznikajú. Paralelný vznik, postupný reťazec aj zmiešané vetvenie preto
zostávajú otvorenými fyzikálnymi možnosťami, ktoré má rozlíšiť lokálny
kovariantný zákon a pozorovania.

Takto formulovaný program skúma, či jeden spoločný mechanizmus môže spojiť:

1. vznik makroskopického priestoru, jeho rozpínanie a neskoré zrýchlenie;
2. pôvod stabilnej hmoty a neviditeľnej zhlukujúcej zložky;
3. možný relativistický produkt a jeho stopu v ranom termálnom pozadí;
4. počiatočné poruchy, CMB a následný rast kozmických štruktúr;
5. vlnové šírenie excitácií, emergentný svetelný kužeľ, Lorentzovu limitu
   a gravitačný limit siete;
6. fyzickú nezvratnosť, jazvu udalosti a šíp času.

### 1.6 Svetlo, vlnenie a spoločné limitné `c`

V prípade svetla má návrh dve odlišné úrovne. V auditovanom skalárnom
grafovom operátore možno použiť rovinnú vlnu
$e^{i\mathbf q\cdot\mathbf x}$ ako variačný
skúšobný stav; na náhodnom grafe nejde všeobecne o presný vlastný mód.
Príslušný variačný výraz je párny v $\mathbf q$. Oddelene simulovaný
signálový front
sa rozširuje sublineárne, takže jeho relatívna šírka klesá. To poskytuje
kandidátsky mechanizmus prenosu vlnovej excitácie. Ostrý fyzický svetelný
kužeľ by však nasledoval až po preukázaní, že toto škálovanie pretrvá v
makroskopickom a continuum limite. Teória preto navrhuje čítať vlnovú povahu
svetla ako šírenie excitácie siete. Zatiaľ to nie je odvodenie
elektromagnetického poľa ani dôkaz, že fotón je práve touto sieťovou vlnou.

Zamýšľaná hypotéza pre rovnakú lokálne meranú rýchlosť svetla je, že svetlo,
hmota, hodiny aj meradlá sú excitáciami toho istého substrátu a majú čítať
ten istý limitný kužeľ. Samotný spoločný substrát alebo kapacita tento záver
nedokazujú. Ak by sa pre všetky tieto excitácie odvodila spoločná lokálna
Lorentzovská metrika, jeden limitný kužeľ a boostovo kovariantná dynamika,
transformácie hodín, meradiel a signálov by boli vzájomne konzistentné a
inerciálni pozorovatelia by lokálne merali rovnaké `c`. Ide o podmienený cieľ
hypotézy, nie uzavretý dôkaz: ešte treba odvodiť fotónový sektor, spoločnú
metriku a univerzálnu väzbu všetkých polí, boostovú symetriu, absenciu
neprípustnej birefringencie a ekvivalenčný princíp.

### 1.7 Čo už teória skutočne urobila — krok za krokom

Interné označenia ako `A1-K1` alebo `A2-K4` nie sú fyzikálne veličiny.
Slúžia iba ako stabilné adresy dôkazov. `A` označuje kontrolnú stanicu a `K`
jednu z fyzikálnych možností, ktoré sa na nej preverovali. Pre čitateľa je
dôležitý najprv názov výsledku a až potom jeho interný kód.

Doterajší postup možno bežným jazykom zhrnúť takto:

1. **Navrhol sa geometrický pôvod réžie prestavby.** Zo strednej konektivity
   referenčnej siete a pracovnej kapacity bunky vznikol podmienený kandidát
   $\delta\simeq0.02297$. Je to mechanistický most, nie potvrdená konštanta
   prírody.
2. **Uzavrel sa homogénny energetický účet** (`A1-K1`). Palivo môže v
   homogénnom účte strácať presne toľko energie, koľko získa popol, ktorý sa
   zatiaľ skúma ako nerelativistický zhlukujúci CDM kandidát. Tým prešla
   backgroundová konzervácia $Q_f+Q_c=0$, nie ešte jeho zhlukovanie ani úplná
   lokálna dynamika.
3. **Opravila sa univerzálnosť kozmického pozadia** (`A1-K1`). Zabudnutá
   transformácia amplitúdy odstránila Fourierov mód $k$ z globálnej expanzie:
   $\Phi(k)z^p=A_fa^p$. Vesmír tak nemá iné $H(a)$ pre každú poruchu.
4. **Začali sa testovať lineárne poruchy.** Viaceré konkrétne fluidné,
   barotropické a prenosové možnosti narazili na fyzikálne steny. Zo skorých
   možností sa najďalej dostala štvrtá — spoločný energetický rámec paliva a
   popola — a zostala hlavnou živou koľajou (`A2-K4`). Ďalšie neotvorené
   záložné koľaje sú uvedené v §9.3.
5. **Prešli najväčšie a najmenšie vlnové dĺžky v obmedzenom scope.** Živá
   možnosť dostala regulárnu superhorizontovú bázu (`A2-K4.1`, kontrola
   `G5=50/100`) a high-$k$ principal symbol bez vlastného exponenciálne
   rastúceho K4 módu (`A2-K4.2`, kontrola `G6=60/100`). G6 platí iba v
   zmrazenom deväťpremennom perfect-radiation effective-fluid scope; nie je
   mikroskopickou no-ghost vetou ani dôkazom globálnej stability.
6. **Oddelili sa fyzikálne druhy a statické Einsteinove constrainty.** Model
   eviduje palivo, popol, baryóny, fotóny, neutrína a paru osobitne, zachováva
   anisotropický stress a v statickej rekonštrukcii dáva štyri presné nulové
   Einsteinove rezíduá (`A2-K4.3a`, `P5.1-P5.2`).
7. **Dnešná hranica je existencia spoločného lokálneho zákona** (`P5.3`).
   Evidenčné pokrytie `10/10` a logická matica `45/45` sú hotové, ale ešte
   neexistuje certifikát úplného fyzického quotientu $Q_Z$, zdrojovaná
   actual whole-map $X_Z$ ani dokázane neprázdna úplná rodina prípustných
   máp. Preto sa whole-map jadro zatiaľ nesmie fyzicky klasifikovať ako
   nulové alebo nenulové. Aj po tejto klasifikácii by ostali pevné rezíduum,
   owner/power/reservoir a globálny bridge; registrovaná hĺbka prejdených
   fyzikálnych brán preto zostáva `60/100`.

Rovnaká cesta zapísaná iba ako auditná skratka je

$$
\boxed{
\underbrace{\text{homogénne pozadie}}_{\mathrm{A1-K1}}
\;\longrightarrow\;
\underbrace{\text{lineárne poruchy}}_{\mathrm{A2-K4};\,60/100}
\;\dashrightarrow\;
\underbrace{\text{CMB/LSS implementácia}}_{\mathrm{A3}}
}
\tag{4}
$$

Plná šípka označuje prijatý podmienený prechod z pozadia do živej koľaje
porúch. Prerušovaná šípka znamená, že cesta k implementácii v CLASS/CAMB,
CMB-normalizovaným spektrám a likelihoodu ešte neprešla.

#### Čo sme zistili o vzniku hmoty

**Otázku vzniku hmoty sme riešili, ale vznik obyčajnej hmoty sme ešte
neodvodili.** Doterajšie výsledky problém podstatne zúžili:

- prestavba priestoru nemôže vytvoriť iba expanziu; musí mať úplný účet
  energie a hybnosti;
- homogénny model ukázal konzistentný kanál `palivo -> popol`, v ktorom je
  popol nerelativistickým a gravitačne zhlukujúcim kandidátom na tmavú hmotu;
- baryóny sú v tejto živej koľaji zachovávané, takže dnešný transfer ich
  nevytvára a nie je odvodením baryogenézy ani častíc Štandardného modelu;
- para zostáva možným relativistickým produktom a jazva možným vnútorným
  záznamom udalosti; ani jedno sa nesmie bez operátora stotožniť s hmotou;
- chýbajúci lokálny zákon musí ešte určiť, či produkty vznikajú naraz,
  postupne alebo vetvením, aké stabilné excitácie predstavujú častice a ako
  sa celý účet prenesie do CMB, rastu a lensingu.

Výsledkom teda nie je veta „hmota už vznikla z buniek“, ale presnejšia
fyzikálna úloha: nájsť jeden konzervačný produkčno-transportný operátor,
ktorý vytvorí prípustný zhlukujúci produkt bez porušenia baryónového,
radiačného a Einsteinovho ledgera. To je súčasný most medzi otázkou pôvodu
hmoty a otvoreným blokátorom `P5.3`.

Po dokončení tejto brány ešte nasleduje dynamická evolúcia porúch, plná
fotónová a neutrínová hierarchia a až potom nezávislá implementácia a dáta
(`A3`). Lokálny zdroj pary, reheating a entropický ledger zostávajú ďalšou
otvorenou stanicou (`A4`).

Tento zoznam je výskumný program, nie zoznam potvrdených vysvetlení. Presný
stav číselných tvrdení P01–P11 je v dokumente
[`02_Prediction_Status_Table_SK.csv`](02_Prediction_Status_Table_SK.csv)
a nevyriešené odvodenia Q1–Q34 sú v dokumente
[`03_Methodology_and_Question_Register_SK.md`](03_Methodology_and_Question_Register_SK.md).
Úplný index exaktných podmienok, otvorených mantinelov, benchmarkov a ich
death reach je v
[`04_Theory_Existence_Conditions_Register_SK.csv`](04_Theory_Existence_Conditions_Register_SK.csv).
Fyzikálnym vysvetlením sa návrh môže stať iba vtedy, ak z jedného lokálneho
zákona vyplynú konzervačné rovnice, kauzálna a stabilná evolúcia porúch a
pozorovateľné veličiny kompatibilné s meraniami. Dokument preto dôsledne
oddeľuje ontologický návrh, obmedzené matematické výsledky a otvorené časti.

## 2. Fyzikálny obraz a jeho kauzálne poradie

Slovo bunka neoznačuje biologickú bunku. Je to názov pre hypotetický
diskrétny lokálny stupeň voľnosti. Bunka nie je objekt vložený do už hotového
priestoru; priestor má naopak emergovať z buniek a ich vzťahov. Povrchová
sieť určuje lokálne kontakty, po ktorých sa môžu šíriť excitácie. Navrhované
„vnútro“ bunky predstavuje konečnú internú kapacitu; jeho presná kvantová
realizácia však nie je odvodená.

### 2.1 Čo musí lokálna udalosť urobiť

Teória ešte nepozná úplné časové poradie všetkých produktov. Preto
nepredkladá vymyslený lineárny reťazec, ale iba **nutné čiastočné kauzálne
poradie**:

1. bunka a jej okolie majú počiatočný stav a lokálne dostupnú energiu
   označovanú ako palivo `f`;
2. lokálny zákon môže povoliť fyzickú udalosť — prechod, prestavbu alebo
   delenie bunky;
3. táto udalosť musí mať naraz uzavretý geometrický a energeticko-hybnostný
   účet: zmena siete nesie réžiu `delta` a energia nesmie zmiznúť;
4. povolené výstupy účtu sa skúmajú ako stabilný zhlukujúci produkt `c`
   (popol), relativistický produkt $s$ (para) a prípadne ďalšie hmotné
   excitácie; ich paralelný vznik, postupný reťazec aj zmiešané vetvenie sú
   stále otvorené;
5. udalosť **môže** zanechať pretrvávajúcu lokálnu zmenu vnútorného stavu
   alebo väzieb — jazvu/doménu I. Nie je dokázané, že vzniká pri každom
   delení, že je energeticky totožná s popolom, ani že sama vyberá jeden
   výsledok kvantového merania;
6. až makroskopický limit opakovaných udalostí má dať expanziu `H(a)` a
   poruchy produktov majú ovplyvniť CMB, rast štruktúr a lensing.

Toto poradie určuje iba to, že výsledok nemôže predchádzať lokálnej udalosti
a že geometria, produkty aj prípadná pamäť musia mať jeden konzistentný
účet. Neurčuje, či najprv vznikne popol, para alebo jazva. O tom má rozhodnúť
lokálny kovariantný produkčno-transportný operátor a pozorovania. Dnešný
backgroundový model prenáša energiu z paliva do CDM/popola a baryóny v ňom
zachováva; neodvodzuje vznik obyčajnej hmoty, pary ani jazvy.

| Pracovný názov | Fyzikálna rola | Stav vo v3.18 |
|---|---|---|
| bunka | lokálny stupeň voľnosti substrátu | `HYPOTHESIS`; Planckova veľkosť nie je odvodená |
| palivo `f` | metastabilná zložka s tlakom blízkym vákuu | homogénny ledger existuje; mikrofyzika je otvorená |
| delenie/prestavba | lokálna zmena siete navrhovaná ako pôvod expanzie | `HYPOTHESIS`; continuum limita chýba |
| réžia `delta` | efektívna disipačná cena prestavby | geometrické čítanie je `CONDITIONAL` |
| popol `c` | gravitačne zhlukujúci produkt/CDM kandidát | backgroundová identita je podmienená; particle model otvorený |
| para $s$ | voľne sa šíriaci relativistický produkt | zdroj, časovanie a entropická história otvorené |
| V-spoj | klasická zdieľaná interná kapacita dvoch buniek | kvantová identifikácia nie je odvodená |
| jazva/doména I | kandidát na pretrvávajúcu vnútornú alebo väzbovú zmenu po bunkovej udalosti | toy test Q8-K1 podporuje úplne pozitívny, stopu zachovávajúci dephasing, potlačenie koherencie, nárast entropie pre zvolený vstup a no-signalling v testovanom kvbitovom rozsahu; explicitný trvalý register, mikroskopický operátor, jediný výsledok, Bornovo pravidlo a šíp času netestoval |

Jazva bola teda zaradená ako povinný kandidát, ak má program vysvetliť nosič
trvalého záznamu a fundamentálnej nezvratnosti. Audit starej koľaje `Q8-K1`
ukázal, že dephasingový operátor
môže potlačiť koherenciu a zvýšiť entropiu, ale vytvorí zmes, nie jeden
objektívne vybraný výsledok. Tento čiastkový úspech podporuje iba efektívnu
dekoherenciu a vznik klasickej zmesi v zvolenej báze; nepreukazuje fyzickú
pamäť ani trvalú jazvu a nedokazuje, že jazva rieši kolaps alebo že jej počet
či energia vysvetľujú malé číslo `epsilon`.

### 2.2 Míľniky, ktoré už cesta dosiahla

Nasledujúca mapa je čitateľným súhrnom všetkých prijatých míľnikov aktívnej
cesty. Podrobné rovnice, obmedzenia a reprodukčné odkazy sú v §9.2.

| Míľnik | Čo sa skutočne podarilo | Čo tým ešte nebolo dokázané |
|---|---|---|
| Homogénny energetický účet (`A1-K1`) | opačné zdroje paliva a popola uzavreli homogénny účet $Q_f+Q_c=0$ | úplný štvorvektor prenosu, hybnosť ani poruchy |
| Univerzálna normalizácia backgroundu (`A1-K1`) | mapovanie $\Phi(k)z^p=A_fa^p$ odstránilo neprípustnú závislosť globálneho backgroundu od Fourierovho módu | mikrofyzický pôvod $A_f$ ani celý exact-background perturbatívny most |
| Definícia živej fyzikálnej koľaje (`A2-K4`) | transfer bol definovaný v spoločnom energetickom rámci paliva a popola | úplný lokálny produkčno-transportný operátor |
| Oprava falošnej smrti (`M-011`) | rozlíšenie absolútneho transferu od relatívneho zisku odstránilo neplatný dôvod STOP | automatický PASS koľaje |
| Regulárna superhorizontová báza (`A2-K4.1`, `G5=50/100`) | bol odvodený regulárny superhorizontový módový základ a tri nulové korene v presnom scope | použiteľnosť starého seedu a úplná kozmologická evolúcia |
| Vysokofrekvenčný principal symbol (`A2-K4.2`, `G6=60/100`) | high-$k$ principal symbol nemal v deklarovanom efektívnom scope K4-špecifický rastúci koreň | úplná no-ghost veta a globálna stabilita všetkých módov |
| Druhový a anisotropický ledger (`A2-K4.3a`) | druhy boli oddelené, anisotropický stress zachovaný a Thomsonov hybnostný účet algebraicky uzavretý | plná dynamická evolúcia; skóre ostalo `60/100` |
| Statický rámec a Einsteinove constrainty (`P5.1-P5.2`) | spoločný statický rámec a štyri Einsteinove rezíduá boli algebraicky rekonštruované ako presné nuly | zachovanie constraintov počas evolúcie |
| Planárna Landauova prípustná oblasť (`EC42`) | v pravidelnom interface-adapted $1+1$ rámci bola odvodená presná podmienka $|E+P_n|>2|q|$ a jediný subluminálny koreň | nejde o Landau PASS, dôkaz neprázdneho fyzického rozsahu ani dynamickú stabilitu |
| Evidenčné pokrytie a logická úplnosť (`P5.3`, `C2/C3`) | pokrytie `10/10` atómov a logická matica `45/45` sú úplné vo svojom evidenčnom scope | fyzický seed witness alebo dôkaz existencie operátora |
| Dnešná hranica P5.3 | desať tried ostáva `WAITING` a žiadna nie je fyzikálne vylúčená | complete $A_Q(Z)$, zdrojovaná actual whole-map alebo dokázane neprázdna P1–P2 úplná rodina $A_X(Z,Q)$ a až potom klasifikácia $\ker X_Z=\{0\}$ verzus nenulový fyzický prvok. Tento per-state tangent-map diskriminátor sám nie je witness globálneho lokálneho zákona; A2-K4 zostáva `LIVE/WAITING` na `60/100` |

Ak má tento obraz prežiť, musí rešpektovať celkovú energiu a hybnosť,
kauzalitu, lokálnosť, Einsteinove a gauge constrainty, stabilitu,
termodynamiku, Lorentzove a ekvivalenčné medze aj observačné dáta. Overená
fyzika je mantinel modelu, nie súper, ktorého možno ignorovať.

## 3. Čo znamená „odvodené“, „podmienené“ a „otvorené“

| Štítok | Význam |
|---|---|
| `DERIVED` | odvodené v presne uvedenom matematickom scope |
| `CONDITIONAL` | platí iba pri uvedených vstupoch, kotve alebo modeli |
| `HYPOTHESIS` | fyzikálne prípustný návrh bez dôkazu existencie |
| `OPEN` | povinné odvodenie, mechanizmus alebo výpočet nie je uzavretý |
| `WITHDRAWN` | staršia presná formulácia sa už nepoužíva ako current claim |
| `HISTORICAL` | úplne označený starší výsledok bez current predikčnej váhy |
| `STOP_SCOPE` | certifikovaný rozpor iba v presne uvedenej podtriede |

Niekoľko opakovaných technických slov má v dokumente úzky význam.
`Scope` je presne ohraničená trieda modelov, pre ktorú bol výsledok naozaj
odvodený. `Comparator` je kontrola, či obmedzený mechanizmus reprodukuje
známe škálovanie alebo číslo; nie je to automaticky odvodenie celej fyziky.
`Background` je homogénna kozmologická evolúcia bez priestorových porúch.
`Ledger` je sústava bilančných rovníc, ktorá eviduje, odkiaľ energia odchádza
a kam vstupuje. `Closure` znamená, že pre danú úroveň opisu nechýba potrebná
rovnica alebo protizdroj. `Observable` je veličina, ktorú možno cez presnú
mapu porovnať s meraním.

Nenájdená funkcia ani prázdny numerický grid sám osebe nie je dôkazom
neexistencie. Kým nie je dokázaná neprázdnosť alebo prázdnosť spoločnej
prípustnej množiny, stav je `GLOBAL_FEASIBILITY_INCOMPLETE`.

Filozofický základ možno zhrnúť do piatich pravidiel. Pozorovateľná realita
môže byť efektívnou vrstvou hlbšieho substrátu (F1), no nepozorovateľný
objekt musí mať kvantifikovateľnú nepriamu stopu (F2). Meranie sa nemá
opierať o výsadné vedomie, ale o fyzickú nezvratnosť (F3). Model nepripisuje
vesmíru účel (F4). Lokálna prestavba nemá byť zadarmo: musí mať energetickú,
entropickú alebo kapacitnú cenu (F5). F5 motivuje `delta`, ale sám jeho
hodnotu nedokazuje.

Nasledujúce kapitoly preto nezačínajú záverom, ale jednotlivými mostami,
ktoré by museli spojiť bunkovú hypotézu so známou fyzikou.

## 4. Od bunkovej siete k merateľnej fyzike

Prvým mostom je geometria. Druhým je šírenie signálu. Tretím je otázka, či
rovnaká lokálna štruktúra môže niesť gravitáciu, kvantové korelácie a
kozmologickú dynamiku bez porušenia známych zákonov. Doterajšie výsledky sú
komparátory a obmedzené operátorové vety; nie sú ešte continuum teóriou.

### 4.1 Poissonova–Delaunayova geometria

Geometrický comparator používaný modelom je

$$
\boxed{
\langle k\rangle=\frac{48\pi^2}{35}+2\simeq15.535
}
\tag{5}
$$

**Symboly:** $k$ je stupeň jedného uzla, teda počet jeho susedov;
$\langle k\rangle$ je ensemble priemer; $\pi$ je kruhová konštanta.

**Mainstream a rozdiel:** ide o známy stereologický výsledok pre ideálnu
trojrozmernú Poissonovu–Delaunayovu geometriu, nie o nový zákon KBTP. KBTP ho
používa ako geometrický vstup do rovnice (1), čím mu dáva nový kozmologický
význam, ktorý samotná stereológia neobsahuje.

Archivované simulácie uvádzali
približne `15.58` pre Poissonovu a `15.32–15.54` pre delením vyrastenú
sieť.

**Stav v3.18:** `CONDITIONAL / HISTORICAL_SUPPORT`. Comparator a historické
merania zostávajú použiteľné v ich presnom sieťovom scope. Nie sú dôkazom,
že fyzický časopriestor je práve tento náhodný graf, ani analytickou vetou o
limite dynamicky rastúcej siete. Makroskopický limit anizotropie zostáva
otvorený.

### 4.2 Réžia delenia

Podmienené geometrické čítanie modelu je

$$
\boxed{
\delta=\frac{1}{\langle k\rangle+C}
}
\tag{6}
$$

Pri $\langle k\rangle=15.535$ a $C=28$ dáva

$$
\delta=\frac{1}{15.535+28}\simeq\boxed{0.02297}.
\tag{7}
$$

**Symboly:** $\delta$ je bezrozmerná réžia; $\langle k\rangle$ počet
povrchových kontaktov; $C$ pracovná vnútorná kapacita.

**Mainstream a rozdiel:** moderná kozmológia môže parametrizovať
$w=-1+\delta$, ale vzťah (6) nepozná. Novosť KBTP je hypotéza, že odchýlku od
vákuového tlaku určuje cena prestavby lokálnej siete.

Motivácia je podiel jedného prestavaného rozhrania na povrchovej a vnútornej
kapacite bunky. Tu treba oddeliť dve fyzikálne definície. Rovnica (6) môže
byť priamo definíciou globálnej réžie z priemerného stupňa. Ak je však
lokálnou réžiou každej bunky $1/(k+C)$ a až táto veličina sa priemeruje,
Jensenova nerovnosť dáva exaktný mantinel

$$
\boxed{
\delta_{\rm loc}=\left\langle\frac{1}{k+C}\right\rangle
\geq
\frac{1}{\langle k\rangle+C}=\delta_{\rm mean}
}
\tag{7a}
$$

s ostrou nerovnosťou pri nenulovom rozptyle stupňa. Pre
$\mu=\langle k\rangle$ má formálny momentový rozvoj v oblasti svojej
platnosti tvar

$$
\delta_{\rm loc}
=\frac{1}{\mu+C}
+\frac{\operatorname{Var}(k)}{(\mu+C)^3}
-\frac{\langle(k-\mu)^3\rangle}{(\mu+C)^4}+\cdots.
\tag{7b}
$$

Pri $\mu=48\pi^2/35+2$ a $C=28$ je
$\delta_{\rm mean}=0.0229697827528021$ a koeficient vedúcej absolútnej
korekcie je $1/(\mu+C)^3=1.2119108203766\times10^{-5}$ na jednotku
$\operatorname{Var}(k)$. Číselné $\delta_{\rm loc}$ z toho ešte nevyplýva:
treba celú distribúciu stupňa rastúcej siete alebo dostatočne kontrolované
momenty. Historické meranie pri $C=0$,
$\langle1/k\rangle=0.0701>1/\langle k\rangle=0.0647$, iba potvrdzuje, že
efekt fluktuácií môže byť nenulový; nemožno ho preniesť ako hotovú korekciu
na $C=28$ ani na dynamicky deliacu sa sieť.

**Stav v3.18:** `CONDITIONAL`. Aritmetika rovnice (6) je presná po prijatí
`<k>` a `C`, ale jej identifikácia s univerzálnym kozmologickým disipačným
parametrom nie je samostatne dokázaná. Ak má ísť o priemer lokálnej réžie,
hodnota `0.02297` je iba Jensenova dolná hranica; ak je (6) definíciou
globálnej réžie z priemerného stupňa, ide o inú coarse-graining hypotézu.
Vo v3.18 medzi nimi nie je rozhodnuté.

### 4.3 Kapacita `C=28`

Hypotéza kapacity počíta bozónové stavy Standard Modelu v obnovenej
symetrii:

$$
\boxed{
C=16_{\rm gluon}+8_{\rm EW}+4_{\rm Higgs}=28
}
\tag{8}
$$

**Symboly:** prvý člen počíta polarizačné stavy ôsmich gluónov, druhý
kalibračné stavy obnovenej elektroslabej fázy a tretí reálne stupne voľnosti
Higgsovho dubletu.

**Mainstream a rozdiel:** samotné počítanie stavov patrí Štandardnému modelu.
Neštandardná je identifikácia tohto počtu s vnútornou kapacitou bunky.

**Stav v3.18:** `HYPOTHESIS / LOOK_ELSEWHERE_ACKNOWLEDGED`. Aritmetický
rozklad je štandardný počet bozónových stupňov voľnosti neporušeného
Standard Modelu: komplexný Higgsov dublet už obsahuje štyri reálne smery a
tri z nich sa po narušení symetrie interpretujú ako would-be Goldstonove
módy; nejde o ďalšie štyri stavy, ktoré treba pripočítať druhý raz. Otvorená
nie je táto aritmetika, ale fyzická identifikácia: prečo má vnútorná kapacita
bunky počítať práve všetky bozónové a žiadne fermiónové stupne, prečo má byť
tento počet vlastnosťou substrátu namiesto už emergentného Standard Modelu a
prečo zostáva dynamickým atraktorom bez použitia CMB čísla. Kým neexistuje
nezávislé pre-dátové odvodenie, zhoda `C=28` sa nesmie vykazovať ako
predikcia teórie.

### 4.4 Emergentný front signálu

Archivované grafové simulácie merali

$$
\boxed{
\sigma(R)\propto R^{\chi},
\qquad
\chi\simeq0.26\text{--}0.32<1
}
\tag{9}
$$

**Symboly:** $R$ je stredný polomer grafového frontu, $\sigma(R)$ jeho
priestorová šírka a $\chi$ fitovaný exponent rastu šírky.

**Mainstream a rozdiel:** sublineárne zdrsňovanie frontov má analógie v
first-passage percolation a KPZ triedach. KBTP navyše skúma, či limit
$\sigma/R\to0$ môže byť mikroskopickým pôvodom ostrého svetelného kužeľa.

Relatívna šírka `sigma/R` preto klesá, ak `chi<1`.

**Stav v3.18:** `DERIVED_WITHIN_SIMULATED_GRAPH / OPEN_PHYSICAL_MAP`.
Sublineárne rozširovanie frontu je vlastnosť testovaného grafového procesu.
Samo osebe nedokazuje univerzálny relativistický svetelný kužeľ,
mikrokauzalitu QFT ani boostovú symetriu fyzického časopriestoru.

### 4.5 Skalárny cosine-Laplacian operátor a podmienka pre disperziu

Pre skúmaný nevažovaný reálny symetrický grafový Laplacián platil
bezrozmerný variačný Rayleighov podiel

$$
\boxed{
\widehat{\lambda}(\mathbf{q})=
\frac{2}{N}\sum_{\langle ij\rangle}
\left[1-\cos\!\left(\mathbf{q}\!\cdot\!\boldsymbol{\Delta}_{ij}\right)\right]
}
\tag{10}
$$

**Symboly:** $\widehat{\lambda}$ je bezrozmerná Rayleighova hodnota
grafového Laplaciánu; $\mathbf q$ je skúšobný vlnový vektor v súradniciach
vloženého grafu, nie automaticky kozmologické komové $\mathbf k$; $N$ je počet
uzlov, $\langle ij\rangle$ označuje hrany a $\boldsymbol{\Delta}_{ij}$
geometrický vektor danej hrany. Fyzická uhlová frekvencia by navyše
vyžadovala odvodenú časovú alebo väzbovú škálu, napríklad
$\omega^2=\Omega_{\rm cell}^2\widehat{\lambda}$; hodnota
$\Omega_{\rm cell}$ tu odvodená nie je.

**Mainstream a rozdiel:** ide o Rayleighov podiel reálneho symetrického
grafového Laplaciánu, teda o štandardnú spektrálnu matematiku. KBTP ho skúma
ako kandidátsky efektívny operátor priestorového substrátu; zatiaľ nie ako
odvodený Maxwellov alebo fotónový operátor.

Preto je tento konkrétny operátor presne párny:

$$
\boxed{
\widehat{\lambda}(\mathbf q)=\widehat{\lambda}(-\mathbf q)
}
\tag{11}
$$

Rovnica (11) hovorí, že tento skalárny operátor je párny pod zmenou smeru
skúšobného vlnového vektora. Zakazuje lineárny nepárny člen v tomto presnom
scope; nezakazuje automaticky všetky Lorentz-porušujúce členy vo všetkých
spinových sektoroch.

Jeho Taylorov rozvoj neobsahuje lineárny nepárny člen v $\mathbf q$.
Vedúci člen má všeobecne párny kvadratický tvar
$q_aA^{ab}q_b$ a prvá absolútna diskrétna korekcia je štvrtého rádu.
Až odvodená izotropná continuum mapa a časová škála by dovolili
identifikovať kvadratický koeficient s fyzickým $c^2$; tento krok zatiaľ
chýba.

**Stav v3.18:** `DERIVED_IN_SCALAR_OPERATOR_SCOPE / SCOPE_NARROWED`.
Exaktná nula lineárneho člena platí pre auditovaný skalárny operátor. Nie je
to ešte odvodenie fotónového, fermiónového ani gravitačného operátora,
univerzálneho limitného `c`, ekvivalenčného princípu alebo absencie
birefringencie. Dosadenie `l_cell=l_P` je ďalšia hypotéza, nie výsledok
samotnej párnosti.

### 4.6 Jedno limitné `c`

Súčasná hypotéza navrhuje, že všetky polia čítajú tú istú lokálnu bunkovú
kapacitu. Ak by sa táto identita odvodila pre všetky spinové sektory, mohla
by viesť k spoločnému limitnému kužeľu.

Zamýšľaný univerzálny limit možno zapísať ako povinnosť

$$
\boxed{
c_{\gamma}=c_{\rm GW}=c_{\rm matter}\equiv c
}
\tag{12}
$$

**Symboly:** $c_{\gamma}$ je limitná rýchlosť fotónového sektora,
$c_{\rm GW}$ gravitačných vĺn, $c_{\rm matter}$ hmotných polí a $c$ spoločný
lokálny limit.

**Mainstream a rozdiel:** v lokálnej relativistickej QFT a GR je spoločný
svetelný kužeľ základnou štruktúrou metriky. KBTP ho chce odvodiť ako
emergentný limit siete. Rovnica (12) je preto cieľ/constraint, nie dnešný
odvodený výsledok.

**Stav v3.18:** `OPEN`. Úplný dôkaz vyžaduje spoločnú efektívnu metriku pre
všetky spinové sektory, lokálnu Lorentzovu limitu, presné potlačenie
lineárnej disperzie, ekvivalenčný princíp a konzistentnú interakciu. Starý
argument z dvoch zvolených sieťových väzieb nie je dôkazom jedinečnosti
všetkých fyzikálne prípustných väzieb.

### 4.7 Vnútorná kapacita a pravidlo polovičného vena

Pracovný klasický model V-spojov predpokladá, že dve dcérske bunky po
delení zdedia polovicu rodičových väzieb a navzájom si pridelia polovicu
kapacity `C`. Pre priemernú vnútornú väzbu `n_V` má mapa tvar

$$
\boxed{
n_{V}^{\rm new}=\frac12 n_{V}^{\rm old}+\frac12 C,
\qquad
n_{V}^{\ast}=C
}
\tag{13}
$$

**Symboly:** $n_V^{\rm old}$ a $n_V^{\rm new}$ sú vnútorné väzbové váhy
pred a po aktualizácii, $C$ kapacita a $n_V^{\ast}$ pevný bod mapy.

**Mainstream a rozdiel:** afinná kontrakčná mapa a jej pevný bod sú
elementárna dynamika. Neštandardná je hypotéza, že táto mapa opisuje delenie
bunkových vnútorných stavov a nesie fyzický význam previazania.

Archivované simulácie približne desiatich tisíc buniek podporili
konvergenciu k pevnému bodu zhora aj zdola, relatívnu šírku približne
`std/mean=0.13` a škálovanie V-váhy cez guľovú hranicu približne ako
`R^1.97`.

**Stav v3.18:** `HISTORICAL_NUMERICAL_SUPPORT / OPEN_QUANTUM_MAP`. Rovnica
je presná pre uvedené klasické pravidlo aktualizácie a simulácie podporujú jeho
atraktor a plošný comparator. Neodvodzujú Hilbertov priestor, entanglement
entropy, kvantový kanál, Bekensteinovu entropiu ani fyzický gravitačný zákon.
Ak má vnútorná vrstva reprezentovať kvantovú previazanosť, musí samostatne
prejsť kauzalitou a zákazom nekontrolovaného prenosu energie alebo signálu.

### 4.8 Newtonov grafový comparator

V konkrétnych archivovaných sieťových simuláciách dve zvolené lokálne
väzbové schémy — rovnocenné kontakty a FEM váhy úmerné ploche rozhrania —
reprodukovali inverse-square comparator s uvádzanými regresnými hodnotami
približne `R^2=0.9991` a `R^2=0.9996`.

Porovnávaný mainstreamový tvar bol

$$
\boxed{
|\mathbf{g}(r)|\propto\frac{1}{r^2}
}
\tag{14}
$$

**Symboly:** $\mathbf{g}(r)$ je efektívna radiálna odozva comparatora a $r$
vzdialenosť od zdroja. Rovnica (14) je Newtonov slabopoľový tvar; KBTP tu
nepriniesla inú mocninu, iba testovala, či ju vie reprodukovať lokálny graf.

**Stav v3.18:** `HISTORICAL_NUMERICAL_SUPPORT / SCOPE_NARROWED`. Ide o
podporu jedného grafového mechanizmu v simulovanom scope, nie o odvodenie
Einsteinových rovníc, univerzálneho `G`, PPN limitov, lensingu,
ekvivalenčného princípu alebo kvantovej gravitácie.

## 5. Homogénne kozmologické pozadie

Sieťové comparátory samy neurčujú, ako sa rozpína vesmír. Na to treba
prejsť od lokálneho obrazu k homogénnemu účtovníctvu hustôt. Background je
prvý nutný test: musí zachovať energiu, mať jedinú expanznú históriu
`H(a)` a nesmie závisieť od toho, ktorý Fourierov mód poruchy neskôr
evolvujeme. Úspech na tejto úrovni je však iba vstupom do fyziky porúch,
nie dôkazom celej teórie.

### 5.1 Efektívny background ledger V1

Pri `x=ln a` používa živá backgroundová koľaj efektívny systém

$$
\boxed{
\begin{aligned}
\frac{d\rho_f}{dx}
  &=-3\delta\rho_f-\lambda\frac{H_0}{H}\rho_f,\\
\frac{d\rho_c}{dx}
  &=-3\rho_c+\lambda\frac{H_0}{H}\rho_f,\\
\frac{d\rho_b}{dx}&=-3\rho_b,\\
\frac{d\rho_r}{dx}&=-4\rho_r,\\
H^2&=\frac{8\pi G}{3}\rho_{\rm total}.
\end{aligned}
}
\tag{15}
$$

**Symboly:** $x\equiv\ln a$ je počet e-foldov, $a$ mierkový faktor;
$\rho_f,\rho_c,\rho_b,\rho_r$ sú hustoty paliva, popola/CDM, baryónov a
radiácie; $H$ je Hubbleova miera, $H_0$ jej dnešná hodnota, $G$ Newtonova
konštanta, $\delta$ réžia a $\lambda\equiv\Gamma/H_0$ bezrozmerný parameter
efektívnej transferovej miery $\Gamma$.

**Mainstream a rozdiel:** Friedmannova rovnica, riedenie baryónov $a^{-3}$ a
radiácie $a^{-4}$ sú štandardné. Nové sú prvé dve rovnice: KBTP povoľuje
výmenu medzi palivom a popolom. V ΛCDM sú $\Lambda$ a CDM samostatne
konzervované; zodpovedajúci transfer je nulový.

Pri `p_f=(-1+delta)*rho_f` a `p_c=0` možno v homogénnom FLRW rámci zaviesť
backgroundové zdrojové skaláre konvenciou

$$
\dot\rho_A+3H(\rho_A+p_A)=Q_A,
\qquad
\boxed{
Q_f=-Q_c=-\lambda H_0\rho_f
}.
\tag{16}
$$

**Symboly:** bodka je derivácia podľa kozmického času, $A$ index zložky,
$p_A$ jej tlak a $Q_A$ backgroundový skalárny zdroj. Protisúčet
$Q_f+Q_c=0$ uzatvára homogénny energetický účet.

**Mainstream a rozdiel:** prvá rovnica je štandardná kontinuita
interagujúcich kozmologických tekutín. KBTP špecifikuje fenomenologický tvar
druhej rovnice; úplný kovariantný štvorvektor $Q_A^{\mu}$ ešte neodvodila.

Ich súčet uzatvára iba homogénnu energetickú bilanciu. Nedokazuje
existenciu úplného kovariantného štvorvektora `Q_A^mu`, momentum closure ani
Einsteinovu/Bianchiho konzistenciu porúch. Baryóny sú v A1-K1 konzervované
a produktom backgroundového transferu je CDM/popol, nie baryónová hmota.

**Stav v3.18:** `BACKGROUND_GATE_PASS / CONDITIONED`. Systém je
fenomenologický efektívny ledger a vie byť backgroundovo konzistentný.
Samotný zápis `Q_f=-Q_c` neurčuje priestorový prenos hybnosti,
perturbácie $\delta Q$, mikrofyzickú mieru udalostí, obsah častíc ani
produkciu pary. Preto neuzatvára A2.

#### Rodina `lambda` a jej zatiaľ otvorený rozsah platnosti

Zákon zachovania v rovnici (16) vynucuje opačné zdroje po zvolení
transferového kanála. Zápis

$$
\Gamma\equiv\lambda H_0,
\qquad
Q_f=-Q_c=-\Gamma\rho_f
$$

definuje skúmanú **jednoparametrovú rodinu efektívnych mier**, nie jedinú
odvodenú prírodnú konštantu. Fyzikálnym parametrom tohto efektívneho modelu
je konštantný skalár $\Gamma$; zápis $\lambda=\Gamma/H_0$ je jeho
bezrozmerná parametrizácia voči dnešnej referenčnej hodnote $H_0$. Pri
prechode z kozmického času na $x=\ln a$ potom presne vznikne faktor
$\Gamma/H=\lambda H_0/H$ v rovnici (15). Vnútorné hodiny bunky sú možným
budúcim mikrofyzickým pôvodom $\Gamma$, nie už hotovým odvodením. Dnešná
mikrodynamika preto neurčila ani $\Gamma$, ani číselnú hodnotu $\lambda$.

Pre smer „palivo $\rightarrow$ popol“ sa skúma $\lambda\ge0$; $\lambda=0$
je kontrolný nulový transferový limit. Historické screeningy vyhodnotili
oddelené body `0.10` a `0.15`. Neznamená to, že celý interval medzi nimi je
už fyzikálne povolený. Hodnota `lambda=0.15` je dnes zmrazený, historicky
dátami vybraný referenčný bod aktívnej A1-K1/A2-K4 koľaje. Zmrazenie bráni
tomu, aby sa parameter počas stabilitných testov potichu dolaďoval; nie je
dôkazom jeho jedinečnosti.

Súvislý prípustný rozsah $\lambda$ bude možné označiť za platný až tam, kde
sa súčasne preukáže:

1. kladnosť hustôt a $H^2$ na celej požadovanej backgroundovej histórii;
2. zachovanie energie a hybnosti a správny $\lambda\to0$ limit;
3. superhorizontová aj subhorizontová stabilita úplného A2 operátora;
4. kompatibilita s BBN, CMB, BAO, rastom a lensingom vrátane neistôt a
   kovariancií;
5. jedna módovo nezávislá expanzia $H(a)$ bez nového skrytého fitu.

Takýto certifikovaný interval v3.18 ešte nemá. Teória preto povoľuje rodinu
kandidátskych hodnôt, ale číselne zatiaľ skúma zmrazený benchmark `0.15` a
historické porovnanie s bodom `0.10`. Čítanie
`epsilon_eff=lambda*H0*t_P` zostáva iba podmienenou parametrickou mapou;
zhoda rádu `epsilon_eff^2` s kozmologickou mierkou nie je dôkazom
nukleačného mechanizmu jaziev.

### 5.2 Univerzálny background a zákaz módovej závislosti

Pri skorom perturbatívnom odvodení sa zaviedla bezrozmerná súradnica

$$
\boxed{
z\equiv\frac{k\,a}{H_0\sqrt{\Omega_{r0}}}
=\frac{k}{\mathcal H_r}
}
\tag{17}
$$

**Symboly:** $z$ je bezrozmerná skorá perturbatívna súradnica, $k$ komové
Fourierovo vlnové číslo, $\Omega_{r0}$ dnešný radiačný podiel a
$\mathcal H_r=H_0\sqrt{\Omega_{r0}}/a$ referenčná konformná Hubbleova miera
v radiačnej ére.

**Mainstream a rozdiel:** bezrozmernenie módu pomerom $k/\mathcal H$ je
štandardná perturbatívna technika. Chyba starého runnera bola, že túto
módovú súradnicu preniesol do globálneho backgroundu.

Palivový pomer však z backgroundovej rovnice kontinuity spĺňa

$$
y_f\equiv\frac{\rho_f}{\rho_r},
\qquad
\boxed{
\frac{dy_f}{dx}
=\left(4-3\delta-\lambda\frac{H_0}{H}\right)y_f
}.
\tag{18}
$$

**Symboly:** $y_f$ je pomer hustoty paliva k radiácii; ostatné symboly sú
definované pri rovnici (15). Člen `4` vzniká vydelením radiáciou, ktorá sa
riedi ako $a^{-4}$.

Bez prenosovej korekcie je vedúca mocnina

$$
y_f\propto a^p,
\qquad
\boxed{p=4-3\delta}.
\tag{19}
$$

**Symboly:** $p$ je vedúci skorý exponent pomeru $\rho_f/\rho_r$ v limite,
kde sa transferová korekcia $\lambda H_0/H$ zanedbá. Tento exponent je
backgroundový; nie je určený voľbou Fourierovho módu.

Ak sa skoré riešenie zapíše ako `Phi(k)*z^p`, backgroundová amplitúda musí
transformovať podľa

$$
\boxed{
\Phi(k)=A_f
\left(\frac{H_0\sqrt{\Omega_{r0}}}{k}\right)^p
}
\tag{20}
$$

**Symboly:** $\Phi(k)$ je integračný koeficient pri zápise skorého riešenia
v súradnici $z$; $A_f$ je jediná backgroundová amplitúda nezávislá od módu.
Nejde tu o Newtonov potenciál, hoci sa historicky používalo rovnaké písmeno.

aby

$$
\boxed{
\Phi(k)z^p=A_fa^p
}
\tag{21}
$$

Rovnica (21) je presná algebraická kancelácia všetkých mocnín $k$. Jej
mainstreamový význam je jednoduchý: homogénna FLRW expanzia nesmie závisieť
od toho, ktorý perturbatívny mód sa práve evolvuje. KBTP-špecifické je
mapovanie skorého palivového riešenia na amplitúdu $A_f$.

**Stav v3.18:** `REQUIRED_NORMALIZATION_MAP / CONDITIONAL_A1_NORMALIZATION_ACCEPTED`.
Odstránenie holého `k^p` z homogénneho backgroundu je povinné. Pre zmrazený
A1-K1 closure s `lambda=0.15`, `delta=0.02297`, `Omega_m0=0.3517`,
`h=0.6637`, plochou uzávierkou a vyhodnotením pri `x_reference=-18` bolo
bez ďalšieho fitu odvodené

$$
\boxed{A_f=7809.270101963506}
\tag{22}
$$

**Vypočítaná hodnota:** číslo (22) platí iba pre zmrazený A1 pracovný bod
uvedený vyššie. Nie je to univerzálna konštanta ani posterior. Externý T2
audit reprodukoval multi-$k$ kanceláciu a nezávislú integráciu v tomto
scope.

**Externá auditná stopa:**
[zapečatený balík EA-004 — presný scope a poradie čítania](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/PACKAGES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/00_SCOPE_AND_READ_ORDER.md),
[odpoveď externého auditora](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/RESPONSES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/00_AUDITOR_AUDIT.md)
a
[projektové posúdenie odpovede](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/RESPONSES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/01_MAIN_ORCHESTRATOR_ASSESSMENT_2026-07-18.md).
Dosiahnutá úroveň je `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP`
v presne uvedenom scope; projektová koľaj ani jej skóre sa tým nezmenili.

Ide o parameter-bookkeeping výsledok podmienený týmito A1 vstupmi, nie o
konštantu prírody ani mikrofyzicky odvodenú amplitúdu. Projektová RK4
hodnota bola externe reprodukovaná a nezávislá DOP853 kontrola súhlasila
približne na relatívnej úrovni `1e-12`. Otvorené zostávajú mikrofyzický
pôvod `A_f` (P2b), exact-background perturbatívne preodvodenie a úplný
viac-módový systém. Normalizovaný skrátený K7 rad je iba skorá radiačná
aproximácia a nesmie sa používať ako plný neskorý background. Pred týmito
uzávermi sa CLASS/CAMB K4 adapter nesmie prezentovať ako fyzikálny výsledok.

Pevná hodnota `K_MPC=0.05` v starom runneri nie je v existujúcej proveniencii
odvodená korelačná dĺžka bunkovej siete ani dynamická rýchlosť popola. Je to
pevne vložená hodnota perturbatívneho Fourierovho $k$. Súvis s Planckovým
pivotom je iba plausibilná konvencia, nie doložený úmysel zdrojového kódu;
táto hodnota nesmie riadiť globálnu expanziu.

### 5.3 Efektívny účtovný tieň

Efektívna účtovná rekonštrukcia definuje

$$
\boxed{
\begin{aligned}
\rho_{\rm DE,eff}(a)
  &=E^2(a)-\Omega_{m0}a^{-3}-\Omega_{r0}a^{-4},\\
w_{\rm eff}(a)
  &=-1-\frac13\frac{d\ln\rho_{\rm DE,eff}}{dx}.
\end{aligned}
}
\tag{23}
$$

**Symboly:** $E=H/H_0$ je bezrozmerná expanzná miera;
$\Omega_{m0},\Omega_{r0}$ dnešné referenčné podiely hmoty a radiácie;
$\rho_{\rm DE,eff}$ účtovný zvyšok v rovnakej normalizácii ako $E^2$ a
$w_{\rm eff}$ jeho rekonštruovaná stavová rovnica.

**Mainstream a rozdiel:** táto rekonštrukcia je štandardná účtovná definícia
po odčítaní zvoleného matter/radiation modelu. KBTP ju interpretuje odlišne:
ak popol vzniká transferom, zvyšok nemusí byť fundamentálne phantomové pole.

Na porovnanie s dvojparametrovou CPL reprezentáciou sa používa

$$
\boxed{
w_{\rm CPL}(a)=w_0+w_a(1-a)
}.
\tag{23a}
$$

**Symboly:** $w_0$ je dnešná hodnota CPL aproximácie a $w_a$ jej lineárna
evolučná zložka v premennej $1-a$. Pôvodná účtovná projekcia bola
$\rho_{\rm DE,eff}$-vážená na intervale $0<z<1$ a uvádzala zaokrúhlené
hodnoty približne $(-0.92,-0.61)$. V3.18 prijíma dvojicu

$$
\boxed{w_0=-0.919,\qquad w_a=-0.612}
\tag{23b}
$$

ako cieľ prežitia presnej efektívnej účtovnej formulácie P06. Nie je to nový
fit ani posterior. Úplná váhovacia funkcia, spoločná kovariancia a aktuálna
dátová pipeline neboli v tomto vydaní znovu odvodené; platné vylúčenie preto
vyžaduje rovnakú CPL projekciu a spoločný likelihood dvojice, nie dve
nezávislé porovnania čísel.

Ak pozorovateľ odčíta striktne konzervovanú hmotu, hoci model obsahuje
backgroundový transfer do CDM, zvyšok môže mať efektívne `w_eff<-1` bez
toho, aby fundamentálna zložka mala rovnakú stavovú rovnicu.

**Stav v3.18:** `CONDITIONAL_INTERPRETATION / RECALCULATION_OPEN`. Rovnica
(23) je účtovná identita po zvolení backgroundu a referenčného rozkladu.
Dvojica (23b) je aktuálny formulation-scoped survival target P06, nie
mikrofyzicky odvodená stavová rovnica paliva, certifikovaný interval,
posterior ani experimentálne potvrdenie.

### 5.4 Para a relativistický produkt

Termálny comparator pod predpokladom skorého odpojenia je

$$
\boxed{
\Delta N_{\rm eff}=\frac47 g_x
\left[
\frac{g_{\ast s}(T_{\nu,\rm dec})}
     {g_{\ast s}(T_{x,\rm dec})}
\right]^{4/3}
=\frac47 g_x
\left(\frac{10.75}{g_{\ast s,\rm dec}}\right)^{4/3}
}
\tag{24}
$$

**Symboly:** $\Delta N_{\rm eff}$ je dodatočná radiačná energia vyjadrená v
neutrínových jednotkách; $g_x$ je počet vnútorných bozónových stupňov
voľnosti pary; $g_{\ast s}(T)$ je efektívny počet **entropických** stupňov
voľnosti plazmy pri teplote $T$; $T_{x,\rm dec}$ a $T_{\nu,\rm dec}$ sú
teploty odpojenia pary a neutrín. Faktor $4/7$ prevádza jeden bozónový
stupeň na neutrínovú konvenciu a hodnota `10.75` je štandardné
$g_{\ast s}$ pri neutrínovom odpojení. Historický faktor $8/7$ vznikne až po
prijatí $g_x=2$.

**Mainstream a rozdiel:** vzorec je štandardná entropická aritmetika pre
skoro odpojený bozónový relikt. KBTP dáva pare kvalitatívny kauzálny pôvod:
je to odviazaný vlnový produkt spracovania vákuového paliva pri bunkovej
genéze. Historický test navyše ukázal, že neskorá tvorba hmoty posúva `H0`
nadol, zatiaľ čo chýbajúci relativistický príspevok pôsobí opačným smerom.
Teória však zatiaľ neodvodila lokálny branching, presný čas odpojenia ani
prečo fyzická para realizuje práve dve polarizácie v tejto termálnej limite.

Pre deklarované vstupy formulácie $g_x=2$ a
$g_{\ast s,\rm dec}=106.75$ vychádza

$$
\Delta N_{\rm eff}=0.0535,
\qquad
N_{\rm eff}=3.045+0.0535\simeq3.10.
\tag{24a}
$$

Mainstreamová referencia použitá v tomto podmienenom výpočte bola
$N_{\rm eff}=3.045$ bez dodatočného reliktu. Rozdiel KBTP comparatora je
$+0.0535$, ale zatiaľ je iba podmienený vstup. Z rovnakého
instant-decoupling čítania pochádzali hodnoty `0.90 K / 53 GHz`.

**Rozsah tvrdenia v3.18:** Aritmetika termálneho reliktu a kvalitatívny
pôvod pary sú zachované. Pri
uvedených vstupoch sú `0.0535`, `3.10`, `0.905 K` a `53 GHz` podmienenými
survival targets presnej skoroodpojenej dvojpolarizačnej formulácie. Chýbajú
kovariantný zdroj $C_s^mu$ (historicky `C_g`), jeho podpora v čase,
branching medzi hmotou, parou, popolom a jazvou, exit/reheating, prežitie a
úplná BBN/CMB observable mapa. Robustné vylúčenie cieľov zabije túto presnú
termálnu formuláciu; zhoda ju iba ponechá živú a sama nepotvrdí bunkový
pôvod.

## 6. Lineárne poruchy a pozorovateľné veličiny

Homogénny vesmír môže vyzerať konzistentne aj vtedy, keď jeho lokálne
poruchy porušujú constrainty, rastú nestabilne alebo dávajú nesprávne CMB a
zhlukovanie. Preto je A2 samostatnou stanicou. Musí rozhodnúť, či možno
backgroundový prenos rozšíriť na úplný kovariantný systém bez skrytého
zdroja energie, hybnosti alebo nového neohláseného parametra.

### 6.1 Čo musí úplný A2 systém obsahovať

Úplná lineárna stanica musí z jedného kovariantného modelu odvodiť:

- rovnice kontinuity a Eulerove rovnice všetkých interagujúcich zložiek;
- časové aj priestorové zložky prenosu `Q_A^mu` a ich protisúčty;
- Einsteinove constrainty a Bianchiho identitu;
- gauge-invariantné relatívne hustotné a rýchlostné módy;
- adiabatic/NIV/seeds a superhorizontálne nulové limity;
- stabilnú subhorizontálnu evolúciu;
- úplnú fotónovú a neutrínovú Boltzmannovu hierarchiu;
- mapu na CMB, lensing a rast bez nového neohláseného fitu.

**Stav v3.18:** `NOT_COMPLETE`. Redukované testy, constraint identity alebo
stabilita jedného módu nesmú byť prezentované ako splnenie celej stanice.

### 6.2 Rast štruktúr a cieľ prežitia `S8`

Zjednodušený zmrazený výpočet používal `x=ln a`, čiarku ako `d/dx`,
`E(x)=H(x)/H0`, rastovú amplitúdu `d(x)` a rýchlostnú konvenciu
`Theta=-d'`. Dynamická veličina `M(x)` je clustering-matter background
v rovnakej normalizácii ako `E^2`; nie je to dnešná hodnota `Omega_m0`.

$$
\boxed{
\begin{aligned}
d'&=-\Theta,\\
\Theta'&=-\left(2+\frac{d\ln E}{dx}\right)\Theta
-\frac32\frac{M}{E^2}d,\\
x_0&=-\ln(1001),\qquad
d(x_0)=e^{x_0},\qquad
\Theta(x_0)=-d(x_0),\\
\sigma_8&=0.811\frac{D}{D_{\Lambda{\rm CDM}}},
\qquad
S_8=\sigma_8\sqrt{\frac{\Omega_{m0}}{0.3}}.
\end{aligned}
}
\tag{25}
$$

**Symboly:** čiarka znamená $d/dx$ pri $x=\ln a$; $d$ je lineárna rastová
amplitúda, $\Theta=-d'$ rýchlostná konvencia, $E=H/H_0$, $M$ zhlukujúca
hmota v normalizácii $E^2$, $D$ celkový rast do dneška,
$D_{\Lambda{\rm CDM}}$ rast referenčného nulového behu a $\sigma_8,S_8$
štandardné pozorovateľné veličiny zhlukovania.

**Mainstream a rozdiel:** prvé dve rovnice sú štandardná aproximovaná
lineárna rastová sústava bez nového K4 perturbatívneho operátora. KBTP v nej
mení najmä background $E(x)$ a históriu $M(x)$. Preto je výsledok užitočný
ako citlivosť, ale nemôže nahradiť plný Einsteinov–Boltzmannov výpočet.

`D_LCDM` sa počíta tou istou implementáciou s
`lambda=delta=Delta N_eff=0`; `D` a `D_LCDM` používajú rovnakú štartovaciu
normalizáciu. V tomto scope vyšlo približne `S8=0.874`.

V3.18 prijíma `S8≈0.86–0.87` ako cieľ prežitia presnej zjednodušenej
rastovej formulácie P05. Tento rozsah nie je odvodený z troch bodov v §6.4;
ide o samostatne zmrazený záväzok formulácie. Tri body `0.87450–0.88561`
tvoria diskrétnu citlivostnú diagnostiku v inom zjednodušenom scope, nie
spojitý interval ani neistotu cieľa.

**Stav v3.18:** `RECALCULATION_OPEN / FORMULATION_SCOPED_SURVIVAL_TARGET`.
Bez úplného A2, plnej hierarchie, CMB/LSS observable mapy a spoločnej
likelihood s neistotami, kovarianciami a systematikami nejde o validovaný
posterior. Robustné vylúčenie zasahuje túto rastovú formuláciu, nie
automaticky celú KBTP. Staré mriežky trenia a krivosti sú citlivostné alebo
toy testy; ich nižšie `chi^2` nie je dôkazom lepšieho globálneho fitu.

### 6.3 CMB kotva, zvukový horizont a cieľ prežitia `H0`

Štandardné geometrické vzťahy ostávajú

$$
\boxed{
r_s(z_\ast)=\int_{z_\ast}^{\infty}
\frac{c_s(z)}{H(z)}\,dz,
\qquad
\theta_\ast=\frac{r_s(z_\ast)}{D_M(z_\ast)}
}
\tag{26}
$$

**Symboly:** $z_\ast$ je redshift posledného rozptylu, $c_s$ zvuková
rýchlosť baryónovo-fotónovej plazmy, $r_s$ komový zvukový horizont,
$D_M$ komová uhlová vzdialenosť a $\theta_\ast$ pozorovaný uhlový rozmer
akustického pravítka.

**Mainstream a rozdiel:** rovnica (26) je štandardná CMB geometria. KBTP
neponúka inú definíciu pravítka; musí dodať vlastný konzistentný $H(z)$ a
species históriu a pritom reprodukovať rovnaký nulový limit.

Ich použitie vyžaduje jeden univerzálny background, konzistentné fyzické
hustoty, rekombinačný model a jasnú dátovú kotvu.

V3.18 prijíma `H0≈66.4±0.4 km/s/Mpc` ako cieľ prežitia zmrazenej
backgroundovej formulácie P04. Šírka `±0.4` je prijaté cieľové okno tejto
formulácie, nie neistota odvodená z troch bodov v §6.4. Tieto tri body
`65.792–66.374 km/s/Mpc` sú samostatná diskrétna diagnostika, nie spojitý
interval.

**Stav v3.18:** `RECALCULATION_OPEN / FORMULATION_SCOPED_SURVIVAL_TARGET`.
Nejde o tvrdú theory-level predikciu, nový fit ani posterior. Robustné
vylúčenie je dovolené až po úplnom A2/A3 modeli, rovnakej observable mape a
likelihood zahŕňajúcej neistoty, kovariancie a systematiky; zasahuje presnú
backgroundovú formuláciu, nie automaticky celú KBTP.

### 6.4 Externe reprodukovaná podmienená `H0/S8` citlivosť

V zmrazenom kotvovom scope externý T2 audit reprodukoval deväť
grid-cell výsledkov — tri hodnoty $\Delta N_{\rm eff}$ pri troch rozlíšeniach.
Release zobrazuje tri najjemnejšie endpointy pri $N=8000$:

| `Delta N_eff` | podmienené `H0` [km/s/Mpc] | podmienené `S8` |
|---:|---:|---:|
| `0` | `65.79213819466531` | `0.8856095825403126` |
| `0.02675` | `66.08320294879377` | `0.8800254370658636` |
| `0.0535` | `66.37433224357665` | `0.874499891729803` |

Ide o tri diskrétne podmienené citlivostné body zmrazeného kotvového
výpočtu, nie o spojitý interval.

Všetkých deväť buniek troch rozlíšení prešlo interným auditom a externou T2
reprodukciou. Endpointový rozdiel v tomto scope je

$$
\boxed{
\begin{aligned}
\Delta H_0^{\rm full-null}
  &=+0.582194048911333\ {\mathrm{km\,s^{-1}\,Mpc^{-1}}},\\
\Delta S_8^{\rm full-null}
  &=-0.0111096908105096.
\end{aligned}
}
\tag{27}
$$

**Symboly:** `full` je zmrazený beh s vloženým
$\Delta N_{\rm eff}=0.0535$ a `null` ten istý kotvový model s týmto
príspevkom vypnutým. Rozdiel preto meria iba citlivosť na tento jeden vstup.

**Porovnanie s mainstreamom:** nulový bod nie je ΛCDM a čísla v
tabuľke nie sú Planck/SH0ES/KiDS posterior. Mainstreamová rovnica rastu a
akustická geometria sú rovnaké; odlišný je podmienený background a vložený
relativistický príspevok. Balík preto nedokazuje lepší alebo horší globálny
fit KBTP voči ΛCDM.

**Externá auditná stopa:**
[primárny reprodukčný balík EA-047](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/PACKAGES/EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY/00_SCOPE_AND_READ_ORDER.md)
a jeho
[externá odpoveď](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/RESPONSES/EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY/SUB-20260801-047-001/00_AUDITOR_AUDIT.md).
Nemennú control-only históriu package uzávierky tvoria
[R1 oprava](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/PACKAGES/EA-20260801-047-R1-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-REPAIR/00_SCOPE_AND_READ_ORDER.md)
s
[odpoveďou `CANNOT_AUDIT`](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/RESPONSES/EA-20260801-047-R1-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-REPAIR/SUB-20260801-047-R1-001/00_AUDITOR_AUDIT.md)
a následná
[R2 uzávierka](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/PACKAGES/EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE/00_SCOPE_AND_READ_ORDER.md)
s
[control-only PASS odpoveďou](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/RESPONSES/EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE/SUB-20260801-047-R2-001/00_AUDITOR_AUDIT.md).
R1 ani R2 neopakovali a nerozšírili vedecký výpočet EA-047.

Tieto čísla nie sú likelihood, posterior, confidence/credible interval,
spojitá obálka, fit ani tvrdá predikcia v3.18. `H0` je podmienená inverzia
voči syntetickej kotve `h_ref=0.673`; `S8` používa zjednodušený rast a
`sigma8_LCDM=0.811`. `Delta N_eff=0` vypína iba vložený parný príspevok a nie je
ΛCDM ani nulový limit teórie.

### 6.5 Spektrum skalárnych porúch

Mechanistické, zatiaľ neuzavreté čítanie bolo

$$
\boxed{
n_s-1=-\frac32\delta
}
\tag{28}
$$

**Symboly:** $n_s$ je skalárny spektrálny index a $\delta$ pracovná réžia z
rovnice (1).

**Mainstream a rozdiel:** v štandardnej inflácii je $n_s$ určené slow-roll
parametrami potenciálu inflatónu. KBTP skúšala odvodiť sklon z geometrickej
réžie bez samostatného inflatónu. Tento rozdiel by bol významný iba po
odvodení amplitúdy, gauge-invariantného $\zeta$, gaussovskosti a úplného
seedu; tieto kroky zatiaľ chýbajú.

cez kvázi-de Sitter background, plošnú tepelnú kapacitu a exponent
`m=1/2`.

**Stav v3.18:** `RECALCULATION_OPEN / MECHANISM_READING_NOT_THEOREM`.
Exponent `m=1/2`, kvantitatívna amplitúda, gaussovskosť, gauge-invariantný
prevod na `zeta`, izokurvatúry a bispektrum nie sú odvodené z jedného
uzavretého systému. Po dosadení
$\delta_{\rm mean}=0.0229697827528021$ do rovnice (28) však presný
mechanistický model dáva

$$
\boxed{
n_s=1-\frac32\delta_{\rm mean}
=0.9655453258707969\simeq0.9656
}.
\tag{28a}
$$

V3.18 prijíma `n_s=0.9656±0.0016` ako cieľ prežitia presného
`delta/m=1/2` skalárneho mechanizmu P02. Polovičná šírka `±0.0016` je
zmrazené cieľové okno, nie neistota odvodená z rovnice (28), nie Planckova
neistota a nie nový posterior. Robustné vylúčenie po úplnej
source-to-observable mape zabíja tento presný mechanizmus, nie automaticky
všetky bunkové zdroje $\mathcal P_\zeta$. Presná formula spájajúca `n_s` a
`w` zostáva `WITHDRAWN`.

### 6.6 Tenzorový sektor

Pôvodný termálny/Rayleighovo–Jeansov odhad používal v prirodzených
Planckových jednotkách $c=\hbar=k_B=1$ schematické čítanie
$\Delta_h^2\simeq0.4HT/M_{\rm Pl}^2$ — ekvivalentne
$0.4(H/M_{\rm Pl})(T/M_{\rm Pl})$ — a obsadenie $n_k=T/k$ vyhodnotené pri
$k=H$.
Viedol k veľmi silnému potlačeniu tensorov, ale bez úplného tenzorového
operátora, zdroja, skalárnej aj tenzorovej normalizácie a pivotnej konvencie
ho nemožno v tomto vydaní autoritatívne prepočítať ako hotovú predikciu.

V3.18 napriek tomu prijíma dve rozdielne formuláciou ohraničené hranice P03:

- `r<1e-10` je ostrý cieľ prežitia presného termálneho odhadu;
- robustná detekcia `r>=1e-3` je samostatný praktický marker vylúčenia
  širšej termálnej tenzorovej realizácie.

Interval `1e-10<=r<1e-3` teda ruší ostrý odhad bez automatickej smrti širšej
termálnej realizácie. Ani hranica `1e-3` nemá sama theory-level dosah, kým
nie je dokázané, že nijaká iná bunková tenzorová koľaj nie je prípustná.

**Stav v3.18:** `RECALCULATION_OPEN / FORMULATION_SCOPED_SURVIVAL_TARGET`.
Úplný rozsudok vyžaduje tenzorový operátor, zdroj, normalizáciu, pivotnú
konvenciu, B-mode likelihood a systematiky. Nedetekcia formuláciu iba
ponecháva živú; nie je jej potvrdením.

## 7. Na ktoré fyzikálne otázky dnes teória odpovedá

### 7.1 Čo je podľa hypotézy priestor?

Priestor je navrhnutý ako emergentný makroskopický opis lokálnej siete
bunkových stupňov voľnosti. Táto veta určuje ontológiu a smer výskumu, ale
ešte nie je odvodeným výsledkom. Aby sa z nej stala fyzikálna teória, treba
ukázať continuum limitu, spoločnú efektívnu metriku a pozorovateľné stopy,
ktoré nie sú iba premenovaním známej fyziky.

### 7.2 Čo sa pri kozmologickej expanzii zväčšuje?

Navrhovaná odpoveď je, že sa mení počet alebo usporiadanie lokálnych buniek,
nie že sa bunky pohybujú do vonkajšieho prázdneho priestoru. Homogénny ledger
v §5 ukazuje, že takýto obraz možno zapísať ako konzistentnú expanznú
históriu. Neodvodzuje však ešte mikroskopickú mapu medzi jednou prestavbou a
FLRW metrikou. Preto je pôvod expanzie vo v3.18 `HYPOTHESIS`, nie hotové
vysvetlenie.

### 7.3 Je palivo tmavá energia?

Palivo `f` je pracovná metastabilná zložka s tlakom blízkym vákuu. V
backgroundovom modeli môže niesť časť efektu pripisovaného tmavej energii a
pri zvolenom účtovnom rozklade môže vytvoriť efektívny tieň s
`w_eff<-1`. Z toho nevyplýva, že bola mikrofyzicky odvodená tmavá energia,
ani že `w0` a `wa` sú mikrofyzicky odvodenou stavovou rovnicou paliva.
V3.18 ich dvojicu `(-0.919,-0.612)` prijíma iba ako cieľ prežitia presnej
efektívnej účtovnej rekonštrukcie P06; zhoda nedokazuje fundamentálnu povahu
paliva. Jeho fyzikálny obsah musí určiť lokálna akcia alebo operátor, nie iba
vhodný priebeh `H(a)`.

### 7.4 Čo sú obyčajná hmota, popol a para?

V živej A1-K1 koľaji sú baryóny konzervované a nevznikajú z
backgroundového transferu. Popol $c$ je tam zhlukujúci CDM kandidát a para
$s$ zamýšľaný relativistický produkt. Model zatiaľ nevie, či tieto tri
zložky vznikajú paralelne, v reťazci alebo cez zmiešané vetvenie. Každá
možnosť musí mať spoločný energeticko-hybnostný ledger a musí prejsť BBN,
CMB, lensingom a rastom štruktúr. Popol sa preto nesmie bez ďalšieho
odvodenia stotožniť s obyčajnou hmotou a termálny comparator sa nesmie
vydávať za odvodenú paru.

### 7.5 Určuje model dnes `H0` a `S8`?

Nie ako tvrdé predikcie. V3.18 obsahuje reprodukovanú odpoveď na užšiu
otázku: ako sa v zmrazenom kotvovom výpočte zmenia dva endpointy, keď
sa zmení vložený príspevok `Delta N_eff`. Tri body v §6.4 dokazujú
numerickú citlivosť tohto modelu. Neurčujú posterior, pravdepodobný interval
ani riešenie Hubbleovej alebo `S8` tenzie. Oddelene od nich v3.18 prijíma
formulation-scoped survival targets `H0≈66.4±0.4 km/s/Mpc` (P04) a
`S8≈0.86–0.87` (P05). Tieto ciele možno vylúčiť iba po úplnej spoločnej
observable mape s neistotami, kovarianciami a systematikami; dnešné tri body
ich samy nepotvrdzujú ani nevyvracajú.

### 7.6 Ako má vzniknúť svetelný kužeľ a Lorentzova symetria?

Grafové šírenie poskytuje sublineárne sa rozširujúci front a auditovaný
skalárny cosine-Laplacian má exaktne párnu disperziu. To odstraňuje lineárny
nepárny člen iba v tomto operátorovom scope. Úplná odpoveď musí ešte odvodiť
rovnaký limitný kužeľ pre fotóny, fermióny a gravitáciu, boostový sektor,
absenciu neprípustnej birefringencie a kompatibilitu s ekvivalenčným
princípom.

### 7.7 Je gravitácia už odvodená zo siete?

Nie. Dve archivované grafové schémy reprodukovali inverse-square
comparator, čo je užitočný mechanistický test. Nie je to odvodenie
Einsteinových rovníc, hodnoty `G`, postnewtonovských limitov, lensingu ani
univerzálneho voľného pádu. Model musí tieto mosty odvodiť skôr, než môže
tvrdiť náhradu alebo mikroskopické vysvetlenie gravitácie.

### 7.8 Vysvetľuje model meranie a šíp času?

Navrhuje fyzickú jazvu alebo doménu I ako nezvratný záznam udalosti bez
výsadnej úlohy vedomia. Presný operátor, ktorý by jedným mechanizmom
produkoval jazvu, kvantový výsledok a termodynamickú šípku času, však chýba.
Ide o otvorenú otázku Q8, nie o vyriešený problém merania.

Tieto odpovede ukazujú hranicu v3.18: model má konkrétny výskumný program a
niekoľko auditovaných matematických mostov, ale ešte nemá jedinú uzavretú
mikrodynamiku, z ktorej by všetky uvedené javy vyplynuli naraz.

## 8. Predikcie a ich dnešný stav

Označenie `P01–P11` je stabilný register predikčných skupín. V3.18 ich číta
predovšetkým ako **podmienky prežitia**. Hodnota alebo okno nemusí byť úplnou
mikrofyzickou vetou, aby bolo vedecky záväzné: výsledok mimo cieľa môže zabiť
presný deklarovaný scope, kým výsledok v cieli ho iba ponechá živý. Zhoda
nie je potvrdením mechanizmu. Celú teóriu zabíja iba `THEORY_LEVEL` rozpor
alebo smrť preukázane úplných top-level alternatív.

Žiadny riadok P01–P11 vo v3.18 zatiaľ nemá certifikovaný dosah
`THEORY_LEVEL`. Pri každom riadku s aktívnym cieľom prežitia však musí
robustne nekompatibilný výsledok po úplnom požadovanom observable teste,
vrátane neistôt, covariance a systematík, vyvolať zapísaný STOP daného scope
alebo, rozhodnutím Martina Jambora, fyzikálne odlišnú novú koľaj; cieľ sa po
výsledku nesmie potichu posunúť.

| ID | Veličina/test | Survival target alebo záväzok | Dosah vylúčenia |
|---|---|---|---|
| `P01` | `N_eff / Delta N_eff` | pri `g_x=2`, `g_*s=106.75`: `Delta N_eff=0.0535`, `N_eff≈3.10` | presná skorá termálna para; širší meraný rozsah ešte treba odvodiť |
| `P02` | skalárny sklon `n_s` | `n_s=0.9656±0.0016`; šírka je cieľové okno, nie neistota odvodená z (28) | presný mechanistický `delta/m=1/2` skalárny mechanizmus po úplnej source-to-observable mape |
| `P03` | tensor-to-scalar ratio `r` | ostrý cieľ `r<1e-10`; samostatný praktický marker `r>=1e-3` | `r>=1e-10` ruší ostrý odhad; `r>=1e-3` zabíja širšiu termálnu realizáciu, nie automaticky celú KBTP |
| `P04` | `H0` | cieľ zmrazenej backgroundovej formulácie `66.4±0.4 km/s/Mpc`; tri auditované body `65.792–66.374` sú samostatná diskrétna diagnostika | presná backgroundová formulácia po úplnom A2/A3 a spoločnej likelihood |
| `P05` | `S8` | cieľ zjednodušenej rastovej formulácie `0.86–0.87`; tri auditované body `0.87450–0.88561` sú iný diagnostický scope | presná rastová formulácia po úplnej CMB/LSS likelihood |
| `P06` | `w0, wa` | `w0=-0.919`, `wa=-0.612` | presná efektívna účtovná/CPL rekonštrukcia po rovnakej projekcii a joint likelihood |
| `P07` | priama detekcia DM/popola | nulová negravitačná detekcia pri odvodenej citlivosti | sterilná identita popola, nie každá možná tmavá hmota |
| `P08` | presný vzťah `n_s-w` | žiadny aktuálny cieľ | odvolaná formula nesmie rozhodovať aktuálne koľaje |
| `P09` | časový drift `delta` | iba benchmark: konštantné `delta=0.02297`; funkcia `delta(a)`/`delta(x)`, aktívny survival target aj číselné kill okno chýbajú | žiadny target-based STOP v nijakom scope, kým nevznikne zákon driftu, observable mapa a predregistrované okno s neistotami, kovarianciami a systematikami |
| `P10` | Lorentzova limita/disperzia | lineárny nepárny koeficient presne nula | auditovaný skalárny cosine-Laplacian operátor |
| `P11` | termálne vlnové pozadie | `T≈0.905 K`, peak `≈53 GHz` spolu s P01 | presná termálna parná formulácia |

Úplné povolené tvrdenie v3.18, dôkazová stopa a povinný nonclaim každého
riadka sú v `02_Prediction_Status_Table_SK.csv`. Zmena predikčnej
tabuľky je release trigger: potvrdené obmedzenie sa nesmie zadržať iba preto,
že ostatné časti teórie ešte čakajú na výpočet.

### 8.1 Predikcia nie je to isté ako podmienka existencie

Nie všetky povinné hodnoty patria do P01–P11. Napríklad
`Σ_A Q_A^mu=0`, nezávislosť `H(a)` od realizovaného Fourierovho módu,
kladnosť fyzických hustôt, zachovanie Einsteinových constraintov, existencia
zdrojovanej prípustnej whole-map a správne rozlíšenie jej nulového alebo
nenulového jadra, existencia jedného globálneho lokálne-prirodzeného bridge
na celej povinnej doméne alebo správny nulový limit sú podmienky existencie
formulácie, nie samostatné observačné predikcie.

Úplný strojovo čitateľný index týchto podmienok je v
`04_Theory_Existence_Conditions_Register_SK.csv`. Jeho riadky
`EC01–EC43` pri každej hodnote alebo exaktnom mantineli rozlišujú:

- či ide o exaktný zákon, otvorený mantinel, mechanistické čítanie,
  kalibračný benchmark alebo observačný survival target;
- aká observable mapa, neistota, covariance a systematika musí predchádzať
  rozsudku;
- či neúspech zasiahne iba formuláciu, celú koľaj alebo potenciálne teóriu;
- ktoré numerické a procesné čísla nemajú fyzikálny death reach.

Žiadny P01–P11 cieľ nie je vo v3.18 automaticky `THEORY_LEVEL`. Naopak,
exaktný zákon nemá voľnú toleranciu, ale jeho zlyhanie v jednej formulácii
nezabíja inú fyzikálne odlišnú alternatívu. Povinné podmienky sa pretínajú
**vnútri** každej top-level koľaje, kým fyzikálne alternatívne koľaje sa
spájajú zjednotením:

$$
\mathcal A_t=\mathcal A_{{\rm exact},t}\cap
\mathcal A_{{\rm obs},t}\cap\bigcap_i f_{i,t}^{-1}(\mathcal A_{i,t}),
\qquad
\mathcal A_{\rm theory}=\bigcup_{t\in\mathcal T_{\rm top}}\mathcal A_t.
$$

Celá KBTP zomiera v kontrolovanom scope iba vtedy, keď je zoznam
$\mathcal T_{\rm top}$ preukázane úplný a pre každú jeho koľaj platí
$\mathcal A_t=\varnothing$. Prienik navzájom výlučných koľají sa na tento
rozsudok nesmie použiť.

## 9. Mapa staníc, koľají a vedeckého progresu

### 9.1 Ako čítať kontrolné stanice a koľaje (`A1-K1 -> A2-K4 -> A3`)

`A1`, `A2` a `A3` sú stabilné identifikátory **kontrolných staníc**
(`verification stations`). `K1`, `K4` a ďalšie `K` sú **koľaje**
(`tracks`) skúšané na danej stanici. Označenia sa spätne nemenia na `S1`
alebo `T1`: `S1` už označuje auditný nález opraviteľný v rovnakej koľaji a
`T1` technický nález bez dosahu na tvrdenie. Premenovanie by preto vytvorilo
kolíziu a porušilo odkazy na staršie dôkazy.

Hĺbka `60/100` neznamená 60 % pravdepodobnosť pravdivosti. Znamená, že
`A2-K4` prešla fyzikálnymi bránami s kumulatívnou váhou 60 bodov. Otvorené
brány sa nepočítajú ako úspech a historická technická hĺbka redukovaného
K7 runnera `66.5/100` sa do fyzikálneho skóre neprenáša.

### 9.2 Čo bolo na trase skutočne odvodené

Každý nasledujúci bod uvádza rovnicu, význam symbolov a presný dosah. Tam,
kde existuje materiálne zodpovedajúci zapečatený externý balík, je pripojený
konkrétny odkaz na zamýšľaný nemenný Git tag `v3.18`. Neprítomnosť odkazu
znamená, že pri obsahovom cut-offe neexistoval kanonický externý balík pre
daný vzorec; neznamená automaticky neprítomnosť interného pracovného dôkazu.

#### Homogénny energetický ledger (`A1-K1`)

Prijatý backgroundový krok je sústava (15) spolu s

$$
\boxed{Q_f+Q_c=0}.
\tag{29}
$$

$Q_f$ a $Q_c$ sú iba homogénne skalárne zdroje paliva a popola. Výsledok
preukazuje energetickú kanceláciu na pozadí, nie priestorové zložky
$Q_A^{\mu}$, momentum closure ani gauge mapu $\delta Q_A$.

**Auditná hranica:** interný backgroundový decision record zostáva v
pracovnom evidence archíve. V tomto vydaní pre rovnicu (29) neexistuje
materiálne zodpovedajúci kanonický externý balík; rovnica uzatvára iba
homogénnu energiu v deklarovanom scope.

#### Univerzálna normalizácia backgroundu (`A1-K1`)

Rovnice (20)–(22) zabezpečujú

$$
\boxed{\Phi(k)z^p=A_fa^p},
\qquad
A_f=7809.270101963506.
\tag{30}
$$

Všetky symboly sú definované pri rovniciach (17)–(22). Fyzický význam je, že
jedna FLRW expanzia nesmie závisieť od zvoleného Fourierovho módu. $A_f$ je
podmienené parameter-bookkeeping číslo, nie mikroskopická konštanta.

**Externá auditná stopa:** rovnakú normalizačnú identitu a jej podmienené
číselné vyhodnotenie pokrýva
[zapečatený balík EA-004](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/PACKAGES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/00_SCOPE_AND_READ_ORDER.md).
Balík neauditoval CLASS/CAMB, úplné poruchy, CMB ani $S_8$.

#### Definícia fyzikálnej koľaje (`A2-K4`)

Koľaj viaže transfer na spoločný energetický rámec popola a paliva:

$$
\boxed{
\theta_d=
\frac{\rho_c\theta_c+\delta\rho_f\theta_f}
     {\rho_c+\delta\rho_f}
},
\qquad
\boxed{
Q_f^{\mu}=-\Gamma\rho_fu_d^{\mu}=-Q_c^{\mu}
}.
\tag{31}
$$

**Symboly:** $\theta_c,\theta_f,\theta_d$ sú divergencie rýchlosti popola,
paliva a spoločného energetického rámca; $u_d^{\mu}$ je jeho štvor-rýchlosť;
$\Gamma=\lambda H_0$ efektívna transferová miera zmrazeného benchmarku
opísaného v §5.1. Menovateľ je efektívna
inerciálna hustota dvojice.

**Mainstream a rozdiel:** kovariantné interagujúce fluidy sú štandardný
formalizmus. KBTP-špecifická je voľba energetického rámca a tvrdenie, že ten
istý lokálny proces má produkovať popol. Rovnica (31) definuje identitu
koľaje, ale ešte nie úplný produkčný operátor.

**Auditná hranica:** route plán rovnice (31) zostáva v internom pracovnom
archíve a nie je potrebný na jej pochopenie ani citovanie. V tomto vydaní
pre rovnicu (31) neexistuje materiálne zodpovedajúci kanonický externý
balík.

#### Oprava falošnej smrti (`M-011`)

$$
\boxed{\ln T_{K4}=0.462<1}.
\tag{32}
$$

$T_{K4}$ je absolútny transfer normy skúmaného módu. Staré číslo `11.5901`
bolo relatívnym ziskom voči takmer nulovej vetve $\Gamma=0$, nie dôkazom
absolútnej explózie. Oprava ruší iba starý dôvod smrti; sama koľaji neudeľuje
PASS.

**Auditná hranica:** interný erratum audit zostáva v pracovnom evidence
archíve. V tomto vydaní pre rovnicu (32) neexistuje materiálne
zodpovedajúci kanonický externý balík; oprava falošného dôvodu smrti preto
nie je externý PASS koľaje.

#### Regulárna superhorizontová báza (`A2-K4.1`, `G5`)

Pre lokálny indiciálny exponent $s$ má charakteristický polynóm tvar

$$
\boxed{
\mathcal P_{\rm SH}(s)=
s^3(s+2)^2(s+3)
\left[s^2+(5-3\delta)s+12-6\delta\right]
}.
\tag{33}
$$

Nulový koreň má násobnosť tri, čo v presnom perfect-radiation scope dáva tri
regulárne superhorizontové módy. $s$ je tu lokálny indiciálny exponent a
nesmie sa zamieňať s backgroundovým exponentom $p$ z rovnice (19).

Historický seed mal projekčný reziduál `0.978949...`, preto tento výsledok
neoprávňuje použiť starý seed. Historický checkpoint bol `55/100`, kanonicky
G5=`50/100`.

**Auditná hranica:** interné skripty a audit tohto kroku zostávajú v
pracovnom evidence archíve. V tomto vydaní pre rovnicu (33) neexistuje
materiálne zodpovedajúci kanonický externý balík, preto sa tu nevytvára
zavádzajúci package odkaz.

#### Vysokofrekvenčný principal symbol (`A2-K4.2`, `G6`)

$$
\boxed{
\mathcal P_{\rm high-k}(\mu)
=\mu^4(\mu^2+1)\left(\mu^2+\frac13\right)
}.
\tag{34}
$$

$\mu$ je bezrozmerná charakteristická frekvencia/rastový exponent principal
symbolu. Korene zodpovedajú nulovým módom a oscilujúcim rýchlostiam $1$ a
$1/\sqrt3$; v deklarovanom efektívnom scope sa neobjavil K4-špecifický
exponenciálne rastúci high-$k$ koreň. Nie je to úplná no-ghost veta ani
dôkaz fundamentálnej silnej hyperbolicity dust sektora.

Historický checkpoint bol `59/100`; po rekalibrácii je kanonicky G6=`60/100`.

**Auditná hranica:** interné skripty a audit principal symbolu zostávajú v
pracovnom evidence archíve. V tomto vydaní pre rovnicu (34) neexistuje
materiálne zodpovedajúci kanonický externý balík; výsledok sa preto nesmie
rozšíriť na úplnú no-ghost alebo globálnu hyperbolicitu.

#### Druhový a anisotropický ledger (`A2-K4.3a`)

$$
\boxed{
\sum_A Q_A^{\mu}=0,
\qquad
\Phi\neq\Psi\ \text{je povolené}
}.
\tag{35}
$$

$A$ prechádza cez deklarované druhy $c,f,b,\gamma,\nu,s$, kde $s$ označuje
paru; $\Phi,\Psi$
sú dva skalárne metrické potenciály. Algebraická brána oddelila druhy,
zachovala anisotropický stress, Thomsonovu kanceláciu hybnosti a
perfect-radiation nulový limit. Nevykonala plnú dynamickú evolúciu a
zachovala `60/100` bez zmeny skóre.

**Auditná hranica:** interný algebraický skript a audit zostávajú v pracovnom
evidence archíve. V tomto vydaní pre rovnice (35)–(36) neexistuje materiálne
zodpovedajúci kanonický externý balík; statické algebraické nuly sa preto
nesmú prezentovať ako externe reprodukovaná dynamická evolúcia.

#### Statický rámec a Einsteinove constrainty (`P5.1-P5.2`)

$$
\boxed{
U_d=(1-\beta)U_c+\beta U_f,
\qquad
\beta=\frac{\delta r}{1+\delta r}
},
\tag{36}
$$

$$
\boxed{
R_{00}=R_{0i}=R_{\rm tr}=R_{\rm tl}=0
}.
\tag{37}
$$

$U_c,U_f,U_d$ sú bezrozmerné rýchlostné/hybnostné premenné; $r=\rho_f/\rho_c$
a $\beta$ entalpická váha paliva. $R_{00},R_{0i},R_{\rm tr},R_{\rm tl}$ sú
rezíduá energetického, hybnostného, trace a traceless Einsteinovho ledgera.
Presné nuly dokazujú statickú algebraickú rekonštrukciu, nie zachovanie
constraintov počas evolúcie.

**Auditná hranica:** interné ledger skripty, výsledok a route plán zostávajú
v pracovnom evidence archíve. V tomto vydaní pre rovnice (36)–(37)
neexistuje materiálne zodpovedajúci kanonický externý balík. Dnešné tvrdenie
je preto presne statické a nie je externou reprodukciou evolučného
zachovania constraintov.

#### Planárna Landauova prípustná oblasť (`EC42`)

V interface-adapted $1+1$ ortonormálnom rámci označme
$E=T^{(00)}$, $q=T^{(0n)}$, $P_n=T^{(nn)}$ a $S=E+P_n$. Pre nenulový tok
má pravidelná planárna Landauova vetva presnú prípustnú podmienku a stabilne
racionalizovaný koreň

$$
\boxed{
q\neq0:\quad |S|>2|q|,
\qquad
v_L=\frac{2q}{S+\operatorname{sgn}(S)\sqrt{S^2-4q^2}}
},
\tag{37a}
$$

zatiaľ čo nulová vetva vyžaduje

$$
\boxed{q=0:\quad S\neq0,\qquad v_L=0}.
\tag{37b}
$$

**Symboly:** $T^{(ab)}$ sú zložky úplného stress-energy tenzora v lokálnom
rámci, $q$ normálový energetický tok a $P_n$ normálový tlak. V rovniciach
(37a)–(37b) je $v_L\equiv\beta_L$ bezrozmerný Landauov boost parameter v
jednotkách $c=1$; zodpovedajúca fyzická normálová rýchlosť je $c\,v_L$.
Okrem uvedených nerovností zostávajú povinné Type-I
klasifikácia, jednoduchý časupodobný vlastný smer, priečna nedegenerovanosť,
budúca orientácia a hladké okolie.

**Stav v3.18:** `ACCEPTED_RANGE_ONLY`. Výsledok určuje presný algebraický
rozsah Q1R6 midpoint source packetu na pravidelnej Landauovej doméne. Nie je
to `LANDAU_PASS`, dôkaz fyzicky neprázdneho alebo prázdneho rozsahu ani veta
o dynamickej stabilite. Chýbajúci úplný $Z_0$, owner, current, reservoir a
ďalšie guardy nezabíjajú A2-K4.

#### Evidenčné pokrytie, logická úplnosť a dnešný blocker (`P5.3`)

$$
\boxed{C2=10/10},
\qquad
\boxed{C3=45/45}.
\tag{38}
$$

C2 počíta pokrytie desiatich registrovaných seed atómov a C3 logickú maticu
45 kontrol. Ani jedno číslo nie je fyzický seed witness. C2 má zapečatený
reprodukčný kapsul, ale jeho externá odpoveď nebola pri obsahovom cut-offe
dokončená. Externý T2 audit overil iba logický agregát C3, nie pôvodné
fyzikálne solvery.

**Externá auditná stopa:** pre C2 je dostupný
[zapečatený balík EA-029](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/PACKAGES/EA-20260719-029-KMPC127-C2-AUTHORITATIVE-AGGREGATE/00_SCOPE_AND_READ_ORDER.md),
no nejde o dokončené externé potvrdenie. Pre C3 sú dostupné
[zapečatený balík EA-039](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/PACKAGES/EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE/00_SCOPE_AND_READ_ORDER.md),
[externá T2 odpoveď](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/RESPONSES/EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE/00_AUDITOR_AUDIT.md)
a
[projektové posúdenie](https://github.com/jambormartinsvk-netizen/cellular-universe/blob/v3.18/External_Audits/RESPONSES/EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE/01_MAIN_ORCHESTRATOR_ASSESSMENT_2026-07-22.md).
Tieto balíky auditujú agregáciu a registre, nie fyziku jednotlivých seed
atómov; $C2=10/10$ ani $C3=45/45$ preto nie sú fyzikálny witness.

Po zostavení chýbajúcich vstupov má whole-map diskriminačná rodina tvar

$$
\boxed{
\mathcal A_K(Z)=\left\{(Q,X,\ker X):
Q\in\mathcal A_Q(Z),\ X\in\mathcal A_X(Z,Q)\right\}
}.
\tag{39}
$$

$\mathcal A_Q(Z)$ obsahuje iba úplné, prekryvy riešiace quotienty
$Q_Z=V_{\rm raw}(Z)/V_{\rm rel}(Z)$. $\mathcal A_X(Z,Q)$ obsahuje lineárne
tangent-map generátory $X_Z:Q_Z\to\Gamma(TW_{\rm pc})$, ktoré sú zdrojované
prijatou fyzikou a spĺňajú linearitu, lokálnosť/lokálnu prirodzenosť,
kovarianciu, jednotky, causal support, smoothness, prijatú generator
provenienciu a zostup cez $V_{\rm rel}$. Definícia týchto rodín sama
nedokazuje, že majú člena; treba konkrétny zdrojovaný prvok alebo existenčnú
vetu.

Iba pre certifikovaný $Q$ a zdrojované $X$ sa definuje
$K_{\rm all}(X)=\ker X$. Každé jadro lineárnej mapy obsahuje nulu, takže
samotná neprázdnosť jadra nie je test. Relevantné vetvy sú
$\ker X=\{0\}$ a existencia nenulového fyzického kernel witnessu. Nenulový
witness vylučuje presný scope `PK1/I0`; injektivita povoľuje iba prechod k
pevnému rezíduu $E_N$ a ďalším bránam. Zmiešaná úplná rodina bez výberu
actual mapy ostáva `WAITING`. Táto per-state tangent-map klasifikácia sama
nie je dôkazom jedného globálneho lokálne-prirodzeného operátora. Dnes nie
je certifikovaný ani úplný $Q_Z$, ani člen $\mathcal A_X$; stav
`10 WAITING / 0 EXCLUDED` preto nie je witness ani no-go.
Ako current claims platia iba prijaté opravené
nástupnícke tvrdenia uvedené v tomto dokumente a v priložených release
súboroch `02` a `03`. Staršie superseded alebo karantenizované dosahy ostávajú
historickou auditnou stopou, nie súčasným tvrdením v3.18.
Pre tento najnovší bod ešte neexistuje canonical sealed externý balík.

### 9.3 Aktuálny stav koľají

Koľaj je presne pomenovaná fyzikálna možnosť. Uchováva vlastné predpoklady,
rovnice, výpočty a dôvod rozhodnutia. `STOP_SCOPE` preto označuje smrť
konkrétnej testovanej triedy, nie automaticky všetkých príbuzných
mechanizmov.

| Koľaj | Stav v3.18 | Presný význam |
|---|---|---|
| `A1-K1` | `LIVE / CONDITIONED` | prijatý backgroundový kandidát; čaká na úplnú A2 koľaj |
| `A2-K1` | `STOP_SCOPE M-009 / SCIENTIFIC` | zomrel presný fluidný scope; nový mechanizmus by bol novou koľajou |
| `A2-K2` | `STOP_SCOPE M-008 / SCIENTIFIC` | zomrela skúmaná barotropická trieda |
| `A2-K3` | `STOP_SCOPE M-010 / SCIENTIFIC` | zomrel presný prenosový scope |
| `A2-K4` | `LIVE_ACTIVE / 60/100` | hlavná koľaj; fyzický produkčno-transportný operátor a úplný seed chýbajú |
| `A2-K5` | `STOP_SCOPE M-012 / SCIENTIFIC` | zomrela konkrétna konformná akcia |
| `A2-K6` | `STOP_SCOPE M-013 / SCIENTIFIC` | zomrel zdravý interval daného operátora |
| `A2-K7` | `LIVE_BACKUP / WAITING` | potrebuje pozitívny lokálny kernel prenosu, disipácie, noise a memory |
| `A2-K8` | `LIVE_BACKUP / WAITING` | potrebuje explicitný relaxačný/collision operátor |
| `A2-K9` | `LIVE_BACKUP / WAITING` | potrebuje spoločný produkčno-transportný operátor bez druhého fitu |
| `A2-K11` | `LIVE_BACKUP / WAITING` | potrebuje odvodený regulárny ortogonálny operátor a multispecies DAE |
| `A2-K12` | `LIVE_BACKUP / WAITING` | potrebuje párový kernel, momentum ledger a stabilný separation mód |
| `A2-K10` | `SEPARATE_ROUTE / NOT_AUTHORIZED` | patrí pod inú backgroundovú koľaj A1-K2 |
| `A3` | `BLOCKED_BY_NO_COMPLETE_A2_GATE` | výpočtová implementácia a fit dát nie sú autorizované ako fyzikálny výsledok |
| `A4` | `NOT_PASSED / OPEN` | para, exit a reliktný sektor nemajú odvodený lokálny zdroj $C_s$ (historicky `C_g`), časovanie ani entropický ledger |

`STOP_SCOPE` nie je tvrdenie, že neexistuje žiadna príbuzná fyzika. Mŕtva
koľaj, jej rovnice, skripty, výpočty a dôvod sa nemažú. Nová koľaj musí
explicitne odstrániť konkrétnu príčinu smrti a vysvetliť rozdiel.

### 9.4 Presný blocker A2-K4 pri hĺbke `60/100`

Aktuálny P5.3 test má tri presne zoradené objekty:

1. `N1`: úplný, prekryvy riešiaci fyzický quotient `Q_Z` alebo dokázane
   neprázdna úplná rodina $\mathcal A_Q(Z)$;
2. `N2`: jedna fyzicky zdrojovaná actual whole-map `X_Z`, alebo dokázane
   neprázdna P1–P2 úplná rodina $\mathcal A_X(Z,Q)$; formálny zoznam guardov
   sám nie je existenčný dôkaz;
3. `N3`: až potom whole-map klasifikácia: $\ker X=\{0\}$, nenulový fyzický
   kernel witness, alebo pri úplnej rodine univerzálna injektivita,
   univerzálna neinjaktivita či dokázane zmiešaný rozsah. `W1-W4` môže
   nahradiť priamu whole-map analýzu iba pri úplnom prekryvovom a
   image-independence dôkaze.

Ak chýba N1, stav je `N1_WAITING` bez kernel inference. Ak chýba člen N2,
stav je `N2/N3_ACTUAL_MAP_OR_COMPLETE_FAMILY_WAITING`. Zmiešaná rodina bez
výberu actual mapy zostáva `N3_RANGE_MIXED_LIVE_WAITING`. Nenulový fyzický
prvok jadra vylučuje iba presný scope `PK1/I0`; whole-map injektivita povoľuje
iba pokračovať k pevnému rezíduu $E_N=0$ a ďalším owner/power/reservoir
bránam — sama nie je existenčný dôkaz globálneho zákona ani PASS A2-K4.
P5.3 sa uzavrie až po neskoršom global local-natural bridge dôkaze. Kým tieto
objekty a potomkovia chýbajú, stav je `LIVE / WAITING`, nie PASS ani STOP.
Nález
`10 waiting / 0 excluded` znamená, že dnešné mantinely žiadnu z desiatich
tried nezabili, ale ani nepreukázali existenciu fyzikálne prípustnej funkcie.

### 9.5 Čo ešte treba splniť do kontrolnej stanice A3

1. **Dokončiť P5.3:** nájsť fyzický witness spoločného lokálneho
   produkčno-transportného zákona alebo exaktný no-go; uzavrieť source,
   current, owner, power, reservoir a globálny bridge bez kruhovej definície.
2. **Prejsť P5.4:** odvodiť a otestovať úplné species-first kontinuity a
   Eulerove rovnice, dynamické Einsteinove constrainty, linearitu, dva
   nezávislé štarty a krokovú/tolerančnú konvergenciu.
3. **Uzavrieť globálnu bránu G7:** spojiť P5.4 s plnou fotónovou a
   neutrínovou hierarchiou, presným background adapterom, fyzickými
   transfermi, nezávislým alebo gauge cross-checkom a konvergenciou v `lmax`
   aj numerickej metóde. P5.4 a hierarchia spolu tvoria jeden úplný
   Einsteinov–Boltzmannov bridge; nesmú dostať dvojité skóre.
4. **Zmraziť route-local A2 fyziku pred dátami:** uzavrieť pred-A3 transferový
   a observačný passport bez dodatočného ladenia operátora podľa výsledku.
   Tento krok je vstupná hranica, nie ešte nezávislý CLASS/CAMB release claim.
5. **A3-M1 až A3-M6:** po uzavretí G7 v presne zmrazenej verzii CLASS/CAMB
   nezávisle implementovať a reprodukovať celý prijatý A2 operátor a jeho
   štandardný nulový limit. Globálna `G8` potom počíta CMB-normalizované
   spektrá a rast vrátane `sigma8/S8` a `H0`; `G9` vykoná spoločnú likelihood
   a porovnanie s dátami. A3 nesmie spätne meniť A2 operátor.

V historickom jemnom registri znamená `C7-G8` plnú hierarchiu a `C7-G9`
CMB/`S8` likelihood. V kanonickom globálnom pase v3.18 však `G7` označuje
celý Einsteinov–Boltzmannov bridge, `G8` CMB-normalizované spektrá a rast a
`G9` spoločnú likelihood. Preto sa pri historických výsledkoch vždy používa
úplný prefix; holé `G8` bez namespace nie je jednoznačný dôkazový odkaz.

## 10. Otvorené fundamentálne otázky

Najvyššiu prioritu majú:

1. `Q4`: mikroskopický vzťah zlyhania, jazvy a malého čísla `epsilon`;
2. `Q8`: či doména I môže jedným exaktným mechanizmom niesť ireverzibilnú
   jazvu, kolaps a šíp času;
3. `Q18/Q23`: zdroj pary, koniec éry paliva, reheating, entropia a BBN;
4. `Q20`: úplný gauge-invariantný systém interagujúcich porúch;
5. `Q22`: pôvod `zeta`, `P_zeta`, `A_s`, `n_s`, runningu, izokurvatúr a
   bispektra z jedného systému;
6. `Q24/Q25`: 4D Lorentzova limita alebo preferovaný rámec, spoločná metrika
   všetkých polí a ekvivalenčný princíp;
7. `Q29`: druhý zákon pre všetky zásobníky;
8. `Q31/Q32`: particle model popola a kontinuálna limita gravitácie.

Úplný register Q1–Q34 a metodické pravidlá sú súčasťou tohto vydania v
`03_Methodology_and_Question_Register_SK.md`.

## 11. Čo v3.18 priznáva a čo netvrdí

Súčasný snapshot priznáva:

- zákon $Q_f=-Q_c=-\Gamma\rho_f$ je skúmaná efektívna rodina a
  $\lambda=\Gamma/H_0$ jej bezrozmerná parametrizácia; antisymetria zdrojov
  uzatvára homogénny účet, ale mikrodynamika neurčila ani $\Gamma$, ani
  jedinečnú číselnú hodnotu $\lambda$;
- `lambda=0.15` je zmrazený historicky dátami vybraný benchmark aktívnej
  koľaje, nie jediná dovolená ani z prvých princípov odvodená hodnota;
  samostatne skúmané body `0.10` a `0.15` ešte nevymedzujú certifikovaný
  súvislý interval platnosti;
- podmienená backgroundová normalizácia
  `A_f=7809.270101963506` je odvodená zo zmrazeného A1-K1 closure bez
  ďalšieho fitu, ale jej mikrofyzický pôvod, P2b a exact-background
  perturbatívne preodvodenie nie sú uzavreté;
- `C=28` a `m=1/2` sú mechanistické čítania, nie vety;
- gaussovskosť, doména I, reheating a kontinuálna kvantová/gravitačná limita
  sú otvorené;
- aktuálna teória nemá plný CMB/LSS likelihood ani jednu dokončenú A2
  koľaj.
- v3.18 zachováva iba výslovne označené podmienené alebo formuláciou
  obmedzené hodnoty ako survival targets s presným death reachom; `P08` je
  `WITHDRAWN` a `P09` iba benchmark bez aktívneho cieľa či target-based STOP;
  zhoda znamená nanajvýš prežitie deklarovaného scope, nie experimentálne
  potvrdenie;

Súčasný snapshot netvrdí:

- experimentálne potvrdenie bunkovej ontológie;
- dokončenie A2-K4, globálnych brán `G7`, `G8`, `G9` ani vstup do A3 alebo
  A4;
- lepší globálny fit než ΛCDM;
- vyriešenie Hubbleovej alebo `S8` tenzie;
- posterior alebo theory-level tvrdú hodnotu `H0`, `S8`, `Delta N_eff`,
  `n_s`, `r`, `w0` alebo `wa` bez podmienok a death scope uvedených v §8;
- úplnú Lorentzovu invarianciu, ekvivalenčný princíp alebo absenciu piatej
  sily;
- odvodenú mikrofyziku hmoty, pary, popola, kolapsu alebo šípu času.

## 12. Falzifikácia a ďalší postup

Fyzikálna funkcia alebo kernel sa najprv vedie ako prípustná množina.
Exact zákony sa uplatňujú bez tolerancie; merané hranice iba cez explicitnú
model-to-observable mapu, neistoty a covariance. Koľaj zomiera až po dôkaze,
že jej presná prípustná množina je prázdna. Teória zomiera v kontrolovanom
scope až vtedy, keď je v každej koľaji prázdny prienik jej povinných
mantinelov a všetky koľaje preukázane úplného top-level zoznamu zomreli.

Ak sa BBN/CMB alebo iné meranie použije na rekonštrukciu $C_s$, branchingu
alebo $delta(a)$, je kalibračným dátovým vstupom a nesmie sa druhýkrát
započítať ako nezávislé potvrdenie. V súčasnej existenčnej fáze môžu všetky
dáta tvoriť mantinely; úspech potom dokazuje iba observačne kompatibilného
svedka. Predikčná sila vyžaduje out-of-sample observablu alebo vstupy
zafixované bunkovou mikrodynamikou.

Najbližší vedecký cieľ nie je nový fit. Je ním explicitný lokálny,
kovariantný a konzervačný svedok pre produkciu a postupnosť hmoty, pary a
popola, ktorý:

- dá jeden módovo nezávislý background `H(a)`;
- uzavrie prenos energie aj hybnosti;
- prejde superhorizontálnou a subhorizontálnou stabilitou;
- poskytne úplný seed pre P5.4 a následné uzavretie globálneho
  Einsteinovho–Boltzmannovho bridge `G7`;
- až následne umožní CMB/LSS likelihood a nové predikčné intervaly.

---

## 13. Citačná hranica

Tento dokument sa musí citovať spolu s jeho verziou a dôkazovým štítkom.
Podmienené číslo bez vstupov a nonclaims nie je tá istá vedecká veta.
DOI celého vydania je `10.5281/zenodo.21915608`.
Release v3.18 je platný iba ako presný manifestom a Git commitom/tagom
viazaný payload; samostatný draft súbor nie je publikované vydanie.

---

## 14. Register použitých skratiek a interných označení

Register rozbaľuje skratky a stabilné kódy, ktoré sa objavujú vo výkladovom
texte, tabuľkách a mape vedeckej cesty. Matematické symboly sú úplne
definované pri príslušných rovniciach; nižšie sú zopakované iba tie, ktoré sa
používajú aj ako zaužívané názvy pozorovateľných veličín. Názvy súborov,
SHA-256 odtlačky a jednorazové identifikátory auditných balíkov nie sú
fyzikálne skratky a register ich nerozpisuje.

### 14.1 Fyzika, kozmológia a pozorovania

| Skratka | Plný názov a význam v tomto dokumente |
|---|---|
| `BAO` | *baryon acoustic oscillations* — baryónové akustické oscilácie |
| `BBN` | *Big Bang nucleosynthesis* — nukleosyntéza veľkého tresku |
| `CAMB` | *Code for Anisotropies in the Microwave Background* — verejný Boltzmannov kód pre kozmologické poruchy a anizotropie |
| `CDM` | *cold dark matter* — studená tmavá hmota |
| `CLASS` | *Cosmic Linear Anisotropy Solving System* — verejný Boltzmannov kód pre kozmologické poruchy a pozorovateľné veličiny |
| `CMB` | *cosmic microwave background* — kozmické mikrovlnné pozadie |
| `CPL` | Chevallierov–Polarskiho–Linderov dvojparametrový zápis $w(a)=w_0+w_a(1-a)$ |
| `DAE` | *differential-algebraic equation/system* — diferenciálno-algebraická rovnica alebo sústava |
| `DE` | *dark energy* — tmavá energia; vyskytuje sa najmä v dolnom indexe $\rho_{\rm DE,eff}$ |
| `DM` | *dark matter* — tmavá hmota všeobecne |
| `EW` | *electroweak* — elektroslabý sektor Štandardného modelu |
| `FEM` | *finite element method* — metóda konečných prvkov; tu názov jednej archivovanej schémy grafových váh |
| `FLRW` | Friedmannova–Lemaîtrova–Robertsonova–Walkerova homogénna a izotropná kozmologická geometria |
| `GR` | *general relativity* — všeobecná teória relativity |
| `GW` | *gravitational waves* — gravitačné vlny; napríklad $c_{\rm GW}$ je ich limitná rýchlosť |
| `KBTP` | Kvantová bunková teória priestoru — pracovný názov tejto teórie |
| `KiDS` | *Kilo-Degree Survey* — observačný prieskum slabého gravitačného šošovkovania |
| `KPZ` | Kardarova–Parisiho–Zhangova trieda rastu a zdrsňovania rozhraní |
| `LSS` | *large-scale structure* — veľkoškálová štruktúra vesmíru |
| `NIV` | *neutrino isocurvature velocity* — neutrínový izokurvatúrny rýchlostný počiatočný mód |
| `PPN` | *parameterized post-Newtonian* — parametrizovaný postnewtonovský formalizmus/testy slabej gravitácie |
| `QFT` | *quantum field theory* — kvantová teória poľa |
| `SH` | *superhorizon* — superhorizontový režim; používa sa napríklad v $\mathcal P_{\rm SH}$ |
| `SH0ES` | *Supernovae and H0 for the Equation of State of dark energy* — program lokálneho merania $H_0$ pomocou rebríka vzdialeností |
| `ΛCDM` | *Lambda cold dark matter* — štandardný kozmologický model s kozmologickou konštantou $\Lambda$ a studenou tmavou hmotou; `LCDM` v názve premennej je iba ASCII zápis toho istého názvu |

### 14.2 Numerika, dátové formáty a jednotky

| Skratka alebo zápis | Plný názov a význam |
|---|---|
| `ASCII` | *American Standard Code for Information Interchange*; v tomto dokumente označuje textový zápis bez gréckeho znaku, napríklad `LCDM` namiesto `ΛCDM` |
| `CSV` | *comma-separated values* — textový tabuľkový formát použitý pre registre predikcií a podmienok existencie |
| `DOP853` | explicitná vysoko-rádová Rungeho–Kuttova integračná metóda s vloženými rádmi 8/5/3 |
| `ID` | *identifier* — stabilný identifikátor riadka, otázky, predikcie alebo koľaje |
| `RMS` | *root mean square* — kvadratický priemer použitý pri definícii amplitúdy $\sigma_8$ |
| `RK4` | klasická explicitná Rungeho–Kuttova metóda štvrtého rádu |
| `SHA-256` | *Secure Hash Algorithm 256-bit* — kontrolný odtlačok presných bajtov artefaktu; nie fyzikálna veličina |
| `GHz` | gigahertz, $10^9\,\mathrm{Hz}$ |
| `Hz` | hertz, počet cyklov za sekundu |
| `K` | kelvin, jednotka termodynamickej teploty; v spojeniach `K1`, `K4` však znamená koľaj, nie kelvin |
| `Mpc` | megaparsek |
| `km/s/Mpc` | kilometre za sekundu na megaparsek; jednotka Hubbleovej konštanty, typograficky $\mathrm{km\,s^{-1}\,Mpc^{-1}}$ |
| `K_MPC` | historický názov premennej runnera s hodnotou $0.05\,\mathrm{Mpc}^{-1}$; v prijatej proveniencii je to pevne vložená hodnota perturbatívneho Fourierovho $k$; spojenie s Planckovým pivotom je iba plausibilná konvencia, nie doložený úmysel zdrojového kódu; nie je to fundamentálna škála siete ani rýchlosť popola |

### 14.3 Najčastejšie označenia pozorovateľných veličín

| Zápis | Význam |
|---|---|
| $A_s$ | amplitúda primordiálneho skalárneho spektra pri určenej pivotnej škále |
| $H_0$ alebo `H0` | dnešná Hubbleova konštanta |
| $N_{\rm eff}$ | efektívny počet relativistických druhov |
| $\Delta N_{\rm eff}$ alebo `Delta N_eff` | prírastok $N_{\rm eff}$ oproti zvolenej štandardnej referencii |
| $n_s$ | spektrálny index primordiálnych skalárnych porúch |
| $\mathcal P_\zeta$ alebo `P_zeta` | výkonové spektrum komovovej krivostnej poruchy $\zeta$ |
| $r$ | tensorovo-skalárny pomer; pri rovnici (36) je rovnaké písmeno lokálne nanovo definované ako $\rho_f/\rho_c$ |
| $S_8$ alebo `S8` | kombinácia amplitúdy zhlukovania a hustoty hmoty definovaná pri rovnici (25) |
| $\sigma_8$ alebo `sigma8` | lineárna RMS amplitúda hmotových fluktuácií vyhladených na škále $8\,h^{-1}\,\mathrm{Mpc}$ |
| $w_0,w_a$ | dvojica parametrov časovo závislej efektívnej stavovej rovnice tmavej energie |

### 14.4 Stanice, koľaje, brány a registre projektu

| Kód | Význam |
|---|---|
| `A1` | kontrolná stanica homogénneho kozmologického pozadia a jeho bilančnej konzistencie |
| `A2` | kontrolná stanica úplných lineárnych porúch, kovariancie, constraintov a stability |
| `A3` | kontrolná stanica nezávislej implementácie prijatého A2 operátora v CLASS/CAMB a porovnania s dátami |
| `A4` | otvorená kontrolná stanica zdroja pary, ukončenia palivovej éry, reheatingu, reliktného sektora a entropického účtu |
| `K1`, `K2`, … | číslo fyzikálnej koľaje, teda alternatívneho mechanizmu skúšaného na danej stanici; napríklad `A2-K4` je štvrtá koľaj stanice A2 |
| `A1-K1 -> A2-K4 -> A3` | aktuálna hlavná cesta: podmienený background, živá poruchová koľaj a budúca nezávislá implementácia |
| `V1` | prvá verzia efektívneho backgroundového ledgera v §5.1; nejde o verziu celého vydania |
| `G5` | brána regulárnej superhorizontovej bázy A2-K4 |
| `G6` | brána vysokofrekvenčného/subhorizontového principal symbolu A2-K4 |
| `G7/G8/G9` | v kanonickom globálnom pase postupne: úplný Einsteinov–Boltzmannov bridge vrátane species-first dynamiky, hierarchie, fyzických transferov a cross-checkov; CMB-normalizované spektrá a rast; spoločná likelihood a porovnanie s dátami. Vždy treba uviesť namespace, lebo historické `C7-G8` a `C7-G9` označujú plnú hierarchiu a likelihood |
| `C7` | historický jemný namespace série poruchových kontrol; samostatné číslo bez nasledujúcej brány nie je dôkazový výsledok |
| `P01–P11` | stabilné identifikátory jedenástich predikčných skupín v §8 a v CSV registri |
| `EC01–EC43` | *existence conditions* — stabilné identifikátory exaktných zákonov, otvorených mantinelov, benchmarkov, predikčných väzieb a vylúčených procesných čísel v dokumente `04` |
| `Q1–Q34` | stabilné identifikátory otázok v metodickom registri |
| `Q8-K1` | prvá skúmaná koľaj pod otázkou Q8; rovnaké skladanie prefixov sa používa aj pri ďalších route-local adresách |
| `P2b` | otvorený route-local krok mikrofyzického pôvodu a normalizácie $A_f$; nie hotová fyzikálna brána |
| `P5.1` | statická rekonštrukcia spoločného energetického rámca A2-K4 |
| `P5.2` | statický úplný Einsteinov constraint ledger A2-K4 |
| `P5.3` | existenčná brána spoločného lokálneho produkčno-transportného zákona |
| `P5.4` | budúca dynamická species-first evolúcia po získaní fyzického witnessu P5.3 |
| `C2` | pokrytie desiatich registrovaných seed atómov; `10/10` je evidenčná úplnosť, nie fyzický witness |
| `C3` | logická matica 45 kontrol; `45/45` je logická úplnosť v určenom scope, nie dôkaz existencie operátora |
| `M-008` až `M-013` | stabilné identifikátory materiálnych fyzikálnych nálezov alebo dôvodov STOP; presný dosah každého je uvedený pri jeho koľaji |
| `N1` | požiadavka na úplný fyzický quotient $Q_Z$ so vyriešenými prekryvmi |
| `N2` | požiadavka na zostavenie celej mapy $X_Z$ z tohto quotientu |
| `N3` | až po N1/N2 klasifikácia whole-map jadra: injektivita, nenulový fyzický kernel witness alebo dokázane zmiešaná úplná rodina; výsledok rozlišuje `PK1/I0`, ale sám nie je globálny operator witness ani A2-K4 PASS |
| `W1–W4` | štyri registrované diskriminačné kontroly obrazu/jadra v aktuálnom P5.3 kontrakte; nie sú to fyzikálne konštanty a bez route prefixu sa nemajú citovať samostatne |
| `A3-M1` až `A3-M6` | budúce implementačné a reprodukčné míľniky stanice A3 po úplnom uzavretí A2 |
| `F1–F5` | päť filozofických pravidiel z §3: efektívna vrstva, nepriamy merateľný dôsledok, fyzická nezvratnosť merania, zákaz účelového výkladu a povinná cena lokálnej prestavby |
| `R3.18` alebo `v3.18` | identifikátor tejto verzie/release; číslo nie je fyzikálne skóre ani stanica |

### 14.5 Stavové a auditné kódy

Zložený štítok oddelený lomkou spája význam všetkých svojich častí. Nie je
novým skóre ani novým fyzikálnym výsledkom. Dlhší štítok s podčiarkovníkmi
spresňuje scope základného stavu; nerozširuje ho nad význam uvedený nižšie.

| Kód | Význam |
|---|---|
| `PASS` | deklarovaná brána v presnom scope prešla |
| `REVIEW` | záver nie je uzavretý; treba presne uvedený dôkaz, vstup alebo rozhodnutie |
| `STOP_SCOPE` | zomrela iba presne testovaná podtrieda; nejde automaticky o smrť všetkých príbuzných mechanizmov |
| `LIVE`, `LIVE_ACTIVE`, `LIVE_BACKUP` | koľaj nie je fyzikálne vylúčená; prípony rozlišujú hlavnú aktívnu a záložnú živú možnosť |
| `WAITING` | chýba povinný fyzický vstup, witness alebo výpočet; nejde o PASS ani STOP |
| `EXCLUDED` | konkrétna testovaná trieda bola vylúčená z deklarovanej prípustnej množiny |
| `CONDITIONED` alebo `CONDITIONAL` | tvrdenie platí iba pri výslovne uvedených vstupoch a nie je univerzálnou vetou |
| `DERIVED` | výsledok bol odvodený v presne uvedenom matematickom scope |
| `HYPOTHESIS` | fyzikálne zatiaľ nevylúčený návrh bez dôkazu existencie |
| `OPEN`, `NOT_COMPLETE`, `NOT_PASSED` | povinná časť ešte nebola uzavretá alebo prejdená |
| `HISTORICAL`, `WITHDRAWN` | starší výsledok sa zachováva pre audit, ale nemá current predikčnú váhu alebo jeho presná formulácia bola odvolaná |
| `HISTORICAL_SUPPORT`, `HISTORICAL_NUMERICAL_SUPPORT` | archivovaný argument alebo numerický výsledok podporuje iba výslovne uvedený mechanizmus či comparator a nemá automaticky current predikčnú váhu |
| `DERIVED_WITHIN_SIMULATED_GRAPH`, `DERIVED_IN_SCALAR_OPERATOR_SCOPE` | odvodenie platí iba v uvedenom simulovanom grafe alebo v skúmanom skalárnom operátore; nie je univerzálnou vetou teórie |
| `LOOK_ELSEWHERE_ACKNOWLEDGED` | dokument výslovne priznáva, že skúmané číslo alebo štruktúra boli známe pred formulovaním príslušného testu |
| `OPEN_PHYSICAL_MAP`, `OPEN_QUANTUM_MAP` | matematický alebo simulačný výsledok existuje, ale jeho mapa na fyzikálny, respektíve kvantový mechanizmus zostáva otvorená |
| `BACKGROUND_GATE_PASS` | prešla iba homogénna backgroundová bilančná brána; neznamená prejdenie porúch ani celej teórie |
| `REQUIRED_NORMALIZATION_MAP` | uvedené normalizačné mapovanie je povinné na odstránenie neprípustnej závislosti backgroundu |
| `CONDITIONAL_A1_NORMALIZATION_ACCEPTED` | konkrétna A1 normalizácia je prijatá iba pri zmrazených vstupoch uvedených v texte |
| `CONDITIONAL_INTERPRETATION`, `CONDITIONAL_MECHANISM_READING` | uvedené fyzikálne alebo mechanistické čítanie je podmienená interpretácia, nie jedinečne odvodený mechanizmus |
| `MECHANISM_READING_NOT_THEOREM` | mechanistická motivácia existuje, ale výsledok nie je dokázanou vetou bunkovej dynamiky |
| `SCOPE_NARROWED` | neskorší audit obmedzil dosah staršieho širšieho tvrdenia |
| `RECALCULATION_OPEN`, `NOT_YET_AVAILABLE` | číselná predikcia sa musí prepočítať alebo zatiaľ nie je k dispozícii |
| `NOT_AUTHORIZED`, `BLOCKED_BY_…` | nasledujúca fáza sa nesmie začať, kým neprejde pomenovaná upstream brána |
| `SCIENTIFIC` | STOP alebo nález vznikol z fyzikálneho/matematického rozporu v deklarovanom scope, nie zo syntaxe, runtime alebo sandboxu |
| `SEPARATE_ROUTE` | položka patrí do inej fyzikálnej vetvy a nesmie sa vydávať za pokračovanie aktuálnej koľaje |
| `GLOBAL_FEASIBILITY_INCOMPLETE` | spoločná prípustná množina ešte nebola dokázaná ako neprázdna ani prázdna |
| `S1` | materiálny auditný nález lokálne opraviteľný v tej istej koľaji |
| `T1` | technický nález bez dosahu na vedecké tvrdenie |
| `T2` | skrátený zápis projektovej úrovne `T2_REPRODUCIBLE_CALCULATION` — zapečatený balík s provenienciou primárneho vzorca, runnerom, všetkými importmi a runtime vstupmi, preregistráciou, immutable rawom, toleranciami a verziami, ktorý umožňuje nezávisle zopakovať deklarovaný official výpočet; nejde o ľubovoľnú kontrolu balíka ani o pokračovanie finding class `T1` z predchádzajúceho riadka |
