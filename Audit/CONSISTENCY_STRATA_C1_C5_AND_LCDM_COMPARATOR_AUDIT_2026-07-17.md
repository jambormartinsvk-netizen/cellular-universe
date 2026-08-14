# Audit vrstiev konzistencie C1–C5 a férového porovnania s ΛCDM

**Dátum:** 2026-07-17  
**Stav:** `AUTHORITATIVE_SCOPE_AUDIT / NO_ROUTE_VERDICT_CHANGE`  
**Rozsah:** porovnanie priloženého návrhu „A1–A5 zákony konzistencie“ s existujúcim programom A0–A8; kontrola férovosti porovnávania s ΛCDM; kontrola využitia ΛCDM v skriptoch  
**Nemení:** stav A1-K1, A2-K4 (`60/100`), žiadne skóre, žiadny PASS/REVIEW/STOP koľaje ani release stav

## 1. Hlavný záver

Priložená hierarchia je užitočná, ale jej názvy `A1–A5` sa **nesmú** zaviesť do projektu pod týmto označením. Už existujúce stanice `A1–A8` znamenajú postup práce:

- `A1`: prijímateľ zdroja a background;
- `A2`: kovariantné perturbácie;
- `A3`: Boltzmannov riešič;
- `A4`: para, časovanie a exit.

Príloha naopak triedi **typy požiadaviek**: vnútorná konzistencia, symetrie, presná dynamika, pozorovania a vzdialené cieľové stanice. Ide o dve kolmé osi. Rovnaké názvy by vytvorili zámenu typu „A3 prešla“, hoci raz by to znamenalo PPN a druhý raz implementáciu CLASS/CAMB.

Pre ďalšiu prácu sa preto príloha premenúva iba terminologicky:

| Názov v prílohe | Bezkolízny názov v projekte | Význam |
|---|---|---|
| A1 | `C1 — tvrdá konzistencia` | zákony, ktorých porušenie je okamžitý STOP |
| A2 | `C2 — experimentálne symetrie` | porušenie musí byť pod meracou medzou |
| A3 | `C3 — presná dynamika` | GR/PPN, termodynamika, primordiálna a lineárna dynamika |
| A4 | `C4 — observačná životaschopnosť` | úplný fit dát, nie zhoda s ΛCDM |
| A5 | `C5 — fundamentálny dlh` | otvorené cieľové stanice bez dnešnej numerickej tolerancie |

`C1–C5` nie sú ďalšou cestou ani novým skóre. Sú priečnou checklistovou vrstvou, ktorú musia prechádzať všetky stanice A1–A8.

## 2. Dôkazové zdroje a ich limity

Primárne interné zdroje:

1. `Audit/00_PRAVIDLO_vsetky_vstupy_autora_su_hypotezy.md` — štvorúrovňový audit a jediný aktuálny význam skóre `N/100`.
2. `tracks/00_CURRENT_EXECUTION_PLAN.md` — aktuálny vykonávací plán a pauza high-cost fyziky.
3. `tracks/A1/A1K1/A2/A2K4/00_TRACK.md` a `00_SCORECARD.md` — aktuálny stav živej A2-K4 vetvy.
4. `Audit/00_GLOBALNY_STAV_PROGRAMU_v3.18_2026-07-13.md` — stav staníc A0–A8, s výhradou, že aktuálnu navigáciu nahrádza novší current plan.
5. `theory/SK/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_SK.md` — neskoršie obmedzenia starších tvrdení L1–L7.
6. `Audit/AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md` — dôvod, prečo interné trojbodové pseudo-skóre nie je likelihood ani dôkaz prevahy nad ΛCDM.

