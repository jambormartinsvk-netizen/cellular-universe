# B6b-2.10 — Q1R3 explicitný S0–S13 physics-screen kapsul

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-S0-S13-PREREG-20260727-187`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_PREREGISTRATION / EXACT_Q1R3_ONLY / NO_NEW_SEARCH / NO_PYTHON`

## 1. Jediný cieľ a nemenný kandidát

Cieľom je vykonať už zmrazený screen `S0–S13` z dokumentu 261 nad jediným
obnoveným kandidátom:

```text
frozen rank: Q1R3
title: Model-dependent analysis method for energy budget of the
       cosmological first-order phase transition
authors: Xiao Wang; Chi Tian; Fa Peng Huang
arXiv: 2301.12328
journal: JCAP 07 (2023) 006
DOI: 10.1088/1475-7516/2023/07/006
family: F-A
```

Dokument266 prijal iba dostupnosť rovníc. Tento atóm rozhodne, či presne tento
model poskytuje celý W10 passport; nesmie vybrať iný zdroj, zmeniť rank ani
doplniť chýbajúcu fyziku z companion paperu.

## 2. Nemenný W10 a klasifikačný kontrakt

Vyžadovaný passport zostáva:

```text
(Z_rec, P_rec, W_*, u_cell, dmu_cell, R_reset^Z,
 disjoint local conservation ledger)
```

Každé pole sa označí iba `SOURCE_EXACT`, `DERIVED_SAME_MODEL`, `E3_MAPPING`
alebo `MISSING`. `E3_MAPPING` nesmie vytvoriť nový stav, tok, threshold,
congruence, measure, reset ani conservation channel. Jediné `MISSING`
vylučuje complete-W10 výsledok.

Výsledok musí obsahovať jednu povinnú passport tabuľku, v ktorej nijaký
riadok nemožno vynechať:

| Passport pole | Povinný fyzický obsah |
|---|---|
| `Z_rec` | explicitná lokálna konfigurácia a `W_rec=W[Z_rec]` |
| `P_rec` | odvodený causal current/stress-work/reservoir power, znamienko a podmienky `>=0` |
| `W_*` | kladná finite pre-event cycle-frozen barrier/interface work z tej istej fyziky |
| conservation | disjunktné stored/dissipated/RW1-export/external-loss kanály, local identity a residual-interface tok |
| `u_cell` | source-native future-directed unit timelike pole |
| congruence/`dmu_cell` | regular once-only parent worldtube/congruence a finite invariant proper measure |
| crossing | dosiahnuteľná on-shell absolútne spojitá jednoduchá upward cesta |
| `R_reset^Z` | fyzická daughter/event mapa, zero daughter credit a oddelená residual energy |
| source-off | bez vstupu a dostupného reservoiru nevzniká rast ani crossing |
| noncircularity | bez downstream/observačného/biologického targetu vo vstupe |

Každý riadok má samostatné stĺpce `SOURCE_EQUATION_OR_SECTION`,
`PROVENANCE_CLASS` a `EVIDENCE_STATUS`. `PROVENANCE_CLASS` je iba jedna zo
štyroch hodnôt vyššie. `EVIDENCE_STATUS` je `ASSESSABLE_COMPLETE` alebo
`NOT_ASSESSABLE_EVIDENCE_INCOMPLETE`. Pri druhom stave sa provenance nesmie
nútene označiť `MISSING`; zostáva `UNASSIGNED_DUE_TO_INCOMPLETE_EVIDENCE`.
Neúspešný `find` pattern sám nikdy nedokazuje absenciu. `MISSING` je prípustné
iba po evidence-complete full-text/section coverage.

Rodičovský kontrakt sa nemení:

```text
W_rec(tau_birth)=0,
D_u W_rec=P_rec>=0,
W_*>0 a D_u W_*=0 počas parent cyklu,
chi_div=W_rec/W_*, chi_c=1,
prvý jednoduchý transverzálny upward crossing.
```

