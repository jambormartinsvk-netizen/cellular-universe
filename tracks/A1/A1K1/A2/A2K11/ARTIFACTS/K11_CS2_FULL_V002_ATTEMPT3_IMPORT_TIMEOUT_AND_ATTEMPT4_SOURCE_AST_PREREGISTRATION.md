# K11-CS2 full v002 — pokus 3 import-timeout a predregistrácia source-AST pokusu 4/10

**Dátum:** 2026-07-16  
**Architektúra:** `ARCH-A / K11-TC-A3`  
**Counter po pokuse 3:** `3/10`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`

## 1. Výsledok pokusu 3

Shard `L=4` vypočítal všetky checks PASS za interných `0.687 s` a zapísal
správny generický scope verdict. Celý proces však pre variabilný import
CAMB/SymPy skončil `exit 124` po približne `10.2 s`. Preto nejde o
autoritatívny PASS a `L=6/8` sa nespustili.

**Kategória:** `PYTHON_OR_DEPENDENCY_FAILURE / CAMB_SYMPY_IMPORT_OVERHEAD`.

Tri po sebe zachované diagnostické payloady ukazujú rovnakú algebraickú
odpoveď. Problém je procesný limit, nie rezíduál. Ďalšie opakovanie rovnakého
importu by nemalo informačnú hodnotu.

## 2. Pokus 4 — ľahký source-AST kontrakt

Pokus 4 nebude importovať CAMB ani SymPy. Štandardnou knižnicou Pythonu:

1. overí SHA-256 pripnutého `.deps/python/camb/symbolic.py`;
2. cez `ast` porovná presný strom výrazov `J_eq`, `G_eq`, `E_eq`, ich
   `ell=2` zdroje, return substitúcie a `range(2,lmax)` generátora;
3. overí ordered state register a negatívne fixtures spoločným contractom;
4. pre `L=4/6/8` overí hardcoded počty `25/33/41` a racionálne CAMB-E
   streaming/zero-tail koeficienty;
5. vyžaduje `is_exact_physics=false` a `requires_lmax_convergence=true`.

Pripnutý CAMB source hash pred behom:

```text
F380B56A15F678F6D8DBA8981BBE5A4E57377050945ADE91C6CD4B9262C7A608
```

Tento test je nezávislý od runtime symbolického importu, ale predchádzajúce
diagnostické payloady poskytujú krížovú evidenciu, že rovnaké zdrojové
vzorce dali pri vykonaní nulové symbolické rezíduá.

## 3. Očakávanie a rozhodnutie

Očakávame jeden full proces pod 1 s interne aj výrazne pod 10 s wall,
všetky AST/contract/rational checks true a exit 0.

**PASS:**

```text
PASS_ARCH_A_SOURCE_AST_EXACT_SET_AND_REGISTERED_TRUNCATION_ONLY
```

Counter sa eviduje ako použitý pokus `4/10` (tri neúspešné, štvrtý úspešný).
Bez bodov a bez fyzikálneho closure PASS.

**FAIL:** hash/source AST/contract nesúlad je fail-closed a vyžaduje nový
source audit; syntax/runtime chyba je štvrtý technický neúspech. Výstup sa
zachová.

## 4. Artefakty

```text
scripts/baseScripts/a2_k11_cs2/finite_hierarchy_source_ast_preflight_v003.py
scripts/269_script_A2_K11_CS2_full_v002_source_ast_preflight.py
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_ATTEMPT4_SOURCE_AST.json
```

