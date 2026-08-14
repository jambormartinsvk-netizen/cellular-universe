# P5.1 — výsledok statického exact-A1 general-synchronous ledgera

**Dátum:** 2026-07-15  
**Skript:** `scripts/236_script_KMPC_003_P5_1_general_synchronous_static_ledger.py`  
**Immutable výsledok:** `scripts/results/k_mpc_005/RUN_KMPC_003_P5_1_GENERAL_SYNCHRONOUS_STATIC_LEDGER.json`  
**Limity:** vnútorný 5 s, vonkajší 10 s; reálny čas `0.188 s`.

## Rozsudok

**PASS-P5.1.** Všetkých deväť predregistrovaných algebraických kontrol
prešlo; šesť symbolických rezíduí je presne `0`.

Prešla najmä:

- párová bilancia transferu palivo ↔ popol;
- exact-A1 odvodenia `ell`, `beta_c` a `beta_f`;
- energy-frame definícia `U_d` s dynamickým `U_c`;
- radiačný limit `gamma=lambda/E -> lambda a^2/sqrt(Omega_r0)`;
- zákaz `k` v backgroundových koeficientoch a jeho prítomnosť iba v
  `s2=k^2/Hconf^2`;
- obsah `U_c` aj `U_b` v plnom hybnostnom zdroji.

## Význam a hranica

P5.1 dokazuje, že nástupca K7 možno postaviť bez nového parametra a bez
zmeny A2-K4 mechanizmu. Nedokazuje ešte Einsteinove constrainty, regulárne
počiatočné módy, stabilitu ani G8. Skóre A2-K4 sa preto nemení a G8 ostáva
blokované.

## Ďalší krok

**P5.2:** staticky odvodiť `00`, `0i`, slip a trace constrainty s úplnou
hybnosťou, pred každou ODE. Ak nebude možné získať uzavretý constraint
ledger, P5 končí pred solverom a A2-K4 sa presunie na záložné fyzikálne
koľaje.
