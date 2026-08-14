# Externý audit — `EA-20260720-036-KMPC131-C3-NIV-FIRST-REVIEW`

## Povinné metadáta

- Auditor/model/verzia: nezávislý Codex audit agent; GPT-5 family (presná runtime revízia modelu nie je agentovi exponovaná)
- Dátum a časová zóna: 2026-07-22, Europe/Bratislava
- Audit mode: `FORENSIC + REPRODUCTION`
- Package revision: `SEALED_READY_FOR_EXTERNAL_AUDIT`, 2026-07-20
- SHA-256 `01_MANIFEST_SHA256.tsv`: `371ADB50818F4D7152FB6D910E5FDF5480E0F6DDD071704EE41564985717AD16`
- SHA-256 `04_RUNTIME_DEPENDENCY_MAP.tsv`: `49BE750EE2B41BD791030F9E247F9B70F3005FE707B2735A48C506076DD48F11`
- Overenie manifestu: `PASS` pre deklarovaných `31/31` source/copy položiek
- Najvyššia dosiahnutá úroveň: `T1`
- Oficiálna vetva bez odchýlky: `FAIL`
- Deklarované odchýlky: `D-001` — iba v štvrtej dočasnej kópii boli z live projektu doplnené dve chýbajúce runtime závislosti s očakávanými hashmi; tento beh sa nepočíta do package tieru a skončil vonkajším timeoutom bez rawu.

## Prostredie

- OS/architektúra: `Windows-10-10.0.26200-SP0 / AMD64`
- Python: `3.11.3`, MSC v.1934, 64-bit
- NumPy: `2.4.4`
- SciPy: `1.17.1`
- SymPy: `1.14.0`
- BLAS/LAPACK: `scipy-openblas 0.3.31.188.0`, `USE64BITINT`, `DYNAMIC_ARCH`, `NO_AFFINITY`, Haswell, max 24 threads
- Pracovné kópie: nové adresáre pod `%TEMP%\EA036_AUDITOR_20260722_8f3e1c7a`; zapečatený package nebol vykonávaný ani menený.

## Procesný ledger

| Fáza | Presný príkaz | Exit code | Wall time | Output SHA-256 | Stav |
|---|---|---:|---:|---|---|
| manifest preflight | `powershell -NoProfile -ExecutionPolicy Bypass -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 -PackagePath External_Audits\PACKAGES\EA-20260720-036-KMPC131-C3-NIV-FIRST-REVIEW` | 0 | 4.1 s | n/a | PASS `221/221` |
| environment capture | `python -c "import platform,sys,numpy,scipy,sympy; print('OS='+platform.platform()); print('ARCH='+platform.machine()); print('PYTHON='+sys.version.replace(chr(10),' ')); print('NUMPY='+numpy.__version__); print('SCIPY='+scipy.__version__); print('SYMPY='+sympy.__version__); numpy.show_config()"` | 0 | 3.4 s | n/a | PASS |
| compile | `python -c "from pathlib import Path; p=Path(r'scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"` | 0 | 1.5 s | n/a | PASS |
| help | `python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --help` | 0 | 3.0 s | n/a | PASS |
| smoke | `python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --smoke --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 0 | 4.5 s | n/a | PASS, `4/4`, bez fyziky a rawu |
| official audit bez odchýlky | `python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 1 | 4.1 s | failure receipt `4FB10E747FC05C4C5D168C89E45FAB60E832A7E1FDC801CD889B0B3EB631F784` | FAIL-CLOSED; generated JSON nevznikol |
| negative guard: chýba nominal | `Remove-Item -LiteralPath scripts\results\k_mpc_005\RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json`, potom rovnaký smoke príkaz | 1 (smoke) | 4.3 s | žiadny output | PASS fail-closed |
| negative guard: chýba aggregate | `Remove-Item -LiteralPath scripts\results\k_mpc_005\RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json`, potom rovnaký smoke príkaz | 1 (smoke) | 4.2 s | žiadny output | PASS fail-closed |
| declared deviation `D-001` | do novej kópie pridané `scripts\88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py` a `tracks\A1\A1K1\A2\A2K4\SUBTRACKS\P5\P5_3_SEEDS\26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`; potom official audit príkaz vyššie | 124 | 11.1 s | žiadny raw/receipt | vonkajší timeout; nezvyšuje tier |

### Procesné výstupy

