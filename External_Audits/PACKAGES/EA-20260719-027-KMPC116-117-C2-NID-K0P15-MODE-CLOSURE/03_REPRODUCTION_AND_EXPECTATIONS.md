# Reprodukcia — EA-027

Pracuj v samostatných čerstvých kópiách adresára `REPRO`. Každý vedecký beh
má vnútorný deadline `4.8 s`; vonkajší procesný limit má byť aspoň `30 s`.
REPRO obsahuje pôvodné immutable KMPC-115 a KMPC-116 ako hashované runtime
prerequisites. KMPC-117 zámerne nie je prítomný.

## Negatívny dependency guard

V pomocnej kópii odober
`scripts/results/k_mpc_005/RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json`
a spusti:

```powershell
python scripts/360_script_KMPC_116_P5_3g7_C2_NID_k0p15_nominal.py --smoke --max-runtime-seconds 4.8
```

Očakáva sa nonzero exit v `static_hash_guard`, bez fyzikálneho volania a
bez success raw KMPC-116. Pomocnú kópiu potom zahoď.

## Prečo sú vetvy nezávislé

File SHA rawu zámerne zahŕňa aj `runtime_seconds`. Fieldovo zhodný fresh
KMPC-116 preto nemožno použiť ako exact-hash predchodcu KMPC-117. Každá
fáza začína z pôvodného hashovaného predchodcu a reprodukuje iba svoj cieľ.

## Vetva A — KMPC-116

V prvej fresh copy odstráň iba pôvodný KMPC-116 raw a spusti:

```powershell
python -m py_compile scripts/360_script_KMPC_116_P5_3g7_C2_NID_k0p15_nominal.py
python scripts/360_script_KMPC_116_P5_3g7_C2_NID_k0p15_nominal.py --help
python scripts/360_script_KMPC_116_P5_3g7_C2_NID_k0p15_nominal.py --smoke --max-runtime-seconds 4.8
python scripts/360_script_KMPC_116_P5_3g7_C2_NID_k0p15_nominal.py --atom --mode NID --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_116_P5_3G7_C2_NID_K0p15_NOMINAL.json --max-runtime-seconds 4.8
```

## Vetva B — KMPC-117

V druhej fresh copy ponechaj pôvodný KMPC-116. KMPC-117 v REPRO nie je;
spusti:

```powershell
python -m py_compile scripts/361_script_KMPC_117_P5_3g7_C2_NID_k0p15_same_matrix_refinement.py
python scripts/361_script_KMPC_117_P5_3g7_C2_NID_k0p15_same_matrix_refinement.py --help
python scripts/361_script_KMPC_117_P5_3g7_C2_NID_k0p15_same_matrix_refinement.py --smoke --max-runtime-seconds 4.8
python scripts/361_script_KMPC_117_P5_3g7_C2_NID_k0p15_same_matrix_refinement.py --atom --mode NID --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_117_P5_3G7_C2_NID_K0p15_SAME_MATRIX_REFINEMENT.json --max-runtime-seconds 4.8
```

Všetkých osem príkazov má exit `0`. Generated raw každej vetvy sa porovná
s Evidence 004 alebo 006 po rekurzívnom odrátaní iba polí nazvaných
`runtime_seconds` a po normalizácii iba absolútneho root prefixu poľa
`frozen_B1_left_null_Bianchi.frozen_algebra_source`. Relatívny suffix
`scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py` musí
zostať zhodný. Generated KMPC-116 sa nepoužije ako prerequisite vetvy B.

Očakávané jadro:

- KMPC-116 candidate `REVIEW_C2_CORE_GATE_UNCLOSED`, false iba M3 driver;
- KMPC-117 candidate
  `PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`, exact same matrix,
  tri corrections a všetky technical/physics brány true;
- C2 dopad vzniká až interným auditom Evidence 007.

Obídenie runnera, zmena prahu alebo ručné vloženie rawu je
`DECLARED_DEVIATION` a nedosahuje T2 deklarovanej vetvy.
