# A2/Q20 — problém perturbácií a koľaje K1 až K5

**Dátum založenia:** 2026-07-13  
**Nadväzuje na:** A1/Q19, koľaj A1-K1  
**Aktuálny stav:** A2.0 kovariantný ledger zostavený; A2-K1 postupuje do odvodenia lineárnych perturbácií

## 1. Presný problém

A1-K1 určila, že homogénny prenos

`Q = Gamma rho_f`, `Gamma = lambda H0 > 0`

odoberá energiu palivu a vytvára iba CDM/popol. Na presne homogénnom pozadí však všetky kozmické zložky zdieľajú jednu štvorrýchlosť. Pozadie preto nedokáže rozlíšiť:

- smer prenosového štvorvektora;
- prenos hybnosti;
- pokojovú zvukovú rýchlosť paliva;
- tlakovú poruchu a anizotropný stres;
- adiabatické a izokurvatúrne módy.

Q20 znie:

> Aký je úplný kovariantný, gauge-konzistentný a stabilný systém lineárnych porúch pre palivo, CDM/popol, baryóny, fotóny, neutrína a paru, ktorý má background A1-K1 ako svoju homogénnu limitu?

## 2. Nezameniteľné označenia

- **A1-K1:** backgroundová voľba príjemcu — `Q` vytvára iba CDM/popol.
- **A2-K1 až A2-K5:** možné kovariantné a perturbačné uzávery toho istého backgroundu.
- **S8-K1a:** staré ad hoc trenie celej látky — mŕtve.
- **S8-K1b:** prípadná dodatočná výmena hybnosti v tmavom sektore — nesmie sa otvoriť pred dokončením základnej A2-K1.

## 3. Koľaje Q20

| Poradie | Koľaj | Definícia | Stav |
|---:|---|---|---|
| 1 | **A2-K1** | `Q^mu = Gamma rho_f u_c^mu`; CDM rámec; palivo má efektívnu skalárno-poľovú uzáveru `c_s,f^2=1`, `pi_f=0` | **AKTÍVNA; PREŽÍVA A2.0 48/100** |
| 2 | **A2-K2** | Rovnaký prenos, ale striktne barotropické palivo `p_f=w_f rho_f`, `c_s,f^2=c_a,f^2=w_f` | **MŔTVA — ARCHIVOVANÁ** |
| 3 | **A2-K3** | `Q^mu = Gamma rho_f u_f^mu`; bez prenosu hybnosti v rámci paliva | `ČAKÁ` |
| 4 | **A2-K4** | `Q^mu = Gamma rho_f u_d^mu`; smer celkovej štvorrýchlosti tmavého sektora | `ČAKÁ` |
| 5 | **A2-K5** | Prenos odvodený z lokálnej akcie/mediátora namiesto fenomenologického štvorvektora | `ČAKÁ`; môže vyžadovať v4 |

Hodnotenie je zrelosť dôkazu, nie pravdepodobnosť pravdivosti.

## 4. Prečo začíname A2-K1

A2-K1:

- presne reprodukuje A1-K1 background;
- nepridáva parameter do backgroundu;
- zachováva geodetickú Eulerovu rovnicu CDM v jeho vlastnom rámci;
- má explicitný protizdroj v palive;
- používa známu efektívnu uzáveru `c_s^2=1` ako najbezpečnejší prvý test.

Uzávera `c_s,f^2=1` je **pracovný efektívny postulát**, nie odvodenie kanonického skalárneho poľa. Ak nebude možné nájsť kompatibilnú akciu alebo stabilné počiatočné podmienky, A2-K1 zomrie aj napriek správnemu backgroundu.

## 5. Smrť A2-K2

Pri konštantnom

`w_f = -1 + delta = -0.97703`

má striktne barotropická tekutina

`c_s,f^2 = dp_f/d rho_f = w_f = -0.97703 < 0`.

V krátkovlnnom limite má porucha hlavný člen

`delta_f'' + c_s,f^2 k^2 delta_f approximately 0`,

