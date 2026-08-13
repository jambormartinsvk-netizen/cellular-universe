# Externý audit — EA-039 KMPC-148 C3 autoritatívny agregát

## Povinné metadáta

- Auditor/model/verzia: nezávislý Codex audit agent `Lagrange`; GPT-5
  family (presná runtime revízia modelu nie je agentovi exponovaná)
- Dátum a časová zóna: 2026-07-22, Europe/Bratislava
- Audit mode: `BLIND / FORENSIC / REPRODUCTION`
- Package revision: `SEALED_READY_FOR_EXTERNAL_T2_AUDIT`
- SHA-256 manifestu:
  `724489858A4D1DEB1C285F782CA0C054BB74D97D8BA0D76D518B402B1F37F99D`
- Overenie manifestu: `PASS`, source/copy `25/25`
- Najvyššia dosiahnutá úroveň: `T2_REPRODUCIBLE_CALCULATION`
- Oficiálna vetva bez odchýlky: `PASS`
- Deklarované odchýlky: `NONE`
- Autor teórie: Martin Jambor
- Tvorca skriptov: Codex (OpenAI)

## Prostredie a integrita

- OS/architektúra: `Windows-10-10.0.26200-SP0 / AMD64`
- Python: `3.11.3`, MSC v.1934, 64-bit
- PowerShell: `pwsh 7.6.3`
- Knižnice official vetvy: iba Python standard library
- Fresh audit root: `%TEMP%\EA039_AUDITOR_20260722_fa196630`
- Fresh vetvy: `official`, `missing_pair`, `missing_authority`

Environment proces skončil exit code `0` za `0.310549 s`; stderr bol
prázdny a stdout bol:

```text
OS=Windows-10-10.0.26200-SP0
ARCH=AMD64
PYTHON=3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)]
```

Whole-package snapshot vznikol z lexikograficky zoradených riadkov
`relative/path<TAB>SHA256` a SHA-256 nad ich UTF-8 reprezentáciou:

| fáza | package files | snapshot SHA-256 |
|---|---:|---|
| pred fresh reprodukciou | 32 | `1111F3BF68103EFF35099B849E79818E7FAD1DFAFE9618E645913680C8B4274C` |
| po všetkých behoch | 32 | `1111F3BF68103EFF35099B849E79818E7FAD1DFAFE9618E645913680C8B4274C` |

Response adresár mal jeden súbor. Duplicate hash groups: `0`; temp súbory
v package: `0`. Originálny package ostal exact immutable. Všetky Python
behy prebehli iba vo fresh dočasných kópiách `REPRO/`.

## Procesný ledger

| Fáza | Presný príkaz | Exit code | Wall time | Output SHA-256 | Stav |
|---|---|---:|---:|---|---|
| manifest preflight | `pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 -PackagePath External_Audits\PACKAGES\EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE` | 0 | `1.599075 s` | n/a | PASS `212/212` |
| compile | `python -m py_compile scripts\baseScripts\p5_general_synchronous\c3_authoritative_logical_aggregate.py scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py` | 0 | `0.229793 s` | n/a | PASS |
| help | `python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --help` | 0 | `0.275099 s` | n/a | PASS |
| smoke | `python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --smoke` | 0 | `0.149174 s` | n/a | PASS `6/6` |
| official audit | `python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --aggregate` | 0 | `1.053096 s` | `82CB60CC2D766D85B225745A20C5244F02F6B793DF30B985BC9E23D2B69CE0A4` | PASS |
| missing-pair guard | odstránenie frozen AD/.005 pair rawu; potom nezmenený official príkaz | 3 | `0.354453 s` | failure `DC7A354380F67572D08150FDBF585F70898543F5E5656054CA353CFC363D3F21` | PASS fail-closed |
| missing-authority guard | odstránenie AD mode authority 206; potom nezmenený official príkaz | 3 | `0.319878 s` | failure `D4845F3EC9197B7CE9F720D976BD32F7DACB217D6E64E4A0AB9E57251C477BB3` | PASS fail-closed |
| declared deviation | n/a | n/a | n/a | n/a | `NONE` |

Každý Python proces mal vonkajší limit `10 s`; žiadny timeout nenastal.

### Preflight stdout/stderr

R6 stdout skončil:

```json
{"package_id":"EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE","checks":212,"failed":0,"passed":true}
```

