# Externý audit — mapa čítania a skladanie dôkazových balíkov

- Stav dokumentu: `ACTIVE_HANDOFF_GUIDE`
- Dátum: `2026-07-17`
- Trasa: `A1-K1 / A2-K4 / P5`
- Autorita: balíky pripravuje hlavný orchestrátor; externý auditor je read-only
- Účel: umožniť posielať na externý audit malé, samostatne overiteľné časti bez straty kontextu
- Tento dokument: nemení fyzikálny stav, skóre ani verdikt žiadnej koľaje
- Prevádzkový protokol balíkov a odpovedí: `External_Audits/00_AUDITOR_PACKAGE_PROTOCOL_SK.md`

## 1. Základné pravidlo

Externému auditorovi sa neposiela celý projekt bez mapy. Pošle sa:

1. raz spoločný orientačný balík `P0`;
2. raz aktuálny route snapshot `P1`;
3. jeden presne vymedzený dôkazový balík konkrétnej otázky;
4. až na vyžiadanie jeho staršie závislosti alebo širšia história.

Každý vstup autora teórie je hypotéza, kým neprejde auditom. Kandidátsky verdikt vypísaný skriptom nie je projektový `PASS/REVIEW/STOP`. Autoritatívny verdikt zapisuje iba hlavný orchestrátor.

Mŕtve koľaje, neúspešné skripty a staršie formulácie sa nemažú. Auditor musí dostať aj neskorší dokument, ktorý staršie tvrdenie obmedzil, opravil alebo zrušil.

## 2. Kde sa nachádza aký druh informácie

| Adresár | Význam | Ako ho čítať |
|---|---|---|
| `theory/` | hlavné publikované alebo už prijaté dokumenty teórie | nie je pracovným scratch priestorom |
| `tracks/` | živý stav trás, pracovné plány, preregistrácie, lokálne audity a história | hlavný zdroj aktuálneho pracovného stavu |
| `scripts/baseScripts/` | zdieľané implementácie rovníc a kontrol | najprv auditovať rovnicu tu, potom runner |
| `scripts/` | ohraničené runnery konkrétnych testov | overiť import, parametre, limit a presnú volanú base verziu |
| `scripts/results/` | strojové výsledky, najmä immutable JSON | číselné tvrdenia čítať priamo z JSON, nie z parafrázy |
| `Audit/` | projektové a prierezové audity | skontrolovať dátum, scope a či ich neobmedzil novší audit |
| `Independent_Audits/` | samostatné provenienčné alebo tematické audity | vhodné pre audit pôvodu vzorcov |
| `External_Audits/` | odovzdávacie mapy a diskusné vlákna externých auditov | externý posudok sám nemení projektový verdikt |
| `Questions/` | skratky, identifikátory, otázky a navigácia | význam ID áno; fyzikálny stav vždy overiť v route dokumentoch |

`tracks/00_READ_FIRST.md` a staršie indexy sú užitočné ako navigácia, ale môžu obsahovať historický snapshot. Aktuálny stav má prednosť v `tracks/00_CURRENT_EXECUTION_PLAN.md` a v novšom route-local výslednom audite.

## 3. Precedencia dôkazov

Neexistuje jedna univerzálna „posledný súbor vždy vyhráva“ precedencia. Rozhoduje typ tvrdenia:

1. **Integrita balíka:** presný path a SHA-256. Nezhoda hashu znamená `CANNOT_AUDIT`, nie fyzikálny nesúhlas.
2. **Otázka, očakávanie, prahy a rozhodovací strom:** preregistrácia vytvorená pred behom. Neskorší text ich nesmie spätne zmeniť.
3. **Implementovaná fyzika a matematika:** verzovaný base modul a jeho deklarované zdroje.
4. **Čo sa naozaj volalo:** runner, CLI parametre, defaults a execution ledger.
5. **Číselné hodnoty a raw kontroly:** immutable JSON. Pri rozpore s prose má číslo z JSON prednosť.
6. **Autoritatívny verdikt v danom scope:** výsledný auditný Markdown hlavného orchestrátora.
7. **Aktuálny stav a ďalší krok:** lokálny work plan, nadradený track a globálny current plan.
8. **Obmedzenie staršieho tvrdenia:** novší explicitný erratum/limitation dokument mení jeho aktuálnu interpretáciu, ale pôvodný artefakt zostáva historickým dôkazom.

