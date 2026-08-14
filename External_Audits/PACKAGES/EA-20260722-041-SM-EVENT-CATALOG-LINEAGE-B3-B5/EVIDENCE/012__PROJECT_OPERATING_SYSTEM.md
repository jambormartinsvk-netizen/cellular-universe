# Operačný systém projektu — roly, handoffy a lifecycle

**Stav:** `ACTIVE / COMPRESSION_SAFE / NO_SCIENTIFIC_VERDICT`  
**Dátum:** 2026-07-22  
**Autor teórie:** Martin Jambor  
**Procesný vlastník:** hlavný orchestrátor  
**Účel:** zachovať spôsob práce aj po kompresii kontextu a zabrániť
opakovaniu známych dokumentačných, Python a auditných chýb.

Tento dokument neurčuje aktuálny fyzikálny stav. Ten je iba v
`tracks/00_CURRENT_EXECUTION_PLAN.md` a v najnižšom route-local result/work
ledgeri. Chatové súhrny sú iba navigačná pomôcka.

## 1. Autoritatívne poradie

Pri konflikte sa používa toto poradie:

1. výslovné aktuálne rozhodnutie autora teórie v povolenom rozsahu;
2. pracovná metodika a bezpečnostné/provenance registre;
3. `tracks/00_CURRENT_EXECUTION_PLAN.md` pre globálny živý stav;
4. najnižší route-local contract, preregistrácia a immutable raw;
5. prijatý hlavný posudok externého alebo interného auditu;
6. staršie plány, README, chat a historické dokumenty.

Nižšia vrstva nesmie potichu zmeniť vyššiu. Historický súbor sa neopravuje
prepisom; nová interpretácia patrí do nového assessmentu alebo registra.

## 2. Sekvenčné roly

Osem rolí neznamená osem súbežných agentov. Aktivujú sa podľa fázy a
naraz pracujú najviac traja bez prekrývajúcich sa write scopes.

| Rola | Konfigurácia/vlastník | Smie | Nesmie | Povinný handoff |
|---|---|---|---|---|
| autor teórie | Martin Jambor | zvoliť fyzikálny mechanizmus, definície a nové vstupy | byť nahradený agentovým odhadom | autor-input contract orchestrátorovi |
| hlavný orchestrátor | hlavná úloha | zmraziť scope, povoliť run, vykonať bounded preflight/official, prijať audity, zapísať verdict a centrálne registre | meniť frozen prereg, predstierať nezávislý audit, vymyslieť chýbajúcu fyziku | task capsule každej ďalšej role |
| Python script author | `python_script_author.toml` | editovať iba pridelený base/runner podľa draftu preregistrácie | spustiť project Python, meniť rovnice/prahy/prereg/raw/verdikt | source map, diff scope a SHA script auditorovi |
| Python/math script auditor | `math_script_auditor.toml` | read-only overiť vzorce, code path, guards, schému a provenance | editovať kód, spustiť project Python alebo official, prideliť verdict | `RECOMMEND_STATIC_SCRIPT_AUDIT_PASS` alebo presný blocker orchestrátorovi |
| interný vedecký auditor | `physics_track_auditor.toml` | read-only posúdiť raw, zákony, scope, holdouty a nonclaims | meniť raw/kód/prahy, zvoliť mechanizmus alebo udeliť projektový verdict | scoped odporúčanie orchestrátorovi |
| dokumentačný/release steward | `documentation_release_steward.toml` | read-only nájsť stale stavy, odkazy, count, SK/EN a release rozpory | fyziku, editáciu alebo verdict; opravy vykoná orchestrátor jedným batchom | checklist opráv a dotknutých ciest |
| kurátor externého balíka | `external_package_curator.toml` | zostaviť nový balík iba z approved exact artefaktov, manifestu a runtime mapy | opravovať dôkaz, písať auditný názor alebo meniť sealed package | preflight, štyri county, seal handoff externému auditorovi |
| externý auditor | `external_auditor.toml` | pracovať nad sealed package/fresh copy a zapísať response audit | čítať live projekt mimo scope, editovať package alebo udeľovať projektový verdict | T1/T2/T3 odporúčanie hlavnému orchestrátorovi |

Dokumentačný steward je zámerne read-only: zabraňuje tomu, aby ten istý
agent súčasne rozhodol stav, prepísal registre a sám si potvrdil správnosť.
Hlavný orchestrátor aplikuje jeho presný batch a následný steward/reviewer ho
overí.

## 3. Povinný task capsule

Kapsul je stavový kontrakt, nie voľný prompt. Vkladá sa do pripravovanej
preregistrácie alebo existujúceho append-only route ledgera:

