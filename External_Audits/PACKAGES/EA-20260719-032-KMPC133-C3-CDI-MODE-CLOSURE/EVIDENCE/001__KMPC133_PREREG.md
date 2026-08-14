# KMPC-133 — C3 CDI/.15 same-matrix refinement nulového páru

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Východisko:** KMPC-131 CDI/.15 je technicky úplný core-only REVIEW;
K4 ostáva `60/100`.

## 1. Presný blocker

Na supporte `[0,5]→[0,7]`, M1 depth `7`, prešli pri `gamma0` aj `af0`
accepted solve, rank, holdout, forbidden vrstvy/stress, production contract,
common bridge, tail, background, nulový limit a `af0` nominal bridge.
Zlyhal iba audit M3 driver na rank-104 matici:

| variant | max relative driver residual | limit | worst row |
|---|---:|---:|---|
| gamma0 | `8.199227816e-10` | `1e-10` | `tight_coupling[7]` |
| af0 | `3.844141885e-10` | `1e-10` | `gamma_Euler[7]` |

Immutable REVIEW raw má SHA-256
`A3D934512C5303AC22E4607CCB6D1FFF13A51972463D2D52A703953F477641B6`.

## 2. Jediná otázka

Znížia tri korekcie riešenia na presne tej istej audit M3 matici a RHS oba
driver residualy pod nezmenený limit `1e-10`, bez poškodenia holdoutu alebo
ostatných C3 brán?

Ide o rovnaký vopred použitý numerický mechanizmus ako KMPC-075 nominal
CDI/.15. Nie je to nový support, rovnica, fyzikálny variant ani fit.

## 3. Zmrazená náprava

- identita iba `CDI/k=.15/gamma0+af0`;
- support ostáva accepted `[0,5]`, audit `[0,7]`, M1 depth `7`;
- štyri izolované shardy `gamma0/af0 × accepted/audit`;
- accepted rank `78` sa nerefinuje;
- iba solve s `expected_rank=104` dostane presne `3` iteratívne korekcie;
- každá korekcia používa tú istú equilibration, matrix, constant, row labels,
  column scale a `rcond`; nepridáva riadky ani unknowns;
- refined riešenie sa prijme iba ak je konečné, relative residual sa zlepší
  a absolute-fallback residual sa nezhorší;
- všetky prahy, plochy, brány a nulové definície ostávajú z KMPC-128/131;
- každý worker `≤4.8 s`, parent solver calls `0`, jeden immutable receipt;
- compile/help/smoke/official sú oddelené procesy s limitom `≤10 s`.

## 4. Predregistrované hodnotenie

- oba refined audit drivers `<1e-10` a všetky pôvodné brány PASS:
  `PASS_C3_CDI_K0P15_ZERO_PAIR_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY`;
- refinement selection alebo driver ostane FAIL:
  `REVIEW_C3_CDI_K0P15_NUMERICAL_BOUNDARY_UNCLOSED`;
- holdout, common, tail, null, background alebo `af0` bridge fail sa
  klasifikuje svojou pôvodnou C3 bránou a nesmie sa skryť driver PASSom;
- syntax/import/hash/schema/timeout/child-process chyba je iba technická bez
  fyzikálneho verdiktu;
- ďalší CDI krok ani módový PASS sa nesmie zapísať pred interným auditom.

## 5. Source freeze pred prvým Python procesom

| artefakt | SHA-256 |
|---|---|
| KMPC-131 four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| historický KMPC-075 refinement base | `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6` |
| nový KMPC-133 overlay base | `96CD52283B9B992247FE79DD43903D15173560D73A3CF971B26F893BA743C092` |
| runner 377 | `878DC12A9065391817A0750B89AFEADC4236D488CDDFC3175FC14D54AA1E07B8` |

## 6. R5 rozpočet

Successor smie pridať iba túto predregistráciu, jeden overlay base, jeden
tenký runner a jeden raw. Spoločný CDI mode audit bude piaty artefakt tejto
nástupníckej vetvy a zároveň zhrnie tri pôvodné CDI receipts. Centrálne
registre a externý balík sa aktualizujú iba pri mode closure alebo novom
významnom blockeri.
