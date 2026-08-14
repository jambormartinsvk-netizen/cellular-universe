# KMPC-056 — NIV support step 2: finite-owner technický nástupca

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_PASS / AUTHORITATIVE_PASS_NIV_SUPPORT_MINUS1_4_ADEQUATE`  
**Fyzický scope:** presne KMPC-055, bez zmeny rovníc, supportov, M1 hĺbky,
prahov, plôch, parametra alebo rozhodovacieho stromu.

## Jediná povolená oprava

V1 modul nesprávne volal `niv_c1_coverage._all_finite`. Skutočný vlastník
je `nid_c1_coverage._all_finite`, ktorý už NIV modul používa interne.
Versioned V2 overlay smie počas smoke/auditu:

1. overiť presnú callable identity skutočného ownera;
2. dočasne pripojiť túto callable pod očakávané meno V1;
3. spustiť nezmenený V1 výpočet;
4. obnoviť pôvodný stav owner namespace v `finally`;
5. nahradiť iba source-hash mapu payloadu úplným V2 closure.

Smoke musí helper skutočne zavolať na vnorenom payload-e s native aj NumPy
skalárom a overiť obnovu namespace. V1 base, runner 299 a failure JSON sa
nemenia a zostávajú `DO_NOT_RUN_AUDIT_TECHNICAL`.

## Artefakty

- base: `scripts/baseScripts/p5_general_synchronous/niv_support_step2_v2_finite_owner.py`;
- runner: `scripts/300_script_KMPC_056_P5_3g7_NIV_support_step2_finite_owner_successor.py`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json`.

Interný limit `4.8 s`, vonkajší `10 s`; compile, help, smoke, čistá cesta a
presne jeden audit. Technický counter po PF-076 je `1/10`; úspešný vecný
výpočet ho vynuluje.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | PF-076 zapísaný, V1 a runner 299 zakázané pre audit | `PREREGISTERED_SUCCESSOR` |
| 2026-07-18 | V2 base SHA `F920F51313B44450DABC5A526769C42CD9A3988CBEB011A7954A0F88A4A7006D`; runner SHA `5D338FA0A6BFDAA6946EC829B2BD7CA87CED12639686E0B1C38A33A8D63ED301` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base/runner, `--help`, owner-behavior smoke | `PASS / PASS / PASS / PASS` |
| 2026-07-18 | jediný audit, external exit `0`, internal `2.766 s`; JSON SHA `9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332` | `TECHNICAL_PASS` |
| 2026-07-18 | regression, M1 depth-6, core, common, tail `5,6` a owner restore prešli | `PASS_NIV_SUPPORT_MINUS1_4_ADEQUATE_AT_K005_NOMINAL` |
