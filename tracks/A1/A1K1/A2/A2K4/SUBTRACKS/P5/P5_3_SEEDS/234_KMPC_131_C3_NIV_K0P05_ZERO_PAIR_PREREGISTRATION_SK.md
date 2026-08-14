# KMPC-131 — C3 NIV/k=0.05 nulový pár

**Dátum:** 2026-07-20  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NIV/k=0.05`  
**Stav:** `EXECUTED / IMMUTABLE / CONSUMED_BY_INTERNAL_AUDIT_235`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Vstupný stav:** C3 `41/45 PASS`; NIV `5/9 PASS`; K4 `LIVE / 60/100`;
consecutive technical failures `0/10`

## 1. Presná otázka

Prejdú dva ešte neuzavreté C3 atómy `NIV/k=0.05/gamma0` a
`NIV/k=0.05/af0` všetkými frozen core, common, tail, background,
null-limit, bridge a logical-atom bránami pri historickej nominal autorite
KMPC-056, accepted supporte `[-1,4]`, audit supporte `[-1,6]` a M1 depth
`6`?

Nominal atóm sa neprepočítava. Rovnice, support, depth, prahy, nominal
hodnoty ani štvor-shardová architektúra sa nemenia. Použije sa byteovo
nezmenený runner 375/KMPC-131.

## 2. Read-only kontrola pred predregistráciou

| položka | overený stav |
|---|---|
| nominal autorita | `RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json` |
| nominal SHA-256 | `9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332` |
| nominal identity | `mode=NIV`, `k=0.05`, `variant=nominal` |
| nominal candidate | `PASS_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_ADEQUATE_CANDIDATE_ONLY` |
| frozen schema | `niv_depth6`; accepted key `candidate_minus1_4`, audit key `audit_minus1_6` |
| frozen support/depth | accepted `[-1,4]`, audit `[-1,6]`, M1 depth `6` |
| leading-power kontrola | accepted aj audit F0/M3 stavy obsahujú explicitný prvý rád `j=-1` |
| C2 aggregate | SHA `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F`; pri `.05` slúži ako globálny PASS prerequisite, priamou support autoritou je KMPC-056 |
| output collision | success, failure aj oba `.tmp` ciele sú neprítomné |
| do-not-run register | bez zákazu pre `KMPC-131 / NIV/.05` |

Loader má explicitnú `niv_depth6` vetvu a fail-closed overuje celý
trojpoľový identity objekt, run ID, candidate, exact support powers a
13-stavový M3 register. Inkluzívny rozsah od `support[0]` zachováva záporný
rád; nedochádza k premapovaniu `-1` na `0`.

## 3. Frozen výpočet a runtime

```text
gamma0 × accepted [-1,4]
gamma0 × audit    [-1,6]
af0    × accepted [-1,4]
af0    × audit    [-1,6]
```

Každý worker má limit presne `4.8 s`. Parent iba validuje `4/4` payloady a
skladá odvodené brány pri wall limite `9.0 s`; vonkajší limit je `10 s`.
NIV/.005 s dlhším supportom `[-1,6]→[-1,8]` skončil za `5.234 s` parent a
`2.547–3.500 s` na worker. Historický KMPC-056 nominal skončil za
`2.766 s`. Tieto časy dokazujú iba technickú realizovateľnosť.

## 4. Frozen prahy a rozhodovanie

Prahy ostávajú: driver `1e-10`, independent holdout `1e-9`, common
accepted→audit `1e-8`, cancellation-safe tail `1e-6`, absolute fallback
`1e-12` a background `1e-12`.

1. Úplné `4/4` workery a všetky brány true →
   `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY`.
2. Technicky úplný payload s aspoň jednou false frozen fyzikálnou bránou →
   `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`; zastaviť na prvom REVIEW a
   ďalší krok odvodiť iba z presnej false množiny.
3. Timeout, hash/schema/parity chyba alebo neúplný receipt →
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`; zachovať failure raw, zapísať
   Python error ledger a nemenit C3 ani K4.

Skriptový candidate nie je autoritatívny verdikt. Pri úplnom PASS sa NIV
zmení `5/9→7/9` a globálne C3 `41/45→43/45`. Pri REVIEW sa započíta iba
samostatne úplný logický atóm s pravdivými vlastnými bránami.

## 5. Predregistrovaná exekúcia

Poradie je presne:

```text
compile frozen scientific base
compile frozen four-shard base
compile frozen runner
runner --help
NIV/.05 four-worker smoke
output/failure/temp guard
presne jeden NIV/.05 official audit
```

Smoke nesmie spustiť fyziku ani zapísať raw. Official smie vytvoriť práve
jeden z cieľov:

```text
scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p05_ZERO_VARIANT_PAIR.json
scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p05_ZERO_VARIANT_PAIR_TECHNICAL_FAILURE.json
```

Žiadny z nich ani jeho `.tmp` pred prvým Python procesom neexistuje.
Immutable výsledok sa nikdy neprepisuje ani neopakuje.

## 6. Source freeze pred prvým Python procesom

| artefakt | SHA-256 |
|---|---|
| scientific/pair base `c3_zero_variant_pair.py` | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| four-support-shard base `c3_zero_variant_parallel_v3_support_shards.py` | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| runner `375_script_KMPC_131_P5_3g7_C3_four_support_shards.py` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |

Pred vytvorením dokumentu nebol pre NIV/.05 spustený nijaký Python proces.
Od tohto bodu sú tri zdroje pre túto jednotku immutable. Externý auditný
balík vznikne po NIV mode closure alebo pri pomenovanom REVIEW/STOP bode.

## 7. Execution ledger

| Fáza | Výsledok |
|---|---|
| statický hash/output preflight | PASS; 5/5 hashov, 4/4 ciele neprítomné, 0 pending markerov |
| compile scientific base / shard base / runner | exit `0/0/0` |
| `--help` | exit `0`; frozen CLI potvrdené |
| four-worker smoke | exit `0`; `4/4`, `physics_executed=false`, bez rawu |
| output guard po smoke | success/failure/temp `ABSENT` |
| jediný official NIV/.05 beh | exit `0`; parent `4.297 s`; workery `1.859–2.594 s` |
| immutable raw | SHA-256 `9E8E7D0F22D471E3C806DDBF5B2B4E587B209A537D55F1A8EFE259AC4F9DEFDD` |
| script candidate | `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY` |
| autoritatívne spracovanie | interný audit 235: `PASS_C3_NIV_K0P05_3_OF_3` |
