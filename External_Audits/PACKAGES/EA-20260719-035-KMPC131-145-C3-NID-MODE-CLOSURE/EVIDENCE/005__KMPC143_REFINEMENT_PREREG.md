# KMPC-143 — C3 NID/k=0.05 same-matrix refinement

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.05`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Východisko:** `KMPC-142 / interný audit 223`; K4 ostáva `60/100`.

## 1. Presný blocker

KMPC-142 je technicky úplný nulový pair. Pri oboch variantoch prešli
accepted solve, plný rank, F0, independent holdout, forbidden vrstvy/stress,
production contract, common, tail, background, nulový limit a af0 nominal
bridge. Zlyhal iba audit `[0,7]` rank-104 M3 driver:

| variant | audit M3 driver max rel. | limit | worst row |
|---|---:|---:|---|
| `af0` | `1.399416137e-10` | `1e-10` | `fuel_Euler[7]` |
| `gamma0` | `1.934843229e-10` | `1e-10` | `fuel_continuity[7]` |

Immutable REVIEW raw SHA-256 je
`95CC95E96E04E32A3EB98FEA3A7EBD5E6D64A36A43A34B1143C778DE662A76D2`.

## 2. Jediná otázka a jediná povolená zmena

Znížia presne tri korekcie riešenia na tej istej audit M3 matici a RHS oba
driver residualy pod nezmenený limit `1e-10`, bez poškodenia holdoutu alebo
ostatných C3 brán?

Ide o mechanizmus už úspešne použitý v KMPC-133. Historický modul má v názve
CDI/.15, ale jeho zmrazená numerická funkcia je mode-agnostická: zasahuje
iba solve s `expected_rank=104` a používa odovzdanú maticu, RHS, riešenie,
row labels a deadline. KMPC-143 ho smie použiť iba pod novým exact target
guardom `NID/k=0.05`.

## 3. Zmrazená náprava

- identita iba `NID/k=.05/gamma0+af0`;
- support ostáva accepted `[0,5]`, audit `[0,7]`, M1 depth `7`;
- accepted rank `78` sa nerefinuje;
- iba audit solve s `expected_rank=104` dostane presne `3` korekcie;
- každá korekcia používa tú istú equilibration, matrix, constant, row labels,
  column scale a `rcond`; nepridáva riadky ani unknowns;
- refined riešenie sa vyberie iba ak je finite, relative residual sa zlepší
  a absolute-fallback residual sa nezhorší;
- exact KMPC-142 šesťpoľový nominal schema adaptér ostáva povinný;
- všetky rovnice, vstupy, prahy, plochy, nulové definície a aggregate brány
  ostávajú nezmenené;
- každý worker `≤4.8 s`, parent wall `≤9 s`, vonkajší proces `≤10 s`;
- parent vykoná `0` solverov a vznikne jeden immutable pair receipt.

## 4. Predregistrované hodnotenie

- oba refined audit M3 drivers `<1e-10` a všetky pôvodné brány PASS:
  `PASS_C3_NID_K0P05_ZERO_PAIR_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY`;
- refinement selection alebo driver ostane FAIL:
  `REVIEW_C3_NID_K0P05_NUMERICAL_BOUNDARY_UNCLOSED`;
- holdout/common/tail/null/background/bridge fail sa klasifikuje svojou
  pôvodnou bránou a nesmie sa skryť driver PASSom;
- syntax/import/hash/schema/timeout/child chyba je technical failure bez
  fyzikálneho verdiktu.

Skriptový candidate nie je autoritatívny verdikt. NID/.05 ani globálny C3
register sa nesmú zmeniť pred samostatným interným auditom rawu.

## 5. Predregistrovaný postup a output

`compile frozen+overlay+runner → help → NID/.05 refinement smoke →
NID/.05 official`.

Smoke musí overiť exact four-shard register, schema adapter, tri korekcie na
fixture, same-matrix label, zlepšenie residualu, obnovenie solver ownera a
`physics_executed=false`. Official smie vytvoriť iba:

`scripts/results/k_mpc_005/RUN_KMPC_143_P5_3G7_C3_NID_K0p05_ZERO_VARIANT_PAIR_SAME_MATRIX_REFINEMENT.json`

alebo príslušný `_TECHNICAL_FAILURE.json`. Ani jeden pred source freeze
neexistoval.

## 6. Source freeze pred prvým KMPC-143 Python behom

| artefakt | SHA-256 |
|---|---|
| frozen KMPC-131 four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| frozen KMPC-142 identity adapter | `7151201BE9007263D8345FD63C54129BE2A1B2898C5D5CF02D0C9F4322853354` |
| frozen three-correction mechanism | `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6` |
| nový NID/.05 refinement overlay | `3B1D88A980DBB7C499A0B63008A5097337F1F744177E63BA8630E69CBE5D62EC` |
| nový runner `387/KMPC-143` | `F82F30F5FF00DC2AC272C949001C4641CEEA466D38C0D914E056D841550E3443` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal. Zdroje sa odteraz nemenia.
Externý auditný balík vznikne až po uzavretí alebo pomenovanom STOP celého
NID módu.
