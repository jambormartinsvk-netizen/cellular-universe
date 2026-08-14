# Externý audit — EA-20260717-005-KMPC035-CDI-SUPPORT-CLOSURE

## Povinné metadáta

- Auditor/model/verzia: Claude (Anthropic), externý fyzikálno-matematický audit
- Dátum a časová zóna: 2026-07-18, 16:22 UTC
- Audit mode: `REPRODUCTION`
- Package revision a SHA-256 manifestu: `EA-20260717-005`; ľudský manifest pri seale `8685A02D60746471F6FA4946485412C06C23A8172837CBDE660220566B093108` (nerekomputovateľný z plochej kópie, pozri N7); strojový `01_MANIFEST_SHA256.tsv` overený po položkách
- Overenie manifestu: `PASS` — všetkých 24 EVIDENCE kópií aj všetkých 14 runtime ciest má SHA-256 presne podľa oboch máp (`INDEPENDENTLY_RECOMPUTED`)
- Najvyššia dosiahnutá úroveň: `T1_PRIMARY_FORMULA` + deklarované deviácie s plnou rekomputáciou; **official `T2` NEDOSIAHNUTÉ** — official audit vetva z balíka nedobehne (nález N1)
- Oficiálna vetva bez odchýlky: smoke `PASS`; official audit `FAIL` (`TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`, `FileNotFoundError`)
- Deklarované odchýlky: D1 (metriková rekomputácia z raw JSON), D2 (priamy solver bez B1 guardu), D3 (izolovaný rerun B1 algebry s neutralizovaným hash lookupom) — podrobne nižšie

## Prostredie

- OS/architektúra: Linux 6.18.5, x86_64, glibc 2.39
- Python: 3.12.3 (CPython)
- NumPy: 2.4.4
- SciPy/SymPy: 1.17.1 / 1.14.0
- BLAS/LAPACK: scipy-openblas64, OpenBLAS 0.3.31 (USE64BITINT, DYNAMIC_ARCH)

Pôvodné prostredie balíka: Windows, `D:\Teoria`, Python 3.11 — teda toto je skutočná cross-platform reprodukcia.

## Procesný ledger

| Fáza | Presný príkaz | Exit code | Wall time | Output SHA-256 | Stav |
|---|---|---:|---:|---|---|
| manifest preflight | `sha256sum` všetkých 24 EVIDENCE + 14 runtime kópií vs. `01_MANIFEST_SHA256.tsv` a `04_RUNTIME_DEPENDENCY_MAP.tsv` | 0 | <1 s | n/a | `PASS` 38/38 |
| smoke | `timeout 10s python REPRO/scripts/281_...py --smoke --max-runtime-seconds 4.8` | 0 | 0.62 s | žiadny JSON (podľa kontraktu) | `PASS`; official smoke PASS; `collision_caught=true`, `target_unchanged=true`, `temp_files_after_collision=[]` |
| official audit | `timeout 10s python REPRO/scripts/281_...py --audit --max-runtime-seconds 4.8 --output scripts/results/k_mpc_005/RUN_EA005_KMPC035_REPRODUCTION_CLOSURE.json` | 2 | 0.87 s | failure JSON `78E8E11E5ED98F327FADFF018559618D9012BEFCCBB40C3B93FC5B8E855621DC` | `FAIL` — `FileNotFoundError: .../REPRO/scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py`, phase `OFFICIAL_AUDIT_UNCHANGED_THRESHOLDS`; generated success JSON nevznikol |
| official audit (opakovaný) | ten istý príkaz | 2 | 0.58 s | failure preserved | `failure_write_status=PRESERVED_EXISTING_FAILURE_FILE`; nula temp súborov — F5 oprava behaviorálne potvrdená |
| declared deviation D1 | rekomputácia regresie/common/tail z `010`/`011` JSON | 0 | <1 s | n/a | `PASS`, zhoda s dokumentáciou |
| declared deviation D2 | priamy `_standard_state` + `_solve_support` 01/03/05 (obchádza `run_audit` a B1 guard) | 0 | 1.34 s | n/a | 180/180 koeficientov reprodukovaných |
| declared deviation D3 | izolovaný `build_preflight` B1 algebry (hash lookup neutralizovaný, rovnice nezmenené) | 0 | 0.14 s | n/a | všetky exact rezíduá `0` |

## Odpoveď na presnú otázku

