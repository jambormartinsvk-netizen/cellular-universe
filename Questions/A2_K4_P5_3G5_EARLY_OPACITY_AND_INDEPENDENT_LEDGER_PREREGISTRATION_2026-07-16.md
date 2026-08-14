# A2-K4/P5.3g5 — predregistrácia skorého opacity seedu a nezávislého ledgeru

**Route:** `A1-K1 / A2-K4 / P5 / P5.3g5`  
**Skóre:** bez zmeny; A2-K4 zostáva `60/100`.  
**Plánovaný runner:** `256_script_KMPC_019_P5_3g5_early_opacity_and_einstein_ledger.py`  
**Vnútorný limit:** 5 s. **Vonkajší limit:** 10 s. **Bez ODE.**

## Čo sa overuje ľudskou rečou

V dostatočne ranej, plne ionizovanej plazme je Thomsonova opacity určená
štandardnou fyzikou, nie novým K4 parametrom:

```text
dot(kappa) = a n_e sigma_T,
n_e = x_e rho_b/m_p,   x_e -> 1,   rho_b propto a^(-3).
```

Z toho musí vyplynúť `dot(kappa) propto a^(-2)`, `tau_c propto a^2` a v
radiačnom limite `Hconf tau_c propto a -> 0`. Tento výsledok dáva chýbajúci
skorý časový rád pre P5.3g4, ale nenahrádza rekombinačnú históriu.

Súčasne sa z nezávisle zapísaných `00` a `0i` synchronous Einsteinových
constraintov overí, že do zdroja vstupujú samostatné hybnosti `U_c`, `U_b`,
`U_f` a radiačné entalpie. Ide o ledger povinných členov, nie o deklaratívne
opakovanie P5.2 a nie o dynamickú reziduálnu skúšku konkrétneho seedu.

## Vstupy a hranice

- exact-A1 background je k-nezávislý (`Independent_Audits/K_MPC_0_05/09...`);
- K-N2/P2a určil `A_f` zo zmrazeného A1 closure bez nového fitu;
- štandardné atómové sadzby a `sigma_T` sa nemenia, ale úplná `x_e(a)` na
  K4 backgrounde patrí až rekombinačnému backendu;
- nesmú sa použiť K7/213, pevné `K_MPC=0.05`, opacity fit, ODE ani G8 skóre.

## Očakávanie

PASS vyžaduje presnú mocninovú identitu `dot(kappa) a^2 = const`, nulový
limit `Hconf tau_c -> 0` pri `a -> 0` a explicitnú prítomnosť `U_c`, `U_b`,
`U_f` v nezávislom zdrojovom ledgeri. Výsledok bude iba
`FORMULA_PASS_EARLY_OPACITY_AND_LEDGER_SCOPE`.

STOP nastane pri nesprávnom znamienku/mocnine, pri chýbajúcej hybnosti alebo
ak by bol potrebný nový voľný koeficient. Technický timeout je
`REVIEW_BLOCKED`, bez zmeny fyziky.

## Čo nasleduje

Aj pri PASS zostanú otvorené: plná rekombinačná `x_e(a)` na exact-A1
backgrounde, konkrétne regular-mode Einsteinove rezíduá a full photon+
neutrino seed na dvoch štartoch. P5.4 a G8 sa tým neotvoria.
