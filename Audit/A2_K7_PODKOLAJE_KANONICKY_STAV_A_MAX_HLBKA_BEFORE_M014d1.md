# A2-K7 — kanonický stav podkoľají a Max. hĺbka

**Dátum:** 2026-07-13  
**Aktualizácia:** po K7.1a-K3.1-K2.1  
**Účel:** jedna aktuálna tabuľka, v ktorej žiadnej podkoľaji nechýba
`Max. hĺbka`

## Stupnica K7.1a

| Hĺbka | Význam |
|---:|---|
| `30/100` | prijatý K7.0 ledger a collision-sign brána |
| `32/100` | audit konštantných lokálnych šírok |
| `34/100` | audit state-dependent backgroundovej rekonštrukcie |
| `36/100` | kovariantný `delta Q`, gauge a vektorový ledger |
| `38/100` | SK/Onsager/noise pozitivitná štruktúra |
| `39/100` | rozmerová backgroundová existencia bez odvodeného kúpeľa |
| `40/100` | rozmerový mikrofyzický kernel, bath a background uzavreté |
| `50/100` | úplné lineárne a superhorizontové perturbácie |
| `60/100` | high-k a efektívny rast |
| `70/100` | CMB-normalizovaná rastová brána |
| `80+/100` | Boltzmann likelihood, nelinearity a systematiky |

## Aktuálna tabuľka

| Podkoľaj | Stav | Max. hĺbka | Akceptovaná hĺbka nadradenej K7 | Dôvod/stena |
|---|---|---:|---:|---|
| K7.1a-K1 | `MŔTVA M-014a` | `32/100` | `30/100` | fixed-width no-go |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | `34/100` | `30/100` | neodvodené `Upsilon`, memory a noise |
| K7.1a-K3.0 | `PREŽILA FORMULAČNÚ BRÁNU` | `36/100` | `30/100` | `Theta_phi/deltaTheta_phi` prešli, mikrofyzika nie |
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `38/100` | `30/100` | záporná vlastná hodnota holej Onsagerovej matice |
| K7.1a-K3.1-K2 | `PREŽÍVA IBA TERMODYNAMICKÚ FORMULÁCIU` | `38/100` | `30/100` | pozitívne doplnenie existuje, koeficienty/bath nie sú odvodené |
| K7.1a-K3.1-K2.1 | `PREŽÍVA IBA ROZMEROVÚ BACKGROUNDOVÚ EXISTENCIU` | `39/100` | `30/100` | 18/24 bodov prešlo; `ell_hat`, bath a absolútny noise zostávajú voľné |
| K7.1a-K3.1-K2.2-K1 | `AKTÍVNA` | `5/100` | `30/100` | lokálny termálny/KMS bath |
| K7.1a-K3.1-K2.2-K2 | `ČAKÁ` | `5/100` | `30/100` | vákuový kvantový farebný kernel |
| K7.1a-K3.1-K2.2-K3 | `ČAKÁ` | `5/100` | `30/100` | netermálny farebný bath s pamäťou |
| K7.1a-K4 | `ČAKÁ` | `5/100` | `30/100` | zatiaľ iba opísaný threshold smer |

Maximálna hĺbka mŕtvu koľaj neoživuje. Akceptovaná hĺbka K7 sa zmení až
po prejdení celej nadradenej brány, nie iba po hlbšom diagnostickom teste
jednej podkoľaje.

Aktuálnym dôkazom pre K2.1 sú skript 59, jeho numerický výstup a samostatný
fyzikálny audit. `39/100` sa nesmie čítať ako dôkaz lokálneho KMS,
odvodenie transportných koeficientov ani ako povolenie spustiť K7.1b.

