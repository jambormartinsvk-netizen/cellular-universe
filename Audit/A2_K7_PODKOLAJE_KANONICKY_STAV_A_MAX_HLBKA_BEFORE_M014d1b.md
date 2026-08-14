# A2-K7 — kanonický stav podkoľají a Max. hĺbka

**Dátum:** 2026-07-13  
**Aktualizácia:** po `M-014d2a`, úplná hierarchia  
**Akceptované skóre K7:** `30/100`

## Stupnica

| Hĺbka | Význam |
|---:|---|
| `5/100` | pomenovaná, ešte neauditovaná možnosť |
| `30/100` | prijatý K7.0 ledger a collision-sign brána |
| `32/100` | konštantné lokálne šírky |
| `34/100` | backgroundová rekonštrukcia |
| `36/100` | kovariantný/gauge ledger |
| `38/100` | Onsager/noise pozitivita |
| `39/100` | rozmerová backgroundová existencia |
| `40/100` | konkrétna bath/rate brána |
| `41/100` | vedúca spin-2 action/Ward/rate brána |
| `50/100` | úplné lineárne a superhorizontové perturbácie |
| `60/100` | high-k a rast |
| `70/100` | CMB-normalizovaná rastová brána |
| `80+/100` | likelihood, nelinearity, systematiky |

## Aktuálna tabuľka

`Max. hĺbka` nadradeného uzla je najhlbší vykonaný test v jeho potomkoch;
nie je to automaticky akceptované skóre.

| Podkoľaj | Stav | Max. hĺbka | Akceptovaná hĺbka K7 | Dôvod/stena |
|---|---|---:|---:|---|
| K7.1a-K1 | `MŔTVA M-014a` | `32/100` | `30/100` | fixed-width no-go |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | `34/100` | `30/100` | chýba kernel/memory/noise |
| K7.1a-K3.0 | `PREŽILA FORMULAČNÚ BRÁNU` | `36/100` | `30/100` | mikrofyzika chýba |
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `38/100` | `30/100` | záporný Onsagerov eigenmode |
| K7.1a-K3.1-K2 | `OTVORENÁ CEZ PODKOĽAJE` | `41/100` | `30/100` | pozitívna kompletizácia existuje; žiadna mikrofyzická dcéra zatiaľ neprežila |
| K7.1a-K3.1-K2.1 | `PREŽÍVA IBA ROZMEROVÚ BACKGROUNDOVÚ EXISTENCIU` | `39/100` | `30/100` | 18/24 bodov; voľný bath/noise |
| K7.1a-K3.1-K2.2 | `OTVORENÁ CEZ BATH PODKOĽAJE` | `41/100` | `30/100` | dva konkrétne gravitonové varianty zomreli; ďalšie čakajú |
| K7.1a-K3.1-K2.2-K1 | `OTVORENÁ TERMÁLNA VETVA` | `41/100` | `30/100` | K1a a K1b1 mŕtve; K1b2 aktívna |
| K7.1a-K3.1-K2.2-K1a | `MŔTVA M-014d1` | `40/100` | `30/100` | gravity-only para príliš slabá |
| K7.1a-K3.1-K2.2-K1b | `OTVORENÁ CEZ K1b2/K1b3` | `41/100` | `30/100` | vedúca väzba mŕtva, curvature/multigraviton možnosti nerozhodnuté |
| K7.1a-K3.1-K2.2-K1b1 | `MŔTVA M-014d2a` | `41/100` | `30/100` | vedúca spin-2 väzba vyžaduje `G_eff~1e48 G_N` |
| K7.1a-K3.1-K2.2-K1b2 | `AKTÍVNA` | `5/100` | `30/100` | higher-derivative curvature operátory |
| K7.1a-K3.1-K2.2-K1b3 | `ČAKÁ` | `5/100` | `30/100` | ďalšie massless spin-2 pole |
| K7.1a-K3.1-K2.2-K1c | `ČAKÁ` | `5/100` | `30/100` | nový nespin-2 termálny bath |
| K7.1a-K3.1-K2.2-K1d | `ČAKÁ` | `5/100` | `30/100` | interný tracked bath |
| K7.1a-K3.1-K2.2-K2 | `ČAKÁ` | `5/100` | `30/100` | vákuový farebný kernel |
| K7.1a-K3.1-K2.2-K3 | `ČAKÁ` | `5/100` | `30/100` | netermálny farebný bath |
| K7.1a-K4 | `ČAKÁ` | `5/100` | `30/100` | threshold smer |

M-014d2a platí iba pre K1b1. K1b2 ostáva aktívna. Mŕtve podkoľaje, skripty,
erratum, dôvody a maximálne hĺbky zostávajú zachované. Nadradený uzol sa
označí za mŕtvy až vtedy, keď zomrú všetky jeho dcéry.

