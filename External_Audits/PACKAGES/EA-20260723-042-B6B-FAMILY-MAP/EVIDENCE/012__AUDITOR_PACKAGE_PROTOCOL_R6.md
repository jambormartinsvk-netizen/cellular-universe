# Protokol balíkov pre externého auditora

**Stav:** `ACTIVE`  
**Dátum:** 2026-07-22  
**Revízia:** `R6` — R5 + exact REPRO closure, preregistračný freeze, presné oddelenie live artefaktov/registrov a agentový separation-of-duties closure po EA-039  
**Účel:** odovzdávať externému auditorovi malé, samostatne auditovateľné balíky bez ručného kopírovania a bez zahltenia celým projektom.

## 1. Jednoduchý model

Jeden auditný problém = jeden balík. Balíky sa vytvárajú iba na výslovnú
žiadosť používateľa alebo hlavného orchestrátora.

```text
External_Audits/
  PACKAGES/   <- nemenné dôkazové balíky pre čítanie
  RESPONSES/  <- Markdown odpovede externého auditora a následná diskusia
  HISTORY/    <- register vytvorených balíkov; nič sa z neho nemaže
  A1/         <- staršie route-local externé audity; zachované ako história
```

Auditor môže dostať toľko balíkov naraz, koľko problémov má súčasne
kontrolovať. Každý balík je samostatný; auditor nemusí prechádzať strom
`tracks/`, `scripts/` ani `Audit/` mimo balíka, pokiaľ si výslovne
nevyžiada ďalší artefakt.

## 2. Tvar jedného balíka

```text
PACKAGES/EA-YYYYMMDD-NNN-kratky-nazov/
  00_SCOPE_AND_READ_ORDER.md
  01_MANIFEST_SHA256.md
  01_MANIFEST_SHA256.tsv
  02_AUDITOR_INSTRUCTIONS.md
  03_REPRODUCTION_AND_EXPECTATIONS.md
  04_RUNTIME_DEPENDENCY_MAP.tsv
  05_PACKAGE_HISTORY.md
  EVIDENCE/
    001__nazov_suboru.md
    002__nazov_vysledku.json
  REPRO/
    scripts/...
```

`EVIDENCE/` má iba jednu hĺbku. `REPRO/` zachováva presné runtime cesty.
Súbory sa kopírujú, nie linkujú. Od R5 platí **single-copy capsule**:
rovnaký fyzický súbor sa v jednom balíku nachádza iba raz. Ak je runtime
súbor zároveň dôkazom, číta sa priamo z `REPRO/` a manifest mu pridelí obe
logické roly; nesmie mať druhú kópiu v `EVIDENCE/`.

`00_SCOPE_AND_READ_ORDER.md` vždy obsahuje tvrdenie, nonclaims, poradie
čítania, predregistrované PASS/REVIEW/STOP kritérium a presnú otázku pre
auditora. `01_MANIFEST_SHA256.md` je zdroj pravdy pre integritu balíka.

## 3. Odpovede auditora a viac-kolová diskusia

Auditor nepíše do `PACKAGES/` ani nemení dôkazy. Jeho výstup sa zapisuje do:

```text
RESPONSES/EA-YYYYMMDD-NNN-kratky-nazov/
  00_AUDITOR_AUDIT.md
  01_PROJECT_RESPONSE.md
  02_AUDITOR_FOLLOWUP.md
  03_PROJECT_DECISION.md
```

Stačí vytvoriť len súbory, ktoré sú v danej diskusii potrebné. Všetky sú v
Markdownu. Ak audit skončí po prvom posudku, vznikne iba
`00_AUDITOR_AUDIT.md`.

Externý posudok je read-only odporúčanie. Iba hlavný orchestrátor môže po
jeho vyhodnotení zapísať autoritatívny PASS/REVIEW/STOP do route-local
stavu.

## 4. Nemennosť a revízie

1. Kým je balík explicitne `DRAFT_NOT_DELIVERED`, možno ho refreezeovať, ale
   každá revízia musí zostať v `05_PACKAGE_HISTORY.md`.
2. Od stavu `SEALED_READY_FOR_AUDIT` sa dôkazový balík nemení ani nedopĺňa
   potichu. Ak je nutný ďalší súbor, nová verzia dôkazov alebo oprava hashu,
   vznikne nový balík s novým `NNN` a odkazom na predchodcu.
3. Odpoveď auditora sa nikdy neprepisuje; nasledujúca reakcia je nový súbor
   v `RESPONSES/`.
4. Stav vytvorených balíkov vedie
   `HISTORY/00_PACKAGE_REGISTER.md`.

