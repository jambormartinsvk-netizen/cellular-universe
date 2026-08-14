# KMPC-113–115 — C2 NID/k=.005 support closure: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Interný auditor a autoritatívny zápis:** Codex (OpenAI)  
**Stav:** `INTERNAL_AUDIT_PASS / SCOPED_C2_ATOM_PASS`  
**Autoritatívny verdict:**
`PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_HP_NOT_REQUIRED`  
**Dopad:** C2 `6/10 → 7/10 PASS`; P5.3 zostáva čiastočný PASS; K4 zostáva
`LIVE / 60/100`; aktívny technický counter `0/10`

## Auditovaný reťazec

| Beh | Rola | Immutable raw SHA-256 | Výsledok |
|---|---|---|---|
| KMPC-113 | nominal `[0,5]→[0,7]`, M1 depth 7 | `DD5B3075AB7581C4DC590CFE668952217B58C969B07FEC1CCDE5FA02C7B3B533` | netail brány PASS; tail na `.01` REVIEW |
| KMPC-114 | verdict-free checkpoint accepted `[0,7]`, M1 depth 9 | `339FD13BE750060793FCE04698BA5726AFD58DCB08BBDD3DB7B1FDFE76B35195` | `TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT` |
| KMPC-115 | resume audit `[0,9]`, M1 depth 9 | `7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851` | všetky frozen brány PASS |

Všetky tri SHA boli prepočítané z live artefaktov. KMPC-114 overil všetkých
deväť checkpoint preconditions; KMPC-115 overil jeho file SHA, identitu
NID/k, support, depth, candidate rolu, completion status a source lineage.
Pozorované 13-stavové poradie sa presne rovná autoritatívnemu poradiu
`h, eta, delta_gamma, delta_fs, delta_b, delta_c, U_gamma, U_fs,
sigma_fs, U_b, U_c, delta_f, U_f`.

## Čo ukázal nominal a prečo sa support rozšíril

KMPC-113 neodhalil core, M1, common ani background problém. Pri accepted
`[0,5]` však added powers `6,7` na `z=.01` dali tail:

| Blok | Najhorší stav | Metrika | Limit | Stav |
|---|---|---:|---:|---|
| F0 | `delta_f` | `1.1184032923e-5` | `1e-6` | FAIL |
| M3 | `delta_f` | `2.4036752636e-5` | `1e-6` | FAIL |

Na `z=1e-4` bol F0 absolute tail iba `5.1348e-28` a M3 relative tail
`1.7870e-15`. To zodpovedá predregistrovanému tail-only rozhodnutiu:
rozšíriť accepted support, nie meniť rovnice alebo toleranciu.

## KMPC-115 numerické brány

| Brána | Najhoršia auditovaná hodnota | Zmrazený prah | Audit |
|---|---:|---:|---|
| M1 driver | `4.2632564146e-14` | `1e-10` | PASS |
| M1 independent holdout | `2.9976021665e-14` | `1e-9` | PASS |
| F0 `[0,9]` driver relative | `1.7749440873e-14` | `1e-10` | PASS |
| M3 `[0,9]` driver relative | `1.6132606588e-11` | `1e-10` | PASS |
| M3 independent `00/0i` holdout relative | `4.2396377958e-13` | `1e-9` | PASS |
| F0 common `[0,7]` relative | `7.3378958440e-14` | `1e-8` | PASS |
| M3 common `[0,7]` relative | `8.5369765105e-11` | `1e-8` | PASS |
| F0 tail `[8,9]`, `z=.01` | `2.7843150709e-9` (`delta_f`) | `1e-6` | PASS |
| M3 tail `[8,9]`, `z=.01` | `8.9418819803e-9` (`delta_f`) | `1e-6` | PASS |
| background k-independence | `1.1519529664e-16` | `1e-12` | PASS |

M1 má rank `120/120`, condition `7380.90` a exact hard-anchor difference
`0`. F0 má audit rank `20/20`; M3 `130/130`. Všetkých 15 audit-solve checks
je true, vrátane forbidden-layer/stress guardov, production contractu,
shape restoration a independent `00/0i` holdoutov. Combined-`R_fs`, frozen
B1 left-null/Bianchi, independent contract, S-C0 všetkých rádov `0…9`,
core a background sú PASS. Žiadny prah sa nezmenil a žiadny holdout riadok
nebol pridaný do driver solve.

Na rozhodujúcom povrchu `.01` je najhorší tail `8.94e-9`, približne
`111.8×` pod limitom `1e-6`. Rozšírenie `[0,5]→[0,7]` teda stabilizovalo
NID atóm bez potreby `[0,9]→[0,11]` alebo high-precision následníka.

## Technický incident a procesný audit

Prvé operátorské smoke volanie KMPC-114 použilo starý prepínač
`--smoke-test` a chýbal mu povinný runtime argument. Argparse skončil exit
`2` pred importom fyziky; incident je PF-113. Runner sa nemenil, správne
volanie `--smoke --max-runtime-seconds 4.8` prešlo a official checkpoint aj
resume boli vecne úspešné. Preto sa active consecutive counter po KMPC-115
resetuje na `0/10`; historický incident ostáva zachovaný.

Preventívne pravidlo pre ďalší atóm: príkazy sa po `--help` zostavia iba z
aktuálne zobrazeného CLI. Zároveň sa pri vopred známom monolitickom runtime
riziku použije už auditovaný checkpoint/resume bez vytvárania nového base
modulu. Táto časť potrebovala iba dva malé runnery a dve predregistrácie;
vedecké base súbory ostali byteovo nezmenené.

## Autoritatívny rozsudok a nonclaims

Interný audit prijíma scoped verdict
`PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_HP_NOT_REQUIRED`. Tým je atóm
`NID/k=.005` siedmym z desiatich C2 bodov.

Tento PASS nepotvrdzuje NID/k=.15, NIV body, S-M mikrofyzikálnu vetvu,
časovú evolúciu P5.4, plnú Boltzmannovu hierarchiu G8, likelihood G9,
pozorovaciu životaschopnosť ani prechod A2→A3. Nezvyšuje K4 nad `60/100` a
nie je release, prediction-table ani Zenodo trigger.

## Ďalší zmrazený krok

Ďalší C2 atóm je `NID/k=.15/nominal` s accepted `[0,5]`, audit `[0,7]`,
M1 depth 7 a presne rovnakými prahmi. Má znovu použiť stabilný
`c2_single_atom_adapter.py`; nový base modul nevznikne. Až jeho nominal raw
smie rozhodnúť, či stačí `[0,5]`, treba support successor, vznikla
numerická boundary vetva alebo core/background blocker. Po uzavretí tejto
ucelenej NID/k=.005 časti sa najprv vytvorí externý auditný balík EA-026.
