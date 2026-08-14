# R3.18-CONSOLIDATED — release contract v3.18

**Stav:** `CONTRACT_R8_STANDALONE_COMPLETENESS_AUTHOR_INPUT_RECORDED / PRIOR_14_FILE_DELTA_DRAFT_SUPERSEDED`  
**Dátum:** 2026-08-02  
**Autor:** hlavný orchestrátor; finálne fyzikálne vstupy a vydanie schvaľuje Martin Jambor  
**Release class:** `R3.18-CONSOLIDATED / COMPLETE_SELF_CONTAINED_SNAPSHOT`  
**Nie je:** `R3.18-PHYS`, `R3.18-PREDICTION` ani v4  
**RUN_AUTHORIZED:** `false`; tento contract nepovoľuje Python, Git staging, tag, push ani Zenodo publikovanie

## 1. Cieľ a hotový stav

Cieľom je vydať nemenného nástupcu v3.17, ktorý:

1. je úplným samostatne čitateľným snapshotom teórie: čitateľ nepotrebuje
   v3.17 na pochopenie ontológie, filozofie, definícií, mechanizmov, rovníc,
   stavov, otvorených otázok ani nonclaims;
2. opraví rozsah starších tvrdení bez tichého prepisovania v3.17;
3. zverejní aktuálny stav predikcií ako statusy, nie ako neoverené tvrdé čísla;
4. uvedie tri externe T2 potvrdené body `H0/S8` iba ako podmienenú
   legacy-anchor citlivosť;
5. zlúči pracovnú metodiku do jedného SK/EN páru bez ďalšieho množenia
   súborov `05*`;
6. dodá changelog, staging manifest, SHA-256 manifest a presný Git/Zenodo
   audit trail.

Changelog je voliteľná skratka pre čitateľa v3.17, nie nositeľ definícií
potrebných na čítanie v3.18. Odkaz na starú verziu smie dokazovať históriu,
ale nesmie nahrádzať vysvetlenie current obsahu. Detailné raw, skripty a
auditné checkpointy môžu zostať v hashovo viazanom Git archíve; release
text však musí sám uviesť vedecký význam, rovnice, vstupy, výsledok a
nonclaims každého citovaného míľnika.

Contract je dokončený až po nezávislom read-only review. Až potom môže
hlavný orchestrátor samostatne povoliť tvorbu release súborov.

## 2. Publikovaný baseline a nemenné vstupy

### 2.1 Autoritatívny historický baseline

Historický baseline nie je aktuálny Git `main`, ale publikovaný snapshot:

```text
ZENODO_RECORD_ID=21297228
DOI=10.5281/zenodo.21297228
VERSION=2.0
PUBLICATION_DATE=2026-07-10
API=https://zenodo.org/api/records/21297228
FILE_COUNT=16
```

Oficiálne Zenodo API 2026-08-01 vrátilo túto exact MD5 mapu:

| Zenodo súbor | MD5 |
|---|---|
| `00_README_EN.md` | `7bfc3e84c1653c03e92ce752ae1b86a0` |
| `01_Introduction_and_Philosophy_SK.md` | `8667297005bdd0f87df36816c38cfe7f` |
| `01b_Introduction_and_Philosophy_EN.md` | `fb97e07c7c712dc96f9ec47e1b54400c` |
| `02b_Predictions_Table_v3.17_SK.pdf` | `9c229bc1421850b6852b43ca5f5e0f0b` |
| `02_Predictions_Table_v3.17_EN.pdf` | `6dd7d46611eaa8f6e0a9129f84812882` |
| `03b_Predictions_Table_v3.17_SK.csv` | `0c489c9aac33ecd0c6b5b6bc3ba14858` |
| `03_Predictions_Table_v3.17_EN.csv` | `754f4e9e6a40a16304c69019f0bb73a5` |
| `04_Main_Document_Theory_Equations_Values_v3.17_SK.md` | `8b942abc62b6333b789a3c6aac66309d` |
| `04b_Main_Document_Theory_Equations_Values_v3.17_EN.md` | `ac45868b41b4ffb9ea096677e6b78971` |
| `05_Methodology_Rules_and_Question_Register_SK.md` | `4f60e2e27961c64e6b87c1281b7be42d` |
| `05b_Methodology_Rules_and_Question_Register_EN.md` | `9a896b77fc991d8b2e72d7335f6aeb3f` |
| `06_script_Q14_light_cone_front_sharpening.py` | `8d3f0e1767b270184b611c3dc40f8f1d` |
| `07_script_Q12_dispersion_Lorentz_test.py` | `7579c7bcfddd051dd144f49cbf8b0a4d` |
| `08_script_Q7_sound_horizon_H0.py` | `f5b43100fec3b6c3aaf2fe0ae86e41ec` |
| `09_script_K3_cosmology_pipeline.py` | `2e2c6b32c8d39a5a6dc399018424d039` |
| `10_script_Q10_Vlinks_dowry_rule.py` | `ddd8d9f48fd4136bd333515d7f3f83d7` |

