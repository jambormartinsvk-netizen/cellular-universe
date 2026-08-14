# B6b-2.4 — P4-v1 MF1/F01∩F03 dependency freeze a jediný witness pokus

**Task:** `A2K4-B6B2-4-P4-V1-MF1-WITNESS-20260724-98`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.4/P4-v1`  
**Autor teórie a epistemického smeru:** Martin Jambor  
**Autor analytického pokusu:** Codex, hlavný orchestrátor  
**Stav:** `REVIEW_P4_V1_DEPENDENCY_FREEZE_BLOCKED_BEFORE_WITNESS / NO_RUN / NO_PYTHON`

## 1. Presný cieľ a hranica pokusu

Tento dokument vykonáva jediný povolený `DERIVATION_P4` pokus po matici
P0–P3. Nemá uhádnuť nepozorovateľnú Planckovu mikrofyziku. Má zistiť, či sa
z dnešného korpusu dá bez nového autorovho axiómu alebo fundamentálneho poľa
zostaviť aspoň jeden explicitný lokálny svedok fyzickej neprázdnosti.

Poradie je fail-closed:

```text
lexikografický výber jedného base/fiberu
  -> candidate-local freeze D03/D05/D07/D09/D11
    -> iba ak všetkých päť blokov prejde: jeden explicitný ansatz
      -> analytické M0–M14
        -> hard stop.
```

Ak dependency freeze neprejde, explicitný ansatz sa nesmie doplniť
ľubovoľnými funkciami. Taký výsledok nie je STOP fiberu ani rodiny.

## 2. Zmrazený lexikografický výber

Použité poradie bolo:

1. kompatibilita s A0–A6, `SM_v1` a autorom schválenou topológiou B6-C0;
2. nulový počet nových autorových axióm a fundamentálnych polí;
3. minimum sektorov, carrierov, stavov a cohort stages;
4. minimum nezávislých funkcií a konštánt;
5. analytická kontrolovateľnosť M0–M14 a recovery limitov;
6. až pri úplnej remíze rozlišovacia sila v `R_test`.

S8, H0, legacy para, dnešný `M/C` pomer ani očakávaný úspech nevstúpili do
výberu.

| Kandidát | Prvý rozhodujúci rozdiel | Lexikografický výsledok |
|---|---|---|
| `B-MF1 + F01∩F03` | používa existujúce division opportunities, uzavretý prompt `e->s+M` a completion bez extra produktu `p_C=p_M` | **prvý attempt target** |
| `B-MF2` | vyžaduje samostatný internal clock alebo novú identitu phase-winding = event | neskorší |
| `B-MF3S/MF3A` | pridáva dva režimy, diskriminátor, prah a transition ledger | neskorší |
| `B-MF4/F07` | pridáva najmenej dva súbežné kanály a cross-channel covariance | neskorší |
| `B-RES/F09` | pridáva celú novú reprezentáciu | posledný residual |

Vybraný target je teda

```text
P4_V1_TARGET = B-MF1 + F01(closed parent inventory)
                       intersect F03(momentum-preserving completion).
