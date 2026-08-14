# Audit P5.3g7-M3/TCA0 RERUN1

**Rozsah:** nezávislé posúdenie výsledku KMPC-023 bez zmeny rovníc alebo
prahov.  
**Rozsudok:** `REVIEW — chýba tvrdá väzba prijatej M1 normalizácie`.

## Auditná stopa

| Artefakt | SHA-256 | Stav |
|---|---|---|
| `261_script_KMPC_023_P5_3g7_mode_resolved_full_seed_audit_rerun1.py` | `56cae70e6391a5e09dabac233615be2c7f26accd8a37b6c646d1afa8cfe55537` | `RUNNABLE_REVIEW_ONLY` |
| `baseScripts/p5_general_synchronous/mode_resolved_puiseux.py` | `5a89cf82006cb5ecc1d8b4be1fd56a463453ee3d6261968cb64de8ccf2c8b7ae` | `V1_UNANCHORED_M1 / REVIEW_ONLY` |
| `RUN_KMPC_023_P5_3G7_M3_TCA0_RERUN1.json` | `4c925d10627a69430f2d3ac59f2609423a8743165d518644ffb1ec9bba869469` | immutable REVIEW výsledok |

Embedded pole `test` v JSON zostalo pomenované `KMPC-022`, hoci autoritatívna
cesta, runner hash a názov výsledku sú KMPC-023/RERUN1. Ide o stale metadata
label, nie zámenu vykonaného zdroja. Nástupca ho musí opraviť a exportovať
vlastný zdrojový hash.

## Rovnosť auditu vzorcov, výpočtu a rozhodnutia

1. Predregistrácia 27 označila M1 za prijatý externý štandardný seed.
2. V base V1 funkcia `solve_standard_seed` zostaví driver maticu a počiatočné
   constrainty, vyrieši ich cez `lstsq` a až potom volá `_m1_expected_h`.
3. M1 hodnota preto nie je riadkom matice ani pevnou eliminovanou premennou.
4. Výstup vo všetkých prípadoch reportuje `rank=76`, `unknowns=77`.
5. Veľmi malé driver rezíduum iba potvrdzuje existenciu rodiny riešení; bez
   amplitúdovej podmienky neurčuje správneho člena rodiny.
6. Následný M1 a `00/0i` FAIL je preto konzistentný s implementáciou a nesmie
   sa prehlásiť za fyzikálnu smrť mechanizmu.

Klasifikácia je priamou aplikáciou existujúceho AR50, nie zavedením nového
duplicitného pravidla. AR50 už vyžaduje tvrdú rovnosť alebo elimináciu každej
presnej normalizačnej kotvy.

## Nezávislé platné zistenia

Presné `k`-cancel identity, background invariancia a S-C algebraická
kancelácia nie sú závislé od voľby M1 normalizácie a ostávajú platné v
rozsahu tohto runnera. Frakčná plná hodnosť a malé driver rezíduá sú len
podmienené technické zistenie; fyzikálny holdout musí byť zopakovaný po
M1 ukotvení.

## Zakázaná interpretácia

- nepripísať K4 nový PASS ani body;
- nevyhlásiť K4 za mŕtvu z frakčných holdoutov RERUN1;
- nepoužiť RERUN1 `h` amplitúdy ako seed P5.4 alebo G8;
- neopravovať problém vložením `00/0i` medzi driver rovnice;
- nerobiť tretí technický suffix po RERUN2 bez nového architektonického
  auditu.
