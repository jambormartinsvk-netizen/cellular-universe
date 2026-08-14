# B6b-2.10 — Q1R6 immutable-archive local reprocessing W10 preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R6-LOCAL-REPROCESS-W10-PREREG-20260727-253`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_LOCAL_ONLY_REPROCESS / NO_NEW_SOURCE_OPERATION / UTPHYS_BST_CONTENT_NOT_INSPECTED / NO_PYTHON`

## 1. Jediný cieľ a genealogické oddelenie

Cieľom je bez nového fetchu odstrániť jedinú klasifikačnú hranicu Q1R6:
frozen extension allowlist dokumentu277 nepoznal `utphys.bst`. Tento successor
nemení dokument277 ani result278, spätne ich neprepisuje a neresetuje Q1R6
`1/1_TERMINAL`. Vytvorí nový, samostatne auditovaný local-reprocessing atóm
nad byte-identickým immutable archive277A.

```text
Q1R3 = 24/24_TERMINAL / unchanged
Q1R5 = 15/15_TERMINAL / unchanged
Q1R6 source operations = 1/1_TERMINAL / unchanged
new internet or source operations = 0
archive277A copy or mutation = forbidden
receipt277B/result278 mutation = forbidden
```

Pravidlo sa zmrazuje pred čítaním alebo interpretáciou bytes `utphys.bst`.
Známy je iba jeho manifestový názov, dĺžka a SHA z receipt277B. Nevyberá sa
podľa fyzikálne priaznivého obsahu.

## 2. Immutable vstupy a stav

```text
parent prereg277 SHA256:
  C57404A73B558B4EF53D314EE9669347CBB94D35378CC2B67145864CFC5EBD56
archive277A SHA256:
  5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416
archive277A length:
  280993 bytes
receipt277B SHA256:
  E26C8CCEC518E0358D8B8368EF1AEC9261315571F31C2D3AD374D1DA31953D02
result278 SHA256:
  55E1722828985079568F76833C42D749796AFBDDCEE021B9D8CB435539A5FFCA
utphys.bst manifest-only facts:
  length=25698;
  SHA256=58D9FCB341615E47A32B3E17A5F4C67DF3086867EA43EE7671147C3BEECEA78B
current plan after task251 SHA256:
  2A672545D63BF9E2720733BD48447834BCA76DEFC0405184CC9B2C6BFDE883F0
K4 plan after task251 SHA256:
  5491C789F370D07FFC72E2EF7A9ADC671BFD9F87950C14A0A3491FEEDFF82DB2
P5 plan after task251 SHA256:
  A56C4973309915E1BB8CAC5792EF901B4F316F78FD8E611A2E5DA03AF1D1D5D5
event ledger through task251 SHA256:
  030482A8EA8967A845C5AB232C8E11CBE4C5043171351F94D7149E82E6875D38
progress review task252:
  BOUNDARY_OR_BLOCKER_PROGRESS / local immutable-archive reprocessing is
  smaller lawful successor than Q1R7
```

K4 ostáva `60/100`, P5 `3.5/6`, P4 work atoms `2`, physical witness
attempts `0`, `RUN_AUTHORIZED=false`.

## 3. Extension-independent classifier

Každý regular entry archive277A sa klasifikuje rovnakým obsahovým pravidlom;
prípona ani názov nerozhodujú.

### 3.1 Binary-magic vetva

Entry je `BINARY_NON_TEXT` iba pri jednom z exact magic preobrazov:

```text
PDF: 25 50 44 46 2D                         (%PDF-)
PNG: 89 50 4E 47 0D 0A 1A 0A
JPEG: FF D8 FF
GIF: 47 49 46 38 37 61 alebo 47 49 46 38 39 61
TIFF: 49 49 2A 00 alebo 4D 4D 00 2A
BMP: 42 4D
```

Binary entry zostáva v complete manifeste s path, length a SHA; jeho bytes sa
neinterpretujú ako fyzikálny text. Ak obrázok/binárny asset nesie jedinú
definíciu W10 objektu bez textového preobrazu, passport je MISSING, nie
doplnený z grafiky.

ZIP magic `50 4B 03 04`, `50 4B 05 06`, `50 4B 07 08` a GZIP magic `1F 8B`
znamenajú `UNCLASSIFIED_NESTED_CONTAINER` a okamžité
`SOURCE_UNIVERSE_NOT_CERTIFIED`; tento protokol nemá rekurzívnu vetvu.

Pri každom známom binary magic sa zároveň mechanicky vykoná text-candidate
kontrola zo sekcie 3.2. Ak entry prejde binary magic aj úplnú text vetvu,
výsledok je `AMBIGUOUS_MAGIC_TEXT / SOURCE_UNIVERSE_NOT_CERTIFIED`, nie
prednosť jednej vetvy.

### 3.2 Text vetva

