# B6b-2.5 — H_D03-MF1-v1 autorov vstup a analytická preregistrácia

**Task:** `A2K4-B6B2-5-H-D03-MF1-V1-PREREG-20260724-104`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.5`  
**Autor teórie a schválenia testovacej rodiny:** Martin Jambor  
**Formalizácia preregistrácie:** Codex, hlavný orchestrátor  
**Stav:** `FINAL_PREREGISTRATION_AWAITING_EXTERNAL_SHA_RECEIPT / NO_RUN / NO_PYTHON`  
**Nadradený výsledok:** dokument 251,
`REVIEW_P4_V1_DEPENDENCY_FREEZE_BLOCKED_BEFORE_WITNESS`

## 1. Autorov nový vstup a jeho presný epistemický význam

Martin Jambor 2026-07-24 výslovne schválil:

> Schvaľujem H_D03-MF1-v1 ako testovaciu kandidátnu rodinu.

Schválenie povoľuje preskúmať nižšie zmrazenú množinu. Nie je tvrdením, že
Planckovská bunka tento mechanizmus používa, ani že niektorá hodnota
`pi_0` je fyzikálne pravdivá.

```text
SOURCE_CLASS = E3_PROVISIONAL / EXPLICIT_AUTHOR_APPROVED_TEST_HYPOTHESIS
DERIVATION_STATUS = CANDIDATE_FAMILY_AUTHORIZED_FOR_BOUNDED_TEST
NOT_A_FIXED_AUTHOR_AXIOM
NOT_E1_DIRECT_MEASUREMENT
NOT_A_PHYSICAL_PASS
```

## 2. Zmrazený objekt H_D03-MF1-v1

Nech `E_div/~` je spočítateľná množina kanonických fyzických parent udalostí
delenia, lokálne konečná na každom kompaktnom event supporte. Všetky
labelové reprezentácie tej istej fyzickej udalosti patria do jednej
ekvivalenčnej triedy `[e]`. Na merateľnom marked priestore
`M x Y` (spacetime krát lokálny event state) je kovariantná kladná counting
measure definovaná setovo

```text
N_div(A x S) = sum_[e] 1_A(x_[e]) 1_S(Y_[e]),