Read-only kontrola lokálneho workspace dala `15/16` exact zhôd. Jediná
nezhoda je živý `scripts/09_script_K3_cosmology_pipeline.py`, ktorý je
pracovný post-release delta a nesmie byť zdrojom historického importu.

Čistý chránený worktree `D:/Teoria-main` je:

```text
REMOTE=https://github.com/jambormartinsvk-netizen/cellular-universe.git
BRANCH=main
HEAD=77828f767ce2ecdbf7e4535e91926f7cbc1b5a50
TREE=5e8a579e79b6c21c697813671596fc2dddb9723f
STATUS=CLEAN
```

Tento Git commit je iba technický štart release vetvy, nie publikovaný
baseline: jeho SK/EN main dokumenty, EN README a skript 09 sa nezhodujú so
Zenodo MD5. Pred tvorbou v3.18 musí vzniknúť samostatný archival-sync commit
podľa §8, ktorý dá `16/16` zhodu s publikovaným snapshotom.

### 2.2 Pracovné vstupy pre v3.18

| Vstup | SHA-256 | Úloha |
|---|---|---|
| `theory/README.md` | `A628994F861984DC8924FE826C3F7210BF695866720643A950322EA6324D9486` | pracovný repository-index delta; nie publikovaný baseline |
| `00_README_EN.md` | `9E1ACD7726F633AD13828FA03CF4008BFB359299E3F1A6E4BB5378A796E23A6B` | exact Zenodo EN README mirror |
| `theory/SK/04_Main_Document_Theory_Equations_Values_v3.17_SK.md` | `01B8DD903C3BB97B30E29E2C1E2E2B280D3968EDD0679C610E84A78CC55CBF43` | exact Zenodo v3.17 SK mirror; iba source pre nový v3.18 successor |
| `theory/EN/04b_Main_Document_Theory_Equations_Values_v3.17_EN.md` | `9F0C10A4CA3DB85CF324050648B69D22F87FF64C083284C89ED436417FF0ADD9` | exact Zenodo v3.17 EN mirror; iba source pre nový v3.18 successor |
| `theory/SK/03b_Predictions_Table_v3.17_SK.csv` | `4B146239F39C4B9354E44F76CB9F5AF615897748C84501D3F6AAF241B0D0D55B` | exact Zenodo historické SK predikcie |
| `theory/EN/03_Predictions_Table_v3.17_EN.csv` | `FE7D987CA65CB640700294F5824A5CB4ED568CDBBF6ABAA48B7B1FE82304CB87` | exact Zenodo historické EN predikcie |
| `tracks/RELEASE/V3_18/PT1_H0/ARTIFACTS/H0_S8_C2_C3_RESULT_AND_INTERNAL_AUDIT_2026-08-01_SK.md` | `E2DF985FA198F4DBC3AD05C5EA2A0E8607161E3BDE26A4C3754C3CC383E229DE` | prijaté výsledky a nonclaims |
| `tracks/METHODOLOGY/00_RELEASE_PROMOTION_LEDGER.md` | `B0D57C066CFB1D12C5E043C3126644D6D7702D35D5FDBECCCC86F830483F4EC5` | autoritatívny promotion stav vrátane FS-GATE-02/02a |
| `Audit/V3_18_RELEASE_READINESS_AUDIT_2026-07-28_SK.md` | `6AF0B2FD0D289CD2160DE858B2CA33AB690DE78D52A4EA68446BF96544660F79` | release-readiness obmedzenia |
| `Questions/ZENODO_VERSION_PUBLICATION_CRITERIA.md` | `908809B97C0C37548541A913C90392D644264051E67CFA2FEFF7598A685B005B` | verzovanie a publication gates |
| `Questions/ZENODO_RELEASE_CHECKLIST_v3.18.md` | `CBD16E59B6CCAD5B5E2B8080131C764D5102349EF588EA9C2F0EB29EC9425B44` | hlavný checklist |
| `Questions/ZENODO_RELEASE_CHECKLIST_v3.18_ADDENDUM_PREDICTION_TABLE.md` | `54C4A94C3F2DE1FA28A492B1A687056129D3DB754A878BB86FC2B1BBCDE5F6EF` | prediction-table checklist |
| `D:/Teoria-v3.18-release/theory/SK/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_SK.md` | `21F2B70EC7A9F4A5C9B737869CE71CBC5E4985A9C70EA59692CEB840F80BF0E3` | prijatý SK release-meaning cutoff zdroj; pri standalone prepise sa nesmie zmeniť jeho stavový obsah |
| `D:/Teoria-v3.18-release/theory/EN/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_EN.md` | `691C4C0991D4BB9041D47744BB39CFFB3AF7A8128DEB614C2355D8067D78A2F5` | prijatý významovo zhodný EN release-meaning cutoff zdroj |
| `tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md` | `02E0D3886180607423542F3CE107321FF8E80CE737DAEB23613B0DFA7D4774C7` | detailný SK mantinelový pas a AND/OR topológia smrti |
| `tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_EN.md` | `E52917CAFC5BA62A28FD0F0684F6783DF3595186E6F203674838727DB3A81344` | významovo zhodný EN mantinelový pas |
| `External_Audits/RESPONSES/EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE/SUB-20260801-047-R2-001/00_AUDITOR_AUDIT.md` | `F1735B8CB0036B1B8271EC8E2DF6281EAE0FB142A82791739D03C061DC09FE7E` | externé P0 closure |
| `scripts/results/k_mpc_005/RUN_KMPC_001_A1_AF_FROZEN_BACKGROUND.json` | `FADE4F37CE84958C35BFC23073CFA6AB92F18AAE188B5CCA6C77A280D2CD05FD` | immutable parameter-bookkeeping raw pre `A_f` |
| `Independent_Audits/K_MPC_0_05/06_AF_FROM_FROZEN_A1_RESULT_SK.md` | `24780282EBB24262E963C885ADBF757002392C9B4E5B0E62C555CB00BBB4CFC6` | projektová interpretácia PASS-P2a a nonclaims |
| `External_Audits/RESPONSES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/00_AUDITOR_AUDIT.md` | `F5A8D1AB9BF1E9306C7786D39037D0A09BFCA0DBD5732C142869F9920987A487` | externá T2 reprodukcia `A_f`, multi-k mapy a K7 limitu |
| `External_Audits/RESPONSES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/01_MAIN_ORCHESTRATOR_ASSESSMENT_2026-07-18.md` | `8E8B62F23B19530A4C6382AB2A5D99D8DE9349C09109268A04CC7A1B38985490` | prijatie T2 s presným claim reach |

