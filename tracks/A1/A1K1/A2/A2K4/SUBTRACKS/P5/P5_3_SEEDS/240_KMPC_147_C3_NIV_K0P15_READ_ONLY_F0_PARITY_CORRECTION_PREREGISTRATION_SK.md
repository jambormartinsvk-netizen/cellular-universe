# KMPC-147 — C3 NIV/k=0.15 read-only F0 parity correction

**Dátum:** 2026-07-22  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NIV/k=0.15`  
**Stav:** `EXECUTED_ONCE / IMMUTABLE_PASS / CONSUMED_BY_AUDIT_241`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Technický predchodca:** `KMPC-146 / PF-129 / interný audit 239`

## 1. Presný problém

KMPC-146 úspešne vykonal štyri predregistrované rank-104/130 same-matrix
korekcie. Oba varianty a všetky fyzikálne brány prešli. Pair ostal false
iba pre presnú štvoricu `f0_exact_predecessor_parity`: živé F0 stromy mali
integer power keys, hashovo načítaný KMPC-131 predecessor JSON string keys.
V publikovanom KMPC-146 JSON sú všetky štyri F0 stromy exact zhodné s
predecessorom.

Source raw:
`RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json`,
SHA `BA595163C3A2E1D464558B035FE478A16E36678FA215C46B124E4062DC77227E`.
Predecessor raw má SHA
`88DFD9AAD5F378CBD9F7E7D1AA9738C40855CA0EC9FD191A77C682D643A0CFE6`.

## 2. Jediná povolená transformácia

KMPC-147 nesmie importovať projektový fyzikálny modul ani volať worker,
solver, matrix builder alebo fyzikálnu funkciu. Smie iba:

1. hashovo načítať oba immutable JSON rawy;
2. vyžadovať source run KMPC-146, NIV/.15 identity, false pair/refinement a
   presnú false množinu štyroch F0 parity polí;
3. vyžadovať všetky ostatné row checks, všetky štyri refinement provenance
   a všetky fyzikálne brány true;
4. porovnať štyri F0 stromy už v spoločnej JSON-semantic reprezentácii a
   zhodu potvrdiť aj kanonickým SHA-256;
5. nastaviť iba štyri F0 parity checks a odvodené row pass,
   `same_matrix_multi_rank_pass`, `pair_pass`, candidate, run/test identitu;
6. zverejniť protected-snapshot SHA pred/po a operation counts
   `workers=solvers=physics=0`.

Protected snapshot zahŕňa všetky coefficienty, stavy, matice publikované v
diagnostike, residualy, holdout, common, tail, background, null-limit,
bridge, support, M1, prahy, source hashe a úplnú refinement provenienciu.
Vylúčené sú iba presne menené parity/odvodené polia a nový read-only audit
blok.

## 3. Rozhodovacie vetvy

- všetky input, semantic parity a protected checks true, pair true a nulové
  operation counts →
  `PASS_C3_NIV_K0P15_MULTI_RANK_PARITY_CORRECTION_CANDIDATE_ONLY`;
- presná false množina, fyzikálna brána, provenance, semantic parity alebo
  protected snapshot fail → žiadny PASS; NIV ostáva `7/9`;
- hash/schema/runtime/write chyba → technical failure bez fyzikálneho
  verdiktu.

Skriptový candidate nie je verdikt. Až interný audit môže prijať NIV
`7/9→9/9`, globálne C3 `43/45→45/45` a resetovať technický counter na
`0/10`. K4 ostáva `60/100`. C3 aggregate sa pred týmto auditom a externým
auditným balíkom nesmie spustiť.

## 4. Predregistrovaná exekúcia a output

`compile → help → read-only smoke → output guard → presne jeden read-only official`.

Smoke nesmie zapisovať raw a musí mať `physics_executed=false` a
`workers=solvers=physics=0`. Official smie vytvoriť iba:

```text
scripts/results/k_mpc_005/RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_READ_ONLY_F0_PARITY_CORRECTION.json
scripts/results/k_mpc_005/RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_READ_ONLY_F0_PARITY_CORRECTION_TECHNICAL_FAILURE.json
```

Oba ciele aj ich `.tmp` varianty boli pred source freeze neprítomné.

## 5. Source freeze pred prvým KMPC-147 Python behom

| artefakt | SHA-256 |
|---|---|
| KMPC-146 source raw | `BA595163C3A2E1D464558B035FE478A16E36678FA215C46B124E4062DC77227E` |
| KMPC-131 predecessor raw | `88DFD9AAD5F378CBD9F7E7D1AA9738C40855CA0EC9FD191A77C682D643A0CFE6` |
| runner `391/KMPC-147` | `8DEFEDED804EEE350CA57CDD5CD450500757653C43379A792435488CD1EB65E6` |

Pred vytvorením dokumentu nebol pre KMPC-147 spustený nijaký Python proces.
Runner je odteraz immutable.

## 6. Exekučný ledger

Compile, help a read-only smoke prešli. Smoke potvrdil všetkých `13/13`
input checks, `physics_executed=false` a nulové operation counts. Presne
jeden read-only official beh skončil exit `0` za `0.016 s` a vytvoril:

`scripts/results/k_mpc_005/RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_READ_ONLY_F0_PARITY_CORRECTION.json`

SHA-256:
`2780A8D6527C892E1EF665B59D514DD94A95495D536C56DFE3332A113956B16E`.

Candidate je
`PASS_C3_NIV_K0P15_MULTI_RANK_PARITY_CORRECTION_CANDIDATE_ONLY`, pair aj
všetky štyri refinement rows sú true, protected snapshot pred/po má SHA
`9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A` a
operation counts sú `workers=solvers=physics=0`. Autoritatívny verdikt je v
internom audite 241.
