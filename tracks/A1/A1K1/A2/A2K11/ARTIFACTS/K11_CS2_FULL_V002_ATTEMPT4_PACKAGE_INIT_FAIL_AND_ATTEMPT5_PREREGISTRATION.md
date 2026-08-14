# K11-CS2 full v002 — pokus 4 package-init FAIL a predregistrácia pokusu 5/10

**Dátum:** 2026-07-16  
**Architektúra:** `ARCH-A / K11-TC-A3`  
**Counter po pokuse 4:** `4/10`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`

## 1. Výsledok a koreň chyby pokusu 4

Source-AST payload mal `55/55` checks PASS a interný čas `0.047 s`, ale
proces skončil `exit 124` po približne `10.6 s`. Audit ukázal, že

```text
scripts/baseScripts/a2_k11_cs2/__init__.py
```

pri každom importe eager načítal `full_multispecies_constrained_dae`, a tým
aj CAMB/SymPy. Starý hash inicializátora bol

```text
8FB3EB481E1061C5F238AA0612A936B6BF0D46393A65D82494263BD5DD2F61E1
```

**Kategória:** `SCRIPT_IMPLEMENTATION_FAILURE / EAGER_PACKAGE_IMPORT`.
Všetkých 55 kontrol ostáva diagnostickou evidenciou, nie autoritatívnym
PASS, pretože vonkajší limit neprešiel.

## 2. Oprava pokusu 5

Package initializer sa zmení na lazy export. Staré verejné mená
`BaseStatus`, `ModelParameters`, `exact_structural_audit`, `state_names`
zostanú dostupné, ale ťažký legacy modul sa načíta iba vtedy, keď si ich
volajúci skutočne vyžiada. Import ľahkého source-AST submodulu tak nesmie
načítať CAMB/SymPy.

Nový runner 270 použije rovnaký auditný base, ale autoritatívne zapíše
`technical_attempt=5`, hash runnera a nový hash lazy inicializátora.

## 3. Očakávanie

- compile a `--help`: exit 0 pod 1 s;
- full audit: `55/55`, `failed=0`, exit 0;
- internal aj wall výrazne pod 10 s;
- verdict:

```text
PASS_ARCH_A_SOURCE_AST_EXACT_SET_AND_REGISTERED_TRUNCATION_ONLY
```

Ak full proces stále prekročí limit, pokus 5 je technický FAIL a counter
prejde na `5/10`. Ak prejde, je to úspešný technický balík číslo 5; tri
timeout payloady a stale-ID výsledok zostávajú v histórii. Fyzikálna hĺbka
sa nemení.

## 4. Artefakty

```text
scripts/baseScripts/a2_k11_cs2/__init__.py
scripts/270_script_A2_K11_CS2_full_v002_source_ast_preflight_lazy.py
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_ATTEMPT5_SOURCE_AST.json
```

