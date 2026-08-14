# Audit pripravenosti verzie 3.18 — stav k 2026-07-28

**Dátum:** 2026-07-28  
**Typ:** read-only release snapshot; nemení vedecké verdikty  
**Autoritatívny živý stav:** `tracks/00_CURRENT_EXECUTION_PLAN.md`  
**Odporúčaná release trieda:** `R3.18-DOC/ERRATUM`  
**Aktuálny release verdikt:** `NO-GO / RELEASE_CANDIDATE_NOT_OPEN`

## 1. Stručný záver

Teória má dostatok materiálneho auditného obsahu na zmysluplnú verziu
`3.18`, ale k 2026-07-28 ešte nemá pripravený publikovateľný release
candidate. Fundament v3.17 sa nemení, preto nejde o v4.0. Najbližšie
vydanie má byť úzko ohraničená konsolidačná a opravná verzia
`DOC/ERRATUM`, nie `PHYS` ani `PREDICTION`.

Najsilnejším dôvodom na vydanie je PT1 z 2026-07-16: niektoré verejné
predikčné tvrdenia v3.17 už nemožno držať ako aktuálne predikcie. PT2
nevznikol, preto sa nesmú vymyslieť náhradné čísla.

## 2. Aktuálny vedecký stav

| Úroveň | Stav | Význam |
|---|---|---|
| A0 | dokončená metodicky | publikované verzie sú nemenné; každá nová verzia má changelog a SHA manifest |
| A1-K1 | prešiel iba backgroundovou bránou | existuje konzistentný kandidát homogénneho pozadia; nejde o potvrdené poruchy ani úplnú teóriu |
| A2 | nedokončená | žiadna koľaj zatiaľ neprešla celou lineárnou stanicou |
| A2-K4 | hlavná živá koľaj, `60/100 = G6` | nemá fyzikálny STOP; numerická coverage C2 `10/10`, C3 `45/45`, ale chýba fyzicky uzavretý produktový mechanizmus a úplný seed |
| A2-K1/K2/K3/K5/K6 | scoped STOP | dôvody smrti boli po nájdených implementačných chybách znovu ohraničene potvrdené |
| A2-K7/K8/K9/K11/K12 | živé zálohy, `REVIEW_BLOCKED_PARENT` | majú zmapované mantinely a mŕtve podtriedy; nemajú explicitný úplný kernel/svedka na ďalšiu bránu |
| P5.4 | `NOT RUN` | krátka species-first evolúcia nie je povolená pred úplným seedom |
| G8/G9 | `BLOCKED/NOT RUN` | plná Boltzmannova hierarchia a likelihood zatiaľ neexistujú |
| A3/A4 | nedosiahnuté | CLASS/CAMB a ďalšie stanice nemožno prezentovať ako prejdené |

Historická hĺbka K7 `66.5/100` je iba technická hĺbka redukovanej RHS.
Platná fyzikálna hĺbka K4 je `60/100`.

## 3. Na čom sa pracuje

Aktívna route je:

`A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> D03 -> B6b-2.10 -> C01-RW1 -> Q1R1-V3`.

Numerické brány C2/C3 sú uzavreté. Aktuálny blocker je fyzikálny pôvod
lokálneho procesu, ktorý má konzistentne určiť vznik a postupnosť hmoty,
pary a popola, event rate, energiu udalosti, conservation momenty, reset a
kauzálny nosič.

Autor zvolil first-passage topológiu `e -> s+M`, následne `M -> C`, iba ako
pracovný rámec. Rodiny MF1–MF4 a formálne mantinely prešli mapovacími
bránami, ale fyzický witness nebol nájdený. C01-RW1 je testovacia E3 vetva,
nie fyzikálna pravda. Jej množina nie je dokázane prázdna ani neprázdna.

Najnovší dokument 291 je `DRAFT_UNFROZEN`. Povoľuje iba nezávislý read-only
audit Q1R1-V3 transportnej preregistrácie. `RUN_AUTHORIZED=false`; sieť,
Python a fyzikálna inferencia nie sú povolené.

