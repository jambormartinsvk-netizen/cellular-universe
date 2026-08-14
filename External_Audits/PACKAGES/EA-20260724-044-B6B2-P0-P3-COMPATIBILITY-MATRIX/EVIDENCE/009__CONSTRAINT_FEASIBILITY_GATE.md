# Brána realizovateľnosti — neprázdny prienik mantinelov

**Pracovný identifikátor:** `FS-GATE-01`  
**Vrstva:** `tracks/`; `WORKING / NOT_RELEASED`  
**Dátum:** 2026-07-16  
**Doplnené:** 2026-07-17 — triedy dôkazu a štítky základu rozhodnutia  
**Účel:** pred voľbou konkrétnej funkcie, akcie alebo collision kernelu
rozhodnúť, či vôbec môže existovať objekt spĺňajúci všetky povinné
fyzikálne mantinely súčasne.

## 1. Matematická definícia

Nech `X_K` je presne definovaný priestor kandidátnych objektov koľaje `K`:
funkcií, kernelov alebo akcií s určenou doménou, kodoménou, regularitou,
rozmermi a parametrami. Každý mantinel vytvorí podmnožinu

```text
C_i = {F in X_K : F spĺňa mantinel i}.
```

Prípustná množina je

```text
F_K = intersection_i C_i.
```

Všetky podmienky musia platiť pre **ten istý objekt, ten istý parameterový
bod a tie isté okrajové podmienky**. Nestačí, ak každý mantinel prejde s
inou funkciou alebo inou hodnotou parametra.

### 1.1 Behaviorálny obal pred poznaním funkcie

Presný mikroskopický tvar nie je potrebný na prvé vylučovanie. Najprv sa
definuje množina dovoleného vstupno-výstupného správania

```text
B_K = intersection_j B_j,
```

kde `B_j` obsahujú pozorované alebo zákonom vynútené nulové body, znamienka,
monotónnosť, konečnosť, prahy, saturáciu a energetické hranice. Každá
fyzická realizácia musí mať svoje výstupy v `B_K`, teda

```text
image(F_K) subset B_K.
```

Ak `B_K` je prázdna, nijaká presná funkcia ju nemôže zachrániť. Je to
analógia ohňa: netreba poznať chémiu horenia, aby kombinácia „bez paliva
horí“ alebo „čím viac vody, tým povinne silnejšie horí“ odporovala
pozorovanému správaniu v deklarovanom rozsahu. Ak `B_K` nie je prázdna,
vieme iba, že behaviorálne mantinely sa nebili; existencia fyzikálnej
funkcie ešte nie je dokázaná.

Behaviorálny pas preto vždy začína tabuľkou:

| Vstup/podmienka | Povinný výstup | Znamienko alebo trend | Okraj/nulový bod | Zdroj poznania |
|---|---|---|---|---|

## 2. Vnorené úrovne

Existencia sa preveruje postupne:

```text
F_K^(3) superset F_K^(5) superset F_K^(6)
        superset F_K^(7) superset F_K^(8-9),
```

kde:

- `F_K^(3)` zahŕňa identitu koľaje a G1–G3: background, conservation,
  lokálnosť, kovarianciu, pozitivitu, nulové limity a úplný operátor;
- `F_K^(5)` navyše zahŕňa úplné G4 rovnice a regulárnu G5 bázu;
- `F_K^(6)` pridáva ghost/gradient/high-`k` a kauzálnu stabilitu;
- `F_K^(7)` pridáva úplnú Einstein–Boltzmannovu realizáciu;
- `F_K^(8-9)` pridáva CMB-normalizované spektrá a predregistrované
  pozorovacie likelihoody.

Prázdnosť ktorejkoľvek skoršej množiny znamená prázdnosť všetkých jej
potomkov. Neprázdnosť skorej množiny nedokazuje neprázdnosť neskoršej.

## 3. Povinné triedy mantinelov

Každý pas musí uviesť:

1. **identitu objektu:** doména, kodoména, tenzorový typ, stavové premenné,
   parametre a rozdiel od existujúcich koľají;