## 4. Povinná logika čítania jedného výpočtu

Auditor má čítať vrstvy v tomto poradí:

```text
scope a nonclaims
  -> preregistrácia a zmrazené prahy
    -> zdroj vzorca / formula provenance
      -> base modul a jeho verzia
        -> runner, parametre a limity
          -> immutable raw JSON
            -> execution ledger
              -> výsledný audit a projektový verdikt
                -> neskoršie limitation/erratum a route stav
```

Pri audite, či sa pôvodná formulácia nestratila v nižšom skripte, treba pre každý podstatný vzorec vytvoriť tento ledger:

| Vrstva | Povinná otázka |
|---|---|
| fyzikálny zdroj | Aký je presný vzorec, gauge, konvencia znamienok, jednotky a scope? |
| odvodenie | Ktoré aproximácie a limity boli použité? |
| base modul | Je výraz implementovaný presne, bez zameneného koeficientu, znamienka alebo premennej? |
| runner | Importuje správnu verziu a neprepisuje vzorec lokálnou kópiou? |
| parametre | Sú CLI hodnoty, defaults a jednotky rovnaké ako v preregistrácii? |
| raw výsledok | Potvrdzuje JSON, že sa použila deklarovaná konfigurácia a zdrojové hashe? |
| verdikt | Aplikuje audit pôvodný zmrazený prah bez post-hoc zmäkčenia? |
| neskorší audit | Nebolo tvrdenie následne obmedzené alebo zrušené? |

## 5. Režimy externého auditu

### 5.1 Slepý audit

Auditor dostane scope, preregistráciu, fyzikálny zdroj, base modul, runner a raw JSON. Výsledný projektový verdikt sa mu ukáže až po odovzdaní jeho vlastného záveru. Tento režim znižuje confirmation bias.

### 5.2 Forenzný audit

Auditor dostane aj execution ledger, výsledný audit, route stav a históriu. Tento režim skúma správnosť projektového rozhodnutia a dokumentačnú konzistenciu.

### 5.3 Reprodukčný audit

Auditor dostane celý dependency closure, verziu Pythonu/knižníc, príkaz behu a immutable JSON. Má vytvoriť vlastný výsledok, nie iba čítať náš.

## 6. P0 — spoločný orientačný balík

P0 sa jednému auditorovi posiela iba raz. Povinné súbory:

1. `External_Audits/A1/A1K1/A2/A2K4/P5/00_EXTERNAL_AUDIT_HANDOFF_SK.md`
2. `tracks/00_CURRENT_EXECUTION_PLAN.md`
3. `tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md`
4. `tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md`
5. `Questions/00_ABBREVIATION_AND_IDENTIFIER_REGISTER_SK.md`
6. `Audit/00_MULTI_AUDITOR_ROLE_CONTRACT_2026-07-16.md`
7. `Audit/00_PRAVIDLO_vsetky_vstupy_autora_su_hypotezy.md`

Ak auditor kontroluje Python, doplniť:

8. `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`
9. `scripts/00_KNOWN_PYTHON_ERROR_PATTERNS.md`
10. `scripts/00_EXECUTION_TIME_LIMITS.md`
11. `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md`
12. `scripts/baseScripts/00_MODULE_OWNERSHIP_REGISTER.md`
13. `scripts/baseScripts/00_VERSION_REGISTER.md`

Anglické ekvivalenty sa pridávajú iba auditorovi, ktorý ich potrebuje. Pracovné metodické pravidlá sa berú z `tracks/METHODOLOGY/`; historické pomocné súbory `05...` v `theory/` sa nesmú zameniť za aktuálny pracovný register.

## 7. P1 — aktuálny stav trasy A1-K1 / A2-K4 / P5

