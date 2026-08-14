# B6b-2.1 — autor-input balík D04 + D08 + D10

**Task:** `A2K4-B6B2-1-AUTHOR-INPUT-DRAFT-20260723-72`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> V1-D03 -> B6b-2.1`  
**Autor teórie a budúcich fyzikálnych odpovedí:** Martin Jambor  
**Tvorca otázok a formalizácie:** Codex, hlavný orchestrátor  
**Stav:** `PASS_QUESTION_BUNDLE_FOR_AUTHOR / AWAITING_AUTHOR_INPUT / NO_RUN / NO_PYTHON`  
**Účel:** získať najmenší spoločný fyzikálny vstup pre `D04`, `D08` a
`D10` bez predstierania, že tým vznikne spustiteľný kandidát.

## 1. Čo už otázky nesmú meniť

Nasledujúce body sú zdedené a v tomto formulári sa znovu nevyberajú:

1. skorá topológia je `e -> s + M`, po nej lokálne dokončenie `M -> C`;
2. `C` nie je tretia prompt vetva a neskorý A1 kanál `F -> C` je oddelený;
3. jedna kohorta sa ráta najviac raz a po source-off nevznikajú nové parent
   udalosti; skôr narodené `M` kohorty smú kauzálne dobehnúť;
4. na každom parent aj completion vertexe sa musí presne zachovať
   štvorhybnosť, nie iba FLRW priemer;
5. background, perturbácie, pressure/shear a noise musia pochádzať z toho
   istého lokálneho operátora;
6. `S8`, `H0`, legacy steam alebo dnešný pomer `M/C` nesmú určiť event rate,
   energiu udalosti, branch ratio ani completion rate.

Odpoveď `NEVIEM / TREBA ODVODIŤ` je platná. Znamená presný blocker; nedáva
Codexu právo doplniť chýbajúci zákon.

## 2. D04 — product energy-momentum ledger

### D04-1 — úplný zoznam prompt produktov

Je na parent vertexe úplný produktový zoznam iba

```text
e -> s + M,
```

alebo musí existovať ešte ďalší explicitný produkt, ktorý odnáša energiu,
hybnosť alebo kvantové číslo?

```text
D04-1 = ONLY_s_PLUS_M
      | s_PLUS_M_PLUS_EXPLICIT_PRODUCT:<názov a dôvod>
      | NEVIEM_TREBA_ODVODIT
```

Skrytý „ostatný“ sink nie je prípustný: ak existuje, musí dostať vlastné
`T_A^(mu nu)` a riadok v conservation ledgeri.

Pre každý event mark musí platiť signed vertex identita

```text
-p_J^mu + p_s^mu + p_M^mu + sum_X p_X^mu = 0,
```

kde každý ďalší produkt `X` z `D04-1` má vlastné `T_X^(mu nu)`. Nejde iba
o identitu priemerovaných FLRW sourceov.

### D04-2 — čo určuje rozdelenie medzi paru a M

Má byť steam fraction `beta_s`:

```text
D04-2 = DETERMINISTIC_LOCAL_STATE_FUNCTION:<od akých lokálnych stavov>
      | EVENT_MARK_DISTRIBUTION:<čo je mark a čo určuje distribúciu>
      | DERIVED_FROM_ONE_MICROSCOPIC_VERTEX
      | NEVIEM_TREBA_ODVODIT
```

V tejto odpovedi sa nepýta numerická hodnota ani funkčný fit. Potrebujeme
iba rozhodnúť, či je rozdelenie deterministické, distribuované alebo musí
byť odvodené z jedného vertexu. Vždy musí platiť `0 <= beta_s <= 1` a

```text
S_D^nu = S_s^nu + S_M,birth^nu
```

prípadne plus každý explicitne priznaný produkt z `D04-1`.

### D04-3 — fyzikálny význam bezprostredného M

Čo je `M` bezprostredne po parent udalosti na úrovni potrebnej pre ledger?

```text
D04-3 = MASSIVE_LOCAL_EXCITATION_OR_SM_PRECURSOR
      | RELATIVISTIC_PRODUCT_THAT_LATER_BECOMES_COLD
      | MIXED_MARKED_DISTRIBUTION
      | INY_POPIS:<text>
      | NEVIEM_TREBA_ODVODIT