Stderr bol prázdny. R6 potvrdil manifest `25/25`, runtime mapu `22/22`,
exact REPRO coverage `22/22`, package `32`, response `1`, nulové duplicate
hash groups, placeholdery, temp súbory a pending hash markery. Runtime-map
SHA-256 je
`53633A7E7A47CA5F8E5B7321D3ECC05295FE4F08FD7D8039B975FB831E8E26E5`.

### Compile a help stdout/stderr

Compile stdout aj stderr boli prázdne.

Help stdout:

```text
usage: 392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py
       [-h] (--aggregate | --smoke) [--result-dir RESULT_DIR]
       [--track-dir TRACK_DIR] [--output OUTPUT]
       [--max-runtime-seconds MAX_RUNTIME_SECONDS]

Read-only exact-hash aggregate of 45 authoritative C3 atoms.

options:
  -h, --help            show this help message and exit
  --aggregate
  --smoke
  --result-dir RESULT_DIR
  --track-dir TRACK_DIR
  --output OUTPUT
  --max-runtime-seconds MAX_RUNTIME_SECONDS
```

Help stderr bol prázdny.

### Smoke stdout/stderr

```json
{
  "checks": {
    "contract_guard": true,
    "missing_authority_fail_closed": true,
    "missing_pair_fail_closed": true,
    "no_solver_symbols": true,
    "twenty_read_only_inputs": true,
    "zero_runtime_operations": true
  },
  "operation_counts": {
    "matrices_built": 0,
    "physics": 0,
    "solvers": 0,
    "workers": 0
  },
  "pass": true,
  "physics_executed": false,
  "run_id": "KMPC-148",
  "source_hashes": {
    "base": "EE688EAEFC370163F6AE555E169AC61A78D03EFEECC635101DA06D4ECAC17505",
    "runner": "191E0627220E75DF18A4FA416A2C61ECF38BD6DA006182BDA71BDFD486ED7E21"
  }
}
```

Smoke stderr bol prázdny. Po smoke neexistoval success raw, failure raw ani
`.tmp`.

### Official stdout/stderr a generated JSON

```json
{
  "aggregate_gate_pass": true,
  "candidate_interpretation_not_verdict": "PASS_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45_CANDIDATE_ONLY",
  "observed_atoms": 45,
  "operation_counts": {
    "files_read": 20,
    "matrices_built": 0,
    "physics": 0,
    "solvers": 0,
    "workers": 0
  },
  "output": "C:\\Users\\jambor.CHASTIA\\AppData\\Local\\Temp\\EA039_AUDITOR_20260722_fa196630\\official\\scripts\\results\\k_mpc_005\\RUN_KMPC_148_P5_3G7_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45.json",
  "run_id": "KMPC-148",
  "runtime_seconds": 0.46799999999348074
}
```

Official stderr bol prázdny. Generated JSON:

```text
path = official/scripts/results/k_mpc_005/RUN_KMPC_148_P5_3G7_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45.json
bytes = 49172
SHA-256 = 82CB60CC2D766D85B225745A20C5244F02F6B793DF30B985BC9E23D2B69CE0A4
failure raw = absent
.tmp = absent
```

Generated raw má `20/20` inputov, `15/15` pair pass, `5/5` authority
pass, `all_inputs_pass=true`, `aggregate_gate_pass=true` a neobsahuje
žiaden false boolean.

## Nezávislý register 45 atómov

Očakávaný register bol zostavený v PowerShelli iba z literálov dokumentu
03, bez importu alebo volania agregátora:

```powershell
$expected = foreach ($mode in @('AD','CDI','BI','NID','NIV')) {
  foreach ($k in @('0.005','0.05','0.15')) {
    foreach ($variant in @('nominal','gamma0','af0')) {
      "$mode/k=$k/$variant"
    }
  }
}
```

Výsledok nezávislej kontroly:

```text
independent count = 45
independent unique = 45
generated expected_register = independent register: true
generated observed_register = independent register: true
generated expected_register = observed_register: true
generated observed unique = 45
mode counts = AD:9, CDI:9, BI:9, NID:9, NIV:9
pair inputs = 15/15 pass
mode authorities = 5/5 pass
```

Poradie je presne `AD, CDI, BI, NID, NIV × 0.005, 0.05, 0.15 ×
nominal, gamma0, af0`; prvý atóm je `AD/k=0.005/nominal` a posledný
`NIV/k=0.15/af0`. Duplicita ani chýbajúci atóm neexistuje.

## Exact field parity

