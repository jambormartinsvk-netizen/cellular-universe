# KMPC-131 — C3 štyri paralelné support shardy

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

## 1. Dôvod a jediná dovolená zmena

KMPC-130/PF-119 dokázal, že variantová izolácia funguje, ale nie s bezpečnou
rezervou: `gamma0` prešiel za `4.7960 s`, `af0` prekročil vlastný limit.
Failure raw SHA je
`01E9498EC21C9BA2229CE77416A0E906FF804BA7CF4D7C898CC7CC252EFFB5C6`;
finálny pair výsledok ani fyzikálny verdikt nevznikol.

KMPC-131 smie nahradiť dva variantové workery štyrmi paralelnými workermi:

```text
gamma0 × accepted
gamma0 × audit
af0    × accepted
af0    × audit
```

Každý worker má vlastný interný limit `4.8 s`, overí nominal hash a všetky
shared kontrakty, vypočíta M1 a presne jeden F0/M3 support solve. Parent
nevykoná solver. Z worker payloadov iba:

- overí exact `4/4` register, source/nominal/support/threshold a M1 paritu;
- zostaví common accepted→audit a cancellation-safe tail;
- vykoná S-C0, background a príslušný nulový limit;
- pre `af0` vykoná nominal coefficient bridge accepted aj audit;
- zapíše jeden immutable párový receipt.

Workery nevytvoria medzisúbory. Ak niektorý zlyhá, jediný failure receipt
zachová všetky úspešné worker payloady. Parent pri child procesoch zmrazí
`OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1`, aby štyri malé
lineárne solve neboli spomalené BLAS oversubscription.

## 2. Čo sa nesmie meniť

Bez zmeny ostávajú dokument 200, 45 logických atómov, všetkých 15 nominal
hashov, support/depth register, rovnice, R-A/B1/TCA0/S-C0 kontrakty, fyzické
plochy, driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`, absolute
`1e-12`, background `1e-12`, nulové podmienky a všetky
PASS/REVIEW/STOP vetvy. Štyri workery sú technické shardy jedného
`mode × k` receipt, nie štyri nové fyzikálne atómy.

Výstup je
`RUN_KMPC_131_P5_3G7_C3_{MODE}_K{token}_ZERO_VARIANT_PAIR.json`.
Worker limit je `4.8 s`, parent wall guard `9.0 s` a vonkajší process limit
`10 s`.

## 3. Predregistrovaný postup

`compile base → compile runner → help → AD/.005 four-worker smoke → AD/.005
official`. Smoke nesmie spustiť solver ani zapísať raw; musí potvrdiť `4/4`
identít. `.05` a `.15` sa spustia iba po technicky úplnom prvom receipt.
Pri akomkoľvek nonzero workeri sa zachová failure raw a ďalšie k sa
nespúšťajú.

## 4. Source freeze

| artefakt | SHA-256 |
|---|---|
| frozen KMPC-128 scientific/pair base | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| frozen KMPC-129 parallel base | `8D839A2F628A311DCC2C951D7A23974A2276FF11031ADD2984FF708854B0C2E5` |
| frozen KMPC-130 identity base | `C2ECBAF99CDCCE5CCDB9B3F5EAD8C19528687E0CA19E9021B707F453B7AA59C6` |
| nový four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| runner `375/KMPC-131` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal; source freeze je dokončený a
predregistrácia sa odteraz nemení.