```text
TASK_ID:
ROUTE:
ROLE:
ROLE_CONFIG_SHA256:
ASSIGNED_AGENT_TASK_ID:
ARTIFACT_AUTHOR_TASK_ID:
STATIC_AUDITOR_TASK_ID:
INTERNAL_AUDITOR_TASK_ID:
PACKAGE_CURATOR_TASK_ID:
EXTERNAL_AUDITOR_TASK_ID:
SEPARATION_OF_DUTIES_CHECK:
CURRENT_PHASE:
PARENT_DECISION:
CLAIM:
NONCLAIMS:
ALLOWED_NEXT_ACTION:
ALLOWED_READS:
ALLOWED_WRITES:
FORBIDDEN_ACTIONS:
IMMUTABLE_INPUT_PATHS_AND_SHA256:
FROZEN_EQUATIONS_AND_THRESHOLDS:
PREREG_SHA256:
RULESET_PATHS_AND_SHA256:
AUDITOR_RULESET_PATHS_AND_SHA256:
AUDITOR_ROLE_CONFIG_SHA256:
RUN_AUTHORIZED: false
TIMEOUT_AND_OUTPUT_GUARDS:
OUTPUT_PATHS:
LIVE_FILE_BUDGET:
DONE_WHEN:
NEXT_ROLE:
```

Pred freeze môže mať `PREREG_SHA256=PENDING`, ale `RUN_AUTHORIZED` musí byť
`false`. Po freeze sa SHA zapíše do samostatného immutable receiptu alebo
append-only registra; samotná preregistrácia sa už nemení.

Po kompresii agent znovu načíta kapsul a pravidlá. Chýbajúce pole, zmenený
hash alebo nejasný next action znamená
`HANDOFF_OR_RULESET_DRIFT_REVIEW / NO_RUN`.

Orchestrátor a pridelená rola pred prácou overia actual role-config SHA voči
kapsule aj `.codex/agents/00_MANIFEST.md`. Zakázaná rovnosť identity autora
a jeho script/internal auditora alebo package kurátora a external auditora
znamená `SEPARATION_OF_DUTIES_FAILURE / NO_RUN`. Pole
`SEPARATION_OF_DUTIES_CHECK` nesmie byť iba tvrdenie: uvedie porovnané task
identity a výsledok každej nerovnosti.

## 4. Fail-closed lifecycle jedného výpočtového atómu

```text
CONTEXT_RELOADED
  -> PHYSICS_CONTRACT_DRAFTED
  -> SOURCE_IMPLEMENTED_NO_PYTHON
  -> STATIC_SCRIPT_AUDIT_ACCEPTED_BY_ORCHESTRATOR
  -> PREREG_FROZEN_AND_RECEIPTED
  -> BOUNDED_PREFLIGHT_PASSED
  -> OFFICIAL_PUBLISHED_ONCE
  -> INTERNAL_SCIENCE_AUDITED
  -> MAIN_ORCHESTRATOR_ASSESSED
  -> DOCUMENTATION_BATCH_VERIFIED
  -> PACKAGE_CURATED_AND_SEALED (iba ucelená časť)
  -> EXTERNAL_AUDIT_ASSESSED
```

Žiadna rola sa sama nepovýši do ďalšej fázy. Handoff overí orchestrátor.

### 4.1 Fyzikálny contract a draft preregistrácie

Pred implementáciou sa určia rovnice, stav, poradie, jednotky, gauge,
vstupy, thresholdy, vetvy PASS/REVIEW/STOP, nonclaims, holdouty, nulové
limity a output guard. Neznámy fyzikálny vstup sa neodhaduje; vracia sa
autorovi teórie.

### 4.2 Autor skriptu

Autor vytvorí najviac jeden versioned base a jeden tenký runner v pridelených
cestách. Musí zachovať ownership registra a uviesť všetky runtime-opened
vstupy, explicitné state order, CLI, internal deadline, external timeout,
exclusive publish, temp cleanup a machine-readable failure receipt.

Autor nespúšťa project Python. Odovzdá source SHA a implementačnú mapu
nezávislému script auditorovi.

### 4.3 Statický script audit

Auditor načíta celý error ledger, nie iba starší known-pattern checklist.
Exact celý názov runnera aj importovaných predchodcov vyhľadá v živom DNR
registri. Historický checker môže pomôcť, ale jeho `NOT_IN_QUARANTINE` nikdy
neudeľuje run permission.

Auditor read-only overí najmä:

- formula/source lineage, znamienka, jednotky a state/RHS parity;
- skutočnú generated/executed cestu, markery a reachability;
- explicitné state/register poradie a JSON key kanonizáciu;
- fail-closed kľúče: existencia, typ, konečnosť a až potom porovnanie;
- realistický JSON payload a native skaláre;
- runtime dependency mapu, missing-input a collision guard;
- rank/worker/aggregate schémy, checkpoint completeness a runtime rezervu;
- rozlíšenie `independent_gate`, `enforced_identity` a monitorov.

