# EA-047 — v3.18 PT1 H0/S8 trojbodová legacy citlivosť

**Stav:** `SEALED_READY_FOR_AUDIT / NOT_SENT`  
**Target tier:** `T2_REPRODUCIBLE_CALCULATION`  
**Autorita:** immutable contracty, RC zdroje, rawy a interný audit; externý auditor iba odporúča  
**Autor teórie:** Martin Jambor  
**PACKAGE_CURATOR_TASK_ID:** `/root`  
**EXTERNAL_AUDITOR_TASK_ID:** `/root/v318_pt1_h0_s8_external_auditor`  
**SEPARATION_OF_DUTIES_CHECK:** `PASS(curator != external auditor; external auditor != RC author)`  
**AUDITOR_ROLE_CONFIG_SHA256:** `98E55F94679F49D4DCE08E3281AE2A38F899B896E25726F9A3C2A85A9FC997E3`  
**RUN_AUTHORIZED:** `false` pre live projekt; sealed package povoľuje iba fresh-copy T2 reprodukciu podľa `03`

```text
CHECKPOINT_ID: CP-RELEASE-V318-PT1-H0-S8-C2C3-20260801-001
ROUTE_AND_GATE: RELEASE/v3.18/PT1_H0/C2-C3
ACCEPTED_STATE: WORKING_ACCEPTED_NINE_CELL_SAMPLED_LEGACY_SENSITIVITY / NOT_RELEASED
PARENT_CHECKPOINT_IDS: NONE_FIRST_RELEASE_DIAGNOSTIC_CHECKPOINT
SUPERSEDES_CHECKPOINT_ID: NONE
CHECKPOINT_STATUS: SEALED_READY_FOR_AUDIT
AUDIT_SUBMISSION_ID: SUB-20260801-047-001 reserved at seal; registration/sent state lives outside immutable package
```

## Súborový rozpočet

```text
LIVE_SCIENTIFIC_ARTIFACTS=27 (5 contracts + 2 RC sources + 19 immutable raws + 1 result/audit dossier)
LIVE_CENTRAL_REGISTERS_UPDATED=4
LIVE_FILES_CHANGED_TOTAL=31
AUDIT_PACKAGE_COPIES=39
RESPONSE_TEMPLATE_FILES=1
NEW_PACKAGE_AND_RESPONSE_FILES_TOTAL=40
```

`BUDGET_EXCEPTION_JUSTIFICATION`: live vedecký počet prekračuje bežných 5,
pretože auditovaný výsledok je explicitná mriežka 3x3 a n=8000 používa
hashovo viazaný reference + A/B/C continuation reťazec. Zlúčenie by zrušilo
immutable hashe a auditnú reprodukovateľnosť. Samotný package ostáva na
štandardnom limite 40 a neobsahuje duplicitnú fyzickú kópiu.

## AUDITOR_RULESET_PATHS_AND_SHA256

```text
EVIDENCE/001__AGENTS.md=472F31C5CAE790EFA16A815BE3183B7A2C1438E4961B2BE4A16AEAE0FF57BA72
EVIDENCE/002__PROJECT_OPERATING_SYSTEM.md=45CDDF6CBD458CC8C18147C438557143E1EB962BB159058070A8CAA7E866921E
EVIDENCE/003__AUDITOR_PACKAGE_PROTOCOL_R8.md=F0F8DB2F7A63666709CCC77E92B80C95F895752E3A16DDF62AA77B0D1D96279C
EVIDENCE/004__EXTERNAL_AUDITOR_ROLE.toml=98E55F94679F49D4DCE08E3281AE2A38F899B896E25726F9A3C2A85A9FC997E3
```

## Presná otázka

Reprodukujú zmrazené contracty a RC v fresh copy všetkých deväť grid-cell
rawov a podporujú iba záver, že legacy pipeline má pri
`Delta N_eff = 0, 0.02675, 0.0535` tri numericky konvergované podmienené
body, pričom endpointový posun je materiálny pre tabuľkovú presnosť, ale
nejde o likelihood, interval ani aktuálnu tvrdú predikciu `H0/S8`?

## Predregistrované rozhodovanie externého auditu

- `PASS_T2_CONDITIONAL_DIAGNOSTIC` iba ak manifest/ruleset/parita prejdú,
  fresh-copy official vetvy dobehnú bez obídenia guardov, po normalizácii
  výlučne top-level `runtime_seconds` sú generated rawy presne zhodné a
  audit zachová všetky nonclaims.
- `REVIEW` pri platformovej odchýlke, neuzavretom runtime, neúplnej
  reprodukcii alebo nejasnom claim reach; nejde automaticky o fyzikálny STOP.
- `STOP_IN_SCOPE` iba pri reprodukovanom matematickom/fyzikálnom rozpore,
  pričom auditor uvedie `S1-S4`, earliest invalid checkpoint a návratový bod.
- Technický pád je `T1_TECHNICAL_NO_CLAIM_REACH`, nie smrť koľaje.

`REQUIRED_PROTOCOL_RESULT_CLASSIFICATION=NONE_OF_FIVE_ACCEPTED_CONDITIONAL_DIAGNOSTIC`
alebo jedna z piatich R8 tried s odôvodnením. Balík sám verdict nepredurčuje.

## Poradie čítania

1. `EVIDENCE/001` až `004` — izolovaný ruleset a rola.
2. `01_MANIFEST_SHA256.md/.tsv`, `04_RUNTIME_DEPENDENCY_MAP.tsv` a
   `06_CHECKPOINT_PROVENANCE.tsv`.
3. `EVIDENCE/005` až `009` — V1 až V5 contract lineage.
4. `REPRO/scripts/393...py` a jeho jediný project import v
   `REPRO/scripts/baseScripts/...py`.
5. `EVIDENCE/010` až `028` — reference, 9 finálnych a 9 continuation rawov.
6. `EVIDENCE/029__RESULT_AND_INTERNAL_AUDIT.md`.
7. `02_AUDITOR_INSTRUCTIONS.md` a `03_REPRODUCTION_AND_EXPECTATIONS.md`;
   reprodukciu vykonať iba v novej dočasnej kópii `REPRO/`.

## Nonclaims

- Nie je to likelihood, posterior, confidence/credible interval, fit ani
  spojitá `Delta N_eff` obálka.
- Nie je to aktuálna tvrdá predikcia `H0` alebo `S8` pre v3.18.
- `H0` je podmienená inverzia voči syntetickej legacy kotve `h_ref=0.673`.
- `S8` dedí zjednodušený rast a `sigma8_LCDM=0.811`; nie je G9 výsledok.
- `Delta N_eff=0` vypína iba legacy paru; nie je LambdaCDM ani mechanizmus-off.
- Bez uzavretia P5.4, G8, G9, covariance, gauge, causality alebo stability.
- Bez zmeny A2-K4, A1-K1, skóre alebo hĺbky a bez autorizácie Zenodo release.
