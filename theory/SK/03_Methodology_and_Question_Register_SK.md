# 03 — Kvantová bunková teória priestoru v3.18: metodika a register otázok

**Autor:** Martin Jámbor<br>
**Jazyková autorita:** slovenská verzia<br>
**Release trieda:** `R3.18-CONSOLIDATED / COMPLETE_SELF_CONTAINED_SNAPSHOT`<br>
**Obsahový cutoff:** 9. august 2026<br>
**Plánované publikačné okno:** 11.–13. august 2026<br>
**Stav teórie:** pracovná fyzikálna hypotéza s auditovanými čiastkovými
výsledkami; zatiaľ nie je experimentálne potvrdená

## 0. Účel, autorita a samostatnosť

Tento dokument je jediným úplným release registrom metodiky a otázok pre
v3.18. Obsahuje všetky pravidlá potrebné na čítanie current vydania a pri
otázkach uvádza dnešný užší stav. Predchádzajúci metodický dokument netreba
čítať. Historické tvrdenie sa nemaže; ak ho neskorší audit obmedzil,
register uvádza dôvod a current dosah. Pracovná chronológia a detailné
výpočtové vetvy zostávajú v `tracks/`, nie v release dokumente.

Súvislý fyzikálny výklad je v `01_Bunkovy_Vesmir_SK.md` a stabilný
strojovo čitateľný register predikcií P01–P11 v
`02_Prediction_Status_Table_SK.csv`. Úplný index exaktných zákonov,
otvorených mantinelov, kalibrácií, predikčných väzieb a death reach je v
`04_Theory_Existence_Conditions_Register_SK.csv`. Tento súbor
vysvetľuje, podľa akých pravidiel sa ich stav audituje a ktoré otázky
zostávajú otvorené.

Pri výklade v3.18 rozhoduje tento zmrazený slovenský release payload podľa
rozdelenia rolí v sprievodcovi `00`: dokument `02` je autoritou pre riadky
P01–P11, dokument `01` pre súvislý fyzikálny výklad a stav koľají, tento
dokument `03` pre metodiku a otázky a dokument `04` pre index podmienok
existencie. Starší publikovaný záznam zostáva nemennou provenienciou, ale
nesmie prepísať neskorší užší stav prijatý v tomto vydaní. Nové rozhodnutie
autora zmení význam vydania až cez hashovo viazané erratum alebo novú verziu.
Route-local contract riadi iba svoj pracovný rozsah a nesmie rozšíriť ani
prepísať schválené release tvrdenie. V3.18 nemení fundament a nepridáva nový
fit.

Stavy majú presný význam:

- `PASS` — uzavretý iba uvedený scope;
- `STRUCTURAL_PASS` — algebraická alebo štrukturálna brána, nie plná fyzika;
- `LIVE / CONDITIONED` — bez dokázaného rozporu, ale závislý od otvorených brán;
- `LIVE / WAITING` — koľaj nie je mŕtva, chýba presný vstup alebo odvodenie;
- `REVIEW` — dôkaz alebo dosah ešte nie je uzavretý;
- `STOP_SCOPE` — mŕtvy je iba presne testovaný scope;
- `WITHDRAWN` — staré tvrdenie sa už nesmie prezentovať ako current;
- `HISTORICAL` — zachovaný záznam bez current predikčnej váhy;
- `SURVIVAL_TARGET` — vopred zapísaná hodnota alebo rozsah nutný na
  prežitie presného deklarovaného scope; nie je to automaticky posterior ani
  dokázaná veta;
- `EXACT_SCOPED_SURVIVAL_CONDITION` — exact podmienka odvodená iba v
  uvedenom operátorovom alebo mechanistickom scope;
- `HISTORICAL_TARGET_PROVENANCE` — archívny údaj o pôvode staršieho výpočtu;
  nie je samostatnou current rozhodovacou triedou. Ak hodnota zostáva v3.18
  aktívnym mantinelom, musí dostať vlastnú current triedu a presný death reach;
- `OPEN_NO_KILL_WINDOW` — povinnosť je známa kvalitatívne alebo funkčne, ale
  číselný rozsah a observable mapa ešte neboli odvodené; výsledok zatiaľ
  nesmie vytvoriť fyzikálny death verdict;
- `CALIBRATION_BENCHMARK` — zmrazený vstup alebo odvodená bookkeeping
  hodnota presného výpočtu; nie je automaticky predikciou ani kill hranicou;
- `NOT_A_SCIENTIFIC_SURVIVAL_CONDITION` — procesné alebo numerické číslo bez
  fyzikálneho death reach.

Tieto označenia netvoria jeden lineárny zoznam. Prvých osem opisuje stav
overovania tvrdenia alebo koľaje; zostávajúce označenia opisujú vedeckú rolu
hodnoty či podmienky. Typický workflow jedného presne zmrazeného scope je:

```text
LIVE / WAITING
  -- doplnenie chýbajúceho vstupu alebo odvodenia --> REVIEW
REVIEW
  -- prejdenie iba algebraickej/štrukturálnej brány --> STRUCTURAL_PASS
STRUCTURAL_PASS
  -- ďalšie povinné brány ešte zostávajú --> LIVE / CONDITIONED
REVIEW alebo LIVE / CONDITIONED
  -- všetky povinné brány daného scope prešli --> PASS
REVIEW alebo LIVE / CONDITIONED
  -- preukázaný rozpor v danom scope --> STOP_SCOPE
```

`STRUCTURAL_PASS` teda nie je slabší názov úplného `PASS`; je to prijatý
medzivýsledok, po ktorom rodičovská koľaj zvyčajne ostáva
`LIVE / CONDITIONED`. `WITHDRAWN` a `HISTORICAL` sú publikačno-provenienčné
stavy mimo tejto vetvy: odvolané tvrdenie sa nesmie používať ako current,
ale jeho pôvod a dôvod obmedzenia zostávajú v histórii. Označenia od
`SURVIVAL_TARGET` po `NOT_A_SCIENTIFIC_SURVIVAL_CONDITION` neurčujú poradie
workflow; hovoria, akú rozhodovaciu váhu má konkrétna hodnota alebo
podmienka.

Register `04` používa v stĺpci `canonical_class` presne šesť vzájomne
zdieľaných tried: `OBSERVATIONAL_SURVIVAL_TARGET`, `EXACT_PHYSICAL_LAW`,
`CONDITIONAL_MODEL_OUTPUT`, `CALIBRATION_BENCHMARK`, `MECHANISM_READING` a
`OPEN_NO_KILL_WINDOW`. Jemnejší historický názov zostáva v samostatnom
stĺpci `subtype_v3_18`; nesmie vytvárať siedmu rozhodovaciu triedu.
`CONDITIONAL_MODEL_OUTPUT` je výstup zmrazeného modelu a vstupov, nie
univerzálny zákon, posterior ani potvrdenie teórie. `MECHANISM_READING` je
interpretácia mechanizmu bez samostatného death reach, pokiaľ ho konkrétny
riadok výslovne nepridelí.

