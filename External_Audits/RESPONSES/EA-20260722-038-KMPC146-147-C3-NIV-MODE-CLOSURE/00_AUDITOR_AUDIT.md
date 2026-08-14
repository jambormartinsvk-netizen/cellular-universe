# Externý audit — `EA-20260722-038-KMPC146-147-C3-NIV-MODE-CLOSURE`

## Povinné metadáta

- Auditor/model/verzia: nezávislý Codex audit agent `Lagrange`; GPT-5
  family (presná runtime revízia modelu nie je agentovi exponovaná)
- Dátum a časová zóna: 2026-07-22, Europe/Bratislava
- Audit mode: `FORENSIC_T1 + REPRODUCTION_T2`
- Package revision: `SEALED_READY_FOR_EXTERNAL_MIXED_TIER_AUDIT`
- Autor teórie: Martin Jambor
- Tvorca skriptov: Codex (OpenAI)
- SHA-256 `01_MANIFEST_SHA256.tsv`:
  `2B7066A1B5D6E48910575D329F3A50E8F16672BA0AF8BC43A5869149C057EEA9`
- SHA-256 `04_RUNTIME_DEPENDENCY_MAP.tsv`:
  `288B561BB354711CCB93D91D80D5A8908088C86583D0476B98FFEFC79C6159FF`
- Overenie manifestu: `PASS`, source/copy `15/15`
- Dosiahnuté úrovne: KMPC-146 `T1_PRIMARY_FORMULA`; KMPC-147
  `T2_REPRODUCIBLE_CALCULATION`
- Official KMPC-147 bez odchýlky: `PASS`
- Deklarované odchýlky: `NONE`
- Neautoritatívne odporúčanie: `AGREE` v deklarovanom mixed-tier scope

## 1. Prostredie, preflight a integrita balíka

### Prostredie

- OS/architektúra: `Windows-10-10.0.26200-SP0 / AMD64`
- Python: `3.11.3`, MSC v.1934, 64-bit
- PowerShell pre R6: `pwsh 7.6.3`
- Fresh audit root:
  `%TEMP%\EA038_AUDITOR_20260722_8dbd5bbf`
- Fresh vetvy: `official`, `missing_kmpc146`, `missing_kmpc131`

Environment proces:

```text
python -c "import platform,sys; print('OS='+platform.platform()); print('ARCH='+platform.machine()); print('PYTHON='+sys.version.replace(chr(10),' '))"
exit code = 0
wall time = 0.324195 s
stdout =
OS=Windows-10-10.0.26200-SP0
ARCH=AMD64
PYTHON=3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)]
stderr = <prázdny>
```

### R6 preflight

Presný vecný príkaz spustený z `D:\Teoria`:

```powershell
pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 -PackagePath External_Audits\PACKAGES\EA-20260722-038-KMPC146-147-C3-NIV-MODE-CLOSURE
```

Výsledok:

```text
exit code = 0
wall time = 1.878882 s
stdout final = {"package_id":"EA-20260722-038-KMPC146-147-C3-NIV-MODE-CLOSURE","checks":105,"failed":0,"passed":true}
stderr = <prázdny>
```

R6 potvrdil manifest `15/15`, runtime mapu `3/3`, exact REPRO coverage
`3/3`, všetky required controls, response šablónu, nulové pending hash
markery a nulové temp súbory.

### Integrita pred a po audite

Whole-package snapshot bol zostavený z lexikograficky zoradených riadkov
`relative/path<TAB>SHA256` a zahashovaný ako UTF-8:

| fáza | package files | snapshot SHA-256 |
|---|---:|---|
| pred fresh kópiami | 22 | `4A904F13AC6286EC03ECC9CF982CC15CB5A81317D9A3CC6C09113AA44F1D1917` |
| po všetkých behoch | 22 | `4A904F13AC6286EC03ECC9CF982CC15CB5A81317D9A3CC6C09113AA44F1D1917` |

Response adresár mal jeden súbor. Duplicate hash groups v package: `0`;
temp súbory: `0`. Originálny package ostal exact immutable. Všetky Python
behy prebehli iba v fresh dočasných kópiách `REPRO/`.

## 2. KMPC-146 — T1 delta a forenzný audit

### Source lineage a frozen hashe

R6 nezávisle prepočítal source/copy hashe všetkých piatich T1 súborov:

