# Program auditu prenosu formulácie do výpočtov

**Spustené:** 2026-07-15  
**Pravidlo:** AR8 v SK/EN registri.  
**Stav:** `L0b inventár + L1 + L2-B1/B2/B2.1 PASS v deklarovanom scope; P5.2 constraint ledger OTVORENÝ.`

## Otázka

Dostal sa každý povinný prvok rodičovskej fyzikálnej formulácie do nižších
skriptov, alebo sa po ceste zmenil či vypustil bez označenia?

## Kontrakt, ktorý sa teraz kontroluje

| ID | Povinný prvok A1 → A2-K4/P5 |
|---|---|
| C1 | `Q_f^mu=-Gamma rho_f u_d^mu`, `Q_c^mu=+Gamma rho_f u_d^mu` a energy-frame `u_d` |
| C2 | `Gamma=lambda H0`, presný pomer `gamma=Gamma/H=lambda/E(a)` |
| C3 | plný k‑nezávislý A1 background `X_i(a), D_A1(a)` |
| C4 | dynamické `U_c`, samostatné `U_b`, úplná hybnosť v `0i` constrain­te |
| C5 | Fourierov mód iba v poruchových gradientoch/horizonte, nie v backgrounde |
| C6 | `00`, `0i`, slip a trace constrainty plus `Gamma->0` limit |

## Rozsah L0–L3

1. **L0 — inventár a kontrakt:** rodičovské zdroje a potomkovia; bez
   fyzikálneho verdiktu.
2. **L1 — statický source audit:** prítomnosť C1–C5 v zdroji a deklarovaný
   rozsah každého skriptu.
3. **L2 — equation audit:** porovnanie koeficientov, znamienok a stavov s
   rodičovskými rovnicami; nesúlad = STOP konkrétnej implementácie.
4. **L3 — rerun audit:** iba pre implementácie, ktoré po L2 prežijú;
   reprodukovať relevantné testy s limitmi a immutable výstupmi.

## Prvé cieľové skupiny

| Skupina | Artefakty | Predbežný stav |
|---|---|---|
| A1 canonical | 11, 234, 235 | zdroj pre C2/C3; P2a/P3 už auditované |
| K4 species | 86 a ledger A2-K4.3b-RG | obsahuje `U_c`; treba overiť C1/C2/C6 |
| K7 legacy | 146, 159, 197, 199, 209, 213 | známy C3/C4 STOP; históriu zachovať |
| G8 screens | 221/233 a `baseScripts/a2_k4_g8` | screen scope, nie plný K4; musí sa označiť C4-limit |
| P5 successor | 236 a budúce P5.2+ | musí prejsť C1–C6 pred ODE |

## Dosiahnutý výsledok L1

`02_L1_STATIC_SOURCE_AUDIT_RESULT_SK.md` potvrdzuje očakávané obmedzenia
K7/G8 a zachovanie `U_c` v 86/P5. `03_L0B_DEPENDENCY_INVENTORY_SK.md`
rozdeľuje celý relevantný corpus do piatich balíkov. `05_L2_B1_PROJECTED_K7_RESULT_SK.md`
uzatvára projektovaný K7 lineage ako fyzikálne obmedzený. `07_L2_B2_GENERAL_SYNCHRONOUS_RESULT_SK.md`
našiel kandidátov 89/90 s `U_c`,`U_d` a constraintmi. `09_L2_B2_1_BR2_EQUATION_RESULT_SK.md`
overil ich skoré interaction jadro; aktívny je P5.2 constraint ledger.
Pred ďalšou ODE P5 sa nesmie vynechať.

## Rozhodnutia

- Nedostatok v historickom skripte neprepisuje jeho JSON ani hash.
- Skript dostane stav `HISTORICKÝ / FYZIKÁLNE OBMEDZENÝ`, `TECHNICKY
  NEVYKONÁVAŤ` alebo `AKTUÁLNY`, vždy s dôvodom.
- Až po L2 sa rozhodne, ktoré staršie výpočty treba zopakovať; nič sa
  neprepočítava iba preto, že existuje novší skript.
- L0/L1/L2 sú ohraničené audity; nesmú sa rozrásť na nečíslované suffixy.