## 1. Kotva a pracovný protokol

**KOTVA:** Je pozorovaná fyzika povrchovou stopou metabolizmu bunkovej siete
priestoru?

Pracovný sled zostáva:

`NÁVRH -> PREKLAD NA ROVNICE A STOPY -> SÚD -> PASS/REVIEW/STOP_SCOPE`.

Každý vstup autora je hypotéza. Reprodukcia tabuľky potvrdzuje čísla, nie
mechanizmus. Falzifikácia presného scope je informačný zisk. K rozhodnutému
scope sa možno vrátiť iba s novou fyzikou, preukázanou chybou alebo novými
nezávislými dátami.

### 1.1 Podmienky prežitia, rozsah smrti a zákaz dvojitého použitia dát

Predikcia môže byť vedecky záväzná aj pred úplným mikrofyzickým dôkazom, ak
je zapísaná ako podmienka prežitia. Meranie v cieľovom okne znamená iba, že
presný scope zostáva živý; nepotvrdzuje bunkový mechanizmus. Meranie mimo
okna vedie k `STOP_SCOPE` až po úplnej model-to-observable mape, zahrnutí
experimentálnych a teoretických neistôt, covariance a systematík.

Každý survival target musí uviesť dosah smrti:

- `FORMULATION_LEVEL` — zomrie presný ansatz alebo historický výpočet;
- `TRACK_LEVEL` — zomrie celá koľaj s rovnakou fyzikálnou identitou;
- `THEORY_LEVEL` — celá KBTP zomrie iba pri rozpore s fundamentom alebo keď
  je v každej koľaji preukázane úplného top-level zoznamu prázdny prienik
  jej povinných podmienok.

Ak sa BBN, CMB alebo iné meranie použije na rekonštrukciu `C_s`, branchingu
alebo inej neznámej funkcie, je to `CALIBRATION_DATA`. Tá istá dátová vrstva
sa nesmie znovu počítať ako nezávislé potvrdenie. Pre súčasný test
životaschopnosti možno všetky dáta použiť ako mantinely a hľadať
`OBSERVATIONALLY_COMPATIBLE_EXISTENCE_WITNESS`; predikčná sila však vyžaduje
out-of-sample observablu alebo mikrofyzicky zafixované vstupy.

Register `04` je povinný spoločný index všetkých current hodnôt a
mantinelov. Pri P01–P11 nesmie prepisovať register `02`, ale musí naň
odkazovať. Exaktné zákony zapisuje bez voľnej tolerancie; merané porovnania
zapisuje s datasetom, modelom, CL, neistotami, covariance a systematikami.
Položka bez odvodeného okna zostáva `OPEN_NO_KILL_WINDOW`; číslo sa nesmie
doplniť odhadom iba preto, aby tabuľka pôsobila úplne.

## 2. Zrod, identita a archivácia koľají

### K-ZROD

Nová koľaj vznikne iba ak:

1. rieši podotázku kotvy;
2. nejde o technickú opravu existujúcej koľaje;
3. má vlastný mechanizmus, metódu a najmenej jednu povrchovú stopu;
4. uvádza rozdiel od existujúcich a mŕtvych koľají;
5. uvádza, čo nie je jej úlohou a aké sú jej kill conditions.

Ak existuje viac fyzikálne odlišných možností, vzniknú koľaje `K1...Kn`.
Jednotlivá koľaj `t` dostane `STOP_SCOPE`, keď je jej vlastná prípustná
množina `A_t` certifikovane prázdna v presne testovanom scope. Nadradený
`OR` uzol zostáva živý, kým je aspoň jedna alternatíva otvorená alebo
neprázdna; zomiera až po dôkaze úplnosti zoznamu a prázdnosti každej jeho
alternatívy v spoločnom scope.

### M-ZROD a Q-ZROD

Míľnik potrebuje výstup, kritérium uzavretia, spôsob uzavretia, váhu a
kontrolu duplicity. Nová otázka potrebuje koľaj, povrchovú stopu a
rozhodovaciu bránu; inak je iba lešením.

### AR-MŔTVA-KOĽAJ

Mŕtve koľaje sa nemažú. Uchováva sa hypotéza, scope, zákon/test, dôvod smrti,
vstupy, skripty, raw, audit, čo verdikt nezabíja a podmienka znovuotvorenia.
Premenovanie parametra, širší grid alebo iný solver nevytvára novú fyziku.
Technický timeout, syntax chyba alebo vyčerpanie implementačnej dávky nie je
fyzikálny STOP.

## 3. Povinné verifikačné pravidlá a známe pasce

### P1–P5

- `P1`: pipeline sa porovná s referenčným modelom v tom istom behu, ak je
  taký comparator významovo definovaný;
- `P2`: stuhnutý systém potrebuje vhodný solver a audit krokovej konvergencie;
- `P3`: solver má fyzikálne medze, nulové limity, finite guardy a checkpointy;
- `P4`: mocninový fit najprv kontroluje okrajovú a truncation kontamináciu;
- `P5`: žiadne číslo bez jednotiek, konvencie, citlivosti a claim class.

### M1–M9

`M1` neohraničená sekantová metóda — numerické hľadanie koreňa z dvoch
posledných bodov bez použitia derivácie; bez fyzikálneho intervalu môže
preskočiť do nepovolenej oblasti, cez singularitu alebo ku nesprávnemu
koreňu. `M2` prehodené časové polia; `M3` bisekcia bez samosúladnosti; `M4`
okraj skresľujúci mocninu; `M5` pevný Euler pri
bilineárnom zdroji; `M6` porovnanie intervalov s odlišným backgroundom;
`M7` boxové okraje vo vlnovej úlohe; `M8` nevalidované počítanie stupňov
voľnosti; `M9` tuhé zrkadlá vytvárajúce falošný éter.

### AR-LINEAGE

Pred fyzikálnou váhou downstream skriptu musí existovať physics contract:
rodičovská rovnica, gauge/frame, stavový priestor a poradie, backgroundové
koeficienty, význam Fourierovho módu, units, nulové limity a constrainty.
Audit overuje, že každý prvok prešiel do implementácie alebo je označený ako
kontrolovaná aproximácia. Chýbajúci stupeň voľnosti, zmena smeru `Q_A^mu`,
zámena radu za exact background alebo presun realizovaného `k` do FLRW
backgroundu je STOP implementácie a claim quarantine, nie obyčajná solverová
chyba.

## 4. Dôkazové triedy, mantinely a neznáme funkcie

