# B6b-2.2 — odvodenie priestoru možností D04 + D08 + D10

**Task:** `A2K4-B6B2-2-POSSIBILITY-SPACE-DRAFT-20260723-77`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.2`  
**Autor teórie a epistemického smeru:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `PASS_B6B2_2_POSSIBILITY_SPACE_PROTOCOL / NO_RUN / NO_PYTHON`  
**Nahrádza ako aktívny krok:** dokument 248 ako požiadavku na autorove
odpovede o priamo nepozorovateľnej mikrofyzike. Dokument 248 zostáva
historický a jeho otázky sa nemusia zodpovedať.

## 1. Autorova korekcia smeru

Pri procesoch na Planckovej škále dnes neexistuje prístroj, ktorý by priamo
videl vnútro bunky alebo potvrdil konkrétny event operator. Neznámy fakt sa
preto nesmie nahradiť autorovou voľbou ani agentovým odhadom.

Správny cieľ je:

1. odvodiť, čo **musí** platiť z teórie, matematiky a známych zákonov;
2. zmapovať všetky rozlíšiteľné triedy toho, čo **môže** platiť;
3. každej triede určiť rozsahy a nutné dôsledky;
4. vyradiť iba triedy s certifikovaným rozporom;
5. zvyšné možnosti niesť súbežne až po test, ktorý ich dokáže rozlíšiť.

To, že mikrofyziku nevieme priamo pozorovať, nie je dôkaz, že ľubovoľná
mikrofyzika je dovolená. Obmedzujú ju conservation, kovariancia, kauzalita,
pozitivita, termodynamika, recovery limity a neskôr makroskopické dáta.

## 2. Epistemické triedy

Zložený riadok nesmie dostať jednu blanket triedu. Najprv sa rozdelí na
atómové tvrdenia. Každé atómové tvrdenie dostane oddelene:

```text
SOURCE_CLASS = FIXED_AUTHOR_AXIOM | E0 | E1 | E2 | E3 | PROCESS_CONTRACT,
DERIVATION_STATUS = FIXED | OPEN_DERIVATION | DERIVED | REQUIRES_NEW_AUTHOR_AXIOM.
```

Tým sa napríklad neznámy product inventory (`OPEN_DERIVATION`) neprehlási za
E0 iba preto, že conservation nad už úplným inventory je exact.

| Trieda | Význam | Smie urobiť |
|---|---|---|
| `FIXED_AUTHOR_AXIOM` | filozofická alebo ontologická súčasť bunkovej teórie výslovne určená autorom | definuje skúmaný priestor, nie empirický dôkaz |
| `E0_EXACT` | matematická identita, invariant, symetria alebo zákon v presnej doméne | tvrdo vylúči protirečiacu podtriedu |
| `E1_DIRECT_MEASUREMENT` | priamo meraná observabla s chybami a mapovaním | vylúči iba úplne zmapovaný observačný scope |
| `E2_REFERENCE_MODEL` | štandardný model alebo recovery comparator | označí mismatch, nie sám STOP |
| `E3_PROVISIONAL` | modelovo závislá inferencia, hypotéza alebo návrhové vodidlo | vedie hľadanie, nevylučuje samo |
| `OPEN_DERIVATION` | fyzikálny detail nie je priamo známy, ale môže byť obmedzený alebo odvodený | zostáva otvorenou množinou, nie otázkou na odhad |
| `REQUIRES_NEW_AUTHOR_AXIOM` | dve možnosti sa líšia iba novým ontologickým tvrdením, ktoré súčasná teória neurčuje | jediný prípad, keď sa vec vracia autorovi ako nová axióma |

`OPEN_DERIVATION` nie je blocker mapovania. Je blockerom až pre konkrétny
spustiteľný kernel, kým sa nezúži na svedka alebo auditovaný rozsah.

## 3. Dnes zmrazené vstupy

```text
A0: skorá topológia e -> s + M, potom lokálne M -> C;
A1: C nie je tretia prompt vetva;
A2: neskorý A1 kanál F -> C zostáva oddelený;
A3: first-passage — jedna kohorta sa započíta najviac raz;
A4: po parent source-off nevznikajú nové parent udalosti, existujúci M tail
    smie kauzálne dobehnúť;