| súbor | SHA-256 | výsledok |
|---|---|---|
| `390_script_KMPC_146_P5_3g7_C3_NIV_k0p15_multi_rank_refinement.py` | `C3B7E7B41B53891F5E5C86FC1604B1430D246350E31F1334B2071C0A6294ADEB` | exact |
| `c3_zero_variant_parallel_v10_niv_k0p15_multi_rank_refinement.py` | `46365EF983E7ECAE53B804E0882730CE96475554533EB0029FAFF12FA5037D91` | exact |
| `c2_same_matrix_refinement_v2_multi_rank.py` | `1E2600C366590B7FC56289D1FBC386EF24DA50DA9ED5686AE5FB5A50E0992F08` | exact |
| `c2_cdi_k0p15_same_matrix_refinement.py` | `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6` | exact |
| `c2_single_atom_adapter.py` | `C018ACB17311A8CB522FB612AB0EDD1DD5B9C47E16DC5D915A5F6DAF4204BAF8` | exact |

Priamy source review potvrdil:

1. `_refine_solution` prijíma existujúcu `matrix`, `constant` a pôvodné
   riešenie. Z nich tvorí iba škálované pracovné reprezentácie a presne
   trikrát rieši residual correction. Nepridáva rovnicu, stĺpec, riadok ani
   holdout a nemení vstupnú maticu alebo konštantu.
2. Selection rule vyberie refined riešenie iba pri konečnom výsledku,
   striktne menšom relative residuale a nezhoršenom absolute fallback
   residuale.
3. Multi-rank router povoľuje iba ranky `(104, 130)`. Support/depth guard
   povoľuje iba accepted `[-1,6]`, audit `[-1,8]` a M1 depth `8`.
4. KMPC-146 overlay mení iba process-local owner
   `scientific.physics._solve_equilibrated` a obnoví ho v `finally`.
   Worker raw potvrdzuje `owners_restored=true` vo všetkých štyroch
   shardoch.
5. Parent vyžaduje exact predecessor SHA
   `88DFD9AA...A0CFE6`, štyri shardy
   `gamma0/af0 × accepted/audit`, target rank podľa levelu, tri kroky,
   selection pass a frozen source hashe.
6. Refinement kód nemá vstup independent holdoutu. Raw process receipt má
   `independent_holdout_rows_added_to_driver=0` a
   `matrix_rhs_support_depth_threshold_changes=0`.

EA-037 T2 audit a jeho prijatý hlavný posudok tvoria autoritu nezmeneného
KMPC-131 fyzikálneho základu. EA-038 zámerne neposkytuje ani netvrdí fresh
T2 vykonanie KMPC-146; táto časť zostáva striktne T1.

### Nezávislé vyčítanie KMPC-146 rawu

KMPC-146 raw má exact manifestový SHA
`BA595163C3A2E1D464558B035FE478A16E36678FA215C46B124E4062DC77227E`.
Identity je `NIV / 0.15` a source runtime je
`2.905999999959022 s`.

| shard | rank | baseline driver | refined driver | refined abs fallback | selection |
|---|---:|---:|---:|---:|---|
| gamma0 / accepted | 104 | `1.0986663411350403e-10` | `1.62657201412256e-16` | `2.46519032881566e-31` | PASS |
| gamma0 / audit | 130 | `9.900088472975171e-8` | `1.66241459076056e-16` | `7.88860905221012e-31` | PASS |
| af0 / accepted | 104 | `1.4819148859280634e-10` | `1.72470951444806e-16` | `2.95822839457879e-31` | PASS |
| af0 / audit | 130 | `1.4168295759127785e-7` | `2.13942874133211e-16` | `4.68386162474976e-31` | PASS |

Všetky štyri baseline relative aj absolute hodnoty sú exact rovné
zodpovedajúcim KMPC-131 diagnostics. Každý provenance blok má exact rank,
`iterations=3`, tri kroky,
`matrix_identity=EXACT_SAME_MATRIX_AND_CONSTANT` a
`selection_rule_pass=true`.

Independent holdouty po refined riešení prešli:

| shard | holdout relative | pass |
|---|---:|---|
| gamma0 / accepted | `2.021821827054078e-12` | true |
| gamma0 / audit | `9.606207283252414e-11` | true |
| af0 / accepted | `2.0216874241780258e-12` | true |
| af0 / audit | `9.606023213457964e-11` | true |

Oba varianty majú current driver, core, common, tail, background,
null-limit, bridge a logical atom gates true. Contract, independent
contract a všetky shared worker parity kontroly sú true. Frozen hodnoty v
rawe sú support `[-1,6] / [-1,8]`, M1 depth `8` a prahy driver/holdout/
common/tail/absolute/background
`1e-10 / 1e-9 / 1e-8 / 1e-6 / 1e-12 / 1e-12`.

