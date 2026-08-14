# Pracovný register metodických pravidiel a otázok — SK

**Vrstva:** `tracks/` — pracovná, nie release korpus  
**Aktualizované:** 2026-07-17  
**Stav:** autoritatívny pracovný smerovník; do `theory/` sa konsoliduje až pri release candidate

## Kontrola duplicity

Zmrazený základ obsahuje AR1–AR8, historické dodatky obsahujú AR9–AR69.
AR5 chráni publikované verzie, AR7 vyžaduje SK/EN súlad, AR66 riadi živé
plány a AR69 vlastníctvo artefaktov. Nijaké z nich však neurčuje hranicu,
kde vzniká pracovný kandidát a kedy smie vstúpiť do `theory/`.

## AR70 — hranica pracovného registra a release korpusu

1. Nová pracovná otázka, zmena stavu, kandidát pravidla, obmedzenie, auditná
   diskusia a predregistrácia vznikajú v najnižšom príslušnom uzle
   `tracks/<route>/`.
2. Bežný stav koľaje sa vedie v `00_WORK_PLAN.md`, `00_CURRENT_DECISION.md`,
   `HISTORY/00_EVENT_LEDGER.md`, manifeste alebo `AUDIT_THREADS/`; nevytvára
   nový súbor `theory/*/05...`.
3. Ak uzol potrebuje skutočný lokálny register delty AR/Q/L, použije voliteľný
   pár `05_RULE_AND_QUESTION_CANDIDATES_SK.md` a
   `05_RULE_AND_QUESTION_CANDIDATES_EN.md`. Obsahuje iba nové delty, nie kópiu
   celého registra, a je označený `WORKING / NOT_RELEASED`.
4. Kandidát spoločný pre viac koľají sa vedie v tomto globálnom pracovnom
   registri v `tracks/METHODOLOGY/`, opäť v obsahovo zhodnom páre SK/EN.
5. `theory/SK` a `theory/EN` obsahujú vydaný alebo release-ready konsolidovaný
   obsah. Priebežný runner, technické erratum, otvorená otázka ani stav
   `REVIEW` sa tam nezapisujú ako nový tematický dodatok.
6. Povýšenie do `theory/` smie vykonať iba hlavný orchestrátor pri otvorenom
   release candidate, po kontrole duplicity, dôkazovej reťaze, SK/EN súladu,
   changelogu, release triggera a SHA-256 manifestu.
7. Existujúce historické súbory rodiny `theory/*/05*` sa nemažú ani fyzicky
   nepresúvajú bez Git baseline, úplnej mapy `OLD_PATH -> NEW_PATH`, kontroly
   odkazov a hashov. Od 2026-07-16 sú zmrazené ako historická/release vrstva;
   nie sú živým miestom pracovného zápisu.

## Náhrada starého workflow

Starú inštrukciu „nové pravidlo dostáva nový párový dodatok v `theory`“
nahrádza:

> Nové pravidlo najprv dostáva párový pracovný záznam v príslušnej hĺbke
> `tracks`. Do `theory/SK` a `theory/EN` sa konsoliduje iba po prijatí
> hlavným orchestrátorom a otvorení release candidate.

## FS-GATE-01 — funkcia sa najprv obmedzuje správaním

Pred voľbou konkrétnej funkcie, akcie alebo kernelu sa vytvorí behaviorálny
a následne fyzikálny mantinelový pas podľa
`tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md`.

1. Najprv sa zapíšu vstupy, výstupy, znamienka, trendy, prahy, nulové body,
   saturácie a energetické hranice známe zo zákonov alebo pozorovania.
2. Ak sú tieto nutné správania navzájom nezlučiteľné, podtrieda dostane
   `BEHAVIORAL_EMPTY_SCOPE`; presný tvar funkcie netreba poznať.
3. Ak je behaviorálny obal neprázdny, vzniká iba `BEHAVIORAL_OPEN`, nie
   fyzikálny PASS. Ďalej sa hľadá jeden explicitný lokálny svedok.
4. Neúspešný grid alebo nenájdený ansatz nie je dôkaz prázdnosti.
5. Dôvod smrti sa zapisuje ako certifikovaná neexistencia spoločnej množiny
   výstupov v presne uvedenom rozsahu, nie ako „funkciu sme nenašli“.
6. Táto pracovná brána nepridáva skóre a nevytvára nové AR/Q číslo, kým je
   identifikátorový register zamknutý.

### FS-GATE-01a — dôkazová váha a odlíšenie predbežného no-go

**Prijaté používateľom:** 2026-07-17  
**Stav:** záväzné spresnenie existujúcej FS-GATE-01; bez nového AR/Q čísla.

1. Každý mantinel budúcej funkcie/kernelu sa označí `E0_EXACT`,
   `E1_DIRECT_MEASUREMENT`, `E2_REFERENCE_MODEL` alebo `E3_PROVISIONAL`
   podľa `00_CONSTRAINT_FEASIBILITY_GATE_SK.md`.
