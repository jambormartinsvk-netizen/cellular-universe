# B6b-2.10 — H_RDIV-C01-RW1-v1 preregistrácia získania jedného úplného W10 passportu

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-W10-SOURCE-PREREG-20260727-155`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Autorov pokyn:** `získať jeden kompletný W10`  
**Stav:** `CORRECTED_DRAFT_PREREGISTRATION / AWAITING_EXACT_DELTA_REAUDIT / NO_SEARCH_YET / NO_RUN / NO_PYTHON`

## 1. Cieľ a presný význam úspechu

Cieľom je nájsť a explicitne zmapovať **jeden** lokálny interface-action
model, ktorý súčasne dodá celý fyzický W10 passport:

```text
(Z_rec, P_rec, W_*, u_cell, dmu_cell, R_reset^Z, disjoint conservation ledger).
```

Úspech neznamená pravdivosť modelu pre bunky priestoru. Znamená iba, že
existuje jeden fyzicky formulovaný `E3_PROVISIONAL` svedok, ktorého všetky
položky pochádzajú z jednej koherentnej lokálnej fyziky a možno ich následne
nezávisle testovať. Autorov pokyn sa nesmie čítať ako povolenie doplniť
chýbajúcu položku odhadom.

## 2. Nemenný rodičovský kontrakt

Dokument 259 zostáva nedotknutý. Kandidát musí zachovať:

```text
W_rec(tau_birth)=0,
D_u W_rec=P_rec>=0,
W_*>0,
D_u W_*=0 počas parent cyklu,
chi_div=W_rec/W_*,
chi_c=1,
```

a prvý jednoduchý transverzálny upward crossing. `W_rec` musí byť
rekonštruovateľná z fyzického lokálneho stavu `Z_rec`, nie iba z pridaného
history integrátora.

## 3. Zmrazená source-search stratégia

Použijú sa iba primárne vedecké zdroje: pôvodný research paper, jeho
autorský preprint alebo vydavateľská verzia. Review, blog, populárny text a
sekundárne zhrnutie smú navigovať, ale nesmú niesť passport claim.

Rodiny sa preveria v tomto poradí:

1. `F-A` — lokálny kovariantný scalar-field/domain-wall model s explicitným
   fluid/reservoir sektorom a odvodeným kritickým interface barrierom;
2. `F-B` — kovariantný alebo relativistický irreversible phase-field/damage
   model s jedným energetickým a disipačným ledgerom;
3. `F-C` — lokálny materiálový phase-field fracture/interface model iba
   vtedy, ak samotný primárny framework explicitne dodá fyzický časový tok,
   mieru a reset mapovateľné bez externého transplantovania.

Zmrazené vyhľadávacie dotazy:

```text
Q1: relativistic scalar field fluid first order phase transition stress energy conservation critical bubble energy primary paper
Q2: covariant critical bubble surface tension energy barrier scalar field fluid primary paper
Q3: relativistic irreversible phase field energy balance internal variable primary paper
Q4: covariant phase field fracture interface energy conservation reset primary paper
```

Provider a poradie sú zmrazené takto:

1. vykonajú sa presne dve volania `web__run/search_query` s
   `response_length=long`, bez domain/recency filtra: prvé obsahuje `Q1,Q2`,
   druhé `Q3,Q4`; žiadny ďalší query rewrite ani pagination nie sú povolené;
2. `F-A` dostane ordered union hitov `Q1` a potom `Q2`; `F-B` dostane `Q3`;
   `F-C` dostane `Q4`;
3. v každom query sa zachová providerom vrátené poradie. Deduplikácia používa
   v poradí DOI, arXiv ID a potom normalizovaný `title+year+first_author`;
   prvý výskyt vlastní rank;
4. každý hit dostane immutable ledger riadok: global/family/query rank,
   bibliografická identita, URL, `ELIGIBLE_PRIMARY`, `NAVIGATION_ONLY`,
   `SECONDARY_EXCLUDED`, `DUPLICATE`, `INACCESSIBLE` alebo iný exact exclusion
   reason a open status;
5. eligible je iba pôvodný research zdroj s dostupnou akciou/EOM alebo
   energetickými rovnicami relevantnými pre definíciu danej rodiny. Review,
   thesis, proceedings summary, patent, blog, source bez rovníc alebo model
   mimo definície rodiny sa loguje, ale nie je eligible;
6. secondary/navigation hit smie viesť iba na canonical DOI, vydavateľskú
   verziu alebo autorský preprint toho istého primárneho zdroja. Takto
   vyriešený primárny zdroj zdedí rank pôvodného hitu;
7. otvárajú a vyhodnocujú sa eligible kandidáti v rank poradí, najviac päť
   na rodinu. Zero-hit a menej než päť sa explicitne zaznamenajú;
8. inaccessible eligible kandidát sa najprv skúsi cez jeho canonical
   publisher/preprint alternatívu. Ak rovnice stále nemožno overiť, search sa
   zastaví `REVIEW_SEARCH_COVERAGE_INCOMPLETE`; skorší hit sa nesmie preskočiť;
9. prvý kandidát v poradí, ktorý prejde všetkými S0–S13, je jediný vybraný
   anchor a search končí. Ak prvých päť eligible kandidátov rodiny neprejde,
   pokračuje sa ďalšou rodinou. Po vyčerpaní F-C sa search končí;
10. companion zdroje patria do rovnakého päťzdrojového family capu. Najviac
    dva možno otvoriť v citation poradí anchoru iba na objasnenie tej istej
    fyziky; nesmú pridať nový dynamický sektor, stav, constitutive closure,
    reset ani conservation kanál.

Anchor a každý companion musia mať exact parity akcie, EOM, state space,
`T^{mu nu}`/current ledgera, sign a gauge konvencií, dimenzie, boundary
conditions a fyzikálneho režimu. Nezhoda znamená `S1 FAIL / NO_SPLICE`.
Bibliografická dostupnosť sama nie je fyzikálny PASS.

## 4. Povinná passport mapa

Jeden prijateľný kandidát musí v jednej tabuľke doložiť:

| Pole | Povinný obsah |
|---|---|
| `Z_rec` | explicitná lokálna fyzická konfigurácia; exact source equation a mapovanie `W_rec=W[Z_rec]` |
| `P_rec` | odvodený causal current, stress-work alebo reservoir power; exact znamienko a podmienky `P_rec>=0` |
| `W_*` | kladná konečná barrier/interface work z tej istej akcie; určená pred eventom a cycle-frozen |
| conservation | disjunktné stored/dissipated/RW1-export/external-loss kanály bez double countu a s lokálnou energy-momentum identitou |
| `u_cell` | fyzicky určené future-directed unit timelike pole, nie voľba súradníc |
| congruence/`dmu_cell` | regular parent worldtube alebo congruence a invariantná lokálne konečná proper measure |
| crossing | explicitne dosiahnuteľná absolútne spojitá pre-event cesta s `P_rec/W_*>0` pri prvom crossingu |
| `R_reset^Z` | lokálna fyzická daughter/event mapa s nulovým novým work creditom; residual interface energy v oddelenom post-event ledgeri |
| source-off | bez vstupu a dostupného rezervoára nevzniká rast `W_rec` ani crossing |
| nekruhovosť | bez `R_div`, produktov, expansion outputu, `S8/H0/k` alebo biologického targetu vo vstupe |

Carrier, výkon a threshold musia navyše patriť tej istej on-shell causal
pre-event trajektórii a pointwise spĺňať

```text
D_u W[Z_rec] = P_rec >= 0.
```

Ručne nakreslená interpolácia medzi dvoma riešeniami nestačí. Framework musí
mať kauzálny/well-posed initial-value význam v použitom režime a nesmie mať
relevantnú ghost, gradient, negative-reservoir alebo inú nestabilitu, ktorá
znehodnotí passport ešte pred crossingom. `W`, `W_*`, `u_cell` a
`dmu_cell` musia mať kovariantný alebo source-native gauge-invariant význam.
Parent worldtube/count musí byť source-native a once-only. Reset musí byť
dynamický fyzický následok EOM/event mapy, nie numerical reinitialization,
nový názov pre ten istý stav alebo účtovné odčítanie konštanty. Residual
interface energy musí mať exact lokálny tok v tom istom energy-momentum
ledgeri.

Ku každému poľu sa uvedie exact rovnica/sekcia primárneho zdroja a oddelí sa:

```text
SOURCE_EXACT        — priamo v primárnom modeli,
DERIVED_SAME_MODEL  — algebraicky odvodené bez novej fyziky,
E3_MAPPING          — iba ne-kreatívne premenovanie existujúceho fyzického
                      objektu na Y_div po SOURCE_EXACT/DERIVED_SAME_MODEL,
