# Reprodukcia — EA-026

Pracuj v samostatných čerstvých kópiách adresára `REPRO`. Každý vedecký beh
má vnútorný deadline `4.8 s`; vonkajší procesný limit má byť aspoň `30 s`.
REPRO obsahuje pôvodné immutable KMPC-113 a KMPC-114 ako hashované runtime
prerequisites. KMPC-115 zámerne nie je prítomný.

## Negatívny dependency guard

V pomocnej kópii odober runtime prerequisite:

`scripts/results/k_mpc_005/RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json`

Spusť:

```powershell
python scripts/357_script_KMPC_113_P5_3g7_C2_NID_k0p005_nominal.py --smoke --max-runtime-seconds 4.8
```

Očakáva sa nonzero exit v `static_hash_guard`, bez fyzikálneho volania a bez
success raw KMPC-113. Pomocnú kópiu potom zahoď; súbor neobnovuj ručne v
tej istej vetve.

## Prečo musia byť tri vetvy nezávislé

Celý immutable SHA rawu zámerne zahŕňa aj `runtime_seconds`. Nová field-level
reprodukcia teda po odrátaní runtime polí môže byť obsahovo zhodná, ale má
iný file SHA. Taký generated raw sa nesmie vložiť ako predchodca ďalšej
fázy, pretože by obchádzal jej exact-hash guard. Každá fáza preto začína z
pôvodného hashovaného predchodcu a reprodukuje iba svoj cieľ.

## Vetva A — KMPC-113

V prvej fresh copy odstráň iba pôvodný
`RUN_KMPC_113_P5_3G7_C2_NID_K0p005_NOMINAL.json`, potom spusti:

```powershell
python -m py_compile scripts/357_script_KMPC_113_P5_3g7_C2_NID_k0p005_nominal.py
python scripts/357_script_KMPC_113_P5_3g7_C2_NID_k0p005_nominal.py --help
python scripts/357_script_KMPC_113_P5_3g7_C2_NID_k0p005_nominal.py --smoke --max-runtime-seconds 4.8
python scripts/357_script_KMPC_113_P5_3g7_C2_NID_k0p005_nominal.py --atom --mode NID --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_113_P5_3G7_C2_NID_K0p005_NOMINAL.json --max-runtime-seconds 4.8
```

## Vetva B — KMPC-114

V druhej fresh copy ponechaj pôvodný KMPC-113 a odstráň iba pôvodný
KMPC-114 checkpoint, potom spusti:

```powershell
python -m py_compile scripts/358_script_KMPC_114_P5_3g7_C2_NID_k0p005_support_07_checkpoint.py
python scripts/358_script_KMPC_114_P5_3g7_C2_NID_k0p005_support_07_checkpoint.py --help
python scripts/358_script_KMPC_114_P5_3g7_C2_NID_k0p005_support_07_checkpoint.py --smoke --max-runtime-seconds 4.8
python scripts/358_script_KMPC_114_P5_3g7_C2_NID_k0p005_support_07_checkpoint.py --atom --mode NID --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_114_P5_3G7_C2_NID_K0p005_SUPPORT_07_ACCEPTED_CHECKPOINT.json --max-runtime-seconds 4.8
```

## Vetva C — KMPC-115

V tretej fresh copy ponechaj pôvodné KMPC-113 aj KMPC-114. KMPC-115 v
REPRO nie je; spusti:

```powershell
python -m py_compile scripts/359_script_KMPC_115_P5_3g7_C2_NID_k0p005_support_07_09_checkpoint_resume.py
python scripts/359_script_KMPC_115_P5_3g7_C2_NID_k0p005_support_07_09_checkpoint_resume.py --help
python scripts/359_script_KMPC_115_P5_3g7_C2_NID_k0p005_support_07_09_checkpoint_resume.py --smoke --max-runtime-seconds 4.8
python scripts/359_script_KMPC_115_P5_3g7_C2_NID_k0p005_support_07_09_checkpoint_resume.py --atom --mode NID --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_115_P5_3G7_C2_NID_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json --max-runtime-seconds 4.8
```

Všetkých dvanásť príkazov má exit `0`. Generated raw každej vetvy sa
porovná s Evidence 004, 006 alebo 008 po rekurzívnom odrátaní iba polí
nazvaných `runtime_seconds` a po normalizácii iba absolútneho root prefixu
poľa `frozen_B1_left_null_Bianchi.frozen_algebra_source`. Jeho relatívny
suffix `scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py`
musí byť presne zhodný. Generated raw jednej vetvy sa nikdy nepoužije ako
prerequisite inej vetvy.

Očakávané jadro:

- KMPC-113 candidate `REVIEW_C2_NID_K0p005_SUPPORT_07_09_REQUIRED`, netail
  PASS a tail false iba pre rozhodovací tail rozsah;
- KMPC-114 checkpoint-only bez fyzikálneho verdictu a všetky preconditions
  true;
- KMPC-115 candidate
  `PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`, všetky technical
  a physics brány true a najhorší `.01` tail pod `1e-6`;
- C2 dopad vzniká až interným auditom Evidence 009.

Ak sa runner obíde priamym volaním modulu, zmenou prahu alebo ručným
vložením checkpointu, výsledok označ `DECLARED_DEVIATION` a neudeľ T2
deklarovanej vetve.
