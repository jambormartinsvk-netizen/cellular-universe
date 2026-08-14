# B6b-2 — perturbation, search-space a S8 calibration/holdout passport

**Task:** `A2K4-B6B2-PASSPORT-DRAFT-20260723-57`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> S-M/Q18/Q22 -> SM_v1 -> V1-D03 -> B6b-2`  
**Autor teórie a fyzikálneho smeru:** Martin Jambor  
**Tvorca pracovného analytického artefaktu:** Codex, hlavný orchestrátor  
**Stav:** `PASS_B6B2_PASSPORT_SCHEMA / REVIEW_B6B2_PHYSICAL_CONTENT_BLOCKED_D03_D11 / NO_RUN / NO_PYTHON`  
**Dátový cut:** 2026-07-23

## 1. Cieľ a presný scope

B6b-1 uzavrel iba analytické obálky `MF1–MF4`. B6b-2 má pred akýmkoľvek
výpočtom oddeliť tri rôzne objekty:

1. **perturbation passport** — čo musí z jedného lokálneho kernelu vzniknúť;
2. **search-space contract** — čo sa počas kalibrácie smie meniť a čo nie;
3. **data passport** — ktoré dáta sú calibration, comparator alebo holdout.

B6b-2 nesmie nahradiť otvorené fyzikálne vstupy `V1-D04` a `V1-D08–D10`
agentovým odhadom. Preto môže uzavrieť schému a observačný comparator, ale
nie plný fyzikálny perturbation kernel ani spustiteľný search space.

## 2. Dôkazová trieda komprimovaného S8

Používame definíciu

```text
S8 = sigma8 sqrt(Omega_m/0.3).
```

Publikované jednorozmerné `S8` intervaly nie sú priamym meraním jednej
model-independent veličiny. Sú posterior compression odvodená po voľbe
kozmologického modelu, nuisance parametrov, scale cuts a likelihoodu. V tomto
passporte sa preto evidujú na dvoch neaditívnych osiach:

```text
INTERVAL_EVIDENCE_CLASS = E3_MODEL_DEPENDENT_INFERENCE,
REFERENCE_MAPPING_CLASS = E2_FLAT_LCDM_COMPARATOR.
```

nie `E1_DIRECT_MEASUREMENT`. Smú viesť hľadanie a označiť napätie, ale samy
nemôžu vydať `OBSERVATIONAL_STOP_SCOPE` pre novú interagujúcu dynamiku.

## 3. Zmrazený calibration comparator v1

### 3.1 Primárne zdroje a presné publikované 68 % intervaly

| ID | Primárny zdroj | Model/scope | Publikované `S8` | 68 % interval použitý v passporte | Rola |
|---|---|---|---:|---:|---|
| `CAL-DESY6` | DES Collaboration, *Dark Energy Survey Year 6 Results: Cosmological Constraints from Galaxy Clustering and Weak Lensing*, arXiv:2601.14559v2 | Y6 `3x2pt`, flat LambdaCDM | `0.789 +0.012/-0.012` | `[0.777,0.801]` | calibration |
| `CAL-KIDS` | Wright et al., *KiDS-Legacy: Cosmological constraints from cosmic shear with the complete Kilo-Degree Survey*, arXiv:2503.19441v2 | cosmic shear, flat LambdaCDM | `0.815 +0.016/-0.021` | `[0.794,0.831]` | calibration |
| `CMP-HSC` | Choppin de Janvry et al., *Cosmic Shear constraints from HSC Year 3 with clustering calibration ... from DESI*, arXiv:2511.18134v3 | HSC Y3 reanalysis with DESI redshift calibration | `0.805 +/-0.018` | `[0.787,0.823]` | comparator only |

Primary links frozen by this document:

- `https://arxiv.org/abs/2601.14559v2`;
- `https://arxiv.org/abs/2503.19441v2`;
- `https://arxiv.org/abs/2511.18134v3`.

