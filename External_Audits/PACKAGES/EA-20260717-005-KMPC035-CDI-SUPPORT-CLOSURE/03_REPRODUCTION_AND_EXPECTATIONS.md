# Reprodukcia EA-005 — KMPC-035 closure

**Reproduction root:** `REPRO/`  
**Interný limit:** presne `4.8 s` pre pôvodný KMPC-035 smoke/audit  
**Externý limit:** `10 s` na proces  
**Generated output:** na začiatku nesmie existovať
`REPRO/scripts/results/k_mpc_005/RUN_EA005_KMPC035_REPRODUCTION_CLOSURE.json`

Adresár výsledkov obsahuje KMPC-034 JSON ako explicitný
`runtime-prerequisite`, nie ako generated výsledok tohto balíka.

## Očakávaný smoke

```bash
timeout 10s python REPRO/scripts/281_script_EA005_KMPC035_external_reproduction_closure.py --smoke --max-runtime-seconds 4.8
```

Očakávanie: exit `0`, official KMPC-035 smoke PASS, runtime/source hash
closure PASS a atomic collision fixture:

```text
collision_caught=true
target_unchanged=true
temp_files_after_collision=[]
```

## Očakávaný official audit

```bash
timeout 10s python REPRO/scripts/281_script_EA005_KMPC035_external_reproduction_closure.py --audit --max-runtime-seconds 4.8 --output scripts/results/k_mpc_005/RUN_EA005_KMPC035_REPRODUCTION_CLOSURE.json
```

Očakávanie: proces technicky dobehne a zapíše immutable generated JSON.
Pôvodný strict regression prah ostáva `1e-12`; na inej BLAS platforme smie
official candidate skončiť `REVIEW_REGRESSION_OR_FORMULA_DRIFT`. To nie je
technický pád ani dôvod meniť prah.

Bez ohľadu na strict regression sa majú porovnať tieto invariantné/scoped
polia:

| Kontrola | Reference pattern |
|---|---|
| support count | F0 `4/8/12`; M3 `26/52/78` |
| common bridge | hlboko pod `1e-8` |
| tail `z=1e-4` | autoritatívny PASS oboch sektorov |
| tail `z=1e-2` | FAIL iba F0 `delta_f` a M3 `sigma_fs` |
| F0 fail metric | približne `2.524016e-5` |
| M3 fail metric | približne `3.216708e-3` |
| cross-platform diagnostic | 180 koeficientov; prah `1e-9/1e-13`; verdict effect NONE |

## Vyhodnotenie tieru

- Manifest + smoke + official audit bez obídenia guardov a s generated JSON:
  kandidát na `T2_REPRODUCIBLE_CALCULATION`.
- Chýbajúci prerequisite, timeout, exception alebo obídenie official vetvy:
  T2 sa neudeľuje; fyzika `NOT_RUN` alebo iba declared deviation.
- Rovnaký imported equation engine nikdy nie je T3, ani pri exact arithmetic.

Generated JSON porovnaj s `EVIDENCE/011__KMPC035_REFERENCE_RESULT.json` po
poliach a prahoch. Bitová zhoda nie je povinná. Ulož SHA-256 generated JSON
do odpovede; generated súbor sa nepridáva spätne do zapečateného balíka.