Nezávislý rekurzívny comparator načítal generated JSON a
`EVIDENCE/003__KMPC148_PASS_REFERENCE.json`. Z oboch objektov odstránil iba
top-level `runtime_seconds` a následne porovnal typ, key-set, poradie a
dĺžku arrays a každú scalar hodnotu.

Proces skončil exit code `0` za `0.131211 s`; stderr bol prázdny:

```text
ALLOWED_NORMALIZATION=runtime_seconds
DIFF_COUNT=0
NORMALIZED_REFERENCE_SHA256=3D034C70DB3B5CB944396885612E5EB30BE8CAE7BF656978BCDDF70CFFC879AC
NORMALIZED_GENERATED_SHA256=3D034C70DB3B5CB944396885612E5EB30BE8CAE7BF656978BCDDF70CFFC879AC
```

Nijaký hash, source path, identity, candidate, gate, register, count,
scope alebo operation count nebol normalizovaný. Fyzický SHA generated
rawu sa oproti reference SHA
`C493B102859CE6181F42BABDFE69A12C9D3B5900040F796D2DECAE0403678238`
líši iba pre povolenú nedeterministickú runtime hodnotu.

## Negatívne guardy

### Missing-pair guard

V osobitnej fresh kópii bol vykonaný presne tento zásah a official:

```powershell
Remove-Item -LiteralPath scripts\results\k_mpc_005\RUN_KMPC_131_P5_3G7_C3_AD_K0p005_ZERO_VARIANT_PAIR.json
python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --aggregate
```

Výsledok:

```text
exit code = 3
wall time = 0.354453 s
stdout = <prázdny>
stderr = KMPC-148 technical failure receipt: ...\RUN_KMPC_148_P5_3G7_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45_TECHNICAL_FAILURE.json
failure SHA-256 = DC7A354380F67572D08150FDBF585F70898543F5E5656054CA353CFC363D3F21
execution_status = TECHNICAL_FAILURE_NO_PHYSICS_VERDICT
physics_verdict = NONE_TECHNICAL_FAILURE
error_type = FileNotFoundError
error_message = missing frozen C3 pair: RUN_KMPC_131_P5_3G7_C3_AD_K0p005_ZERO_VARIANT_PAIR.json
operation_counts = workers:0, solvers:0, physics:0, matrices_built:0
orchestrator_verdict = NOT_ASSIGNED_BY_SCRIPT
success raw = absent
.tmp = absent
```

### Missing-mode-authority guard

V druhej fresh kópii bol vykonaný presne tento zásah a official:

```powershell
Remove-Item -LiteralPath tracks\A1\A1K1\A2\A2K4\SUBTRACKS\P5\P5_3_SEEDS\206_KMPC_132_AND_C3_AD_MODE_CLOSURE_INTERNAL_AUDIT_SK.md
python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --aggregate
```

Výsledok:

```text
exit code = 3
wall time = 0.319878 s
stdout = <prázdny>
stderr = KMPC-148 technical failure receipt: ...\RUN_KMPC_148_P5_3G7_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45_TECHNICAL_FAILURE.json
failure SHA-256 = D4845F3EC9197B7CE9F720D976BD32F7DACB217D6E64E4A0AB9E57251C477BB3
execution_status = TECHNICAL_FAILURE_NO_PHYSICS_VERDICT
physics_verdict = NONE_TECHNICAL_FAILURE
error_type = FileNotFoundError
error_message = missing C3 mode authority: 206_KMPC_132_AND_C3_AD_MODE_CLOSURE_INTERNAL_AUDIT_SK.md
operation_counts = workers:0, solvers:0, physics:0, matrices_built:0
orchestrator_verdict = NOT_ASSIGNED_BY_SCRIPT
success raw = absent
.tmp = absent
```

Oba guardy sú `PASS_FAIL_CLOSED`: vytvorili iba immutable technical-failure
receipt, nie success raw ani fyzikálny/orchestrátorový verdikt.

## Odpoveď na presnú otázku

1. `ÁNO.` Package je úplná T2 runtime closure: runner, base, 15 pair
   rawov a 5 mode-closure autorít; R6 potvrdil exact coverage `22/22`.
2. `ÁNO.` Fresh official bez odchýlky overil kontrakt `20/20`, vytvoril
   exact register `45/45`, bez duplicity, s mode counts `9/9/9/9/9`.
3. `ÁNO.` Po jedinej povolenej normalizácii top-level
   `runtime_seconds` zostal field diff `0`.
