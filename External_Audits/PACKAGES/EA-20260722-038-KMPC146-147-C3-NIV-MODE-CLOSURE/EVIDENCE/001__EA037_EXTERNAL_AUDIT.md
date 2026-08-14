# Externý audit — `EA-20260722-037-KMPC131-C3-NIV-T2-RUNTIME-CLOSURE`

## Povinné metadáta

- Auditor/model/verzia: nezávislý Codex audit agent; GPT-5 family (presná runtime revízia modelu nie je agentovi exponovaná)
- Dátum a časová zóna: 2026-07-22, Europe/Bratislava
- Audit mode: `FORENSIC + REPRODUCTION`
- Package revision: `SEALED_READY_FOR_EXTERNAL_T2_AUDIT`, 2026-07-22
- SHA-256 `01_MANIFEST_SHA256.tsv`: `138D38E804900E3FCEA99446BC7A29C3BF114C25E526F7C5EF1B2E653E560330`
- SHA-256 `04_RUNTIME_DEPENDENCY_MAP.tsv`: `CD74A29FC07F09EED3B02730F2C456B598B6976D15C1EA8B858B2815BC5F2A23`
- Overenie manifestu: `PASS`, source/copy `30/30`
- Najvyššia dosiahnutá úroveň: `T2`
- Oficiálna vetva bez odchýlky: `PASS`
- Deklarované odchýlky: `NONE`
- Neautoritatívne odporúčanie: `AGREE_IN_SCOPE`

## Prostredie

- OS/architektúra: `Windows-10-10.0.26200-SP0 / AMD64`
- Python: `3.11.3`, MSC v.1934, 64-bit
- NumPy: `2.4.4`
- SciPy/SymPy: `1.17.1 / 1.14.0`
- BLAS/LAPACK: `scipy-openblas 0.3.31.188.0`, `USE64BITINT`, `DYNAMIC_ARCH`, `NO_AFFINITY`, Haswell, max 24 threads
- R6 preflight runtime: `pwsh 7.6.3`
- Temp root: `%TEMP%\EA037_AUDITOR_20260722_6b9d42c1`; tri nezávislé fresh kópie `official`, `missing_script88`, `missing_sourcemap26`

## Integrita package pred a po audite

Deterministický whole-package snapshot vznikol z lexikograficky zoradených
riadkov `relative/path<TAB>SHA256`, následne SHA-256 nad UTF-8 obsahom:

| fáza | package files | snapshot SHA-256 | manifest SHA-256 | runtime-map SHA-256 |
|---|---:|---|---|---|
| pred auditom | 37 | `CBD619F64612955C4B1D9CD0F2976A633A0D6E515263064BAA28A17BB4C54A0C` | `138D38E8...E560330` | `CD74A29F...5F2A23` |
| po všetkých behoch | 37 | `CBD619F64612955C4B1D9CD0F2976A633A0D6E515263064BAA28A17BB4C54A0C` | `138D38E8...E560330` | `CD74A29F...5F2A23` |

Pred/po integrita je `PASS / EXACT`. Package mal `37` súborov, response
šablóna bola osobitný jeden súbor, manifest `30`, runtime mapa `25` a
fyzických duplicate hash groups bolo `0`.

## Procesný ledger

