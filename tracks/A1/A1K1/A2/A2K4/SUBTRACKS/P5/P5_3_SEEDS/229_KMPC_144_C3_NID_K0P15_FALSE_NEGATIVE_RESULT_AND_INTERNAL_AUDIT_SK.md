# Interný audit KMPC-144 — NID/.15 refinement PASS, parity false-negative

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.15`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Výsledok:** `PHYSICS_GATES_PASS / PARENT_PARITY_FALSE_NEGATIVE / NO_NEW_VERDICT`  
**NID register:** `8/9 PASS`  
**Globálny C3 register:** `38/45 PASS`  
**K4 score effect:** `NONE`, ostáva `60/100`

## 1. Výsledok

KMPC-144 technicky dokončil všetky štyri shardy. Cielený `af0/audit`
same-matrix refinement prešiel a oba varianty majú v raw
`logical_atom_pass=true`. Parent napriek tomu nastavil pair REVIEW iba pre
dve nepravdivé provenance parity podmienky, ktoré neporovnávali správnu
semantickú projekciu.

Immutable raw:
`RUN_KMPC_144_P5_3G7_C3_NID_K0p15_AF0_AUDIT_SAME_MATRIX_REFINEMENT.json`,
SHA `7288ADE2BBC876D5F26677186ACF37BD3FE6B6DC439458C90A640B1C8FD103EB`.

## 2. Fyzikálny obsah

Af0 audit rank-104 driver sa na identickej matici a RHS zlepšil:

| metrika | baseline | po 3 korekciách | limit |
|---|---:|---:|---:|
| max relative driver | `4.1866e-10` | `1.3514e-16` | `1e-10` |
| max absolute fallback | `9.8321e-15` | `9.8608e-32` | nezhoršiť |

Selection rule, finite, same-matrix label, rank 104 a tri iterations sú
PASS. Af0 core/common/tail/background/null/bridge aj gamma0 všetky brány sú
PASS. Gamma0 audit neobsahuje refinement provenance. Runtime bol `3.968 s`;
workery `1.891–2.672 s`, všetky pod `4.8 s`.

## 3. Presná false-negative príčina

False sú iba:

1. `af0_accepted_exact_predecessor_parity` — in-memory restored state používa
   integer power keys, predecessor načítaný z JSON string keys; po
   JSON-semantickej serializácii sú celé accepted subtrees presne zhodné;
2. `gamma0_variant_exact_predecessor_parity` — fyzikálny variant sa líši iba
   očakávanou runtime diagnostikou a pridaným pravdivým checkom
   `af0_audit_refinement_contract=true`. Po odstránení týchto dvoch
   nevedeckých polí je zvyšok presne zhodný s predchodcom.

Všetkých ostatných sedem refinement/parity checks je true. Chyba nemení
žiadnu vedeckú hodnotu, ale predregistrácia 228 vyžadovala parity checks,
preto tento audit zatiaľ neprideľuje nový af0 verdikt.

## 4. Jediný nástupca

KMPC-145 smie byť iba read-only transform immutable KMPC-144 rawu. Bez
workerov a solverov musí:

- overiť source raw hash a presnú false množinu dvoch parity checks;
- overiť JSON-semantickú af0 accepted paritu;
- porovnať gamma0 po odstránení iba runtime a pridaného true contract checku;
- overiť všetky fyzikálne a refinement brány true;
- zmeniť iba dve parity hodnoty a odvodené
  `same_matrix_refinement_pass/pair_pass/candidate/run_id` polia;
- publikovať protected-snapshot hash pred/po a nulové worker/solver counts.

Ak protected snapshot nie je identický alebo vznikne ďalší false check,
NID/.15 ostáva `8/9` a KMPC-145 musí skončiť REVIEW/technical failure.