```

Toto ešte neurčuje presnú state equation; tá ostáva v `D09/D11`. Odpoveď má
iba povedať, aký typ energie a hybnosti musí D08 ledger prenášať.

### D04-4 — princíp dostupnej energie a kauzálneho regiónu

Ktorá veta má určovať `E_available(C_x)` pre jednu udalosť?

```text
D04-4 = ENERGY_INSIDE_ONE_CELL_AT_FIRST_PASSAGE
      | ENERGY_IN_DERIVED_LOCAL_CAUSAL_COLLECTION_REGION
      | ACTION_DERIVED_LOCAL_VERTEX_SUPPORT_WITH_DERIVED_ENERGY_CAP
      | INY_PRINCIP:<text>
      | NEVIEM_TREBA_ODVODIT
```

Nežiada sa veľkosť regiónu. Vyžaduje sa iba princíp, z ktorého sa neskôr dá
dokázať `E_J <= E_available(C_x)` vrátane boundary fluxu.

## 3. D08 — birth frame, recoil a spoločný collision kernel

### D08-1 — pravidelný lokálny birth frame

V ktorom fyzickom frame sa má definovať produktový vertex aj v bodoch, kde
scalar-rest frame môže byť nedefinovaný?

```text
D08-1 = TOTAL_STRESS_ENERGY_LANDAU_FRAME
      | CELL_WORLDLINE_FRAME:<ako je odvodený>
      | ACTION_DERIVED_VERTEX_FRAME
      | INY_PRAVIDELNY_FRAME:<text>
      | NEVIEM_TREBA_ODVODIT
```

Voľba nesmie použiť globálny kozmický čas ani realizovaný Fourierov mód.
Ku každej možnosti treba uviesť doménu existencie a jednoznačnosti. Ak frame
na event supporte zlyhá, odpoveď musí určiť iný odvodený lokálny frame alebo
explicitnú `REVIEW/STOP` hranicu. Landau frame je prípustný iba tam, kde má
`T_tot^(mu nu)` jednoznačný future-directed timelike eigenvector.

### D08-2 — angular/recoil štruktúra jednej udalosti

Ktorý opis je fyzikálne zamýšľaný?

```text
D08-2 = INDIVIDUAL_EVENTS_HAVE_RECOIL_BUT_ENSEMBLE_IS_LOCALLY_ISOTROPIC
      | EACH_VERTEX_IS_EXACTLY_ISOTROPIC_IN_BIRTH_FRAME
      | ANISOTROPY_DERIVED_FROM_LOCAL_CELL_STATE
      | INY:<text>
      | NEVIEM_TREBA_ODVODIT
```

Pri každej možnosti musí platiť signed identita

```text
-p_J^mu + p_s^mu + p_M^mu + sum_X p_X^mu = 0.
```

FLRW izotropia ani nulový ensemble recoil samy nie sú event-level dôkazom.

### D08-3 — pôvod jedného operátora

Akú úroveň fyziky autor povoľuje ako prvý kandidátsky passport?

```text
D08-3 = ACTION_DERIVED_COUPLING_AND_MATRIX_ELEMENT
      | LOCAL_KINETIC_OR_COLLISION_OPERATOR_WITH_EXPLICIT_PROVENANCE
      | CAUSAL_MARKED_EVENT_OPERATOR:
        <MARKOV_LIMIT_DERIVED | MEMORY_OR_COHORT_STATE_RETAINED>
      | MULTIPLE_VERSIONED_FAMILIES_WITH_NO_PRIOR_PREFERENCE
      | INY_ODVODENY_OPERATOR:<text>
      | NEVIEM_TREBA_ODVODIT
