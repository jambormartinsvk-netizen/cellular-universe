# External audit response — EA-047-R2 P0 control follow-up

**CONTROL_REPAIR_RESULT:** `PASS_P0_CONTROL_REPAIR`  
**ADVISORY_RECOMMENDATION:** `AGREE_IN_SCOPE`  
**TIER:** `P0_CONTROL_REPAIR_AUDIT` (static package-only follow-up; parent T2 not rerun)  
**PACKAGE_CLASS:** `PACKAGE_REPAIR_REVISION`  
**PACKAGE_ID:** `EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE`  
**REPAIRS_PACKAGE_ID:** `EA-20260801-047-R1-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-REPAIR`  
**TASK_ID:** `V318-PT1-H0-S8-EA047-R2-EXTERNAL-P0-FOLLOWUP-20260801`  
**CHECKPOINT_ID:** `CP-RELEASE-V318-PT1-H0-S8-C2C3-20260801-001`  
**PARENT_CHECKPOINT_IDS:** `NONE_FIRST_RELEASE_DIAGNOSTIC_CHECKPOINT`  
**AUDIT_SUBMISSION_ID:** `SUB-20260801-047-R2-001`  
**PACKAGE_MANIFEST_SHA256:** `B6EE1EABEAFA52210465DE4E08C445B282421CDEA10AB550F858C0862661A6BF`

## Auditor identity and independence

- Actual agent/task identity: `/root/v318_pt1_h0_s8_external_auditor`.
- Role: `external_auditor`; model/version: `OpenAI gpt-5.6-sol`; reasoning profile: `high`.
- Environment: Windows / PowerShell, workspace `D:\Teoria`, timezone `Europe/Bratislava`, audit date `2026-08-01`.
- Execution environment: `NOT_RUN_P0_STATIC_FOLLOWUP`; network not used; Python and scientific commands not run; generated JSON: `none`.
- Artifact/package curator: `/root`; auditor: `/root/v318_pt1_h0_s8_external_auditor`. These identities differ. The assigned auditor identity also differs from the static preseal reviewer `/root/v318_pt1_h0_s8_preseal_review`. `SEPARATION_OF_DUTIES_CHECK=PASS`.
- I did not author or curate the sealed package and did not inspect sibling submission responses. `EVIDENCE/030__EA047_EXTERNAL_RESPONSE.md` was read only because this prior R1 response is an explicitly hash-approved evidence item in the R2 charter.

## Bootstrap and package closure

The sealed charter contains an explicit `AUDITOR_RULESET_PATHS_AND_SHA256` map. The packaged ruleset/profile bytes match it exactly:

- `EVIDENCE/001__AGENTS.md`: `472F31C5CAE790EFA16A815BE3183B7A2C1438E4961B2BE4A16AEAE0FF57BA72`
- `EVIDENCE/002__PROJECT_OPERATING_SYSTEM.md`: `45CDDF6CBD458CC8C18147C438557143E1EB962BB159058070A8CAA7E866921E`
- `EVIDENCE/003__AUDITOR_PACKAGE_PROTOCOL_R8.md`: `F0F8DB2F7A63666709CCC77E92B80C95F895752E3A16DDF62AA77B0D1D96279C`
- `EVIDENCE/004__EXTERNAL_AUDITOR_ROLE.toml`: `98E55F94679F49D4DCE08E3281AE2A38F899B896E25726F9A3C2A85A9FC997E3`

Manifest closure passes: 37 manifest rows, 40 sealed package files, 30 evidence files, two REPRO files, two runtime-map entries, no missing copies, no copy-hash mismatches, no declared source/copy mismatches for copied evidence, and no runtime hash mismatch. The exact R1 response is present as `EVIDENCE/030__EA047_EXTERNAL_RESPONSE.md` with SHA-256 `FB55DA8D5FE55D85C7D7776EA27B391235A95F03658A847CFED0A94862E9E8D1`. Evidence `001–029` and both REPRO files retain their manifest-declared source hashes byte-for-byte.

Pre-response package inventory SHA-256 (UTF-8 encoding of sorted `relative_path<TAB>file_sha256` rows): `0315D371662D58829D51B7073511560E0D3ECA06F2BF456EDF9F06302501B7E2`.  
Post-response package inventory SHA-256: `0315D371662D58829D51B7073511560E0D3ECA06F2BF456EDF9F06302501B7E2` (40 files; exit `0`; wall `196 ms`). Package immutability therefore passes.

## Corrected control-contract assessment

The corrected `02_AUDITOR_INSTRUCTIONS.md` and `03_REPRODUCTION_AND_EXPECTATIONS.md` remove the prior contradiction without weakening fresh-chain integrity:

1. Fresh whole-file SHA binding is exact and unnormalized. The sealed runner hashes the actual input file and rejects a mismatch before parsing it.
2. Segment A records the actual fresh reference-file hash. Segments B and C record that same actual reference hash plus the actual whole-file hash of their immediate fresh predecessor. The sealed base validates the expected predecessor SHA, its schema/lineage/verdict/mapping, and the embedded reference hash before continuation.
3. Aggregation independently binds the actual fresh reference and model files to the supplied expected hashes and rechecks the model-to-reference lineage.
4. Accepted-output parity permits differences only in fields that necessarily change when the independently rerun whole-file chain changes: `runtime_seconds`; plus `reference_stage_sha256` for A; plus `reference_stage_sha256` and `predecessor_segment_sha256` for B/C. Those dynamic hashes are not ignored: each must equal the actual corresponding fresh file hash.
5. No physics, state, bracket, count, guard, threshold, identity, schema, path, frozen-input, comparator, verdict, or final aggregate field is excepted. This makes stable-field parity strict while preserving stronger, exact provenance binding for the fresh chain.

Therefore the R1 closure blocker `EA047-R1-EXT-P0-001` is resolved, and the earlier parity-control contradiction addressed by this repair is closed at the package-control layer. No new material finding was identified.

## Finding disposition and implications

**Finding disposition:** `EA047-R1-EXT-P0-001` — `P0_PACKAGE_PROCESS_ONLY` — resolved by R2 package-control repair.  
**CLAIM_REACH:** `NONE`  
**EARLIEST_POSSIBLY_INVALID_CHECKPOINT:** `NONE`  
**KNOWN_DOWNSTREAM_CLAIMS:** `NONE_INVALIDATED`  
**SMALLEST_WORKFLOW_RETURN_POINT:** main orchestrator assessment of this response; no DEV, RC, official, or internal-science rerun.

- Mathematical/logical implication: none to the sealed scientific equations, numerical values, decision thresholds, or internally audited conclusion. The repaired contract is logically consistent because parity-field exceptions are paired with exact fresh-file hash validation.
- Physical implication: none; no covariance, conservation, gauge, causality, stability, unit, limit, or observable claim is changed.
- Philosophical/track-identity implication: none; no mechanism, state space, interaction topology, causal architecture, ontology, or explanatory target is changed. Track creation/termination is outside this audit.

This response does not assign project `PASS/REVIEW/STOP`, score, depth, release status, official-run permission, checkpoint acceptance, or track decision. Those remain with the main orchestrator/author under the packaged rules.

## Exact read-only command record

All commands were package-local or targeted the one authorized response template. Exit codes and measured wall times below are actual.

Primary manifest verifier (exit `0`, internal wall `249 ms`):