`W_rec` musí byť rekonštruovateľná z lokálneho fyzického `Z_rec`, nie z
pridaného history integrátora. Barrier/free energy nie je automaticky reálne
dodaná kumulatívna work energia.

## 3. Immutable vstupy

- document261 SHA-256
  `FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B`;
- document264 SHA-256
  `DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A`;
- frozen document265 SHA-256
  `544D63C41537CACBA13C59A2EDD1CEFE936139B56A3AF12FF3D5515AC0FA3DAC`;
- access evidence265A SHA-256
  `006BF1E8BC3A88F2A9D2F68EA031AFD8CE6665DE8521436177EA6AA2E69E0F5D`;
- accepted access result266 SHA-256
  `E7CB30F250B7C263C68088C98DE3FBBE55097907FF9A44235617236199A4F19D`.

Evidence265A `A2_ARXIV_LANDING` už fixuje same-identity primary arXiv full-text
view s 527 riadkami a čitateľnými rovnicami vrátane `(2.1)–(2.3)`, `(3.4)`,
`(4.11)–(4.14)` a `(4.19)–(4.20)`.

## 4. Frozen same-source transport a dôkazová hranica

Nie je povolený `search_query`, nový titul, nový DOI, companion, citation
follow ani neskorší query hit. Povolené sú iba read-only `open`, `click` a
`find` operácie v exact same-identity arXiv zázname 2301.12328:

1. najprv sa skúsi existujúci recovered full-text provider ref
   `turn39view0` jedným `open(response_length=long)`;
2. ak ref vráti cache miss alebo neúplný landing text, otvorí sa presne
   `https://arxiv.org/abs/2301.12328`;
3. z tohto záznamu sa smie otvoriť alebo kliknúť iba jeho same-record HTML,
   PDF alebo TeX full-text route; priority sú HTML, PDF, TeX;
4. po získaní full-text ref sa v jednom batched `find` calle preveria presne
   tieto patterns v tomto poradí:

```text
energy-momentum
friction term
energy conservation
critical bubble
nucleation
initial condition
source
reservoir
reset
daughter
worldtube
congruence
proper measure
residual
```

5. otvoria sa iba line windows vrátené týmito findmi a exact equation/section
   windows potrebné pre `(2.1)–(2.3)`, scalar-field EOM/friction,
   hydrodynamical conservation/matching, `(3.4)` a reprezentatívny model;
6. celkový cap po freeze je `open+click+find <= 24` operations; jedna batched
   požiadavka sa počíta podľa počtu vnútorných operations;
7. cache miss nesmie byť interpretovaný ako absencia fyzikálneho objektu.
   Ak úplnosť zdroja alebo relevantný kontext rovníc nemožno verifikovať v
   cape, výsledok je iba
   `REVIEW_Q1R3_SCREEN_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE`.

Pred prvou novou operation musí hlavný orchestrátor zopakovať absent-target
preflight exact ciest 267A aj 268. Ak ktorýkoľvek cieľ existuje, výsledok je
`REVIEW_Q1R3_SCREEN_TARGET_COLLISION_NO_OVERWRITE`; žiadna operation ani
overwrite nie sú povolené.

Každý tool návrat sa bez úprav v tom istom `functions.exec` zapíše do nového
append-only súboru:

`267A_B6B2_10_Q1R3_S0_S13_PHYSICS_SCREEN_EVIDENCE.txt`.