Entry bez známeho binary magic je `READABLE_TEXT` iba ak súčasne:

1. neobsahuje NUL byte ani raw `DEL=0x7F`;
2. každý raw byte `<0x20` je iba `HT=09`, `LF=0A`, `FF=0C` alebo `CR=0D`;
3. celý byte stream sa dekóduje UTF-8 s explicitným exception decoder
   fallbackom; ak to zlyhá, celý stream sa dekóduje Windows-1252 s
   explicitným exception decoder fallbackom a bez replacement znaku;
4. po dekódovaní sa pre každý Unicode scalar/category zakáže
   `UnicodeCategory.Control`, okrem presne `HT`, `LF`, `FF`, `CR`; tým sú
   zakázané aj `U+007F` a C1 controls `U+0080..U+009F`;
5. encoder s exception fallbackom z použitého encodingu musí dať byte-exact
   pôvodný stream;
6. exact decoded content sa uloží s path/length/SHA/encoding boundary.

Entry bez binary magic, ktorý neprejde text vetvou, nested container alebo
entry s ambiguous binary/text klasifikáciou je
`UNCLASSIFIED_CONTENT` a celý výsledok je
`REVIEW_Q1R6_LOCAL_REPROCESS_SOURCE_UNIVERSE_NOT_CERTIFIED_NO_PHYSICAL_INFERENCE`.

Toto pravidlo je extension-independent a musí sa aplikovať aj na všetky už
známe `.tex`, `.bbl`, `.bib` a `.pdf` entries, nie iba na `utphys.bst`.

## 4. Lokálna integrity a safety procedúra

Pred reprocessingom musia byť absent `279A` a `280`. Archive277A musí presne
sedieť dĺžkou a SHA. Použije sa iba `C:\Windows\System32\tar.exe`, bez siete
a bez Pythonu.

Znova sa overí:

- `tar -tf` a `tar -tvf` order/count parity do 60 s;
- presne 11 regular entries, žiadny iný typ;
- path/traversal/backslash/ADS/drive/UNC/device/resolved-root guard z doc277;
- entry max 512, single max 128 MiB, total max 256 MiB;
- bounded extraction do nového same-volume GUID temp adresára do 120 s;
- extracted path/size/SHA parity s archive manifestom aj receipt277B.

Nesúlad znamená technical REVIEW bez fyziky. Temp sa odstráni po close.

## 5. Complete local receipt

Pri úspešnom reprocessingu sa create-new publikuje jediný nový raw receipt:

`279A_B6B2_10_Q1R6_LOCAL_REPROCESS_COMPLETE_SOURCE_RECEIPT.txt`.

Obsahuje archive hash, parent receipt hash, exact manifests, safety a timing,
všetkých 11 entry riadkov s content-derived class, byte round-trip status,
include-closure kontrolu a celé decoded contents každého `READABLE_TEXT`
entry. Boundary nesmie kolidovať s obsahom. Receipt sa neappenduje ani
neprepisuje.

```text
LOCAL_SOURCE_UNIVERSE_COMPLETE=PASS
```

platí iba ak všetkých 11 entries patrí do `BINARY_NON_TEXT` alebo
`READABLE_TEXT`, všetky parity prejdú a `\input`/`\include` closure nemá
medzeru. Nová source operation sa neúčtuje; Q1R6 ostáva `1/1_TERMINAL`.

## 6. Passport a S0–S13

Pri complete local universe sa z jedného Q1R6 modelu zmapuje:

```text
(Z_rec, P_rec, W_*, conservation, u_cell, congruence/dmu_cell,
 crossing, R_reset^Z, source-off, noncircularity).
```

Každý riadok musí mať exact source path + line/equation/section,
`SOURCE_EXACT`, `DERIVED_SAME_MODEL`, `E3_MAPPING` alebo `MISSING` a
evidence status. Passport kontrakt zostáva:

```text
W_rec(tau_birth)=0,
D_u W_rec=P_rec>=0,
W_*>0 a D_u W_*=0 počas parent cyklu,
chi_div=W_rec/W_*, chi_c=1,
prvý jednoduchý transverzálny upward crossing.
```

| ID | PASS podmienka |
|---|---|
| S0 | original primary Q1R6 identity a complete local source universe |
| S1 | jedna action/EOM/state/`T^{mu nu}`/convention/dimension/boundary/regime closure bez splice |
| S2 | fyzický lokálny `Z_rec` a `W[Z_rec]` bez hidden history clocku |
| S3 | on-shell pointwise `D_uW=P_rec>=0` s odvodeným zdrojom a reservoir |
| S4 | finite positive cycle-frozen `W_*` z tej istej fyziky |
| S5 | disjunktný local conservation ledger, residual-interface tok a source-off identity |
| S6 | source-native future unit `u_cell`, once-only congruence/worldtube a finite invariant `dmu_cell` |
| S7 | dosiahnuteľná absolútne spojitá jednoduchá upward cesta, nie jump/interpolation/init |
| S8 | dynamická `R_reset^Z`, zero daughter credit a oddelená residual energy |
| S9 | covariance/gauge meaning, causal well-posed režim, stabilita, jednotky/orientation |
| S10 | bez GW/S8/H0/division/biology/downstream targetu alebo fitu vo vstupe |
| S11 | všetky objekty v jednom provisional `Y_div` bez novej fyziky |
| S12 | bez fyzického vstupu/rezervoára nevzniká rast ani event |
| S13 | bez Pythonu, fitu, steam/completion, score/depth change alebo downstream runu |