MISSING             — zdroj pole nedodáva.
```

Každé W10 pole musí mať fyzický preobraz `SOURCE_EXACT` alebo
`DERIVED_SAME_MODEL`. `E3_MAPPING` nesmie vytvoriť nový stav, dynamiku,
congruence, measure, reset ani conservation kanál. `E3_MAPPING` bez fyzického
preobrazu sa zapisuje ako `MISSING`. Jediné `MISSING` znamená, že kandidát nie
je kompletný W10.

## 5. Zakázané skladanie passportu

Nie je dovolené:

- vziať `W_*` z critical-bubble modelu, dissipáciu z fracture modelu a
  `u_cell` z nesúvisiacej všeobecnej relativity;
- definovať `W_rec` iba integrálom, ak ho nenesie fyzický `Z_rec`;
- zameniť barrier/free energy za reálne dodanú work energiu bez zdroja;
- použiť quantum/thermal jump ako regular v1 crossing bez explicitnej
  absolútne spojitej pre-event trajektórie;
- nastaviť dcérsky work credit na nulu iba účtovným premenovaním, ak fyzický
  daughter stav stále dáva `W[Z_rec]>0`;
- odvodiť energy scale z `delta`, `C=28`, Planckovej dimenzie alebo fitu;
- použiť S8, H0, division rate, biologické delenie alebo post-event produkty
  na výber či ranking kandidáta.

## 6. Predregistrovaný screen S0–S13

| ID | Kontrola | PASS podmienka |
|---|---|---|
| `S0` | primary-source provenance | anchor je pôvodný research zdroj s dostupnými rovnicami |
| `S1` | one-model closure | anchor/companions majú exact action/EOM/state/`T^{mu nu}`/convention/dimension/boundary/regime parity; žiadny nový sektor ani splice |
| `S2` | carrier/state | fyzický `Z_rec` a `W[Z_rec]` bez hidden history clocku |
| `S3` | coupled causal power | na tej istej on-shell pre-event ceste platí pointwise `D_uW[Z_rec]=P_rec>=0` a zdroj/rezervoár sú odvodené |
| `S4` | threshold | finite positive cycle-frozen `W_*` z rovnakej fyziky |
| `S5` | conservation | disjunktný lokálny energy-momentum ledger, residual-interface tok a source-off identita |
| `S6` | cell flow | source-native future unit `u_cell`, regular once-only parent worldtube/congruence a finite invariant `dmu_cell` |
| `S7` | regular reachability | dynamicky dosiahnuteľná on-shell absolútne spojitá jednoduchá upward cesta; nie ručná interpolácia alebo jump |
| `S8` | reset | fyzická dynamická `R_reset^Z`, zero daughter credit a oddelená residual energy; nie rename/reinitialization |
| `S9` | covariance/stability/units | kovariancia alebo source-native gauge invariance, well-posed causal režim, bez relevantnej ghost/gradient/negative-reservoir instability; jednotky, pozitivita a orientation konzistentné |
| `S10` | noncircularity | žiadny zakázaný downstream alebo observačný vstup |
| `S11` | Y_div mapping | všetky source objekty sú explicitne v jednom provisional `Y_div` stave |
| `S12` | null/source-off | bez vstupu/rezervoára nevznikne event |
| `S13` | scope | bez Pythonu, fitu, steam/completion a zmeny skóre/hĺbky |

## 7. Zmrazené rozhodovacie vetvy

```text
Ak prvý eligible kandidát v zmrazenom poradí prejde S0-S13 a každé pole má
SOURCE_EXACT alebo DERIVED_SAME_MODEL fyzický preobraz bez MISSING:
  CANDIDATE_COMPLETE_W10_INTERFACE_ACTION_PASSPORT_FOUND
  / PENDING_INDEPENDENT_PHYSICS_AUDIT;
  spotrebuje 1 physical-witness attempt až po prijatí hlavného posudku.

