# KMPC-131 — C3 NIV/k=0.005 nulový pár

**Dátum:** 2026-07-20  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NIV/k=0.005`  
**Stav:** `EXECUTED / IMMUTABLE / CONSUMED_BY_INTERNAL_AUDIT_233`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Vstupný stav:** externý audit EA-035 prijatý; C3 `39/45 PASS`; K4
`LIVE / 60/100`; consecutive technical failures `0/10`

## 1. Presná otázka

Prejdú dva ešte neuzavreté C3 atómy `NIV/k=0.005/gamma0` a
`NIV/k=0.005/af0` všetkými frozen core, common, tail, background,
null-limit, bridge a logical-atom bránami pri C2 autorite KMPC-120,
accepted supporte `[-1,6]`, audit supporte `[-1,8]` a M1 depth `8`?

Historický nominal atóm sa neprepočítava. Rovnice, support, depth, prahy,
nominal hodnoty ani štvor-shardová procesná architektúra sa nemenia. Použije
sa byteovo nezmenený runner 375/KMPC-131.

## 2. Read-only kontrola pred predregistráciou

| položka | overený stav |
|---|---|
| nominal autorita | `RUN_KMPC_120_P5_3G7_C2_NIV_K0p005_SUPPORT_06_08_CHECKPOINT_RESUME.json` |
| nominal SHA-256 | `D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136` |
| nominal candidate | `PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY` |
| nominal identity | `mode=NIV`, `k=0.005`, `variant=nominal` |
| frozen support/depth | accepted `[-1,6]`, audit `[-1,8]`, M1 depth `8` |
| leading-power kontrola | accepted aj audit F0/M3 stavy obsahujú explicitný prvý rád `j=-1` |
| C2 aggregate autorita | `RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json` |
| aggregate SHA-256 | `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F` |
| output collision | success, failure aj `.tmp` cieľ sú neprítomné |
| do-not-run register | bez zákazu pre `KMPC-131 / NIV/.005`; selektorová výnimka sa týka iba legacy `NID/.05` |

`c3_zero_variant_pair._filter_support` a validátor používajú inkluzívny
`range(support[0], support[1] + 1)`, preto záporný vedúci rád nie je
odrezaný ani premapovaný na nulu. Worker dostáva celý frozen support tuple.

## 3. Frozen výpočet a runtime

Štyri izolované procesy sú:

```text
gamma0 × accepted [-1,6]
gamma0 × audit    [-1,8]
af0    × accepted [-1,6]
af0    × audit    [-1,8]
```

Každý worker má interný limit presne `4.8 s`. Parent nespúšťa solver,
validuje `4/4` payloady, skladá common/tail/null/bridge brány a má wall guard
`9.0 s`; vonkajší procesný limit je `10 s`. NID/.005 s rovnakým počtom
support koeficientov a vyšším M1 depth `9` skončil za `5.281 s` parent a
`2.657–3.625 s` na worker. To je iba technická realizovateľnosť, nie
predikcia NIV výsledku.

## 4. Frozen prahy a rozhodovanie

Prahy ostávajú: driver `1e-10`, independent holdout `1e-9`, common
accepted→audit `1e-8`, cancellation-safe tail `1e-6`, absolute fallback
`1e-12` a background `1e-12`.

1. Úplné `4/4` workery a všetky brány true →
   `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY`.
2. Technicky úplný payload s aspoň jednou false frozen fyzikálnou bránou →
   `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`; zastaviť na prvom REVIEW a
   odvodiť prípadného nástupcu iba z presnej false množiny.
3. Chýbajúci worker, timeout, hash/schema/parity alebo neúplný receipt →
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`; zachovať failure raw, zapísať
   Python error ledger a nemenit C3 ani K4.

Skriptový candidate nie je autoritatívny verdikt. Ten vznikne až po
samostatnom internom audite immutable rawu. Pri PASS sa NIV stav zmení z
historických `3/9` nominal atómov na `5/9` a globálne C3 z `39/45` na
`41/45`. Pri REVIEW sa započíta iba atóm, ktorého všetky vlastné brány
samostatne prešli.

## 5. Predregistrovaná exekúcia

Poradie je presne:

```text
compile frozen scientific base
compile frozen four-shard base
compile frozen runner
runner --help
NIV/.005 four-worker smoke
output/failure/temp guard
presne jeden NIV/.005 official audit
```

Smoke nesmie spustiť fyziku ani zapísať raw. Official smie vytvoriť práve
jeden z cieľov:

```text
scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p005_ZERO_VARIANT_PAIR.json
scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p005_ZERO_VARIANT_PAIR_TECHNICAL_FAILURE.json
```

Žiadny z nich ani jeho `.tmp` pred prvým Python procesom neexistuje.
Immutable výsledok sa nikdy neprepisuje ani neopakuje.

## 6. Source freeze pred prvým Python procesom

| artefakt | SHA-256 |
|---|---|
| scientific/pair base `c3_zero_variant_pair.py` | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| four-support-shard base `c3_zero_variant_parallel_v3_support_shards.py` | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| runner `375_script_KMPC_131_P5_3g7_C3_four_support_shards.py` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |

Pred vytvorením tohto dokumentu nebol pre NIV/.005 spustený nijaký Python
proces. Od tohto bodu sú tri uvedené zdroje pre túto jednotku immutable.
Externý auditný balík vznikne až po ucelenom NIV mode closure alebo po
pomenovanom STOP/REVIEW bode vyžadujúcom externé rozhodnutie.

## 7. Execution ledger

| Fáza | Výsledok |
|---|---|
| statický hash/output preflight | PASS; 5/5 hashov, 4/4 ciele neprítomné, 0 pending markerov |
| compile scientific base / shard base / runner | exit `0/0/0` |
| `--help` | exit `0`; frozen CLI potvrdené |
| four-worker smoke | exit `0`; `4/4`, `physics_executed=false`, bez rawu |
| output guard po smoke | success/failure/temp `ABSENT` |
| jediný official NIV/.005 beh | exit `0`; parent `5.234 s`; workery `2.547–3.500 s` |
| immutable raw | SHA-256 `9088E7D8470E3F4CD118025ECA266646883A76ED87BED69B3FA1DCCEBB0FD156` |
| script candidate | `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY` |
| autoritatívne spracovanie | interný audit 233: `PASS_C3_NIV_K0P005_3_OF_3` |
