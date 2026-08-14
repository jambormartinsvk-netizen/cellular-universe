# K11-CS2 full v002 — pokus 2 metadata FAIL a predregistrácia pokusu 3/10

**Dátum:** 2026-07-16  
**Architektúra:** `ARCH-A / K11-TC-A3`  
**Counter po pokuse 2:** `2/10`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`

## 1. Prečo pokus 2 nebol dokončený

Shard `L=4` skončil `exit 0`, mal 25 stavov a presné checks PASS. JSON však
zdedil z base text

```text
PASS_ARCH_A_ATTEMPT_1_EXACT_SET_INTERIOR_AND_REGISTERED_TRUNCATION_ONLY
```

hoci patril pokusu 2. Je to formálna chyba proveniencie výsledku. Výpočty
sa neznehodnocujú, ale výsledok sa nesmie autoritatívne priradiť pokusu 2.
`L=6/8` sa preto v tomto pokuse nespustili.

**Kategória:** `SCRIPT_IMPLEMENTATION_FAILURE / STALE_ATTEMPT_IDENTIFIER`.

## 2. Oprava pokusu 3

Pokus 3 nemení base, rovnice, checks ani tolerancie. Nový runner:

1. zachová pôvodný base verdict v poli `upstream_scope_verdict`;
2. autoritatívny scope pomenuje bez čísla pokusu;
3. číslo uloží samostatne ako `technical_attempt=3`;
4. zapíše hash runnera;
5. znovu vykoná tri immutable shardy `L=4/6/8`.

Generický očakávaný scope verdict je

```text
PASS_ARCH_A_EXACT_SET_INTERIOR_AND_REGISTERED_TRUNCATION_ONLY
```

Všetky tri shardy musia mať counts `25/33/41`, všetky checks true, presné
algebraické rezíduá nula, exit 0 a wall pod 10 s. Ak ktorýkoľvek zlyhá,
pokus 3 je technický/algebraický FAIL a counter prejde na `3/10`.

PASS pokusu 3 nemení fyzikálnu hĺbku. Iba uzavrie bounded štrukturálny
preflight a dovolí predregistrovať full DAE/thermal/TCA implementáciu.

## 3. Artefakt

```text
scripts/268_script_A2_K11_CS2_full_v002_structural_truncation_shard_v2.py
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_ATTEMPT3_L4.json
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_ATTEMPT3_L6.json
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_ATTEMPT3_L8.json
```

