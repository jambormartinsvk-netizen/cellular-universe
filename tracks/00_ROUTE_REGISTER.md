# Register ciest

**Aktualizované:** 2026-08-14  
**Autorita živého stavu:** `tracks/00_CURRENT_EXECUTION_PLAN.md`

Hĺbka je najvyššia sekvenčne prejdená kanonická brána; nie je to
pravdepodobnosť pravdy ani najhlbší historický technický test.

## Upstream blok od 2026-08-14

Zavedená stanica `A0` (`tracks/A0/00_STATION.md`) je **upstream od všetkých
routes nižšie**. Do jej rozhodnutia sú všetky `R-A1K1-*` a `R-A1K2-*`
`FROZEN_PENDING_A0`: zostávajú živé, ich hĺbky sa nemenia, ale **žiadny nový
task, prereg, RC ani official run sa v nich neotvára**. Dôvod v
`Audit/EA_EXT2_2026-08-14/00_RESPONSE_TO_EXTERNAL_AUDIT_2_SK.md` §6.

| Route ID | Cesta | Autoritatívny stav | Workflow fáza | Hĺbka | Najbližší zákonný prechod |
|---|---|---|---|---:|---|
| `R-A0-K5` | `A0K5` — separácia škál EFT/LV | `LIVE_ACTIVE / PRIORITA_1` | `CONTRACT_DRAFT_OPEN` | `10/100 = G1` | smyčka s cutoffom `M < k_max`; overiť škálovanie `(M/Λ)²` |
| `R-A0-K3` | `A0K3` — silne viazaný RG fixný bod | `LIVE / OPEN / PRIORITA_2` | `CONTRACT_DRAFT_NOT_OPEN` | `10/100 = G1` | model na sieti s **bezrozmernou** väzbou; null-kontrola `W=k²` |
| `R-A0-K1` | `A0K1` — ochrana supersymetriou | `STOP_SCOPE / CONDITIONAL` | zatvorená pri fixnom `C` | `10/100 = G1` | iba odvodenie škálovo závislej kapacity (`TRACK_IDENTITY_GATE`) |
| `R-A0-K2` | `A0K2` — diskrétnosť v priestoročase | `SEPARATE_ROUTE` | mimo súčasnej ontológie | `20/100 = G2` | Rideout–Sorkin CSG rekonštrukcia; prepis od základov |
| `R-A0-K4` | `A0K4` — ladenie `g/Λ` | `NOT_ADMISSIBLE` | — | `0/100` | žiadny; nie je to mechanizmus |
| `R-A1K1-A2K1` | `A1K1 -> A2K1` | `STOP_SCOPE M-009 / SCIENTIFIC` | closed exact scope | `40/100 = G4` | iba nový mechanizmus |
| `R-A1K1-A2K2` | `A1K1 -> A2K2` | `STOP_SCOPE M-008 / SCIENTIFIC` | closed exact scope | `30/100 = G3` | iba nová fyzická uzávera |
| `R-A1K1-A2K3` | `A1K1 -> A2K3` | `STOP_SCOPE M-010 / SCIENTIFIC` | closed exact scope | `40/100 = G4` | iba nový operátor |
| `R-A1K1-A2K4` | `A1K1 -> A2K4 -> P5/B6b-2.11` | `LIVE_ACTIVE` | `CONTRACT_RC_FROZEN / AUDIT_PENDING` | `60/100 = G6` | audit contractu 293, potom D1-D2 |
| `R-A1K1-A2K5` | `A1K1 -> A2K5` | `STOP_SCOPE M-012 / SCIENTIFIC` | closed exact action | `40/100 = G4` | nová akcia je nová koľaj |
| `R-A1K1-A2K6` | `A1K1 -> A2K6` | `STOP_SCOPE M-013 / SCIENTIFIC` | closed exact operator class | `30/100 = G3` | iba nový operátor/akcia |
| `R-A1K1-A2K7` | `A1K1 -> A2K7` | `LIVE_BACKUP / WAITING` | `CONTRACT_DRAFT_NOT_OPEN` | `20/100 = G2` | pozitívny lokálny kernel + noise/memory |
| `R-A1K1-A2K8` | `A1K1 -> A2K8` | `LIVE_BACKUP / WAITING` | `CONTRACT_DRAFT_NOT_OPEN` | `10/100 = G1` | explicitný relaxačný/collision `C[f]` |
| `R-A1K1-A2K9` | `A1K1 -> A2K9` | `LIVE_BACKUP / WAITING` | `CONTRACT_DRAFT_NOT_OPEN` | `10/100 = G1` | shared production/transport operator |
| `R-A1K1-A2K11` | `A1K1 -> A2K11` | `WITHDRAW_FALSE_PASS / LIVE_BACKUP / WAITING` | `CONTRACT_DRAFT_NOT_OPEN`; active technical counter `0/10` | `10/100 = G1` | derived regular operator + full DAE contract |
| `R-A1K1-A2K12` | `A1K1 -> A2K12` | `LIVE_BACKUP / WAITING` | `CONTRACT_DRAFT_NOT_OPEN` | `10/100 = G1` | pair kernel + separation ledger |
| `R-A1K2-A2K10` | `A1K2 -> A2K10` | `SEPARATE_ROUTE / NOT_AUTHORIZED` | pred A1-K2 passportom | orientačne `10/100` | samostatný background contract |

`LIVE_BACKUP / WAITING` nahrádza nejednoznačné `REVIEW_BLOCKED_PARENT` tam,
kde chýba fyzikálny contract, ale neexistuje scientific STOP celého rodiča.
Technický terminál podkoľaje sa nikdy neprenáša na rodičovskú route.

Historická K7 technická hĺbka `66.5/100` zostáva iba v K7 histórii. K7
reduced-RHS implementácia je terminálna, no A2-K4 pokračuje cez P5.