### PF-129

V `same_matrix_multi_rank_audit` je presná false množina:

```text
gamma0/accepted/f0_exact_predecessor_parity
gamma0/audit/f0_exact_predecessor_parity
af0/accepted/f0_exact_predecessor_parity
af0/audit/f0_exact_predecessor_parity
```

V publikovanej JSON reprezentácii sú fuel/F0 projekcie exact rovné
KMPC-131 predecessorovi:

| shard | source = predecessor SHA-256 |
|---|---|
| gamma0 / accepted | `F82A2448D3AF70E917618DAE1EBF1FDA6802287FDB30109DF883E7052D2493A6` |
| gamma0 / audit | `94053B35E062D4B0B37C58C7B810B86397A4E69A0033AABFCD8B7F3B0F1F4D5D` |
| af0 / accepted | `93A387F6AAD2F29BCCDC7D8E965B87425DB798FE6773167491F7E38A0AD7E47B` |
| af0 / audit | `848CB15A1CF7AAD2E2302AE7B0D27F7CBA525A724DB72ACD3AF438047C897B2B` |

Tým je potvrdená príčina `int` versus JSON `str` power keys, nie fyzikálny
ani numerický rozdiel. Mimo tejto auditnej false množiny raw prirodzene
obsahuje historické baseline `pass_driver=false` a
`gamma0 bridge applicable=false`; prvé dokumentuje stav pred korekciou a
druhé neaplikovateľnosť, nie zlyhanie current fyzikálnej brány.

## 3. KMPC-147 — T2 reprodukčný ledger

Všetky štyri procesy bežali oddelene z fresh koreňa `official` s vonkajším
limitom `10 s`.

| fáza | presný príkaz | exit code | wall time | stav |
|---|---|---:|---:|---|
| compile | `python -c "from pathlib import Path; p=Path(r'scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"` | 0 | `0.165507 s` | PASS |
| help | `python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --help` | 0 | `0.207353 s` | PASS |
| smoke | `python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --smoke --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 0 | `0.290288 s` | PASS `13/13` |
| official | `python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 0 | `0.558769 s` | PASS |

### Presné procesné výstupy

Compile stdout bol `COMPILE_PASS`; stderr prázdny.

Help stdout:

```text
usage: 391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py
       [-h] (--smoke | --audit) --mode {NIV} --k {0.15}
       [--result-dir RESULT_DIR] [--max-runtime-seconds MAX_RUNTIME_SECONDS]

Read-only correction of four KMPC-146 F0 parity predicates.

options:
  -h, --help            show this help message and exit
  --smoke
  --audit
  --mode {NIV}
  --k {0.15}
  --result-dir RESULT_DIR
  --max-runtime-seconds MAX_RUNTIME_SECONDS
```

Help stderr bol prázdny.

Smoke stdout:

```json
{
  "checks": {
    "af0_accepted_f0_json_semantic_parity": true,
    "af0_audit_f0_json_semantic_parity": true,
    "all_other_refinement_checks_true": true,
    "all_refinement_provenance_pass": true,
    "all_row_pass_false_only_from_parity": true,
    "all_variant_physics_gates_pass": true,
    "false_parity_set_exact": true,
    "gamma0_accepted_f0_json_semantic_parity": true,
    "gamma0_audit_f0_json_semantic_parity": true,
    "predecessor_run_exact": true,
    "source_identity_exact": true,
    "source_review_exact": true,
    "source_run_exact": true
  },
  "identity": {
    "k_Mpc_inverse": 0.15,
    "mode": "NIV"
  },
  "operation_counts": {
    "physics": 0,
    "solvers": 0,
    "workers": 0
  },
  "pass": true,
  "physics_executed": false,
  "run_id": "KMPC-147"
}
```

Smoke stderr bol prázdny. Po smoke neexistoval success raw, failure raw ani
`.tmp`.

Official stdout:

```json
{
  "candidate_interpretation_not_verdict": "PASS_C3_NIV_K0P15_MULTI_RANK_PARITY_CORRECTION_CANDIDATE_ONLY",
  "operation_counts": {
    "physics": 0,
    "solvers": 0,
    "workers": 0
  },
  "output": "C:\\Users\\jambor.CHASTIA\\AppData\\Local\\Temp\\EA038_AUDITOR_20260722_8dbd5bbf\\official\\scripts\\results\\k_mpc_005\\RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_READ_ONLY_F0_PARITY_CORRECTION.json",
  "pair_pass": true,
  "read_only_runtime_seconds": 0.0779999999795109,
  "run_id": "KMPC-147"
}
```