Každý mantinel má triedu. Trieda nehovorí, či sa nám výsledok páči, ale odkiaľ
pochádza jeho autorita a na aké rozhodnutie sa smie použiť. Tým sa zabraňuje,
aby sa pomocný benchmark, predpoklad alebo zhoda s referenčným modelom vydávali
za dokázaný zákon či priame meranie:

- `E0_EXACT` — matematická identita alebo dokázaný fyzikálny zákon v presne
  uvedenom scope. Používa sa ako tvrdý vnútorný guard: po overení mapovania
  rovníc, jednotiek a predpokladov jeho porušenie môže priamo vylúčiť daný
  scope;
- `E1_DIRECT_MEASUREMENT` — observačné alebo experimentálne dáta. Rozhodovaciu
  váhu dostanú až s úplnou model-to-observable mapou, neistotami, covariance,
  systematikami a deklarovaným štatistickým testom; až potom môžu obmedziť
  alebo vylúčiť fyzikálny scope;
- `E2_REFERENCE_MODEL` — comparator, benchmark alebo nulový limit. Slúži na
  kontrolu implementácie, znamienok, jednotiek a očakávaného limitného
  správania. Samotná nezhoda s referenčným modelom nie je fyzikálny STOP,
  pokiaľ porovnávaná vlastnosť nie je samostatne povinným `E0` alebo úplne
  zmapovaným `E1`;
- `E3_PROVISIONAL` — pracovný odhad, heuristika alebo vodidlo na výber
  ďalšieho testu. Pomáha zúžiť hľadanie a určiť prioritu, ale nemá
  vylučovaciu váhu a nesmie vytvoriť PASS ani STOP.

Jedna veličina môže mať v rôznych použitiach odlišnú evidenčnú triedu.
Napríklad číslo použité na kalibráciu je vstupom rekonštrukcie, nie zároveň
nezávislým `E1` potvrdením; jeho konkrétna rola preto musí byť pri každom
teste zapísaná vopred.

Iba `E0` alebo úplne zmapovaný `E1` môže zabiť fyzikálny scope. Nezhoda s
nedokázanou predpoveďou referenčného modelu je iba
`REFERENCE_MISMATCH_ONLY`. Dokázaný zákon nemá voľnú toleranciu; meraný test
používa deklarovanú experimentálnu neistotu.

### FS-GATE-01 — najprv správanie, potom vzorec

Pred voľbou ansatzu sa píšu doména, kodoména, units, regularita, covariance,
lokálnosť, symetrie/parita, conservation, causality, stabilita, nulové a
hraničné limity, pozitivity a observačné mapy. Pred-výpočtovo vylúčený scope
sa označí `PRECHECK_EXCLUDED_SCOPE`, nie `COMPUTED_STOP_SCOPE`.

Ak konkrétnu funkciu ešte nepoznáme, FS-GATE-01 sa uplatňuje na úrovni
správania celej prípustnej triedy, nie ako požiadavka na uzavretý analytický
vzorec. Doména, jednotky, symetrie, limity a guardy vtedy definujú
`F_adm`; FS-GATE-02 následne skúma, či v tejto triede existuje aspoň jedna
funkcia spĺňajúca všetky povinné mantinely. Obe brány sú teda postupné, nie
protichodné.

Pre Lorentzov sektor je povinné rozlíšenie: v auditovanom skalárnom
cosine-Laplacian scope a v každej vetve odvolávajúcej sa na paritnú ochranu
musí byť nepárny lineárny člen exaktne nulový. Všeobecný fyzický fotónový
sektor môže namiesto toho prežiť iba s odvodeným koeficientom a znamienkom
kompatibilným s príslušnou experimentálnou medzou. Kvadratický/Planckom
potlačený člen sa porovnáva s osobitnou medzou. Pre hmotové zložky musí úplná
teória rešpektovať ekvivalenčný princíp vrátane kompozičnej univerzality;
skalárny even operator to sám nedokazuje.

### FS-GATE-02 — prípustná množina

Ak funkciu nepoznáme, nehádame potichu jeden reprezentant. Definujeme

```text
A_t = {f in F_adm,t : všetky E0 identity a guardy platia a všetky otvorené
       E1 observably ležia v predregistrovanej tolerančnej oblasti}.
```

Tu `t` označuje jednu fyzikálnu koľaj a `A_t` jej prípustnú množinu; nejde o
skalárnu backgroundovú amplitúdu `A_f` z dokumentu `01`.
`RANGE_EXISTENCE_PASS` vyžaduje svedka v celej spoločnej `A_t` na povinnej
doméne alebo rovnocennú existenčnú vetu; lokálny function/output svedok
nestačí.
`RANGE_CONDITIONAL_OPEN` znamená iba neprítomnosť dokázaného rozporu.
Konečný prázdny grid nie je dôkaz prázdnej funkčnej množiny. Pri `AND` uzle
rozhoduje spoločný prienik povinných podmienok jednej koľaje. Pri `OR` uzle
sa prípustné množiny fyzikálne alternatívnych koľají zjednocujú a ich zoznam
musí byť preukázane úplný. Teória je `GLOBAL_FEASIBILITY_INCOMPLETE`, kým
chýba povinná funkcia alebo observable mapa; zomiera v scope až po
certifikáte, že každá množina `A_t` úplného top-level zoznamu je prázdna.
Alternatívne koľaje sa nikdy nesmú navzájom pretínať ako keby boli súčasne
povinné.

Riadkové kill okno je test deklarovanej formulácie alebo koľaje
(`FORMULATION_LEVEL` alebo `TRACK_LEVEL`). Výsledok mimo okna po úplnej
observable mape a likelihood vylúči iba tento scope. FS-GATE-02 dáva
`THEORY_LEVEL` rozsudok až vtedy, keď je top-level zoznam alternatív
preukázane úplný a prípustná množina každej z nich je certifikovane prázdna.
Lokálny kill preto nevyžaduje globálnu prázdnosť, ale ani sa nesmie potichu
povýšiť na smrť celej teórie.

Output-range relaxácia môže niesť celú povolenú korešpondenciu do potomkov,
ale nesmie ju nahradiť stredom, nulovým smerom ani fitovaným reprezentantom.
Jej neprázdnosť nedokazuje existenciu jednej globálnej hladkej lokálnej
funkcie.

### FS-GATE-03 — konečný a zmrazený register alternatív

Pre každý release sa top-level zoznam `T_top^(v)` zmrazí ako konečný,
autorom schválený register fyzikálne odlišných koľají. `LIVE_BACKUP / WAITING`
bez úplného contractu, prípustnej množiny a witnessu nie je pozitívny dôkaz
životaschopnosti; iba bráni neodôvodnenému `THEORY_STOP` a ponecháva stav
`GLOBAL_FEASIBILITY_INCOMPLETE`. Nová koľaj po cut-offe musí dostať nové ID,
presný rozdiel mechanizmu, predregistrované mantinely a author decision v
novom release alebo auditnom delte. Nesmie spätne zmeniť smrť staršieho
scope ani sa pridať iba preto, že už poznáme nepriaznivý výsledok. Teória je
pozitívne `RANGE_EXISTENCE_PASS` iba vtedy, keď aspoň jedna úplne
špecifikovaná top-level koľaj má globálneho svedka v kompletnej spoločnej
`A_t` alebo rovnocennú existenčnú vetu; lokálny function/output svedok ani
samotný zoznam predstaviteľných alternatív nestačia.