- Preflight stdout skončil `{"package_id":"EA-20260720-036-KMPC131-C3-NIV-FIRST-REVIEW","checks":221,"failed":0,"passed":true}`; stderr bol prázdny.
- Compile stdout bol `COMPILE_PASS`; stderr bol prázdny.
- Help vypísal očakávané selektory `--smoke | --audit`, `--mode`, `--k`, `--result-dir`, `--output`, `--max-runtime-seconds`; stderr bol prázdny.
- Smoke stdout mal `pass=true`, `exact_four_shard_register=true`, všetky štyri worker checks true, `physics_executed=false`; stderr bol prázdny. Po smoke neexistoval success/failure raw ani `.tmp`.
- Official bez odchýlky vytvoril iba technický failure receipt. Všetky štyri workery skončili return code 2 s `FileNotFoundError` pre chýbajúci `scripts\88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py`.
- Oba negatívne smoke guardy mali všetky štyri worker checks false, `physics_executed=false`, presnú missing-input príčinu a nevytvorili success ani failure output.
- `D-001` bol ukončený vonkajším limitom; nezostal Python proces, raw, failure receipt ani `.tmp`.

## Odpoveď na presnú otázku

1. Package neumožnil reprodukčne potvrdiť official KMPC-131 výsledok, pretože jeho deklarovaná runtime closure nie je úplná. Reference `008` však ako primárny existujúci artefakt obsahuje technicky úplný payload `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`, `pair_pass=false`, nie PASS ani fyzikálny STOP. Toto je T1 forenzné potvrdenie, nie T2 reprodukcia.
2. Reference presne podporuje tvrdenú primárnu false množinu: štyri M3 driver brány sú nad `1e-10`, jedna pre každý variant a support. Rank, M1, F0 driver, independent holdout, common, tail, background, null-limit a zmrazené kontrakty sú true. `accepted_solve.pass`, `audit_solve.pass`, `core_pass`, `logical_atom_pass` a `pair_pass` sú odvodené false polia, nie ďalšie nezávislé príčiny.
3. Nepravdivý `af0` audit M3 bridge je odvodený. Jeho nerefinované accepted/audit baseline hodnoty sú bitovo rovnaké ako baseline hodnoty v nominal KMPC-126 pred jeho trojkrokovým same-matrix refinementom; porovnáva sa teda refined nominal s nerefinovaným C3 af0 riešením. Nie je to samostatný fyzikálny nález.
4. Package evidencia je konzistentná s nezmeneným stavom NIV `7/9`, C3 `43/45`, K4 `60/100`, bez fyzikálneho STOP a bez povolenia aggregate. Tento externý audit účtovanie nemení.
5. Úzky successor je metodicky prípustný iba po novej predregistrácii. Musí pokryť `gamma0` aj `af0` a v každom variante rank `104` aj `130`, zachovať presne rovnakú maticu, RHS/konštantu, support `[-1,6]→[-1,8]`, M1 depth 8, nominal autoritu a všetky prahy. Nesmie ladiť prah podľa výsledku a musí znovu overiť holdout/common/tail/background/bridge/logické brány. Pred jeho auditom treba opraviť self-contained runtime kapsulu a parity kontrakt.

## Overenie tvrdení

