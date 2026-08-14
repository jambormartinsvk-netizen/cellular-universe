# Audit Lorentzovej disperzie, WEP a stop kritérií voči ΛCDM

**Dátum:** 2026-07-17  
**Stav:** `AUTHORITATIVE_SCOPE_AUDIT / NO_ROUTE_VERDICT_CHANGE`  
**Rozsah:** overenie tvrdení o lineárnej/kvadratickej fotónovej disperzii a MICROSCOPE WEP; pravidlo, ktoré druhy tvrdení ΛCDM môžu byť STOP relevantné  
**Nemení:** aktuálnu hĺbku A2-K4 `60/100`, žiadny stav A1–A8, žiadny release ani predikčnú tabuľku

## 1. Rozhodnutie o tom, čo je STOP relevantné

Pouhá predpoveď ΛCDM nie je STOP podmienka pre bunkovú teóriu. Relevantné sú iba tieto triedy:

| Trieda | Význam | Použitie v audite bunkovej teórie |
|---|---|---|
| `S0` | presná matematická konzistencia: Bianchi, zachovanie, stabilita, dobre položený limit | invariantný rozpor je okamžitý STOP v presne testovanom scope |
| `S1` | priame meranie s publikovanou neistotou, systematikami, confidence intervalom a jasne zmapovanou observablou | môže byť STOP, ak model po predregistrovanom mapovaní leží mimo vopred určeného intervalu |
| `S2` | predikcia/parametrizácia štandardného modelu alebo ΛCDM | povinný benchmark a nulový limit, ale nie automatický STOP pre odlišný model |
| `S3` | modelovo závislá inferencia, napätie medzi datasetmi alebo otvorená anomália | výskumný mantinel; bez samostatného plného likelihoodu nie je STOP |

Pre `S1` platí: do skriptu sa nesmie vložiť iba centrálna hodnota. Preregistrácia musí uviesť experiment, dátový vektor alebo likelihood, confidence level, štatistickú a systematickú chybu, znamienko/modelový sektor a presné mapovanie modelového parametra na meranú observablu.

Tým sa splní súčasne obava z dvoch opačných chýb:

1. nevyhlásiť smrť len preto, že sa model líši od ΛCDM;
2. neprehliadnuť priamo meraný rozpor tým, že sa chyba alebo systematika zjednoduší na jednu nulovú hranicu.

## 2. Fotónová Lorentzova disperzia — presný rozsah meraní

Použitá parametrizácia je

$$
E^2 \simeq p^2c^2\left[1-s\left(\frac{E}{E_{\rm QG,n}}\right)^n\right],
\qquad s=\pm1,
$$

kde `n=1` je lineárna a `n=2` kvadratická korekcia rýchlosti fotónu. Ide o konkrétny time-of-flight sektor, nie o dôkaz celej Lorentzovej grupy.

### 2.1 Overené limity

| Zdroj | Sektor | Výsledok | Správne čítanie |
|---|---|---|---|
| Fermi-LAT, GRB 090510 (2013) | lineárny, subluminálny | `E_QG,1 > 7.6 E_Pl` pri 95 % CL | tvrdenie v prílohe je správne, ale má konkrétne znamienko a predpoklady o zdrojovej disperzii |
| Fermi-LAT, GRB 090510 (2013) | kvadratický, subluminálny | `E_QG,2 > 1.3×10^11 GeV` pri 95 % CL | slabšia než lineárna medza v Planckových jednotkách |
| LHAASO, GRB 221009A (2024) | lineárny | približne `E_QG,1 > 10 E_Pl` pri 95 % CL v ich kombinovanom zhrnutí; detailné hranice závisia od znamienka/metódy | nezistila sa LIV časová odozva; limit je likelihoodový, nie identita |
| LHAASO, GRB 221009A (2024) | kvadratický | `E_QG,2 > 6×10^-8 E_Pl` v zhrnutí; detailný ML výsledok približne `6.9–7.0×10^11 GeV` podľa znamienka | hranica je asi o sedem rádov pod `E_Pl`, teda Planckom potlačený kvadratický člen s koeficientom rádu 1 je bezpečne pod týmto limitom |