4. `ÁNO.` Missing-pair aj missing-authority guard skončili nonzero,
   vytvorili iba technical-failure receipt a nepridelili fyzikálny verdikt.
5. `ÁNO.` Evidencia podporuje interný C3 aggregate `45/45`; nevytvára nový
   fyzikálny bod a nemení K4 `60/100`, P5 `3.5/6` ani P5.4 `NOT RUN`.

## Overenie tvrdení

| Tvrdenie | Tag dôkazu | Primárny zdroj path + pole | Metóda | Výsledok |
|---|---|---|---|---|
| package a runtime closure sú úplné | `INDEPENDENTLY_RECOMPUTED` | `01_MANIFEST_SHA256.tsv`; `04_RUNTIME_DEPENDENCY_MAP.tsv`; R6 stdout | hash/source-copy/exact coverage + snapshot pred/po | PASS `25/25`, `22/22`, exact immutable |
| source je read-only bez fyziky | `OBSERVED_IN_PRIMARY` | `REPRO/scripts/baseScripts/.../c3_authoritative_logical_aggregate.py`; runner 392 | priamy source review | iba JSON/Markdown/hash/logika; bez physics importu, workerov, solverov a matíc |
| fresh generated JSON má exact register 45/45 | `INDEPENDENTLY_RECOMPUTED` | generated `logical_register`, `pair_inputs`, `mode_authorities` | fresh official | PASS; `20/20`, `15/15`, `5/5`, gate true |
| independent register je exact a bez duplicity | `INDEPENDENTLY_RECOMPUTED` | generated `expected_register`, `observed_register`, `mode_counts` | samostatná PowerShell kartézska konštrukcia | PASS; exact order, unique 45, päťkrát 9 |
| field parity po jedinej normalizácii má diff 0 | `INDEPENDENTLY_RECOMPUTED` | generated JSON vs `EVIDENCE/003` | exact recursive compare po odobratí iba `runtime_seconds` | PASS, diff `0` |
| oba negatívne guardy fail-closed | `INDEPENDENTLY_RECOMPUTED` | dve fresh failure receipts | missing-pair a missing-authority official | PASS `2/2`, exit 3, bez success rawu/verdictu |
| C3 aggregate 45/45 je podporený | `INDEPENDENTLY_RECOMPUTED` | generated aggregate gate a register; `EVIDENCE/002` | T2 reprodukcia + konzistenčná kontrola interného auditu | PASS v deklarovanom logickom scope |
| K4 60/100 a P5 3.5/6 ostávajú nezmenené | `INFERRED_FROM_PROJECT_DOCS` | `EVIDENCE/002`, sekcia 5; generated `K4_score_effect`, `scope` | konzistenčná kontrola | podporené; P5.4 `NOT RUN` |

## Nálezy

Nebol zistený žiadny `CRITICAL`, `MATERIAL` ani `MINOR` nález. Package
tooling fungoval podľa kontraktu a official T2 vetva nemala nijakú
`DECLARED_DEVIATION`.

## Nonclaims a odchýlky

- Audit nereviduje pôvodné fyzikálne solvery ani ich rovnice; hashovo a
  logicky reprodukuje iba agregovanie prijatých autorít.
- KMPC-148 nepridáva experimentálne dáta, seed solve, predikciu ani
  fyzikálny bod.
- T2 nie je T3; balík neobsahuje druhú nezávislú implementáciu.
- C3 `45/45` je logické coverage účtovanie, nie dôkaz empirickej pravdivosti
  celej teórie.
- K4 ostáva `60/100`; P5 ostáva `3.5/6`; P5.4, S-M successor, G8 a G9
  neboli spustené.
- Release, Zenodo a prediction table sa nemenia.
- Deklarované odchýlky: `NONE`.

## Neautoritatívne odporúčanie

`AGREE_IN_SCOPE`

EA-039 dosahuje T2 bez odchýlky. Fresh official reprodukuje exact
autoritatívny register 45/45; nezávislá kartézska konštrukcia, corrected
field parity aj oba fail-closed guardy prešli. Interný záver je podporený
v deklarovanom rozsahu: C3 má autoritatívny logický aggregate receipt, ale
K4 ostáva `60/100`, P5 `3.5/6` a P5.4 `NOT RUN`.

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, C3 register,
K4 score ani ďalšiu fyzikálnu route. Autoritatívne spracovanie vykoná iba
hlavný orchestrátor v novom response súbore.