Hash drift ktoréhokoľvek vstupu pred review znamená
`CONTRACT_INPUT_DRIFT_REVIEW`; release súbory sa nezačnú tvoriť.

### 2.3 Obsahový cutoff úplného snapshotu

```text
RELEASE_CONTENT_CUTOFF_DATE=2026-08-01
RELEASE_CONTENT_CUTOFF_CHECKPOINT=CP-RELEASE-V318-PT1-H0-S8-C2C3-20260801-001
POST_CUTOFF_ACTIVE_WORK=Q1R6/task532+ and descendants
POST_CUTOFF_RELEASE_STATUS=NOT_INCLUDED_UNTIL_OWN_SCIENTIFIC_AND_PARITY_CLOSURE
```

„Úplný“ znamená úplný samostatne čitateľný stav teórie k tomuto explicitnému
cutoffu. Neznamená automatické preberanie rozpracovaných alebo ešte
neauditovaných zmien zo živých `tracks/`. Post-cutoff práca sa nesmie použiť
na zmenu tvrdenia v3.18, kým nemá vlastný prijatý vedecký a SK/EN parity
closure; jej neprítomnosť v release nie je tichým vymazaním, ale deklarovanou
verzovacou hranicou.

## 3. Zmrazený 16-súborový release write set

Iný release súbor sa nesmie pridať bez revízie contractu a nového review.

### 3.1 Vedecký a metodický obsah — 10 súborov