1. **Odstraňuje priloženie KMPC-034 JSON blocker F1 a prejdú smoke aj official audit?** Čiastočne. Pôvodný F1 blocker (chýbajúci KMPC-034 JSON) je odstránený — smoke vetva prechádza kompletne officiálne. **Official audit vetva však z balíka nedobehne**: `run_audit` volá `b1_guard.build_contract_guard` → `full_ra_b1_preflight.build_preflight`, ktorý runtime-hashuje dva ďalšie súbory relatívne ku koreňu REPRO — `scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py` (očakávaný hash `0F13DA6C...`) a `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md` (`7C927999...`). Ani jeden nie je v balíku, v `EVIDENCE/` ani v `04_RUNTIME_DEPENDENCY_MAP.tsv`. Guardy zlyhali korektne fail-closed (technický failure, žiadny tichý skip), ale ide o **recidívu presne tej triedy chyby (PF-070), ktorú mal tento balík uzavrieť**. `OBSERVED_IN_PRIMARY` + `INDEPENDENTLY_RECOMPUTED` (spustením).
2. **Reprodukuje externá platforma scoped KMPC-035 pattern?** Áno — ale iba cez deklarovanú deviáciu D2, nie cez official vetvu. Všetkých 180 koeficientov sa reprodukovalo; core brány (ranky F0 `4/8/12`, M3 `26/52/78`, driver, holdout, forbidden, `U_c` regularita, M1 order-5 rank 76, condition 340.3) prešli; tail zlyhal **presne** na F0 `delta_f` (`2.524016e-5`) a M3 `sigma_fs` (`3.216708e-3`) pri `z=1e-2` a nikde inde; pri `z=1e-4` prešli oba sektory. `INDEPENDENTLY_RECOMPUTED`.
3. **Zostáva prah `1e-12` nezmenený a `1e-9` iba diagnostika?** Áno. Runner 281 fail-closed kontroluje rovnosť `REGRESSION_REL_TOL/ABS_TOL` s frozen hodnotami; pár `1e-9/1e-13` je iba v `_cross_platform_diagnostic` s `verdict_effect=NONE` a osobitným poľom. Na tejto platforme by mimochodom prešiel aj strict same-machine prah: najhorší bound ratio D2 vs. reference je `0.024` (t.j. drift hlboko pod `1e-12`), zatiaľ čo audítor 003 videl `1.7e-11` — drift je silne závislý od BLAS buildu, čo potvrdzuje správnosť dvojtierového návrhu. `OBSERVED_IN_PRIMARY` + `INDEPENDENTLY_RECOMPUTED`.
4. **Publish wrapper po kolízii?** Áno. Smoke fixture: `collision_caught=true`, `target_unchanged=true`, `temp_files_after_collision=[]`. Navyše behaviorálne overené na reálnej double-failure ceste: opakovaný audit zachoval existujúci failure JSON a nezanechal žiadny `.tmp-EA005-*`. F5 z auditu 003 je uzavretý. `INDEPENDENTLY_RECOMPUTED`.

## Overenie tvrdení