## 5. Čo používateľ napíše pri žiadosti

Stačí krátka veta, napríklad:

```text
Priprav externý balík pre KMPC-036: iba numerický floor a tri driver[7] riadky.
```

alebo:

```text
Priprav balík pre A2-K4/P5: audit Bianchi identity a prenosu vzorca do runnera.
```

Hlavný orchestrátor potom vyberie iba potrebné zdroje podľa
`A1/A1K1/A2/A2K4/P5/00_EXTERNAL_AUDIT_HANDOFF_SK.md`, vytvorí manifest,
skopíruje súbory a založí prázdnu šablónu odpovede. Nevykoná nový fyzikálny
beh, pokiaľ to nie je výslovne súčasťou zadania.

## 6. Povinné rozlíšenie výsledkov

Balík aj odpoveď musia uviesť, či zistenie je:

- `PRECHECK_EXCLUDED_SCOPE` — predbežne certifikované vylúčenie bez behu;
- `COMPUTED_STOP_SCOPE` — fyzikálny STOP z úplného testu;
- `OBSERVATIONAL_STOP_SCOPE` — STOP z úplnej likelihood reťaze;
- `REFERENCE_MISMATCH_ONLY` — nezhoda s benchmarkom, nie sama STOP;
- `TECHNICAL_STOP` — technický problém, nie smrť fyziky.

Tým sa externý auditor nedozvie iba „mŕtva/živá“, ale aj aký druh dôkazu
daný stav naozaj nesie.

## 7. Povinná dôkazová úroveň externého auditu

Každý balík a odpoveď označia najvyššiu skutočne dosiahnutú úroveň:

| Úroveň | Obsah | Čo smie auditor tvrdiť |
|---|---|---|
| `T0_CONTEXT` | iba súhrny, statusy a vysvetlenia | kontextová pripomienka, nie formula alebo computed verdict |
| `T1_PRIMARY_FORMULA` | primárny zdroj vzorca/kódu, presná cesta, hash a riadky | formula-lineage záver a rozmerová kontrola |
| `T2_REPRODUCIBLE_CALCULATION` | T1 + runner, všetky importy a runtime-opened vstupy, prereg, raw výsledok, tolerancie, verzie a reprodukčný príkaz; predpísaná oficiálna vetva dobehne bez obídenia guardov | nezávislá reprodukcia deklarovaného výpočtu |
| `T3_INDEPENDENT_IMPLEMENTATION` | T2 + druhá implementácia, ktorá nekopíruje testovanú logiku | silná nezávislá numerická/algebraická kontrola |

Auditor pri každom hlavnom tvrdení použije jeden z tagov:
`OBSERVED_IN_PRIMARY`, `INDEPENDENTLY_RECOMPUTED`,
`INFERRED_FROM_PROJECT_DOCS`, `CONTEXT_ONLY`.

Tvrdenie `COMPUTED_STOP_SCOPE` sa nesmie udeliť iba zo sekundárneho
Markdown súhrnu. Auditor musí mať aspoň T2 alebo explicitne napísať, že
kontroluje iba mapu už existujúceho computed verdiktu.

## 8. Povinný výpočtový kapsul

Ak scope obsahuje vzorec, numerické číslo, konvergenciu alebo raw verdict,
balík musí obsahovať najmenšiu reprodukovateľnú sadu:

1. runner a všetky používané projektové importy;
2. vstup/config a zdroj externých dát;
3. preregistrované očakávanie, tolerancie a PASS/REVIEW/STOP vetvenie;
4. raw výstup a ľudský audit;
5. verzie prostredia a krátky reprodukčný príkaz;
6. vnútorný a vonkajší timeout;
7. aspoň jednu negatívnu alebo nulovú kontrolu, ak je relevantná.

Za runtime vstup sa považuje aj JSON, config, tabuľka alebo iný súbor
otvorený až počas `smoke` alebo `audit` vetvy. Import closure bez týchto
súborov nie je úplný výpočtový kapsul.

Neprikladajú sa nesúvisiace tisíce skriptov. Kapsul má byť minimálny, ale
úplný pre tvrdenie v scope.

## 9. Dodatočný kontext mimo balíka

Ak auditor dostane neskôr prístup k ďalším dokumentom, addendum musí uviesť
ich presné relatívne cesty a SHA-256. Bez toho má addendum stav
`UNSEALED_CONTEXT_REVIEW` a nesmie samo zmeniť projektový verdikt.

Manifest každého nového balíka musí pri každej fyzickej položke uviesť:

