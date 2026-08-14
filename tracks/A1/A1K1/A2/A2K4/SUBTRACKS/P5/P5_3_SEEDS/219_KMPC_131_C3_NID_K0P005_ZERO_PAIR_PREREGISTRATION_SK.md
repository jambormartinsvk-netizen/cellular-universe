# KMPC-131 — C3 NID/k=0.005 nulový pár

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.005`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

## 1. Rozsah a účel

Táto jednotka overí dva ešte neuzavreté podmienené C3 atómy
`NID/k=0.005/gamma0` a `NID/k=0.005/af0`. Historický nominal atóm sa
neprepočítava; používa sa jeho immutable C2 autorita KMPC-115. Výpočet
nesmie meniť rovnice, support, hĺbku M1, thresholdy ani nominal hodnoty.

Nový runner ani nový vedecký base nevznikne. Použije sa frozen KMPC-131,
ktorý izoluje štyri fyzikálne solve do workerov:

```text
gamma0 × accepted [0,7]
gamma0 × audit    [0,9]
af0    × accepted [0,7]
af0    × audit    [0,9]
```

Každý worker má vlastný limit `4.8 s`; parent iba validuje `4/4` payloady,
zostaví common/tail/null/bridge brány a má wall guard `9.0 s`. Vonkajší
process limit ostáva `10 s`. Technické shardy nie sú samostatné fyzikálne
atómy.

## 2. Frozen nominal a support kontrakt

| položka | frozen hodnota |
|---|---|
| mód / k | `NID / 0.005` |
| C2 nominal autorita | `RUN_KMPC_115_P5_3G7_C2_NID_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json` |
| nominal SHA-256 | `7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851` |
| nominal candidate | `PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY` |
| accepted / audit support | `[0,7] / [0,9]` |
| M1 depth | `9` |
| C2 aggregate autorita | `RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json` |
| aggregate SHA-256 | `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F` |

KMPC-115 uzavrel všetky nominal C2 brány bez HP successor potreby. Jeho
tail maximá pri `.01` boli `F0=2.7843e-9` a `M3=8.9419e-9` voči `1e-6`;
M3 driver maximum bolo `1.6133e-11` voči `1e-10` a holdout
`4.2396e-13` voči `1e-9`. Tieto čísla sú vstupná autorita, nie predikcia
výsledku nulových variantov.

## 3. Frozen prahy a rozhodovacie vetvy

Bez zmeny ostávajú driver `1e-10`, independent holdout `1e-9`, common
accepted→audit `1e-8`, cancellation-safe tail `1e-6`, absolute fallback
`1e-12` a background `1e-12`.

- `PASS candidate`: oba varianty technicky dokončia všetky štyri shardy a
  všetky core, common, tail, background, null-limit, bridge a logical-atom
  brány sú pravdivé.
- `REVIEW candidate`: výpočet je technicky úplný, ale aspoň jedna frozen
  fyzikálna brána je nepravdivá. Nasledujúci krok sa smie odvodiť iba z
  pomenovanej zlyhanej brány; threshold ani support sa spätne neupravuje.
- `TECHNICAL FAILURE / NO VERDICT`: chýba worker, prekročí sa runtime,
  zlyhá identita/hash/schema alebo nevznikne úplný pair receipt. Failure raw
  sa zachová a nesmie sa interpretovať ako fyzikálny REVIEW alebo STOP.

Skriptový candidate nie je autoritatívny verdikt. Ten smie vzniknúť až v
samostatnom internom audite immutable rawu.

## 4. Predregistrovaný postup

`compile runner → help → NID/.005 four-worker smoke → NID/.005 official`.

Smoke nesmie spustiť solver ani zapísať raw. Official beh smie vytvoriť
práve jeden z výstupov:

`scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NID_K0p005_ZERO_VARIANT_PAIR.json`

alebo príslušný immutable technical-failure receipt. Pred predregistráciou
neexistoval ani jeden z nich, preto nehrozí prepísanie historického rawu.
Rovnaký support/depth kontrakt dokončili KMPC-131 CDI/.005 za `6.047 s` a
BI/.005 za `5.750 s`; to podporuje technickú uskutočniteľnosť pod parent
limitom, nie fyzikálny výsledok NID.

Po oficiálnom behu sa overí raw SHA-256, register workerov, runtime a každá
frozen brána. Táto jednotka nevytvorí externý auditný balík: balík sa podľa
aktívneho procesu vytvorí až po ucelenom uzavretí alebo pomenovanom STOP
celého módu NID.

## 5. Source freeze

| artefakt | SHA-256 |
|---|---|
| frozen scientific/pair base | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| frozen four-support-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| frozen runner `375/KMPC-131` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal. Predregistrácia a source
freeze sú dokončené pred compile, smoke aj official behom a odteraz sa
nemenia.
