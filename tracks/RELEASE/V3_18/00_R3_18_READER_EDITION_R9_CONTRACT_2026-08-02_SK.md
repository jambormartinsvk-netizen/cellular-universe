# R3.18-READER — zmluva čitateľského vydania v3.18 (R9)

**Autorovo rozhodnutie:** Martin Jambor, 2. august 2026  
**Rodič:** prijatý R8 standalone contract SHA-256
`493EE924C9344EF145CFA14AD2F8178A0FCA98D91402EC6035F872A82DE5A2B0`  
**Trieda zmeny:** `P0_READER_ARCHITECTURE_AND_EDITORIAL_REWRITE`  
**Vedecký cutoff:** 1. august 2026  
**Stav:** contract draft; pred zápisom release korpusu vyžaduje nezávislý
physics, math/parity a documentation/release audit  
**RUN_AUTHORIZED:** `false`

## 1. Dôvod nástupcu

R8 dokázal zostaviť samostatný a vedecky opatrný korpus, ale jeho hlavný
text zostal príliš technický, heslovitý a rozdelený medzi úvod, hlavný
dokument a scope. Chýbal slovenský README a názvy nevytvárali jednoznačné
poradie čítania. Martin preto zrušil stav `READY_FOR_MARTIN_FILE_REVIEW` a
vyžiadal čitateľské vydanie, ktoré:

1. nevyžaduje čítanie nijakej staršej verzie;
2. vysvetľuje fyzikálny problém, mechanizmus, rovnice, dôkazy, predikcie,
   otázky a limity v súvislom odbornom texte;
3. nepoužíva rozprávkový ani prozaický štýl, ale každý technický pojem pri
   prvom použití vysvetlí;
4. čísluje všetky jazykové dokumenty podľa poradia čítania;
5. uchová exact staršie vydania v `HISTORY/` bez ich miešania s current
   tvrdeniami.

R9 nemení fundament, rovnice, čísla, statusy P01–P11, Q1–Q34, koľaje,
skóre, hĺbku ani obsahový cutoff. Ak by redakčný prepis potreboval takúto
zmenu, musí sa zastaviť a otvoriť vedecký decision gate.

## 2. Čitateľská architektúra

`README.md` zostáva nečíslovanou technickou výnimkou, pretože je štandardným
vstupom GitHubu. Jazykové dokumenty majú presné poradie:

```text
theory/SK/00_README_SK.md
theory/SK/01_Bunkovy_Vesmir_v3.18_SK.md
theory/SK/02_Prediction_Status_Table_v3.18_SK.csv
theory/SK/03_Methodology_and_Question_Register_v3.18_SK.md

theory/EN/00_README_EN.md
theory/EN/01_The_Cellular_Universe_v3.18_EN.md
theory/EN/02_Prediction_Status_Table_v3.18_EN.csv
theory/EN/03_Methodology_and_Question_Register_v3.18_EN.md
```

Súbor `01` v každom jazyku nahrádza staré samostatné `01`, `04` a `06`.
Musí byť úplným odborným výkladom; `02` je machine-readable ledger a `03`
je auditná metodika s úplným Q1–Q34 registrom.

### 2.1 Zmrazené R8 zdroje a old-to-new mapa

