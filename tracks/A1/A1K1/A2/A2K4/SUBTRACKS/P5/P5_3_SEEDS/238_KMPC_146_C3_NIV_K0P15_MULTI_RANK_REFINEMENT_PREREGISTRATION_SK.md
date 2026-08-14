# KMPC-146 — C3 NIV/k=0.15 same-matrix multi-rank refinement

**Dátum:** 2026-07-22  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NIV/k=0.15`  
**Stav:** `EXECUTED_ONCE / IMMUTABLE_LOGIC_FALSE_NEGATIVE / AUDIT_239`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Vstupný stav:** C3 `43/45`; NIV `7/9`; K4 `LIVE / 60/100`;
consecutive technical failures `0/10`

## 1. Autorita a presná otázka

Interný audit 237 prijal pre immutable KMPC-131 raw stav
`REVIEW_C3_NIV_K0P15_MULTI_RANK_NUMERICAL_BOUNDARY`. Externý audit EA-037
na úrovni T2 nezávisle reprodukoval auditnú vrstvu bez odchýlky, overil
field parity s nulovým rozdielom a odporučil `AGREE_IN_SCOPE`. Tým uzavrel
externú procesnú pauzu, nie fyzikálny REVIEW.

KMPC-146 sa pýta iba toto: uzavrie presne tri iterácie numerickej korekcie
nad tou istou maticou a konštantným vektorom frozen driver residual pri
všetkých štyroch posledných riešeniach?

```text
gamma0 × accepted [-1,6] × rank 104
gamma0 × audit    [-1,8] × rank 130
af0    × accepted [-1,6] × rank 104
af0    × audit    [-1,8] × rank 130
```

Nepridáva sa nový fyzikálny člen ani rovnica. Nehľadá sa nový support,
depth, rcond alebo prah. Independent holdout sa nepoužíva na výber ani
fitting korekcie.

## 2. Frozen vstupy a zakázané zmeny

| položka | frozen hodnota |
|---|---|
| predecessor raw | `RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json` |
| predecessor SHA-256 | `88DFD9AAD5F378CBD9F7E7D1AA9738C40855CA0EC9FD191A77C682D643A0CFE6` |
| mode / k | `NIV / 0.15 Mpc^-1` |
| varianty | `gamma0`, `af0` |
| accepted / audit support | `[-1,6] / [-1,8]` |
| M1 depth | `8` |
| cieľové ranky | accepted `104`, audit `130` |
| korekcie | presne `3` na každý cieľový solve |
| driver / holdout | `1e-10 / 1e-9` |
| common / tail | `1e-8 / 1e-6` |
| absolute fallback / background | `1e-12 / 1e-12` |

Zakázaná je zmena matice, RHS, rovníc, vstupov, supportu, depth, ranku,
prahov, počtu iterácií a logických brán. Zakázané je dopĺňať holdout riadky
do drivera alebo podľa holdoutu vyberať výsledok. Povolená je iba už
auditovaná numerická transformácia KMPC-126: vyriešiť korekciu residualu
na presne tej istej ekvilibrovanej matici a RHS. Refined riešenie sa vyberie
iba ak je konečné, zlepší driver relative residual a nezhorší absolute
fallback residual.

## 3. Povinná proveniencia a parity

Každý zo štyroch shardov musí zapísať:

- exact cieľový rank `104` alebo `130` podľa support levelu;
- tri correction kroky;
- `matrix_identity=EXACT_SAME_MATRIX_AND_CONSTANT`;
- úspešnú selection rule a obnovenie pôvodného solver ownera;
- baseline relative aj absolute residual presne rovný zodpovedajúcemu
  KMPC-131 predecessor shardu;
- exact F0/fuel paritu s predecessorom.

Chýbajúca alebo nezhodná proveniencia je technická chyba, nie fyzikálny
FAIL alebo REVIEW.

## 4. Predregistrované rozhodovanie

1. Úplné `4/4` workery, všetky inherited frozen brány true, všetky
   refinement kontroly true a exact predecessor parity →
   `PASS_C3_NIV_K0P15_ZERO_PAIR_MULTI_RANK_REFINEMENT_CANDIDATE_ONLY`.
   Až interný audit môže prijať NIV `7/9→9/9` a C3 `43/45→45/45`.
2. Technicky úplný payload s aspoň jednou false fyzikálnou alebo selection
   bránou → `REVIEW_C3_NIV_K0P15_MULTI_RANK_NUMERICAL_BOUNDARY_UNCLOSED`.
   Zastaviť; nepripravovať ďalší výpočtový successor ani C3 aggregate.
3. Timeout, source/predecessor hash, schema, parity, owner alebo neúplný
   receipt → `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`. Zachovať immutable
   failure raw, zapísať Python error ledger a nemenit NIV, C3 ani K4.

Ani candidate PASS nemení K4 `60/100`, release, Zenodo alebo prediction
table. C3 aggregate sa nesmie spustiť pred interným auditom a externým
auditným balíkom tejto ucelenej časti.

## 5. Predregistrovaná exekúcia

```text
compile frozen four-shard base
compile frozen multi-rank refinement base
compile KMPC-146 base a runner
runner --help
NIV/.15 four-worker smoke bez fyziky
output/failure/temp guard
presne jeden NIV/.15 official audit
```

Official smie vytvoriť práve jeden z cieľov:

```text
scripts/results/k_mpc_005/RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json
scripts/results/k_mpc_005/RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT_TECHNICAL_FAILURE.json
```

Oba ciele aj ich `.tmp` varianty boli pred predregistráciou neprítomné.
Runner 390 ani selektor KMPC-146 nie sú v do-not-run registri. Official je
jednorazový; úspešný ani failure raw sa neprepisuje a výpočet sa neopakuje.

## 6. Source freeze pred prvým Python procesom

| artefakt | SHA-256 |
|---|---|
| scientific pair base `c3_zero_variant_pair.py` | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| four-shard base `c3_zero_variant_parallel_v3_support_shards.py` | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| single-rank refinement base `c2_cdi_k0p15_same_matrix_refinement.py` | `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6` |
| multi-rank refinement base `c2_same_matrix_refinement_v2_multi_rank.py` | `1E2600C366590B7FC56289D1FBC386EF24DA50DA9ED5686AE5FB5A50E0992F08` |
| KMPC-146 base `c3_zero_variant_parallel_v10_niv_k0p15_multi_rank_refinement.py` | `46365EF983E7ECAE53B804E0882730CE96475554533EB0029FAFF12FA5037D91` |
| runner `390_script_KMPC_146_P5_3g7_C3_NIV_k0p15_multi_rank_refinement.py` | `C3B7E7B41B53891F5E5C86FC1604B1430D246350E31F1334B2071C0A6294ADEB` |

Pred vytvorením tohto dokumentu nebol pre KMPC-146 spustený nijaký Python
proces. Od tohto bodu sú uvedené zdroje pre official exekúciu immutable.

## 7. Exekučný ledger

Compile `4/4`, help a four-worker smoke prešli. Smoke mal `4/4` receipts,
`physics_executed=false` a nevytvoril raw. Presne jeden official beh skončil
exit `0` a vytvoril immutable raw:

`scripts/results/k_mpc_005/RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json`

SHA-256:
`BA595163C3A2E1D464558B035FE478A16E36678FA215C46B124E4062DC77227E`.

Všetky štyri refined drivery aj inherited fyzikálne brány prešli. Parent
však vydal REVIEW pre štyri false F0 parity predikáty. Audit 239 preukázal,
že ide o PF-129: porovnanie živých integer power keys s predecessor JSON
string keys. V immutable JSON sú všetky štyri F0 projekcie exact. Výpočet
sa neopakuje; povolená je iba osobitne predregistrovaná read-only oprava
bez workerov a solverov.