```powershell
$sw=[System.Diagnostics.Stopwatch]::StartNew(); $pkg='D:\Teoria\External_Audits\PACKAGES\EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE'; $tsv=Join-Path $pkg '01_MANIFEST_SHA256.tsv'; $rows=Import-Csv -LiteralPath $tsv -Delimiter "`t"; $errs=[System.Collections.Generic.List[string]]::new(); foreach($row in $rows){ $copy=Join-Path $pkg $row.copy_path; if(-not (Test-Path -LiteralPath $copy -PathType Leaf)){ $errs.Add("MISSING_COPY=$($row.copy_path)"); continue }; $h=(Get-FileHash -Algorithm SHA256 -LiteralPath $copy).Hash; if($h -ne $row.copy_sha256){ $errs.Add("COPY_HASH_MISMATCH=$($row.copy_path)") }; if($row.source_path -ne 'PACKAGE_GENERATED' -and $row.source_sha256 -ne $row.copy_sha256){ $errs.Add("DECLARED_SOURCE_COPY_MISMATCH=$($row.copy_path)") } }; $all=Get-ChildItem -LiteralPath $pkg -File -Recurse; $ev=Get-ChildItem -LiteralPath (Join-Path $pkg 'EVIDENCE') -File; $rp=Get-ChildItem -LiteralPath (Join-Path $pkg 'REPRO') -File -Recurse; if($rows.Count -ne 37){$errs.Add("MANIFEST_ROW_COUNT=$($rows.Count)")}; if($all.Count -ne 40){$errs.Add("PACKAGE_FILE_COUNT=$($all.Count)")}; if($ev.Count -ne 30){$errs.Add("EVIDENCE_FILE_COUNT=$($ev.Count)")}; if($rp.Count -ne 2){$errs.Add("REPRO_FILE_COUNT=$($rp.Count)")}; $runtimeRows=Import-Csv -LiteralPath (Join-Path $pkg '04_RUNTIME_DEPENDENCY_MAP.tsv') -Delimiter "`t"; $runtimePaths=@($runtimeRows.runtime_path | Sort-Object); $reproPaths=@($rp | ForEach-Object {$_.FullName.Substring($pkg.Length+1).Replace('\','/')} | Sort-Object); if(($runtimePaths -join '|') -ne ($reproPaths -join '|')){$errs.Add("RUNTIME_MAP_PATH_MISMATCH")}; foreach($rr in $runtimeRows){$rh=(Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $pkg $rr.runtime_path)).Hash; if($rh -ne $rr.sha256){$errs.Add("RUNTIME_HASH_MISMATCH=$($rr.runtime_path)")}}; $temps=@($all | Where-Object {$_.Name -match '(?i)(\.tmp$|~$|\.bak$|\.orig$)'}); if($temps.Count -ne 0){$errs.Add("TEMP_FILES=$($temps.Count)")}; $dups=@($rows | Group-Object copy_path | Where-Object Count -gt 1); if($dups.Count -ne 0){$errs.Add("DUPLICATE_MANIFEST_PATHS=$($dups.Count)")}; $inventoryLines=@($all | Sort-Object FullName | ForEach-Object { $rel=$_.FullName.Substring($pkg.Length+1).Replace('\','/'); "$rel`t$((Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash)" }); $inventoryText=($inventoryLines -join "`n"); $sha=[System.Security.Cryptography.SHA256]::HashData([System.Text.Encoding]::UTF8.GetBytes($inventoryText)); $inventoryHash=[Convert]::ToHexString($sha); $sw.Stop(); "MANIFEST_ROWS=$($rows.Count)"; "PACKAGE_FILES=$($all.Count)"; "EVIDENCE_FILES=$($ev.Count)"; "REPRO_FILES=$($rp.Count)"; "RUNTIME_ENTRIES=$($runtimeRows.Count)"; "ERROR_COUNT=$($errs.Count)"; $errs; "PACKAGE_INVENTORY_SHA256=$inventoryHash"; "WALL_MS=$($sw.ElapsedMilliseconds)"; if($errs.Count){exit 1}else{exit 0}
```

Static source slices (exit `0`, wall `208 ms`) were read with:

```powershell
$sw=[System.Diagnostics.Stopwatch]::StartNew(); $pkg='D:\Teoria\External_Audits\PACKAGES\EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE'; $runner=Join-Path $pkg 'REPRO\scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py'; $base=Join-Path $pkg 'REPRO\scripts\baseScripts\release_v318_h0_s8_legacy_sensitivity_dev.py'; $rl=Get-Content -LiteralPath $runner; $bl=Get-Content -LiteralPath $base; foreach($range in @(@('RUNNER',49,205),@('BASE_CHAIN',854,1100),@('BASE_AGGREGATE',1261,1335))){$label=$range[0];$a=[int]$range[1];$b=[int]$range[2];"===== $label $a-$b ====="; $src=if($label -eq 'RUNNER'){$rl}else{$bl}; for($i=$a;$i -le $b;$i++){"$i|$($src[$i-1])"}}; $sw.Stop(); "WALL_MS=$($sw.ElapsedMilliseconds)"
```

Final consolidated assertion (exit `0`, internal wall `244 ms`) used the same package-local hash/inventory logic, additionally asserting the four charter hashes, E030 hash, scope/instruction/contract hashes, curator/auditor identity tokens, corrected-contract tokens, and sealed-source SHA-binding tokens. Its result was `RULESET_HASHES=4/4`, `ERRORS=0`, and package inventory `0315D371662D58829D51B7073511560E0D3ECA06F2BF456EDF9F06302501B7E2`.

## Deviations

Three preliminary PowerShell checker invocations exited `1` because of auditor command construction errors, not package content:

1. Generic manifest/runtime names were assumed (`PACKAGE_PATH`, `COPY_SHA256`, `04_RUNTIME_MAP.txt`); exit `1`, internal wall `362 ms`.
2. A consolidated check used shortened evidence filenames and English token spellings not present in the sealed package; exit `1`, internal wall `353 ms`.
3. After correcting filenames, that check still used abbreviated/stale expected ruleset hash literals rather than the full charter literals; exit `1`, internal wall `249 ms`.

Each failed command was read-only, performed no Python/scientific execution, generated no JSON, and left the package inventory hash unchanged: `PACKAGE_EFFECT=NONE`; `SCIENCE_EFFECT=NONE`. The corrected manifest and consolidated checks then passed. No package, evidence, source, preregistration, raw, threshold, plan, scorecard, manifest, or register was edited.

## Nonclaims and handoff

- This P0 follow-up does not independently rerun or enlarge the parent T2 scientific audit.
- It does not re-estimate the nine high-grid cells, reinterpret historical DEV incidents, or alter the parent T2 recommendation.
- It confirms only that the R2 package closes the R1 bootstrap defect and repairs the fresh-chain/parity control contradiction while preserving byte-identical scientific evidence.
- Direct handoff: main orchestrator should assess this advisory response. No new package, DEV/RC/official rerun, internal science audit, project verdict, or track decision is requested by this auditor.

## Artifact accounting

`LIVE_SCIENTIFIC_ARTIFACTS=0`  
`LIVE_CENTRAL_REGISTERS_UPDATED=0`  
`AUDIT_PACKAGE_COPIES=40` (unchanged)  
`AUDITOR_RESPONSE_FILES_WRITTEN=1`