| R8 zdroj | SHA-256 | R9 cieľ |
|---|---|---|
| `theory/SK/01_Introduction_and_Philosophy_v3.18_SK.md` | `9532DA3BEC2E3691699762FEC0A4F5A9BC798D6D2BE6DED89E6853B9B69970D1` | `theory/SK/01_Bunkovy_Vesmir_v3.18_SK.md` |
| `theory/SK/04_Main_Document_Theory_Equations_Values_v3.18_SK.md` | `0B9E83178CF4194B2938B64258056448F45A671A4DAC11DC3E032A41654929EE` | `theory/SK/01_Bunkovy_Vesmir_v3.18_SK.md` |
| `theory/SK/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_SK.md` | `BF4C15E674F0186BB29515DA184A210063CBAA5570C158E4073EEB7CB71977C9` | `theory/SK/01_Bunkovy_Vesmir_v3.18_SK.md` |
| `theory/SK/03b_Prediction_Status_Table_v3.18_SK.csv` | `AD0C8FBABF2042D58592D58CB7305CD7856AA0B10CCBA26803038DF207810093` | `theory/SK/02_Prediction_Status_Table_v3.18_SK.csv` |
| `theory/SK/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_SK.md` | `B330A221F118FBA6F539B419D12330A5203F717C32F5F945F46E4751CD349DF7` | `theory/SK/03_Methodology_and_Question_Register_v3.18_SK.md` |
| `theory/EN/01b_Introduction_and_Philosophy_v3.18_EN.md` | `4884CBC896893CCF5EFF86F55C61E398308B164292BF70D8AE56D8EC4F40AA0D` | `theory/EN/01_The_Cellular_Universe_v3.18_EN.md` |
| `theory/EN/04b_Main_Document_Theory_Equations_Values_v3.18_EN.md` | `B2CF3F51FE72E216244D49A738F00C7B8CFFAF36C1D1A5A6AE5F1356817FDB27` | `theory/EN/01_The_Cellular_Universe_v3.18_EN.md` |
| `theory/EN/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_EN.md` | `0A3F4F9E6FED0C2976322BEFD53747F1672E525F859A13F610D8D97BE54769C4` | `theory/EN/01_The_Cellular_Universe_v3.18_EN.md` |
| `theory/EN/03_Prediction_Status_Table_v3.18_EN.csv` | `21C9534F32D2721A7BFA0BAF56E55CE26B5D71E3BD7E2DC42ECA55775A018583` | `theory/EN/02_Prediction_Status_Table_v3.18_EN.csv` |
| `theory/EN/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_EN.md` | `9B6C3CB217306B1EF76EE9D5026D6D6EE4B443119A68CA2997B541CFF843BA26` | `theory/EN/03_Methodology_and_Question_Register_v3.18_EN.md` |

Navigačný successor `theory/SK/00_README_SK.md` je nový. Existujúci
`theory/EN/00_README_EN.md` sa aktualizuje na mieste zo zdroja SHA-256
`665A06ACF1A9F362A014EC335AF723A216E33DFEC150E5B665B80AD5B3C4D0B1`.
Každý R9 successor musí mať content-coverage ledger dokazujúci, že žiadna
rovnica, P/Q ID, status ani nonclaim zo svojich zmrazených rodičov nezmizli.

## 3. Povinná kostra hlavného dokumentu `01`

Text musí tvoriť jeden kauzálny oblúk:

1. aký fyzikálny problém teória rieši a čo presne tvrdí;
2. pracovná ontológia a preklad metafor na fyzikálne veličiny;
3. navrhovaná postupnosť bunka–palivo–prestavba–produkty;
4. presne odvodené, podmienené a otvorené časti geometrie siete;
5. homogénny kozmologický ledger a jeho zákony zachovania;
6. prečo je úplná lineárna A2 stanica nevyhnutná;
7. čo model navrhuje pre expanziu, tmavú hmotu, raný vesmír, poruchy,
   Lorentzovu limitu, gravitáciu, meranie a šíp času;
8. tabuľka P01–P11 s current stavom a ľudským vysvetlením;
9. presný status podmienenej H0/S8 diagnostiky;
10. živé a mŕtve fyzikálne koľaje vrátane dôvodu, prečo scoped STOP nie je
    smrť celej teórie;
11. čo by teóriu podporilo, čo by zabilo presný scope a čo ešte nemožno
    testovať;
12. otvorené otázky, najbližší výskumný krok a úplný zoznam nonclaims.

Každá rovnica má mať pred sebou otázku alebo fyzikálny dôvod, za sebou
význam symbolov, status a hranicu použitia. Stavové kódy smú byť v texte,
ale nesmú nahrádzať vetné vysvetlenie.

## 4. Zákaz straty alebo nafúknutia tvrdenia

Prepis musí zachovať najmenej tieto R8 invarianty:

- bunková ontológia je hypotéza, nie experimentálne potvrdenie;
- obyčajná hmota, popol a para nemajú odvodené úplné poradie ani branching;
- A1-K1 prešiel iba backgroundovou bránou;
- A2-K4 zostáva `LIVE_ACTIVE / 60/100`; žiadna A2 koľaj nie je úplná;
- scoped STOPy A2-K1/K2/K3/K5/K6 a živé zálohy K7/K8/K9/K11/K12 sa
  nezmenia;
