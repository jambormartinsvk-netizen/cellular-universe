# Interný audit C3 NID/k=0.05 — KMPC-143 same-matrix refinement

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.05`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita dokumentu:** interný audit hlavného orchestrátora  
**Výsledok:** `PASS_C3_NID_K0P05_3_OF_3`  
**NID register:** `7/9 PASS`  
**Globálny C3 register:** `37/45 PASS`  
**K4 score effect:** `NONE`, ostáva `60/100`

**Účtovné erratum 2026-07-19:** pôvodné mode-local označenie `5/9`
nezapočítalo dva historické nominal atómy pri `.005` a `.15`. Správne je
`NID 7/9`; globálne `37/45`, fyzikálny verdikt aj raw ostávajú nezmenené.

## 1. Autoritatívny záver

NID/k=0.05 je uzavretý `3/3 PASS`:

| logický atóm | zdroj | autoritatívny stav |
|---|---|---|
| `NID/k=0.05/nominal` | historický KMPC-053 / audit 98 | PASS |
| `NID/k=0.05/gamma0` | KMPC-143 + tento audit | PASS |
| `NID/k=0.05/af0` | KMPC-143 + tento audit | PASS |

Immutable raw:

`scripts/results/k_mpc_005/RUN_KMPC_143_P5_3G7_C3_NID_K0p05_ZERO_VARIANT_PAIR_SAME_MATRIX_REFINEMENT.json`

SHA-256:
`2F461DF24C4E7490A40411FCBDC2B98EEF4ADC19ACAFCAFDCA9007501B7D447F`.

Skriptový candidate nebol prevzatý automaticky. Audit osobitne overil
source/identity kontrakt, original REVIEW provenance, exact same-matrix
mechanizmus, selection rule, accepted parity a všetky C3 brány.

## 2. Transparentná technická línia

| krok | výsledok | autoritatívny význam |
|---|---|---|
| KMPC-131 smoke / PF-127 | whole-object schema equality odmietla správny KMPC-053 identity objekt | bez fyziky, bez rawu a bez verdiktu |
| KMPC-142 | exact šesťpoľový adapter; technicky úplný pair | oba varianty REVIEW iba na audit M3 driveri |
| KMPC-143 | presne tri same-matrix korekcie audit rank-104 | podklad pre tento scoped PASS |

KMPC-143 compile prešiel `7/7`; help bol zúžený na jedinú identitu NID/.05.
Smoke prešiel `4/4`, vrátane refinement fixture, same-matrix labelu,
residual improvement a owner restoration, pri `physics_executed=false`.

Official parent skončil za `4.453 s < 9.0 s`; worker runtimes boli
`1.953/2.750 s` pre gamma0 accepted/audit a `2.156/2.907 s` pre af0.
Všetky ostali pod `4.8 s`.

## 3. Audit jediného opravovaného blockera

Accepted rank-78 solve neobsahuje refinement provenance a jeho celý JSON
subtree je pre oba varianty presne zhodný s KMPC-142. Audit solve má v
každom variante presne tri kroky, `target_rank=104`, label
`EXACT_SAME_MATRIX_AND_CONSTANT` a pravdivú selection rule.

| variant | baseline M3 driver | refined M3 driver | limit | baseline abs. fallback | refined abs. fallback |
|---|---:|---:|---:|---:|---:|
| `af0` | `1.3994e-10` | `1.5468e-16` | `1e-10` | `3.1964e-15` | `1.1833e-30` |
| `gamma0` | `1.9348e-10` | `1.0698e-16` | `1e-10` | `4.2007e-15` | `3.1554e-30` |

Refinement teda splnil obe predregistrované podmienky: relative residual sa
zlepšil a absolute-fallback residual sa nezhoršil. Matica, RHS, support,
rows, unknowns, rcond, prahy a variantové vstupy sa nezmenili.

Dve polia `same_matrix_refinement.*.provenance.baseline.pass_driver=false`
ostávajú zámerne v raw ako immutable dôkaz pôvodného KMPC-142 blockera.
Nie sú finálnymi bránami. Všetky aktívne refinement checks vrátane
`driver_pass_after_refinement` sú pravdivé.

## 4. Nezávislé a nezasiahnuté brány

Auditný independent holdout po refinement je `2.6215e-11` v oboch
variantoch, pod `1e-9`. Holdout rows neboli pridané do driver solve.

| metrika | af0 | gamma0 | limit |
|---|---:|---:|---:|
| M3 common max rel. | `1.1068e-10` | `1.6762e-10` | `1e-8` |
| tail envelope max | `1.01361e-16` | `1.01361e-16` | `1e-6` |
| background worst rel. | `0.0` | `0.0` | `1e-12` |

F0, frozen B1/TCA0, M1, rank/shape, forbidden layer/stress, production
contract, null limits, af0 coefficient bridge, logical-atom accounting,
contract guard a sedem worker-parity checks sú PASS.

## 5. Source stopa

| artefakt | overený SHA-256 |
|---|---|
| scientific/pair base | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| KMPC-131 four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| KMPC-142 identity adapter | `7151201BE9007263D8345FD63C54129BE2A1B2898C5D5CF02D0C9F4322853354` |
| three-correction mechanism | `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6` |
| KMPC-143 refinement overlay | `3B1D88A980DBB7C499A0B63008A5097337F1F744177E63BA8630E69CBE5D62EC` |
| runner `387/KMPC-143` | `F82F30F5FF00DC2AC272C949001C4641CEEA466D38C0D914E056D841550E3443` |

Výsledok nemení C2, rovnice, prediction table, K4 skóre ani release/Zenodo
stav. Same-matrix refinement nie je nový support ani fit na holdout.

## 6. Ďalší predregistrovateľný krok

NID mód je `7/9`; zostávajú `NID/k=0.15/gamma0+af0`. Ďalší krok je
read-only kontrola KMPC-117 nominal autority, frozen support/depth,
nekolidujúceho outputu a runtime realizovateľnosti. Až potom smie vzniknúť
samostatná predregistrácia a official raw.

Externý auditný balík sa zatiaľ nevytvára. Vznikne po uzavretí alebo
pomenovanom STOP celého NID módu.
