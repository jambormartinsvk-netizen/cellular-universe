# KMPC-130 — C3 paralelný smoke/identity nástupca

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

## 1. Presný delta rozsah

KMPC-129/PF-118 zastal iba v smoke: raw stav `physics_executed=False` bol
nesprávne použitý ako bool podmienka, ktorá mala byť true. Žiadny solve ani
raw výsledok nevznikol.

KMPC-130 smie:

- premenovať check na `no_physics_executed` a vyhodnotiť ho ako true;
- obaliť frozen KMPC-129 worker payload identitou `KMPC-130`;
- pri aggregate dočasne obnoviť vnútornú KMPC-129 identitu iba pre použitie
  byteovo nezmenenej parity logiky a finálny receipt označiť `KMPC-130`;
- použiť tenký runner 374 nad nezmenenou procesnou implementáciou runnera
  373, pričom child proces musí smerovať späť na runner 374.

Nesmie meniť rovnice, support, nominal hashe, prahy, nulové kontroly,
coefficient bridge, paralelné spúšťanie ani worker deadline `4.8 s`.
Rozhodovacie vetvy a súborový rozpočet ostávajú podľa dokumentov 200–201.

## 2. Predregistrovaný postup

`compile base → compile runner → help → AD/.005 parallel smoke → AD/.005
official`. Ďalšie k body sa spustia iba po technicky úplnom prvom receipt.
Smoke nesmie zapisovať raw a musí potvrdiť presne `2/2` worker payloady,
obidva s `physics_executed=false` a celkovým `pass=true`.

## 3. Source freeze

| artefakt | SHA-256 |
|---|---|
| frozen parallel base KMPC-129 | `8D839A2F628A311DCC2C951D7A23974A2276FF11031ADD2984FF708854B0C2E5` |
| frozen parallel runner 373 | `8B04AEFF533F70A2D13B6D4772F2743BD956877B00332B37F65FA7200A241803` |
| nový identity/smoke base | `C2ECBAF99CDCCE5CCDB9B3F5EAD8C19528687E0CA19E9021B707F453B7AA59C6` |
| runner `374/KMPC-130` | `0CC2D350F2319C7061F47A068C51804613D711CD2CA8F3C903B8620F71B4612B` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal; source freeze je dokončený a
predregistrácia sa odteraz nemení.