1. `theory/SK/01_Introduction_and_Philosophy_v3.18_SK.md`
2. `theory/EN/01b_Introduction_and_Philosophy_v3.18_EN.md`
3. `theory/SK/04_Main_Document_Theory_Equations_Values_v3.18_SK.md`
4. `theory/EN/04b_Main_Document_Theory_Equations_Values_v3.18_EN.md`
5. `theory/SK/03b_Prediction_Status_Table_v3.18_SK.csv`
6. `theory/EN/03_Prediction_Status_Table_v3.18_EN.csv`
7. `theory/SK/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_SK.md`
8. `theory/EN/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_EN.md`
9. `theory/SK/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_SK.md`
10. `theory/EN/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_EN.md`

### 3.2 Navigácia, changelog a release control — 6 súborov

11. `README.md` — aktualizácia tracked repository indexu v novej release vetve
12. `theory/EN/00_README_EN.md` — aktualizácia tracked EN indexu v novej release vetve
13. `CHANGELOG_v3.18.md` — dvojjazyčný zápis `OLD -> NEW -> REASON -> EVIDENCE`
14. `zenodo_description_v3.18.html`
15. `RELEASE_STAGING_MANIFEST_v3.18.tsv`
16. `MANIFEST_v3.18.sha256`

### 3.3 Finálny current-only Git strom — 18 súborov

Po RC preflight a pred release commitom smie byť v aktuálnom strome vetvy
`codex/v3.18-release` iba týchto 18 tracked ciest:

1. `.gitattributes`
2. `LICENSE`
3. až 18. presných 16 release ciest z §3.1 a §3.2.

`FINAL_REPOSITORY_TREE_ALLOWLIST_COUNT=18`. Súbory v3.17 nebudú vo finálnom
current tree uložené vedľa v3.18. Ich nemenná verzia ostáva dosiahnuteľná v
Git histórii na prijatom archívnom commite
`e9e3579afdffc3c719f0beabb4ec33929cfb4d62` a na publikovanom Zenodo
snapshote `21297228`.

Aktuálny archívny baseline obsahuje 29 tracked ciest. Presne štyri existujúce
cesty sa zachovajú; dve z nich sa obsahovo aktualizujú ako v3.18 payload:

```text
CURRENT_ONLY_RETAIN_OR_UPDATE_ALLOWLIST_COUNT=4
.gitattributes
LICENSE
README.md
theory/EN/00_README_EN.md
```

Presne štrnásť ciest sa vytvorí nanovo:

```text
CURRENT_ONLY_CREATE_ALLOWLIST_COUNT=14
CHANGELOG_v3.18.md
MANIFEST_v3.18.sha256
RELEASE_STAGING_MANIFEST_v3.18.tsv
theory/EN/01b_Introduction_and_Philosophy_v3.18_EN.md
theory/EN/03_Prediction_Status_Table_v3.18_EN.csv
theory/EN/04b_Main_Document_Theory_Equations_Values_v3.18_EN.md
theory/EN/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_EN.md
theory/EN/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_EN.md
theory/SK/01_Introduction_and_Philosophy_v3.18_SK.md
theory/SK/03b_Prediction_Status_Table_v3.18_SK.csv
theory/SK/04_Main_Document_Theory_Equations_Values_v3.18_SK.md
theory/SK/05aa_CONSOLIDATED_METHODOLOGY_AND_QUESTION_REGISTER_v3.18_SK.md
theory/SK/06_RELEASE_SCOPE_AND_CLAIM_STATUS_v3.18_SK.md
zenodo_description_v3.18.html
```

Po existencii všetkých 14 successorov a úspešnom static preflight sa smie
odstrániť iba tento doslovný zoznam 25 ciest:

```text
CURRENT_ONLY_DELETION_ALLOWLIST_COUNT=25
scripts/06_script_Q14_light_cone_front_sharpening.py
scripts/07_script_Q12_dispersion_Lorentz_test.py
scripts/08_script_Q7_sound_horizon_H0.py
scripts/09_script_K3_cosmology_pipeline.py
scripts/10_script_Q10_Vlinks_dowry_rule.py
theory/EN/01b_Introduction_and_Philosophy_EN.md
theory/EN/02_Predictions_Table_v3.17_EN.pdf
theory/EN/03_Predictions_Table_v3.17_EN.csv
theory/EN/04b_Main_Document_Theory_Equations_Values_v3.17_EN.md
theory/EN/05b_Methodology_Rules_and_Question_Register_EN.md
theory/SK/01_Introduction_and_Philosophy_SK.md
theory/SK/02b_Predictions_Table_v3.17_SK.pdf
theory/SK/03b_Predictions_Table_v3.17_SK.csv
theory/SK/04_Main_Document_Theory_Equations_Values_v3.17_SK.md
theory/SK/05_Methodology_Rules_and_Question_Register_SK.md
theory/theory/EN/01b_Introduction_and_Philosophy_EN.md
theory/theory/EN/02_Predictions_Table_v3.17_EN.pdf
theory/theory/EN/03_Predictions_Table_v3.17_EN.csv
theory/theory/EN/04b_Main_Document_Theory_Equations_Values_v3.17_EN.md
theory/theory/EN/05b_Methodology_Rules_and_Question_Register_EN.md
theory/theory/SK/01_Introduction_and_Philosophy_SK.md
theory/theory/SK/02b_Predictions_Table_v3.17_SK.pdf
theory/theory/SK/03b_Predictions_Table_v3.17_SK.csv
theory/theory/SK/04_Main_Document_Theory_Equations_Values_v3.17_SK.md
theory/theory/SK/05_Methodology_Rules_and_Question_Register_SK.md
```

Presný strojovo kontrolovaný deletion allowlist sa pred odstránením porovná
s `git ls-files`. Ak počet nie je `25`, cesta leží mimo vyššie uvedených
troch skupín alebo chýba ktorýkoľvek successor z §3, stav je
`CURRENT_ONLY_TREE_PREFLIGHT_REVIEW` a nič sa neodstráni.

`.gitattributes` sa pri RC prepíše z historických 16 pravidiel na exact
pravidlá potrebné pre finálnych 16 payload ciest. `LICENSE` a
`.gitattributes` sú Git-only riadiace súbory a nevstupujú do 16-súborového
Zenodo payloadu.

Plánované počítadlá:

```text
PLANNED_RELEASE_PAYLOAD_FILES=16
PLANNED_SCIENTIFIC_AND_METHODOLOGY_FILES=10
PLANNED_NAVIGATION_AND_RELEASE_CONTROL_FILES=6
ARCHIVAL_SYNC_REPO_CONTROL_FILES=1 (.gitattributes; not Zenodo payload)
LIVE_CENTRAL_REGISTERS_UPDATED_DURING_DRAFT=0
MAX_CENTRAL_REGISTERS_AT_RC_CLOSURE=4
AUDIT_PACKAGE_COPIES_BEFORE_FROZEN_RC=0
```

Po každom skutočnom batchi sa vykážu reálne unikátne zmenené cesty; plánované
čísla sa nesmú prezentovať ako vykonané.

## 4. Historická nemennosť a archív

- Všetky v3.17 PDF, CSV, main dokumenty, metodické registre a publikované
  skripty zostávajú byte-identickou históriou na commite `e9e3579...` a v
  Zenodo 2.0; nemusia zostať v current-only v3.18 strome.
- Dve živé v3.17 main dokumenty sú exact Zenodo mirrors, hoci sa voči
  staršiemu Git `main` javia ako modified. Musia sa archiválne importovať,
  nie zahodiť ani označiť za post-publication edit.
- `theory/README.md` nie je súčasťou Zenodo 2.0 a nie je Git `HEAD` baseline;
  je iba pracovný delta kandidát. Do release vetvy sa nekopíruje ako
  historický súbor. Jeho užitočný obsah možno po review preniesť iba do
  nového tracked `README.md`.
- Živý zmenený skript 09 je pracovný delta kandidát a nevstupuje do
  historického importu; historická kópia sa berie z exact Zenodo content URL.
- Aktuálnych `114` pracovných súborov `05*` (`57 SK + 57 EN`) v
  `D:/Teoria` sa touto release operáciou nemení. Historické release súbory
  `05*` zostávajú v Git histórii; finálny current tree obsahuje iba nový
  konsolidovaný pár 05aa.
- `theory/05c_REGISTER_v3.18_SK_EN_MANIFEST.md` sa neprepisuje; viaže starý
  pár 05c.
- `zenodo_description_v2.html` sa neprepisuje.
- Žiadna odvolaná hodnota sa neprenesie ako current iba preto, že nový
  výpočet nie je hotový.
- Staršie obmedzené formulácie dostanú v changelogu konkrétny dôvod a
  evidence cestu.

## 5. Zmrazená 11-ID prediction-status schéma