ekvivalentne
dN_div(dx,dY) = sum_[e] delta_g^(4)(x,x_[e]) delta_Y(dY,Y_[e]) dV_4(x),
dV_4(x) = sqrt(-g(x)) d^4x,
```

kde `delta_g^(4)` je definovaná vzťahom
`integral f(x) delta_g^(4)(x,x_e) dV_4 = f(x_e)`. Odlišné fyzické parent
udalosti majú odlišné kanonické ID a každé ID sa započíta práve raz.

Nech `G_-` obsahuje lokálnu históriu dostupnú tesne pred parent udalosťou.
Predikovateľná/merateľná conditional mean (kompenzátorová) measure je

```text
R_div(A x S) = E[N_div(A x S) | G_-],
```

pričom zápis `dR_div(dx,dY)` vždy označuje túto marked measure, nie ďalšiu
nezávisle zvolenú rate funkciu. Pre každú kanonickú parent udalosť sa
zavádza thinning mark

```text
B_e in {0,1},
P(B_e=1 | Y_e,I_res=1,G_-) = pi_0,
B_e=0 pri I_res=0,
E[B_e | Y_e,G_-] = pi_0 I_res(Y_e),
0 <= pi_0 <= 1,
I_res(Y_e) = 1_{E_available(C_x;Y_e) > 0}.
```

`Y_e` je lokálny stav na event supporte. `E_available` musí byť lokálny
skalár v regulárnom cell frame; jeho konkrétny vzorec ani frame týmto
artefaktom nie sú odvodené. Nezávislosť rôznych `B_e`, Poissonov počet ani
vyššie count cumulants sa nepredpokladajú.

`I_res:Y->{0,1}` musí byť merateľná a predikovateľná voči `G_-`.
Realizovaná digestion counting measure a jej podmienená kompenzátorová
measure sú na tom istom marked priestore

```text
N_D(A x S) = sum_[e] B_e 1_A(x_[e]) 1_S(Y_[e]),
R_D(A x S) = integral_(A x S) pi_0 I_res(Y) dR_div(x,Y),
skrátene dR_D(dx,dY) = pi_0 I_res(Y) dR_div(dx,dY),
0 <= dR_D <= dR_div.
```

Ak `B_e=1`, platí

```text
PARENT_EVENT_ID_D = PARENT_EVENT_ID_div.
```

Jedna parent division udalosť teda vytvorí v tejto rodine najviac jednu
parent digestion udalosť. Dcérska kohorta a neskorší completion event majú
nové ID podľa first-passage ledgera. `pi_0` je jeden bezrozmerný parameter
rodiny; nie je fitovaný na `S8`, `H0`, realizovaný `k` ani kozmický čas.

## 3. Doména a presné hranice rodiny

```text
X_H = {
  (dR_div, canonical_event_map, I_res, pi_0):
  dR_div je lokálne konečná nezáporná invariantná marked kompenzátorová measure,
  canonical_event_map countuje každú fyzickú parent udalosť raz,
  I_res in {0,1} je lokálny availability gate,
  pi_0 in [0,1]
}.
```

Rodina je iba prvý D03 bridge. Neobsahuje výber eventovej energie,
four-momentum mark distribution, steam dispersion/collision law,
completion hazard ani noise/response closure.

Parameterové okraje majú vopred tento význam:

| Podrozsah | Predregistrovaný význam |
|---|---|
| `pi_0 < 0` | vylúčené pozitivitou fyzickej thinning measure |
| `pi_0 = 0` | exact null-coupling člen rodiny; žiadne digestion parent eventy |
| `0 < pi_0 < 1` | podmienený čiastočný thinning; nie je predpoklad Poissonovej nezávislosti |
| `pi_0 = 1` | každý eligible division event vytvorí práve jeden digestion parent event |
| `pi_0 > 1` | vylúčené one-parent/at-most-one-event normalizáciou |
| `I_res = 0` | `dR_D=0` pre ľubovoľné dovolené `pi_0` |

## 4. Predregistrovaný analytický test H0–H8

Test sa vykoná bez Pythonu a bez numerického solvera nad presne týmto
zmrazeným objektom.

| ID | Kontrola | PASS podmienka | Zlyhanie znamená |
|---|---|---|---|
| `H0` | typ a jednotky | `pi_0,I_res` bezrozmerné; `N_div,N_D` lokálne konečné counting measures; `R_div,R_D` ich kompenzátorové measures na tom istom `M x Y` | `REVIEW_ILL_TYPED_CANDIDATE` |
| `H1` | kanonická event identity | ekvivalentné labely -> jedno ID, odlišné parent eventy -> odlišné ID, once-only count | chýbajúca mapa=`REVIEW`; dokázaný duplicate count=`IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `H2` | pozitivita | `dR_div>=0` a `0<=pi_0 I_res<=1` dávajú `dR_D>=0` | nedefinovaná measure=`REVIEW`; dokázaná negatívna fyzická measure alebo `pi_0` mimo probability domény=`IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE` |
| `H3` | MF1 horný mantinel | `dR_D<=dR_div` na tej istej measure/doméne | `REVIEW_NOT_DIVISION_LOCKED` |
| `H4` | conditional event-rate off only | `I_res=0 => dR_D=0` bez kozmického clocku | `REVIEW_EVENT_RATE_OFF_NOT_DEFINED`; neuzatvára D07 energy-weighted source ani completion |
| `H5` | nulová väzba | `pi_0=0 => dR_D=0` | `REVIEW_NULL_LIMIT_FAILURE` |
| `H6` | nonzero vnútro mapy | pri `0<pi_0<=1` a `integral_(U x Y) I_res(Y)dR_div>0` (ekvivalentne `R_div((U x Y) intersect {I_res=1})>0`) je `R_D(U x Y)>0` | iba mapová neprázdnosť/neprázdnosť sa nepreukáže |
| `H7` | zakázané argumenty | žiadny `t`, `ln a`, `H0`, realizovaný `k`, `S8` alebo legacy target | `PROCESS_CONTRACT_FAILURE` |
| `H8` | hranica tvrdenia | výsledok nevyhodnotí `E_J`, `Pi_J`, `K_s`, `K_C`, `K_Rtest` ani M0–M14 ako celok | overclaim/fail-closed oprava |

## 5. Zmrazené rozhodovacie vetvy

```text
Ak H0-H8 prejdú:
  PASS_H_D03_MF1_V1_EVENT_MEASURE_BRIDGE_BEHAVIORAL_OPEN
  iba pre mapping/event-measure scope.

Ak presne pi_0<0 alebo pi_0>1:
  IMPOSSIBLE_E0_CERTIFIED / PRECHECK_EXCLUDED_SCOPE
  iba pre tieto parameterové podrozsahy tejto rodiny.

Ak invariantná measure, canonical event map alebo local I_res nie sú
  matematicky dobre definované ani podmienene:
  REVIEW_H_D03_MF1_V1_DEFINITIONAL_BOUNDARY.

Nikdy z tohto testu:
  NONEMPTY_WITNESS pre celý P4,
  STOP/PASS MF1,
  fyzikálna pravdivosť pi_0,
  D03 CLOSED,
  zmena K4/P5,
  povolenie Pythonu alebo forward S8/H0 testu.
```

Ak mapový bridge prejde, prvým zostávajúcim D03 blockerom bude stále
evaluable event-energy/mark law a regular `C_x`/cell-frame budget. Presné
poradie sa potvrdí až v result audite; tento text ho nesmie post-hoc meniť.

## 6. Frozen task capsule

