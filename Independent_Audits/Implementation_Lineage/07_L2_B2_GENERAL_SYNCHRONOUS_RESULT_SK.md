# L2-B2 — výsledok mapy general-synchronous/BR/P5 línie

**Dátum:** 2026-07-15  
**Autoritatívny výstup:** `scripts/results/k_mpc_005/RUN_LINEAGE_L2_B2_GENERAL_SYNCHRONOUS_AUDIT_RERUN2.json`  
**Predchádzajúce immutable pokusy:** prvý STOP (PF-039), `RERUN1` s neúplným kritériom (PF-040)  
**Metóda:** statický AST/source audit, 0 ODE, 0 importov modelu, 0 zmeny skóre  
**Verdikt:** `PASS_L2_B2_LINEAGE_MAP / PHYSICS_NOT_YET_PASSED`

## Mapa, ktorú výsledok potvrdil

| Trieda | Súbory | Stav po L2-B2 | Čo to znamená |
|---|---|---|---|
| Standard/null baseline | 66 | zachovaný baseline | má `U_c` a constrainty, ale nie `U_d`; nesmie sa vyhlásiť za plný energy-frame K4 |
| Plný skorý kandidát | 89, 90 | živý kandidát na L2-B2.1 | majú dynamickú RHS, `U_c`, `U_d` a explicitné constrainty |
| Testové pole | 85, 86, 95 | obmedzená, užitočná evidencia | obsahujú `U_c`/`U_d`, ale ich vlastný scope vylučuje plnú metric backreaction alebo induced metric |
| Wrapper | 92, 94 | technický alias | sám neurčuje fyzikálnu RHS |
| Seed/redukovaný potomok | 130, 136, 155 | fyzikálne obmedzený | 130 je iba seed scope; 136/155 nesú starý pevný `K_MPC` a nemajú plný `U_c`,`U_d` stav |
| Checker redukovaného stavu | 140, 143, 148 | `RUNNABLE_REVIEW_ONLY` | nekonštruujú vlastnú RHS, preto nemôžu opraviť jej chýbajúce stupne voľnosti |
| P5.1 | 236 | správny statický kontrakt | explicitne hlási `U_c`, `U_b`, `M_full`; ešte nemá ODE ani constraint evolúciu |

## Čo je podstatné

Obava používateľa sa **potvrdila iba čiastočne**: k strateniu formulácie
naozaj došlo v K7 a neskorších redukovaných potomkoch, no staršia BR2 línia
89/90 stále obsahuje presne tie dynamické objekty (`U_c`, `U_d`, constrainty),
ktoré K7 stratila. A2-K4 preto nie je slepá vetva. Nesmie sa však tvrdiť,
že 89/90 už prešli: L2-B2 zatiaľ overila iba prítomnosť a scope, nie znamienka,
koeficienty, gauge transformáciu ani úplné nulové limity.

## Dôsledok pre ďalšiu prácu

Najlepšia ďalšia koľaj nie je ďalšie numerické hľadanie. Je to `L2-B2.1`:
presný equation audit rovníc 89/90 proti covariantnému K4 kontraktu C1–C6.
Prejde iba vtedy, ak sedí energy-frame `U_d`, CDM Euler, palivový Euler,
momentum v `0i` constrain­te, `Gamma/H=lambda/E` a limit `lambda→0`.

Až po tom môže P5.2 prevziať rovnice do nového plného ledgeru. G8 zostáva
zakázané na redukovanej K7 báze.