A5: žiadne nové fundamentálne inflatónové pole; efektívna lokálna súradnica
    musí mať bunkový pôvod;
A6: S8, H0 ani želaná dnešná kompozícia neurčujú mikrofyziku.
```

`A0–A6` definujú skúmanú teóriu. Nie sú meraním Planckovej bunky.

## 4. Matematický objekt — kompatibilný fiber product

Nech

```text
B = spoločný base passport:
    sektory + lokálny state + event/cohort identity + causal domain
    + unresolved väzby D03/D05/D07/D09/D11;

X_04 -> B = product-energy-momentum ledgers,
X_08 -> B = local causal recoil/collision/event operátory,
X_10 -> B = statistical/noise completions.

X_compat = X_04 x_B X_08 x_B X_10
         subset X_04 x X_08 x X_10.
```

Fiber product povoľuje iba trojice s rovnakými sektormi, stavom, event
labels, causal supportom a cohort ledgerom. Každý mantinel vytvorí
podmnožinu `C_i subset X_compat`. Aktuálne prípustný priestor
je

```text
F_D0410 = X_compat intersection (intersection_i C_i).
```

Všetky mantinely musia platiť pre ten istý spojený parent/completion
passport. Nemožno použiť jeden operator na background, druhý na recoil a
tretí na noise iba preto, že každý osobitne vyhovuje inému testu.

## 5. Osi priestoru možností

Nasledujúce osi sú klasifikačné súradnice, nie autorove otázky ani vybrané
hypotézy. Sú

```text
EXHAUSTIVE_ONLY_AT_DECLARED_EFFECTIVE_MOMENT_RESOLUTION,
```

ktorá je dnes `background + linear perturbations + classical two-point
noise`. Nejde o úplný zoznam všetkých funkcií alebo Planckovských ontológií.
Každý blok obsahuje residual
`OTHER_CAUSAL_CONSERVATIVE / UNRESOLVED_REPRESENTATIVE`, aby nová platná
trieda nebola vylúčená iba preto, že nie je v dnešnom slovníku.

### 5.1 D04 — product a energy ledger

| Os | Dovolené triedy pred testom | Tvrdý mantinel |
|---|---|---|
| prompt inventár | iba `s+M`; alebo `s+M+X` s explicitným `T_X^(mu nu)` | žiadny skrytý sink |
| allocation provenance | phenomenological local law; kinetic/action-derived law; unresolved representative | žiadny fit podľa S8/H0 |
| allocation stochasticity | deterministic; conditional distribution; joint marked distribution | `0<=beta_s<=1` |
| joint energy-angular marks | factorized only if derived; correlated energy/recoil marks; unresolved | spoločný event ledger |
| multiplicity/charges | fixed; distributed; coherent transition; unresolved | každý nosič/charge explicitný |
| dispersion/on-shell class M | massive; relativistic; mixed/marked; unresolved D09/D11 completion | kladná energia v deklarovanej doméne |
| causal support | jedna bunka; odvodený causal region; action-local support | vždy `E_J<=E_available(C_x)` vrátane boundary fluxu |
| boundary/environment carrier | closed vertex; explicit boundary flux/environment sector; unresolved | žiadny skrytý sink |

Pre každý parent event mark musí platiť signed identita

```text
-p_J^mu + p_s^mu + p_M^mu + sum_X p_X^mu = 0.
```

### 5.2 D08 — frame, recoil a operator

| Os | Dovolené triedy pred testom | Tvrdý mantinel |
|---|---|---|
| regular frame | Type-I Landau frame; odvodená cell worldline; action/vertex frame; iný lokálny frame | existencia a jednoznačnosť na event supporte alebo fail-closed hranica |
| angular/recoil | event recoil s ensemble isotropiou; event-level isotropia; lokálne stavová anizotropia | signed four-momentum na každej realizácii |
| operator provenance | action/matrix element; kinetic/collision; effective marked operator; unresolved | explicitná formula lineage |
| temporal structure | Markov iba ak odvodený; finite/infinite-memory cohort operator; unresolved | retarded support |
| spatial support | point-local; finite causal neighborhood; unresolved | žiadny superluminal support |
| system carrier | closed sectors; explicit environment/boundary carrier; unresolved | úplný conservation ledger |
| reaction arity/coherence | one-to-many; many-to-many; coherent transition; unresolved | explicitné event labels a multiplicity |
| completion typ | local decay; collision/relaxation; internal first-passage | rovnaký cohort ledger, bez double-count |
| completion produkty | `p_M=p_C`; alebo `p_M=p_C+sum_X p_X` | každý `X` explicitný; conservation na completion vertexe |
| completion network | single stage; multi-stage cohort network; unresolved | bez skrytého double-count |

### 5.3 D10 — statistical/noise completion

Tento blok je explicitne obmedzený na linear/two-point resolution.
Štatistická ontológia môže byť fundamentálne stochastic, deterministická s
ensemble uncertainty alebo zmiešaná. Na aktuálnej rozlišovacej úrovni môžu
byť tieto mikroskopické výklady ekvivalentné; rozhoduje odvodený kernel.

Korelácie sa mapujú po nezávislých dimenziách, ktoré môžu koexistovať:

```text
CELL_SPATIAL: conditional independence | finite causal correlation support;
COHORT_LINEAGE: multi-label parent-completion | intergeneration | exclusion;
CROSS_CHANNEL: derived zero | nonzero auto/cross blocks;
COUNT_STATISTICS: Poisson | sub-Poisson | super-Poisson/clustered;
TEMPORAL_MEMORY: white Markov limit | colored/memory-bearing;
INITIAL_MODES: adiabatic-derived | isocurvature | correlated mixture.
JOINT_COUNT_ENERGY_MARKS: factorized only if derived | correlated | unresolved;
HIGHER_CUMULANTS: negligible only if bounded | retained | unresolved;
NOISE_TYPE: classical | quantum/operator-valued | unresolved.
```

Žiadna z prvých možností nie je default. Každý dovolený klasický
covariance/noise kernel musí byť PSD, mať exact ľavé aj pravé
energy/momentum conservation null smery a obsahovať všetky relevantné
cross-sector bloky. Kvantový alebo nonstationary objekt musí najprv zmraziť
ordering a full two-time/spectral kernel; až potom dostane príslušnú
positivity alebo uncertainty bránu.

## 6. Atómové mantinely M0–M14

| ID | Atómové tvrdenie | Source class / stav | Rozhodovacia sila |
|---|---|---|---|
| `M0a` | skutočný product inventory | `OPEN_DERIVATION` | nevylučuje, kým scope nie je úplný |
| `M0b` | conservation closure nad deklarovaným úplným inventory | podmienené `E0` | vylúči skrytý sink iba v deklarovanom scope |
| `M1` | signed four-momentum na každom úplne definovanom vertexe vrátane boundary carrierov | podmienené `E0` | vylúči nekonzervatívny vertex |
| `M2a` | `0<=beta_s<=1` | definičné `E0` | vylúči over-allocation |
| `M2b` | nezáporná fyzická marked measure/rate | podmienené `E0`; ontológia miery musí byť deklarovaná | nevzťahuje sa automaticky na amplitúdy/intermediate weights |
| `M3a` | causal region, boundary flux a `E_available` | `OPEN_DERIVATION` | zatiaľ nevylučuje |
| `M3b` | `E_J<=E_available(C_x)` po uzavretí M3a | podmienené `E0` | vylúči prekročenie dostupného budgetu |
| `M4a` | existencia/jednoznačnosť zvoleného frame na supporte | `OPEN_DERIVATION` | vyžaduje dôkaz domény |
| `M4b` | nepoužiť frame mimo dokázanej domény | podmienené `E0` regularity guard | vylúči singular extrapolation |
| `M5a` | retarded causal support v deklarovanej relativistickej doméne | `E0` | vylúči acausal/superluminal support |
| `M5b` | žiadny voľný kozmický čas alebo realizovaný `k` v mikrofyzike | `FIXED_AUTHOR_AXIOM + PROCESS_CONTRACT` | definuje skúmaný scope |
| `M6a` | first-passage | `FIXED_AUTHOR_AXIOM A3` | definuje event identity |
| `M6b` | zákaz double-count v zmrazenom cohort ledgeri | `E0` bookkeeping dôsledok M6a | vylúči opakované započítanie |
| `M7a` | po source-off nevznikajú nové parent births | `FIXED_AUTHOR_AXIOM A4` | definuje recovery scope |
| `M7b` | completion tail: causal, energy-finite/integrable; časová podpora nemusí byť konečná | `OPEN_DERIVATION` | nevylučuje iba pre nekonečné trvanie |
| `M8` | spoločný versioned passport pre background/perturbations/noise | `PROCESS_CONTRACT` | blokuje post-hoc nezávislé funkcie; nie fyzikálny theorem |
| `M9a` | definícia classical/quantum, ordering a two-time/spectral noise objektu | `OPEN_DERIVATION` | predchádza positivity testu |
| `M9b` | classical PSD a conservation null smery po uzavretí M9a | podmienené `E0` | vylúči neplatnú klasickú covariance |
| `M9c` | quantum positivity/uncertainty podmienka po zmrazení ordering | `OPEN_DERIVATION`, neskôr podmienené `E0` | nevkladá klasickú PSD naslepo |
| `M10` | pressure/shear/entropy momentová mapa | `OPEN_DERIVATION` | ručne doplnená closure nesmie prejsť |
| `M11a` | zero-coupling limit | definičné `E0` po definícii coupling |
| `M11b` | exhausted-reservoir source limit | `OPEN_DERIVATION` podľa source zákona |
| `M11c` | oddelený late A1 recovery | `FIXED_MODEL_CONTRACT / E2 comparator` |
| `M12` | zákaz target fitu a versioned mutation lineage | `PROCESS_CONTRACT` | nie epistemické E0 |
| `M13` | passivity alebo nezáporná entropy production v deklarovanej termodynamickej doméne | `OPEN_DERIVATION`, neskôr podmienené `E0` | vylúči termodynamický rozpor v scope |
| `M14` | ghost/gradient/characteristic stability v deklarovanej dynamike | `OPEN_DERIVATION`, neskôr podmienené `E0` | vylúči nestabilný svedok, nie celú nezmapovanú triedu |

P1 smie vylúčiť triedu iba konkrétnym atómom `E0` alebo úplne zmapovaným
`E1`, s jeho doménou a provenance. Zlyhanie celého zloženého M-bloku nie je
certifikát.

## 7. Postup odvodenia bez mikroskopického prístroja

### Krok P0 — schema matrix na deklarovanej rozlišovacej úrovni

Vytvorí sa kompatibilná fiber schema, nie karteziánsky zoznam všetkých
funkcií. Pokryje ortogonálne atribúty oddielu 5 a residual
`OTHER_CAUSAL_CONSERVATIVE / UNRESOLVED_REPRESENTATIVE`. Nepridávajú sa
numerické pravdepodobnosti.

### Krok P1 — analytické E0 prechecky

Na každú triedu sa aplikujú atómy `M0–M14`. Vylúčenie musí obsahovať rovnicu,
doménu a presný rozpor. Výstupom môže byť napríklad:

```text
IMPOSSIBLE_E0_CERTIFIED:
  - hidden energy sink violates M0/M1;
  - superluminal support violates M5a;
  - negative eigenvalue of a fully defined classical covariance violates M9b.
