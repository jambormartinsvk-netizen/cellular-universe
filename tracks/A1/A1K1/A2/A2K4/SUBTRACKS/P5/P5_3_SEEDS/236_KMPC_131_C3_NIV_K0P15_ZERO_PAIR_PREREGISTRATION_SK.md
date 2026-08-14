# KMPC-131 — C3 NIV/k=0.15 nulový pár

**Dátum:** 2026-07-20  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NIV/k=0.15`  
**Stav:** `EXECUTED_ONCE / IMMUTABLE_REVIEW / CONSUMED_BY_INTERNAL_AUDIT_237`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Vstupný stav:** C3 `43/45 PASS`; NIV `7/9 PASS`; K4 `LIVE / 60/100`;
consecutive technical failures `0/10`

## 1. Presná otázka

Prejdú posledné dva C3 atómy `NIV/k=0.15/gamma0` a
`NIV/k=0.15/af0` všetkými frozen core, common, tail, background,
null-limit, bridge a logical-atom bránami pri nominal autorite KMPC-126,
accepted supporte `[-1,6]`, audit supporte `[-1,8]` a M1 depth `8`?

Nominal atóm sa neprepočítava. Rovnice, support, depth, prahy, nominal
hodnoty ani štvor-shardová architektúra sa nemenia. Použije sa byteovo
nezmenený runner 375/KMPC-131. Historický nominal potreboval same-matrix
multi-rank refinement; tento fakt je rizikový kontext, nie povolenie
automaticky refinovať nový nulový variant.

## 2. Read-only kontrola pred predregistráciou

| položka | overený stav |
|---|---|
| nominal autorita | `RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json` |
| nominal SHA-256 | `1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0` |
| nominal identity | `mode=NIV`, `k=0.15`, `variant=nominal` |
| nominal candidate | `PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY` |
| frozen support/depth | accepted `[-1,6]`, audit `[-1,8]`, M1 depth `8` |
| leading-power kontrola | accepted aj audit F0/M3 stavy obsahujú explicitný prvý rád `j=-1` |
| C2 aggregate autorita | SHA `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F`; atóm NIV/.15 je exact registrovaný |
| output collision | success, failure aj oba `.tmp` ciele sú neprítomné |
| do-not-run register | bez zákazu pre `KMPC-131 / NIV/.15` |

Loader používa frozen `accepted_audit` schému, overuje exact SHA, identity,
run ID, candidate aj KMPC-127 atom authority. Inkluzívny support validátor
zachováva `j=-1` v každom z 13 M3 stavov.

## 3. Frozen výpočet a runtime

```text
gamma0 × accepted [-1,6]
gamma0 × audit    [-1,8]
af0    × accepted [-1,6]
af0    × audit    [-1,8]
```

Každý worker má presný limit `4.8 s`, parent wall guard `9.0 s` a vonkajší
limit `10 s`. NIV/.005 s rovnakým support countom a depth skončil za
`5.234 s` parent a `2.547–3.500 s` na worker, čo podporuje iba technickú
realizovateľnosť.

## 4. Frozen prahy a rozhodovanie

Prahy ostávajú: driver `1e-10`, independent holdout `1e-9`, common
accepted→audit `1e-8`, cancellation-safe tail `1e-6`, absolute fallback
`1e-12` a background `1e-12`.

1. Úplné `4/4` workery a všetky brány true →
   `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY`.
2. Technicky úplný payload s aspoň jednou false frozen fyzikálnou bránou →
   `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`. Toto je používateľom určený prvý
   REVIEW stop: nespúšťať refinement ani iného nástupcu, presne pomenovať
   false množinu a pripraviť auditovateľný stop.
3. Timeout, hash/schema/parity chyba alebo neúplný receipt →
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`; zachovať failure raw, zapísať
   Python error ledger a nemenit C3 ani K4.

Pri úplnom PASS sa NIV zmení `7/9→9/9` a globálne C3 `43/45→45/45`; ani
vtedy sa aggregate nespustí pred interným mode-closure auditom a externým
auditným balíkom. Pri REVIEW sa započíta iba samostatne úplný logický atóm.

## 5. Predregistrovaná exekúcia

```text
compile frozen scientific base
compile frozen four-shard base
compile frozen runner
runner --help
NIV/.15 four-worker smoke
output/failure/temp guard
presne jeden NIV/.15 official audit
```

Official smie vytvoriť práve jeden z cieľov:

```text
scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json
scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_TECHNICAL_FAILURE.json
```

Žiadny cieľ ani `.tmp` pred prvým Python procesom neexistuje. Výsledok je
immutable a nesmie sa prepisovať ani opakovať.

## 6. Source freeze pred prvým Python procesom

| artefakt | SHA-256 |
|---|---|
| scientific/pair base `c3_zero_variant_pair.py` | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| four-support-shard base `c3_zero_variant_parallel_v3_support_shards.py` | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| runner `375_script_KMPC_131_P5_3g7_C3_four_support_shards.py` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |

Pred vytvorením dokumentu nebol pre NIV/.15 spustený nijaký Python proces.
Od tohto bodu sú zdroje immutable.

## 7. Exekučný ledger

Predregistrované compile `3/3`, help a four-worker smoke prešli. Smoke
potvrdil `4/4` receipts s `physics_executed=false` a nevytvoril výsledkový
raw. Presne jeden official audit bol vykonaný 2026-07-20; vytvoril immutable
raw:

`scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json`

SHA-256:
`88DFD9AAD5F378CBD9F7E7D1AA9738C40855CA0EC9FD191A77C682D643A0CFE6`.

Candidate je `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`. Podľa bodu 4 sa
exekúcia zastavila pri prvom REVIEW; refinement, successor ani aggregate
neboli spustené. Autoritatívnu interpretáciu a nezmenené účtovanie zapisuje
interný audit 237.