## 5. Výpočtový, auditný a release workflow

`CONTRACT/DRAFT -> DEV_SANDBOX -> RC_FREEZE -> nezávislý statický audit ->
OFFICIAL RUN presne raz -> interný science audit -> rozhodnutie orchestrátora
-> MILESTONE_PROGRESS_REVIEW -> {ACCEPTED_CHECKPOINT_FREEZE iba pri prijatom
auditovateľnom míľniku | NEXT_ATOM / WAIT}`.

Osobitná nevýpočtová vetva je `FROZEN_MANUAL_ANALYTIC_RESULT ->
MANUAL_ANALYTIC_RESULT_AUDIT -> ORCHESTRATOR_DECISION`. Neobsahuje Python,
RC ani official run a nesmie sa za ne vydávať.

Šípka je hlavná úspešná cesta jedného **vedeckého atómu** — jednej presne
ohraničenej otázky alebo výpočtu. Jednotlivé fázy znamenajú:

| Fáza | Čo znamená | Čo ju otvorí | Čo ju uzavrie a spôsobí ďalší prechod |
|---|---|---|---|
| `CONTRACT/DRAFT` | Vedecká otázka sa preloží na presný scope, rovnice, vstupy, jednotky, gauge/frame, očakávaný výsledok, prahy a vetvy `PASS/REVIEW/STOP`. Ešte nejde o spustiteľný dôkaz. | Nová fyzikálne samostatná otázka, povolený ďalší krok koľaje alebo návrat po chybe v samotnom contracte/rovnici. | Contract je obsahovo úplný a orchestrátor povolí technickú implementáciu v `DEV_SANDBOX`. Nejasná fyzikálna voľba ide najprv na rozhodnutie autora. |
| `DEV_SANDBOX` | Technická dielňa. Autor skriptu smie implementovať a opravovať pracovný source a používať iba offline syntetické compile/help/unit/selftest kontroly. Výsledok nemá fyzikálnu váhu. | Úplný contract a kapsul, ktorý presne povoľuje DEV súbory, testy a write scope. | Celý povolený DEV suite prejde, vznikne stav `DEV_TESTS_PASS` a kandidát môže byť zmrazený ako RC. Technická chyba vracia prácu do toho istého DEV source; pri `10/10` vzniká `TECHNICAL_PERMISSION_GATE`. |
| `RC_FREEZE` | Z úspešného DEV kandidáta sa vytvorí nemenný release candidate výpočtu: zmrazia sa SHA contractu, presné hashe source/base/runner/input, absent-output guard, mapa runtime závislostí, official príkaz a timeout, prahy, identita autora RC a odlišného statického audítora. | `DEV_TESTS_PASS` bez otvorenej technickej chyby. | Exact RC kapsul je úplný a odovzdaný nezávislému statickému audítorovi. Každá zmena zmrazeného bajtu ruší RC a vyžaduje nový freeze. |
| `INDEPENDENT_STATIC_MATH_AUDIT` | Odlišný audítor bez official runu kontroluje rovnice, znamienka, jednotky, gauge, stavové poradie, provenienciu, guardy, rozhodovacie vetvy a runtime kontrakt exact RC. Nevydáva fyzikálny verdikt. | Hashovo zhodný RC a potvrdené oddelenie autora od audítora. | Odporúčanie `PASS` umožní orchestrátorovi zvážiť autorizáciu official runu. Chyba kódu/prepisu vracia do `DEV_SANDBOX`; chyba contractu do `CONTRACT/DRAFT`; zmena identity koľaje ide na rozhodnutie autora. |
| `OFFICIAL_RUN_AUTHORIZED / OFFICIAL RUN` | Orchestrátor povolí jeden ohraničený beh exact auditovaného RC nad official vstupmi. Výstup sa zapisuje presne raz do vopred neprítomného cieľa a po úspechu sa stáva immutable rawom. | Statický audit odporučil PASS, hashe sedia, RC nie je v DNR, cieľ neexistuje a `RUN_AUTHORIZED=true`. | Úplný raw a execution receipt sedia so schémou a hashmi, potom sa otvorí interný science audit. Crash, timeout, dependency alebo schema fail je technická chyba bez fyzikálneho verdiktu a vracia sa na najskorší chybný upstream bod. |
| `INTERNAL_SCIENCE_AUDIT` | Pri official raw nezávislý fyzikálny audítor interpretuje výsledok voči contractu: kontroluje fyzikálny význam, covariance, conservation, gauge, causality, stabilitu, limity, konvergenciu, observably a presný claim/death reach. | Úplný immutable raw, execution receipt a odlišný interný fyzikálny audítor. | Audit dá odporúčanie pre orchestrátora. Materiálny nález `S1–S4` aktivuje `CLAIM_QUARANTINE` a finding-impact/identity review; technický `T1` sa vracia na dosiahnuteľný technický bod. |
| `FROZEN_MANUAL_ANALYTIC_RESULT / MANUAL_ANALYTIC_RESULT_AUDIT` | Samostatná non-RC vetva pre ručne odvodený analytický výsledok. Zmrazí sa presné telo dôkazu, vstupy, rozsah tvrdenia a záznam jednorazovo spotrebovanej autorizácie; odlišný `manual_analytic_result_auditor` kontroluje rovnice, logiku, provenienciu a claim reach. Táto vetva nepoužíva projektový kód, Python, sieť, RC, official output ani sama nevytvára observable claim. | Výslovná jednorazová autorizácia, hashovo zmrazené telo a vstupy a potvrdený zákaz self-auditu. | Audítor odovzdá iba odporúčanie orchestrátorovi. Samotný ručný audit neautorizuje checkpoint, externý package ani fyzikálny či observačný verdikt. |
| `ORCHESTRATOR_DECISION` | Hlavný orchestrátor spojí dôkazy príslušnej vetvy a nezávislý audit a ako jediný zapíše autoritatívny stav presného scope: prijatý `PASS`, `REVIEW/LIVE-WAITING` alebo `STOP_SCOPE`. Vo výpočtovej vetve číta contract, RC/raw a interný science audit; v ručnej vetve zmrazené analytické telo a vstupy, záznam autorizácie a manuálny audit. Nesmie rozšíriť dosah dôkazov. | Dokončený interný alebo manuálny audit, prípadne uzavretý finding decision record. Pri zmene fyziky/identity musí predtým rozhodnúť Martin Jámbor. | Autoritatívny scoped stav a jeho závislosti sú zapísané; tým sa otvorí milestone progress review. |
| `MILESTONE_PROGRESS_REVIEW` | Posúdi sa informačný prínos: či sa uzavrela brána, zmenil blocker alebo route, či práca stále smeruje k cieľu a aký je najmenší užitočný ďalší vedecký atóm. Nemení fyzikálny verdikt. | Prijatý official/scientific výsledok, zmena autoritatívneho blockeru/route, `10/10` permission gate alebo explicitné podozrenie na goal drift. | Určí sa ďalší krok, čakanie, vhodnosť externého auditu alebo — iba pri prijatom opakovateľne auditovateľnom míľniku, scoped STOP či vedecky významnom blockeri — `ACCEPTED_CHECKPOINT_FREEZE`. Samotný `TECHNICAL_PERMISSION_GATE` checkpoint ani externý package nevytvára. Bežná DEV oprava, compile či smoke test túto fázu nespúšťajú. |
| `ACCEPTED_CHECKPOINT_FREEZE` | Prijatý ucelený míľnik, scoped STOP alebo významný prijatý blocker sa zviaže s rodičmi a dôkazmi príslušnej vetvy do opakovateľného checkpointu. Výpočtový checkpoint viaže hashe contractu, RC, vstupov, rawu a interného auditu; ručný analytický checkpoint viaže hashe zmrazeného analytického tela, vstupov, záznamu autorizácie a manuálneho auditu. Checkpoint nezväčšuje vedecký dosah výsledku. | Orchestrátor prijal presný výsledok a progress review potvrdil, že má trvalú informačnú alebo auditnú hodnotu. | Checkpoint sa zapíše do append-only registra. Môže sa stať zdrojom ďalšieho vedeckého atómu alebo canonical externého auditného balíka; bez nového výsledku sa znovu neprepisuje. |