- cestu jedinej kópie v `EVIDENCE/` alebo `REPRO/`;
- pôvodnú relatívnu cestu;
- SHA-256 zdroja aj kópie;
- rolu `primary/derived/context/raw-result`;
- dôvod zaradenia.

Kontrola iba hashu kópie bez source mapy nestačí na formula-lineage audit.

## 10. Povinný lifecycle balíka

Každý balík prechádza iba týmto sledom:

```text
DRAFT_NOT_DELIVERED
  -> PREFLIGHT_PASSED
    -> SEALED_READY_FOR_AUDIT
      -> SENT_TO_EXTERNAL_AUDITOR
        -> AUDIT_RECEIVED
          -> ASSESSED_BY_MAIN_ORCHESTRATOR
```

Stav `READY` sa nesmie zapísať iba preto, že existuje manifest. Pred
zapečatením musí prejsť strojový preflight, runtime dependency closure a
kontrola prázdnej response šablóny. Register balíkov vedie zvlášť stav
odovzdania, odpoveď auditora a autoritatívne spracovanie.

## 11. Strojový manifest a package preflight

Nový balík povinne obsahuje ľudský `01_MANIFEST_SHA256.md` a strojový
`01_MANIFEST_SHA256.tsv`. TSV má stĺpce:

```text
copy_path  source_path  role  source_sha256  copy_sha256  reason
```

Ďalej obsahuje `04_RUNTIME_DEPENDENCY_MAP.tsv` so stĺpcami:

```text
runtime_path  role  sha256  required_by
```

Pred `SEALED_READY_FOR_AUDIT` sa musí spustiť read-only kontrola:

```powershell
pwsh -NoProfile -File External_Audits/TOOLS/Test-ExternalAuditPackage.ps1 -PackagePath <package>
```

R6 preflight vyžaduje PowerShell `7+`; legacy Windows PowerShell 5.1 nie je
podporovaný a musí fail-fast skončiť pred kontrolou balíka.

Preflight overí povinné control súbory, source/copy parity, všetky runtime
vstupy, response template, absenciu temp súborov a nedoplnených hashov.
Výsledok preflightu sa zapíše do `05_PACKAGE_HISTORY.md`; samotný tool nič
nemení.

## 12. Dependency closure nie je iba import closure

Príprava balíka musí staticky aj behaviorálne rozlíšiť:

1. Python/project importy;
2. runtime-opened JSON/config/data vstupy;
3. referenčné raw výsledky používané iba na porovnanie;
4. generated outputs;
5. voliteľné diagnostické vstupy.

Každý povinný runtime vstup musí byť v presnej runtime ceste pod `REPRO/`,
v SHA manifeste aj runtime mape a v negatívnom teste chýbajúcej závislosti.
Od R5 sa už neduplikuje do `EVIDENCE/`; dokument 00 odkáže auditora na
jeho jedinú `REPRO/` kópiu. Output adresár smie obsahovať vstupný JSON iba
vtedy, keď je v runtime mape explicitne označený
`runtime-prerequisite`, nie generated result.

Od R6 sa closure nesmie odvodiť iba z importov a očividných JSON loaderov.
Preflight musí porovnať runtime mapu so **všetkými fyzickými súbormi** pod
`REPRO/` a staticky prejsť aj lokálne `scripts/...` a `tracks/...` cesty
uvedené v source hash mapách alebo otvorené nepriamo. Každá taká cesta musí
mať jedinú exact-hash kópiu v `REPRO/`, manifestový riadok a runtime-map
riadok. Historický preflight, ktorý iba overil deklarovanú mapu, nie je sám
osebe dôkazom úplnosti mapy.

## 13. Zmrazené prahy, platformové diagnostiky a odchýlky

- Projektový rozhodovací prah sa po výsledku nezmäkčuje.
- Same-machine immutable regresia a cross-platform reprodukcia sú dve
  rozdielne kontroly.
- Nový cross-platform prah môže vzniknúť iba v novom predregistrovanom
  balíku, musí byť `DIAGNOSTIC_ONLY` a mať `verdict_effect=NONE`.
- Ak oficiálna vetva zlyhá a auditor obíde guard alebo priamo zavolá solver,
  výsledok je `DECLARED_DEVIATION`. Môže podporiť interpretáciu, ale sám
  nedosahuje T2 deklarovaného runnera.
- Exact arithmetic tej istej implementácie odstraňuje FP neistotu, nie
  spoločnú formulačnú chybu. T3 vyžaduje druhý row/equation builder, ktorý
  nekopíruje testovanú logiku.