Ak model je koherentný reference interface model, ale chýba fyzická
Y_div/cell/reset mapa:
  PASS_REFERENCE_INTERFACE_MODEL_ONLY
  / REVIEW_NOT_A_COMPLETE_W10_WITNESS;
  physical-witness attempt sa nespotrebuje.

Ak bol frozen protokol úplne vykonaný a po vyhodnotení všetkých povolených
eligible kandidátov neprešiel žiadny kandidát všetkými S0-S13:
  REVIEW_NO_COMPLETE_W10_PRIMARY_SOURCE_WITNESS_FOUND_IN_FROZEN_SEARCH;
  nie STOP C01, nie globálny literature no-go ani dôkaz prázdnosti A_RW1.

Ak provider zlyhá, query payload nie je úplný alebo skorší eligible zdroj
ostane inaccessible bez verifikovateľnej canonical alternatívy:
  REVIEW_SEARCH_COVERAGE_INCOMPLETE_NO_PHYSICAL_INFERENCE;
  nesmie sa interpretovať ako nenájdenie witnessu.

Ak konkrétny kandidát zamieňa barrier/free energy za reálne dodanú
kumulatívnu work energiu bez causal source/reservoir ledgera, potrebuje jump
crossing, double credit alebo fitted threshold:
  PRECHECK_EXCLUDED_SCOPE iba pre tento kandidát.