Official stderr bol prázdny. Generated JSON:

```text
path = official/scripts/results/k_mpc_005/RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_READ_ONLY_F0_PARITY_CORRECTION.json
bytes = 168112
SHA-256 = 8633DF7C8E583A04A6EE4F05BCEA9D4CB04F7A410BCC9DA6EE9E00AC8BF3A2CE
failure raw = absent
.tmp = absent
```

Generated physical SHA sa smie líšiť od reference SHA
`2780A8D6...956B16E` iba preto, že jediná povolená wall-time hodnota nie je
deterministická. Nijaká odchýlka nebola použitá.

## 4. Corrected field parity a protected snapshot

### Corrected field parity

Nezávislý rekurzívny comparator načítal generated JSON a
`EVIDENCE/007`. Na oboch stranách odstránil iba:

```text
read_only_f0_parity_correction.runtime_seconds
```

Potom porovnal typ, key-set, dĺžku polí a každú scalar hodnotu. Proces
skončil exit `0` za `0.229348 s`, stderr bol prázdny:

```text
DIFF_COUNT=0
NORMALIZED_REFERENCE_SHA256=33C977BA43D3E94D4EF3798C5A82EE8BC74D66C05324ED3E9E410868D36E5635
NORMALIZED_GENERATED_SHA256=33C977BA43D3E94D4EF3798C5A82EE8BC74D66C05324ED3E9E410868D36E5635
```

Nijaký path, source hash, fyzikálna hodnota, brána, threshold, identity ani
provenance nebol normalizovaný.

### Nezávislá protected projekcia

Osobitný comparator neimportoval runner. Implementoval presne exclusion
set dokumentu 03 na KMPC-146 source a generated KMPC-147. Proces skončil
exit `0` za `0.160533 s`, stderr bol prázdny:

```text
PROTECTED_EXACT=True
PROTECTED_SOURCE_SHA256=9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A
PROTECTED_GENERATED_SHA256=9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A
DECLARED_BEFORE=9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A
DECLARED_AFTER=9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A
OPERATION_COUNTS={"physics":0,"solvers":0,"workers":0}
CORRECTION_PASS=True
SOURCE_RUNTIME_SECONDS=2.905999999959022
ROW_gamma0_accepted=f0:True,pass:True
ROW_gamma0_audit=f0:True,pass:True
ROW_af0_accepted=f0:True,pass:True
ROW_af0_audit=f0:True,pass:True
```

Priamy source review runnera 391 navyše potvrdil, že je standalone
standard-library JSON/hash transformácia bez projektového importu, worker
procesu, solvera, matrix buildera alebo fyzikálnej funkcie. Nulové operation
counts preto podporuje output aj kontrola vykonateľnej source vetvy.

## 5. Negatívne missing-input guardy

Každý guard použil osobitnú fresh trojsúborovú kópiu. V každej bol
odstránený iba uvedený vstup a následne spustený nezmenený official príkaz
s vonkajším limitom `10 s`.

### Guard A — chýba KMPC-146 source raw

```powershell
Remove-Item -LiteralPath scripts\results\k_mpc_005\RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json
python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8
```

```text
exit code = 2
wall time = 0.256686 s
stdout = <prázdny>
stderr = KMPC-147 pre-output technical failure: RuntimeError: immutable input missing or hash-mismatched: RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json
success raw = absent
failure raw = absent
.tmp = absent
```

### Guard B — chýba KMPC-131 predecessor

```powershell
Remove-Item -LiteralPath scripts\results\k_mpc_005\RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json
python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8
```

```text
exit code = 2
wall time = 0.243753 s
stdout = <prázdny>
stderr = KMPC-147 pre-output technical failure: RuntimeError: immutable input missing or hash-mismatched: RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json
success raw = absent
failure raw = absent
.tmp = absent
```

Oba guardy sú `PASS_FAIL_CLOSED`. Nevznikol generated success JSON ani
žiaden payload s fyzikálnym verdiktom.

## 6. Oddelené posúdenie tvrdení

