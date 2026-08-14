# A2.1 — reprodukčný manifest a uzavretie stavu

**Dátum:** 2026-07-13  
**Koľaj:** A2-K1  
**Konečný stav:** `MŔTVA — ARCHIVOVANÁ`  
**Register mŕtvych koľají:** M-009

## 1. Rozsah verdiktu

Verdikt platí pre uzáveru

```text
Q_f^mu = -Gamma rho_f u_c^mu,
Q_c^mu = +Gamma rho_f u_c^mu,
Gamma = lambda H0 > 0,
lambda = 0.15,
w_f = -1 + delta,
delta = 0.02297,
c_s,f^2 = 1.
```

A2-K1 je mŕtva pre nekontrolovaný gauge-invariantný superhorizontový relatívny rýchlostný mód. Verdikt nezabíja background A1-K1 ani nevyskúšané A2-K3 až A2-K5.

## 2. Overené výsledky

- `Gamma/[H0(1+w_f)] = lambda/delta = 6.530256856769699`;
- `H0 Delta t(z_star -> 0) = 0.9351169230555114`;
- exponent rastu `2(lambda/delta)H0 Delta t = 12.213107397329273`;
- zosilnenie `exp(exponent) = 201411.91075800857`;
- relatívny rozdiel exponentu medzi krokmi `5e-4` a `2.5e-4` je `9.189536296867442e-9`;
- predregistrovaná konvergenčná brána `1e-8` prešla;
- algebraické kontroly znamienok, nulových limitov a backgroundovej bilancie: `8/8 PASS`.

## 3. Dodatočná kontrola tlakovej poruchy

Primárny vzťah Valiviita–Majerotto–Maartens, rovnica (29), má v ich konvencii člen

```text
(c_s,A^2-c_a,A^2)[3 mathcal H(1+w_A)rho_A-a Q_A] theta_A/k^2.
```

Pre naše `Q_f=-Gamma rho_f` preto vznikne

```text
delta p_f = delta rho_f
  +(1-w_f)[3 mathcal H(1+w_f)+a Gamma]
   rho_f theta_f/k^2.
```

Znamienko `+a Gamma` v hlavnom odvodení A2.1 je potvrdené; erratum nie je potrebné.

## 4. Vykonané reprodukčné kontroly

### Skript 23

- Python kompilácia: `PASS`;
- návratový kód: `0`;
- všetky tri kill checks: `true`;
- výstupný verdikt: `MRTVA_A2_K1`.

### Skript 24

- Python kompilácia: `PASS`;
- návratový kód: `0`;
- všetkých osem symbolických kontrol: `true`;
- výstupný stav: `PASS`.

Skript 22 sa zachováva ako prvý konvergenčne neuzavretý beh. Jeho návratový kód 1 a dôvod sú zdokumentované v `scripts/ERRATUM_22_23_A2_K1_SUPERHORIZON.md`; nesmie sa mazať ani ticho prepisovať.

## 5. SHA-256 artefaktov

| Súbor | SHA-256 |
|---|---|
| `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py` | `7FB9E3BF82ABE1A1985E426AA37F00B40329EEA9781B4334B20359A99898BA6E` |
| `scripts/22_script_A2_K1_superhorizon_velocity_instability.py` | `717C81D4A77B9D88759E65D9AE3CB44AAE625142BFF167D4EED9923EBDE7FAB2` |
| `scripts/23_script_A2_K1_superhorizon_velocity_instability_converged.py` | `6AD94F01C7FCDDFB0C4481AC2003EEA0202481DB484C28572215287E92535FC6` |
| `scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py` | `2D95E4DFB7FDCAB632B22C1080B3AE9BEF1A487B2B2720E92CEC7EEACEAC7FCE` |
| `scripts/ERRATUM_22_23_A2_K1_SUPERHORIZON.md` | `31CE6268EC5A8F396EEC2D733A8FFC2B9B04EE809505AB6C4EC91CEFC8865AF3` |
| `scripts/README_AUDIT_SCRIPTS_22-24.md` | `41636E00B0574D6DCE242E48BA7334F0D21F1FF0658D5EF5F14270EF58419AE2` |
| `Audit/A2_1_linearne_perturbacie_Einsteinove_constrainty_a_superhorizontovy_test.md` | `33E00A58D79B8004E772C5A3C8CCCBE70B0D29A96F4FC3A0DE3ACC8F21F7BB87` |
| `Audit/A2_K1_MRTVA_superhorizontova_rychlostna_nestabilita.md` | `B276313AF17A71104B8B9775713ECF1A02E2FF375E5BEB3B1923B68164603773` |
| `Audit/ERRATUM_A2_00_PO_TESTE_A2_1.md` | `2A3E0209FF573B2252A409143AE28BC3AE76C2749B27E851971820FCE8BE1947` |
| `Audit/ADDENDUM_REGISTER_MRTVYCH_KOLAJI_A2_M009.md` | `01FDF3736290201FE5847ECE72ADCC72E49BEF463572D06447D913559D7990FE` |
| `Audit/00_READ_FIRST_A2.md` | `1D0C54A3E6C7A4CB710667B4EA949BF354398705731578F62ED982078A358AAC` |
| `Questions/A2_1_STAV_PO_SUPERHORIZONTOVOM_TESTE.md` | `F52BD5F6A43E6EFD0B25443D49813F788CE64B297DD859BD5D02AD70BBD96598` |
| `theory/SK/05e_Methodology_Rules_and_Question_Register_A2_1_SK.md` | `24F519CCBBEFD5B4A871AB2FEC760239A177F5E074A8AF64DB5C47BBAAFFFBD5` |
| `theory/EN/05e_Methodology_Rules_and_Question_Register_A2_1_EN.md` | `B4E0E51DA21F6628CC39364CFE2F852A9A33C56A650C2D96A9902A92D8E3514C` |

Hash tohto manifestu nie je uvedený v ňom samom. Pri balení verzie sa má dopočítať v nadradenom release manifeste.

## 6. Ďalší krok

Aktívnou koľajou sa stáva A2-K3: `Q^mu` rovnobežné s `u_f^mu`, pri `c_s,f^2=1`. Musí dostať vlastné odvodenie kontinuít a Eulerových rovníc, znamienkový a nulový test a samostatný superhorizontový eigenmód. Predbežné varovanie z literatúry nie je verdikt.

