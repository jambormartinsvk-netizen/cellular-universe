# Reprodukcia KMPC-141 a očakávania

Pracujte v novej dočasnej kópii adresára `REPRO`; package originál je
read-only. Z koreňa tejto kópie spustite oddelene:

```powershell
python -c "from pathlib import Path; p=Path(r'scripts\385_script_KMPC_141_P5_3g7_C3_BI_k0p15_supersession_scope_correction.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"

python scripts\385_script_KMPC_141_P5_3g7_C3_BI_k0p15_supersession_scope_correction.py --help

python scripts\385_script_KMPC_141_P5_3g7_C3_BI_k0p15_supersession_scope_correction.py --smoke --mode BI --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8

python scripts\385_script_KMPC_141_P5_3g7_C3_BI_k0p15_supersession_scope_correction.py --audit --mode BI --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8
```

Všetky vetvy majú vonkajší timeout `10 s`; vnútorný read-only cap je
`4.8 s`. Očakávanie: exit `0`, smoke `physics_executed=false`, official
`pair_pass=true`, `HP_M1_exact_resume_pass=true`, worker/solver calls `0`.

Generated output:

`scripts/results/k_mpc_005/RUN_KMPC_141_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_LOCAL_45S_HP_M1_EXACT_RESUME_SUPERSESSION_SCOPE_CORRECTED.json`.

Porovnajte ho s `EVIDENCE/013`. Normalizovať sa smie iba top-level
`runtime_seconds`; source hashe, fyzikálne hodnoty, thresholdy, identity,
brány ani protected snapshot hash sa nesmú meniť.

## Negatívny guard

V druhej čistej dočasnej kópii odstráňte prerequisite
`RUN_KMPC_140_...READ_ONLY_AGGREGATE.json` a spustite smoke. Očakávanie je
nenulový exit pred outputom, správa `frozen source missing`, žiadna fyzika a
žiadny generated success JSON.

## T1 exact kontroly

Bez spustenia exact fyziky overte:

- raw `012`: coefficient `4/4`, exact `2/2`, runtimes
  `19.922/21.344 s`, oba driver a non-fit holdout PASS;
- runner `015`: lokálny owner prijíma iba presne `45.0`, obnovuje pôvodného
  ownera a coefficient limit ostáva `4.8`;
- raw `014`: historical exact authority má limit `45 s`;
- raw `013`: scientific snapshot before/after je identický a thresholdy sa
  nezmenili.

## Očakávaný auditný záver

Read-only KMPC-141 by mal dosiahnuť T2. 45-s exact vetva zostáva T1 aj pri
úspešnej statickej kontrole. Projektový BI `9/9` je predmetom read-only
odporúčania auditora, nie nového autoritatívneho verdictu.