- realizovaný Fourierov mód nesmie určovať FLRW background;
- `A_f=7809.270101963506` je iba conditional frozen-A1 bookkeeping;
- presná párnosť platí iba pre auditovaný skalárny cosine-Laplacian;
- P01–P11 a Q1–Q34 zachovajú rovnaké ID, čísla, statusy a nonclaims;
- tri H0/S8 hodnoty sú diskrétna legacy-anchor citlivosť, nie fit, interval
  ani tvrdá predikcia;
- presný `n_s-w` vzťah ostáva `WITHDRAWN`;
- v3.18 netvrdí náhradu GR, QFT, Standard Modelu ani LambdaCDM v ich
  overenom rozsahu.

## 5. História

Git strom bude obsahovať:

```text
HISTORY/00_README.md
HISTORY/v3.17/<exact 16-file Zenodo 21297228 v2.0 snapshot>
```

Všetkých 16 historických súborov sa exportuje výhradne zo zmrazeného
archívneho commitu
`e9e3579afdffc3c719f0beabb4ec33929cfb4d62` s tree
`6e317b76e17c08febb800fcc80742c77c8801aeb`, nie z pracovnej kópie
`D:/Teoria-v3.17-release`. Pred exportom aj po ňom sa overí `16/16` zhoda s
existujúcou Zenodo MD5 mapou v R8 contracte §2.1. Najmä historický skript 09
sa nesmie prevziať z lokálneho post-release variantu.

Source-to-destination mapping je mechanické a úplné: každá z presných 16
ciest v archívnom commite sa mapuje na
`HISTORY/v3.17/<pôvodná_relativna_cesta>`. Iná transformácia názvu alebo
obsahu je zakázaná.

`HISTORY/00_README.md` uvedie verziu, Zenodo DOI, archívny commit, všetkých
16 MD5 a upozornenie, že ide o historické tvrdenia, nie current stav v3.18.
História je Git provenance vrstva, je vylúčená z current Zenodo payloadu a
nie je potrebná na pochopenie current vydania.

### 5.1 Exact finálny current Zenodo payload — 13 ciest

```text
README.md
theory/SK/00_README_SK.md
theory/SK/01_Bunkovy_Vesmir_v3.18_SK.md
theory/SK/02_Prediction_Status_Table_v3.18_SK.csv
theory/SK/03_Methodology_and_Question_Register_v3.18_SK.md
theory/EN/00_README_EN.md
theory/EN/01_The_Cellular_Universe_v3.18_EN.md
theory/EN/02_Prediction_Status_Table_v3.18_EN.csv
theory/EN/03_Methodology_and_Question_Register_v3.18_EN.md
CHANGELOG_v3.18.md
zenodo_description_v3.18.html
RELEASE_STAGING_MANIFEST_v3.18.tsv
MANIFEST_v3.18.sha256
```

`CURRENT_ZENODO_PAYLOAD_COUNT=13`. SHA manifest obsahuje presne 12 non-self
riadkov; staging manifest 13 jedinečných payload riadkov. História, licencia
a `.gitattributes` do Zenodo payloadu nevstupujú.

### 5.2 Exact Git strom — 32 ciest

Git strom obsahuje presne:

1. 13 current payload ciest z §5.1;
2. `.gitattributes` a `LICENSE`;
3. `HISTORY/00_README.md`;
4. týchto 16 exact archívnych ciest:

```text
HISTORY/v3.17/scripts/06_script_Q14_light_cone_front_sharpening.py
HISTORY/v3.17/scripts/07_script_Q12_dispersion_Lorentz_test.py
HISTORY/v3.17/scripts/08_script_Q7_sound_horizon_H0.py
HISTORY/v3.17/scripts/09_script_K3_cosmology_pipeline.py
HISTORY/v3.17/scripts/10_script_Q10_Vlinks_dowry_rule.py
HISTORY/v3.17/theory/EN/00_README_EN.md
HISTORY/v3.17/theory/EN/01b_Introduction_and_Philosophy_EN.md
HISTORY/v3.17/theory/EN/02_Predictions_Table_v3.17_EN.pdf
HISTORY/v3.17/theory/EN/03_Predictions_Table_v3.17_EN.csv
HISTORY/v3.17/theory/EN/04b_Main_Document_Theory_Equations_Values_v3.17_EN.md
HISTORY/v3.17/theory/EN/05b_Methodology_Rules_and_Question_Register_EN.md
HISTORY/v3.17/theory/SK/01_Introduction_and_Philosophy_SK.md
HISTORY/v3.17/theory/SK/02b_Predictions_Table_v3.17_SK.pdf
HISTORY/v3.17/theory/SK/03b_Predictions_Table_v3.17_SK.csv
HISTORY/v3.17/theory/SK/04_Main_Document_Theory_Equations_Values_v3.17_SK.md
HISTORY/v3.17/theory/SK/05_Methodology_Rules_and_Question_Register_SK.md
```

`FINAL_GIT_TREE_COUNT=32`. `.gitattributes` obsahuje `-text` pre všetkých 13
current payloadov a všetkých 16 byte-exact historických súborov, spolu
`29/29`; `LICENSE` a `HISTORY/00_README.md` ostávajú normálne textové Git
súbory.

### 5.3 Exact superseded R8 deletion set — 10 ciest

Po vytvorení a audite všetkých successorov sa odstránia iba:

```text
theory/SK/01_Introduction_and_Philosophy_v3.18_SK.md
theory/SK/03b_Prediction_Status_Table_v3.18_SK.csv
theory/SK/04_Main_Document_Theory_Equations_Values_v3.18_SK.md
theory/SK/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_SK.md
theory/SK/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_SK.md
theory/EN/01b_Introduction_and_Philosophy_v3.18_EN.md
theory/EN/03_Prediction_Status_Table_v3.18_EN.csv
theory/EN/04b_Main_Document_Theory_Equations_Values_v3.18_EN.md
theory/EN/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_EN.md
theory/EN/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_EN.md
```

`theory/EN/00_README_EN.md` a päť root control ciest sa aktualizujú na
mieste. Mazanie pred successor auditom je zakázané.

## 6. Release a auditné brány

Poradie práce je:

```text
R9 CONTRACT AUDIT
-> SK 00/01/02/03 DRAFT
-> nezávislý SK reader + physics + math audit
-> EN faithful translation
-> nezávislý SK/EN parity audit
-> HISTORY exact-byte population and audit
-> root navigation/changelog/Zenodo/manifests/.gitattributes regeneration
-> exact tree/hash/link/preseal audit
-> MARTIN FILE REVIEW
-> až potom osobitné povolenie commitu
```

Zakázané je: Python scientific run, zmena cutoffu, nový fit, tiché
obnovenie historickej predikcie, staging, commit, tag, push, merge, GitHub
release alebo Zenodo upload/publish bez neskoršieho výslovného súhlasu
Martina Jambora.

## 7. Handoff kapsul

```text
TASK_ID: V318-R9-READER-EDITION-20260802
ROUTE: RELEASE/v3.18/R3.18-READER
CURRENT_PHASE: R9_CONTRACT_P0_CORRECTED_REAUDIT_PENDING
ALLOWED_NEXT_ACTION: independent read-only P0 delta audit; after acceptance create exact SK 00/01/02/03 corpus
ALLOWED_READS: R8 accepted release corpus, R9 contract, v3.17 exact archive, current route plans
ALLOWED_WRITES: none for auditors; /root only after contract acceptance
FORBIDDEN_ACTIONS: Python, scientific result, status/score/depth change, staging, commit, tag, push, publish
RUN_AUTHORIZED: false
ERROR_BATCH_INDEX: reader-edition batch1
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 0
FINDING_ID: P0-R9-HISTORY-SOURCE-001 + P0-R9-FINAL-SET-001
FINDING_CLASS: P0_PACKAGE_PROCESS_ONLY / corrected in same contract
TRACK_IDENTITY_GATE: SAME_TRACK_REQUIRED
DONE_WHEN: one coherent numbered SK/EN reader edition preserves all R8 scientific meanings, exact v3.17 history is present, final manifests pass, and Martin approves every changed/deleted path
NEXT_ROLE: documentation_release_steward + physics_track_auditor + math_script_auditor, read-only
```