2. **rodičovský ledger:** reprodukciu deklarovaného A1 backgroundu,
   `sum_A Q_A^mu=0`, kladné hustoty a `H^2`, žiadne perturbatívne `k` v
   backgrounde;
3. **lokálnosť a kauzalitu:** dovolené lokálne stavy, retarded odozvu,
   žiadny budúci stav ani skrytý kozmický čas;
4. **pozitivitu a termodynamiku:** pozitívny production/noise kernel,
   pasivitu alebo nezápornú produkciu entropie, žiadne ghosty;
5. **okrajové a nulové hodnoty:** nulová väzba, zánik každého média,
   singularity rovnice stavu, skorý/neskorý čas, `k->0`, `k->infinity` a
   podľa potreby cutoff;
6. **poruchové mantinely:** úplné `delta Q_A`, gauge/frame mapa, Bianchi,
   regulárne módy, high-`k` charakteristiky, noise a anizotropný stres;
7. **predikčnosť:** pôvod každej konštanty, zákaz druhého post-data fitu a
   počet zostávajúcich voľných funkcií;
8. **pozorovania:** až po tvrdých fyzikálnych mantineloch predregistrované
   BBN/CMB/BAO/lensing/rastové intervaly, nie iba trafenie centrálnej
   hodnoty `S8` alebo `H0`.

Každý riadok obsahuje zdroj rovnice, jednotky, presný test, stav a čo test
nepokrýva.

## 4. Povolené stavy

| Stav | Presný význam |
|---|---|
| `NOT_MAPPED` | chýba aspoň jeden povinný mantinel alebo jeho matematický tvar |
| `BEHAVIORAL_OPEN` | známe vstupno-výstupné mantinely majú neprázdny prienik; fyzický svedok ešte nemusí existovať |
| `BEHAVIORAL_EMPTY_SCOPE` | pozorované alebo zákonom vynútené správania si v presnom rozsahu odporujú; nijaká funkcia v tomto rozsahu neexistuje |
| `UNDETERMINED_REVIEW` | mantinely sú zmapované iba čiastočne alebo zatiaľ nemáme svedka ani certifikát prázdnosti |
| `NONEMPTY_WITNESS` | jeden explicitný objekt spĺňa všetky mantinely deklarovanej úrovne pri tom istom parameterovom bode |
| `EMPTY_CERTIFIED_SCOPE` | analytický rozpor, dual certificate alebo úplná certifikovaná hranica dokazuje prázdny prienik presne uvedeného priestoru |

`NONEMPTY_WITNESS` nie je dôkaz jedinečnosti ani automatický PASS G5.
`EMPTY_CERTIFIED_SCOPE` zabíja iba presne definovaný priestor `X_K`.
`BEHAVIORAL_OPEN` nepridáva skóre; povoľuje iba pokračovať v hľadaní
realizácie. `BEHAVIORAL_EMPTY_SCOPE` je platný STOP podtriedy, ak sú všetky
jeho vstupno-výstupné hranice a rozsah auditované.

## 5. Čo nie je dôkaz prázdnosti

- konečný grid, ktorý nenašiel riešenie;
- zlyhanie jedného ansatzu, solvera alebo počiatočnej hodnoty;
- samostatné minimá jednotlivých rezíduí pri rôznych parametroch;
- numerická hodnota pod toleranciou bez analytickej alebo intervalovej
  kontroly;
- neexistencia dnes známeho mikrofyzického modelu.

Prázdnosť sa certifikuje napríklad priamym rozporom okrajových hodnôt,
znamienkovou vetou, pozitivitou matice, monotónnou hranicou, intervalovou
aritmetikou alebo optimalizačným dual certificate. Dôvod sa zapisuje ako
**neexistencia spoločnej množiny výsledkov**, nie ako „funkciu sme nenašli“.

## 6. Skóre, história a release

- mapovanie mantinelov ani `NONEMPTY_WITNESS` samo nepridáva body;
- body vzniknú až prejdením príslušnej kanonickej brány G1–G10;
- mŕtve podmnožiny, skripty a výpočty sa nemažú;
- každý certifikát uvedie rozsah a nové dcéry odvodené z odstránenej
  príčiny zlyhania;
