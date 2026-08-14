# baseScripts — register verzií

**Aktualizované:** 2026-07-31

| Verzia/rodina | Stav | Autoritatívny rozsah | Pravidlo zmeny |
|---|---|---|---|
| `LEGACY-UTIL-PDF` | frozen by hash | `000–002`; iba PDF utility | nový súbor/verzia |
| `LEGACY-A2K4-G8` | frozen by hash, historical scope | `a2_k4_g8/*`; stará K7/G8 implementačná línia | nesmie obnoviť K7 fyzický PASS |
| `LEGACY-KMPC-P4` | frozen by hash, review | `k_mpc_005/af_from_a1_background.py` | nová verzia + rozdielový audit |
| `LEGACY-A2K4-P5-STABLE` | frozen by hash, active formula scope | koeficientové/constraint/leading/TCA/opacity moduly v `p5_general_synchronous/` | nový modul/verzia + rerun dotknutých brán |
| `LEGACY-A2K4-P5-M3-V1` | frozen by hash, `DO_NOT_USE_PHYSICS` | `mode_resolved_puiseux.py`; neúplný palivový contract | nahradiť až po coefficient/Bianchi audite |
| `LEGACY-A2K4-P5-M3-V2` | frozen by hash, `M1_ANCHOR_ONLY` | `mode_resolved_puiseux_v2_m1_anchored.py` | hard-anchor helper možno preniesť; plný M3 nie |
| `A2K4-P5-M3-FULL-R-A` | `ATTEMPT_6_FROZEN_READY / NOT_RUN` | exact `Phi^0/Phi^1` formula/state/Bianchi contract a conditional M3-TCA0 seed kód; bez výsledku | spoločný counter `5/10`; source hash `070F...1BF2`, runner `E72D...554A`; prvý Python proces otvorí pokus 6 |
| `A2K4-P5-CDI-C1` | `EXECUTED / CORE+COMMON PASS / PRIMARY [0,1] INSUFFICIENT / HISTORICAL [0,3] OPEN` | fixed CDI/k=.05/nominal; žiadne nové rovnice | result SHA `37FB44...DCE20`; KMPC-035 neskôr obmedzil `[0,3]` na insufficient/REVIEW |
| `A2K4-P5-CDI-SUPPORT-STEP-2` | `EXECUTED / CORE+COMMON PASS / SUPPORT [0,3] REMAINDER REVIEW` | fixed CDI/k=.05/nominal; candidate 03, audit 05; žiadne nové rovnice | result SHA `A9BD51...E42A01`; M1 order-7 provenance gate povinná pred support step 3; score/release NONE |
| `A2K4-P5-M1-ORDER7-PROVENANCE` | `EXECUTED / SCOPED PASS / POWER7 DRIVER PRECISION REVIEW` | `GLOBAL_C1` M1 order-7 provenance/holdout iba; bez support step 3 a bez nových rovníc | result SHA `39BB3886...B7B497`; docs63–65; precision/boundary audit next; score/release/Zenodo NONE |
| `K11-CS2-S0-v001` | frozen by hash, `PASS_FORMULA / STOP_STATE_REGISTER` | `a2_k11_cs2/full_multispecies_constrained_dae.py`; K11/A1/CAMB formula identity scope; PF-062 extra `E_0,E_1` | full v002 opraví state set na `4l+9`; S0 súbor neprepisovať |
| `K11-CS2-FULL-v002` | `SOURCE_AST_CONTRACT_PASS / FULL_DAE_NOT_CREATED` | `finite_hierarchy_contract_v002.py`, source-AST v003, lazy package init; exact register 25/33/41 a deklarovaný numerický top; bez ODE | ARCH-A má `5/10`; ďalší full thermal/TCA/DAE balík 6/10; v003 iba pri zmene fyziky |
| `V318-PT1-H0-S8-LEGACY-C2-RC9-SHARDED` | `DEV_TESTS_PASS_21_OF_21 / RC_FROZEN / STATIC_AUDIT_PENDING` | base SHA `AA3687...E4818`, runner SHA `517B41...6B92`; V2 per-dNeff shardy po RC8 timeout, batch `9/10`; iba sampled legacy-anchor citlivosť | exact RC9 sa nemení; po nezávislom static audite možno povoliť každý z troch shardov najviac raz |
| `V318-PT1-H0-S8-LEGACY-C2-RC10-GRID-CELL` | `DEV_TESTS_PASS_23_OF_23 / RC_FROZEN / STATIC_AUDIT_PENDING` | base SHA `7E81F8...0D982`, runner SHA `28BAFD...2A8EE`, V3 SHA `DC6E8C...E54F7`; 9 grid buniek, batch 2 `0/10`, cumulative `10`; iba sampled legacy-anchor citlivosť | exact RC10 sa nemení; official run každej bunky ostáva zakázaný do nezávislého static auditu a autorizačného zápisu |
| `V318-PT1-H0-S8-LEGACY-C2-RC11-N8000-STAGED` | `DEV_TESTS_PASS_26_OF_26 / RC_FROZEN / STATIC_AUDIT_PENDING` | base SHA `8727CE...25AD2`, runner SHA `6935F3...ADDD0`, V4 SHA `5E2A35...25D42`; spoločná n8000 referencia + 3 hash-bound modely + 3 ľahké agregácie; 6 rawov n2000/n4000 immutable | auditovať najprv exact reference stage; model/aggregate ostáva NO_RUN do zmrazenia upstream SHA |
| `V318-PT1-H0-S8-LEGACY-C2-RC12-N8000-STAGED` | `DEV_TESTS_PASS_27_OF_27 / RC_FROZEN / STATIC_REAUDIT_PENDING` | base SHA `F5E224...8E898`, runner SHA `6935F3...ADDD0`, V4 SHA `5E2A35...25D42`; RC11 T1 evidence omission fixed; batch2 `1/10`, cumulative11 | exact RC12 reference success must expose frozen stage ledger and complete root/distance residual evidence; reference remains NO_RUN pending audit |
| `v001` | `NOT_CREATED` | budúci prvý nemenný balík po parite | vyžaduje samostatný PRERUN a changelog |

Staršia formulácia „žiadny modul neexistuje“ bola pravdivá pri vytvorení
návrhu, ale neskoršie implementácie ju obmedzili. Tento register ju
nenápadne nemaže: zaznamenáva, že moduly vznikli bez formálneho `vNNN` a sú
preto od 2026-07-16 zmrazené hashom ako legacy rodiny.

Presné hashe a vlastníctvo: `00_MODULE_OWNERSHIP_REGISTER.md`.
