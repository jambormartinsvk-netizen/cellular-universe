# Reprodukcia KMPC-131 NIV/k=0.15 a očakávania

Pracujte v novej dočasnej kópii adresára `REPRO`; package originál je
read-only. Z koreňa fresh kópie spustite procesy oddelene:

```powershell
python -c "from pathlib import Path; p=Path(r'scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"

python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --help

python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --smoke --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8

python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8
```

Každá vetva má mať vonkajší timeout `10 s`; worker cap je `4.8 s` a parent
guard `9.0 s`. Očakávané exit codes sú `0/0/0/0`. Smoke musí mať `4/4`
receipts, `physics_executed=false` a nesmie vytvoriť raw. Official musí
vytvoriť:

`scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json`

Očakávanie je technicky úplný generated JSON s
`candidate_interpretation_not_verdict=REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`
a `pair_pass=false`, nie PASS. Expected source hash runnera je
`45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2`;
four-shard base je
`7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23`.

## Field parity

Generated raw porovnajte s package reference
`EVIDENCE/008__KMPC131_NIV_K0p15_REVIEW_REFERENCE.json`. Povolená
normalizácia je výlučne:

- top-level `runtime_seconds`;
- `variants.gamma0.support_worker_runtime_seconds.accepted` a `.audit`;
- `variants.af0.support_worker_runtime_seconds.accepted` a `.audit`.

Po odstránení presne týchto piatich wall-time hodnôt musia byť všetky
ostatné polia identické. Environment nie je súčasťou frozen rawu, preto ho
auditor musí zapísať osobitne do response.

## Negatívne guardy

V druhej fresh kópii odstráňte iba
`RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json`
a spustite smoke. V tretej odstráňte iba
`RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json` a
smoke zopakujte. Očakávanie je v oboch prípadoch nonzero parent exit,
missing/hash-mismatch fail-closed, bez official outputu a bez fyzikálneho
verdiktu. Odstránenie robte iba v dočasných kópiách.

## Forenzné očakávania

- support `[-1,6]→[-1,8]`, M1 depth `8`, leading `j=-1`;
- ranky `104/104` a `130/130` pre oba varianty;
- štyri M3 driver metriky nad `1e-10`, ale všetky štyri holdouty pod
  `1e-9`;
- M3 common pod `1e-8`, tail pri `z=.01` pod `1e-6`, background worst `0`;
- žiadny technical failure, žiadny nový logical PASS a žiadny K4 score
  effect.