## 4. Čo nové má priniesť v3.18

### 4.1 Release-ready smer

V3.18 má byť poctivá konsolidácia v3.17:

1. opravené rozdelenie backgroundu, porúch, mikrofyziky a dátového fitu;
2. A1-K1 označená iba ako backgroundový kandidát;
3. oprava fixed-`K_MPC=0.05` úniku perturbatívneho módu do backgroundu a
   požiadavka jedného univerzálneho `H(a)`;
4. jednoznačný baryón/CDM/fuel ledger a smer `Q^mu`;
5. stavová mapa všetkých A2 koľají vrátane presných dôvodov scoped smrti a
   podmienok znovuotvorenia;
6. metodické pravidlá AR1–AR9: vstupy autora ako hypotézy, koľaje,
   zachovanie mŕtvych vetiev a skriptov, nemennosť publikovaných verzií,
   dôkazové úrovne, SK/EN parita a formula-to-implementation audit;
7. nový register otázok Q17–Q34 a obmedzenia starších tvrdení L1–L7;
8. auditovateľná reprodukčná stopa, error/DNR registre, timeouty, immutable
   outputs a oddelené externé audity;
9. changelog v3.17 -> v3.18, release manifest, SHA-256, Git commit/tag a
   presné nonclaims.

### 4.2 Povinné PT1 opravy predikcií

| Verejné tvrdenie v3.17 | Stav vo v3.18 | Náhrada |
|---|---|---|
| `N_eff=3.09–3.10`, resp. `Delta N_eff=0.0535` | `SUPERSEDED IN SCOPE / CONDITIONAL ESTIMATE` | `NOT YET AVAILABLE` |
| termálne pozadie `0.90 K / 53 GHz` | `SUPERSEDED IN SCOPE / RECALCULATION OPEN` | `NOT YET AVAILABLE` |
| `H0=66.4 km/s/Mpc` | `MATERIAL IMPACT AUDIT REQUIRED` | bez nového čísla, kým nevznikne PT2 |

Rovnako treba jasne uviesť, že staré drag/krivostné `S8/H0` gridy boli toy
alebo post-data sensitivity, nie nové predikcie. `C=28`, `m=1/2`, `r`,
`Delta N_eff`, `f_NL` a viaceré `n_s` interpretácie musia niesť presný
podmienený alebo otvorený status.

### 4.3 Čo sa do v3.18 nesmie povýšiť na hotový výsledok

- fyzický lokálny mechanizmus hmoty–pary–popola;
- complete W10 witness alebo potvrdenie C01-RW1;
- úplné gauge-invariantné poruchy;
- P5.4, G8 alebo G9 PASS;
- nové validované `S8`, `H0`, `Delta N_eff` alebo teplota pary;
- globálne zlepšenie likelihood voči LambdaCDM;
- odvodenie `epsilon`, `C=28`, `m=1/2`, kolapsu alebo šípu času z prvých
  princípov.

Tieto položky môžu byť publikované iba ako otvorené otázky, mantinely,
scoped no-go výsledky alebo pracovný program.

## 5. Release pripravenosť k 2026-07-28

| Oblasť | Stav |
|---|---|
| release candidate | neotvorený |
| `SCOPE_v3.18.md` | chýba |
| `CHANGELOG_v3.18.md` | chýba |
| `MANIFEST_v3.18.sha256` | chýba |
| prediction-table row audit | otvorený |
| SK/EN celková parita | otvorená |
| čistý release checkout a reprodukcia | otvorené |
| Git release commit/tag | chýba |
| nezávislý audit zmrazeného RC | chýba |
| Zenodo draft/post-publish hash kontrola | neprebehla |

Pracovný worktree `D:/Teoria` je na správnej vetve
`work/v3.18-audit-2026-07-16`, ale `git status` ukazuje približne 600
zmenených/nepridaných položiek. Hromadné `git add .` je zakázané. Stav
oddeleného `D:/Teoria-main` nebol v tomto audite dôveryhodne overený pre Git
safe-directory/ownership blokáciu.