| Tvrdenie | Tag dôkazu | Primárny zdroj path + riadok/pole | Metóda | Výsledok |
|---|---|---|---|---|
| Manifest a runtime hashe sedia (38 položiek) | INDEPENDENTLY_RECOMPUTED | `01_MANIFEST_SHA256.tsv`, `04_RUNTIME_DEPENDENCY_MAP.tsv` | sha256sum všetkých kópií | PASS |
| Immutable regresia 034↔035 (`[0,1]`,`[0,3]`, 90 koeficientov) | INDEPENDENTLY_RECOMPUTED | `010.../solve_result` vs `011.../solved_supports` | vlastný výpočet metriky `abs(new-old) <= max(1e-14, 1e-12·scale)` | worst ratio `0` — exportované mapy sú bitovo identické; JSON `pass=true` potvrdený |
| Common bridge `0..3`: F0 max `1.1548e-14` (`delta_f[3]`), M3 max `6.6107e-13` (`U_f[2]`) | INDEPENDENTLY_RECOMPUTED | `011.../common_coefficient_bridges_03_05` | vlastná rekomputácia z koeficientov | zhoda na všetkých vykázaných čísliciach; hlboko pod `1e-8` |
| Tail FAIL presne 2/30: F0 `delta_f@1e-2`=`2.5240162385e-5`, M3 `sigma_fs@1e-2`=`3.2167075395e-3` | INDEPENDENTLY_RECOMPUTED | `011.../pure_added_tails_45` | rekomputácia všetkých 15 stavov × 2 plochy z raw JSON **aj** z vlastného solve (D2) | identický pattern oboma cestami |
| Tail FAIL nie je artefakt | INDEPENDENTLY_RECOMPUTED | `007__KMPC035_RESULT_AUDIT.md §4` | bases `1.7075e-9`/`4.6216e-10` = `1708×`/`462×` nad `ABS_FALLBACK_NORM`; kancelačné pomery `0.999267`/`0.999112`; `sigma_fs` obálka `1.487e-12 > 1e-12` zlyhá aj absolútne | všetky tri protiargumenty (delenie nulou, kancelácia, conditioning) vyvrátené |
| F3 diagnostiky z auditu 003 | INDEPENDENTLY_RECOMPUTED | `011...` states `sigma_fs@1e-4`, `U_c@1e-2` | would-be relative | `3.2153e-5` (32× nad `1e-6`, prechádza iba absolute vetvou) a `6.2677e-7` (tesne pod prahom) — presne ako deklarované |
| Škálovanie kontaminácie a onset | INDEPENDENTLY_RECOMPUTED | koeficienty `[0,5]` | `|c4/c2|=0.2542`, `|c4/c3|=0.3215`, `|c5/c4|=0.0367/0.0444`; numerický onset `z*≈1.99e-3` (`delta_f`), `1.29e-3` (`sigma_fs`) | potvrdzuje audit 003 §4 |
| Predikcia step 3 | INFERRED_FROM_PROJECT_DOCS + vlastný odhad | geometrická extrapolácia `c6,c7` | kontaminácia `[0,5]` pri `z=1e-2`: `delta_f≈3.4e-12`, `sigma_fs≈6.4e-10` | konzistentné s hypotézou, že `[0,5]` prejde; zostáva hypotéza bez verdict effectu |
| B1 konzervačná/Bianchi algebra | INDEPENDENTLY_RECOMPUTED (D3) | `full_ra_b1_preflight.py` | rerun exaktnej SymPy algebry (hash lookup neutralizovaný, rovnice bajtovo nezmenené) | rezíduá `pressure`, `total_energy`, `total_momentum`, `bianchi_C00`, `bianchi_C0i`, `background_k_cancel`, `conditional_steam_split` všetky exaktne `0`; bez solve/ODE |
| FrozenInputs vnútorná konzistencia | INDEPENDENTLY_RECOMPUTED | `010.../solve_result/inputs`, `S_C0.../weights` | racionálne váhy: `20000000+13834932+242997=34077929` (suma 1 exaktne); `R_nu/R_γ=0.2271·3.046`, `R_s/R_γ=0.2271·0.0535` exaktne; `R_fs=R_nu+R_s` | PASS; hodnoty `h=0.6637`, `ombh2=0.02237`, `omega_m0=0.3517`, `delta`, `lam`, `af` sú podľa pravidla 001 hypotézy, nie tu auditovaná zhoda s dátami |
| 180 koeficientov pre cross-platform diagnostiku | INDEPENDENTLY_RECOMPUTED | `011...` | súčet `(4+26)+(8+52)+(12+78)` | presne 180 |
| Smoke registry-restoration a JSON safety | OBSERVED_IN_PRIMARY + spustenie | `cdi_support_ladder.run_smoke` | official smoke beh | PASS vrátane obnovy registrov po deterministickej výnimke |

## Rozdiely generated JSON voči reference

Official generated JSON nevznikol (N1). Porovnanie preto prebehlo z deviácie D2 proti `EVIDENCE/011`: 180/180 koeficientov, najhorší **bound ratio voči diagnostickému páru `1e-9/1e-13` = `2.4e-3`** (`03/M3/U_fs[0]`) → cross-platform diagnostika by prešla; najhorší strict bound ratio `0.024` → aj frozen prah `1e-12` by na tejto platforme prešiel. Jediné „veľké“ relatívne rozdiely sú znamienkové preklopenia numerických núl rádu `1e-17` (napr. `01/M3/U_c[0]`), správne pokryté absolútnym členom bound formuly.

## Nálezy