Každý úplne vykonaný a hlavným posudkom prijatý source-search výsledok zvýši
P4 work-atom count z `2` na `3`, aj keď nájde iba reference model alebo nič
úplné. Physical-witness attempt sa zvýši z `0` na `1` iba pri prijatom
explicitnom complete-W10 kandidátovi; inaccessible, spliced, reference-only
a incomplete kandidáti ostávajú v immutable candidate ledgeri bez
spotrebovania witness attemptu.

Nikdy z tohto atómu:
  pravda C01, closure P4/MF1/D03/P5.3, zmena K4=60/100 alebo P5=3.5/6,
  RUN_AUTHORIZED=true, Python, steam/completion alebo S8/H0 fit.
```

## 8. Výstup a auditný handoff

Po freeze sa vykoná jeden bounded internet/source screen bez Pythonu a
výsledok sa zapíše do jediného dokumentu 262. Citácie budú pri exact claims;
copyrightovo sa použijú parafrázy a iba krátke nevyhnutné citáty.

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-W10-SOURCE-PREREG-DELTA-REAUDIT-20260727-157
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_w10_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root tasks155+156A
STATIC_AUDITOR_TASK_ID: UNASSIGNED_STATIC_AUDITOR_NO_PYTHON
INTERNAL_AUDITOR_TASK_ID: /root/c01_w10_prereg_audit task157
PACKAGE_CURATOR_TASK_ID: UNASSIGNED_PACKAGE_CURATOR
EXTERNAL_AUDITOR_TASK_ID: UNASSIGNED_EXTERNAL_AUDITOR
SEPARATION_OF_DUTIES_CHECK: PASS; artifact author /root tasks155+156A != internal auditor /root/c01_w10_prereg_audit task157; static auditor comparison not applicable because no script/Python; package curator and external auditor are distinct unassigned role identities and no package phase is active
ROUTE: A1_K1_A2_K4_P5.3_B6b-2.10_H_RDIV_C01_RW1_v1
CURRENT_PHASE: CORRECTED_DRAFT_PREREGISTRATION_BEFORE_ANY_NEW_SOURCE_SEARCH
ALLOWED_NEXT_ACTION: same independent auditor verifies the exact bounded correction delta; after PASS and out-of-file SHA freeze, main orchestrator performs the exact bounded search once
ALLOWED_READS: mandatory bootstrap; frozen document259; accepted document260; this document261; event ledger through task155; role config and manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: internet/source search by auditor; edit; select a physical truth; infer missing passport field; Python; downstream physics; score/depth/run change; package work
IMMUTABLE_INPUT_PATHS_AND_SHA256: document259=9766E5223C7AB95B8D3D3B9914BF8B02034F160F84EF0E47BEE8E4C14EB453E2; document260=91C25DD777FB9A10B1157F3CF729408B55A3CA264A03E29AA9C2F9E6747CA774; prior_document261=E9406A9A94B60408CA0E5744B5AB5E1C5AACD0FBF5682B8EACA68BFEE05D9562; corrected_document261=RECORDED_OUTSIDE_THIS_FILE; current_plan=359022D0D50ADA0CAEE2815F2DAAFA40E033CAF912DF4EF09CC79B0E5381E2FD; K4_plan=515A35E454C6B82981B62E15C7F06E72AC448C82A8F830247FD34F6166C3CABC; P5_plan=160FDCF33F3C5FF0D1DE2B0137D5EE26052B283D6EE3B33EBEBA37C331E23FCC; ledger_through_task155=8E34483DA2276270B6D85FCB6227F0CB9C3C8AEB77226A9F18287A32CFF14D35
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation; after freeze one result document262
LIVE_FILE_BUDGET: 1 prereg + 1 append-only ledger; later 1 result; central plans 0; package copies 0
DONE_WHEN: exact correction delta resolves F1-F7; provider/query/result order, eligibility, dedup, caps, companion parity, exhaustion, coverage blocker, physical-precursor rule, on-shell identity, covariance/stability, source-native cell measure, dynamical reset, attempt/work accounting and nonclaims are fail-closed
NEXT_ROLE: main_orchestrator
```