- pracovný výsledok zostáva v `tracks`; do `theory` sa konsoliduje iba pri
  release candidate podľa AR70;
- `NONEMPTY_WITNESS` sám nespúšťa novú predikciu. `EMPTY_CERTIFIED_SCOPE`
  spustí release review iba ak mení už publikovaný mechanizmus alebo číslo.

## 7. Povinný výstup

Každá koľaj alebo konkrétna dcéra používa tabuľku:

| Mantinel | Rovnica/nerovnosť a doména | Povinná okrajová hodnota | Dôkaz/test | Stav | Nepokrýva |
|---|---|---|---|---|---|

Na konci uvedie stav `F_K^(n)`, explicitného svedka alebo certifikát
prázdnosti a počet zostávajúcich voľných funkcií, parametrov a počiatočných
podmienok.

Pred touto tabuľkou uvedie stav behaviorálneho obalu `B_K`. Mikrofyzický
výpočet sa nezačína, kým behaviorálne mantinely obsahujú nevyriešený priamy
rozpor.

## 8. Trieda dôkazu a základ rozhodnutia

Každý mantinel v pase dostane triedu dôkazu; tieto triedy sa nesčítavajú do
jedného čísla:

| Trieda | Zdroj | Rozhodovacia sila | Povinný obsah |
|---|---|---|---|
| `E0_EXACT` | matematická identita, symetria alebo invariant odvodený v scope | tvrdý mantinel | dôkaz a doména platnosti |
| `E1_DIRECT_MEASUREMENT` | priame meranie | tvrdý až po mapovaní modelu na observablu | experiment, CL/likelihood, štatistická a systematická chyba, znamienko/sektor, jednotky |
| `E2_REFERENCE_MODEL` | ΛCDM, GR/SM alebo iný štandardný efektívny model | comparator/nulový limit, nie automatický STOP | spoločný backend alebo analytický limit a nonclaims |
| `E3_PROVISIONAL` | anomália, modelovo závislá inferencia, fit alebo hypotéza | návrhové vodidlo; samo nevylučuje | zdroj, predpoklady, otvorené systematiky |

Pri `E1_DIRECT_MEASUREMENT` sa nepoužíva iba centrálna hodnota: pas uvedie
interval, confidence level, systematiky a presnú transformáciu modelovej
premennej na meranú veličinu. Nezhoda s `E2_REFERENCE_MODEL` znamená iba
potrebu testu proti dátam, nie fyzikálny rozpor.

Každý no-go alebo STOP navyše nesie štítok základu rozhodnutia:

| Štítok | Význam | Účinok |
|---|---|---|
| `PRECHECK_EXCLUDED_SCOPE` | úplné mapovanie `E0` alebo `E1` vylúči presnú podtriedu pred konštrukciou funkcie | `NO_CANDIDATE_RUN`; platí iba v scope a nepridáva kanonickú hĺbku |
| `COMPUTED_STOP_SCOPE` | úplný predregistrovaný analytický alebo numerický test kandidáta fyzikálne zlyhal | výpočtový STOP presne testovaného scope |
| `OBSERVATIONAL_STOP_SCOPE` | úplný model -> observabla -> likelihood reťazec je mimo zmrazeného intervalu | STOP až po chybách, systematikách a parametroch |
| `REFERENCE_MISMATCH_ONLY` | nezhoda s `E2` bez priameho dátového rozporu | `REVIEW`, nikdy sama STOP |
| `TECHNICAL_STOP` | skript, prostredie alebo backend | nie je fyzikálny STOP |

`BEHAVIORAL_EMPTY_SCOPE` alebo `EMPTY_CERTIFIED_SCOPE` s úplným
certifikátom teda môže byť `PRECHECK_EXCLUDED_SCOPE`. Je to hodnotný výsledok,
ktorý šetrí zbytočné behy, ale nesmie sa sumarizovať ako `COMPUTED_STOP_SCOPE`
ani ako prejdená kanonická brána.
