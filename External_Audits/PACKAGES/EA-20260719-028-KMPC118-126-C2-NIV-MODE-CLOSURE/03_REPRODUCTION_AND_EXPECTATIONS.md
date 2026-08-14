# Reprodukcia — EA-028

Každá vetva začína v samostatnej čerstvej kópii `REPRO`. Vnútorný deadline
je `4.8 s`, vonkajší limit aspoň `30 s`. Originálne rawy v REPRO sú iba
exact-hash prerequisites; freshly generated raw jednej vetvy sa nikdy
nepoužije ako predchodca inej vetvy.

## Negatívny guard

Odstráň KMPC-056 prerequisite aj cieľový KMPC-118 raw a spusti:

```powershell
python scripts/362_script_KMPC_118_P5_3g7_C2_NIV_k0p005_nominal.py --smoke --max-runtime-seconds 4.8
```

Očakáva sa exit `2` v static hash guard, bez fyziky a bez success raw.

## Spoločný postup jednej success vetvy

V čerstvej kópii odstráň iba cieľový raw z tabuľky a spusti:

```powershell
python -m py_compile <RUNNER>
python <RUNNER> --help
python <RUNNER> --smoke --max-runtime-seconds 4.8
python <RUNNER> --atom --mode NIV --k-mpc <K> --output <OUTPUT> --max-runtime-seconds 4.8
```

| Run | Runner | K | Output | Očakávanie |
|---|---|---:|---|---|
| 118 | `scripts/362_script_KMPC_118_P5_3g7_C2_NIV_k0p005_nominal.py` | .005 | `scripts/results/k_mpc_005/RUN_KMPC_118_P5_3G7_C2_NIV_K0p005_NOMINAL.json` | tail-only REVIEW |
| 119 | `scripts/363_script_KMPC_119_P5_3g7_C2_NIV_k0p005_support_06_checkpoint.py` | .005 | `scripts/results/k_mpc_005/RUN_KMPC_119_P5_3G7_C2_NIV_K0p005_SUPPORT_06_ACCEPTED_CHECKPOINT.json` | complete checkpoint, no verdict |
| 120 | `scripts/364_script_KMPC_120_P5_3g7_C2_NIV_k0p005_support_06_08_checkpoint_resume.py` | .005 | `scripts/results/k_mpc_005/RUN_KMPC_120_P5_3G7_C2_NIV_K0p005_SUPPORT_06_08_CHECKPOINT_RESUME.json` | scoped PASS candidate |
| 121 | `scripts/365_script_KMPC_121_P5_3g7_C2_NIV_k0p15_nominal.py` | .15 | `scripts/results/k_mpc_005/RUN_KMPC_121_P5_3G7_C2_NIV_K0p15_NOMINAL.json` | core+tail REVIEW |
| 122 | `scripts/366_script_KMPC_122_P5_3g7_C2_NIV_k0p15_same_matrix_refinement.py` | .15 | `scripts/results/k_mpc_005/RUN_KMPC_122_P5_3G7_C2_NIV_K0p15_SAME_MATRIX_REFINEMENT.json` | tail-only REVIEW |
| 123 | `scripts/367_script_KMPC_123_P5_3g7_C2_NIV_k0p15_support_06_checkpoint.py` | .15 | `scripts/results/k_mpc_005/RUN_KMPC_123_P5_3G7_C2_NIV_K0p15_SUPPORT_06_ACCEPTED_CHECKPOINT.json` | incomplete no-verdict checkpoint |
| 126 | `scripts/370_script_KMPC_126_P5_3g7_C2_NIV_k0p15_support_06_08_multi_rank_refinement.py` | .15 | `scripts/results/k_mpc_005/RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json` | scoped PASS candidate |

Všetky štyri príkazy každej success vetvy majú exit `0`. Porovnaj raw s
príslušným Evidence po povolenej normalizácii runtime/root prefixu.

## PF-114 vetva

S originálnym incomplete KMPC-123 spusti compile/help a smoke runnera 368.
Smoke musí skončiť exit `2` pre `checkpoint_complete=false`; official sa
nespúšťa a success raw nesmie vzniknúť.

## PF-115 vetva

V čerstvej kópii odstráň failure raw KMPC-125 a spusti compile/help/smoke a
official runnera 369 rovnakým postupom. Prvé tri príkazy majú exit `0`,
official exit `2`; generated failure JSON musí mať status
`TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`, phase `audit` a
`KeyError('same_matrix_refinement')`.

Obídenie runnera, zmena prahu, ručné doplnenie checkpoint flagu alebo
vloženie generated rawu ako exact-hash predchodcu je `DECLARED_DEVIATION`
a nedosahuje T2 deklarovanej vetvy.

## Interný fresh-copy preflight pred zapečatením

Dňa 2026-07-19 prešlo všetkých desať nezávislých vetiev (`10/10`):

| Vetva | compile/help/smoke/official | Official wall time | Field parity / guard |
|---|---|---:|---|
| negative | `-/-/2/-` | 1.410 s | bez success rawu |
| KMPC-118 | `0/0/0/0` | 3.190 s | PASS |
| KMPC-119 | `0/0/0/0` | 2.790 s | PASS |
| KMPC-120 | `0/0/0/0` | 2.370 s | PASS |
| KMPC-121 | `0/0/0/0` | 3.470 s | PASS |
| KMPC-122 | `0/0/0/0` | 3.610 s | PASS |
| KMPC-123 | `0/0/0/0` | 2.720 s | PASS; checkpoint ostal incomplete/no-verdict |
| KMPC-126 | `0/0/0/0` | 5.500 s | PASS |
| KMPC-124 / PF-114 | `0/0/2/NOT_RUN` | 1.090 s | bez success rawu |
| KMPC-125 / PF-115 | `0/0/0/2` | 5.460 s | failure raw exact parity |

Čerstvé success rawy mali po odstránení iba `runtime_seconds` a po
normalizácii iba root prefixu `frozen_algebra_source` field-level paritu
s Evidence 004, 006, 008, 011, 013, 015 a 020. PF-115 mal exact SHA-256
`1ED339AE9FBA7BA27C066A659926B0B822029F8BC3CF0AE4844DF4845E3A31D0`.
Preflight nemení autoritatívne rawy ani fyzikálne verdikty.