2. Iba `E0` a úplne zmapovaný `E1` môžu vylúčiť podtriedu pred konštrukciou
   funkcie. `E2` je povinný comparator/nulový limit, nie automatický STOP;
   jeho samostatná nezhoda je `REFERENCE_MISMATCH_ONLY`. `E3` je vodidlo,
   nie dôvod smrti.
3. Pri `E1` sa povinne zapisuje confidence level, štatistická a systematická
   chyba, sektor/znamienko, jednotky a mapovanie model -> observabla.
4. Takéto predbežné vylúčenie dostane `PRECHECK_EXCLUDED_SCOPE` a
   `NO_CANDIDATE_RUN`. Je platné iba v presne certifikovanom priestore,
   nepridáva kanonickú hĺbku a nesmie sa sumarizovať ako
   `COMPUTED_STOP_SCOPE`.
5. Až úplný predregistrovaný fyzikálny výpočet je `COMPUTED_STOP_SCOPE`; až
   úplná model -> observabla -> likelihood reťaz je
   `OBSERVATIONAL_STOP_SCOPE`. Technický incident zostáva `TECHNICAL_STOP`.

## WORKING-TECH-INCIDENT-NONCONSUMPTION — technická chyba nespotrebuje fyzikálny pokus

**Prijaté používateľom:** 2026-07-16  
**Stav:** záväzné pracovné pravidlo bez nového AR čísla, kým je register
identifikátorov zamknutý.

Kontrola duplicity: error ledger už oddeľuje parser, import, timeout,
serializáciu a chybu nástroja od fyzikálneho výsledku. AR67 zakazuje zabiť
koľaj iba timeoutom alebo parserom. Chýbala však explicitná veta, že tieto
incidenty nespotrebujú počet fyzikálnych pokusov a nemôžu vyčerpať koľaj.

Za fyzikálny pokus sa počíta iba beh alebo analytický balík, ktorý:

1. implementuje predregistrovanú fyziku, celý povinný stav a rovnice;
2. technicky dobehne s platnou provenienciou, konečným výstupom a bez známej
   formálnej chyby;
3. má dostatočné holdouty a konvergenciu na interpretáciu fyzikálneho
   PASS/STOP kritéria;
4. zlyhá alebo prejde na fyzikálnom zákone, invariantnej matematickej
   podmienke alebo predregistrovanom observačnom rozsahu.

Syntax, import, timeout, chýbajúca závislosť, marker, nesprávny register,
zlá state/RHS parita, serializácia, jednotky, adapter, cache, cesta,
nesprávne prepísaný vzorec alebo iná implementačná chyba sú technické
incidenty. Musia sa zapísať do error ledgeru, chybný artefakt sa zachová a
označí a oprava musí prejsť preflightom. Nespotrebujú fyzikálny pokus,
nesmú vydať fyzikálny STOP a nesmú zabiť ani natrvalo zablokovať rodičovskú
koľaj.

Neexistuje pevný počet technických opráv. Opakovanie rovnakej triedy chyby
vynúti architektonickú kontrolu, zdieľaný base test alebo výmenu technickej
cesty, nie smrť fyziky. Aby nevznikali stovky runnerov, preferuje sa jeden
verziovaný base, jeden stabilný runner a nové immutable run ID; nový
fyzikálny suffix vzniká iba po zmene rovníc, mechanizmu alebo fyzikálneho
rozsahu.

Toto pracovné pravidlo obmedzuje historickú vetu AR66/AR67 o „najviac dvoch
technických opravách“. Pôvodný text zostáva zachovaný ako história. Jeho
rozpočet sa odteraz smie čítať iba ako najviac dva vopred odlíšené
**fyzikálne** varianty/pokusy v danom balíku, nie ako cap syntaktických,
runtime alebo implementačných opráv.

### Neskoršie spresnenie používateľa — technický cap 10

Veta „neexistuje pevný počet technických opráv“ bola ešte 2026-07-16
spresnená: jedna konkrétna technická implementačná vetva má najviac
**10 technických pokusov**. Každý pokus musí mať poradové číslo, vstup,
výsledok a dôvod zlyhania v route-local technickom ledgeri.

Po desiatom technickom neúspechu dostane iba táto implementačná vetva stav
`TECHNICAL_STOP`. Záznam musí jednoznačne uviesť aspoň jednu príčinu:

- `SCRIPT_IMPLEMENTATION_FAILURE` — nepodarilo sa vytvoriť skript, ktorý
  prejde preflightom a stabilne dobehne;
- `PYTHON_OR_DEPENDENCY_FAILURE` — interpreter, balík alebo runtime;
- `SANDBOX_OR_ENVIRONMENT_FAILURE` — sandbox, oprávnenie alebo hostiteľské
  prostredie;
- `BUILD_OR_ADAPTER_FAILURE` — kompilácia, väzba alebo externý backend.

`TECHNICAL_STOP` nie je fyzikálny STOP. Rodičovská fyzikálna koľaj zostáva
`REVIEW_TECHNICAL_UNRESOLVED`; jej mechanizmus sa nesmie označiť za mŕtvy.
Pokračovať možno inou vopred zdokumentovanou technickou architektúrou s
novým vlastným ledgrom `0/10`, ale bez zmeny fyzikálneho suffixu, pokiaľ sa
nemenia rovnice, mechanizmus ani rozsah. Týmto spresnením sa nahrádza iba
predchádzajúca veta o neobmedzenom počte technických opráv; ostatné časti
pravidla zostávajú platné.

