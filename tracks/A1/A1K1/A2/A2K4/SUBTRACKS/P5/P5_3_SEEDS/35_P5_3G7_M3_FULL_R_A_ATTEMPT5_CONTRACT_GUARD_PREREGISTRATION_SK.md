# P5.3g7-M3-FULL/R-A — technický pokus 5/10, contract-guard predregistrácia

**Dátum:** 2026-07-16  
**Stav pred behom:** `PREREGISTERED / NOT_RUN`  
**Dôvod:** PF-064 po raw PASS pokusu 4  
**Rozsah:** exact-set contract guard + regresia platnej algebry; bez solve/ODE  
**Counter pred behom:** `4/10`

## Čo opravujeme

Pokus 4 správne vyrátal algebraické identity, ale state register kontroloval
lokálnym countom. Pokus 5 oddelí autoritatívny contract od preflightu.
Budúci seedový modul aj negatívne fixtures budú volať tú istú funkciu
`validate_contract`; lokálny count nebude môcť nahradiť exact ordered tuple.

## Nové immutable artefakty

```text
scripts/baseScripts/p5_general_synchronous/full_ra_contract.py
scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight_v2.py
scripts/265_script_KMPC_026_P5_3g7_m3_full_ra_b1_contract_guard_rerun1.py
scripts/results/k_mpc_005/RUN_KMPC_026_P5_3G7_M3_FULL_RA_B1_CONTRACT_GUARD.json
```

Pokus 4 sa neprepisuje. Jeho algebraický base má hash
`62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D` a
smie sa použiť iba ako zmrazený algebraický oracle, nie contract oracle.

## PASS kritériá

1. produkčný manifest z pokusu 4 prejde samostatným exact validatorom;
2. validator porovná presné poradie a mená 13 stavov, 13 driver rows a dva
   holdouty;
3. všetky negatívne fixtures prejdú tou istou funkciou a musia byť
   odmietnuté s konkrétnou chybovou správou;
4. fixture s rovnakým countom, ale `fake_state` musí zlyhať;
5. fixture s rovnakou množinou v inom poradí musí zlyhať;
6. chýbajúci/extra/reordered RHS a holdout vložený do drivera musia zlyhať;
7. všetky platné algebraické checks pokusu 4 zostanú true a všetky jeho
   presné rezíduá zostanú reťazec `0`;
8. žiadny solve ani ODE; `score_effect=0`.

Úspešný verdikt:

```text
PASS_R_A_B1_CONTRACT_GUARD_ONLY
```

Ani tento PASS nie je seedový alebo fyzikálny PASS. Uzavrie iba B1 a povolí
predregistrovať nasledujúci úplný seedový solve ako pokus 6/10.

## Ak výsledok neprejde

- syntax/import/CLI/validator chyba: `SCRIPT_IMPLEMENTATION_FAILURE`;
- zmena algebraických núl: regresný STOP a návrat k PF-063/Bianchi auditu;
- hash mismatch: fail-closed provenance STOP;
- žiadny fyzikálny verdikt K4.

## Prevádzka

Samostatne sa spustí `py_compile` troch nových Python súborov, `--help`,
smoke s interným limitom 2 s a full preflight s limitom 5 s. Každý proces
má vonkajší timeout najviac 10 s a používa priamy
`C:\Python311\python.exe`.