takže namiesto oscilácie vznikne

`delta_f proportional exp(|c_s,f| k eta)`.

Lokálny algebraický prenos `Q=Gamma rho_f` nepridáva člen rádu `+k^2`, ktorý by zmenil hlavný symbol rovnice. Negatívne `c_s^2` preto predstavuje gradientovú nestabilitu.

Reprodukčný výpočet:

- `scripts/21_script_A2_barotropic_fuel_gradient_instability.py`;
- `scripts/README_AUDIT_SCRIPT_21.md`;
- `Audit/A2_K2_MRTVA_barotropicke_palivo_gradientova_nestabilita.md`.

Verdikt nezabíja A2-K1 s nezávislou pokojovou zvukovou rýchlosťou `c_s,f^2=1`.

## 6. Brány aktívnej A2-K1

| Brána | Požiadavka | Stav |
|---|---|---|
| A2.0-L | Úplný ledger zložiek a `sum_A Q_A^mu=0`. | **PREŠLA V DEKLAROVANOM EFEKTÍVNOM ROZSAHU** |
| A2.0-G | `Gamma` je lokálny konštantný skalár; `lambda=Gamma/H0` je iba parametrizácia. | **PREŠLA PODMIENEČNE** |
| A2.0-C | Palivová uzávera `c_s,f^2=1`, `pi_f=0` je jednoznačne označená ako postulát. | **PREŠLA DEFINIČNE, NIE MIKROFYZIKÁLNE** |
| A2.1 | Úplné kontinuity, Eulerove rovnice a metrické constrainty. | **NASLEDUJE** |
| A2.2 | Gauge, nulový limit, super/subhorizont, stabilita a počiatočné módy. | `ČAKÁ` |
| A2.3 | Numerická validácia celého systému. | `ČAKÁ` |
| A3 | CLASS/CAMB a spektrá. | `BLOKOVANÉ A2` |
| A8 | Predregistrovaný likelihood. | `BLOKOVANÉ A3` |

## 7. Predregistrované steny A2-K1

Koľaj zomrie, ak sa potvrdí aspoň jedno:

1. `sum_A Q_A^mu != 0` po úplnom perturbačnom rozklade;
2. gauge-dependentná fyzikálna predikcia;
3. nekontrolovaná superhorizontová rastová moda;
4. ghostová alebo gradientová nestabilita;
5. singularita pri `w_f -> -1`, `rho_f -> 0` alebo v požadovanom časovom intervale;
6. nulový limit nereprodukuje štandardné CDM+baryónové perturbácie;
7. počiatočné podmienky vyžadujú ľubovoľné potlačenie nestabilnej mody;
8. plná implementácia vylúči parameter potrebný pre registrovaný background.

## 8. Najbližší výstup

Odvodiť A2.1 pre A2-K1 v Newtonovej gauge a potom vytvoriť nezávislý gauge-invariantný alebo synchrónny cross-check. Nepoužívať pôvodnú rastovú rovnicu V3 ako vstup; musí vyjsť iba ako prípadný limit.

## 9. Primárne metodické zdroje

- [Malik a Wands — gauge-invariantné interagujúce tekutiny](https://arxiv.org/abs/astro-ph/0411703).
- [Valiviita, Majerotto a Maartens — skoré nestability jednoduchých interagujúcich modelov](https://arxiv.org/abs/0804.0232). Ich konkrétny prenos nie je totožný s A2-K1; zdroj určuje povinný typ testu, nie verdikt nášho modelu.
- [Clemson et al. — rozdiel medzi prenosom rovnobežným s `u_c` a `u_x`](https://arxiv.org/abs/1109.6234).
- [Yang a Xu — explicitné porovnanie rámcov prenosu pri perturbáciách](https://arxiv.org/abs/1409.5533).
- [Shah, Mukherjee a Pal — novší príklad spoločnej analýzy backgroundu a perturbácií](https://arxiv.org/abs/2503.21652).