**N1 — VYSOKÝ (delivery closure, recidíva PF-070):** Official audit vetva z balíka nedobehne. `full_ra_b1_preflight.py` (riadky 35–41, `EXPECTED_HASHES`) povinne runtime-hashuje `scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py` a `tracks/.../26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md` relatívne ku `parents[3]` modulu — teda ku koreňu REPRO. Tieto súbory v balíku nie sú a runtime mapa ich neuvádza. Podľa protokolu R3 §8 je runtime vstupom aj súbor „otvorený až počas smoke alebo audit vetvy“ — hashovanie je otvorenie. Balík tým porušuje vlastný §12 (statická **aj behaviorálna** closure; povinný negatívny test chýbajúcej závislosti — žiadny taký fixture neexistuje). Koreňová príčina je zjavná z `05_PACKAGE_HISTORY.md`: „Python nebol pri zostavení balíka spustený“ — audit vetva nebola pred sealom nikdy behaviorálne otestovaná v zbalenom strome; PowerShell preflight kontroluje iba enumerované súbory, takže closure chybu tejto triedy principiálne nevie zachytiť. Dôsledok: cieľový `T2_REPRODUCIBLE_CALCULATION` nie je z balíka dosiahnuteľný; ide o druhý po sebe idúci balík s tou istou triedou zlyhania. Fyzikálny záver KMPC-035 to nemení (potvrdený deviáciou), mení to úplnosť dodávky. Poznámka: keďže sa kontroluje presný hash, placeholder nestačí — musí sa dodať pravý súbor.

**N2 — POZITÍVNY:** Smoke vetva je teraz plne officiálne uzavretá; opravy F1 (KMPC-034 v presnej ceste), F5 (`try/finally` + collision fixture, behaviorálne overené aj na double-failure), F6 (environment/BLAS capture) a F2/F3/F4 (oddelené diagnostiky s `verdict_effect=NONE`) sú v runneri 281 implementované korektne a fail-closed.

**N3 — MENŠÍ (numerická konzistencia diagnostiky):** `_tail_scan_for_state` v runneri 281 používa builtin `sum`, kým autoritatívny `_pure_tail` používa `math.fsum`. Pri 2–5 členoch je rozdiel zanedbateľný a z-scan je `DIAGNOSTIC_ONLY`, ale diagnostika by mala byť numericky identická s autoritatívnou definíciou, aby sa hraničné stavy nedali interpretovať dvojako.

**N4 — INFO (definícia tail metriky):** `base_powers = 1..3` vylučuje mocninu `j=0`, hoci support je `[0,3]`. V tomto CDI atóme sú všetky `c0` numerické nuly (≤`1e-16`), takže bez praktického efektu a v súlade s preregistráciou §5.2; pri prenose brány na mód so skutočným `O(1)` `c0` (napr. iná normalizácia isokrivostného stavu) by však `scale` bol podhodnotený a metrika by sa musela predregistrovať nanovo.

**N5 — INFO (reduction diagnostika):** `_tail_reduction_diagnostic` porovnáva najhorší stav starého a nového tailu na každej ploche — potenciálne rôzne stavy (cross-state, nie per-state monotónnosť) a iba M3 sektor. Správne označené `DIAGNOSTIC_ONLY`; hodnoty (redukcia `311×` pri `z=1e-2`, `4.5e8×` pri `z=1e-4`) som reprodukoval.

**N6 — MENŠÍ (runtime mapa):** `04_RUNTIME_DEPENDENCY_MAP.tsv` uvádza `required_by=smoke+audit` paušálne, hoci reálna množina sa líši (reference JSON je iba audit-diagnostic — správne; ale mapa nerozlišuje, že B1 závislosti sú audit-only) a chýba negatívny missing-dependency fixture podľa §12.

**N7 — INFO (tree seal):** Kanonický tree hash `6EAB8B2A...` nie je z plochej kópie rekonštruovateľný (relatívne cesty balíka sa stratili). Všetkých 38 individuálnych hashov sedí; samotný seal preto značím `NOT_VERIFIABLE_FROM_FLATTENED_MIRROR`, nie FAIL.

**N8 — INFO (fyzika/matematika obsahu):** Vecný záver KMPC-035 je matematicky správne odvodený z preregistrovaného rozhodovacieho stromu: regression PASS → core PASS → common PASS → tail FAIL ⇒ `REVIEW_..._REMAINDER_UNCLOSED`, žiadne tiché povýšenie. Konzervačné identity zdieľaného enginu sú exaktne nulové (D3) — to je však vnútorná konzistencia, nie nezávislosť: drivery, holdouty aj B1 zdieľajú jeden equation engine (poctivo priznané), takže spoločná formulačná chyba by prešla všetkými bránami. F4 obmedzenie trvá: dvojčlenná obálka je lokálna nutná, nie postačujúca podmienka konvergencie nekonečného radu; rozpad koeficientov medzi `j=3→4` (`~0.32`) a `j=4→5` (`~0.04`) nie je geometrický, čo plánovaná M1 order-7 brána a step 3 správne testujú.