Každý SK/EN riadok musí niesť rovnaké `prediction_id`, historické tvrdenie,
stav v3.18, povolené nové tvrdenie, evidence tag/cestu a explicitný nonclaim.

| ID | Koncept | Povinný stav v3.18 | Povolený obsah |
|---|---|---|---|
| `P01` | `N_eff / Delta N_eff` | `SCOPE_NARROWED / NOT_YET_AVAILABLE` | Bez odvodenej tvrdej hodnoty; pôvod zdroja ostáva otvorený. |
| `P02` | `n_s` | `RECALCULATION_OPEN` | Historická hodnota iba ako v3.17, nie current. |
| `P03` | `r` | `RECALCULATION_OPEN` | Historická horná hranica nie je v3.18 potvrdená. |
| `P04` | `H0` | `RECALCULATION_OPEN` | Tri body nižšie iba ako conditional legacy-anchor sensitivity. |
| `P05` | `S8` | `RECALCULATION_OPEN` | Tri body nižšie iba ako conditional simplified-growth sensitivity. |
| `P06` | `w0, wa` | `SCOPE_NARROWED` | Jeden spoločný riadok; bez tichého rozdelenia SK/EN. |
| `P07` | priama detekcia DM/popola | `SCOPE_NARROWED` | Iba presne podopretý rozsah; žiadny absolútny zákaz bez mechanizmu. |
| `P08` | presný vzťah `n_s-w` | `WITHDRAWN` | Presná publikovaná formula sa odvoláva; broad shared-delta hypotéza ostáva otvorená. |
| `P09` | drift `delta` | `NOT_YET_AVAILABLE` | Samostatný riadok; bez odvodenej časovej funkcie. |
| `P10` | Lorentz/disperzia | `SCOPE_NARROWED` | Iba exact evenness auditovaného scalar cosine-Laplacian operátora; žiadny current photon-operator claim. |
| `P11` | graviton thermal background / `0.90 K / 53 GHz` | `RECALCULATION_OPEN` | Bez tvrdej teploty/frekvencie, kým nie je odvodený zdroj `C_g`. |

Povolený diagnostic addendum k `P04/P05`, nie nový prediction ID:

| `Delta N_eff` | podmienené `H0` [km/s/Mpc] | podmienené `S8` |
|---:|---:|---:|
| `0` | `65.79213819466531` | `0.8856095825403126` |
| `0.02675` | `66.08320294879377` | `0.8800254370658636` |
| `0.0535` | `66.37433224357665` | `0.874499891729803` |

Povinný label:
`THREE_DISCRETE_CONDITIONAL_LEGACY_ANCHOR_SENSITIVITY_POINTS`.

Povinné nonclaims: nejde o likelihood, posterior, confidence/credible
interval, spojitú obálku, fit ani tvrdú v3.18 predikciu. `H0` je podmienená
inverzia voči syntetickej kotve `h_ref=0.673`; `S8` používa zjednodušený
rast a `sigma8_LCDM=0.811`. `Delta N_eff=0` nie je nulový limit celej
teórie ani ΛCDM. Výsledok neuzatvára A2-K4, P5.4, G8 ani G9.

### 5.1 Povolená backgroundová provenance hodnota mimo prediction schémy

V3.18 smie uviesť túto hodnotu iba ako podmienený parameter-bookkeeping
výsledok, nie ako nový prediction ID:

```text
A_f = 7809.270101963506
CLAIM_CLASS = CONDITIONAL_FROZEN_A1_BACKGROUND_NORMALIZATION
```

Hodnota je jednoznačne určená spätnou integráciou zmrazeného A1-K1 closure
pri vstupoch

```text
lambda=0.15
delta=0.02297
Omega_m0=0.3517
h=0.6637
flat closure
x_reference=-18
```

a nie je novým nezávislým fitom ani konštantou prírody. Projektová RK4
hodnota má `relative_medium_fine=5.343344047845171e-13`; externý auditor ju
reprodukoval bitovo a nezávislá DOP853 kontrola dala
`7809.270101971514`, relatívne približne `1.0e-12`.

Povinné nonclaims:

- neodvodzuje mikrofyzický pôvod A1 vstupov ani plochosť; P2b zostáva
  otvorené;
- nedokazuje úplný K4 background, perturbácie, multi-mode closure,
  CLASS/CAMB, CMB alebo S8;