| Tvrdenie | Tag dôkazu | Primárny zdroj path + riadok/pole | Metóda | Výsledok |
|---|---|---|---|---|
| Manifestové kópie sú byteovo zhodné so source | `INDEPENDENTLY_RECOMPUTED` | `01_MANIFEST_SHA256.tsv`; preflight stdout | SHA-256 preflight | PASS `31/31` |
| Package count a bez duplicít | `INDEPENDENTLY_RECOMPUTED` | celý package + response adresár | rekurzívny count/hash grouping | `38 + 1`, duplicate groups `0` |
| Deklarovaná runtime closure je úplná | `INDEPENDENTLY_RECOMPUTED` | `REPRO/.../full_ra_b1_preflight.py:35-42,68-70`; official failure receipt | statické čítanie + fresh official | FAIL; chýbajú 2 súbory |
| Reference candidate je REVIEW, nie PASS | `OBSERVED_IN_PRIMARY` | `EVIDENCE/008`: `candidate_interpretation_not_verdict`, `pair_pass` | priame čítanie JSON | REVIEW, false |
| Support/depth/leading rád | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/008`: `support_depth_spec`, `variants.*.*_solve.m3.fractional_state` | kontrola všetkých 4 × 13 registrov | `[-1,6]→[-1,8]`, depth 8, všetky začínajú `-1` |
| Plný M3 rank | `OBSERVED_IN_PRIMARY` | `variants.*.*_solve.m3.diagnostics` | priame čítanie | `104/104`, `130/130` v oboch variantoch |
| Štyri primárne M3 driver failures | `OBSERVED_IN_PRIMARY` | `variants.*.*_solve.m3.diagnostics.max_relative_residual/pass_driver` | porovnanie s `thresholds.driver=1e-10` | FAIL: `1.0986663411350403e-10`, `9.900088472975171e-8`, `1.4819148859280634e-10`, `1.4168295759127785e-7` |
| Štyri independent holdouty | `OBSERVED_IN_PRIMARY` | rovnaké diagnostics, `holdout` | porovnanie s `1e-9` | PASS: `1.2439577849089983e-11`, `2.3440519190341615e-10`, `2.6229962412599687e-12`, `4.941656493336481e-10` |
| Common, tail, background | `OBSERVED_IN_PRIMARY` | `variants.*.common.M3`, `tails.M3.by_z.0.01`, `background_guard` | priame čítanie/prah | PASS; common `3.6150158685734e-10/5.916135094295557e-10`, tail `3.3960675283516687e-12/3.4002896643947348e-12`, background worst `0.0/0.0` |
| M1 prechádza | `OBSERVED_IN_PRIMARY` | `EVIDENCE/008.M1` | priame čítanie | PASS; driver `1.2988308345507257e-14`, holdout `1.0615690107356669e-14` |
| False bridge je odvodený | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/008.variants.af0.nominal_vs_af0_coefficient_bridges`; KMPC-126 `same_matrix_refinement_provenance` | porovnanie baseline hodnôt a refined autority | potvrdené v package scope |
| Missing nominal/aggregate fail-closed | `INDEPENDENTLY_RECOMPUTED` | dve oddelené fresh kópie | negatívny smoke | PASS; exit 1, bez fyziky a outputu |
| NIV/C3/K4 účtovanie | `INFERRED_FROM_PROJECT_DOCS` | `EVIDENCE/001`, `002`, `003`, `004` | konzistenčná kontrola registrov | `7/9`, `43/45`, `60/100`; audit nemení |

## Presná forenzná false množina

Primárne false brány sú iba:

- `variants.gamma0.accepted_solve.checks.M3_driver`;
- `variants.gamma0.audit_solve.checks.M3_driver`;
- `variants.af0.accepted_solve.checks.M3_driver`;
- `variants.af0.audit_solve.checks.M3_driver`.

Ich zrkadlá `m3.diagnostics.pass_driver` sú rovnaké štyri príčiny. False
`accepted_solve.pass`, `audit_solve.pass`, príslušné `core_checks`,
`core_pass`, `logical_atom_pass` a top-level `pair_pass` sú logické
dôsledky. False `af0 ... audit.M3.pass` a nadradené bridge polia sú odvodené
porovnaním s refined nominal autoritou. `gamma0 ... bridges.applicable=false`
je správne neaplikovateľné pole. `frozen_B1_left_null_Bianchi.matrix_solve_executed=false`
a `physics_evolution_executed=false` sú zámerné no-solve/no-ODE receipts,
nie failures.

## Rozdiely generated JSON voči reference

Field parity sa nevykonala, pretože oficiálna vetva z dodaného package
nevytvorila generated JSON. T2 sa preto nepriznáva.

Navyše je zmrazené parity pravidlo v aktuálnej podobe nesplniteľné vo fresh
kópii aj po doplnení runtime súborov: reference obsahuje absolútnu live cestu
`frozen_B1_left_null_Bianchi.frozen_algebra_source = D:\Teoria\...`, ktorú
runner tvorí cez `str(algebra_path)`, a vnorené
`frozen_B1_left_null_Bianchi.runtime_seconds`. Dokument 03 dovoľuje
normalizovať iba top-level runtime a štyri worker runtime hodnoty, nie tieto
dve fresh-run závislé polia.

## Nálezy

### F-001 — `MATERIAL`