Zdroje: [Fermi-LAT GRB limits](https://arxiv.org/abs/1305.3463), [LHAASO GRB 221009A](https://arxiv.org/abs/2402.06009).

LHAASO výslovne pracuje s profile likelihoodom, 95 % intervalmi, vývojom spektra a EBL modelom. Zmena EBL modelu v ich analýze posunula lineárne limity približne o 12–18 % a kvadratické približne o 5–6 %. Tieto neistoty sú súčasťou dôkazu; nesmú sa v projekte nahradiť textom „tolerancia presne nula“.

### 2.2 Čo znamenajú tieto medze pre koeficienty

Ak sa model píše ako

$$
v(E)=c\left[1+\xi_1\frac{E}{E_{\rm Pl}}+\xi_2\left(\frac{E}{E_{\rm Pl}}\right)^2+\cdots\right],
$$

potom limit na mierku nie je priamo limitom „nuly“:

- lineárny limit `E_QG,1 > 7.6–10 E_Pl` zodpovedá pri tejto konvencii približne `|xi_1| < 0.13–0.10` pre príslušný znamienkový/time-of-flight sektor;
- kvadratický limit `E_QG,2 > 6×10^-8 E_Pl` stále povoľuje `xi_2` mnohonásobne väčšie než jedna podľa zvolenej normalizácie; preto je `xi_2` rádu jedna pri Planckovom potlačení ďaleko v bezpečnej oblasti.

Záver: tvrdenie „lineárny Planckom potlačený efekt rádu jedna je silne vylúčený; kvadratický rádu jedna je zatiaľ povolený“ je správne. Tvrdenie „experiment dokázal `xi_1=0` exaktne“ je nesprávne.

## 3. Parita nie je sama osebe dôkaz nulového lineárneho člena

Veta „parita zakazuje lineárny člen“ nie je zatiaľ vo všeobecnosti dokázaná pre bunkovú teóriu.

Pri dokonale symetrickej, lokálnej a analytickej lattice derivácii môže disperzia začínať kvadratickou korekciou. To je sľubná mechanistická možnosť. Samotná priestorová inverzia však nestačí ako univerzálny zákaz všetkých `n=1` efektov: v efektívnych teóriách existujú rotačne invariantné a gauge invariantné operátory dimenzie päť, ktoré vedú k lineárnej energetickej zmene rýchlosti a k polarizačným/birefringenčným stopám. [SME photon-sector classification](https://arxiv.org/abs/0905.0031), [dimension-5 photon constraints](https://arxiv.org/abs/1701.00437)

Pre bunkovú teóriu teda platí:

| Tvrdenie | Stav |
|---|---|
| Naivná diskrétna sieť vždy dá lineárnu disperziu | `FALSE_AS_UNIVERSAL_STATEMENT` |
| Symetrická analytická sieť môže dať prvú kvadratickú korekciu | `PHYSICALLY_PLAUSIBLE / NOT_YET_DERIVED_HERE` |
| Parita sama dokazuje `xi_1=0` pre aktuálny model | `NOT_YET_PROVEN` |
| Model prežil lineárnu LIV bránu | `REVIEW`; najprv treba odvodiť efektívny fotónový operátor, jeho symetrie, znamienko, polarizáciu a radiatívnu stabilitu |

Správne kill kritérium nie je „každý nenulový lineárny člen okamžite smrť“, ale:

> Ak odvodený a stabilný efektívny fotónový sektor bunkovej teórie predpovie v testovanom time-of-flight/polarizačnom kanáli koeficient mimo vopred zvoleného 95 % (alebo prísnejšieho) experimentálneho intervalu, príslušná implementácia zomrie. Ak model odvodí presný selekčný zákon `xi_1=0`, je to silnejší PASS, nie požiadavka vložená do modelu post hoc.

Plná Lorentzova/boost invariancia zostáva širšia brána než disperzia fotónov. PASS v tomto jednom sektore ju nemôže nahradiť.

## 4. MICROSCOPE a slabý princíp ekvivalencie

MICROSCOPE nemeral abstraktnú univerzálnu hodnotu `eta` bez chyby. Meral rozdiel vo voľnom páde konkrétnych zliatin titánu a platiny v gravitačnom poli Zeme. Finálny výsledok je

$$
\eta({\rm Ti,Pt}) = [-1.5 \pm 2.3_{\rm stat} \pm 1.5_{\rm syst}]\times10^{-15}.
$$

Ide o 1σ štatistickú chybu s osobitne uvedenou systematikou. [MICROSCOPE final result](https://arxiv.org/abs/2209.15487)

Preto veta `|eta| < 2.7×10^-15` nie je presná:

- `sqrt(2.3^2+1.5^2)=2.7` je približná kombinovaná **1σ** neistota, nie 95 % horná hranica absolútnej hodnoty;
- pri jednoduchom gaussovskom spojení by 95 % interval bol približne `[-6.9,+3.9]×10^-15`; to je iba ilustrácia, nie náhrada publikovaného likelihoodu;
- pri budúcom STOP teste sa musí použiť publikovaný výsledok a vopred zvolená konvencia CL, nie skrytá zmena medzi 1σ a 95 %.

### 4.1 Čo musí predpovedať bunková teória

„Hmota je popol“ samo osebe ešte nehovorí, či titán a platina padajú rovnako. Treba odvodiť aspoň jedno z dvoch:

1. **univerzálne metrické viazanie:** všetka pokojová energia, väzbová energia a príslušné mikrofyzikálne zložky tela sa viažu na tú istú efektívnu metriku. Vtedy je `eta=0` v test-body limite dôsledok modelu;
2. **neuniverzálne viazanie:** model dá explicitnú kompozične závislú hodnotu `eta(Ti,Pt)` vrátane nukleónov, elektrónov a väzbových energií. Tá musí ležať v predregistrovanom intervale merania.

Tvrdenie „model musí presne predpovedať `eta=0`“ je preto príliš silné ako empirická požiadavka. Správnejšie je: model nesmie predpovedať kompozičnú diferenciálnu akceleráciu, ktorá je podľa deklarovaného mapovania vylúčená MICROSCOPE alebo ďalšími relevantnými testami.

Aktuálne nemáme mikrofyzikálnu mapu `popol -> zloženie Ti/Pt -> efektívny náboj/masa`. WEP je teda priamy a veľmi dôležitý budúci C2 test, ale nie dnešný PASS ani STOP celej teórie.

## 5. Správny postup pre budúce skripty

### 5.1 LIV preregistrácia

Pred výpočtom sa zapíše:

```text
observable = photon time-of-flight / polarization / laboratory SME channel
operator_basis = exact effective photon operator
symmetry_protection = exact stated symmetry plus derivation
coefficient_convention = xi_n or E_QG,n, including sign
null_limit = xi_n -> 0
measurement = source + CL + source/systematic model
pass = coefficient within frozen interval
stop = coefficient outside frozen interval after required robustness checks
nonclaim = time-of-flight PASS is not full boost-invariance PASS
```

### 5.2 WEP preregistrácia

```text
observable = eta(A,B)
composition_map = nuclear/electromagnetic/binding-energy content of A,B
coupling_map = how the cellular mechanism couples to each contribution
limit_source = original MICROSCOPE likelihood or a stated CL reconstruction
pass = predicted eta(Ti,Pt) within frozen interval
stop = predicted eta outside interval
nonclaim = Ti/Pt PASS alone is not all EP tests
```

Tieto položky sú návrh na vykonanie už existujúcej metodiky P1 a S1; nestávajú sa novým globálnym pravidlom, kým nie sú prijaté a zapísané do zhodného SK/EN pracovného registra.

## 6. Konečný rozsudok

1. Nedokázané alebo modelovo závislé predpovede ΛCDM nie sú automatické STOP podmienky pre bunkovú teóriu.
2. Priame experimentálne limity sú STOP relevantné iba s ich chybami, systematikami, confidence levelom a presným mapovaním modelu na meranú observablu.
3. Tvrdenie `E_QG,1 > 7.6 E_Pl` je pre konkrétny Fermi subluminálny lineárny sektor pravdivé; novšie LHAASO limity sú porovnateľné až prísnejšie podľa metódy a znamienka.
4. Kvadratická hranica rádu `6×10^-8 E_Pl` je správna ako dolná medza mierky, nie ako „nulová tolerancia“ ani limit `xi_2`.
5. Experimenty nevyžadujú exaktne `xi_1=0`; môžu však vylúčiť lineárny Planckom potlačený efekt s koeficientom rádu jedna. Parita sama zatiaľ nedokazuje ochranu aktuálneho modelu.
6. MICROSCOPE nedáva `|eta|<2.7×10^-15` ako hotovú hranicu; dáva centrálnu hodnotu so štatistickou a systematickou neistotou. Bunková teória musí najprv odvodiť kompozičný coupling, až potom sa dá vykonať WEP PASS/STOP.