- neoprávňuje použiť skrátený K7 rad ako plný neskorý background;
- nemení hĺbku/skóre A2-K4 a nepridáva druhý fit;
- mapovanie `Phi(k)=A_f[H0*sqrt(Omega_r0)/k]^p` ruší módové `k^p` iba v
  auditovanom ranom rade; nie je dôkazom celého produktového mechanizmu.

## 6. Hranice main dokumentu a metodiky

- Main dokument smie rozlišovať `derived`, `conditional`, `hypothesis`,
  `open`, `withdrawn` a `historical`; nesmie povýšiť pracovný audit na vetu.
- R3.18-CONSOLIDATED nemení fundament ani nepridáva nový fit.
- Main dokument, nový úvod, stavová tabuľka, metodika a scope dokument musia
  spolu tvoriť úplný current snapshot. Žiadna veta typu „v3.17 navrhovala“
  nesmie byť jedinou definíciou mechanizmu; current hypotéza sa najprv
  vysvetlí priamo a historický rozdiel sa uvedie až potom.
- Nový 05aa pár je jediný konsolidovaný release register. Počas tejto
  release línie nevznikne ďalší `05ab`, addendum ani route-local 05 súbor.
- Detailná pracovná história zostáva v `tracks/`; release register obsahuje
  iba kanonické pravidlá, otázky, stav a odkazy na evidence.
- SK je autoritatívny obsah; EN je významovo zhodný preklad s rovnakými ID,
  rovnicami, číslami, stavmi a nonclaims.

## 7. Povinné kontroly pred frozen RC

1. presná 11-ID množina a jedinečnosť v oboch CSV;
2. SK/EN row-by-row stavová, číselná a evidence parity;
3. main-document odkazy iba na existujúce release payload cesty;
4. žiadny active link na historickú tabuľku ako current;
5. changelog obsahuje každé `SCOPE_NARROWED`, `WITHDRAWN`,
   `RECALCULATION_OPEN` a dôvod;
6. konsolidovaný 05aa obsahuje relevantné živé pravidlá bez duplicitných ID;
7. DOI/citation/link audit, UTF-8 a CSV schema audit;
8. secret/temp/duplicate/path a single-copy staging kontrola;
9. manifest viaže exact file SHA, Git commit a budúci immutable tag;
10. nezávislý frozen-RC documentation/release audit.
11. current-only tree preflight: exact 18-path finálny allowlist, exact
    25-path deletion allowlist, existencia všetkých successorov a zákaz
    neznámych tracked ciest;
12. čistý checkout finálneho RC musí zobraziť iba 18 povolených ciest a
    16/16 payload hash parity;
13. standalone-completeness audit: nový čitateľ bez v3.17 musí vedieť z
    aktuálneho SK/EN payloadu zrekonštruovať kotvu, ontológiu, kauzálny
    príbeh, filozofické princípy, základné rovnice, status tvrdení,
    falzifikačné hranice a poradie čítania.

Kontroly musia mať pred spustením očakávania a timeouty. Technická chyba nie
je fyzikálny STOP a riadi sa route-local desaťchybovou dávkou release línie.

## 8. Git, tag a Zenodo

- Aktuálny `D:\Teoria` nie je release-safe worktree; obsahuje existujúce
  zmeny a untracked artefakty.
- `D:\Teoria-main` je čistý read-only obraz `main`; nesmie sa použiť ako
  pracovný release adresár ani sa v ňom nesmie priamo editovať.
- Nový release worktree/branch sa odvodí z exact `main` HEAD/TREE uvedeného
  v §2.1 a bude mať samostatnú cestu a prefix `codex/`.
- Prvý commit release vetvy je iba `V317_ZENODO_2_ARCHIVAL_SYNC`:
  1. načíta 16 súborov z exact Zenodo content URL alebo použije lokálnu
     kópiu iba po zhode MD5 z §2.1;
  2. neprijme živý skript 09, kým nemá Zenodo MD5
     `2e2c6b32c8d39a5a6dc399018424d039`;
  3. uloží Zenodo súbory do kanonických repo ciest bez zmeny bajtov;
  4. pridá jediný repo-control súbor `.gitattributes` s exact `-text`
     pravidlom pre každú zo 16 kanonických ciest; je to nutné, pretože
     systémový Git má `core.autocrlf=true` a bez pravidla by checkout mohol
     meniť publikované bajty;
  5. pred stagingom overí `git check-attr` pre všetkých 16 ciest;
  6. po stagingu overí blob MD5, po commite vytvorí nový čistý testovací
     checkout a znovu dosiahne `16/16` MD5;
  7. nezávislý reviewer overí commit/tree, exact `.gitattributes` a oba
     `16/16` receipts;
  8. zverejnený Zenodo snapshot sa tým nemení — iba Git archív sa
     synchronizuje s už publikovanými bajtmi.