## Nonclaims a odchýlky

- Tento posudok nič netvrdí o BI/NID/NIV, iných `k`/variantoch, S-M, ODE, G8/G9, CLASS/CMB/BBN, `S8/H0` ani o zhode FrozenInputs s observačnými dátami.
- D2 obchádza `run_audit` a B1 guard (nutné pre N1); jeho výsledok nesie tag `INDEPENDENTLY_RECOMPUTED` iba pre koeficienty, metriky a pattern, **nie** ako official T2 deklarovaného runnera (protokol §13). D3 neutralizuje výlučne hash lookup; symbolické rovnice ostali bajtovo totožné so zapečateným zdrojom (`62D6DEEF...`).
- Rovnaký imported equation engine nie je T3 ani pri exaktnej algebre.
- Predikcia PASS pre `[0,5]` v step 3 zostáva testovateľná hypotéza bez verdict effectu.

## Neautoritatívne odporúčanie

`AGREE_WITH_LIMITATION`

Vecne: potvrdiť existujúci scoped rozsudok `PASS_CDI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY / REVIEW_CDI_SUPPORT_03_REMAINDER_UNCLOSED` — nezávisle reprodukovaný na druhej platforme aj druhom BLAS builde. Procesne: balík EA-005 svoj deklarovaný cieľ (T2 reproduction closure) nesplnil; tier balíka je `T2_UNCLOSED_DELIVERY_SECOND_OCCURRENCE`.

Odporúčaný postup (poradie):

1. **EA-006 (nový NNN):** pribaliť `scripts/88_...ledger.py` a `tracks/.../26_..._SOURCE_MAP_SK.md` v presných runtime cestách + `EVIDENCE/` kópie + oba manifesty; doplniť negatívne missing-dependency fixtures a pravdivé `required_by` (smoke vs. audit) pre každú položku.
2. **Povinný behaviorálny pre-seal beh:** pred `SEALED_READY_FOR_AUDIT` spustiť smoke **aj** audit v čerstvej kópii REPRO na baliacom stroji a zapísať exit codes do `05_PACKAGE_HISTORY.md`. Statický preflight sa dvakrát ukázal ako nedostatočný; navrhujem generovať runtime mapu automaticky z instrumentovaného behu (napr. `sys.addaudithook` na `open`), nie ručnou enumeráciou.
3. **Zníženie krehkosti:** modulové `EXPECTED_HASHES` odkazujúce tri úrovne nad seba viažu „frozen algebru“ na absolútny layout projektu; v novej zmrazenej revízii zvážiť package-safe injektovateľné cesty s explicitným statusom (nikdy tichou editáciou).
4. Pokračovať sekvenciou KMPC-036 (M1 order-7 provenance) → CDI_SUPPORT_STEP_3 podľa dokumentu 62; pri STEP_3 FAIL najprv audit rastu koeficientov a polomeru konvergencie, nie automatické `[0,9]`.
5. Dlhodobo: jednorazová exaktná racionálna rekomputácia (uzavrie FP riziko) a nezávislý row/equation builder (jediná cesta k T3 a k uzavretiu rizika spoločnej formulačnej chyby).

## Celkové zhodnotenie

Matematický a fyzikálny obsah KMPC-035 je v rámci svojho úzko vymedzeného scope robustný: všetkých 180 koeficientov, obe konvergenčné brány, presný dvoj-stavový tail-failure pattern, kancelačné a conditioning protiargumenty, F3 would-be diagnostiky, onset škálovanie aj exaktné konzervačné identity som nezávisle reprodukoval na inej platforme; nič nespochybňuje záver, že support `[0,3]` pri zmrazených prahoch nestačí do `z=0.01`, kým jadro a spoločné koeficienty `[0,3]↔[0,5]` sú stabilné. Guardy sú dôsledne fail-closed a diagnostiky korektne oddelené od verdiktov. Jediná vážna vada je procesná, ale nie kozmetická: balík, ktorého jediným účelom bolo uzavrieť dependency closure, opäť nedodáva úplnú closure pre official audit vetvu — tentoraz pre runtime závislosti skryté o vrstvu hlbšie. Kým sa closure nezačne overovať behaviorálne pred sealom, riziko tretej recidívy je reálne. Projektový `PASS/REVIEW/STOP` týmto posudkom nemením.

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`. Autoritatívne spracovanie vykonáva iba hlavný orchestrátor v novom súbore odpovede.