Najdôležitejšie návratové a blokovacie vetvy sú:

| Udalosť | Povinný následok |
|---|---|
| Bežný DEV fail | Opraviť ten istý pracovný source, zapísať jednu technickú chybu a regresný test; nevzniká fyzikálny `STOP`. |
| Desať technických chýb v dávke | `TECHNICAL_PERMISSION_GATE`; ďalší edit alebo run čaká na výslovné povolenie Martina. |
| Statický audit nájde chybu implementácie | Návrat do `DEV_SANDBOX`, nový úspešný DEV suite a nový RC hash. |
| Statický alebo science audit nájde chybu contractu/rovnice pri zachovanej identite | Návrat do `CONTRACT/DRAFT`; opakujú sa iba dotknutý bod a jeho potomkovia. |
| Official run technicky zlyhá | Žiadny fyzikálny výsledok; opraviť najskoršiu dosiahnuteľnú technickú príčinu a official beh neopakovať bez novej autorizácie. |
| Audit nájde `S1–S4` | `CLAIM_QUARANTINE` najskoršieho zasiahnutého bodu a všetkých tranzitívnych potomkov -> jeden spoločný impact/identity decision record -> `MARTIN_DECISION_GATE` pre voľbu opravy tej istej koľaje, novej koľaje alebo ukončenia presného scope -> orchestrátor zapíše presný návratový bod a autoritatívny stav. Audítor iba odporúča. |
| Výsledok je `LIVE / WAITING` | Koľaj zostáva živá; plán musí pomenovať presný chýbajúci vstup, reaktivačnú podmienku a čo sa nesmie bez nového dôkazu opakovať. |

DEV používa syntetické testy a nemá vedecký verdikt. Každý Python proces má
vnútorný aj vonkajší timeout. Pred official runom sa zapíše ľudský význam,
očakávaný rozsah, PASS/REVIEW/STOP vetvenie a postup pri odchýlke. Skripty,
vstupy, prostredie, príkazy, raw a hashe sa zachovávajú. Nepoužiteľný skript
sa označí v DNR/histórii; nesmie zavádzať budúceho auditora.

Jedna implementačná línia má desať technických chýb na dávku. Technická
chyba nie je fyzikálny výsledok. Pri `10/10` rozhoduje autor o ďalšej dávke;
counter nezmizne premenovaním súboru ani agentom. Technické chyby ovplyvňujú
iba proces — zastavia ďalší edit alebo run do novej autorizácie — nikdy samy
nemenia fyzikálny PASS/REVIEW/STOP ani životnosť rodičovskej koľaje.

Auditné nálezy používajú `P0_PACKAGE_PROCESS_ONLY`,
`T1_TECHNICAL_NO_CLAIM_REACH`, `S1_LOCAL_CORRECTABLE_SAME_TRACK`,
`S2_TRACK_IDENTITY_AT_RISK`, `S3_FATAL_IN_SCOPE` a
`S4_PARENT_THEORY_IMPACT`. `S1–S4` aktivujú claim quarantine a jeden spoločný
decision record s matematickým, fyzikálnym a filozoficko-identitným dosahom.
Hlavný orchestrátor jediný zapisuje autoritatívny PASS/REVIEW/STOP.

### 5.1 Interný auditný kapsul a externý canonical package

Pre interný audit sa nevytvára nová kopírovaná evidence sada po každom kroku.
Audítor dostane hashovo viazaný **interný kapsul**, ktorý ukazuje na presný
contract/preregistráciu, RC source a vstupy, rozhodovacie prahy, závislé
checkpointy a auditné otázky. Pri výpočtovej vetve obsahuje immutable raw a
execution receipt; pri ručnej analytickej vetve hashovo zmrazené telo a
vstupy výsledku a záznam spotrebovanej jednorazovej autorizácie. Autor
artefaktu, statický matematický audítor, manuálny analytický audítor a interný
fyzikálny audítor musia byť rozlíšení podľa príslušnej vetvy a pravidiel
oddelenia rolí.

Samostatný **canonical externý auditný package** vzniká až po prijatí
uceleného vedeckého míľnika, fyzikálneho `STOP_SCOPE` alebo materiálneho
blockera, ktorý má zmysel posúdiť mimo projektu. Obsahuje najmenej:

1. scope a poradie čítania;
2. manifest a SHA-256 všetkých pribalených súborov;
3. pokyny pre auditora a presné otázky;
4. očakávania, príkaz reprodukcie a runtime/dependency mapu, ak ide o
   výpočtový výsledok;
5. checkpoint provenance a rodičovské predpoklady;
6. pri výpočtovej vetve exact contract, RC, vstupy, raw, interný audit a iba
   potrebné skripty; pri ručnej analytickej vetve zmrazené analytické telo a
   vstupy, záznam autorizácie a manuálny audit bez predstierania RC/rawu.