- Archival-sync baseline bol prijatý po staged-tree a čistom checkout teste
  `16/16` a po nezávislom read-only audite:
  `commit=e9e3579afdffc3c719f0beabb4ec33929cfb4d62`,
  `tree=6e317b76e17c08febb800fcc80742c77c8801aeb`,
  `branch=codex/v3.18-release`. Remote vetva má rovnaký commit; `main`
  zostal nedotknutý. Tento commit/tree je baseline pre tvorbu 14 nových
  `CURRENT_ONLY_CREATE` ciest v úplnom 16-payload nástupcovi v3.18.
- Archival-sync commit je trvalý historický rodič, nie požadovaný obsah
  finálneho current tree. Finálny v3.18 commit nahradí current obsah
  successor súbormi a odstráni superseded v3.17/duplicitné cesty podľa
  §3.3; história commitu `e9e3579...` zostane nezmenená.
- Pracovné delty z `D:\Teoria` sa smú preniesť iba do nových v3.18
  successorov alebo tracked README po evidence-by-evidence review; nikdy
  neprepíšu v3.17 súbor.
- Poradie je: reviewed RC -> clean status -> commit -> immutable tag
  `v3.18` -> Git push -> Zenodo draft preview -> explicitné Martinovo GO ->
  publish -> download/hash verification.
- Žiadny tag, push ani Zenodo záznam tento contract nepovoľuje.

## 9. Rozhodovacie vetvy review

- `PASS_CONTRACT`: exact scope, 16 payload ciest, 11 ID, nonclaims, evidence a gates
  sú úplné; orchestrátor môže samostatne otvoriť tvorbu release draftu.
- `REVIEW_CONTRACT`: opraviteľná neúplnosť bez zmeny release identity;
  contract sa opraví a znovu audituje.
- `STOP_CONTRACT_SCOPE`: contract by vyžadoval nový fyzikálny claim,
  potlačenie historického nálezu alebo nemožnú SK/EN/release konzistenciu;
  žiadny release draft sa nevytvorí.

## 10. Aktívny handoff

```text
TASK_ID: V318-CONSOLIDATED-STANDALONE-REBUILD-20260802
ROLE: main orchestrator / release artifact author
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/v318_pt1_h0_s8_preseal_review
ROUTE: RELEASE/v3.18/R3.18-CONSOLIDATED
CURRENT_PHASE: CONTRACT_R8_STANDALONE_COMPLETENESS_AUTHOR_INPUT_RECORDED / PRIOR_DELTA_DRAFT_REVIEW_STATE_REVOKED
ALLOWED_NEXT_ACTION: independent read-only audit of this revised contract; after acceptance rebuild the exact SK standalone corpus first, audit it, translate to EN, audit parity, then regenerate the six navigation/control files and manifests
ALLOWED_WRITES: this contract; route-local and central current plans; after contract acceptance exactly the sixteen release paths in sections 3.1 and 3.2 plus .gitattributes
FORBIDDEN_ACTIONS: treating the prior 14-file delta draft as release-ready; Python scientific run; any unlisted release path; staging; release commit; tag; main merge; GitHub release; Zenodo upload or publish before the new 16-payload frozen-RC review and explicit Martin review
RUN_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_RELEASE_DRAFT
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 3_ARCHIVAL_SYNC_HISTORY
CHECKPOINT_ID: CP-RELEASE-V318-PT1-H0-S8-C2C3-20260801-001
CHECKPOINT_STATUS: ACCEPTED_REUSABLE_CHECKPOINT_EXTERNAL_T2_CONFIRMED_P0_CONTROL_CLOSED
DONE_WHEN: exact 16-path self-contained draft exists; a reader without v3.17 passes the standalone-completeness audit; independent physics/math/documentation and SK/EN parity reviews pass; exact 18-path current tree and 16/16 payload hashes pass; Martin reviews every changed/deleted path; only then may a commit be separately authorized
NEXT_ROLE: documentation_release_steward for revised-contract closure; then /root creates the exact SK standalone corpus
```
