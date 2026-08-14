# KMPC-129 — C3 paralelný nulový-variantový technický nástupca

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Nástupca:** KMPC-128/PF-117; fyzikálny suffix a C3 kontrakt sa nemenia.

## 1. Dôvod a dovolená zmena

KMPC-128 pri prvom `AD/k=.005` official dokončil `gamma0`, ale počas `af0`
prekročil spoločný interný limit `4.8 s`. Immutable failure receipt má SHA
`E974DEE195641A68CA753074E73D416E53EFC471A09473929560950E8825E3D9` a
fyzikálny verdikt `NONE_TECHNICAL_FAILURE`.

KMPC-129 smie zmeniť iba procesnú architektúru:

1. parent spustí súčasne worker `gamma0` a worker `af0`;
2. každý worker má vlastný interný limit `4.8 s`, nanovo overí presný nominal
   hash a vypočíta vlastný M1/F0/M3 payload;
3. workery nezapisujú medzisúbor; vrátia plný JSON parentu cez zachytený
   štandardný výstup;
4. parent fail-closed overí identity, hashe, supporty, prahy a skombinuje ich
   do jediného immutable párového receipt;
5. ak jeden worker zlyhá, parent failure receipt zachová celý payload
   úspešného workeru a presnú chybu druhého.

Rovnice, varianty, nominal súbory, support register, plochy, prahy,
PASS/REVIEW/STOP mantinely a 45-logický register zostávajú presne podľa
KMPC-128/dokumentu 200. M1 sa zdieľa významom a kontraktom, nie pamäťovým
objektom; jeho opakovaný výpočet v dvoch izolovaných workeroch je povinná
procesná kontrola, nie nový fyzikálny atóm.

## 2. Limity a výstupy

- každý worker: interný deadline `4.8 s`;
- parent: iba orchestration/merge, bez solvera; celý official proces má
  vonkajší limit `10 s`;
- `compile base`, `compile runner`, `help`, `smoke` a každý official sú
  samostatné externe ohraničené procesy;
- výsledok:
  `RUN_KMPC_129_P5_3G7_C3_{MODE}_K{token}_ZERO_VARIANT_PAIR.json`;
- technické zlyhanie:
  `..._ZERO_VARIANT_PAIR_TECHNICAL_FAILURE.json`;
- success ani failure cieľ sa neprepisuje.

Prvý smoke musí bez fyziky overiť obe worker identity a presný AD nominal
schema/hash. Prvý official je znovu `AD/.005`; `.05` a `.15` sa spustia iba
po jeho technicky úplnom výstupe. Starý runner 372 je `DO_NOT_RUN`.

## 3. Rozhodovacie vetvy

Variantové a párové kandidáty sú byte-for-byte rovnaké ako v dokumente 200.
Technická chyba workeru alebo parent merge nevytvára fyzikálny výsledok.
Módový closure je naďalej iba `3/3` receipts = `9/9` logických atómov a
globálne C3 iba `15/15` receipts = `45/45` logických atómov.

## 4. Source freeze

| artefakt | SHA-256 |
|---|---|
| KMPC-128 base `c3_zero_variant_pair.py` | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| KMPC-128 runner 372 | `32A4B3D6504DCD9A0B7C40F2947721CBF3DA07733F2A1DA4A28483120A7B6C0C` |
| nový base `c3_zero_variant_parallel.py` | `8D839A2F628A311DCC2C951D7A23974A2276FF11031ADD2984FF708854B0C2E5` |
| runner `373/KMPC-129` | `8B04AEFF533F70A2D13B6D4772F2743BD956877B00332B37F65FA7200A241803` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal; source freeze je dokončený a
predregistrácia sa odteraz nemení.

## 5. Súborový rozpočet R5

PF-117 pridal iba jeden povinný failure raw a dva central-ledger zápisy.
Nástupca pridá jeden base a jeden runner; pri úspechu stále vznikne iba jeden
raw na `mode × k`, nie worker checkpointy. Prvé AD closure preto ostáva na
pláne s tromi success receipts plus zachovaným jedným historickým failure
receiptom; externý single-copy balík musí zostať pod 40 súbormi.