```

Action derivation, Markov property ani memorylessness nie sú default ani
preferovaný výsledok. Každá voľba musí uviesť svoj recovery/null limit a
nesmie zaviesť nové fundamentálne pole v rozpore s teóriou.

### D08-4 — fyzikálny charakter completion `M -> C`

Je completion najlepšie chápaný ako:

```text
D08-4 = LOCAL_DECAY_OF_M
      | COLLISION_OR_RELAXATION_OF_M_WITH_CELL_STATE
      | FIRST_PASSAGE_OF_INTERNAL_M_STATE
      | INY:<text>
      | NEVIEM_TREBA_ODVODIT
```

Odpoveď zatiaľ nežiada `Gamma_C`. Určí iba, aký objekt musí neskôr odvodiť
completion rate, cohort tail a momentum transfer.

### D08-5 — completion product ledger

Odnáša completion vertex `M -> C` ešte ďalší explicitný produkt?

```text
D08-5 = MOMENTUM_PRESERVING_STATE_CHANGE:p_M^mu=p_C^mu
      | C_PLUS_EXPLICIT_PRODUCTS:
        p_M^mu=p_C^mu+sum_X p_X^mu;<zoznam X a dôvod>
      | NEVIEM_TREBA_ODVODIT
```

Tento bod neurčuje equation of state `D09/D11`. Určuje iba úplný signed
four-momentum a product inventory completion vertexu.

## 4. D10 — štatistický stav, event noise a módové korelácie

### D10-1 — je náhodnosť fundamentálna alebo emergentná

```text
D10-1 = FUNDAMENTAL_STOCHASTIC_EVENTS
      | DETERMINISTIC_CELL_DYNAMICS_WITH_ENSEMBLE_UNCERTAINTY
      | MIXED_QUANTUM_OR_CELLULAR_MARK_PROCESS
      | NEVIEM_TREBA_ODVODIT
```

Táto odpoveď rozhoduje, či `P_AB(k)` je fundamentálny noise kernel alebo
ensemble compression deterministického mikrostavu.

### D10-2 — korelácie udalostí medzi bunkami/kohortami

Každá dimenzia sa vyplní samostatne; možnosti sa navzájom nevylučujú:

```text
D10-2 = SELECT_EACH_DIMENSION_OR_NEVIEM

CELL_SPATIAL =
    CONDITIONALLY_INDEPENDENT_GIVEN_COMPLETE_LOCAL_STATE
  | CORRELATED_WITHIN_DERIVED_CAUSAL_SUPPORT
  | INY:<text>

COHORT_LINEAGE =
    INDEPENDENT
  | PARENT_COMPLETION_CORRELATED
  | INTERGENERATION_OR_EXCLUSION_CORRELATED
  | INY:<text>

CROSS_CHANNEL =
    ZERO_ONLY_IF_DERIVED
  | NONZERO_AUTO_AND_CROSS_CHANNEL_CORRELATIONS
  | INY:<text>

COUNT_STATISTICS =
    POISSON_ONLY_IF_DERIVED
  | SUB_POISSON_OR_EXCLUSION
  | SUPER_POISSON_OR_COMMON_STATE_CLUSTERING
  | INY:<text>

TEMPORAL_MEMORY =
    MARKOV_WHITE_LIMIT_ONLY_IF_DERIVED
  | COLORED_OR_MEMORY_BEARING
  | INY:<text>
```

Pre každú neuzavretú dimenziu možno odpovedať `NEVIEM_TREBA_ODVODIT`.

`POISSON` sa nepoužije ako default. Ak má vzniknúť, musí vyplynúť z odpovede
a z operátora; first-passage alebo zdieľaná energia môžu prirodzene vytvoriť
sub-Poisson či cross-channel korelácie.

### D10-3 — vzťah k počiatočným kozmologickým módom

```text
D10-3 = FULLY_DERIVED_FROM_SAME_LOCAL_ADIABATIC_STATE
      | INDEPENDENT_ISOCURVATURE_COMPONENT_ALLOWED
      | CORRELATED_ADIABATIC_PLUS_ISOCURVATURE_FROM_ONE_OPERATOR
      | NO_FREE_INITIAL_MODE_MUST_BE_DERIVED
      | NEVIEM_TREBA_ODVODIT
