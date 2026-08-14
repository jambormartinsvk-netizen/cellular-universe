# Projektové pravidlá pre agentov — Teória

Tento súbor je záväzný pre hlavného agenta aj všetkých subagentov v tomto
repozitári. Chat, súhrn po kompresii ani pamäť konkrétneho agenta nie sú
autoritatívnym projektovým stavom.

## Povinný bootstrap

Po otvorení novej úlohy, po kompresii kontextu a pred prvým zápisom vždy
načítaj v tomto poradí:

1. `tracks/00_PROJECT_OPERATING_SYSTEM.md`;
2. `tracks/00_CURRENT_EXECUTION_PLAN.md`;
3. `tracks/00_READ_FIRST.md`;
4. najnižší route-local work plan, preregistráciu a active handoff capsule;
5. `tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md`.

Pred akoukoľvek tvorbou, kontrolou alebo spustením Python artefaktu navyše
načítaj:

1. `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md` — rozhoduje exact celý názov;
2. `scripts/00_KNOWN_PYTHON_ERROR_PATTERNS.md`;
3. celý `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`, pretože checklist je
   starší než najnovšie PF záznamy;
4. `scripts/00_EXECUTION_TIME_LIMITS.md`;
5. `scripts/baseScripts/00_MODULE_OWNERSHIP_REGISTER.md` a
   `scripts/baseScripts/00_VERSION_REGISTER.md`.

Pred prípravou alebo auditom externého balíka navyše načítaj
`External_Audits/00_AUDITOR_PACKAGE_PROTOCOL_SK.md`.

Výnimka nezávislosti: rola `external_auditor` číta iba sealed package a
pravidlá pribalené v ňom. Nesmie kvôli tomuto bootstrapu siahnuť do live
projektu; chýbajúce povinné pravidlo označí ako package-closure blocker.
Package charter preto musí obsahovať `AUDITOR_RULESET_PATHS_AND_SHA256` a
`AUDITOR_ROLE_CONFIG_SHA256`; kurátor vloží exact kópie do sealed balíka.

Ak chýba povinný súbor, nesedí zmrazený hash alebo nie je jednoznačný
`ALLOWED_NEXT_ACTION`, stav je `HANDOFF_OR_RULESET_DRIFT_REVIEW`: nič
nespúšťaj a nič neinterpretuj ako vedecký výsledok.

## Autorita a oddelenie rolí

- Martin Jambor je autor teórie a rozhoduje o nových fyzikálnych vstupoch.
- Hlavný orchestrátor je jediný projektový zapisovateľ autoritatívneho
  `PASS/REVIEW/STOP`, skóre, hĺbky a povolenia `RUN_AUTHORIZED`.
- Subagent vydáva odporúčanie v rozsahu svojej roly; sám nemení verdikt.
- Autor artefaktu nesmie byť jeho jediným auditorom.
- Kurátor externého balíka nesmie vykonať externý audit toho istého balíka.
- Paralelne môžu pracovať najviac traja špecialisti a nesmú mať prekrývajúce
  sa write scopes.

Projektové roly a ich TOML konfigurácie sú v `.codex/agents/`; presný
lifecycle, handoff formát a vlastníctvo sú v
`tracks/00_PROJECT_OPERATING_SYSTEM.md`.

## Python je fail-closed

- Písanie zdroja nie je povolenie spustiť Python.
- Pred prvým Python procesom musí byť hotový nezávislý statický script audit,
  predregistrácia obsahovo uzavretá a jej SHA zaznamenaný v samostatnom
  pre-run receipte alebo append-only route registri.
- Od prvého Python procesu sa preregistrácia už neupravuje.
- Starý quarantine checker nie je autorita pre nové skripty. Jeho
  `NOT_IN_QUARANTINE` nikdy nenahrádza exact vyhľadanie celého názvu v živom
  DNR registri.
- Technická chyba nie je fyzikálny výsledok. Pred successorom sa zapíše do
  error ledgera a podľa potreby do DNR; starý artefakt sa nemaže ani potichu
  neopravuje.
- Official výstup sa publikuje presne raz do neprítomného cieľa; kolízia
  alebo zlyhanie musí skončiť fail-closed.

## Dokumentácia a súborový rozpočet

- Dynamický globálny stav žije iba v `tracks/00_CURRENT_EXECUTION_PLAN.md`;
  `00_READ_FIRST.md` je navigácia, nie druhý stavový register.
- Stav konkrétnej route žije v najnižšom príslušnom work plane/result ledgeri.
- Centrálne registre sa menia jedným batchom až pri zmene autoritatívneho
  stavu, blockeru, uzavretí módu alebo package handoffe.
- Bežný výpočtový atóm má najviac päť live vedeckých artefaktov a ucelený
  closure najviac štyri aktualizované centrálne registre, ak nie je vopred
  zdôvodnená výnimka.
- Pred editáciou oznám plánovaný zoznam/count súborov; po editácii vykáž
  `LIVE_SCIENTIFIC_ARTIFACTS`, `LIVE_CENTRAL_REGISTERS_UPDATED`, total a
  prípadné `AUDIT_PACKAGE_COPIES` osobitne.
- `theory/` je release/historická vrstva. Pracovné zmeny patria do `tracks/`,
  kým hlavný orchestrátor neotvorí release promotion.

## Kompresne odolný handoff

Každá delegácia musí niesť aspoň:

```text
TASK_ID
ROLE
ROLE_CONFIG_SHA256
ASSIGNED_AGENT_TASK_ID
ARTIFACT_AUTHOR_TASK_ID
STATIC_AUDITOR_TASK_ID
INTERNAL_AUDITOR_TASK_ID
PACKAGE_CURATOR_TASK_ID
EXTERNAL_AUDITOR_TASK_ID
SEPARATION_OF_DUTIES_CHECK
ROUTE
CURRENT_PHASE
ALLOWED_NEXT_ACTION
ALLOWED_READS
ALLOWED_WRITES
FORBIDDEN_ACTIONS
IMMUTABLE_INPUT_PATHS_AND_SHA256
PREREG_SHA256
RUN_AUTHORIZED
OUTPUT_PATHS
DONE_WHEN
NEXT_ROLE
```

Kapsul sa vkladá do existujúcej preregistrácie alebo append-only route
ledgera. Samostatný nový súbor vznikne iba pre fyzikálne nezávislú úlohu.
Agent vo výstupe zopakuje task ID, prečítané zdroje, zmenené súbory, vykonané
procesy, nonclaims a odporúčaný handoff. Pri neúplnom kapsule zastaví.

Pred prácou orchestrátor aj pridelená rola prepočítajú hash role configu a
overia:

```text
actual_role_config_sha
  == capsule.ROLE_CONFIG_SHA256
  == .codex/agents/00_MANIFEST.md
```

Pri externom auditorovi túto kontrolu pred sealom vykoná orchestrátor a
kurátor vloží exact config s hashom do balíka; auditor overuje iba package
kópiu. `ARTIFACT_AUTHOR_TASK_ID == STATIC_AUDITOR_TASK_ID`, autor zhodný s
interným auditorom alebo `PACKAGE_CURATOR_TASK_ID == EXTERNAL_AUDITOR_TASK_ID`
znamená `SEPARATION_OF_DUTIES_FAILURE / NO_RUN`.