HSC nevstupuje do selection bandu, pretože jeho redshift calibration používa
DESI informáciu, ktorú rezervujeme pre rastový cross-check. Zostáva
auditným comparatorom. DES Y6 a KiDS sa štatisticky nekombinujú. Ich
konzervatívny vonkajší 68 % search envelope je iba množinová únia:

```text
I_S8_CAL_v1 = [min(0.777,0.794), max(0.801,0.831)]
             = [0.777,0.831].
```

`I_S8_CAL_v1` nie je spoločný posterior, confidence interval ani tvrdenie,
že všetky body v ňom majú rovnakú váhu. Je to široký model-dependent
calibration/search band zvolený tak, aby jedna survey pipeline sama neurčila
tvar neznámej funkcie.

### 3.2 Predregistrovaná interpretácia

Pre budúci úplný modelový výstup platí:

```text
S8_model in [0.777,0.831]
  -> E3_INTERVAL_COMPATIBLE_UNDER_E2_FLAT_LCDM_MAPPING;

S8_model outside [0.777,0.831]
  -> REFERENCE_MISMATCH_ONLY / REVIEW;
```

Ani jedna vetva sama nie je observačný PASS/STOP. Na STOP je potrebný
model -> pôvodný data vector -> likelihood reťazec so systematikami a
nuisance parametrami.

Historická v3.17 hodnota `S8=0.86–0.87` nevstupuje do konštrukcie ani do
calibration bandu. Je to zmrazená legacy prediction na budúce prepočítanie.
Jej poloha mimo `I_S8_CAL_v1` dnes nemení verdict, pretože aktuálny SM_v1
perturbation a growth systém ešte neexistuje.

## 4. Calibration, comparator a holdout split

```text
CALIBRATION:
  iba CAL-DESY6 + CAL-KIDS komprimované S8 intervaly a ich outer envelope;

NONSELECTION_COMPARATOR:
  CMP-HSC; nesmie meniť rodinu, basis, parameter bounds ani ranking;

RESERVED_GROWTH_CROSSCHECK:
  DESI DR1 Full-Shape clustering data products — power-spectrum multipoles,
  window matrices a covariance z official release;

FINAL_INDEPENDENT_HOLDOUT:
  NOT_YET_CERTIFIED.
```

Oficiálny rezervovaný DESI zdroj je
`https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/`.
Rezervácia používa pôvodný data vector/covariance, nie komprimované
`sigma8` z fitu s CMB alebo lensingom.

DESI cross-check zatiaľ nemá štítok nezávislého holdoutu, pretože:

- DES/KiDS a DESI môžu zdieľať sky volume a cosmic variance;
- HSC comparator explicitne použil DESI redshift calibration;
- bias, AP a growth inference sú model dependent;
- cross-covariance s calibration dátami ešte nebola auditovaná.

Preto platí

```text
DESI_DR1_FS_ROLE = RESERVED_QUASI_HOLDOUT_PENDING_CROSS_COVARIANCE,
HOLDOUT_BLINDNESS = NOT_CLAIMED,
NO_LEAKAGE_RULE = DESI data vector ani jeho fit sa nesmie použiť na výber
                  rodiny, funkčnej triedy, basisu alebo parameter bounds.
```

Ak cross-covariance audit nezaručí dostatočné oddelenie, DESI zostane iba
cross-checkom a konečný holdout sa zvolí neskôr z iného observačného sektora.

## 5. Minimálny kovariantný perturbation passport

Pre každý sektor `A in {e,s,M,C}` a zvolený lokálny frame `u^mu` definujeme
bez coordinate-factor konvencie

```text
signature = (-,+,+,+),
u_mu u^mu = -1,
nabla_mu T_A^(mu nu) = Q_A^nu,
Q_A       = -u_mu Q_A^mu,
F_A^mu    = h^mu_nu Q_A^nu,
h^mu_nu   = delta^mu_nu + u^mu u_nu,
u_mu F_A^mu = 0,
Q_A^mu = Q_A u^mu + F_A^mu.
```

