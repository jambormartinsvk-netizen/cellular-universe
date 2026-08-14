# A1/Q19 — čo znamená „prešla iba bránou pozadia“

**Dátum aktualizácie:** 2026-07-13  
**Koľaj:** A1-K1 — prenos `Q` vytvára iba CDM/popol, baryóny sú konzervované  
**Aktuálny verdikt:** **PREŽÍVA 40/100 — iba kandidát kozmologického pozadia**

## 1. Krátka odpoveď

„Prešla bránou pozadia“ znamená, že rovnice správne opisujú vývoj **priemerných homogénnych hustôt** v FLRW vesmíre. Priestor má v tomto teste všade rovnakú hustotu; nepočíta sa `delta rho(x,t)`, rýchlostné pole, gravitačné potenciály, CMB ani rast galaxií.

Prešlo teda účtovníctvo priemernej energie. Ešte neprešla fyzika nerovnomerného vesmíru.

## 2. Čo presne bolo testované a prešlo

Pracovná definícia:

```text
nabla_mu T_f^(mu nu) = -Q^nu
nabla_mu T_c^(mu nu) = +Q^nu
nabla_mu T_b^(mu nu) = C_b^nu
nabla_mu T_r^(mu nu) = C_r^nu

Q^nu = Gamma rho_f u_c^nu
Gamma = lambda H0
C_b^nu + C_r^nu = 0
```

Na homogénnom pozadí sa testovali rovnice:

```text
rho_f' = -3 delta rho_f - lambda(H0/H) rho_f
rho_c' = -3 rho_c + lambda(H0/H) rho_f
rho_b' = -3 rho_b
rho_r' = -4 rho_r
```

| Test pozadia | Čo overil | Stav |
|---|---|---|
| A1-K1-T0 | Prijímateľ, smer a znamienko toku sú jednoznačné. | **PREŠIEL** |
| A1-K1-T1 | Zdroj `-Q+Q` sa v súčte priemerných rovníc presne vyruší. | **PREŠIEL** |
| A1-K1-T2 | `Q=Gamma rho_f` má rozmery hustoty energie za čas. | **PREŠIEL** |
| A1-K1-T3 | Pri `lambda=0` sa obnoví neinteragujúci limit `rho_b,rho_c proportional a^-3`. | **PREŠIEL** |
| A1-K1-T4 | Rozdelenie spoločnej hmoty na baryóny a CDM je algebraicky zhodné s backgroundom skriptov 08/09. | **PREŠIEL** |
| A1-K1-T5 | Hustoty zostali kladné, zachovanie a numerická konvergencia splnili tolerancie. | **PREŠIEL** |
| A1-K1-T6 | Neskorý bunkový prenos nemení komohybné baryónové číslo. | **PREŠIEL ŠTRUKTURÁLNE** |

Reprodukčný dôkaz:

- `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py`;
- `scripts/STATUS_A1_K1_SCRIPTS_11_13.md`;
- neúspešné skripty 11 a 12 sú zachované s erratami.

Referenčný výsledok pracovného bodu:

- približne `8.999 %` dnešnej komovanej CDM vzniklo od rekombinácie;
- baryónový podiel v hmote klesol z približne `0.15644` pri rekombinácii na `0.14439` dnes;
- ide o dôsledok pracovnej implementácie, nie o potvrdené meranie.

## 3. Prečo pozadie nestačí

V presne homogénnom FLRW pozadí majú všetky zložky rovnaký kozmologický pokojový rámec. Viaceré fyzikálne odlišné prenosy `Q^mu` preto môžu viesť k rovnakej rovnici pre priemernú hustotu.

Až pri poruchách sa ukáže:

- ako sa prenos mení v prehustenej a podhustenej oblasti;
- kam ide hybnosť;
- ako sa pohybujú baryóny a CDM;
- či vznikajú nestability;
- čo sa stane s CMB, `P(k)`, lensingom a `S8`.

Preto backgroundový PASS nie je dôkazom, že je správne zvolený celý štvorvektor `Q^mu`.

## 4. Zostávajúce brány

### G2 — A2.0: kovariantný ledger

Treba presne určiť pre každú zložku:

- `rho_A`, `p_A`, `w_A`;
- štvorrýchlosť a pokojový rámec;
- pokojovú zvukovú rýchlosť;
- tlakovú poruchu a anizotropný stres;
- energetickú časť `Q_A` a hybnostnú časť `F_A^mu` v rozklade

  `Q_A^mu = Q_A u^mu + F_A^mu`, `u_mu F_A^mu=0`;

- identitu `sum_A Q_A^mu=0` aj mimo homogénneho pozadia.

**Kill condition:** chýbajúci prijímateľ energie/hybnosti alebo nutnosť skrytého rezervoára bez založenia novej koľaje.

### G3 — A2.1/A2.2: lineárne perturbácie

Treba odvodiť:

1. `delta Q` z lokálnej definície prenosu, nie ju ľubovoľne nastaviť;
2. kontinuitné a Eulerove rovnice paliva, CDM a baryónov;
3. metrické constrainty;
4. palivovú tlakovú poruchu a zvukovú rýchlosť pri `w_f=-1+delta`;
5. gauge-invariantné pozorovateľné veličiny;
6. adiabatické a prípadné izokurvatúrne počiatočné módy.

Povinné testy:

| Test | Požiadavka | Stav |
|---|---|---|
| A2-T0 | Jednoznačná notácia, znamienka, metrika a Fourierova konvencia. | **ČAKÁ** |
| A2-T1 | `sum_A Q_A^mu=0` na pozadí aj v poruchách. | **ČAKÁ** |
| A2-T2 | `lambda->0` obnoví štandardné CDM+baryónové perturbácie. | **ČAKÁ** |
| A2-T3 | Fyzikálne pozorovateľné veličiny sú gauge-invariantné. | **ČAKÁ** |
| A2-T4 | Superhorizontový limit je regulárny; vývoj `zeta` je vysvetlený. | **ČAKÁ** |
| A2-T5 | Subhorizontový limit dá správnu rovnicu rastu. | **ČAKÁ** |
| A2-T6 | Bez ghostovej, gradientovej a nekontrolovanej skorej nestability. | **ČAKÁ** |
| A2-T7 | Hustoty, zvukové rýchlosti a menovatele zostávajú fyzikálne. | **ČAKÁ** |
| A2-T8 | Počiatočné podmienky neobsahujú skrytý ľubovoľný mód. | **ČAKÁ** |

**Hlavná stena:** potvrdená ghostová, gradientová alebo nekontrolovaná superhorizontová nestabilita v oblasti parametrov potrebnej teóriou.

### G4 — A2.3: numerická validácia perturbácií

Po odvodení rovníc treba vytvoriť:

- `scripts/21_script_A2_perturbation_limit_and_stability_tests.py`;
- `scripts/README_AUDIT_SCRIPT_21.md`;
- zmrazené vstupy a výstupy.

Skript musí overiť nulový limit, bilanciu energie/hybnosti, skoré časy, rozsah `k`, singularity a konvergenciu tolerancií.

**Stav:** **ČAKÁ; skript 21 ešte neexistuje.**

### G5 — A3: Boltzmannova implementácia

Po pozitívnom A2 treba model implementovať do zmrazenej verzie CLASS alebo CAMB:

1. najprv reprodukovať štandardné ΛCDM spektrá v tom istom kóde;
2. zapnúť A1-K1 bez dodatočného drag parametra;
3. vypočítať background, CMB `C_ell`, matter power `P(k)`, lensing a rast;
4. overiť konvergenciu a nezávislé limity.

**Stav:** **BLOKOVANÉ A2.**

### G6 — Q31: mikrofyzika popola

Treba určiť:

- spin a hmotnosť;
- stabilitu a kvantové čísla;
- distribučnú funkciu a chladnosť;
- voľnú dráhu a phase-space limity;
- správanie v halách a klastroch;
- dovolené interakcie.

**Stav:** **OTVORENÉ.** Backgroundová rovnica sama nedokazuje, že taká častica alebo excitácia môže existovať.

### G7 — A8: predregistrovaný plný dátový fit

Po A2/A3 treba vopred zmraziť datasety, covariance, nuisance parametre, priory, počet parametrov, štatistický prah a validačnú množinu. Povinný spoločný test zahŕňa aspoň CMB, BAO, SN, RSD, weak lensing, `H0`, `Omega_m`, `S8` a baryónové podiely.

Osobitne sa musí otestovať približne `8.999 %` neskoro vytvorenej CDM.

**Stav:** **BLOKOVANÉ A2+A3.** Lokálne `chi2_3front` túto bránu nenahrádza.

## 5. Mapa stavu

| Brána | Oblasť | Stav |
|---|---|---|
| G1 | Homogénne pozadie a numerika | **PREŠLA** |
| G2 | Kovariantný ledger mimo pozadia | **ČAKÁ — najbližší krok** |
| G3 | Analytické lineárne perturbácie a stabilita | **ČAKÁ** |
| G4 | Numerický test perturbácií | **ČAKÁ** |
| G5 | CLASS/CAMB a spektrá | **BLOKOVANÁ G3/G4** |
| G6 | Mikrofyzika popola | **OTVORENÁ paralelná vetva** |
| G7 | Plný dátový fit | **BLOKOVANÁ G5** |

## 6. Prečo hodnotenie 40/100

Hodnotenie vyjadruje **zrelosť dôkazu, nie 40 % pravdepodobnosť pravdivosti**.

- definícia prijímateľa a znamienok: hotová;
- zachovanie, rozmery, nulový limit a kladnosť pozadia: hotové;
- reprodukovateľná numerika a konvergencia pozadia: hotové;
- perturbácie a stabilita: chýbajú;
- CLASS/CAMB spektrá: chýbajú;
- mikrofyzika popola: chýba;
- plný dátový fit: chýba.

Ak A2 narazí na stenu, A1-K1 sa označí `MŔTVA — ARCHIVOVANÁ` a otvorí sa ďalšia koľaj A1-K4, A1-K5, A1-K2 alebo A1-K3 podľa registrovaného poradia. Backgroundový úspech sa pritom zachová ako negatívne poučenie: konzistentné priemerné účtovníctvo samo nestačí na konzistentnú fyziku porúch.

## 7. Autoritatívne podklady

- `Questions/A1_Q19_problem_prijemcu_Q_kolaje_K1-K5.md` — pôvodný problém, koľaje a testy T0–T8;
- `scripts/STATUS_A1_K1_SCRIPTS_11_13.md` — reprodukovateľná numerika pozadia;
- `Questions/00_AKCNY_PLAN_v3.18_AKTUALNY_2026-07-13.md` — rozpis A2/A3/A8;
- `theory/SK/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_SK.md` — stav Q19/Q20 v hlavnom registri pravidiel a otázok.

