# KMPC-141 — read-only oprava supersession-scope predikátu

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → BI/.15`  
**Stav:** `PREREGISTERED / INPUT_AND_SOURCE_HASH_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Technický predchodca:** KMPC-140 / PF-126

## 1. Pozorovaný problém

KMPC-140 úspešne zložil hashovo zmrazených šesť KMPC-139 worker payloadov.
V oboch variantoch platí:

- pôvodná false množina coefficient audit solve je presne
  `['M3_driver']`;
- `M3_independent_00_0i_holdout` už pred exact supersession prešiel;
- 80-dps exact driver prešiel;
- exact non-fit holdout prešiel a jeho riadky neboli fitované;
- jediná false exact-evidence položka je `original_false_set_exact`.

Zdedený predikát vyžaduje rovnosť pôvodnej false množiny s dvojprvkovým
zoznamom driver + holdout. To je logický false negative: zlepšenie holdoutu
pred exact krokom nesmie zneplatniť následné exact potvrdenie.

## 2. Jediná povolená oprava

KMPC-141 nesmie spustiť fyziku, worker, solver ani CPQR. Nad hlbokou kópiou
raw KMPC-140 smie nahradiť iba chybný rovnostný predikát týmito fail-closed
podmienkami:

1. pôvodná false množina je neprázdna;
2. je podmnožinou deklarovaného scope
   `{M3_driver, M3_independent_00_0i_holdout}`;
3. každý pôvodne false prvok má zodpovedajúci exact PASS;
4. prvok, ktorý už pôvodne prešiel, je v exact kroku opäť potvrdený;
5. neexistuje false položka mimo scope.

Pre tento frozen vstup musí byť skutočne supersedovaný iba `M3_driver`;
holdout sa označí ako `already_passing_exactly_confirmed`, nie ako pôvodne
false. `original_false_checks`, reziduály, riešenia, matice, thresholdy,
supporty, hashe a všetky vedecké hodnoty ostávajú nezmenené.

Po oprave sa smú prepočítať iba odvodené polia:

- exact-evidence `pass`;
- audit-solve `pass`;
- variant `core_checks.audit_solve`, `core_pass`, candidate a logical pass;
- `HP_M1_exact_resume_audit` odvodené checky a pass;
- top-level `HP_M1_exact_resume_pass`, `pair_pass` a candidate.

## 3. Frozen vstup

| artefakt | SHA-256 |
|---|---|
| KMPC-140 raw | `DF45DF6A937177A84832826400725553D5A0EADD104981E8F3992DC3FCC1638F` |
| runner 385 | `007687D1BD2D31750D1D3E189F3831955D759E65F0EE2AF8FDF1B19CC9F354C4` |

## 4. Predbežné očakávanie

Keďže všetky neodvodené brány oboch variantov sú už true, očakáva sa po
korektnej kompozícii PASS candidate pre `gamma0`, `af0` aj BI/.15 pair.
Očakávanie nie je verdikt; autoritatívne rozhodnutie patrí internému auditu.

## 5. Fail-closed a preflight

Ak frozen hash, presná stará false množina, exact dôkaz, pole mimo povoleného
scope alebo post-correction invariant nesedia, vznikne iba immutable technical
failure bez verdiktu. Pred official režimom musia oddelene prejsť compile,
`--help` a read-only smoke. Runner source hash sa doplní sem ešte pred prvým
Python procesom.

## 6. Súborový rozpočet

Bez nového base modulu: jedna predregistrácia, jeden runner a jeden raw alebo
technical receipt. Po úspechu nasleduje jeden spoločný interný audit BI módu,
jedna aktualizácia autoritatívneho plánu a jeden kompaktný externý balík.