| Fáza | Presný príkaz | Exit code | Wall time | Output SHA-256 | Stav |
|---|---|---:|---:|---|---|
| R6 preflight | `pwsh -NoProfile -ExecutionPolicy Bypass -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 -PackagePath External_Audits\PACKAGES\EA-20260722-037-KMPC131-C3-NIV-T2-RUNTIME-CLOSURE` | 0 | 2.7 s | n/a | PASS `249/249` |
| environment | `python -c "import platform,sys,numpy,scipy,sympy; print('OS='+platform.platform()); print('ARCH='+platform.machine()); print('PYTHON='+sys.version.replace(chr(10),' ')); print('NUMPY='+numpy.__version__); print('SCIPY='+scipy.__version__); print('SYMPY='+sympy.__version__); numpy.show_config()"` | 0 | 2.4 s | n/a | PASS |
| compile | `python -c "from pathlib import Path; p=Path(r'scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"` | 0 | 1.6 s | n/a | PASS |
| help | `python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --help` | 0 | 2.5 s | n/a | PASS |
| smoke | `python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --smoke --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 0 | 4.2 s | n/a | PASS, `4/4`, bez fyziky/rawu |
| official bez odchýlky | `python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 0 | 8.7 s | generated JSON `2545020C78CA4C480CBF264EF4D53CDE1F404CA45C0C0A4E4DCE5B361A7E9615` | PASS, očakávaný REVIEW |
| corrected field parity | presný Python recursive compare po odstránení 6 runtime polí a path-root normalizácii podľa dokumentu 03 | 0 | 1.5 s | normalized reference/generated `68C561CDB249CD1A957B97A02AEC06BEF28D302305ABDCE39185207324E17521` | PASS, diff `0` |
| guard bez script 88 | `Remove-Item -LiteralPath scripts\88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py`; potom official príkaz vyššie, outer timeout 20 s | 1 | 4.1 s | failure receipt `EBB6B375346857BAE074000635288681B8E4AD5B5355DFF2F4493A16756D8A4F` | PASS fail-closed |
| guard bez source-map 26 | `Remove-Item -LiteralPath tracks\A1\A1K1\A2\A2K4\SUBTRACKS\P5\P5_3_SEEDS\26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`; potom official príkaz vyššie, outer timeout 20 s | 1 | 5.8 s | failure receipt `5B9C16C9E9DA2FF77981C4E5E8D038960606EC07C1D9F84D751CB0A05BF00748` | PASS fail-closed |
| declared deviation | n/a | n/a | n/a | n/a | `NONE` |

### Procesné výstupy

- R6 preflight stdout skončil `{"package_id":"EA-20260722-037-KMPC131-C3-NIV-T2-RUNTIME-CLOSURE","checks":249,"failed":0,"passed":true}`. Potvrdil manifest `30/30`, runtime `25/25`, exact REPRO coverage `25/25` a tri hardcoded dependency checks.
- Compile stdout: `COMPILE_PASS`; stderr prázdny.
- Help zobrazil očakávané selektory; stderr prázdny.
- Smoke stdout: `pass=true`, `exact_four_shard_register=true`, všetky štyri workery true, `physics_executed=false`; stderr prázdny. Success/failure raw a `.tmp` po smoke neexistovali.
- Official stdout: `run_id=KMPC-131`, `candidate_interpretation_not_verdict=REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`, `pair_pass=false`, parent `runtime_seconds=6.016`; stderr prázdny. Štyri worker runtime boli približne `3.047–4.171 s`, teda pod frozen `4.8 s`; parent ostal pod `9 s` a outer beh pod `20 s`.
- Official generated JSON vznikol v fresh ceste `official/scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json`, veľkosť `143563` B; failure raw ani `.tmp` nevznikli.
- Oba negatívne official guardy vytvorili iba `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` receipt so `score_effect=NONE`, presnou `FileNotFoundError` cestou vo všetkých štyroch workeroch, bez success rawu a bez `.tmp`.

## Odpoveď na presnú otázku

1. `ÁNO.` Self-contained official vetva dobehla bez odchýlky s `exit code 0`, generated JSONom a presne rovnakým `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`. REVIEW je úspešne reprodukovaný frozen fyzikálny stav; nie je to technical failure.
2. `ÁNO.` Runtime mapa a fyzický REPRO obsahujú runner, 20 transitive importov, dva JSON vstupy a oba nové hardcoded exact-hash vstupy. R6 preflight potvrdil exact coverage `25/25`.
3. `ÁNO.` Po výlučne povolenej normalizácii šiestich wall-time hodnôt a absolútneho koreňa `frozen_algebra_source` zostalo `0` rozdielov. Reference aj generated cesta mali exact suffix `scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py`; oba rawy mali exact B1 source hash `62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D`.
4. `ÁNO.` R6 explicitne eviduje všetky tri `EXPECTED_HASHES` dependencies a oba negatívne official guardy samostatne preukázali fail-closed správanie pri vynechaní script 88 aj source-map 26.
5. `ÁNO.` Oprava nemení nijaké fyzikálne pole: nulový normalized diff zahŕňa rovnice, identity, support/depth, prahy, residualy, brány aj účtovacie polia. NIV ostáva `7/9`, C3 `43/45`, K4 `60/100`; fyzikálny STOP nevzniká.