| oblasť | evidence tag | výsledok |
|---|---|---|
| Package integrita | `INDEPENDENTLY_RECOMPUTED` | PASS; R6 `105/105`, exact snapshot pred/po, manifest `15/15`, runtime `3/3` |
| KMPC-146 source lineage | `DIRECT_SOURCE_REVIEW` | PASS na T1; frozen hashe, ranks 104/130, tri corrections, same matrix/RHS, selection a owner restoration podporené |
| KMPC-146 numerika | `INDEPENDENTLY_RECOMPUTED_FROM_RAW` | PASS na T1; štyri baselines exact predecessor, refined drivery a holdouty prešli |
| PF-129 | `INDEPENDENTLY_RECOMPUTED_FROM_RAW` | PASS; presná štvorka false parity, štyri JSON-semantic F0 stromy exact |
| KMPC-147 technická reprodukcia | `REPRODUCED_T2` | PASS; compile/help/smoke/official `0/0/0/0`, generated JSON, bez odchýlky |
| Field parity | `INDEPENDENTLY_RECOMPUTED` | PASS; povolená normalizácia jedného runtime poľa, diff `0` |
| Protected fyzika/numerika | `INDEPENDENTLY_RECOMPUTED` | PASS; exact SHA pred/po `9F76DD48...A0A` |
| Operation counts | `REPRODUCED_T2 + DIRECT_SOURCE_REVIEW` | PASS; workers/solvers/physics `0/0/0` |
| Missing-input guardy | `INDEPENDENTLY_RECOMPUTED` | PASS `2/2`, nonzero, fail-closed, bez fyzikálneho verdiktu |
| Formálna logika | `INDEPENDENTLY_RECOMPUTED` | po semantic correction sú 4/4 rows, refinement a pair true; candidate nie je projektový verdikt |
| Účtovanie NIV/C3 | `INFERRED_FROM_PROJECT_DOCS + AUDITED_EVIDENCE` | evidencia podporuje interné `NIV 7/9 + 2 = 9/9` a `C3 43/45 + 2 = 45/45 logical PASS` v mixed-tier scope |
| K4 | `DIRECT_RAW + PROJECT_DOCS` | `K4_score_effect=NONE_60_OF_100_UNCHANGED`; `60/100` podporené bez zmeny |
| Dokumentácia | `DIRECT_REVIEW` | prereg 238/240, audity 239/241 a package controls sú vzájomne konzistentné |

KMPC-147 generated raw má
`execution_status=TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT`,
`orchestrator_verdict=NOT_ASSIGNED_BY_SCRIPT`, `score_effect=NONE`,
`prediction_table_effect=NONE`, `release_trigger=NONE` a
`zenodo_trigger=NONE`. Audit teda nezamieňa candidate za autoritatívny
projektový verdikt.

## 7. Nálezy, limity a nonclaims

### Nálezy

Nebol zistený žiadny `CRITICAL`, `MATERIAL` ani `MINOR` nález. Official
vetva nemala nijakú `DECLARED_DEVIATION`.

### Deklarované scope limity — nie nálezy

1. KMPC-146 dosahuje v EA-038 iba `T1`. Jeho fresh T2 runtime closure
   balík zámerne neobsahuje a audit ju netvrdí.
2. KMPC-147 dosahuje `T2`, nie T3. Neexistuje nezávislá druhá
   implementácia transformácie.
3. Agentový audit je nezávislý proces/kontext, ale ostáva v rovnakej
   platformovej rodine Codex.

Audit nespustil KMPC-146, C3 aggregate, P5.4, G8, G9, release, Zenodo ani
prediction table. Nezmenil source, package, rawy, registre, K4 skóre alebo
projektový verdikt.

## 8. Neautoritatívne odporúčanie

`AGREE`

V deklarovanom mixed-tier scope balík odpovedá na všetky štyri presné
otázky kladne. KMPC-146 T1 source/raw evidencia podporuje úspešné štyri
same-matrix multi-rank korekcie a izoluje PF-129 na JSON key-type parity.
KMPC-147 bol bez odchýlky reprodukovaný na T2, corrected field parity má
diff `0`, protected projekcia je exact a oba missing-input guardy sú
fail-closed. Evidencia preto podporuje interné účtovanie NIV `9/9`, C3
`45/45 logical PASS` a nezmenené K4 `60/100`, pričom konečné prijatie a
otvorenie ďalšieho kroku patrí výhradne hlavnému orchestrátorovi.

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, NIV/C3
registre ani K4 score. Hlavný orchestrátor musí audit samostatne spracovať
pred predregistráciou alebo spustením read-only C3 aggregate.