```

Táto odpoveď nesmie byť zvolená podľa toho, ktorá možnosť zníži S8.

### D10-4 — povinné algebraické vlastnosti covariance

Prosíme výslovne potvrdiť alebo odmietnuť:

```text
D10-4a: covariance/noise kernel je PSD pre každý dovolený k
         (pri non-Markov procese ako full two-time/spectral kernel)
D10-4b: energy conservation je exact ľavý aj pravý null smer
D10-4c: každý momentum component má exact ľavý aj pravý null smer
D10-4d: auto aj všetky cross-sector/cross-channel bloky sú explicitné

AUTHOR_RESPONSE = CONFIRM_ALL
                | REJECT_OR_MODIFY:<presne ktorý bod a prečo>
                | NEVIEM_TREBA_ODVODIT
```

## 5. Krížové consistency otázky

```text
X1: Vznikajú parent/completion rate a marks, D04 product-energy assignment,
    D08 parent aj completion recoil a D10 auto/cross noise z jedného
    versioned physical passportu — prípadne z explicitne spojených parent
    a completion operatorov cez ten istý cohort ledger — tak, aby background,
    delta Q_A, momentum transfer, pressure, shear, entropy a noise mali
    spoločnú provenienciu?

    YES
  | NO_CONTRACT_CONFLICT_REQUIRES_REDEFINITION:<prečo>
  | NEVIEM_TREBA_ODVODIT

X2: Je event-level conservation presná v každej realizácii, alebo iba v
    ensemble? EACH_EVENT / ENSEMBLE_ONLY:<fyzikálny dôvod> / NEVIEM
```

`ENSEMBLE_ONLY` pri `X2` by bol materiálny konflikt s aktuálnym vertex
conservation guardom a vyžadoval by samostatné autorovo zdôvodnenie; agent
ho nesmie ticho prijať.

## 6. Najkratší formát odpovede autora

Autor môže odpovedať prirodzeným textom alebo skopírovať:

```text
D04-1 =
D04-2 =
D04-3 =
D04-4 =
D08-1 =
D08-2 =
D08-3 =
D08-4 =
D08-5 =
D10-1 =
D10-2 CELL_SPATIAL =
D10-2 COHORT_LINEAGE =
D10-2 CROSS_CHANNEL =
D10-2 COUNT_STATISTICS =
D10-2 TEMPORAL_MEMORY =
D10-3 =
D10-4 =
X1 =
X2 =

AUTOR_POTVRDZUJE_NOVY_FYZIKALNY_VSTUP = YES / NO
POTVRDZUJEM_ZE_ZVOLENE_ODPOVEDE_SU_MOJE_FYZIKALNE_POSTULATY_A_NIE_VOLBA_PODLA_S8_H0 = YES / NO
```

Bez oboch `YES` sa odpoveď interpretuje iba ako diskusia, nie ako
autoritatívne otvorenie D04/D08/D10. Každá nezodpovedaná alebo `NEVIEM`
položka zostáva blockerom; potvrdenie samo nepovoľuje run ani neuzatvára
`D03/D05–D09/D11`.

## 7. Čo odpovede odomknú a čo nie

Úplná konzistentná odpoveď môže otvoriť prvý spoločný **neexekvovateľný**
kernel passport pre `P1/P2/P5` a spresniť `P0/P3/P4/P6/P8`. Sama však:

- neuzavrie D03 rate/state map;
- neuzavrie D05 ordering, D06 constants/initial data ani D09 thermal state;
- neuzavrie D07/D11 source-off a late residue;
- neurčí numerické parametre, basis ani search bounds;
- nepovoľuje Python, P5.4, G8, G9 ani S8 forward výpočet.

Po autorovej odpovedi nasleduje nezávislý fyzikálny audit consistency a až
potom autoritatívne rozhodnutie, ktoré bloky sa skutočne otvorili.