`MISSING` je dovolené iba pri local-universe PASS. Jediné MISSING znamená,
že Q1R6 nie je complete W10.

## 7. Vetvy a účtovanie

```text
complete universe + eligible + S0-S13 PASS + celý passport:
  CANDIDATE_COMPLETE_W10_INTERFACE_ACTION_PASSPORT_FOUND
  / PENDING_INDEPENDENT_PHYSICS_AUDIT.

complete universe + koherentný interface model + MISSING:
  PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY
  / REVIEW_Q1R6_NOT_A_COMPLETE_W10_WITNESS.

complete universe + formula/physical/scope konflikt:
  PRECHECK_Q1R6_EXCLUDED_SCOPE / exact candidate-local cause.

classifier/integrity/closure failure:
  REVIEW_Q1R6_LOCAL_REPROCESS_SOURCE_UNIVERSE_NOT_CERTIFIED_NO_PHYSICAL_INFERENCE
  alebo exact technical variant.
```

Po complete-universe výsledku a nezávislom audite/main acceptance sa P4 work
atoms zvýšia `2->3` pri complete-W10, reference-only alebo candidate-local
exclusion. Physical witness attempts `0->1` iba pri complete-W10. Incomplete
vetva zachová oba počty.

## 8. Rozpočet a nonclaims

Výsledok sa publikuje presne raz do:

`280_B6B2_10_H_RDIV_C01_RW1_V1_Q1R6_LOCAL_REPROCESS_S0_S13_RESULT_SK.md`.

Nový atóm má najviac 3 live vedecké artefakty: document279, receipt279A a
result280. Archive277A je immutable input, nie kópia ani nový artefakt tohto
atómu. Opening batch je document279 + ledger. Central closure najviac
current/K4/P5 + ledger po výsledku. Audit package copies `0`, internet/source
operations `0`, Python processes `0`.

Žiadna vetva sama nedokazuje pravdu C01, `A_RW1` emptiness, P5.3 closure,
A3, score/depth change ani run permission.

## 9. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R6-LOCAL-REPROCESS-W10-PREREG-AUDIT-20260727-254
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task253
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::task254
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit::RESERVED_DISTINCT_RESULT_AUDIT
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_AUTHOR_PREREG_RESULT_AUDITOR_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R6_LOCAL_REPROCESS
CURRENT_PHASE: DRAFT_BEFORE_UTPHYS_BST_CONTENT_INSPECTION_OR_LOCAL_EXTRACTION
ALLOWED_NEXT_ACTION: independent read-only prereg audit; after PASS, SHA freeze and absent-target preflight
ALLOWED_READS: mandatory bootstrap; documents261,277-279; archive277A metadata/hash only; receipt277B header/accounting only; result278; ledger tasks248-253; current/K4/P5; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; read/inspect utphys.bst bytes/content; extract archive; internet/source operation; Python; physics/passport verdict; cap reset; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document277=C57404A73B558B4EF53D314EE9669347CBB94D35378CC2B67145864CFC5EBD56; archive277A=5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416; receipt277B=E26C8CCEC518E0358D8B8368EF1AEC9261315571F31C2D3AD374D1DA31953D02; result278=55E1722828985079568F76833C42D749796AFBDDCEE021B9D8CB435539A5FFCA; current=2A672545D63BF9E2720733BD48447834BCA76DEFC0405184CC9B2C6BFDE883F0; K4=5491C789F370D07FFC72E2EF7A9ADC671BFD9F87950C14A0A3491FEEDFF82DB2; P5=A56C4973309915E1BB8CAC5792EF901B4F316F78FD8E611A2E5DA03AF1D1D5D5; ledger_through_task251=030482A8EA8967A845C5AB232C8E11CBE4C5043171351F94D7149E82E6875D38
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit; after freeze receipt279A and result280
DONE_WHEN: no-fetch/no-reset genealogy, extension-independent classifier, exact binary magics, strict text/control/round-trip rules, local tar safety/parity, complete receipt, include closure, W10/S0-S13, accounting/nonclaims and three-artifact cap are fail-closed before utphys.bst content inspection
NEXT_ROLE: main_orchestrator
```