- Typ: `FORMAL / DOCUMENTATION / REPRODUCIBILITY`
- Presný zdroj: `REPRO/scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py:35-42,68-70`; fresh official failure receipt.
- Pozorované: runtime mapa deklaruje runner + 20 importov + 2 JSON vstupy ako úplnú closure, ale official potrebuje aj `scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py` a `tracks/.../26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`. Prvý chýbajúci súbor zastavil všetky štyri workery.
- Očakávané: self-contained package a official exit 0.
- Dopad na package tier: maximum `T1`, official branch `FAIL`.
- Dopad na fyzikálny scope/verdict: žiadny nový fyzikálny výsledok; existujúci REVIEW sa nemení.
- Minimálny reprodukčný test: fresh exact REPRO + official príkaz z dokumentu 03.
- Navrhovaná oprava: pridať obe exact-hash závislosti do novej versioned package revízie, manifestu a runtime mapy; preflight musí staticky sledovať aj hardcoded file-hash dependencies, nielen Python importy a JSON loadery.

### F-002 — `MATERIAL`

- Typ: `FORMAL / REPRODUCIBILITY`
- Presný zdroj: `REPRO/.../full_ra_b1_preflight_v2.py:133-142`, `EVIDENCE/008.frozen_B1_left_null_Bianchi`, dokument 03 Field parity.
- Pozorované: generated raw obsahuje fresh-path a vnorený runtime, no povolená normalizácia ich nepokrýva.
- Očakávané: všetky polia mimo piatich deklarovaných runtime hodnôt identické.
- Dopad na package tier: exact field parity podľa dokumentu 03 nemožno korektne vyhlásiť ani po oprave F-001.
- Dopad na fyzikálny scope/verdict: žiadny; ide o auditný/provenance kontrakt.
- Minimálny reprodukčný test: úspešný official v ľubovoľnej fresh ceste a rekurzívny diff po aktuálne povolenej normalizácii.
- Navrhovaná oprava: exportovať stabilnú relatívnu provenance cestu alebo explicitne normalizovať `frozen_algebra_source`; zaradiť vnorený B1 `runtime_seconds` medzi povolené runtime polia. Zmenu predregistrovať v novej package revízii.

### F-003 — `MINOR`

- Typ: `DOCUMENTATION / TOOLING`
- Presný zdroj: preflight výsledok `221/221 PASS` oproti F-001.
- Pozorované: preflight vydal plný PASS a `runtime map 23/23`, hoci mapa nebola úplnou runtime closure.
- Očakávané: preflight má odhaliť explicitné file dependencies z `EXPECTED_HASHES` pred odovzdaním balíka.
- Dopad na package tier: samotný preflight PASS nie je dôkaz T2 pripravenosti.
- Dopad na fyzikálny scope/verdict: žiadny.
- Minimálny reprodukčný test: staticky porovnať `EXPECTED_HASHES` s runtime mapou.
- Navrhovaná oprava: pridať preflight pravidlo pre každú lokálnu cestu hashovanú/otváranú počas official vetvy a negatívnu fixture s vynechaním každej takej cesty.

## Nonclaims a odchýlky

- Audit nepriznáva PASS posledným dvom NIV atómom, nemení REVIEW na STOP a nemení K4.
- Reference numerika bola forenzne čítaná a krížovo kontrolovaná, nie fresh T2 reprodukovaná.
- `D-001` použil iba dočasnú kópiu; doplnené súbory mali SHA-256 `0F13DA6C...8364` a `7C927999...999B`. Beh prekročil zmrazený vonkajší limit a nebol opakovaný s dlhším limitom.
- Zapečatený package ani live project súbory neboli zmenené.
- Successor/refinement nebol spustený a nijaký PASS sa z historického KMPC-126 neprenáša automaticky.

## Neautoritatívne odporúčanie

`AGREE_WITH_LIMITATION`

Súhlasím s T1 forenznou interpretáciou reference: REVIEW je lokalizovaný na
multi-rank M3 driver numerical boundary a evidencia nepodporuje fyzikálny
STOP. Nesúhlasím však s tvrdením, že EA-036 v zapečatenej podobe poskytuje
úplnú T2 kapsulu. Pred auditom successor výpočtu treba vydať novú versioned
opravu balíka pokrývajúcu F-001 a F-002.

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, NIV/C3
účtovanie ani K4 score. Autoritatívne spracovanie vykonáva iba hlavný
orchestrátor v samostatnom projektovom zápise.