Tento balík umožňuje overiť, prečo sa rieši práve P5, čo už bolo rozhodnuté a čo ešte chýba:

1. `tracks/00_ROUTE_REGISTER.md`
2. `tracks/A1/A1K1/A2/00_TRACK_REGISTER.md`
3. `tracks/A1/A1K1/A2/A2K4/00_TRACK.md`
4. `tracks/A1/A1K1/A2/A2K4/00_WORK_PLAN.md`
5. `tracks/A1/A1K1/A2/A2K4/00_SCORECARD.md`
6. `tracks/A1/A1K1/A2/A2K4/HISTORY/00_EVENT_LEDGER.md`
7. `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_WORK_PLAN.md`
8. `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_ARTIFACT_INDEX_SK.md`
9. `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/BASE/00_BASE_DEPENDENCIES.md`
10. `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/RUNNERS/00_MANIFEST.md`
11. `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/RESULTS/00_MANIFEST.md`
12. `scripts/results/k_mpc_005/00_RESULTS_INDEX_P5_SK.md`

P1 je mutable snapshot. Pri každom externom odovzdaní sa jeho súbory hashujú nanovo; starý odovzdaný manifest sa potichu neprepisuje.

## 8. P2 — immutable balík KMPC-035

Otázka balíka: audit globálneho `C1` CDI support step 2 v rozsahu `0.3–0.5`. Historický token `C2` v názve súboru neznamená globálny Fourierov koeficient `C2`.

### 8.1 Minimálny čitateľský balík

| Rola | Súbor | SHA-256 |
|---|---|---|
| prereg | `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/60_KMPC_035_CDI_C2_SUPPORT_03_05_LADDER_PREREGISTRATION_SK.md` | `78EFE7FAD691032FD7885665FE66A616E32B244ED32B4D66E6AD523DB05A1F9B` |
| execution | `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/61_KMPC_035_CDI_C2_EXECUTION_LEDGER_SK.md` | `0285DE0104D9A94D4101BB071C4F72DBFC27BF59AA74452CF6C8A07466C899DE` |
| verdict | `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/62_KMPC_035_GLOBAL_C1_CDI_SUPPORT_STEP_2_RESULT_AND_AUDIT_SK.md` | `0F5ECE8192F95FEFF57811CF1D6EB411C53B15CADD18060F6BB6B4AA73FE9765` |
| runner | `scripts/279_script_KMPC_035_P5_3g7_CDI_C2_support_03_05_ladder.py` | `09F86A2A6E8BA81F4F41C73722BC40264888D1EF45BB4016F223A5E2C76649E3` |
| direct base | `scripts/baseScripts/p5_general_synchronous/cdi_support_ladder.py` | `A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068` |
| raw result | `scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json` | `A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01` |

Mutable stavový doplnok: `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/P5_3G7_CDI_C2_TECHNICAL_ATTEMPT_LEDGER.md`. Jeho hash sa vyráta pri odovzdaní a označí sa `MUTABLE_REGISTER_SNAPSHOT`.

### 8.2 Úplný dependency closure pre reprodukciu

Všetky nasledujúce cesty sú uvedené úplne, aby sa pri odovzdaní nezamenila base verzia:

| Súbor | SHA-256 |
|---|---|
| `scripts/baseScripts/p5_general_synchronous/cdi_c1_coverage.py` | `D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F` |
| `scripts/baseScripts/p5_general_synchronous/cdi_support_ladder.py` | `A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068` |
| `scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py` | `62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D` |
| `scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight_v2.py` | `27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C` |
| `scripts/baseScripts/p5_general_synchronous/full_ra_contract.py` | `F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464` |
| `scripts/baseScripts/p5_general_synchronous/full_ra_m3_seed.py` | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` |
| `scripts/baseScripts/p5_general_synchronous/mode_resolved_puiseux.py` | `5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE` |
| `scripts/baseScripts/p5_general_synchronous/mode_resolved_puiseux_v2_m1_anchored.py` | `5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455` |
| `scripts/baseScripts/p5_general_synchronous/s1_collective_contract.py` | `F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68` |
| `scripts/baseScripts/p5_general_synchronous/s_c0_coefficient_passport.py` | `C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95` |
| `scripts/baseScripts/p5_general_synchronous/s_c0_coefficient_passport_v2_numpy_scalar.py` | `06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11` |

### 8.3 Erratum dependency closure po externom audite balíka 003

Externý audit odhalil, že vyššie uvedený zoznam zachytáva importy, ale
vynechal povinný runtime vstup regresnej brány:

| Runtime vstup | SHA-256 | Povinný pre |
|---|---|---|
| `scripts/results/k_mpc_005/RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json` | `37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20` | `run_smoke` aj `run_audit` KMPC-035 |

Balík `EA-20260717-003-KMPC035-CDI-SUPPORT` sa spätne nemení. Jeho oficiálna
T2 reprodukcia je neuzavretá pre neúplnú dodávku, hoci externá deklarovaná
odchýlka podporila lokálny numerický pattern. Nápravu nesie nový balík
`EA-20260717-005-KMPC035-CDI-SUPPORT-CLOSURE`, ktorý obsahuje runtime mapu,
presnú kópiu KMPC-034 v `REPRO/`, collision-safe publish fixture,
environment metadata a oddelenú cross-platform diagnostiku bez zmeny
zmrazených fyzikálnych prahov.

Od tohto errata sa „úplný dependency closure“ vždy skladá z importov aj zo
všetkých súborov otvorených za behu. Bez strojového package preflightu sa
balík nesmie označiť `READY_FOR_EXTERNAL_AUDIT`.

## 9. P3 — immutable balík KMPC-036

Otázka balíka: audit order-7 proveniencie módu `M1`. Balík neuzatvára vyššiu fyzikálnu bránu a nemení skóre K4.

### 9.1 Minimálny čitateľský balík

| Rola | Súbor | SHA-256 |
|---|---|---|
| prereg | `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/63_KMPC_036_M1_ORDER7_PROVENANCE_GATE_PREREGISTRATION_SK.md` | `A195B5953C74FBF42BDEA9D71197FC93A4DCD1923E549E233BFCA48BE11B3587` |
| execution | `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/64_KMPC_036_M1_ORDER7_EXECUTION_LEDGER_SK.md` | `145EF3EDDE9C2300C977065416D73D74658ACA43B24CB714E6027CD1561D85AA` |
| verdict | `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/65_KMPC_036_M1_ORDER7_PROVENANCE_GATE_RESULT_AND_AUDIT_SK.md` | `21B22E97133B811EBD1CC743EE68861B67B3DC7E42B9B42DEC0059A7DE7F9290` |
| runner | `scripts/280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py` | `EBA6F6D0392F94A511D3D0B9FEFDA07558CB6DE5ED968F0CC02AF6754C2A204B` |
| direct base | `scripts/baseScripts/p5_general_synchronous/m1_order7_provenance.py` | `0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7` |
| raw result | `scripts/results/k_mpc_005/RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json` | `39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497` |

Mutable stavový doplnok: `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/P5_3G7_M1_ORDER7_PROVENANCE_TECHNICAL_ATTEMPT_LEDGER.md`. Jeho hash sa vyráta pri odovzdaní.

### 9.2 Úplný dependency closure pre reprodukciu

| Súbor | SHA-256 |
|---|---|
| `scripts/baseScripts/p5_general_synchronous/m1_order7_provenance.py` | `0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7` |
| `scripts/baseScripts/p5_general_synchronous/mode_resolved_puiseux.py` | `5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE` |
| `scripts/baseScripts/p5_general_synchronous/mode_resolved_puiseux_v2_m1_anchored.py` | `5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455` |

## 10. P4 — audit pôvodu K_MPC a backgroundu

Tento balík je pre otázku, či `K_MPC=0.05`, premenná `k`, palivový člen a univerzálny background boli správne odvodené a prenesené do nižších skriptov. Čítať v poradí:

1. `Independent_Audits/K_MPC_0_05/00_TASK_CHARTER.md`
2. `Independent_Audits/K_MPC_0_05/01_HUMAN_EXPLANATION_SK.md`
3. `Independent_Audits/K_MPC_0_05/03_FUEL_TERM_PROVENANCE_AND_K_ROLE_SK.md`
4. `Independent_Audits/K_MPC_0_05/09_P4_EXACT_A1_BACKGROUND_REDERIVATION_PLAN_AND_SOURCE_AUDIT_SK.md`
5. `Independent_Audits/K_MPC_0_05/10_P4B1_EXACT_A1_COEFFICIENT_LEDGER_SK.md`
6. `Independent_Audits/K_MPC_0_05/11_P4B2A_COVARIANT_K4_SPECIES_LEDGER_SK.md`
7. `Independent_Audits/K_MPC_0_05/12_P4B2B_PROJECTED_TRANSFORMATION_LEDGER_SK.md`
8. `Independent_Audits/K_MPC_0_05/13_P4C_K7_MISSING_UC_EXACT_BACKGROUND_STOP_SK.md`
9. `Independent_Audits/K_MPC_0_05/14_P5_FULL_GENERAL_SYNCHRONOUS_SUCCESSOR_PREREGISTRATION_SK.md`
10. `Independent_Audits/K_MPC_0_05/17_MOBILE_CHAT_FULL_RECONCILIATION_AUDIT_SK.md`
11. `Independent_Audits/Implementation_Lineage/10_FORMULA_PROVENANCE_CHECKLIST_SK.md`

Auditor má osobitne oddeliť:

- homogénny background od Fourierovho módu poruchy;
- fyzikálnu amplitúdu od súradnicového integračného koeficienta;
- historický význam pevnej hodnoty `0.05` od novej hypotézy;
- dokázanú algebraickú canceláciu od stále otvorenej normalizácie;
- fyzikálny STOP od technického alebo dokumentačného blockeru.

## 11. P5 — audit mŕtvej alebo zastavenej koľaje

Pre jednu koľaj sa pošle iba jej lokálny balík:

1. lokálny `00_TRACK.md` alebo ekvivalentný sumár;
2. lokálny `00_WORK_PLAN.md`;
3. lokálny `00_SCORECARD.md`;
4. lokálny `HISTORY/00_EVENT_LEDGER.md`;
5. preregistrácia rozhodujúcej brány;
6. base modul a runner rozhodujúceho výpočtu;
7. raw výsledok a jeho SHA-256;
8. výsledný audit s presným dôvodom smrti/STOP;
9. technický attempt ledger;
10. prípadný neskorší re-audit alebo scope seal.

Pri spätnom audite A2 treba doplniť:

- `Audit/A2_R7_POST_ERROR_SCOPE_SEALS_K1_K2_K3_K5_K6_2026-07-16.md`
- `Audit/A2_analyza_hlavnych_pricin_smrti_kolaji.md`
- `Audit/00_PRAVIDLO_ARCHIVACIE_MRTVYCH_KOLAJI.md`

Auditor musí odpovedať na dve samostatné otázky:

1. Bol rozhodujúci výpočet technicky a matematicky platný?
2. Ak áno, stačí jeho fyzikálny výsledok na označenie koľaje za mŕtvu v deklarovanom scope?

Syntax error, timeout, sandbox problém alebo neschopnosť napísať funkčný skript nie sú fyzikálnou smrťou koľaje.

## 12. P6 — dokumentačný a release audit

Tento balík sa používa iba pri kontrole konzistencie dokumentácie alebo pred vydaním. Obsahuje:

1. `tracks/00_CURRENT_EXECUTION_PLAN.md`
2. `tracks/00_ROUTE_REGISTER.md`
3. príslušné route work plány a scorecards;
4. `Audit/00_ROUTE_AUDIT_INDEX.md`
5. SK aj EN metodický register;
6. SK aj EN register skratiek;
7. aktuálnu tabuľku predpovedí SK aj EN;
8. changelog pripravovanej verzie;
9. mapu verzií, kontrolných súčtov a Zenodo record/DOI;
10. release-trigger ledger vrátane zmeny predikcie.

P6 nesmie ticho prepísať publikované číslo. Zmena potvrdenej predikcie je sama release triggerom a musí byť vysvetlená v changelogu.

## 13. Kontrolný zoznam externého auditora

- [ ] Identifikoval som presné tvrdenie, trasu, dátum a scope.
- [ ] Zapísal som, čo výslovne neauditujem.
- [ ] Overil som SHA-256 všetkých immutable artefaktov.
- [ ] Čítal som preregistráciu pred výsledným verdiktom alebo som priznal, že audit nebol slepý.
- [ ] Overil som rozmery, jednotky, znamienka, gauge a nulové/známe limity.
- [ ] Vystopoval som každý rozhodujúci vzorec zo zdroja cez base modul až do runnera.
- [ ] Overil som CLI hodnoty, defaults, timeout a skutočnú verziu modulu.
- [ ] Skontroloval som, že raw JSON nesie očakávanú konfiguráciu a zdrojové hashe.
- [ ] Použil som zmrazené prahy bez post-hoc zmeny.
- [ ] Oddelil som absolútne a relatívne rezíduum a posúdil numerický floor.
- [ ] Oddelil som technickú chybu, matematickú chybu a fyzikálny rozpor.
- [ ] Vyhľadal som neskoršie limitation/erratum dokumenty.
- [ ] Pri mŕtvej koľaji som overil, že dôvod smrti zodpovedá skutočne testovanému scope.
- [ ] Pri živom výsledku som nevyhlásil viac, než test dokázal.
- [ ] Uviedol som minimálny reprodukčný test každého materiálneho nálezu.

## 14. Šablóna odpovede externého auditora

```markdown
# Externý audit — [packet/run]