```

`F01∩F03` je kompatibilný prienik dvoch ortogonálnych schema atribútov, nie
nová MF rodina. Výber znamená iba „najmenej zložitý prvý pokus“, nie
preferenciu, pravdepodobnosť alebo fyzickú existenciu.

## 3. Čo target smie zdediť bez nového vstupu

Z B6-C0 je už autorom schválená iba topológia:

```text
PARENT_EVENT_TOPOLOGY:     e -> s + M
COMPLETION_TOPOLOGY:       M -> C
PARENT_EVENT_CLASS:        local cellular digestion first passage
FORMAL_ENERGY_IDENTITY:     p_J^mu = Delta P_e^mu(C_x), zatiaľ nevyhodnotiteľná
PARENT_CONSERVATION:       p_J^mu = p_s^mu + p_M^mu
MINIMAL_COMPLETION_OPTION: p_C^mu = p_M^mu
```

Topológia C0 sama nedodáva evaluovateľný `C_x`, frame, transportnú konvenciu
ani event-energy law. Posledný riadok je najmenší F03/D08 candidate option,
nie súčasť dôkazu D05. Nie je tvrdením, že príroda
musí zvoliť momentum-preserving relabeling. Ak by completion odnášal ďalšiu
energiu/hybnosť, potreboval by explicitný produkt a target by prešiel do
zložitejšieho fiberu F04.

MF1 pridáva iba nutnú podmienku

```text
dR_D = dR_div Pi_D(dp,dmarks|Y_div),
0 <= dR_D <= dR_div,
```

ale dnešný korpus neurčuje `dR_div` ani `Pi_D`.

## 4. Candidate-local dependency freeze

### 4.1 D03 — division opportunity, event rate a identita

Korpus poskytuje iba:

- backgroundovú kinematiku `N_cell proportional a^3`;
- možnosť `R_div ~ n_cell Theta`, nie odvodenú lokálnu rovnosť;
- MF1 podmienku, že trávenie nemôže nastať mimo fyzicky identifikovaného
  delenia;
- first-passage/no-double-count bookkeeping B6-C0.

Chýbajú tri potrebné identity:

```text
R_div(Y_div)                         -- lokálna invariantná miera delení,
pi_D(Y_div) in [0,1]                 -- thinning: ktoré delenie je trávenie,
PARENT_EVENT_ID(div,cohort,worldline)-- jednoznačná lokálna eventová mapa.
```

A7 výslovne neurčuje mikroskopický počet produktových pokusov a A2 réžia
nie je product-energy source. Voľby `pi_D=1`, `pi_D=delta`, Poisson thinning
alebo prah podľa energie by preto boli nové fyzikálne hypotézy, nie odvodenie.

```text
D03_FREEZE = FAIL
FIRST_EXACT_BLOCKER = DIVISION_OPPORTUNITY_TO_DIGESTION_EVENT_MAP_MISSING
CURRENT_CLASS = OPEN_DERIVATION
DIRECT_UNDERIVED_SELECTION = EXPLICIT_CANDIDATE_HYPOTHESIS_OR_NEW_AUTHOR_INPUT
```

Toto je prvý hard blocker a samo stačí zastaviť explicitný witness.

### 4.2 D05 — poradie steam/matter/ash

Na candidate-local topologickej úrovni možno priamo z autorom schváleného
C0 zmraziť:

```text
e -> s + M       prompt parent vertex,
M -> C           sekvenčný completion vertex.
```

Osobitná voľba `p_C=p_M` je netestovaný minimálny F03/D08 kinematický
option targetu; nie je evidenciou pre D05. Topológia neurčuje completion
time, hazard ani completion kinematiku.

```text
D05_TOPOLOGY_FREEZE = PASS_FROM_AUTHOR_APPROVED_C0
F03_KINEMATIC_OPTION = p_C=p_M / CANDIDATE_LOCAL_UNTESTED
D05_DYNAMICS = OPEN_UNTIL_D07_AND_D11
```

### 4.3 D07 — source-off a completion tail

MF1 sám nevypína division opportunities po vyčerpaní skorého rezervoára.
Treba odvodiť aspoň jednu z ekvivalentných fyzických väzieb:

```text
n_e,act -> 0  => dR_D -> 0,
pi_D(Y_div,e) -> 0 pri empty reservoir,
alebo E_J -> 0 tak, aby R_D <E_J> -> 0,
```

pričom nesmie ísť o voľný kozmický čas. Pre dobiehajúce M kohorty navyše
chýba energy-finite/integrable completion law.

```text
D07_FREEZE = FAIL_INDEPENDENT_OF_D03
MISSING = LOCAL_RESERVOIR_AVAILABILITY_GATE + COMPLETION_TAIL_LAW
```

### 4.4 D09 — steam režim

Korpus neprikazuje, či prompt steam vzniká:

- collisionless a relativistický;
- thermalizovaný a neskôr decoupled;
- alebo v inom explicitne uzavretom režime.

Voľba „collisionless od birth“ by minimalizovala počet interakcií, ale stále
je fyzikálnou hypotézou. Bez dispersion/collision operatora nemožno uzavrieť
pressure, shear, entropy, characteristic cone ani noise.

```text
D09_FREEZE = FAIL_INDEPENDENT_OF_D03
MISSING = STEAM_DISPERSION_AND_COLLISION_OR_DECOUPLING_CONTRACT
```

### 4.5 D11 — residue, recovery a nulové limity

Podmienené `rho_s proportional a^-4` platí až pre uzavretý collisionless
relativistický steam režim. Candidate má topologický completion `M->C`, ale
nemá `omega_C`, cohort-age distribution ani odvodený `Q_M_to_C`. Preto sa
nedá dokázať úplný source-off/recovery limit ani oddelenie všetkých
parent/completion noise momentov.

```text
D11_FREEZE = FAIL_DOWNSTREAM_OF_D07_COMPLETION_AND_D09_STEAM_REGIME
MISSING = COMPLETION_HAZARD_OR_FIRST_PASSAGE_LAW + STEAM_RESIDUE_LAW
```

## 5. Výsledok jediného P4-v1 pokusu

Dependency freeze neprešiel už na D03. V súlade s predregistráciou sa preto
nevytvoril explicitný event kernel, mark distribution, collision operator
ani M0–M14 „witness“ tabuľka s domyslenými hodnotami.

```text
P4_V1_ATTEMPT_TARGET = B-MF1 + F01∩F03
DEPENDENCY_FREEZE = FAIL_BEFORE_WITNESS
EXPLICIT_ANSATZ_CONSTRUCTED = false
M0_M14_EXECUTED = false
NONEMPTY_WITNESS = NOT_ESTABLISHED
TARGET_ANSATZ_EXCLUDED = false
F01_F03_FIBER_EXCLUDED = false
MF1_EXCLUDED = false
OTHER_FIBERS_OR_FAMILIES_TESTED = false
```

Neúspech nie je dôkaz, že MF1 alebo teória je nemožná. Dokazuje užší
procesný fakt: dnešné rovnice neurčujú ani najjednoduchší explicitný
division-locked svedok bez doplnenia event-selection, steam a completion
fyziky.

## 6. Získaný mantinel chýbajúcej funkcie

Aj bez svedka sa blocker zúžil na malý candidate-local bridge, nie na
neurčitú otázku „čo sa deje v Planckovej bunke“. Najmenšia chýbajúca sada je

```text
K_v1 = {
  R_div(Y_div),
  pi_D(Y_div,Y_e) in [0,1],
  PARENT_EVENT_ID(div,cohort,worldline),
  Pi_J(dp,dmarks|Y_div,Y_e),
  C_x + regular u_cell/frame/tetrad + transport convention,
  K_s[dispersion,collision,source-off,response,two-point moments],
  K_C[first-passage,completion,response,two-point moments],
  K_Rtest[initial covariance + full common-provenance R_test closure]
}.
```

Musí spĺňať najmenej:

```text
dR_D = dR_div pi_D Pi_J,
integral Pi_J(dp,dmarks|Y)=1 pri pi_D>0,
pi_D=0 => dR_D=0 a conditional Pi_J sa nevyhodnocuje,
všetky labelové reprezentácie tej istej fyzickej udalosti mapujú na jeden
kanonický PARENT_EVENT_ID; odlišné fyzické parent eventy majú odlišné ID,
každé ID sa započíta raz a dcérska kohorta dostane nové ID,
0 <= E_J <= E_available(C_x),
0 <= beta_s <= 1,
p_J = p_s + p_M,
p_C = p_M                 v tomto exact F03 targete,
empty e reservoir => R_D<E_J> -> 0,
completion tail causal a energy-finite/integrable,
K_s, K_C a K_Rtest generujú Q_A, delta Q_A, delta F_A,
pressure/shear/entropy, response, classical two-point noise,
initial covariance, domain a recovery/null limity z rovnakej provenance,
žiadny argument t, ln(a), H0, realizovaný k, S8 ani legacy target.
```

Toto je rámec množiny možných funkcií. Nie je to jedna zvolená funkcia ani
nový fakt o Planckovej bunke.

## 7. Prečo sa neskúša druhý ansatz

Skúsiť teraz `pi_D=1`, collisionless steam a ľubovoľnú completion width by
vyrobilo matematický model, ale jeho neprázdnosť by pochádzala z troch
vložených fyzikálnych hypotéz. To by obišlo presne ten blocker, ktorý mal P4
zmerať.

Predregistrovaný hard stop zakazuje:

- druhý MF1 ansatz;
- prechod na MF2/MF3/MF4;
- Python alebo solver;
- fit na S8/H0;
- rodinný STOP z jedného nevytvoreného svedka.

Ďalší postup musí najprv prejsť progress-goal review. Až potom možno rozhodnúť,
či najmenší successor je analytické odvodenie niektorej časti `K_v1`, alebo
explicitne označená autorova candidate hypothesis; nie odpoveď na
nepozorovateľný mikroskopický fakt.

## 8. Stav a súborový rozpočet

```text
DOCUMENT250 = PASS_B6B2_3_P0_P3_COMPATIBILITY_MATRIX
DOCUMENT251 = REVIEW_P4_V1_DEPENDENCY_FREEZE_BLOCKED_BEFORE_WITNESS
F_D0410_PHYSICAL_NONEMPTINESS = NOT_ESTABLISHED
F_D0410_UNIVERSAL_EMPTINESS = NOT_ESTABLISHED
MF1_MF2_MF3_MF4 = OPEN_UNCHANGED
D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
D04_D11 = PHYSICAL_EXECUTABLE_CONTENT_BLOCKED_UNCHANGED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
P5_4_G8_G9 = NOT_RUN_UNCHANGED
RUN_AUTHORIZED = false
PYTHON_PROCESSES = 0
LIVE_SCIENTIFIC_ARTIFACTS = 1
LIVE_CENTRAL_REGISTERS_UPDATED = 1
LIVE_TOTAL_FILES = 2
AUDIT_PACKAGE_COPIES = 0
```

## 9. Predregistrované auditné otázky

1. Bol `B-MF1 + F01∩F03` vybraný presne podľa zmrazeného lexikografického
   pravidla bez S8/H0 targetu?
2. Je `F01∩F03` kompatibilný prienik a nie skrytá nová rodina?
3. Určuje A7/B6-C0 naozaj iba opportunity/topology a formálnu
   `p_J=Delta P_e(C_x)` identitu, nie `R_div`, thinning alebo evaluovateľný
   event-energy law?
4. Je D03 prvý exact blocker, takže explicitný ansatz a M0–M14 nesmeli byť
   doplnené?
5. Sú D05, D07, D09 a D11 klasifikované bez povýšenia neznámeho na nemožné?
6. Nevylučuje výsledok MF1, fiber ani inú rodinu a nemení skóre, hĺbku alebo
   run authorization?