Balík sa po zapečatení nemení. Rovnaké bajty možno odovzdať viacerým
nezávislým auditorom; každé odovzdanie má vlastné `AUDIT_SUBMISSION_ID` a
samostatnú response cestu. Nový auditor štandardne nečíta odpovede ostatných.
Kurátor externého balíka nesmie auditovať vlastný balík.
Rozporné posudky otvoria `AUDIT_DISCREPANCY_REVIEW`, nie hlasovanie väčšiny.
DEV chyba, syntax error alebo bežný pomocný krok samostatný externý package
nevytvára. Chyba iba v control vrstve balíka je
`P0_PACKAGE_PROCESS_ONLY`; ak vedecké evidence hashe zostali rovnaké, opraví
sa a znovu zapečatí iba package, nie vedecký výpočet.

Publikované verzie sú nemenné. Každá nová verzia je úplný samostatne
čitateľný snapshot a zároveň má changelog, manifest, SHA-256, odkazy na
erratá a zmenené verdikty. Changelog nesmie niesť definíciu potrebnú na
pochopenie current teórie. SK je významová autorita; EN musí mať rovnaké
ID, rovnice, čísla, stavy a nonclaims.

## 6. Historický cintorín a current mŕtve scope

Úplný historický register #1–#20 zostáva v nemennom archíve ako voliteľná
proveniencia; na pochopenie current v3.18 ho netreba čítať. Jeho staré názvy
sa nesmú automaticky chápať ako smrť širších moderných koľají. Osobitne
staré „brzdy S8 vylúčené“ a tvrdenie „jediná páka lambda->0.10“ nemajú po
novších lineage auditoch univerzálnu platnosť. Každé opätovné použitie musí
ukázať exact starý scope, dôkaz smrti a rozdiel nového mechanizmu.

Aktuálne vedecké scoped STOPy v A2 sú:

- `A2-K1 / M-009`: presný testovaný fluidný scope;
- `A2-K2 / M-008`: presná barotropická trieda;
- `A2-K3 / M-010`: presný testovaný prenosový scope;
- `A2-K5 / M-012`: konkrétna konformná akcia;
- `A2-K6 / M-013`: zdravý interval konkrétneho operátora.

Tieto STOPy nezabíjajú A2 ako celok. `A2-K4` je `LIVE_ACTIVE / 60/100` a
`A2-K7`, `A2-K8`, `A2-K9`, `A2-K11`, `A2-K12` sú čakajúce registrované
alternatívy, nie pozitívne survival witnesses. `A2-K10` je
`SEPARATE_ROUTE / NOT_AUTHORIZED` pod backgroundovou koľajou `A1-K2`; nie je
mŕtvou ani záložnou koľajou aktívnej cesty `A1-K1`. Číslo `60/100` je kumulatívna váha
predregistrovaných fyzikálnych brán, ktoré
A2-K4 autoritatívne prešla: G5 uzavrela 50 bodov a G6 zvýšila hĺbku na 60.
G6 platí iba pre zmrazený deväťpremenný perfect-radiation effective-fluid
scope a jeho auditované znamienka, charakteristické rýchlosti, principal
symbol, stiffness a konvergenciu. Nie je mikroskopickou UV no-ghost vetou,
dôkazom globálnej hyperbolicity ani globálnej stability všetkých módov.
Nie je to percento pravdivosti, posterior, podiel všetkých podmienok ani
podiel nájdených funkcií. Otvorená alebo iba technicky prejdená podbrána
body nepridáva; historická technická hĺbka redukovaného runnera `66.5/100`
sa do tohto fyzikálneho skóre nepočíta. Čitateľský názov tejto veličiny je
**registrovaná hĺbka prejdených fyzikálnych brán**; aktuálna pripravenosť je
osobitne `A2_CLOSURE_NOT_ESTABLISHED / A3_ENTRY_BLOCKED`.

A3 je blokovaná súčasne tromi spôsobmi: procesne nie je autorizované otvoriť
A3 pred prijatím úplnej A2 koľaje; fyzikálne A3 potrebuje uzavretý lineárny
poruchový systém, produkčno-transportný operátor a regulárne počiatočné dáta;
auditne zatiaľ neexistuje úplný hashovo viazaný A2 checkpoint. Je to vstupná
brána `WAITING`, nie fyzikálny STOP A3.

## 7. Register otázok Q1–Q34