## 6. Realistický plán do konca júla

Do 2026-07-30 je realistický iba úzky `R3.18-DOC/ERRATUM`, a aj ten iba po
krátkom release sprinte:

1. zmraziť scope a explicitne presunúť nedokončenú fyziku mimo release;
2. dokončiť riadkový PT1 audit SK/EN predikčnej tabuľky bez náhradných čísel;
3. vytvoriť changelog a verejný register tvrdení/dôkazových úrovní;
4. vybrať malý release obsah cez explicitný staging manifest;
5. vykonať SK/EN, link, secret, size a reprodukčný audit;
6. vytvoriť RC manifest/SHA, reviewed commit a tag;
7. dať nemenný RC nezávisle zaauditovať;
8. až potom vytvoriť Zenodo novú verziu a vykonať post-publish hash kontrolu.

Ak tieto kroky nemožno dokončiť bez skratiek, termín treba posunúť. Samotný
koniec mesiaca nie je release trigger a nesmie prekryť otvorený checklist.

## 7. Verdikt

`v3.18` je správne číslo a projekt má významný nový auditný obsah. K
2026-07-28 však nie je pripravený na publikovanie. Najlepším verejným
sľubom je:

> Konsolidovaná a auditovaná verzia efektívneho modelu v3.17 s opraveným
> rozsahom tvrdení, aktualizovaným registrom otázok a mŕtvych koľají,
> reprodukčnou stopou a explicitným zoznamom otvorených fundamentálnych
> podmienok.

V3.18 nesmie sľubovať dokončenú A2, nové validované kozmologické predikcie
ani mikrofyzický mechanizmus, ktorý projekt zatiaľ nemá.

## 8. Použité autoritatívne zdroje

- `tracks/00_PROJECT_OPERATING_SYSTEM.md`;
- `tracks/00_CURRENT_EXECUTION_PLAN.md`;
- `tracks/00_READ_FIRST.md`;
- `tracks/A1/A1K1/A2/A2K4/00_WORK_PLAN.md`;
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_WORK_PLAN.md`;
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/291_B6B2_10_H_RDIV_C01_RW1_Q1R1_V3_CANONICAL_HOST_SOURCE_ARCHIVE_PREREGISTRATION_SK.md`;
- `tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md`;
- `tracks/METHODOLOGY/00_RELEASE_PROMOTION_LEDGER.md`;
- `tracks/METHODOLOGY/00_GIT_BRANCH_AND_RELEASE_POLICY.md`;
- `Questions/ZENODO_VERSION_PUBLICATION_CRITERIA.md`;
- `Questions/ZENODO_RELEASE_CHECKLIST_v3.18.md`;
- `Questions/ZENODO_RELEASE_CHECKLIST_v3.18_ADDENDUM_PREDICTION_TABLE.md`;
- `Audit/dodatok_ciel_a_vydanie_v3.18_verzus_v4.0_2026-07-13.md`.

## 9. Procesný výkaz

```text
TASK_ID: V3.18-RELEASE-READINESS-SNAPSHOT-20260728
ROLE: main_orchestrator_read_only_assessment
READ_SET_CONFIRMED: mandatory bootstrap + active route/prereg + release ledgers
FILES_CHANGED: Audit/V3_18_RELEASE_READINESS_AUDIT_2026-07-28_SK.md
PYTHON_PROCESSES: 0
LIVE_SCIENTIFIC_ARTIFACTS: 0
LIVE_RELEASE_AUDIT_ARTIFACTS: 1
LIVE_CENTRAL_REGISTERS_UPDATED: 0
TOTAL_FILES_CHANGED: 1
AUDIT_PACKAGE_COPIES: 0
NONCLAIMS: no new physics verdict, score, depth, RUN_AUTHORIZED or release GO
NEXT_ROLE: documentation_release_steward after author opens release candidate
DONE_WHEN: author accepts narrow DOC/ERRATUM scope and release sprint starts
```
