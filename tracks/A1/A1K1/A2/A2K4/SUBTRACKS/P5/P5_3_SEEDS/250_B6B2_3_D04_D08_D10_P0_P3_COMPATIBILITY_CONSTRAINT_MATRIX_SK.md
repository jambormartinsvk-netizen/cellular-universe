# B6b-2.3 — P0–P3 compatibility/constraint matica D04 + D08 + D10

**Task:** `A2K4-B6B2-3-P0-P3-COMPATIBILITY-MATRIX-20260724-85`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.3`  
**Autor teórie a epistemického smeru:** Martin Jambor  
**Tvorca symbolickej matice:** Codex, hlavný orchestrátor  
**Stav:** `PASS_B6B2_3_P0_P3_COMPATIBILITY_MATRIX / NO_RUN / NO_PYTHON`  
**Nadradený contract:** dokument 249,
`PASS_B6B2_2_POSSIBILITY_SPACE_PROTOCOL`

## 1. Cieľ, rozlíšenie a hranica tvrdenia

Úlohou nie je uhádnuť vnútro Planckovej bunky. Matica má na rovnakej
efektívnej úrovni zapísať:

1. ktoré D04, D08 a D10 atribúty možno spojiť do jedného passportu;
2. ktoré rozsahy sú vynútené už dnes;
3. ktoré podrozsahy sú presne nemožné;
4. ktoré možnosti ostávajú neodvodené alebo nerozlíšiteľné;
5. čo musí nasledujúci explicitný svedok skutočne skonštruovať.

Deklarované rozlíšenie je presne

```text
background + linear perturbations + classical two-point noise,
```

pričom quantum/operator-valued a higher-cumulant objekty sa iba evidujú ako
otvorené residual triedy. Matica nie je úplnou ontológiou všetkých možných
Planckovských procesov.

Používame dve odlišné označenia:

```text
DERIVATION_P0..P3 = kroky protokolu dokumentu 249;
PASSPORT_P0..P8   = perturbation riadky dokumentu 247.
```

Tento artefakt vykonáva `DERIVATION_P0..P3`. Nevytvára `P4` explicitného
svedka a neuzatvára fyzikálny obsah žiadneho `PASSPORT_P0..P8`.

## 2. Zmrazený spoločný základ B

Každý zostavený kandidát musí niesť rovnaký base passport

```text
B = (FAMILY_ID,
     LOCAL_STATE_AND_DOMAIN,
     SECTOR_INVENTORY,
     PARENT_EVENT_ID,
     COHORT_AND_COMPLETION_ID,
     RETARDED_RESPONSE_SUPPORT,
     EVENT_INNOVATION_OR_COMMON_CAUSE_DOMAIN,
     INITIAL_STATE_CORRELATION_DOMAIN,
     COMMUTATOR_SUPPORT_IF_QUANTUM,
     FRAME_DOMAIN,
     RESERVOIR_AND_BOUNDARY_LEDGER,
     SOURCE_OFF_AND_RECOVERY_LABELS,
     D03_D05_D07_D09_D11_DEPENDENCIES).
