# Reprodukcia EA-039 a exact field parity

Pracujte v novej dočasnej kópii `REPRO/`. Package originál nechajte
read-only. Z koreňa dočasnej kópie spustite oddelene:

```powershell
python -m py_compile scripts\baseScripts\p5_general_synchronous\c3_authoritative_logical_aggregate.py scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py

python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --help

python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --smoke

python scripts\392_script_KMPC_148_P5_3g7_C3_authoritative_logical_aggregate.py --aggregate
```

Vonkajší limit každého procesu je `10 s`; vnútorný official limit je
`4.8 s`. Očakávané exit codes sú `0/0/0/0`.

Smoke nesmie vytvoriť JSON a musí mať `pass=true`, všetkých `6/6` checks,
`physics_executed=false` a `workers=solvers=physics=matrices_built=0`.

Official musí vytvoriť generated JSON:

`scripts/results/k_mpc_005/RUN_KMPC_148_P5_3G7_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45.json`

Očakávaný candidate je
`PASS_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45_CANDIDATE_ONLY` a
`aggregate_gate_pass=true`.

## Exact register

Nezávisle od Python base zostavte presne 45 reťazcov:

```text
for mode in AD, CDI, BI, NID, NIV
  for k in 0.005, 0.05, 0.15
    for variant in nominal, gamma0, af0
      mode/k=k/variant
```

Generated `expected_register` aj `observed_register` sa musia rovnať tomuto
zoznamu v rovnakom poradí, bez duplicity. `mode_counts` musia byť
`AD=CDI=BI=NID=NIV=9`.

## Field parity

Pred exact rekurzívnym diffom generated JSON verzus
`EVIDENCE/003__KMPC148_PASS_REFERENCE.json` sa smie z oboch objektov
odobrať iba top-level pole:

`runtime_seconds`

Po odobratí musí zostať `0` rozdielov. Nijaký hash, cesta source,
identity, candidate, gate, register, count, scope ani operation count sa
normalizovať nesmie.

## Negatívne guardy

V dvoch osobitných fresh kópiách `REPRO/` odstráňte vždy iba jeden súbor a
spustite official:

1. pair guard:
   `scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_AD_K0p005_ZERO_VARIANT_PAIR.json`;
2. mode-authority guard:
   `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/206_KMPC_132_AND_C3_AD_MODE_CLOSURE_INTERNAL_AUDIT_SK.md`.

Každá vetva musí skončiť nonzero, vytvoriť iba technical-failure receipt,
nevytvoriť success raw a uviesť presnú missing príčinu. Failure musí mať
`TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`, nulové operation counts a žiadny
orchestrátorový verdikt. Guard výsledky sa neporovnávajú s PASS reference.

## Odchýlky

Zmena runnera, base, vstupu, SHA, output mena/cesty, runtime limitu alebo
priame volanie funkcie mimo official CLI je `DECLARED_DEVIATION` a
nepočíta sa do T2. Cross-platform diagnostika môže byť uvedená osobitne,
ale nemení projektový verdikt.