## Overenie tvrdení

| Tvrdenie | Tag dôkazu | Primárny zdroj path + pole | Metóda | Výsledok |
|---|---|---|---|---|
| Package integrita | `INDEPENDENTLY_RECOMPUTED` | celý EA-037 package | SHA-256 snapshot pred/po | PASS, exact `CBD619F6...4C54A0C` |
| Manifest/source-copy | `INDEPENDENTLY_RECOMPUTED` | `01_MANIFEST_SHA256.tsv`, R6 stdout | SHA-256 | PASS `30/30` |
| Runtime closure | `INDEPENDENTLY_RECOMPUTED` | `04_RUNTIME_DEPENDENCY_MAP.tsv`, celý `REPRO/`, R6 stdout | exact coverage + official | PASS `25/25` |
| Hardcoded inputs | `INDEPENDENTLY_RECOMPUTED` | `full_ra_b1_preflight.EXPECTED_HASHES`, R6 `runtime-hardcoded-dependency:*` | static checks + dva negatívne official behy | PASS `3/3`; oba nové guardy fail-closed |
| Official technická úplnosť | `INDEPENDENTLY_RECOMPUTED` | generated `execution_status`, stdout | fresh official, outer 20 s | PASS, `TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT` |
| REVIEW, nie technical failure | `INDEPENDENTLY_RECOMPUTED` | generated `candidate_interpretation_not_verdict`, `pair_pass` | fresh official | `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`, false |
| Corrected field parity | `INDEPENDENTLY_RECOMPUTED` | generated vs `EVIDENCE/005` | exact recursive compare podľa dokumentu 03 | PASS, diff `0`; normalized SHA oba `68C561CD...E17521` |
| Provenance suffix/hash | `INDEPENDENTLY_RECOMPUTED` | `frozen_B1_left_null_Bianchi.frozen_algebra_source/.frozen_algebra_sha256` | suffix a exact hash assertions | PASS/PASS |
| Štyri primárne M3 driver failures | `INDEPENDENTLY_RECOMPUTED` | `variants.*.*_solve.m3.diagnostics` | fresh generated raw + exact parity | rovnaké štyri false brány |
| Rank a holdout | `INDEPENDENTLY_RECOMPUTED` | rovnaké diagnostics | fresh generated raw | rank `104/104`, `130/130`; všetky 4 holdouty PASS |
| Ostatné frozen brány | `INDEPENDENTLY_RECOMPUTED` | generated common/tails/background/null/contract fields | exact parity + primárne čítanie | bez rozdielu; tvrdené PASS zachované |
| NIV/C3/K4 účtovanie | `INFERRED_FROM_PROJECT_DOCS` | `EVIDENCE/002`, `004`; generated score fields | konzistenčná kontrola | `7/9`, `43/45`, `60/100`, bez zmeny |

## Reprodukovaná REVIEW numerika

| variant | solve | rank | M3 driver (`limit 1e-10`) | M3 holdout (`limit 1e-9`) | stav |
|---|---|---:|---:|---:|---|
| `gamma0` | accepted | `104/104` | `1.0986663411350403e-10` | `1.2439577849089983e-11` | driver false, holdout true |
| `gamma0` | audit | `130/130` | `9.900088472975171e-8` | `2.3440519190341615e-10` | driver false, holdout true |
| `af0` | accepted | `104/104` | `1.4819148859280634e-10` | `2.6229962412599687e-12` | driver false, holdout true |
| `af0` | audit | `130/130` | `1.4168295759127785e-7` | `4.941656493336481e-10` | driver false, holdout true |

