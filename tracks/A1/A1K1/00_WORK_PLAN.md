# A1-K1 — živý plán práce a release oporný bod

**Aktualizované:** 2026-07-30  
**Stav A1-K1:** `LIVE / CONDITIONED`  
**Aktívna stanica:** `A2`  
**Aktívna fyzikálna koľaj:** `A2-K4 -> P5 -> B6b-2.11`  
**Kanonická hĺbka najlepšej živej cesty:** `60/100 = G6`

## Cieľ

Nájsť aspoň jeden lokálny a konzistentný A2 uzáver lineárnych porúch, ktorý
zachová zmrazený A1-K1 background a oprávni vstup na A3. Historické
technické checkpointy ani neúspešné implementácie samy A1-K1 nezatvárajú.

## Stav A2 koľají

| Koľaj | Stav | Hĺbka | Workflow návrat alebo ďalší krok |
|---|---|---:|---|
| A2-K1 | `STOP_SCOPE M-009 / SCIENTIFIC` | `40/100` | iba nový mechanizmus |
| A2-K2 | `STOP_SCOPE M-008 / SCIENTIFIC` | `30/100` | iba nová fyzická uzávera |
| A2-K3 | `STOP_SCOPE M-010 / SCIENTIFIC` | `40/100` | iba nový operátor |
| **A2-K4** | **`LIVE_ACTIVE / CONTRACT_RC_FROZEN`** | **`60/100`** | **nezávislý audit contractu 293, potom D1-D2** |
| A2-K5 | `STOP_SCOPE M-012 / SCIENTIFIC` | `40/100` | nová akcia je nová koľaj |
| A2-K6 | `STOP_SCOPE M-013 / SCIENTIFIC` | `30/100` | iba nový operátor/akcia |
| A2-K7 | `LIVE_BACKUP / WAITING_FOR_KERNEL` | `20/100` | nový pozitívny lokálny kernel |
| A2-K8 | `LIVE_BACKUP / WAITING_FOR_COLLISION_OPERATOR` | `10/100` | explicitný relaxačný/collision `C[f]` |
| A2-K9 | `LIVE_BACKUP / WAITING_FOR_SHARED_OPERATOR` | `10/100` | spoločný production/transport operator |
| A2-K11 | `WITHDRAW_FALSE_PASS / LIVE_BACKUP / WAITING_FOR_OPERATOR_AND_FULL_DAE` | `10/100` | fyzický contract; technická A3 vetva má counter `0/10` |
| A2-K12 | `LIVE_BACKUP / WAITING_FOR_PAIR_KERNEL` | `10/100` | pair kernel + separation ledger |
| A1-K2/A2-K10 | `SEPARATE_ROUTE / NOT_AUTHORIZED` | orientačne `10/100` | A1-K2 background passport |

K1/K2/K3/K5/K6 majú R7 potvrdené scoped vedecké dôvody. K7/K8/K9/K11/K12
nemajú scientific STOP celého rodiča: sú živé zálohy čakajúce na presný
fyzikálny contract. Ich staré technické stop-y alebo mŕtve dcéry ich
nesmú držať v stave `CLOSED`.

## Akčné poradie

1. **A2-K4/P5/B6b-2.11** — audit exact contractu 293; po PASS analyticky
   uzavrieť D1-D2, následne D3-D6.
2. **P5.4** — species-first evolúcia až po prijatom fyzikálnom witness alebo
   presnom same-track výsledku P5.3.
3. **G8 -> G9 -> A3** — iba sekvenčne po prijatých predchádzajúcich bránach.
4. Ak A2-K4 čaká na nový autorov fyzikálny vstup, otvoriť nanajvýš jednu
   analytickú zálohu v poradí K8, K9, K12, K11, K7; bez solvera pred
   contractom a bez prepisovania scoped STOP dcér.

Naraz je aktívna iba jedna fyzikálna implementácia. Read-only analytická
kontrola zálohy môže prebiehať samostatne, ale neudeľuje jej bránu.

## Stopping kritérium A1-K1

A1-K1 sa uzavrie až pri všeobecnom no-go backgroundu alebo keď všetky
registrované A2 mechanizmové triedy dostanú úplný scoped vedecký STOP s
nezávislým auditom. `TECHNICAL_PERMISSION_GATE`, timeout, chýbajúci backend
alebo uzavretie pomocnej source línie túto podmienku nespĺňa.

## Nadväzujúce oporné body

- globálny živý stav: `tracks/00_CURRENT_EXECUTION_PLAN.md`;
- register A2: `A2/00_TRACK_REGISTER.md`;
- aktívna koľaj: `A2/A2K4/00_WORK_PLAN.md`;
- aktívny P5 contract: `A2/A2K4/SUBTRACKS/P5/00_WORK_PLAN.md`;
- historická K7 implementácia: `A2/A2K4/SUBTRACKS/C7_7c/K7/00_WORK_PLAN.md`.

Tento súbor sa mení iba pri zmene fyzikálnej koľaje, poradia práce,
kanonickej hĺbky alebo release snapshotu.
