# Reprodukcia KMPC-145 a očakávania

Pracujte v novej dočasnej kópii adresára `REPRO`; package originál je
read-only. Z koreňa tejto kópie spustite oddelene:

```powershell
python -c "from pathlib import Path; p=Path(r'scripts\389_script_KMPC_145_P5_3g7_C3_NID_k0p15_read_only_parity_scope_correction.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"

python scripts\389_script_KMPC_145_P5_3g7_C3_NID_k0p15_read_only_parity_scope_correction.py --help

python scripts\389_script_KMPC_145_P5_3g7_C3_NID_k0p15_read_only_parity_scope_correction.py --smoke --mode NID --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8

python scripts\389_script_KMPC_145_P5_3g7_C3_NID_k0p15_read_only_parity_scope_correction.py --audit --mode NID --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8
```

Každá vetva má vonkajší timeout `10 s`; vnútorný read-only cap je `4.8 s`.
Očakávanie: exit `0`, smoke `physics_executed=false`, official
`pair_pass=true`, všetkých 14 correction checks true a operation counts
`workers=solvers=cpqr=0`.

Generated output:

`scripts/results/k_mpc_005/RUN_KMPC_145_P5_3G7_C3_NID_K0p15_PARITY_SCOPE_CORRECTION.json`.

Porovnajte ho s package reference
`EVIDENCE/017__KMPC145_NID_K0p15_PASS_REFERENCE.json`. Normalizovať sa smie
iba top-level `runtime_seconds`; protected snapshot, varianty, coefficienty,
residualy, holdout, prahy, identity, brány a source hashe sa nesmú meniť.

## Negatívne guardy

V druhej čistej dočasnej kópii odstráňte iba KMPC-131 prerequisite a
spustite smoke. V tretej odstráňte iba KMPC-144 prerequisite a zopakujte
smoke. Očakávanie v oboch prípadoch: exit `2`, správa
`immutable input missing or hash-mismatched`, žiadna fyzika a žiadny nový
success JSON. Odstránenie robte iba v dočasných kópiách.

## T1 forenzné kontroly

- `.005`: raw `014` má pair PASS na `[0,7]→[0,9]`;
- `.05`: `015→016` zachová accepted solve a tri same-matrix korekcie znížia
  oba audit drivery pod `1e-10`, holdout ostáva nezávislý a PASS;
- `.15`: vstupy v `REPRO` dokazujú gamma0 PASS, af0 driver refinement na
  identickej matici a presnú dvojicu parent parity false-negative checks;
- finálny `017`: protected snapshot SHA pred/po
  `EBD4021F5BC285551D2EE8DC521E0A9DE23BA6D61CDE5D6DEBAE473BAA2FD97D`.

## Očakávaný auditný záver

Read-only KMPC-145 by mal dosiahnuť T2. Numerické vetvy zostávajú T1 aj pri
úspešnej forenznej kontrole. Projektový NID `9/9` a C3 `39/45` sú predmetom
read-only odporúčania auditora, nie nového autoritatívneho verdiktu.