Pri blockeri sa Python nespustí. Starý zdroj sa zachová, incident sa zapíše
a autor pripraví versioned successor alebo auditovaný wrapper.

### 4.4 Freeze a preflight

Po prijatí odporúčania `RECOMMEND_STATIC_SCRIPT_AUDIT_PASS` orchestrátor
zapíše stav `STATIC_SCRIPT_AUDIT_ACCEPTED_BY_ORCHESTRATOR`, uzavrie
preregistráciu s final source a input hashmi a jej SHA uloží mimo nej. Až
potom môže orchestrátor vykonať ohraničené fázy:

1. environment/dependency probe;
2. `py_compile`;
3. `--help`;
4. behaviorálny smoke;
5. JSON/output guard;
6. negatívny missing-input alebo collision guard;
7. presne jeden official podľa frozen príkazu.

Každá fáza má externý timeout. Zlyhanie zastaví lifecycle, vytvorí technický
receipt a pred successorom aktualizuje error ledger/DNR. Nie je to fyzikálny
STOP ani automaticky spotrebovaný fyzikálny pokus.

### 4.5 Official a interný audit

Official publikuje success raw presne raz do neprítomného cieľa cez
procesom vlastnený temp a atomic/exclusive publish. Kolízia alebo failure
nesmú prepísať cieľ ani vytvoriť falošný success.

Interný vedecký auditor nemení raw. Overí prereg/source/input/raw SHA,
predregistrovanú vetvu, threshold freeze, zákony, conservation, gauge,
regularitu, kauzalitu, holdouty, konvergenciu, nulové limity a nonclaims.
Jeho záver je odporúčanie. Autoritatívny assessment vydá orchestrátor.

## 5. Dokumentačný closure

Po skutočnej zmene stavu dokumentačný steward pripraví jeden read-only
checklist a orchestrátor vykoná jeden batch. Dynamický globálny stav sa
nešíri do viacerých README:

- `tracks/00_CURRENT_EXECUTION_PLAN.md` — jediný globálny živý stav;
- najnižší route-local plan/result — detail mechanizmu;
- append-only event/error/DNR/package registre — história;
- `tracks/00_READ_FIRST.md` — iba navigácia a pointer na current plan;
- `theory/` — iba release promotion po SK/EN a trigger kontrole.

Každý closure vykáže explicitný zoznam ciest a štyri county z R6. Bežný
atóm zostáva pri piatich vedeckých artefaktoch; agentové posudky sa vkladajú
do jedného interného audit/result dokumentu, nie do nového súboru pre každú
poznámku.

## 6. Externý audit

Balík vzniká až pri ucelenej časti. Orchestrátor zmrazí package charter,
scope, tier, exact artifact list a budget. Kurátor:

1. kopíruje iba approved immutable artefakty;
2. vytvorí single-copy runtime closure, manifest a runtime mapu;
3. vykáže `LIVE_SCIENTIFIC_ARTIFACTS`, centrálne registre, total a package
   copies;
4. spustí R6 preflight a po schválení sealne package;
5. po seal už nič nepridáva.

Externý auditor nesmie byť kurátor toho istého balíka. Číta sealed package,
pri T2/T3 používa fresh copy, zaznamená skutočnú identitu agenta, commands,
exit codes, hashes, tier, deviations a nonclaims. Jeho response je poradná;
hlavný orchestrátor ju prijme, obmedzí alebo odmietne v samostatnom hlavnom
posudku. Sealed audit ani package sa spätne neprepisujú.

Package charter a sealed control vrstva povinne obsahujú exact kópie a hashe
audítorského rulesetu (`AGENTS.md`, tento operating system, R6 protocol a
ďalšie scope pravidlá) a `external_auditor.toml`. Orchestrátor pred sealom
overí live config voči agent manifestu; externý auditor už live projekt
neotvára a overuje iba package kópie. Chýbajúci alebo nezhodný ruleset/config
je `PACKAGE_CLOSURE_BLOCKER / CANNOT_AUDIT`.

## 7. Povinný výstup každej roly

```text
TASK_ID
ROLE / ROLE_CONFIG_SHA256
READ_SET_CONFIRMED
INPUT_HASH_CHECK
FILES_CHANGED (exact paths; 0 pri read-only)
PYTHON_PROCESSES (exact; 0 ak neboli povolené)
FINDINGS_BY_SEVERITY
NONCLAIMS
RECOMMENDATION (non-authoritative)
NEXT_ROLE / DONE_WHEN
```

Takto sa projekt obnovuje zo súborov, hashov a fázového handoffu, nie z
toho, čo si model pamätá pred kompresiou.