```

Kompatibilný priestor je fiber product

```text
X_compat = X_04 x_B X_08 x_B X_10,
F_D0410  = X_compat intersection (intersection_i C_i).
```

Riadky s odlišným `B` sa nesmú kombinovať. Ich nekompatibilita nie je
fyzikálny no-go; znamená iba, že netvoria jeden kandidát.

### 2.1 Base rodiny na rovnakej hĺbke

| Base ID | Mechanism-family základ | Povinná identita | Otvorená derivácia | Stav |
|---|---|---|---|---|
| `B-MF1` | division-locked | `0<=dR_D<=dR_div`; event/cohort labels sú podmierou division opportunities | `R_div`, thinning law, marky a energy cap | `UNRESOLVED_NEEDS_DERIVATION` |
| `B-MF2` | internal-clock/first-passage | `R_D=integral f_act Gamma_int` alebo auditovaná first-passage flux; jedna kohorta najviac raz | `n_act`, clock domain, event identity, energy marks | `UNRESOLVED_NEEDS_DERIVATION` |
| `B-MF3S` | state-switched na spoločnej opportunity measure | `dR_D=w dR_1+(1-w)dR_2`, `0<=w<=1`; `w=w(Y_local)` | lokálny diskriminátor, prah a transition ledger | `UNRESOLVED_NEEDS_DERIVATION` |
| `B-MF3A` | state-switched s rozdielnymi mierami | aditívna marked-measure response, nie konvexný priemer | mapovanie mier/Jacobiánu a distributional transition terms | `UNRESOLVED_NEEDS_DERIVATION` |
| `B-MF4` | paralelné konzervatívne kanály | `dR_D=sum_r dR_D,r`; disjunktné event labels; spoločný reservoir cap | počet kanálov, allocation a cross-channel covariance | `UNRESOLVED_NEEDS_DERIVATION` |
| `B-RES` | iný kauzálny konzervatívny reprezentant | musí reprodukovať A0–A6 a M0–M14 v deklarovanej doméne | celá reprezentácia | `UNRESOLVED_NEEDS_DERIVATION` |

`B-MF3S` a `B-MF3A` nie sú nové rodiny; sú dve matematicky odlišné
realizácie MF3, ktoré nemožno zlúčiť bez spoločnej miery.

## 3. DERIVATION_P0 — typované osi bez kartézskej enumerácie

Každý kandidát vyberá alebo odvodzuje jeden či viac atribútov z každej
povinnej osi. Voľby na ortogonálnych osiach môžu koexistovať. Symbol
`RES` vždy znamená
`OTHER_CAUSAL_CONSERVATIVE / UNRESOLVED_REPRESENTATIVE`.

### 3.1 D04 atribúty

| ID osi | Obsah typovaného vlákna nad B | Povinný guard | Pred-P4 stav |
|---|---|---|---|
| `04-I` | prompt inventory: `s+M`; alebo `s+M+X_explicit`; alebo `RES` | každý `X` má `T_X^(mu nu)` a signed vertex riadok | `UNRESOLVED_NEEDS_DERIVATION` |
| `04-P` | allocation provenance: local phenomenology; action/kinetic derivation; `RES` | nesmie byť určená S8/H0 | `UNRESOLVED_NEEDS_DERIVATION` |
| `04-S` | allocation stochasticity: deterministic; conditional distribution; joint marked distribution; `RES` | `0<=beta_s<=1` na supporte | `NOT_EXCLUDED_BY_CURRENT_CONSTRAINTS` iba ako schema |
| `04-J` | joint energy-angular marks: correlated; factorized iba po odvodení; `RES` | spoločný event mark a ledger | `UNRESOLVED_NEEDS_DERIVATION` |
| `04-M` | multiplicity/charges: fixed; distributed; coherent transition; `RES` | všetky nosiče a charges explicitné | `UNRESOLVED_NEEDS_DERIVATION` |
| `04-D` | dispersion M: massive; relativistic; mixed/marked; `RES` | kladná energia v deklarovanej doméne; D09/D11 ostáva otvorené | `UNRESOLVED_NEEDS_DERIVATION` |
| `04-C` | causal collection: one-cell; odvodený finite causal region; action-local support; `RES` | complete boundary flux a `E_J<=E_available(C_x)` | `UNRESOLVED_NEEDS_DERIVATION` |
| `04-B` | carrier: closed vertex; explicit boundary/environment sector; `RES` | žiadny skrytý sink | `UNRESOLVED_NEEDS_DERIVATION` |

### 3.2 D08 atribúty

| ID osi | Obsah typovaného vlákna nad B | Povinný guard | Pred-P4 stav |
|---|---|---|---|
| `08-F` | Type-I Landau; cell-worldline; action/vertex frame; iný local frame; `RES` | existencia a jednoznačnosť na event supporte | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-R` | event recoil + ensemble isotropia; exact event isotropia; state-derived anisotropy; `RES` | signed four-momentum v každej realizácii | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-O` | action/matrix element; kinetic/collision; effective marked operator; `RES` | versioned formula lineage | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-T` | odvodený Markov limit; finite/infinite-memory cohort operator; `RES` | retarded support | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-L` | point-local; finite causal neighborhood; `RES` | support v povolenom causal cone | `NOT_EXCLUDED_BY_CURRENT_CONSTRAINTS` iba ako schema |
| `08-E` | closed sectors; explicit environment/boundary carrier; `RES` | inventory zhodný s `04-I/04-B` | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-A` | one-to-many; many-to-many; coherent transition; `RES` | multiplicita zhodná s `04-M` | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-K` | local decay; collision/relaxation; internal first-passage; `RES` | rovnaký cohort ledger, bez double-count | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-CP` | `p_M=p_C`; alebo `p_M=p_C+sum_X p_X`; `RES` | completion inventory explicitný | `UNRESOLVED_NEEDS_DERIVATION` |
| `08-N` | single-stage; multi-stage cohort network; `RES` | event identities a first-passage removal na každom stupni | `UNRESOLVED_NEEDS_DERIVATION` |

### 3.3 D10 atribúty na linear/two-point úrovni

