# A2-K7 — kanonický stav podkoľají a Max. hĺbka

**Dátum:** 2026-07-13  
**Aktualizácia:** po errate K1a a `M-014d1b`  
**Akceptované skóre K7:** `30/100`

## Stupnica

| Hĺbka | Význam |
|---:|---|
| `5/100` | pomenovaná, ešte neauditovaná možnosť |
| `30/100` | prijatý K7.0 ledger a collision-sign brána |
| `32/100` | fixed-width audit |
| `34/100` | backgroundová rekonštrukcia |
| `36/100` | kovariantný/gauge ledger |
| `38/100` | Onsager/noise pozitivita |
| `39/100` | rozmerová backgroundová existencia |
| `40/100` | thermal-scattering bath/rate brána |
| `41/100` | vedúca spin-2 soft/Ward brána |
| `42/100` | transition/KMS detailed-balance brána |
| `50/100` | úplné lineárne a superhorizontové perturbácie |
| `60/100` | high-k a rast |
| `70/100` | CMB-normalizovaná rastová brána |
| `80+/100` | likelihood, nelinearity, systematiky |

`Max. hĺbka` rodiča je najhlbší vykonaný test potomka, nie akceptované
skóre.

## Aktuálna tabuľka

| Podkoľaj | Stav | Max. hĺbka | Akceptovaná hĺbka K7 | Dôvod/stena |
|---|---|---:|---:|---|
| K7.1a-K1 | `MŔTVA M-014a` | `32/100` | `30/100` | fixed-width no-go |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | `34/100` | `30/100` | chýba kernel/memory/noise |
| K7.1a-K3.0 | `PREŽILA FORMULAČNÚ BRÁNU` | `36/100` | `30/100` | mikrofyzika chýba |
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `38/100` | `30/100` | záporný Onsagerov eigenmode |
| K7.1a-K3.1-K2 | `OTVORENÁ CEZ PODKOĽAJE` | `42/100` | `30/100` | žiadna mikrofyzická dcéra zatiaľ neprežila |
| K7.1a-K3.1-K2.1 | `PREŽÍVA IBA ROZMEROVÚ EXISTENCIU` | `39/100` | `30/100` | voľný bath/noise |
| K7.1a-K3.1-K2.2 | `OTVORENÁ CEZ BATH PODKOĽAJE` | `42/100` | `30/100` | K1a2b aktívna; K2/K3 čakajú |
| K7.1a-K3.1-K2.2-K1 | `OTVORENÁ TERMÁLNA VETVA` | `42/100` | `30/100` | dve listové realizácie mŕtve; koherentná otvorená |
| K7.1a-K3.1-K2.2-K1a1 | `MŔTVA M-014d1` | `40/100` | `30/100` | iba relativistický thermal-scattering no-go |
| K7.1a-K3.1-K2.2-K1a2 | `OTVORENÁ CEZ K1a2b` | `42/100` | `30/100` | transition spectrum/matrix element neodvodené |
| K7.1a-K3.1-K2.2-K1a2a | `MŔTVA M-014d1b` | `42/100` | `30/100` | nekoherentný KMS rate chýba o 26–33 rádov |
| K7.1a-K3.1-K2.2-K1a2b | `OTVORENÁ KOHERENTNÁ VETVA` | `5/100` | `30/100` | potrebuje odvodený form factor a coherence budget |
| K7.1a-K3.1-K2.2-K1a2b-K1 | `AKTÍVNA` | `5/100` | `30/100` | kauzálne konečná koherentná doména |
| K7.1a-K3.1-K2.2-K1a2b-K2 | `ČAKÁ` | `5/100` | `30/100` | ideálny superradiant horný limit |
| K7.1a-K3.1-K2.2-K1a2b-K3 | `ČAKÁ` | `5/100` | `30/100` | globálna sieťová koherencia |
| K7.1a-K3.1-K2.2-K1a2c | `PRESUNUTÁ DO K2` | `42/100` | `30/100` | high-frequency non-KMS spontaneous emission |
| K7.1a-K3.1-K2.2-K1b1 | `MŔTVA M-014d2a` | `41/100` | `30/100` | vedúce soft zosilnenie; čísla rate sú channel-specific |
| K7.1a-K3.1-K2.2-K1b2 | `ČAKÁ` | `5/100` | `30/100` | higher-derivative curvature operátory nezabité |
| K7.1a-K3.1-K2.2-K1b3 | `ČAKÁ` | `5/100` | `30/100` | ďalšie massless spin-2 pole |
| K7.1a-K3.1-K2.2-K1c | `ČAKÁ` | `5/100` | `30/100` | nový nespin-2 bath |
| K7.1a-K3.1-K2.2-K1d | `ČAKÁ` | `5/100` | `30/100` | interný tracked bath |
| K7.1a-K3.1-K2.2-K2 | `ČAKÁ + PRIJÍMA K1a2c` | `42/100` | `30/100` | vákuový/farebný kernel |
| K7.1a-K3.1-K2.2-K3 | `ČAKÁ` | `5/100` | `30/100` | netermálny farebný bath |
| K7.1a-K4 | `ČAKÁ` | `5/100` | `30/100` | threshold smer |

Mŕtve listy, presunuté listy, errata, skripty a maximálne hĺbky zostávajú
zachované. Rodič zomrie až po smrti všetkých dcér.