Každý blok má unikátne `SCREEN_EVIDENCE_ID`, call type, exact target/patterns,
provider payload, `BEGIN_EXACT_SCREEN_RETURN`, raw hodnotu a
`END_EXACT_SCREEN_RETURN`. String sa nemení; non-string sa serializuje
`JSON.stringify(result, null, 2)`. Transport alebo append failure zakazuje
rerun už spotrebovanej operation aj fyzikálny záver. Recoverable raw body je
presne obsah po newline ukončujúcom jediný BEGIN riadok a pred jedným
publication-added newline bezprostredne pred jediným END riadkom. Ak raw
hodnota sama obsahuje celý delimiter na samostatnom riadku alebo framing nie
je jednoznačný, atóm končí
`REVIEW_Q1R3_SCREEN_EVIDENCE_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE`.
Rovnaký technický výsledok platí pri transport exception, publish/append
failure alebo neobnoviteľnom partial receipte. Čiastočný súbor sa zachová a
nesmie sa potichu opraviť.

## 5. Povinný screen S0–S13

| ID | PASS podmienka |
|---|---|
| `S0` | pôvodný research source, exact Q1R3 identita a dostupné relevantné rovnice |
| `S1` | jedna action/EOM/state/`T^{mu nu}`/convention/dimension/boundary/regime closure; bez splice |
| `S2` | fyzický lokálny `Z_rec` a `W[Z_rec]` bez hidden history clocku |
| `S3` | na tej istej on-shell pre-event ceste pointwise `D_uW=P_rec>=0`, s odvodeným zdrojom/rezervoárom |
| `S4` | finite positive cycle-frozen `W_*` z tej istej fyziky |
| `S5` | disjunktný local energy-momentum ledger, residual-interface tok a source-off identita |
| `S6` | source-native future unit `u_cell`, regular once-only parent worldtube/congruence a finite invariant `dmu_cell` |
| `S7` | dynamicky dosiahnuteľná on-shell absolútne spojitá jednoduchá upward cesta; nie ručná interpolácia ani jump |
| `S8` | fyzická dynamická `R_reset^Z`, zero daughter credit a oddelená residual energy; nie rename, numerical reinitialization ani accounting-only reset |
| `S9` | covariance/source-native gauge invariance, causal well-posed použitý režim, bez relevantnej ghost/gradient/negative-reservoir instability; jednotky, pozitivita a orientation sú konzistentné |
| `S10` | bez `R_div`, produktov, expanzného outputu, `S8/H0/k`, biology targetu alebo fitu vo vstupe |
| `S11` | všetky fyzicky existujúce passport objekty možno mapovať do jedného provisional `Y_div` bez novej fyziky |
| `S12` | bez fyzického vstupu/rezervoára nevzniká rast ani event |
| `S13` | bez Pythonu, fitu, steam/completion, zmeny skóre/hĺbky alebo downstream runu |

Pri každom `S#` musí výsledok uviesť `PASS`, `FAIL`, `MISSING` alebo
`NOT_ASSESSABLE_EVIDENCE_INCOMPLETE`, exact equation/section evidence a jasne
oddeliť source statement od E3 mapovania. Absencia sa smie označiť `MISSING`
iba po full-text find/section coverage; inak je `NOT_ASSESSABLE`.

## 6. Zmrazené rozhodovacie vetvy

```text
Ak S0-S13 prejdú a nijaké W10 pole nie je MISSING:
  CANDIDATE_COMPLETE_W10_INTERFACE_ACTION_PASSPORT_FOUND
  / PENDING_INDEPENDENT_PHYSICS_AUDIT.

Ak Q1R3 je koherentný interface/reference model, ale chýba fyzická
Y_div/cell/reset alebo iné povinné W10 pole:
  PASS_Q1R3_REFERENCE_INTERFACE_MODEL_ONLY
  / REVIEW_Q1R3_NOT_A_COMPLETE_W10_WITNESS.

Ak evidence-complete screen odhalí candidate-only formula, physical alebo
scope konflikt vrátane conservation, causality, reachability, stability,
sign, positivity, orientation, units, jump-only crossingu, barrier bez causal
delivered-work ledgera, fitted thresholdu alebo double creditu:
  PRECHECK_Q1R3_EXCLUDED_SCOPE
  / CAUSE_Q1R3_CANDIDATE_ONLY_FORMULA_PHYSICAL_OR_SCOPE_CONFLICT
  / REVIEW_Q1R3_NOT_A_COMPLETE_W10_WITNESS.

Ak je same-source evidencia neúplná alebo transport zlyhá:
  REVIEW_Q1R3_SCREEN_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE.
```