| ID osi | Obsah typovaného vlákna nad B | Povinný guard | Pred-P4 stav |
|---|---|---|---|
| `10-S` | fundamental stochastic; deterministic ensemble; mixed; `RES` | ontológia nie je odvodená z tvaru covariance | `EQUIVALENT_AT_CURRENT_RESOLUTION` ak dáva rovnaký `R_test` |
| `10-X` | conditional spatial independence; common-cause correlation z explicitnej spoločnej kauzálnej minulosti; explicitná initial-state correlation domain; `RES` | retarded response a prípadný commutator sú causal; covariance sa nesmie zameniť za signal propagation | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-C` | independent cohorts; parent-completion; intergeneration/exclusion; multi-label; `RES` | cohort labels zhodné s `08-K/08-N` | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-H` | derived-zero alebo nonzero cross-channel blocks; `RES` | MF4 a zdieľaný reservoir nesmú defaultovať nulu | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-N` | Poisson; sub-Poisson; super-Poisson/clustered; `RES` | Poisson iba po odvodení procesu | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-T` | white Markov limit; colored/two-time memory; `RES` | zhodné temporal labels s `08-T` | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-I` | adiabatic-derived; isocurvature; correlated mixture; `RES` | bez voľby podľa S8 | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-J` | factorized alebo correlated count-energy marks; `RES` | faktorizácia iba ak odvodená | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-K` | higher cumulants bounded-negligible; retained; `RES` | mimo aktuálneho rozlíšenia sa latentný label zachová | `UNRESOLVED_NEEDS_DERIVATION` |
| `10-Q` | classical; quantum/operator-valued; `RES` | quantum ordering a full two-time object pred positivity testom | `UNRESOLVED_NEEDS_DERIVATION` |

Tým sú pokryté všetky osi dokumentu 249 na deklarovanej úrovni. Matica
netvrdí, že každá ich kombinácia existuje alebo je kompatibilná.

## 4. Kompatibilita vlákien nad spoločným B

Nasledujúce join pravidlá sa aplikujú pred fyzikálnymi mantinelmi. Zlyhanie
joinu dostáva `FIBER_INCOMPATIBLE_NOT_PHYSICS_NO_GO`, nie STOP rodiny.

| Join | Musí byť totožné alebo odvodenou mapou prepojené | Typický neplatný splice |
|---|---|---|
| `J0` | sector inventory v D04, D08 a D10 | D04 má extra `X`, D08/D10 ho nevedú |
| `J1` | parent event ID a mark space | background používa iné udalosti než recoil |
| `J2` | cohort/completion identity | D10 koreluje kohortu, ktorú D08 nevie identifikovať |
| `J3` | local state, parameter point a doména | rate a noise vyhodnotené v odlišných stavoch |
| `J4` | response support, event/common-cause domain, initial-correlation domain, quantum commutator support a boundary convention ako oddelené objekty | energia je z one-cell, recoil z väčšieho neúčtovaného regiónu alebo covariance sa vydáva za response support |
| `J5` | frame/tetrad alebo explicitná kovariantná mapa | energy marks a momentum covariance v neprepojených frames |
| `J6` | multiplicita, charges a carrier labels | coherent D04 prechod spojený s classical one-to-two D08 bez mapy |
| `J7` | completion network a temporal memory labels | instant completion s parent-completion memory bez latentného stavu |
| `J8` | source-off/recovery a oddelený late-A1 ledger | D10 parent noise prežíva po zániku parent energy moments |
| `J9` | classical/quantum object a positivity notion | classical PSD aplikovaná na nezmrazený quantum ordered kernel |

### 4.1 Atómové profily s triedou a doménou

Skratka `cE0` znamená podmienené `E0_EXACT` až po splnení uvedenej
definičnej podmienky. Každý archetyp nižšie menuje exact atómy cez tieto
profily; nejde o zložený blanket E0.

| Profil | Exact atómy, source class a doména |
|---|---|
| `AP-INV` | `M0a OPEN_DERIVATION` pre skutočný inventory; `M0b cE0` iba nad deklarovaným úplným inventory; `M1 cE0` iba na úplne definovanom vertexe vrátane boundary carrierov |
| `AP-ALLOC` | `M2a definičné E0` pre energy-fraction `beta_s`; `M2b cE0` pre nezápornú physical marked measure po deklarovaní ontológie miery |
| `AP-BUDGET` | `M3a OPEN_DERIVATION` pre causal region/boundary flux/`E_available`; `M3b cE0` iba po uzavretí M3a v tom istom frame a boundary ledgeri |
| `AP-FRAME` | `M4a OPEN_DERIVATION` pre existenciu/jednoznačnosť frame na event supporte; `M4b cE0` zákaz použitia mimo už dokázanej frame domény |
| `AP-CAUSAL` | `M5a E0` pre retarded response a, ak je relevantný, commutator v deklarovanej relativistickej doméne; `M5b FIXED_AUTHOR_AXIOM+PROCESS_CONTRACT` pre zákaz voľného času/realizovaného `k` |
| `AP-COHORT` | `M6a FIXED_AUTHOR_AXIOM A3`; `M6b E0` bookkeeping v zmrazenom cohort ledgeri; `M7a FIXED_AUTHOR_AXIOM A4`; `M7b OPEN_DERIVATION` pre causal energy-finite/integrable completion tail |
| `AP-PROV` | `M8 PROCESS_CONTRACT` pre jeden versioned background/perturbation/noise passport |
| `AP-NOISE-C` | `M9a OPEN_DERIVATION` pre typ, argumenty a reprezentáciu classical objectu; `M9b cE0` pre správne typovanú classical positivity a obojstranné conservation null smery po M9a |
| `AP-NOISE-Q` | `M9a OPEN_DERIVATION` pre ordering/two-time object; exact ľavé aj pravé source-conservation null smery cez oba sector indices/kernel arguments po úplnom inventory; `M9c OPEN_DERIVATION`, neskôr `cE0`, pre ordering-specific quantum positivity/uncertainty contract |
| `AP-CLOSURE` | `M10 OPEN_DERIVATION` pre pressure/shear/entropy momentovú mapu v rovnakom passporte |
| `AP-RECOVERY` | `M11a definičné E0` po definícii coupling; `M11b OPEN_DERIVATION` podľa source zákona; `M11c FIXED_MODEL_CONTRACT/E2` pre oddelený late-A1 comparator |
| `AP-PROCESS` | `M12 PROCESS_CONTRACT` pre zákaz target fitu a mutation lineage |
| `AP-THERMO` | `M13 OPEN_DERIVATION`, neskôr `cE0`, v deklarovanej thermodynamic doméne |
| `AP-STAB` | `M14 OPEN_DERIVATION`, neskôr `cE0`, v deklarovanej dynamickej/characteristic doméne |

Každý riadok `F01–F09` dedí bez výnimky

```text
AP-BASELINE-ALL =
  AP-INV(M0a,M0b,M1)
  + AP-ALLOC(M2a,M2b)
  + AP-BUDGET(M3a,M3b)
  + AP-FRAME(M4a,M4b)
  + AP-CAUSAL(M5a,M5b)
  + AP-COHORT(M6a,M6b,M7a,M7b)
  + AP-PROV(M8)
  + [AP-NOISE-C(M9a,M9b) alebo AP-NOISE-Q(M9a,M9c),
     prípadne obe explicitne oddelené vetvy]
  + AP-CLOSURE(M10)
  + AP-RECOVERY(M11a,M11b,M11c)
  + AP-PROCESS(M12)
  + AP-THERMO(M13)
  + AP-STAB(M14).
