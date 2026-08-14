# KMPC-142 — C3 NID/k=0.05 exact identity-schema adaptér

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.05`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Technický predchodca:** `KMPC-131 / PF-127 / predregistrácia 221`

## 1. Pozorovaný problém bez fyzikálneho výsledku

KMPC-131 compile a help prešli, ale NID/.05 smoke skončil `0/4` pred
fyzikou. Každý child vrátil:

`RuntimeError: nominal identity mismatch: RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json`.

Smoke mal `physics_executed=false`, nevykonal M1/F0/M3 solver a nevytvoril
success ani failure raw. NID/.05 nulové atómy preto nemajú nový verdikt.
PF-127 je zapísaný vo formálnom Python error ledgeri.

Koreňová príčina je schema equality, nie fyzika ani nesprávny historický
raw. KMPC-053 obsahuje presne správnu identitu a tri legitímne frozen
schema polia navyše:

```json
{
  "M1_depth": 7,
  "audit_support": [0, 7],
  "candidate_support": [0, 5],
  "k_Mpc_inverse": 0.05,
  "mode": "NID",
  "variant": "nominal"
}
```

Legacy loader tento celý objekt chybne porovnal s redukovanou trojpoľovou
mapou `mode/k/variant`.

## 2. Jediná povolená zmena

KMPC-142 smie pridať iba process-local, fail-closed schema adaptér pre
presnú dvojicu `NID/k=0.05` a presný šesťpoľový KMPC-053 identity objekt.
Adaptér navyše musí overiť:

- presný filename, SHA, `run_id`, candidate a schema keys `05/07`;
- frozen support `[0,5]→[0,7]` a M1 depth `7`;
- globálny KMPC-127 C2 aggregate PASS guard;
- historický immutable raw bez jeho prepisovania.

Pre inú identitu je KMPC-142 CLI fail-closed. Frozen KMPC-131 scientific
pair base, four-shard base a runner sa nemenia. Rovnice, matice, variantové
vstupy, support solve, common/tail/null/bridge agregácia, prahy, precision,
worker limit `4.8 s`, parent limit `9.0 s` a vonkajší limit `10 s` ostávajú
identické.

## 3. Frozen fyzikálny kontrakt

Ostáva presne kontrakt predregistrácie 221:

| položka | frozen hodnota |
|---|---|
| nominal | `KMPC-053`, SHA `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD` |
| accepted / audit | `[0,5] / [0,7]` |
| M1 depth | `7` |
| driver / holdout | `1e-10 / 1e-9` |
| common / tail | `1e-8 / 1e-6` |
| absolute / background | `1e-12 / 1e-12` |
| logické atómy | `NID/k=0.05/gamma0`, `NID/k=0.05/af0` |

PASS/REVIEW/TECHNICAL FAILURE vetvy z dokumentu 221 sa nemenia. Skriptový
candidate ostáva iba podkladom pre samostatný interný audit.

## 4. Predregistrovaný postup

`compile adapter+runner+frozen dependencies → help → NID/.05 exact-schema
smoke → NID/.05 official`.

Smoke nesmie spustiť solver ani zapísať raw a musí potvrdiť `4/4` identity.
Official výstup je výhradne:

`scripts/results/k_mpc_005/RUN_KMPC_142_P5_3G7_C3_NID_K0p05_ZERO_VARIANT_PAIR.json`

alebo príslušný `_TECHNICAL_FAILURE.json`. Ani jeden pred source freeze
neexistoval. Ak smoke neprejde, official sa nesmie spustiť. Ak official
zlyhá technicky, nevznikne fyzikálny verdikt a ďalší krok sa odvodí iba z
failure receiptu.

## 5. Source freeze pred prvým KMPC-142 Python behom

| artefakt | SHA-256 |
|---|---|
| frozen scientific/pair base | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| frozen KMPC-131 four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| frozen runner `375/KMPC-131` | `45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2` |
| nový exact-schema adapter base | `7151201BE9007263D8345FD63C54129BE2A1B2898C5D5CF02D0C9F4322853354` |
| nový runner `386/KMPC-142` | `DB5A711B2D7E2E5A20A4FBE873DDAECE00A2DC4C299E145FF48A5FCAD5953E4A` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal. Tieto zdroje sa odteraz
nemenia. Externý auditný balík sa vytvorí až po uzavretí alebo pomenovanom
STOP celého NID módu.