- Audit ID:
- Auditor/model/verzia:
- Dátum:
- Read-only: áno/nie
- Audit mode: slepý / forenzný / reprodukčný
- Pakety:
- Overené súbory a SHA: PASS/FAIL
- Chýbajúce alebo zmenené artefakty:

## Rozsah a nonclaims

Auditujem:

Výslovne neauditujem:

## Rekonštrukcia tvrdenia

| Vrstva | Očakávanie alebo tvrdenie | Zdroj path + pole/riadok | Moje overenie |
|---|---|---|---|
| prereg |  |  |  |
| formula/base |  |  |  |
| runner/config |  |  |  |
| raw JSON |  |  |  |
| execution |  |  |  |
| main verdict |  |  |  |
| later limitation |  |  |  |

## Nezávislé kontroly

| Kontrola | Metóda | Očakávanie | Výsledok | PASS/FAIL/NEOVERENÉ |
|---|---|---|---|---|

## Nálezy

### F-001 — [CRITICAL/MATERIAL/MINOR/EDITORIAL]

- typ: FORMAL/NUMERICAL/PHYSICAL/DOCUMENTATION
- presný zdroj:
- pozorované:
- očakávané:
- dopad na scope/verdict:
- minimálny reprodukčný test:
- navrhovaná oprava alebo ďalší krok:

## Neautoritatívne odporúčanie

`AGREE_IN_SCOPE / AGREE_WITH_LIMITATION / DISAGREE / CANNOT_AUDIT`

Odôvodnenie:

Čo by zmenilo moje odporúčanie:

## Trigger kontrola

- score:
- prediction table:
- release:
- Zenodo:

## Vyhlásenie autority

Tento externý posudok nemení projektový PASS/REVIEW/STOP. Autoritatívny zápis vykonáva iba hlavný orchestrátor.
```

## 15. Ako pripraviť odovzdávaný snapshot

Každý odovzdaný balík má mať samostatný názov, napríklad:

```text
EA_KMPC036_ROUND01_2026-07-17
```

Jeho manifest musí obsahovať:

```text
packet_id
generated_at
generated_by=MAIN_ORCHESTRATOR
route=A1-K1/A2-K4/P5
exact relative path
SHA-256
IMMUTABLE alebo MUTABLE_SNAPSHOT
prerequisite packet IDs
main verdict source
nonclaims
score/prediction/release/Zenodo trigger status
```

Hash sa na Windows overí napríklad:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'presna\cesta\suboru'
```

Odovzdané súbory sa neprepisujú a nepremenúvajú. Ak sa mutable register zmení, vytvorí sa nový datovaný snapshot s novým hashom.