Vonkajší kontext: Planck potvrdil dobrú konzistenciu šesťparametrového plochého ΛCDM s CMB; DESI DR2 uvádza, že BAO výsledky sú plochým ΛCDM dobre opísané, hoci kombinované analýzy motivujú ďalšie testy dynamickej tmavej energie. To neznamená, že ΛCDM je konečná fundamentálna teória, ale je to povinný empirický benchmark. [Planck 2018](https://doi.org/10.1051/0004-6361/201833910), [DESI DR2 Results II](https://arxiv.org/abs/2503.14738)

## 3. Porovnanie C1–C4 s aktuálnym stavom

| Strata | Čo požaduje príloha | Čo je v projekte naozaj podložené | Aktuálny stav |
|---|---|---|---|
| `C1` tvrdá konzistencia | identická celková konzervácia, kauzalita, unitarita, všeobecná kovariancia | A1-K1 má preverenú bilančnú konzerváciu na homogénnom backgrounde. P5 má `PASS_CONTRACT_PREFLIGHT_ONLY` pre konkrétny Bianchi/left-null kontrakt. Neexistuje však úplný kovariantný, multispecies a perturbatívny dôkaz celej teórie. | `REVIEW_CRITICAL` |
| `C2` experimentálne symetrie | Lorentz/boost, WEP, CPT, gauge a lokálna pozičná invariancia pod experimentálnymi medzami | Parita a absencia lineárnej disperzie sú historické mechanistické čítanie; plná boost invariancia zostáva otvorená. WEP, CPT, gauge a drift konštánt neboli odvodené ani presne testované pre bunkový mechanizmus. | `REVIEW_CRITICAL` |
| `C3` presná dynamika | PPN, BBN, CMB, lineárna dynamika a známe limity v správnej presnosti | `R²=0.9991` nie je priamy výpočet PPN parametra `gamma`, preto z neho nemožno vyvodiť rezíduum `10^-3` ani blízkosť Cassini limitu. `Delta N_eff=0.0535` je po PT1 iba historický podmienený odhad; plný CMB/Boltzmann výpočet je blokovaný A2/A3. | `REVIEW_BLOCKED_BY_A2_A3_A4` |
| `C4` observačná životaschopnosť | porovnanie s dátami cez vopred určené kill kritériá a likelihood | Existujú background a toy citlivosti, nie plná CMB+BAO+SN+RSD+lensing likelihood. `S8/H0` trojbodové čísla nie sú celkové `chi²`; A8 je blokované A2+A3. | `REVIEW_BLOCKED_BY_A2_A3_A8` |

### 3.1 C1 — príloha je správne prísna, ale jej aktuálne fajky sú príliš silné

Pravidlo „porušenie energie-hybnosti alebo kauzality okamžite zabíja krok“ je správne a je kompatibilné s projektovým auditom. Nesprávne by však bolo aktuálne písať pre celú teóriu:

- „`nabla_mu T^{mu nu}=0` je splnené presne“;
- „kauzalita je vynútená vetou VS-1“;
- „kovariancia je iba mierne napätie“.

Tieto formulácie prekračujú dôkazový rozsah. Súčet tokov v jednom backgroundovom alebo contract-preflight scope nie je dôkaz úplnej kovariantnej zachovanosti všetkých zložiek, hierarchií a perturbácií. A6 zostáva kriticky otvorený problém 3D rastového grafu, 4D kauzality a možného preferovaného rámca. Unitarita/Hilbertov priestor patrí do C5 dlhu, nie medzi splnené body C1.

### 3.2 C2 — lineárna disperzia nie je celá Lorentzova invariancia

Príloha správne rozlišuje lineárnu a kvadratickú modifikáciu disperzie. Jej záver však musí zostať úzky:

> Paritný argument môže byť kandidátom na zákaz konkrétneho lineárneho disperzného člena; nie je dôkazom plnej Lorentzovej grupy, boost invariancie, WEP, CPT ani gauge invariancie.

Preto sa starý náznak „Z1 prežíva vďaka parite“ nesmie preklopiť na C2 PASS. Aktuálny project state naďalej vyžaduje úplnú boost invarianciu alebo presne priznanie a test preferovaného rámca.

### 3.3 C3 — najdôležitejšia korekcia k PPN

`R²=0.9991` hodnotí kvalitu určitého fitu/simulácie. Parameter PPN `gamma` sa získava z koeficientov metriky a zo svetelného ohybu/Shapiro delay v definovanom slabom poli. Bez explicitného mapovania

```text
sieťový limit -> efektívna metrika -> PPN gamma -> merateľná veličina
```

nie je matematicky platné interpretovať `1-R²` ako `|gamma-1|`. C3 preto nemá stav „dva rády od Cassini“, ale stav **PPN ešte nebol vypočítaný**.

Rovnako CMB „kotva pipeline“ nie je CMB validácia. Aktuálny plán správne vyžaduje najprv kovariantné perturbácie, potom plný Boltzmannov riešič a až následne likelihood.

### 3.4 C4 — odchýlka od ΛCDM nie je sama osebe výhoda

V C4 sa model neposudzuje podľa blízkosti k ΛCDM, ale podľa likelihood reálnych dát. Príloha má v tomto princípe pravdu. Potrebuje však dve korekcie:

1. Odchýlka od ΛCDM je vedecky užitočná iba vtedy, ak bola predikovaná pred dátami a zlepší alebo aspoň udrží spoločnú likelihood pri férovom počte parametrov.
2. Žiadna odchýlka nie je „požadovaná“ pre fyzikálnu platnosť. Je potrebná iba pre preukázanie **empirickej prevahy** nad ΛCDM. Model môže byť konzistentný a stále nemať preukázanú prevahu.

Aktuálne predikčné riadky `N_eff`, tepelný relikt, `H0`, `S8`, `w0/wa`, `n_s`, `r` a `f_NL` majú rozdielny status. Najmä `Delta N_eff=0.0535` bol PT1 označený ako `SUPERSEDED IN SCOPE / CONDITIONAL ESTIMATE`, `H0=66.4` vyžaduje materiálny impact audit a S8/H0 gridy sú iba toy citlivosti. Preto sa v C4 dnes nesmie prideliť nový bod prevahy ani znížiť skóre ΛCDM cez interné trojbodové pseudo-skóre.

## 4. Vzťah kolmých osí: stanice A0–A8 a straty C1–C5

| Projektová stanica | Povinné straty konzistencie pred uzavretím |
|---|---|
| A1 background | C1 (bilančná konzervácia), C3 (pozitivita, limity), základ C4 iba ako background citlivosť |
| A2 perturbácie | C1 (Bianchi/total transfer), C2 (gauge/Lorentz scope), C3 (stabilita, well-posedness, nulové limity) |
| A3 Boltzmann | C1–C3 plus numerická reprodukcia štandardného benchmarku |
| A4 para/exit | C1 (energia/entropia), C3 (termodynamika), C4 (`N_eff`, BBN, CMB) |
| A5 primordiálne módy | C2 (kauzálny/gauge-invariantný prevod), C3 (spektrum), C4 (`n_s`, `r`, `f_NL`) |
| A6 3D/4D kauzalita | C1 a C2 priamo |
| A8 úplný fit | C4, ale iba po predchádzajúcich C1–C3 bránach |

Táto mapa je kontrolný nástroj. Nezavádza ďalšie percentá ani neoprávňuje preskočiť A2/A3 priamym fitom C4.

## 5. Je ΛCDM férovo bodovateľný „ako náš model“?

Nie jedným číslom. Oponent správne zachytil, že miešanie rôznych osí dáva zavádzajúce výsledky. Jeho návrh prideliť ΛCDM približne `100 %`, `50 %` alebo `0 %` podľa zvolenej interpretácie však ukazuje, že jednotné `P_global` nie je vhodný komparátor modelov.

### 5.1 Správne sú tri oddelené karty

| Karta | Otázka | Ako sa hodnotí | ΛCDM status dnes |
|---|---|---|---|
| `V` — platnosť/konzistencia | Porušuje model známy zákon v deklarovanom efektívnom scope? | hard gates a experimentálne limity | referenčný benchmark; veľmi silný, ale nie tvrdenie o úplnej kvantovej gravitácii |
| `D` — empirická evidencia | Ako si vedie na rovnakých dátach? | spoločná likelihood, kovariancie, priory, nuisance, penalizácia parametrov a slepý holdout | porovnávací baseline |
| `E` — vysvetľovací pôvod | Odvodzuje model nové nezávislé vzťahy a úspešné predikcie? | iba predikcie zafixované pred dátami; jasný scope | `N/A` pre pôvod zo siete, nie nula ani trest |

Pôvodné interné `ZHODA` môže zostať **diagnostikou vlastného programu**: ukazuje, koľko výsledkov bunková teória aktívne odvodila oproti tomu, že ich iba preberá. Nesmie sa však použiť ako výsledková tabuľka, v ktorej je ΛCDM penalizované za to, že nie je mikroskopickou teóriou siete.

Rovnako ΛCDM nemá dostať automaticky „100 % všetkého“: je veľmi úspešný efektívny kozmologický model, ale sám neuzatvára kvantovú gravitáciu, pôvod kozmologickej konštanty ani ďalšie C5 otázky. Správny zápis je `OUT_OF_SCOPE` alebo `N/A`, nie skrytý PASS.

### 5.2 Čo je objektívne platné o doterajších číslach

Tvrdenie „náš model má lepšie `chi²` pri menej parametroch“ **nie je momentálne platným komparatívnym výsledkom**. Projektový audit už uzavrel, že `chi2_3front`:

- nepoužíva pôvodné dátové vektory ani ich kovariancie;
- neobsahuje ani všetky veličiny, o ktorých sa tvrdí zlepšenie;
- používa post-data volené body;
- neobsahuje korektnú penalizáciu a nezávislý holdout.

Môže sa uchovať ako reprodukovaná toy citlivosť, nie ako evidencia `D` karty a nie ako porovnávacie skóre proti ΛCDM.

## 6. Je ΛCDM už zohľadnené v skriptoch?

### 6.1 Pravidlo existuje

Historické metodické pravidlo `P1` hovorí: **každá pipeline sa validuje na ΛCDM v tom istom behu**. Aktuálny plán navyše vyžaduje pred fyzikálnym adapterom reprodukovať štandardné ΛCDM spektrá v rovnakej pipeline.

### 6.2 Dnešný stav je čiastočný, nie globálne uzavretý

| Trieda výpočtu | Správny comparator | Stav |
|---|---|---|
| čistá algebraická identita/Bianchi/počty stavov | analytická identita alebo nulový limit; ΛCDM často `NOT_APPLICABLE` | P5 contract testy sú relevantné, ale nie sú dátovým porovnaním |
| backgroundový runner | explicitný limit `Q -> 0`, `A_f -> 0` a definovaný štandardný background | čiastočne; univerzálny K4 background je ešte neuzavretý |
| lineárne poruchy | rovnaké rovnice v nulovom coupling limite a porovnanie so štandardným solverom | otvorené v A2/P5 |
| Boltzmann/CMB/matter spectra | rovnaký CLASS/CAMB backend, presné parameter file, tolerancie, `lmax`, recombination a spectra | A3/G8 je blokované; štandardný smoke je iba architektonický preflight |
| likelihood a predikčná prevaha | rovnaké datasety, covariancie, priory, nuisance, parameter count a blind holdout | A8 nie je vykonaný |

Záver: ΛCDM je v metodike správne prítomný, ale **nemáme ešte univerzálny manifest**, ktorý by dokazoval uplatnenie P1 pri každom fyzikálne významnom runneri. Neznamená to, že všetky staršie skripty sú chybné; znamená to, že ich komparátorový rozsah sa nesmie predpokladať bez individuálneho auditu.

## 7. Navrhovaný comparator contract pre nové fyzikálne runnery

Nejde o nové pravidlo vedľa P1, ale o návrh jeho vykonateľnej predregistrácie. Tento návrh sa nestáva záväzným metodickým pravidlom, kým ho hlavný orchestrátor nezapíše po prijatí používateľom do zhodného SK/EN pracovného registra. Ak bude prijatý, každý budúci fyzikálne interpretačný runner má mať v Markdown preregistrácii:

```text
COMPARATOR_SCOPE: REQUIRED / NOT_APPLICABLE
WHY_NOT_APPLICABLE: [iba pri algebraickej alebo čisto lokálnej identite]
NULL_LIMIT_MAPPING: [presné parametre a limity]
LCDM_REFERENCE: [parameter file, dataset/version alebo analytický limit]
SAME_BACKEND: [solver, tolerancie, grid, lmax, recombination, gauge]
EXPECTED_BASELINE: [konkrétna hodnota/spektrum/identita a tolerancia]
COMPARATOR_RESULT: PASS / REVIEW / STOP_TECHNICAL
WHAT_THE_PASS_DOES_NOT_PROVE: [najmä nie prevahu modelu]
```

Navrhované pravidlá použitia:

1. Ak je `COMPARATOR_SCOPE=REQUIRED`, baseline sa vykoná v tom istom balíku alebo z rovnakého nemenného base/backendu.
2. Ak je `NOT_APPLICABLE`, musí byť uvedená presná analytická identita či nulový limit; „ΛCDM sa sem nehodí“ bez dôvodu neplatí.
3. Prechod baseline potvrdzuje implementáciu, nie bunkovú fyziku ani jej prevahu.
4. Ak nulový limit nerobí presne ΛCDM, dokument musí povedať, aký známy limit robí a prečo.
5. Až full likelihood používa kartu `D`; toy rezíduá, centrálny bod a samostatná χ² kotva ju nenahrádzajú.

## 8. Následný lacný audit po pauze fyzikálnych behov

Bez spustenia nového Pythonu sa má vytvoriť jeden read-only `P1 comparator coverage manifest` pre aktuálne živé a rozhodujúce historické runnery. Pri každom uvedie:

| runner/gate | fyzikálny scope | comparator required? | skutočne existujúci benchmark | stav P1 | potrebný doplnok |
|---|---|---:|---|---|---|

Priorita klasifikácie:

1. `A1-K1` background a jeho presný nulový limit;
2. `A2-K4/P5` seed/constraint runnery;
3. budúci `A3/G8` CLASS/HyRec backend;
4. historické S8/H0 toy skripty — označiť ich iba ako citlivosti, nie ako model comparison.

Tento manifest je dokumentačná kontrola. Nezvyšuje hĺbku, nemení skóre a nespúšťa drahý výpočet.

## 9. Konečný rozsudok

1. Navrhnutá hierarchia je hodnotná ako **C1–C5 priečna mapa mantinelov**.
2. V aktuálnom stave neprešla žiadna globálna strata C1–C4 pre celú bunkovú teóriu; C1 a C2 sú kritické review, C3 a C4 sú blokované otvorenými stanicami.
3. Aktuálny stav A1-K1 a A2-K4 zostáva nezmenený: backgroundový kandidát prežíva, A2-K4 je živá na `60/100`, A3/A8 sú blokované.
4. ΛCDM musí byť v porovnateľných numerických pipeline povinný benchmark, nie protivník, ktorému sa odoberajú body za inú ambíciu.
5. Neexistuje dnešné objektívne číslo „koľko bodov má ΛCDM oproti nám“. Existujú tri samostatné karty `V/D/E`; iba karta `D` môže neskôr rozhodovať o empirickej prevahe.
6. Interné `P_global`, `ZHODA` a pseudo-`chi²_3front` sa nesmú používať ako priame porovnávacie skóre proti ΛCDM.