Tieto vetvy sú úplné: každý evidence-complete `FAIL` ide do tretej vetvy;
každé evidence-complete `MISSING` bez fyzikálneho konfliktu ide do druhej;
každý neassessable alebo technický prípad ide do štvrtej. Žiadna vetva nie je
C01 no-go, global literature no-go ani dôkaz prázdnosti `A_RW1`.

Pri prvej vetve je Q1R3 prvým kompletným kandidátom a frozen search sa podľa
dokumentu261 končí. Až po nezávislom audite a hlavnom prijatí sa vtedy mení
`P4 work atoms 2 -> 3` a `physical-witness attempts 0 -> 1`. Pri
reference-only, excluded/conflict alebo evidence-incomplete Q1R3 ostáva širší
frozen search nedokončený a počty zostávajú `2` a `0`.

## 7. Výstup, rozpočet a nonclaims

Po uzavretí evidence267A sa presne raz do neprítomného cieľa publikuje:

`268_B6B2_10_H_RDIV_C01_RW1_V1_Q1R3_S0_S13_PHYSICS_SCREEN_RESULT_SK.md`.

Kolízia zistená pri preflight alebo publication race znamená
`REVIEW_Q1R3_SCREEN_TARGET_COLLISION_NO_OVERWRITE`, fail-closed bez overwrite
a bez fyzikálneho záveru. Tento atóm má najviac 3 live
vedecké artefakty (267, 267A, 268), jeden append-only event-ledger update pri
otvorení a najviac jeden štvorsúborový central closure batch po prijatí
výsledku. Audit package copies `0`.

Bez ohľadu na výsledok z tohto atómu samotného nevzniká pravda/nepravda C01,
global literature no-go, closure P4/MF1/D03/P5.3, zmena `K4=60/100`,
`P5=3.5/6`, `RUN_AUTHORIZED=false`, Python ani S8/H0 fit. Pri nekompletnom
Q1R3 sa ďalší kandidát nesmie otvoriť bez progress review a nového frozen
successor kapsulu.

## 8. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-S0-S13-PREREG-AUDIT-20260727-188
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task187
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::task188
INTERNAL_AUDITOR_TASK_ID: RESERVED_DISTINCT_RESULT_AUDITOR_NOT_ACTIVE
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_ALL_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R3_S0_S13
CURRENT_PHASE: DRAFT_EXPLICIT_PHYSICS_SCREEN_BEFORE_ANY_NEW_SOURCE_OPERATION
ALLOWED_NEXT_ACTION: independent read-only prereg audit; after PASS, out-of-file SHA freeze and absent-target preflight
ALLOWED_READS: mandatory bootstrap; documents259-267; evidence265A; relevant event-ledger tasks155-187; physics auditor role config and manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: web/search/open/click/find; edit; physics verdict; new source/candidate/companion; Python; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document261=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; document264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A; document265=544D63C41537CACBA13C59A2EDD1CEFE936139B56A3AF12FF3D5515AC0FA3DAC; evidence265A=006BF1E8BC3A88F2A9D2F68EA031AFD8CE6665DE8521436177EA6AA2E69E0F5D; document266=E7CB30F250B7C263C68088C98DE3FBBE55097907FF9A44235617236199A4F19D
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit; after freeze exact evidence267A and result268 paths from section 7
DONE_WHEN: exact identity-only transport, raw persistence, operation cap, evidence-incomplete branch, full S0-S13/passport mapping, result branches, accounting and nonclaims are fail-closed
NEXT_ROLE: main_orchestrator
```