| ID | Otázka | Stav v3.18 a dôvod obmedzenia |
|---|---|---|
| Q1 | Drží delenie siete stabilnú? | `HISTORICAL / PARTIAL`. Simulácia v3.17 je stopa konkrétneho modelu; nie continuum veta. |
| Q2 | Je `delta` lokálna réžia odvodená zo stupňa siete? | `REVIEW`. `delta_mean=1/(<k>+C)=0.0229697828` je zmrazený benchmark. Ak mikrofyzika určí `delta_loc=<1/(k+C)>`, Jensen dáva `delta_loc>=delta_mean`, striktne iba pre nedegenerované `P(k)`. Bez zmrazeného `P(k)` nemožno dopočítať číselnú korekciu ani univerzálnu `delta(a)`. |
| Q3 | Aký tvar prenosu `Gamma/Q` dá mikrodynamika? | `CONDITIONAL_BACKGROUND_ONLY`. A1-K1 scalar ledger je použiteľný pre background; nie je úplný `Q_A^mu` ani mikrooperátor. |
| Q4 | Aké jazvy dá limit `xi->1` bez bilineárnej pasce? | `OPEN`. Chýba mechanizmus súbehu zlyhania, jazvy a produktov. |
| Q5 | Rastie Newtonov zákon z entropického pravidla? | `HISTORICAL NUMERICAL SUPPORT`. Vysoké R2 v konkrétnych simuláciách nie je odvodenie GR, PPN, lensingu ani univerzálneho G. |
| Q6 | Má rast siete preferovaný smer? | `PARTIAL`. Pozorovaný pokles anizotropie potrebuje analytickú/continuum limitu. |
| Q7 | Mení genéza zvukový horizont? | `SCOPE_NARROWED`. Historické neskoré scenáre neuzatvárajú nový skorý zdroj a úplný background. |
| Q8 | Sú jazva, kolaps a šíp času jedným mechanizmom? | `OPEN`. Slovná identifikácia nemá mikroskopický operátor. |
| Q9 | Znižujú V-spoje réžiu do požadovaného okna? | `HISTORICAL / MODEL-DEPENDENT`. Hodnota `C=28` nie je nezávislá veta. |
| Q10 | Aké je pravidlo vzniku a zániku V-spojov? | `HISTORICAL SUPPORT / OPEN MICROPHYSICS`. Atraktor v simulácii nie je úplná lokálna akcia. |
| Q11 | Vzniká horizont a primordiálne spektrum bez inflatónu? | `RECALCULATION_OPEN / ACTIVE_SCOPED_TARGETS`. P02 `n_s=0.9656 +/- 0.0016` a P03 `r<1e-10` zostávajú current formulation-scoped mantinelmi prežitia, ale chýba gauge-invariantný zdroj, amplitúda a uzavretá tensorová source-to-observable dynamika. Presná relácia `n_s-w` patrí do odvolanej P08. |
| Q12 | Sú pravidlá VCM-1 Lorentzovsky konzistentné? | `SCOPE_NARROWED`. Exact evenness je lokálna algebraická vlastnosť auditovaného skalárneho cosine-Laplacian operátora, nie globálna Lorentzova symetria celého systému; úplný photon/boost/EP sektor je otvorený. |
| Q13 | Je vyrastená sieť štatistická varieta? | `STOP_SCOPE HISTORICAL` pre presné čítanie 1; iné definície potrebujú novú koľaj. |
| Q14 | Zaostruje sa front signálu? | `HISTORICAL NUMERICAL SUPPORT`. KPZ-like exponent v boxe nie je sám dôkaz ostrého Lorentzovho kužeľa. |
| Q15 | Vzniká pri trávení para a aké je `Delta N_eff`? | `CONDITIONAL_NUMERICAL_DERIVATION / OBSERVATIONAL_RANGE_NOT_YET_INFERRED`. Kvalitatívny pôvod pary v spracovaní vákuového paliva je prítomný; pri `g_x=2`, `g_*s,dec=106.75` vychádza `Delta N_eff=0.0535`. Je to survival záväzok presne tejto P01/P11 termálnej formulácie, nie globálna predikcia teórie. Lokálny `C_s^mu`, branching, časovanie, exit/reheating a prežitie zostávajú otvorené. |
| Q16 | Dá sa `C=28` odvodiť z domén? | `OPEN`. Rozklad `16+8+4` je konzistentný počet bozónových stupňov neporušeného Standard Modelu; Higgsove štyri reálne smery už obsahujú tri would-be Goldstonove smery. Chýba odvodenie, prečo sa práve tento bozónový počet rovná kapacite bunky, prečo sa fermióny nepočítajú a prečo nejde o ontologický kruh alebo look-elsewhere výber. |
| Q17 | Aké sú bispektrum a `f_NL`? | `OPEN`. Treba gauge-invariantný prevod, tvar, znamienko a vyšší rád. |
| Q18 | Kedy vzniká para/vlnový relikt? | `CRITICAL OPEN / OBSERVATIONAL INVERSE PROGRAM`. Treba `dot(rho_s)+4H rho_s=C_s` cez skorú fázu, exit a reheating; BBN/CMB majú obmedziť prípustný zdrojový pás bez dvojitého započítania dát. Kým táto forward mapa chýba, `Delta N_eff=0.0535` zostáva scope-bound záväzkom deklarovanej termálnej vetvy, nie posteriorom ani theory-level kill oknom. |
| Q19 | Ktorú hmotovú zložku vytvára `Q`? | `BACKGROUND GATE PASS ONLY`. A1-K1 mapuje produkt v homogénnom účte na tlakovo zanedbateľného popolového/CDM kandidáta a baryóny konzervuje; clustering, časticová identita, perturbácie a mikrofyzika zostávajú otvorené. |
| Q20 | Aký je úplný gauge-invariantný systém porúch? | `CRITICAL OPEN`. Žiadna A2 koľaj ešte nie je úplná; A2-K4 je najhlbšia živá. |
| Q21 | Čo je `T` vo vzťahu `T proportional H`? | `CRITICAL OPEN`. Potrebná nezávislá termodynamická definícia. |
| Q22 | Ako vzniká `zeta`, `P_zeta`, `A_s` a `n_s` z delenia? | `CRITICAL OPEN`. Realizované Fourierovo `k` nesmie určovať FLRW background; je to fundamentálne oddelenie homogénneho backgroundu od porúch, nie nová voliteľná konvencia. Staré zápisy s `K_MPC=0.05` a implicitným `Phi=1` boli obmedzené práve preto, že toto oddelenie porušili. Spoločný zdroj a jeho spektrum nie sú odvodené. |
| Q23 | Čo ukončí éru paliva a reheatuje vesmír? | `CRITICAL OPEN`. Chýbajú exit, entropia, radiačná dominancia a BBN initial conditions. |
| Q24 | Je substrát 3D s tikom alebo 4D kauzálna štruktúra? | `AUTHOR-LEVEL CONCEPTUAL OPEN`. Treba odvodiť Lorentzovskú limitu alebo testovať preferovaný rámec. |
| Q25 | Ako jedna kapacita zabezpečí univerzálnu väzbu polí? | `OPEN`. Treba spoločnú metriku, viac spinov, EP a birefringenciu. |
| Q26 | Je krížová V-váha kvantovou entanglementovou entropiou? | `OPEN`. Klasická váha bez Hilbertovho priestoru a kanála nestačí. |
| Q27 | Aká je lokálna réžia pri fluktuujúcom stupni? | `OPEN`. Treba rozhodnúť medzi `1/(<k>+C)` a `<1/(k+C)>`. Pre druhú voľbu je prvá hodnota exaktná Jensenova dolná hranica, nie hotový priemer; numerický výsledok vyžaduje distribúciu `P(k)` rastúcej siete. |
| Q28 | Aký je dynamický význam `C=28` nezávislý od dát `n_s`? | `OPEN`. Vyžaduje pre-dátové odvodenie zo symetrie alebo akcie a explicitné vysvetlenie mapy medzi bozónovým obsahom emergentného Standard Modelu a kapacitou substrátu; aritmetika `28` sama nestačí. |
| Q29 | Spĺňa delenie druhý zákon termodynamiky? | `OPEN`. Treba entropie všetkých rezervoárov a nezápornú celkovú produkciu. |
| Q30 | Aké sú kill conditions predikcií a ostatných podmienok existencie? | `METHODOLOGY DEFINED / ROW-SCOPED`. Dokument 02 zapisuje survival target, presný death scope a význam zhody pre P01–P11; dokument 04 vedie úplný index EC01–EC43 vrátane exaktných zákonov, otvorených okien, kalibrácií a procesných vylúčení. Výsledok mimo okna zabíja iba deklarovaný scope po úplnej likelihood; výsledok v okne ponecháva živý ten istý scope a v rámci tohto testu KBTP nevylučuje, ale sám nepreukazuje jej globálnu životaschopnosť ani pravdivosť. |
| Q31 | Aká je mikrofyzika popola? | `OPEN`. Spin, hmotnosť, stabilita, distribúcia, phase-space a halo testy nie sú odvodené. |
| Q32 | Aká je kontinuálna limita gravitácie? | `OPEN`. Treba Einstein/Poisson limitu, lensing, PPN a polarizácie. |
| Q33 | Odvodzuje sieť globálnu krivosť bez H0 dát? | `OPEN / SEPARATE TRACK`. Historické gridy nie sú pred-dátové odvodenie `Omega_K`. |
| Q34 | Môže delenie vytvárať kovariantnú výmenu hybnosti v tmavom sektore? | `CONDITIONED OPEN`. Vyžaduje úplné `F_A^mu`, protihybnosť, stabilitu a CMB/LSS mapu; phenomenological drag fit nestačí. |