Každý spustený predregistrovaný technický balík zaberá jedno poradové miesto
`n/10`, či skončí technickým FAIL alebo scoped PASS. Compile a `--help` v
rámci toho istého balíka nie sú samostatné pokusy. Ak desiaty balík
neuzavrie technickú vetvu, dostane `TECHNICAL_STOP`; dôvod rozlíši chyby
predchádzajúcich balíkov a stav desiateho.

Counter sa nesmie vynulovať premenovaním runnera, base alebo technického
suffixu. Nový `0/10` je dovolený iba po differential audite, ktorý dokáže,
že nová architektúra nerieši tú istú implementačnú problémovú líniu a
nezdedila jej chybný contract. K4 R-A preto konzervatívne zdedila pokusy
1–3; K11 full-v002 začala `0/10`, pretože starý S0-v001 bol iba odlišný
formula-regression register a differential audit zmrazil úplne nový
multispecies/thermal/TCA/DAE kontrakt.

### Najnovšie spresnenie používateľa — počíta sa séria technických zlyhaní

**Prijaté:** 2026-07-16. Toto spresnenie nahrádza iba staršie vety, podľa
ktorých každý vecný balík doživotne obsadil miesto `n/10` a úspech nemohol
counter vynulovať.

Aktívny counter znamená počet **po sebe idúcich technických zlyhaní** tej
istej koľaje/podkoľaje a implementačnej problémovej línie. Po každom vecnom
výpočte, ktorý technicky dobehne, má platnú provenienciu, neobsahuje známu
formálnu chybu a prinesie aspoň čiastočný interpretovateľný výsledok, sa
aktívny counter vynuluje na `0/10`. Platí to bez ohľadu na to, či fyzikálny
výsledok skončí scoped PASS, REVIEW alebo invariantným STOP; úspešný výpočet
je technicky úspešný aj vtedy, keď fyziku vyvráti.

`py_compile`, `--help`, smoke, parser/CLI test, hash-only kontrola, prázdny
diagnostický beh alebo testovací skript bez nového čiastočného výsledku
counter **nevynuluje**. Rovnako ho nevynuluje iba premenovanie súboru alebo
architektúry. Route-local ledger musí preto viesť dve odlišné veličiny:

```text
historical_packages_total      — nemenná auditná história,
consecutive_technical_failures — aktívny cap 0..10.
```

Pri `10/10` po sebe idúcich technických zlyhaniach vznikne
`TECHNICAL_STOP` danej implementačnej línie. Staršie zlyhania sa nemažú ani
po resete; zostávajú s príčinami v histórii. Fyzikálny pokus a fyzikálna
smrť sa naďalej posudzujú výlučne podľa bodov 77–93.

## WORKING-TASK-AND-AGENT-BOUNDARY — delenie úloh bez straty autority

**Prijaté používateľom:** 2026-07-16 ako pracovná organizačná zásada bez
nového AR čísla.

Samostatná hlavná úloha sa vytvorí pre fyzikálne nezávislý pracovný balík,
nie automaticky pre každý suffix, mód, parameter alebo technickú opravu.
Nová úloha je opodstatnená, ak balík má vlastný stavový/rovnicový kontrakt,
vlastný PASS/REVIEW/STOP bod, možno ho auditovať prevažne nezávisle a bude
produkovať viacero vecných behov alebo rozsiahlu dokumentáciu.

V jednej úlohe zostávajú atómy, ktoré používajú rovnaké rovnice a líšia sa
iba módom, `k`, variantom, toleranciou alebo supportom. Orchestrátor drží
autoritatívne registre, udeľuje verdikty a prenáša medzi úlohami iba
zmrazený handoff: cieľ, povinné vstupy/hashes, mantinely, aktuálny stav a
presnú definíciu hotového výsledku.

Subagenti sa používajú prednostne na ohraničené read-only úlohy: hash a
manifesty, link/ID kontrolu, indexovanie, log/JSON triage, source-lineage a
nezávislé posudky. Fyzikálne odvodenie, zmena vzorca, výber mechanizmu a
PASS/REVIEW/STOP zostávajú na hlavnom reasoning agentovi. Paralelné
write-heavy úlohy sa nepoužijú tam, kde by mohli editovať rovnaké súbory.

## Otvorené pracovné body

- dokončiť klasifikáciu historických párov `05` bez zmeny ich obsahu;
- vyriešiť potvrdené kolízie AR8, AR9, AR37–39, Q20, Q64–67 a Q72 podľa
  `tracks/METHODOLOGY/00_IDENTIFIER_COLLISION_LEDGER.md`; dovtedy neprideľovať
  ďalšie globálne AR/Q číslo;
- pri vytvorení Git baseline pripraviť presnú migračnú mapu;
- pred v3.18 zostaviť jeden konsolidovaný SK/EN release register namiesto
  reťazca tematických dodatkov.