```

### Krok P2 — intervalové a funkčné mantinely

Pre preživšie triedy sa odvodia rozsahy, nie centrálne odhady:

```text
beta_s(Y,marks) in [0,1],
E_J in [0,E_available(C_x)],
Gamma_C >= 0,
correlation support subset causal support,
classical Cov(k) positive semidefinite with conservation null space
  only after M9a is fixed.
```

Ak zákony nestačia na užší interval, zachová sa celý interval. Šírka nie je
chyba; je to poctivý stav poznania.

### Krok P3 — quotient ekvivalentných mikrofyzík

Najprv sa zmrazí test-resolution tuple

```text
R_test = (Q_A, delta Q_A, delta F_A, pressure/shear/entropy closure,
          two-point noise kernel, initial-mode covariance,
          domain, recovery/null limits).
```

Mikrofyziky sa quotientujú iba vzhľadom na rovnosť tohto tuple v rovnakej
doméne. Latentné subclass labels zostávajú zachované pre budúce nonlinear,
higher-cumulant alebo nové observačné testy.

### Krok P4 — explicitní svedkovia

Pre každú preživšiu efektívnu triedu sa hľadá aspoň jeden explicitný lokálny
svedok. Svedok dokazuje iba neprázdnosť svojho scope, nie pravdivosť ani
jedinečnosť.

### Krok P5 — makroskopická spätná väzba

Až úplný svedok sa propaguje cez background a perturbácie. Pozorovania môžu
zúžiť priestor, ale calibration dáta sa nesmú spätne použiť na zmenu tvaru
toho istého kandidáta. Neznáma Planckovská mikrofyzika sa testuje nepriamo
cez jej nevyhnutné makroskopické dôsledky.

## 8. Povolené stavy každej triedy

| Stav | Význam |
|---|---|
| `NOT_EXCLUDED_BY_CURRENT_CONSTRAINTS` | zatiaľ ju nevylúčil žiadny platný certifikát; existencia nie je dokázaná |
| `UNRESOLVED_NEEDS_DERIVATION` | nemožno ju zatiaľ potvrdiť ani vylúčiť; chýba odvodenie, nie autorov odhad |
| `EQUIVALENT_AT_CURRENT_RESOLUTION` | od inej triedy ju dnešné rovnice/pozorovania nerozlišujú |
| `NONEMPTY_WITNESS` | existuje explicitný objekt pre deklarovaný scope |
| `IMPOSSIBLE_E0_CERTIFIED` | presný E0 rozpor v uvedenej doméne |
| `PRECHECK_EXCLUDED_SCOPE` | procesný dôsledok úplného E0/E1 vylúčenia |
| `REQUIRES_NEW_AUTHOR_AXIOM` | iba ontologický rozdiel mimo dnešnej teórie; nesmie sa použiť na zaplnenie neznámeho faktu |

Nenájdený svedok, zlyhaný ansatz alebo nemožnosť priameho merania nikdy
samé nedávajú `IMPOSSIBLE_E0_CERTIFIED`.

## 9. Povinný výstup nasledujúceho kroku

Nasledujúci no-Python krok vytvorí maticu:

| Common base/fiber | D04 attributes | D08 attributes | D10 linear/two-point attributes | Residual bucket | Atomic constraint + class + domain | Quotient key | Stav/certifikát |
|---|---|---|---|---|---|---|---|

`DONE_WHEN`:

1. každá os z oddielu 5 je pokrytá na deklarovanej efektívnej/momentovej
   rozlišovacej úrovni a residual bucket zostáva otvorený;
2. každé vylúčenie má E0/E1 certifikát a presný scope;
3. nevylúčené možnosti majú intervaly alebo `UNRESOLVED_NEEDS_DERIVATION`;
4. ekvivalentné mikrofyziky sú zlúčené podľa dostupnej rozlišovacej úrovne;
5. nevznikol author-choice, S8 fit, Python ani tvrdenie o pravdivosti.

## 10. Stav a nonclaims

```text
DOCUMENT248 = SUPERSEDED_AS_ACTIVE_AUTHOR_QUESTIONNAIRE_BY_AUTHOR_DIRECTION
D04_D08_D10 = MAPPING_OPEN
D05_D07_D09_D11 = INDEPENDENTLY_BLOCKED_UNCHANGED
F_D0410 = NOT_YET_MAPPED
MF1 = OPEN
MF2 = OPEN
MF3 = OPEN
MF4 = OPEN
D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
D04_D11 = BLOCKED_UNCHANGED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
NO_PYTHON
```

Tento protokol nevidí do Planckovej bunky a netvrdí, že fakty o nej už
poznáme. Mení nepoznateľný dotaz na falsifikovateľný priestor možností:
presne ukáže, čo je nemožné, čo zatiaľ nie je vylúčené a čo ostáva
nerozlíšené.

## 11. Auditné otázky

1. Je rozdiel medzi autorovou axiómou a neznámym mikrofyzikálnym faktom
   dostatočne ostrý?
2. Pokrývajú osi D04/D08/D10 scoped priestor dokumentov 246–248 na
   deklarovanej linear/two-point úrovni vrátane residual bucketu a bez skrytej
   preferencie?
3. Sú atómy `M0–M14` správne rozdelené medzi podmienené E0, axómy,
   procesné kontrakty a otvorené derivácie?
4. Môže byť trieda vyradená iba s reprodukovateľným certifikátom rozporu?
5. Je P0–P5 správne poradie pred akýmkoľvek numerickým S8 testom?