Background má `bar(F_A^mu)=0` iba z FLRW izotropie. Lineárny passport musí
odvodiť `delta Q_A` aj priestorový momentum-transfer response `delta F_A^mu`
z rovnakého event/kernel passportu. Exact conservation dáva

```text
sum_A bar(Q_A) = 0,
sum_A delta Q_A = 0,
sum_A delta F_A^mu = 0.
```

Background znamienka sú

```text
bar(Q_e) = -Q_D <= 0,
bar(Q_s) = +Q_s >= 0,
bar(Q_M) = Q_M,birth - Q_M_to_C  # bez pevného znamienka,
bar(Q_C) = +Q_M_to_C >= 0.
```

`delta Q_A`, momentum transfer, pressure perturbation, shear a jednotlivé
cross-correlation entries nemajú všeobecne pevné znamienko. Vložiť ich
znamienko podľa požadovaného smeru zmeny `S8` je zakázaný fit.

### 5.1 Povinné riadky každého kandidáta

| Blok | Povinný obsah | Tvrdý guard | Aktuálny blocker |
|---|---|---|---|
| `P0` | frame, gauge a gauge-map | bez skrytého gauge fixing | neúplný state/frame D03, D05, D08 |
| `P1` | `bar Q_A`, `delta Q_A` | sumy presne nula | rate D03 + event energy/ledger D04 |
| `P2` | `delta F_A^mu` | ortogonalita a sumy nula | recoil/matrix element D08 |
| `P3` | `delta p_A`, entropy response | odvodené z rovnakého kernelu | collision/thermal state D08–D09 |
| `P4` | anisotropic stress/shear | FLRW null, perturbation odvodená | D08–D09 |
| `P5` | event covariance a `P_AB(k)` | PSD + obidva conservation null smery | statistical state D10 |
| `P6` | source-off perturbation limit | parent moments zaniknú; kauzálny cohort tail je oddelený | D07/D11 |
| `P7` | `k->0`, high-`k`, characteristics | regularita, bez ghost/gradient runaway | po uzavretí P0–P6 |
| `P8` | initial modes/correlations | žiadne skryté Poisson/adiabatic assumption | D10 |

Gauge formula sa nezmrazí, kým nie je zvolený birth frame a úplný state.
Implementácia však musí neskôr dodať general-synchronous reprezentáciu aj
gauge-invariant cross-check; gauge artefakt nesmie rozhodnúť rodinu.

Pre `P6` parent source-off odstráni všetky parent energy-momentum-weighted
`M1–Mnoise` momenty a ich perturbácie. `Q_M_to_C` a jeho perturbácie smú
zostať iba ako kauzálne zdedený konečný cohort tail bez nových parent births;
neskorý kanál `A1 F->C` zostáva vedený v samostatnom ledgeri.

### 5.2 Rodinné linear-response identity

Na rovnakej symbolickej hĺbke musí kandidát obsahovať:

```text
MF1:
  delta(dR_D) = delta[p_D(Y) dR_div Pi_D],
  teda division-rate, thinning aj mark response z jedného lokálneho stavu;

MF2:
  delta R_D = integral dY [delta f_act Gamma_int
                           + f_act delta Gamma_int]
              + povinná measure/Jacobian response;

MF3:
  delta(dR_D) obsahuje endpoint responses aj
  delta w = (partial w/partial z) delta z;
  delta z musí byť odvodená z lokálneho stavu, nie z epochy alebo S8;
  tento delta-w zápis platí iba na spoločnej opportunity measure;
  pri rozdielnych mierach je potrebná aditívna marked-measure response
  vrátane perturbácií miery/Jacobiánu, nie automatická konvexná zmes;

MF4:
  delta Q_A^mu = sum_r delta Q_A,r^mu;
  P_AB obsahuje auto aj cross-channel covariance a spoločné null smery.
```

Tieto identity sú schéma, nie vyplnený fyzikálny kernel.

## 6. Search-space contract

