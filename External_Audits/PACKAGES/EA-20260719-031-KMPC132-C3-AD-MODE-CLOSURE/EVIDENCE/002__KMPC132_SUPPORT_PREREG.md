# KMPC-132 — C3 AD/.05 nulový pár, support `[0,4]→[0,6]`

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Východisko:** KMPC-131 `AD/.05/gamma0+af0` je tail-only REVIEW pri
`[0,2]→[0,4]`; K4 ostáva `60/100`.

## 1. Jediná otázka

Prejdú oba už definované nulové varianty `gamma0` a `af0` bez zmeny rovníc,
plôch alebo prahov pri najbližšom monotónnom supporte
`accepted=[0,4]`, `audit=[0,6]` a M1 depth `6`?

Tento successor nemení fyziku, nominálny C2 verdikt ani počet C3 logických
atómov. Overuje iba, či tailový REVIEW KMPC-131 spôsobila nedostatočná hĺbka
rozvoja.

## 2. Prečo treba aj hlbší nominal checkpoint

Immutable nominal AD/.05 z KMPC-028 obsahuje koeficienty iba na pôvodnom
`[0,2]→[0,4]`. `af0` bridge sa nesmie vyhlásiť z porovnania dvoch rozdielnych
supportov. KMPC-132 preto v tom istom procese vytvorí šesť read-only shardov:

```text
(nominal, gamma0, af0) × (accepted, audit).
```

Nominal `[0,4]→[0,6]` je iba support checkpoint. Nepridáva logický atóm,
nenahrádza KMPC-028/031 a nemá vlastný score efekt. Pred použitím pre `af0`
musí splniť:

1. exact hash/identity autoritu KMPC-028, KMPC-031 a KMPC-127;
2. old nominal audit `[0,4]` → new nominal accepted `[0,4]` coefficient
   bridge pre F0 aj M3;
3. old nominal accepted `[0,2]` → new nominal accepted common bridge;
4. new nominal accepted→audit common bridge, tail, core, S-C0 a background;
5. rovnaké tolerancie `relative=1e-8`, `absolute fallback=1e-12`.

Až potom sa `af0` na `[0,4]` a `[0,6]` porovná s týmto hlbším nominal
checkpointom.

## 3. Zmrazený výpočet

- mode `AD`, `k=0.05`;
- support `accepted=(0,4)`, `audit=(0,6)`, M1 depth `6`;
- varianty bez zmeny: `gamma0 = FrozenInputs(lam=0.0)`,
  `af0 = FrozenInputs(af=0.0)`;
- plochy `z=(1e-4,1e-2)` a background `a=(1e-8,3e-8)`;
- prahy: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`,
  absolute fallback `1e-12`, background relative `1e-12`;
- každý shard má vnútorný limit `4.8 s`, parent nerieši rovnice a zapisuje
  iba jeden immutable receipt;
- compile, help, smoke a official sú samostatné procesy s vonkajším limitom
  najviac `10 s`.

## 4. Nemenné vstupy

| vstup | SHA-256 |
|---|---|
| KMPC-131 AD/.05 REVIEW raw | `1D239D5C94D24C4FD52AC094043A505D41CBDADCA62E6E98A9B2F76A9BAE76E1` |
| KMPC-028 nominal coefficients | `2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83` |
| KMPC-031 nominal support authority | `C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6` |
| KMPC-127 C2 aggregate | `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F` |
| `full_ra_m3_seed.py` | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` |
| `c2_fourier_coverage.py` | `757F97E14657CC7046177C2D33115CA87639B9C92E89BDABE2BFF3B4380DF3FC` |
| `c3_zero_variant_pair.py` | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| KMPC-131 four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| nový KMPC-132 base | `3A47EF9CFAC68E100FCB7A03AD9CD478C99C5BB74DA5210F7844AE619E94F867` |
| runner 376 | `A9E8FD5E6DC0D8208DDF0C15500A8E0B81199F60E63AAF8425551F1E4847092C` |

## 5. Predregistrované hodnotenie

- všetky nominal-checkpoint, gamma0 a af0 brány true:
  `PASS_C3_AD_K0P05_ZERO_PAIR_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`;
- nominal lineage/common/tail/core zlyhá:
  `REVIEW_C3_NOMINAL_SUPPORT_CHECKPOINT_UNCLOSED`;
- nulové varianty zlyhajú iba na taili:
  `REVIEW_C3_SUPPORT_EXTENSION_REQUIRED`;
- core/common/af0-bridge/null/background sa klasifikujú presne podľa
  zmrazeného C3 kontraktu KMPC-128;
- syntax/import/hash/schema/timeout/child-process chyba je iba technická,
  bez fyzikálneho verdiktu;
- `AD/.15` ostáva NOT_RUN, kým hlavný orchestrátor nevyhodnotí KMPC-132.

Žiadny ďalší support nad `[0,6]` nie je týmto dokumentom povolený. Pri
opätovnom tail REVIEW musí najprv vzniknúť nový výsledkový ledger a nová
predregistrácia.

## 6. Súborový rozpočet R5

Plánovaných je najviac päť nových live artefaktov: táto predregistrácia,
jeden versioned base, jeden tenký runner, jeden immutable raw a jeden
výsledkový/interný audit. Centrálne registre sa pri tomto medzičlánku znovu
neaktualizujú. Externý balík vznikne až po uzavretí AD módu, alebo ak tento
krok odhalí významný nový blocker meniaci route.