```text
TASK_ID: A2K4-B6B2-5-H-D03-MF1-V1-PREREG-20260724-104
ROLE: main_orchestrator (artifact author) -> physics_track_auditor
ROLE_CONFIG_SHA256: 9A1E91215069253B022941DD45F9F52F6058D8CF0AB8F2C46719774EA3B1353F
ASSIGNED_AGENT_TASK_ID: /root/b6b2_2_physics_auditor
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: N/A_NO_PYTHON_ARTIFACT
INTERNAL_AUDITOR_TASK_ID: /root/b6b2_2_physics_auditor
PACKAGE_CURATOR_TASK_ID: N/A_AT_THIS_PHASE
EXTERNAL_AUDITOR_TASK_ID: N/A_AT_THIS_PHASE
SEPARATION_OF_DUTIES_CHECK: PASS; /root != /root/b6b2_2_physics_auditor; no package roles active
ROUTE: A1_K1_A2_K4_P5.3_B6b-2.5_H_D03_MF1_v1
CURRENT_PHASE: FINAL_PREREGISTRATION_ADMIN_DELTA_AUDIT
PARENT_DECISION: REVIEW_P4_V1_DEPENDENCY_FREEZE_BLOCKED_BEFORE_WITNESS
CLAIM: bounded event-measure/thinning candidate family authorized by Martin Jambor
NONCLAIMS: no Planck-cell fact, full D03 closure, P4 witness, MF1 verdict, score/depth change or run permission
ALLOWED_NEXT_ACTION: independent read-only final administrative-delta audit; then external SHA receipt without further document edit
ALLOWED_READS: mandatory bootstrap; documents 249-252; exact rules and plans listed in immutable inputs
ALLOWED_WRITES: none for auditor
FORBIDDEN_ACTIONS: change candidate family; select pi_0; add event energy/steam/completion law; Python; solver; S8/H0/k fit; state/score/depth/RUN_AUTHORIZED change
IMMUTABLE_INPUT_PATHS_AND_SHA256:
  tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/249_B6B2_2_D04_D08_D10_POSSIBILITY_SPACE_DERIVATION_PROTOCOL_SK.md=A3888FBB860FB4AB71005B9079AF15856EE9A8C2504DEB712D0148C8BB578264
  tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/250_B6B2_3_D04_D08_D10_P0_P3_COMPATIBILITY_CONSTRAINT_MATRIX_SK.md=50DD361BCCD989458A7614BCCDF625256BC1E9994779DB3140F1D2B709B07B58
  tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/251_B6B2_4_P4_V1_MF1_F01_F03_DEPENDENCY_FREEZE_AND_WITNESS_ATTEMPT_SK.md=775946B341A73B1D5F51623A725F6AC3C734BC0EFEA306523E9170AA5EA62ED9
  tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md=4A0BA3539CFCEE23AEBBA246E4DD1486EEE315B036FE3A0A23821656932A27EC
  tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md=AB29543ACD4F132276DF59E1020EEA6FB3A042C78FAAA1B7DDD448F5479D0FF1
  tracks/A1/A1K1/A2/A2K4/HISTORY/00_EVENT_LEDGER.md snapshot through task104=838D64D64414254D0049232F332176E06E2114AF76434BBEFA518382DC5A6594
PREREG_SHA256: TO_BE_RECORDED_EXTERNALLY_WITHOUT_FURTHER_DOCUMENT_EDIT
RUN_AUTHORIZED: false
TIMEOUT_AND_OUTPUT_GUARDS: no executable process; analytical H0-H8 result must be a new immutable document
OUTPUT_PATHS: chat-only audit recommendation; after acceptance, one new result document
LIVE_FILE_BUDGET: prereg phase 1 scientific artifact + 1 event-ledger append; no central plan batch
DONE_WHEN: final byte-identical preregistration is independently confirmed and its SHA is recorded outside this document
NEXT_ROLE: main_orchestrator
```

## 7. Stav a súborový rozpočet

```text
H_D03_MF1_V1 = AUTHOR_APPROVED_TEST_CANDIDATE / CONTENT_AUDIT_PASS / ADMIN_DELTA_PENDING
D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
P4_PHYSICAL_WITNESS_ATTEMPTS = 0
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
PYTHON_PROCESSES = 0
LIVE_SCIENTIFIC_ARTIFACTS = 1
LIVE_CENTRAL_REGISTERS_UPDATED = 1
LIVE_TOTAL_FILES = 2
AUDIT_PACKAGE_COPIES = 0
```

## 8. Predregistrované auditné otázky

1. Reprezentuje kovariantná counting measure fyzické udalosti bez
   labelového double-countu a bez predpokladu hladkej Poissonovej intensity?
2. Je `dR_D=pi_0 I_res dR_div` presne MF1 thinning family s intervalom
   `[0,1]`, nie tvrdenie o pravdivej hodnote `pi_0`?
3. Je source-off iba podmienený lokálnou definíciou `E_available/C_x/frame`
   a nie potichu uzavretý D07 alebo D03 energy law?
4. Sú `pi_0<0` a `pi_0>1` jediné okamžité E0 parameterové exclusions tejto
   rodiny a zostáva `pi_0=0` platným null členom?
5. Dokáže H6 najviac neprázdnosť event-measure mapy, nie úplný fyzikálny
   P4 witness?
6. Ostávajú event energy, steam, completion, response/noise, K4/P5 a Python
   mimo povoleného tvrdenia?