```

Profily uvedené priamo v riadku sú jeho rozlišujúce aktívne bloky, nie
náhrada zvyšku baseline.

### 4.2 Kompatibilné schema archetypy

Archetyp je typovaný zväzok atribútov, nie explicitný fyzikálny svedok.

| Fiber ID | Common base/fiber | D04 attributes | D08 attributes | D10 attributes | Residual | Atómové brány | Quotient key | Stav |
|---|---|---|---|---|---|---|---|---|
| `F01` | ľubovoľné `B-*`; closed parent inventory | `04-I=s+M`, `04-B=closed`, zvyšok typed/open | `08-E=closed`, parent recoil/operator/frame typed/open | classical alebo unresolved statistics so zhodnými labels | áno na všetkých otvorených osiach | dedí `AP-BASELINE-ALL`; discriminators: `AP-INV`, `AP-ALLOC`, `AP-FRAME`, `AP-CAUSAL`, `AP-PROV`, explicitne zvolená `AP-NOISE-C` alebo `AP-NOISE-Q` vetva | `R_test` až po vyplnení | `UNRESOLVED_NEEDS_DERIVATION` |
| `F02` | ľubovoľné `B-*`; explicit carrier | `04-I=s+M+X`, `04-B=explicit` | `08-E` obsahuje ten istý `X` a boundary flux | D10 obsahuje `X` auto/cross bloky | áno | dedí `AP-BASELINE-ALL`; discriminators: `AP-INV`, `AP-BUDGET`, `AP-FRAME`, `AP-PROV`, explicitne zvolená `AP-NOISE-C` alebo `AP-NOISE-Q` vetva | `R_test+latent(X)` | `UNRESOLVED_NEEDS_DERIVATION` |
| `F03` | ľubovoľné `B-*`; momentum-preserving completion | `M` birth typed/open | `08-CP:p_M=p_C`, completion network/cohort explicitný | parent-completion covariance podľa toho istého cohort ID | áno | dedí `AP-BASELINE-ALL`; discriminators: `AP-INV`, `AP-COHORT`, `AP-PROV`, `AP-RECOVERY`, explicitne zvolená `AP-NOISE-C` alebo `AP-NOISE-Q` vetva | `R_test+latent(completion)` | `UNRESOLVED_NEEDS_DERIVATION` |
| `F04` | ľubovoľné `B-*`; radiative/multiproduct completion | completion `X_C` inventory explicitný | `08-CP:p_M=p_C+sum_X p_X`; carrier/frame explicitný | všetky completion-product auto/cross bloky explicitné | áno | dedí `AP-BASELINE-ALL`; discriminators: `AP-INV`, `AP-FRAME`, `AP-COHORT`, `AP-PROV`, explicitne zvolená `AP-NOISE-C` alebo `AP-NOISE-Q` vetva | `R_test+latent(X_C)` | `UNRESOLVED_NEEDS_DERIVATION` |
| `F05` | ľubovoľné `B-*`, vrátane `B-MF1`; memory-bearing completion cohort | joint marked distribution | `08-T=memory`, `08-N=multi-stage` | colored/two-time + lineage covariance | áno | dedí `AP-BASELINE-ALL`; discriminators: `AP-CAUSAL`, `AP-COHORT`, `AP-PROV`, explicitne zvolená `AP-NOISE-C` alebo `AP-NOISE-Q` vetva | `R_test+latent(memory)` | `UNRESOLVED_NEEDS_DERIVATION` |
| `F06` | ľubovoľné `B-*`; odvodený Markov limit | deterministic alebo marked parent | `08-T=Markov` iba ako limit | white kernel iba ak rovnaký limit odvodí | áno | dedí `AP-BASELINE-ALL`; discriminators: `AP-CAUSAL`, `AP-PROV`, `AP-NOISE-C`, `AP-THERMO`, `AP-STAB` | `R_test+latent(Markov)` | `UNRESOLVED_NEEDS_DERIVATION` |
| `F07` | `B-MF4`; najmenej dva kanály | kanálové inventory a allocation `f_r` | disjunktné event IDs, spoločný alebo oddelený reservoir ledger | auto aj cross-channel bloky | áno | dedí `AP-BASELINE-ALL`; discriminators: `AP-INV`, `AP-BUDGET`, `AP-COHORT`, `AP-PROV`, explicitne zvolená `AP-NOISE-C` alebo `AP-NOISE-Q` vetva | `R_test+channel_labels` | `UNRESOLVED_NEEDS_DERIVATION` |
| `F08` | ľubovoľné `B-*`; coherent/quantum residual | coherent multiplicity a charges | action/vertex frame a operator lineage otvorené | operator-valued/two-time ordering otvorený | povinný | dedí `AP-BASELINE-ALL`; discriminators: `AP-INV`, `AP-FRAME`, `AP-CAUSAL`, `AP-NOISE-Q`, `AP-THERMO`, `AP-STAB` | ešte nedefinovaný | `UNRESOLVED_NEEDS_DERIVATION` |
| `F09` | `B-RES` | všetky D04 osi residual | všetky D08 osi residual | všetky D10 osi residual | celý riadok | dedí `AP-BASELINE-ALL`; noise sa vetví explicitne na `AP-NOISE-C` a `AP-NOISE-Q`, nie na neexistujúci composite profil | ešte nedefinovaný | `UNRESOLVED_NEEDS_DERIVATION` |

Žiadny riadok `F01–F09` zatiaľ nemá `NONEMPTY_WITNESS`. Riadky iba ukazujú,
že dnešné pravidlá nevyžadujú jedinú vopred zvolenú mikrofyzickú ontológiu.

## 5. DERIVATION_P1 — atómové precheck certifikáty

### 5.1 Certifikovane vylúčené podrozsahy

Tieto certifikáty sa týkajú presného podrozsahu, nie celej MF rodiny.

| Certifikát | Presný scope | Rozpor | Trieda/doména | Výsledok |
|---|---|---|---|---|
| `EC01` | allocation mark s `beta_s<0` alebo `beta_s>1` | porušuje definičný podiel energie | M2a, `E0_EXACT`, event support | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC02` | úplne deklarovaný parent alebo completion vertex bez boundary carrieru | `-p_in^mu+sum p_out^mu != 0` | M0b+M1, podmienené `E0_EXACT` po úplnom inventory | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC03` | úplne odvodený causal region a flux ledger | `E_J>E_available(C_x)` | M3b, podmienené `E0_EXACT` | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC04` | identifikovaná parent/completion kohorta | tá istá udalosť alebo energia je započítaná viac než raz | M6a fixed axiom + M6b exact bookkeeping | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC05` | retarded response alebo quantum commutator v deklarovanej relativistickej doméne | má support mimo povoleného causal cone; covariance support sám sem nepatrí | `M5a E0_EXACT` pre response/commutator doménu | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC06` | úplne typovaný classical equal-time, Fourier, two-time alebo spectral kernel | poruší príslušnú positivity podmienku `I14a–I14d` alebo obojstranné conservation null smery `I14e` | `M9a+M9b cE0` až po zmrazení reprezentácie a argumentov | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC06q` | úplne definovaný ordered quantum source kernel s úplným sector inventory | contraction s energy alebo momentum conservation vectorom je nenulová na ľavom alebo pravom sector/kernel argumente | exact operator/source conservation z `M1` v complete-inventory doméne; positivity ostáva ordering-specific `M9c` | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC07` | passport po zmrazení tvrdí úplný inventory, ale reprodukovateľný vertex residual dokáže neúčtovaný sink/environment | conservation closure a deklarovaný úplný inventory si odporujú | `M0a OPEN` uzavreté deklaráciou + `M0b/M1 cE0` v complete-inventory/vertex doméne | `IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `EC08a` | existencia alebo jednoznačnosť frame ešte nebola dokázaná | chýba odvodenie, nie certifikát nemožnosti | `M4a OPEN_DERIVATION` na event supporte | `UNRESOLVED_NEEDS_DERIVATION`, bez exclusion |
| `EC08b` | frame je dokázane neexistujúci/nejednoznačný na required supporte alebo sa preukázane použije mimo platnej domény | passportové veličiny nie sú definované v tvrdenej reprezentácii | `M4a` uzavretý dôkazom + `M4b cE0` v presnom frame scope | `PRECHECK_EXCLUDED_SCOPE` tejto frame reprezentácie |
| `EC09` | MF3 different-measure doména použitá s common-measure convex formula | chýba measure/Jacobian response, takže rovnosť mier neplatí | `E0_EXACT` measure identity v presnej common-measure verzus different-measure doméne | `PRECHECK_EXCLUDED_SCOPE` tejto reprezentácie; MF3 ostáva otvorená cez `B-MF3A` |

### 5.2 Čo dnes nemožno certifikovane vylúčiť

- `s+M` oproti `s+M+X`, kým nie je odvodený úplný inventory;
- deterministic, stochastic alebo mixed ontologický výklad, ak majú rovnaký
  efektívny `R_test`;
- point-local oproti finite causal neighborhood;
- Markov limit oproti memory-bearing operatoru;
- Poisson, sub-Poisson alebo clustered counts;
- adiabatic, isocurvature alebo correlated initial covariance;
- MF1, MF2, MF3 ani MF4 ako celok;
- residual `B-RES/F09`.

Aktuálny E1 register neobsahuje priame meranie Planckovského eventu. Preto
tu nevzniká nijaký `E1_DIRECT_MEASUREMENT` precheck certifikát. S8 je E3
model-dependent inference pod E2 comparatorom a do tejto matice nevstupuje.

Procesný zákaz post-result target fitu je `PROCESS_CONTRACT`, nie fyzikálny
E0 no-go. Kandidát porušujúci tento zákaz je neplatný pre test, ale jeho
mikrofyzická trieda tým nie je dokázaná ako nemožná.

## 6. DERIVATION_P2 — intervalové a funkčné mantinely

| ID | Rozsah | Mantinel | Stav horného/dolného okraja |
|---|---|---|---|
| `I01` | event rate/measure | `dR_D>=0`, `R_D>=0`; použitá fyzická mark measure je nezáporná | lower exact; upper otvorený podľa rodiny |
| `I02` | steam allocation | `0<=beta_s(p,x)<=1` | exact definičný interval |
| `I03` | event energy | `0<=E_J<=E_available(C_x)` | upper platí až po odvodení `C_x`, platného local frame a úplného boundary flux ledgera |
| `I04` | source split | `0<=Q_s<=Q_D`, `0<=Q_M,birth<=Q_D`, `Q_s+Q_M,birth=Q_D` v complete `s+M` scope | exact po úplnom inventory; pri `X` sa rozšíri ledger |
| `I05` | moments | `J_n,D>=0`; každý použitý moment musí byť konečný osobitne | nezápornosť exact; konečnosť otvorená |
| `I06` | rate-energy variance a nulový limit | `Q_D^2<=R_D J_2,D` pre `0<R_D<infinity` a konečný `J_2,D`; pri `R_D=0` physical-measure scope dá `Q_D=J_2,D=0` | podmienené exact |
| `I07` | cold-M completion backlog | kumulatívny `a^3 Q_M_to_C` neprekročí initial M + integrated births | exact iba v cold-M scope; pressure/work vyžaduje rozšírenie |
| `I08` | source-off | nové parent energy-weighted moments `M1–Mnoise ->0`; completion tail je causal a energy-finite/integrable | fixed recovery contract; presný law otvorený D07/D11 |
| `I09` | MF1 | `0<=dR_D<=dR_div`; pri odvodenom `E_max`, `J_n<=R_div E_max^n` | upper moment otvorený bez `E_max` |
| `I10` | MF2 | pri `f_act>=0`, `0<=n_act<infinity` a `0<=Gamma_min<=Gamma_int<=Gamma_max<infinity` na tom istom odvodenom supporte platí `n_act Gamma_min<=R_D<=n_act Gamma_max` | oba bounds otvorené bez clock/rate derivácie |
| `I11` | MF3 | `0<=w(Y)<=1` na common measure; pri different measures platí aditívny integral form | exact reprezentácia po deklarovaní mier |
| `I12` | MF4 | `f_r>=0`, `sum_r f_r<=1` pri spoločnom rezervoári; kanálové sources sa sčítajú | exact allocation guard; kanály otvorené |
| `I13a` | retarded response | `supp(G_ret) subseteq` povolený future causal cone | `M5a E0` v deklarovanej relativistickej doméne |
| `I13b` | event innovation/common cause | joint event covariance uvedie local innovation support alebo explicitnú spoločnú kauzálnu minulosť; nesmie sa interpretovať ako retarded signal | provenance otvorená; bez blanket compact-support požiadavky |
| `I13c` | initial-state correlations | domain a covariance sa uvedú explicitne; spacelike/dlhodosahová korelácia sama nie je acausal response | otvorené D10-I, nie E0 exclusion |
| `I13d` | quantum commutator | commutator/microcausal response má povolený causal support; symmetrized/ordered covariance sa testuje osobitne | otvorené M9a/M9c, neskôr scoped E0 |
| `I14a` | real equal-time classical kernel | `C_AB(x,y)=C_BA(y,x)` a `integral f_A C_AB f_B >=0` pre všetky fyzické real test functions | `M9b cE0` po M9a |
| `I14b` | complex Fourier covariance | `C_AB(k)=C_BA(k)^*` a `z^dagger C(k) z>=0` | `M9b cE0` po M9a |
| `I14c` | general two-time classical kernel | `K_AB(t,t';k)=K_BA(t',t;k)^*` a dvojčasový integrálny quadratic form je nezáporný | `M9b cE0` po M9a |
| `I14d` | stationary spectral kernel, ak reprezentácia existuje | `S_AB(omega,k)=S_BA(omega,k)^*` a Hermitian PSD pre `(omega,k)` | `M9b cE0` po M9a |
| `I14e` | conservation nulls | energy a každý momentum conservation vector je ľavý aj pravý null smer na oboch sector indices; pri two-time/spectral objekte na oboch time/frequency stranách | `M9b cE0` po M9a |
| `I14q` | quantum residual | ordering, symmetrized covariance, commutator a uncertainty/positivity contract sa zmrazia osobitne; energy a momentum source-conservation vectors sú exact ľavé aj pravé null smery cez oba sector indices a oba kernel arguments | conservation exact po complete inventory cez `M1`; positivity `M9a/M9c OPEN`, neskôr scoped `cE0` |
| `I15` | thermodynamics | passivity alebo `nabla_mu s^mu>=0` v deklarovanej thermo doméne | otvorené, neskôr podmienené E0 |
| `I16` | stability | bez ghost/gradient instability; characteristic cone v povolenej causal doméne | otvorené, neskôr podmienené E0 |

Šírka intervalu alebo otvorený upper bound nie sú chyba. Sú explicitným
výsledkom, že dnešné zákony nedávajú užší mantinel bez D03/D05/D07/D09/D11
alebo P4 svedka.

## 7. DERIVATION_P3 — quotient pri dnešnom rozlíšení

Zmrazený porovnávací tuple je

```text
R_test = (Q_A,
          delta Q_A,
          delta F_A,
          pressure/shear/entropy closure,
          classical two-point noise kernel,
          initial-mode covariance,
          domain,
          recovery/null limits).
