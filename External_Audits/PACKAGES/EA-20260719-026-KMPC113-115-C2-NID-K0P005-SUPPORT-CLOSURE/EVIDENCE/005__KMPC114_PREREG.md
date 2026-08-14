# KMPC-114 — C2 NID/k=.005 accepted `[0,7]`: predregistrácia checkpointu

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE_CHECKPOINT / NO_PHYSICS_VERDICT`  
**Fyzikálny prerequisite:** KMPC-113 SHA
`DD5B3075AB7581C4DC590CFE668952217B58C969B07FEC1CCDE5FA02C7B3B533`

## Presná úloha

KMPC-114 je iba prvá technická fáza už predregistrovaného rozšírenia atómu
`NID/k=.005` z accepted `[0,5]`, audit `[0,7]`, M1 depth 7 na accepted
`[0,7]`, budúci audit `[0,9]`, M1 depth 9. Vypočíta a immutable uloží M1
depth 9 a accepted blok `[0,7]`. Musí skončiť stavom
`TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT`; nesmie vydať PASS,
REVIEW, skóre, release ani zmeniť C2 `6/10` alebo K4 `60/100`.

## Prečo je beh rozdelený vopred

Pri rovnakej hĺbke už historický monolitický výpočet prekročil zmrazený
limit `4.8 s`, kým hash-bound checkpoint/resume architektúra KMPC-077/078
prešla. Preto sa známe prevádzkové riziko neopakuje ako nový timeout.
Použije sa byteovo nezmenený `c2_configurable_checkpoint.py`; segmentácia
nemení rovnice, matice, prahy, `rcond`, metriky ani fyzikálny rozsah.

## Zmrazený kontrakt

- `mode=NID`, `k=0.005`, accepted `[0,7]`, audit `[0,9]`, M1 depth `9`;
- ordering/fyzikálny prerequisite je KMPC-113 s candidate
  `REVIEW_C2_NID_K0p005_SUPPORT_07_09_REQUIRED`;
- source contract má presne 19 hashovaných base modulov a prerequisite
  contract šesť immutable raw súborov;
- všetky source hashe boli pred touto predregistráciou overené a zhodujú sa
  so stabilným lineage;
- prahy ostávajú: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail
  `1e-6`, absolute fallback a background `1e-12`;
- interný deadline ostáva `4.8 s`, každý proces dostane vonkajší timeout;
- checkpoint sa smie použiť iba po overení identity atómu, supportu, hĺbky,
  source lineage, kandidáta prerequisite a SHA-256.

## Povinné kontroly a výstup

Pred official behom: `py_compile`, `--help`, behaviorálny smoke, odmietnutie
cudzieho atómu/checkpointu a kontrola, že checkpointová fáza nevydáva
fyzikálny verdict. Úspešný raw:
`scripts/results/k_mpc_005/RUN_KMPC_114_P5_3G7_C2_NID_K0p005_SUPPORT_07_ACCEPTED_CHECKPOINT.json`.

Po immutable SHA checkpointu sa vytvorí samostatná predregistrácia KMPC-115
pre resume a až tá smie vyhodnotiť tail `[8,9]`. Ak checkpoint technicky
zlyhá, nevzniká fyzikálny výsledok ani spotrebovaný fyzikálny pokus; chyba
sa zapíše do Python error ledgeru pred nástupcom.

## Zmrazená implementácia pred prvým Python behom

- runner 358:
  `scripts/358_script_KMPC_114_P5_3g7_C2_NID_k0p005_support_07_checkpoint.py`;
- runner SHA-256:
  `E6C853540B494B2FB654679E13692DC89FBF4D9E85E859334439609BF9AF3325`;
- configurable checkpoint SHA-256:
  `DEB7776EFE28D60978FA49ABB914B3718C7F31F111DDC4B4037DA73961798B9F`;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- canonical output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 358 spustený cez Python.
Od tohto bodu je runner 358 immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | identita, segmentácia, non-verdict rola, hashe a hranice zmeny zmrazené | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | compile/help PASS; prvé chybné smoke CLI volanie zaznamenané ako PF-113 bez fyziky | `TECHNICAL_CLI_INCIDENT / CORRECTABLE` |
| 2026-07-19 | opravený smoke PASS; official checkpoint complete za `2.625 s`, 9/9 preconditions PASS | `IMMUTABLE_CHECKPOINT / NO_PHYSICS_VERDICT` |
| 2026-07-19 | raw SHA `339FD13BE750060793FCE04698BA5726AFD58DCB08BBDD3DB7B1FDFE76B35195` | `FROZEN_FOR_KMPC_115` |
