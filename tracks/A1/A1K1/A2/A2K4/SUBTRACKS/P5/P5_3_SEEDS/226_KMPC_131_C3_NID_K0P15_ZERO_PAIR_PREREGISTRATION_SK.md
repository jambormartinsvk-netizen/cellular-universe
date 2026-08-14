# KMPC-131 — C3 NID/k=0.15 nulový pár

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.15`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Východiskový register:** `NID 7/9`, globálne C3 `37/45`, K4 `60/100`.

## 1. Rozsah

Táto jednotka overí posledné dva NID C3 atómy
`NID/k=0.15/gamma0` a `NID/k=0.15/af0`. Historický nominal atóm sa
neprepočítava; používa sa immutable KMPC-117 autorita. Nový runner ani nový
vedecký base nevznikne.

Frozen KMPC-131 vykoná štyri izolované shardy:

```text
gamma0 × accepted [0,5]
gamma0 × audit    [0,7]
af0    × accepted [0,5]
af0    × audit    [0,7]
```

Každý worker má vlastný limit `4.8 s`, parent wall guard `9.0 s` a
vonkajší proces `10 s`. Parent nevykonáva solver; technické shardy nie sú
nové fyzikálne atómy.

## 2. Frozen nominal a support autorita

| položka | frozen hodnota |
|---|---|
| nominal raw | `RUN_KMPC_117_P5_3G7_C2_NID_K0p15_SAME_MATRIX_REFINEMENT.json` |
| SHA-256 | `F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4` |
| run / candidate | `KMPC-117 / PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY` |
| schema | `accepted_audit` |
| aggregate autorita | KMPC-127, SHA `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F` |
| accepted / audit | `[0,5] / [0,7]` |
| M1 depth | `7` |

KMPC-127 atóm má exact file/hash/identity, všetky required gates PASS a
`technical_failure_rejected=true`. Interný audit 186 potvrdil, že KMPC-117
po troch same-matrix corrections znížil nominal audit driver z
`4.1866e-10` na `1.3514e-16`; independent holdout ostal
`1.4373e-11 < 1e-9`, common `2.1161e-10 < 1e-8` a tail maximá
`1.2342e-7/6.8291e-8 < 1e-6`.

Tieto údaje dokazujú nominal autoritu, nie výsledok nulových variantov.
CDI/.15 a BI/.15 na rovnakom support/depth pôvodne skončili fyzikálne
úplným REVIEW, preto táto predregistrácia nepredpokladá priamy PASS ani
automatický same-matrix successor.

## 3. Frozen prahy a rozhodnutia

Bez zmeny ostávajú driver `1e-10`, independent holdout `1e-9`, common
`1e-8`, cancellation-safe tail `1e-6`, absolute fallback `1e-12` a
background `1e-12`.

- `PASS candidate`: oba varianty dokončia všetky shardy a všetky core,
  common, tail, background, null-limit, bridge a logical-atom brány sú true;
- `REVIEW candidate`: receipt je technicky úplný, ale aspoň jedna frozen
  fyzikálna brána je false; ďalší krok sa odvodí iba z nej;
- `TECHNICAL FAILURE / NO VERDICT`: worker/runtime/identity/hash/schema
  zlyhanie alebo neúplný pair; failure raw sa zachová bez REVIEW či STOP.

Threshold, support ani rovnica sa po výsledku nesmú meniť. Skriptový
candidate nie je verdikt; autoritatívny stav smie prideliť iba interný audit.

## 4. Predregistrovaný postup a output

`compile frozen dependencies+runner → help → NID/.15 four-shard smoke →
NID/.15 official`.

Smoke nesmie vykonať solver ani zapísať raw a musí potvrdiť exact `4/4`.
Official smie vytvoriť iba:

`scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NID_K0p15_ZERO_VARIANT_PAIR.json`

alebo príslušný `_TECHNICAL_FAILURE.json`. Ani jeden pred predregistráciou
neexistoval. Rovnaký support/depth kontrakt technicky dokončili CDI/.15 za
`4.453 s` a BI/.15 za `4.390 s`; ide iba o runtime precedens.

Pri priamom scoped PASS sa NID uzavrie `9/9` a globálne C3 stúpne
`37/45→39/45`. Pri REVIEW ostáva `37/45` až do cause-derived nástupcu alebo
pomenovaného STOP.

## 5. Source freeze

| artefakt | SHA-256 |
|---|---|
| frozen scientific/pair base | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| frozen four-support-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| frozen runner `375/KMPC-131` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal. Predregistrácia a source
freeze sú dokončené pred prvým Python procesom tejto jednotky a odteraz sa
nemenia. Po uzavretí alebo pomenovanom STOP NID módu vznikne jeden externý
auditný balík za celý koherentný mód.