Pri fresh-copy field parity sa smú normalizovať iba vopred pomenované
nevedecké polia: wall/runtime údaje a absolútny koreň cesty, ak zostane
identický relatívny suffix aj SHA-256 zdroja. Každá taká výnimka musí byť
uvedená v reprodukčných pokynoch a package history. Fyzikálne čísla,
identity, gate hodnoty, prahy ani source hashe sa normalizovať nesmú.

Zoznam normalizovaných polí musí byť úplný ešte pred auditom a musí zahŕňať
aj vnorené runtime polia. Pri provenance ceste sa neodstraňuje celý údaj:
normalizuje sa iba absolútny koreň a povinne sa overí relatívny suffix plus
SHA-256 cieľového zdroja.

## 14. Povinný kontrakt odpovede auditora

Každá nová response šablóna vychádza z
`External_Audits/TEMPLATES/00_AUDITOR_RESPONSE_TEMPLATE.md` a vyžaduje:

1. auditor/model/verziu, dátum a časovú zónu;
2. manifest PASS/FAIL a najvyšší skutočný tier;
3. Python, knižnice, BLAS/LAPACK, OS a architektúru;
4. presný príkaz, exit code, wall time a SHA-256 generated výstupu pre
   manifest, smoke, official audit a každú odchýlku;
5. tag dôkazu pri každom hlavnom tvrdení;
6. oddelený dopad na package tier a na fyzikálny verdict;
7. explicitné nonclaims a vyhlásenie autority.

Predikcia budúceho PASS/FAIL patrí medzi testovateľné hypotézy. Nesmie byť
súčasťou prijatého výsledku ani meniť poradie už predregistrovaných brán.

## 15. Kompaktnosť, ucelená časť a rozpočet súborov

Balík sa nevytvára automaticky po každom support medzikroku. Za ucelenú
časť sa štandardne považuje až uzavretý mód cez predregistrované `k` body,
autoritatívny fyzikálny `STOP` alebo významný blocker, ktorý mení ďalšiu
route. Viac blízkych support krokov jedného módu sa zhromaždí do jedného
auditného balíka. Technický neúspech bez fyzikálneho raw nemá samostatný
balík; jeho ledger, `DO_NOT_RUN` stav a nástupca sa priložia k najbližšiemu
ucelenému výsledku.

Pracovný rozpočet jedného bežného výpočtového atómu je najviac:

1. jedna predregistrácia;
2. jeden base alebo versioned successor;
3. jeden tenký runner;
4. jeden immutable raw výsledok;
5. jeden výsledkový dokument.

Odchýlka je dovolená iba pri preukázanom technickom zlyhaní alebo povinnej
provenance vrstve a musí byť vysvetlená v error ledgeri. Centrálne plány,
scorecardy a manifesty sa neaktualizujú po každom support medzičlánku;
menia sa až pri skutočnej zmene autoritatívneho stavu, uzavretí módu,
zmene aktívneho blockeru alebo `STOP`.

Standalone T2 balík môže obsahovať viac **jedinečných** súborov kvôli úplnému
runtime closure, ale od R5 nesmie obsahovať duplicitné fyzické kópie tej istej
source/runtime položky. Počet package kópií sa vždy uvádza oddelene od počtu
pracovných zdrojových zmien. Pred vytvorením balíka sa musí skontrolovať, či
rovnaký auditný cieľ nemožno bezpečne spojiť s ďalšími už rozpracovanými
atómami toho istého módu. EA-013 až EA-015 zostávajú immutable historickým
príkladom príliš jemného delenia; nesmú sa spätne prepisovať ani mazať
potichu.

## 16. R6 single-copy budget a rýchly handoff

Od EA-039 sa pred každou novou ucelenou časťou vedú štyri explicitné
počítadlá a zoznam ciest, z ktorého sa čísla mechanicky odvodia:

```text
LIVE_SCIENTIFIC_ARTIFACTS = nové base/runner/prereg/raw/result artefakty
LIVE_CENTRAL_REGISTERS_UPDATED = existujúce plány, DNR, event/package registre
LIVE_FILES_CHANGED_TOTAL = súčet predchádzajúcich dvoch čísel
AUDIT_PACKAGE_COPIES = fyzické kópie vytvorené iba pre externý audit
```

Počet súborov v Git/Codex UI sa nikdy nesmie prezentovať ako počet zmien
rovníc. `00_SCOPE_AND_READ_ORDER.md`, package history a záverečná správa
uvedú všetky štyri čísla osobitne. Počet sa nesmie odhadnúť z logických
batchov; každý fyzicky vytvorený alebo upravený live súbor sa započíta
presne raz. Package preflight zatiaľ tieto live cesty nepozná, preto ich
pred sealom nezávisle skontroluje druhý agent alebo reviewer.