Každý budúci kandidát dostane immutable record:

```text
CANDIDATE_ID
FAMILY_ID = MF1|MF2|MF3|MF4
LOCAL_STATE_VECTOR_AND_DOMAIN
EVENT_RATE_CLASS
EVENT_ENERGY_MARK_CLASS_AND_CAUSAL_CAP
STEAM_FRACTION_CLASS
COMPLETION_CLASS
FRAME_AND_GAUGE_MAP
PRESSURE_SHEAR_NOISE_RESPONSE
FREE_FUNCTION_COUNT
FREE_PARAMETER_COUNT_AND_BOUNDS
INITIAL_CONDITIONS_AND_BOUNDS
BASIS_TYPE_DEGREE_KNOTS_OR_CHANNEL_COUNT
PHYSICAL_PROVENANCE
CALIBRATION_DATA_ALLOWED
HOLDOUT_DATA_FORBIDDEN_DURING_SELECTION
MODEL_TO_OBSERVABLE_PIPELINE_AND_VERSION
CALIBRATION_ACCEPTANCE_RULE
NUISANCE_MODEL_PRIORS_AND_SCALE_CUTS
SEARCH_ALGORITHM_DOMAIN_COVERAGE_AND_STOPPING_RULE
NUMERICAL_TOLERANCES_AND_RANDOM_SEEDS
PARAMETER_POINT_OR_SURVIVOR_REGION_ID
DATA_ARTIFACT_PATHS_VERSIONS_AND_SHA256
MUTATION_PARENT_ID_AND_PRIOR_DATA_EXPOSURE
```

Po prvom modelovom výstupe sa v tom istom `CANDIDATE_ID` nesmie meniť:

- rodina alebo local-state vector;
- počet voľných funkcií/parametrov;
- basis, stupeň, uzly, počet switchov alebo kanálov;
- bounds, priory, source-off a stability gates;
- calibration/holdout rola datasetov.

Kalibrácia smie meniť iba hodnoty vopred deklarovaných parametrov v ich
zmrazených bounds a vybrať všetky kandidáty, ktoré prejdú. Nový tvar po
nevyhovujúcom výsledku je nový versioned kandidát a starý výsledok zostáva
platný vo svojom scope. Nový kandidát nesmie spätne označiť rovnaké
calibration dáta za nezávislé potvrdenie.

Ak search nemá certifikované pokrytie predregistrovanej domény, výsledok je

```text
SEARCH_COVERAGE_NOT_CERTIFIED -> REVIEW_SEARCH_INCOMPLETE,
```

nikdy `EMPTY_CERTIFIED_SCOPE` ani `OBSERVATIONAL_STOP_SCOPE`.

### 6.1 Ranking pri viacerých preživších funkciách

Ak prežije viac kandidátov, platí:

1. tvrdý predpoklad: prejdú všetky `E0` conservation, stability, recovery a
   same-kernel background/perturbation provenance guards;
2. dataset smie ovplyvniť ranking iba ak
   `FINAL_INDEPENDENT_HOLDOUT=CERTIFIED` a jeho likelihood/ranking štatistika
   bola zmrazená pred otvorením;
3. comparator alebo `RESERVED_QUASI_HOLDOUT_PENDING_CROSS_COVARIANCE` je iba
   diagnostický a nesmie meniť rodinu, basis, bounds, survivor set ani ranking;
4. predregistrované complexity a stability-margin tie-breakers sa použijú iba
   medzi kandidátmi nerozlíšenými certifikovaným holdoutom.

„Najväčší potenciál“ teda nebude subjektívny výber podľa pekného grafu.

## 7. Čo možno a nemožno zmraziť dnes

### Zmrazené týmto draftom po prípadnom prijatí auditu

- `INTERVAL_EVIDENCE_CLASS=E3_MODEL_DEPENDENT_INFERENCE` a oddelený
  `REFERENCE_MAPPING_CLASS=E2_FLAT_LCDM_COMPARATOR`;