```

Dva vyplnené passporty sú `EQUIVALENT_AT_CURRENT_RESOLUTION` iba ak majú
rovnaký celý `R_test` v rovnakej doméne a pri rovnakom parameterovom bode.

| Quotient ID | Dnes možno zlúčiť | Nemožno vymazať |
|---|---|---|
| `Q01` | fundamental stochastic a deterministic-ensemble interpretáciu s rovnakým mean/covariance `R_test` | ontologický label a higher-cumulant rozdiel |
| `Q02` | rôzne allocation provenance s rovnakými background aj linear-response moments | action/kinetic/phenomenology lineage |
| `Q03` | rôzne frame reprezentácie po explicitnej kovariantnej bijektívnej mape | singularity a domain hranice frame |
| `Q04` | Markov limit a memory reprezentáciu iba ak full two-time/spectral kernel na test doméne dá rovnaký `R_test` | latentný memory label mimo domény |
| `Q05` | `s+M` a `s+M+X` iba ak explicitný `X` je zahrnutý a celý sektorový `R_test` je rovnaký | inventory/provenance `X`; nikdy nie hidden sink |
| `Q06` | MF1–MF4 efektívne realizácie s rovnakým `R_test` | `FAMILY_ID`, event/cohort labels, nonlinear a higher-cumulant latentné rozdiely |
| `Q07` | Poisson/sub-/super-Poisson modely iba ak ich relevantný two-point kernel je rovnaký | count-law a higher cumulants |

Rovnaký background `Q_A` nestačí na quotient. Rozdiel v `delta F_A`, shear,
noise, initial covariance, doméne alebo recovery limite znamená odlišnú
triedu už dnes.

## 8. Výsledná stavová matica

| Objekt | Výsledok DERIVATION_P0–P3 | Čo výsledok dokazuje | Čo nedokazuje |
|---|---|---|---|
| osy D04 | `SCHEMA_MAPPED_AT_DECLARED_RESOLUTION` | úplný typovaný slovník plus residual pre dnešný scope | product inventory alebo event energy |
| osy D08 | `SCHEMA_MAPPED_AT_DECLARED_RESOLUTION` | frame/recoil/operator/completion compatibility požiadavky | existenciu frame alebo operátora |
| osy D10 | `SCHEMA_MAPPED_AT_LINEAR_TWO_POINT_RESOLUTION` | correlation/noise typy a positivity/null brány | stochastic ontology, higher cumulants alebo quantum completion |
| `X_compat` | `TYPED_FIBER_SCHEMA_MAPPED` | nekompatibilné splice možno odmietnuť pred kandidátom | neprázdnosť fyzikálnych fiberov |
| `EC01–EC07`, `EC08b`, `EC09`, `EC06q` | `SCOPED_PRECHECK_EXCLUSIONS` | presne uvedené podrozsahy/reprezentácie sú neplatné | STOP MF1–MF4 alebo SM_v1 |
| `EC08a` | `UNRESOLVED_FRAME_DERIVATION` | neznámy frame sa nevyraďuje bez dôkazu | existenciu alebo platnosť frame |
| `F01–F09` | `UNRESOLVED_NEEDS_DERIVATION` | dnešné constrainty ich celé ešte nevylúčili | existenciu alebo pravdivosť |
| quotient | `DEFINED_BY_R_TEST` | pravidlo zlučovania pri dnešnom rozlíšení | jedinečnú mikrofyziku |
| residual | `OPEN_AND_REQUIRED` | slovník nepredstiera absolútnu exhaustivitu | že residual obsahuje svedka |

Najsilnejší oprávnený súhrn je:

```text
F_D0410_SCHEMA = MAPPED_AT_DECLARED_RESOLUTION
F_D0410_PHYSICAL_NONEMPTINESS = NOT_ESTABLISHED
F_D0410_UNIVERSAL_EMPTINESS = NOT_ESTABLISHED
MF1 = OPEN
MF2 = OPEN
MF3 = OPEN
MF4 = OPEN
```

## 9. Čo musí dodať najmenší nasledujúci P4 krok

Táto časť nie je povolením P4; iba definuje jeho budúci vstupný contract.
Najmenší svedok musí pre jeden explicitný `B` a jeden fiber bundle dodať:

1. úplný parent a completion inventory vrátane boundary carrierov;
2. local state, event/cohort identity, frame a causal support;
3. event/marked measure, energiu a signed four-momentum ledger;
4. rovnakú provenance pre `Q_A`, `delta Q_A`, `delta F_A`, pressure, shear,
   entropy a classical two-point noise;
5. source-off/recovery a nulové limity;
6. analytické kontroly M0–M14 v deklarovanej doméne.

P4 nesmie naraz skúšať všetkých deväť archetypov. Výber prvého svedka musí
byť odôvodnený najmenšou zložitosťou alebo rozlišovacou silou bez S8/H0
targetu a musí zostať versioned, aby neúspech jedného ansatzu nezabil fiber.

## 10. Stav, súborový rozpočet a nonclaims

```text
DOCUMENT249 = PASS_B6B2_2_POSSIBILITY_SPACE_PROTOCOL
DOCUMENT250 = PASS_B6B2_3_P0_P3_COMPATIBILITY_MATRIX
D04_D08_D10 = SCHEMA_MATRIX_DRAFTED_PHYSICAL_CONTENT_OPEN
D05_D07_D09_D11 = INDEPENDENTLY_BLOCKED_UNCHANGED
D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
D04_D11 = BLOCKED_UNCHANGED
MF1_MF2_MF3_MF4 = OPEN_UNCHANGED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
P5_4_G8_G9 = NOT_RUN_OR_BLOCKED_UNCHANGED
RUN_AUTHORIZED = false
PYTHON_PROCESSES = 0
LIVE_SCIENTIFIC_ARTIFACTS = 1
LIVE_CENTRAL_REGISTERS_UPDATED = 1
LIVE_TOTAL_FILES = 2
AUDIT_PACKAGE_COPIES = 0
```

Matica nevidí do Planckovej bunky. Nepriraďuje pravdepodobnosť, preferenciu
ani pravdivosť žiadnemu fiberu. Certifikuje iba presné lokálne rozpory a
zvyšok uchováva ako neodvodený alebo nerozlíšiteľný pri dnešnom rozlíšení.

## 11. Predregistrované auditné otázky

1. Pokrývajú typované osi všetky osi dokumentu 249 bez kartézskej
   enumerácie a bez skrytej default voľby?
2. Oddeľujú join failures nekompatibilný splice od fyzikálneho no-go?
3. Majú exclusion certifikáty `EC01–EC07`, `EC08b`, `EC09`, `EC06q` presný
   scope, dôkazovú triedu a doménu a zostáva `EC08a` správne nevylučujúci?
4. Neprisudzuje nijaký riadok `NOT_EXCLUDED` fyzickú existenciu?
5. Je quotient naozaj viazaný na celý `R_test`, nie iba background?
6. Zostáva residual otvorený a sú quantum/higher-cumulant nonclaims jasné?
7. Je P4 explicitne mimo tohto atómu a zostali všetky nadradené stavy,
   skóre a run authorization nezmenené?