Najhoršie accepted riadky sú `fuel_Euler[6]`; najhoršie audit riadky sú
`tight_coupling[8]`. Presný normalized diff `0` potvrdzuje aj nezmenené M3
common `3.6150158685734e-10 / 5.916135094295557e-10`, M3 tail pri `.01`
`3.3960675283516687e-12 / 3.4002896643947348e-12`, background worst `0/0`,
M1 driver `1.2988308345507257e-14` a holdout
`1.0615690107356669e-14`.

Primárne false brány ostávajú iba štyri `M3_driver` brány. Ich
`pass_driver`, solve/core/logical a top-level `pair_pass` polia sú zrkadlá
alebo logické dôsledky. False af0 audit bridge ostáva odvodený z refined
nominal verzus nerefinovaný C3 solve. No-solve/no-ODE receipt booleany a
`gamma0 bridge applicable=false` nie sú failures.

## Rozdiely generated JSON voči reference

- Odstránených bolo presne šesť povolených runtime hodnôt.
- Normalizovaný bol iba absolútny koreň jednej provenance cesty.
- Reference suffix guard: `PASS`.
- Generated suffix guard: `PASS`.
- B1 source SHA guard v oboch rawoch: `PASS`.
- Normalized reference SHA-256: `68C561CDB249CD1A957B97A02AEC06BEF28D302305ABDCE39185207324E17521`.
- Normalized generated SHA-256: `68C561CDB249CD1A957B97A02AEC06BEF28D302305ABDCE39185207324E17521`.
- Rekurzívny rozdiel: `0`.

Nijaké fyzikálne číslo, identita, brána, prah ani source hash neboli pri
porovnaní normalizované.

## Nálezy

### F-001 — `MINOR`

- Typ: `DOCUMENTATION / TOOLING COMPATIBILITY`
- Presný zdroj: `External_Audits/TOOLS/Test-ExternalAuditPackage.ps1:93`.
- Pozorované: R6 používa `[System.IO.Path]::GetRelativePath`. Diagnostický prvý pokus cez legacy `powershell.exe` skončil `exit 1` za `2.7 s`, pretože Windows PowerShell/.NET runtime túto metódu neposkytuje. Nezmenený R6 následne cez dostupný `pwsh 7.6.3` prešiel `249/249`.
- Očakávané: control dokument má pomenovať PowerShell 7 (`pwsh`) ako runtime R6.
- Dopad na package tier: `NONE`; povinný R6 preflight bol úspešne vykonaný pred fresh reprodukciou a official vetva nemala odchýlku.
- Dopad na fyzikálny scope/verdict: `NONE`.
- Minimálny reprodukčný test: spustiť R6 raz cez Windows PowerShell 5.1 a raz cez `pwsh 7+`.
- Navrhovaná oprava: v budúcich balíkoch uviesť explicitný príkaz `pwsh -NoProfile ...` alebo implementovať kompatibilný fallback pre relatívnu cestu.

Žiadny `CRITICAL` ani `MATERIAL` nález neostal. EA-036 F-001 až F-003 sú
v rozsahu EA-037 technicky odstránené.

## Nonclaims a odchýlky

- Official T2 vetva nemala nijakú odchýlku.
- Legacy PowerShell diagnostika nezasiahla package ani reprodukciu; úspešný R6 preflight bežal cez PowerShell 7 pred Python výpočtom.
- T2 znamená reprodukciu existujúceho REVIEW, nie logický PASS dvoch NIV atómov.
- T3 ani nezávislý druhý equation builder sa netvrdí.
- Refinement, successor ani aggregate nebol spustený.
- Externý audit nemení prediction table, release, Zenodo, NIV/C3 registre ani K4 score.

## Neautoritatívne odporúčanie

`AGREE_IN_SCOPE`

EA-037 odstraňuje materiálne a procesné chyby EA-036 v deklarovanom scope.
Package je self-contained pre T2, corrected parity je nulová a oba nové
hardcoded-input guardy fail-closed fungujú. Reprodukovaný stav ostáva
`REVIEW_C3_NIV_K0P15_MULTI_RANK_NUMERICAL_BOUNDARY`; nejde o technical
failure ani fyzikálny STOP.

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, NIV/C3
účtovanie ani K4 score. Autoritatívne spracovanie vykonáva iba hlavný
orchestrátor v novom projektovom zápise.