- `I_S8_CAL_v1=[0.777,0.831]` ako outer search envelope, nie likelihood;
- calibration/comparator/reserved-cross-check roly datasetov;
- minimálna perturbation passport schéma `P0–P8`;
- immutable candidate record a zákaz post-result shape mutation.

### Fyzikálne nezmraziteľné bez autora

- event energy/recoil a úplný product ledger (`D04`);
- konkrétny local state/rate-energy map v nedokončenom `D03`;
- paralelné/sekvenčné poradie produktov a prípadný medzistav (`D05`);
- nové konštanty a počiatočné podmienky (`D06`);
- matrix element alebo collision operator (`D08`);
- thermalization/decoupling a stavové rovnice produktov (`D09`);
- statistical/noise prescription a initial correlations (`D10`);
- konečný source-off residue (`D07/D11`);
- exact basis, počet parametrov a bounds každého fyzikálneho kandidáta.

Preto je aktuálny návrh stavu

```text
B6B2_SCHEMA = PASS_B6B2_PASSPORT_SCHEMA
S8_CALIBRATION_ENVELOPE = FROZEN_E3_INTERVAL_E2_REFERENCE_[0.777,0.831]
PERTURBATION_PHYSICS = INCOMPLETE_BLOCKED_D03_D11
SEARCH_SPACE_RECORD_SCHEMA = PASS_IMMUTABLE_SCHEMA_ONLY
SEARCH_SPACE_CONTENT = NOT_FREEZABLE_YET
DESI_DR1_FS = RESERVED_QUASI_HOLDOUT_PENDING_CROSS_COVARIANCE
FINAL_INDEPENDENT_HOLDOUT = NOT_YET_CERTIFIED
MF1 = OPEN
MF2 = OPEN
MF3 = OPEN
MF4 = OPEN
D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
D04_D11 = BLOCKED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
NO_PYTHON
```

## 8. Gate ordering a A3

B6b-2 nemení poradie kanonických brán. Žiadny S8 ani DESI forward test sa
nespustí pred úplným fyzikálnym kandidátom, P5.4 evolúciou a potrebnou G8
hierarchiou/interface closure. Komprimovaný `S8` screen môže byť neskôr
lacný comparator, ale plný observačný verdict patrí až G9.

Najbližší vedecký krok po audite B6b-2 nie je Python. Je ním ohraničený prvý
autor-input subbalík `D04 + D08 + D10` pre energiu/recoil, collision momenty
a noise. Tento subbalík je zámerne **neexekvovateľný** a sám neuzavrie
`P0–P8`: background rate zostáva v `D03`, poradie/medzistav v `D05`, nové
konštanty a initial conditions v `D06`, thermal state v `D09` a source-off
ledger v `D07/D11`. Až ich dependency closure môže vytvoriť spustiteľný
perturbation kandidát.

## 9. Predregistrované auditné otázky

1. Sú `S8` intervals a ich model dependence zapísané bez falošného E1?
2. Je outer envelope matematicky správny a jasne odlíšený od likelihoodu?
3. Je HSC správne vyradené zo selection kvôli DESI-linked calibration?
4. Je DESI iba rezervovaný quasi-holdout bez predstieranej nezávislosti?
5. Sú conservation, gauge/frame, moment a noise riadky úplné na schema úrovni?
6. Nevložil dokument do otvorených D04/D08–D10 nový fyzikálny zákon?
7. Je search-space mutation guard kompatibilný s autorovým inverse-search cieľom?
8. Zachováva dokument P5.4/G8/G9 ordering a `NO_PYTHON`?

## 10. Nonclaims a handoff

Tento dokument nevyberá funkciu, rodinu, event energy, clock, collision
kernel, S8 prediction ani holdout verdict. Neotvára D04–D11, P5.4, G8 alebo
G9 a nemení skóre. Odporúčaný handoff je nezávislý read-only fyzikálny audit
dokumentu 247 a jeho troch primárnych observačných referencií.