## 16. Text, ktorý možno skopírovať externému auditorovi

```text
Si nezávislý read-only auditor teórie Bunkového vesmíru. Každé tvrdenie autora považuj za hypotézu, nie za fakt. Najprv over integritu súborov podľa SHA-256 a čítaj ich v poradí určenom v 00_EXTERNAL_AUDIT_HANDOFF_SK.md. Neudeľuj projektový PASS/REVIEW/STOP; daj iba neautoritatívne odporúčanie AGREE_IN_SCOPE, AGREE_WITH_LIMITATION, DISAGREE alebo CANNOT_AUDIT. Rozlišuj formálnu, numerickú, fyzikálnu a dokumentačnú chybu. Skontroluj, či sa preregistrovaný vzorec bez zmeny dostal cez base modul a runner do raw výsledku, či sa nezmenili prahy po behu a či neskorší audit neobmedzil staršie tvrdenie. Každý materiálny nález podlož presným pathom, poľom/riadkom, výpočtom a minimálnym reprodukčným testom. Výstup vráť v priloženej Markdown šablóne.
```

## 17. Tri prioritné externé audity

### Priorita 1 — P4: `K_MPC`, `k` a univerzálny background

**Prečo prvý:** je to audit základnej separácie homogénneho backgroundu od Fourierových porúch. Ak sa do `H(a)` naozaj preniesla voľba konkrétneho módu `k=0.05`, výsledky nižších K4 runnerov nesmú byť interpretované ako univerzálny kozmologický background. Tento audit je prevažne analytický a provenance-based; nepotrebuje drahý nový beh.

**Čo má rozhodnúť:** či je reťazec
`zdrojový vzorec -> zmena premennej -> amplitúda -> base implementácia -> runner -> background`
bez neprípustnej módovej závislosti a či otvorená normalizácia `A_f` nie je potichu nový fit.

**Pošlite:** `P0 + P1 + P4`. Pre slepý audit možno výsledné STOP dokumenty poslať až po vlastnej rekonštrukcii auditora.

### Priorita 2 — P3: KMPC-036 a numerický floor order-7

**Prečo druhý:** tento test je lokálny, presne zmrazený a jeho tri zlyhania sú veľmi blízko float64 precision floor. Externý numerický audit dokáže relatívne lacno určiť, či ide o chybu implementácie, nesprávne zostavenú rovnicu, alebo o čisto limit presnosti, ktorý vyžaduje iba ohraničený high-precision refinement.

**Čo má rozhodnúť:** či aktuálny `REVIEW` verne zodpovedá dôkazom a aký minimálny následný test môže odlíšiť rounding od fyzikálno-matematického rozporu bez menenia rovníc, parametrov alebo prahov po behu.

**Pošlite:** `P0 + P3`; `P1` iba ak auditor hodnotí aj dopad na celú trasu.

### Priorita 3 — P2: KMPC-035 a CDI support

**Prečo tretí:** tento audit kontroluje rozsah podporného tvrdenia `C1`/CDI v intervale `0.3–0.5`. Je dôležitý pre pokračovanie dôkazu, ale jeho výsledok sám osebe zatiaľ nerozhoduje o fyzikálnej životaschopnosti A2-K4 ani o univerzálnosti backgroundu.

**Čo má rozhodnúť:** či sú algebraické kroky, dependency closure, premenné a rozsah tvrdenia presné a či je správne označenie `[0,3]` remainder ako `REVIEW`, nie ako skrytý `PASS`.

**Pošlite:** `P0 + P2`; `P1` len pri forenznej kontrole ďalšieho kroku.

### Až potom

4. `P1`: konzistencia aktuálneho route stavu, skóre a ďalšieho kroku.
5. `P6`: release audit až pri reálnom release triggeri.

Toto poradie nemení projektový plán ani aktuálnu rozpočtovú pauzu fyzikálnych výpočtov.