## 8. Povinný ledger starších obmedzených formulácií

| Staršia formulácia | Pôvodný scope | Rozhodujúci test alebo mantinel | Stav v3.18 a presný dosah |
|---|---|---|---|
| `K_MPC=0.05` ako backgroundová alebo sieťová škála | globálny FLRW background alebo fundamentálna škála siete | background musí byť invariantný pri zmene realizovaného Fourierovho módu, teda `partial H_FLRW(a)/partial k=0` | `WITHDRAWN INTERPRETATION`. Proveniencia ukazuje mód/pivot; hodnota `0.05` sama nie je kill condition, ale jej použitie ako backgroundovej škály zneplatní danú formuláciu. |
| `Phi=1` a `Phi z^p` ako globálny palivový člen | globálna normalizácia paliva v K4 backgrounde | exact módová kancelácia `Phi(k) z^p=A_f a^p` | `CORRECTED`. Starý globálny člen je superseded; oprava nemení sama osebe životnosť širšej A2-K4 koľaje. |
| `A_f` ako neodvodený nový parameter | normalizácia paliva v zmrazenom A1 background closure | lineage k deklarovaným A1 vstupom a zákaz nového tichého fitu | `CORRECTED / CONDITIONAL`. `A_f=7809.270101963506` je bookkeeping výsledok, nie mikrofyzická konštanta; nemá samostatné observačné kill okno. |
| `Delta N_eff=0.0535`, `0.905 K`, `53 GHz` | skorá dvojpolarizačná termálna P01/P11 formulácia | úplný `C_s^mu`, branching, exit/reheating, survival a BBN/CMB forward mapa s likelihoodom | `CONDITIONAL_NUMERICAL_DERIVATION / SURVIVAL_TARGET`. Robustná nezhoda po úplnom teste zabíja túto formuláciu, nie automaticky celú teóriu. |
| `n_s=0.9656 +/- 0.0016` a `r<1e-10` | presný `delta/m=1/2` skalárny mechanizmus a presná termálna tenzorová formulácia | úplný gauge-invariantný skalárny a tensorový systém, source-to-observable mapa, normalizácia a likelihood | `ACTIVE_FORMULATION_SCOPED_SURVIVAL_TARGETS / RECALCULATION_OPEN`. P02 a P03 zostávajú current mantinelmi; zhoda ich iba ponechá živé a nie je potvrdením KBTP. |
| presná relácia `n_s-w` | presný spoločný skalárny/backgroundový vzťah | nové nezávislé odvodenie relácie | `WITHDRAWN / NO_CURRENT_DEATH_REACH`. P08 nemá v3.18 cieľ prežitia a nesmie zabíjať ani zachraňovať aktuálnu koľaj. |
| všeobecná Lorentzova invariancia z parity jedného operátora | celý photon/boost/EP a multi-field sektor | odlíšenie lokálnej evenness operátora od globálnej covariance a univerzality | `SCOPE_NARROWED`. Zachovaná je exact evenness skalárneho operátora; všeobecný Lorentzov záver z nej nevyplýva. |
| jeden scalar `Q_A` určuje poradie vzniku hmoty, popola a pary | lokálny kauzálny graf produkcie troch zložiek | úplné kovariantné `Q_A^mu`, protihybnosť, lokálne branchingy a `delta Q_A` | `SCOPE_NARROWED`. Backgroundový energy ledger ostáva použiteľný, ale poradie paralelne/verižene ostáva otvorené. |
| tri H0/S8 body ako nový interval alebo fit | spojitý observačne interpretovaný interval alebo posterior | úplná likelihood, covariance, systematiky a spojitá parameter mapa | `FORBIDDEN CLAIM`. Body ostávajú iba diskrétnou podmienenou diagnostikou voči syntetickej kotve; mantinely prežitia P04/P05 sú osobitné current záväzky. Zlyhanie troch bodov má dosah na diagnostiku, nie automaticky na teóriu. |

## 9. Živé nenájdené funkcie a návratové body pri obsahovom cut-offe

Nasledujúca tabuľka zmrazuje stav k 9. augustu 2026. Neskoršie pracovné
výsledky patria do ďalšieho release delta alebo novej verzie a nesmú potichu
meniť tento snapshot.

| ID | Funkcia / route | Aktuálny stav | Čo ju môže uzavrieť |
|---|---|---|---|
| `UF-C01-RW1-KBRIDGE-001` | `A2-K4/P5`, lokálny stress-work/current bridge | `RANGE_CONDITIONAL_OPEN / LIVE-WAITING` | globálny local-natural svedok alebo existenčná veta nad úplnými face/bulk dátami a guardmi |
| `OR-C01-RW1-KOUT-001` | state-local output korešpondencia bridge | `CORRECTED RESULT ACCEPTED / OUTPUT_RANGE_CONDITIONAL_OPEN / RESERVOIR_INTERSECTION_CONDITIONAL_OPEN` | dôkaz neprázdnosti, kompatibility a neskôr realizovateľnosti jednou prípustnou funkciou; prijatie podmieneného výsledku nedokazuje globálny `K_bridge` ani existenciu witnessu |
| `UF-Q18-CG-001` | skorý parný/vlnový zdroj `C_s` (historicky `C_g`) | `OBSERVATIONAL_RANGE_NOT_YET_INFERRED / OPEN` | kovariantný source/rezervoár, branching, exit, reheating, BBN/CMB forward mapa a calibration/validation split |
| `UF-Q22-SOURCE-001` | spoločný zdroj porúch z energeticky náročných delení | `OPEN` | lokálny operátor, `P_S(k)`, gauge-invariantný prevod a zákaz `k`-dependent backgroundu |

## 10. Release nonclaims

Tento register nie je dôkaz celej teórie, neudeľuje A2 PASS, nemení
`A2-K4 / 60/100` a neotvára A3. Zachováva iba výslovne označené podmienené
alebo formulation-scoped survival targets `H0`, `S8`, `N_eff`, `n_s`, `r`,
`w0`, `wa`, teploty a frekvencie ako falzifikačné záväzky s riadkovo
obmedzeným dosahom. P08 je odvolaná bez current cieľa a P09 je iba benchmark
bez aktívneho targetu alebo target-based STOP. P01 a P11 tvoria jeden
spoločný termálny záväzok a nesmú sa počítať ako nezávislé potvrdenia. Zhoda
s mantinelom iba ponecháva presný scope živý; tieto hodnoty nie sú
automaticky nové posterior intervaly ani potvrdené theory-level predikcie.