### Preregistračný freeze

Pred prvým Python procesom musí byť predregistrácia obsahovo konečná,
musí obsahovať source/input hashe, rozhodovacie vetvy a output guard a jej
SHA-256 sa zaznamená v pre-run receipte alebo append-only route registri.
Od prvého Python procesu sa predregistrácia už nikdy neupravuje.

Compile/help/smoke/official ledger, raw SHA a post-run interpretácia patria
do samostatného execution/result/audit dokumentu. Doplnenie execution
ledgeru späť do preregistrácie je od R6 zakázané, pretože by zničilo exact
hash obsahu, ktorý existoval pred výpočtom. Ak historický atóm takýto
receipt nemá, audit musí uviesť `PREREG_CHRONOLOGY_PROCESS_ASSERTION_ONLY`
a nesmie tvrdiť kryptograficky úplnú časovú provenienciu.

### Default hard budget

- jeden bežný výpočtový atóm: najviac `5` nových live artefaktov;
- aktualizácie živých centrálnych registrov: najviac `4` pri ucelenom
  closure, nie po každom medziatómovom kroku;
- štandardný externý balík: najviac `40` fyzických súborov vrátane
  control súborov a response šablóny;
- jedna source/runtime položka: presne jedna fyzická kópia v balíku.

Prekročenie nie je automaticky zakázané, ale ešte pred kopírovaním vyžaduje
v commentary oznámiť plánovaný počet, dôvod a najmenšiu alternatívu.
`00_SCOPE_AND_READ_ORDER.md` potom obsahuje
`BUDGET_EXCEPTION_JUSTIFICATION`. Bez tohto zápisu balík ostáva
`DRAFT_NOT_DELIVERED`.

### Rýchly postup

1. predregistrácia a jeden versioned base/runner iba ak ich skutočne treba;
2. preregistráciu zmraziť, zaznamenať jej SHA a overiť neprítomnosť outputu;
3. compile/help/smoke/official a samostatný interný audit/result ledger;
4. centrálne registre aktualizovať jedným batchom až pri zmene stavu;
5. z explicitného zoznamu ciest spočítať live artefakty a registre;
6. balík zostaviť z jedinečných fyzických súborov podľa runtime mapy;
7. jeden negatívny guard a jedna nezávislá success vetva; ďalšie vetvy iba
   ak dokazujú odlišný failure mechanizmus;
8. po seal už nič nepridávať; nový kontext patrí do response alebo nového
   package ID podľa pravidiel nemennosti.

## 17. Audítorský ruleset a oddelenie kurátora

Pred zostavením nového balíka package charter povinne uvedie:

```text
PACKAGE_CURATOR_TASK_ID
EXTERNAL_AUDITOR_TASK_ID
SEPARATION_OF_DUTIES_CHECK
AUDITOR_RULESET_PATHS_AND_SHA256
AUDITOR_ROLE_CONFIG_SHA256
```

Kurátor a externý auditor toho istého balíka musia mať rozdielne task
identity. Rovnosť alebo chýbajúca identita znamená
`SEPARATION_OF_DUTIES_FAILURE / DRAFT_NOT_DELIVERED`.

Balík obsahuje v control vrstve exact kópie audítorského rulesetu potrebného
na izolovaný bootstrap — minimálne projektové `AGENTS.md`,
`tracks/00_PROJECT_OPERATING_SYSTEM.md`, tento R6 protokol a použitý
`external_auditor.toml`. Všetky kópie sú v package manifeste, read orderi a
charterovom zozname SHA. Orchestrátor pred sealom overí live role-config hash
voči `.codex/agents/00_MANIFEST.md`; kurátor overí source/copy paritu.

Externý auditor po seal nečíta live projekt. Overuje iba package kópie a ich
charterové hashe. Chýbajúci alebo nezhodný ruleset/config znamená
`PACKAGE_CLOSURE_BLOCKER / CANNOT_AUDIT`; nesmie sa obísť načítaním live
súboru. Kým R6 preflight nemá túto kontrolu implementovanú mechanicky,
vykoná ju pred sealom druhý read-only reviewer, odovzdá checksumovaný
výsledok kurátorovi alebo orchestrátorovi a ten ho verbatim zapíše do
package history.

EA-028 a EA-029 ostávajú immutable historickými R4 balíkmi. Ich duplicitné
`EVIDENCE/REPRO` súbory sa spätne nemažú ani neprepájajú.
