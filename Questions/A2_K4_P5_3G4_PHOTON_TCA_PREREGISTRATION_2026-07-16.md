# A2-K4/P5.3g4 — predregistrácia fotónového `l=2` a TCA seedu

**Route:** `A1-K1 / A2-K4 / P5 / P5.3g4`  
**Skóre:** žiadna zmena; P5.3 je stále `REVIEW`, A2-K4 zostáva `60/100`.  
**Skript:** `255_script_KMPC_018_P5_3g4_photon_l2_tca_seed.py`  
**Vnútorný limit:** 5 s. **Vonkajší limit:** 10 s. **Bez ODE.**

## Čo sa počíta ľudskou rečou

Fotón a baryón sú v ranej horúcej plazme tak tesne spojené, že fotón nemá
voľný quadrupól ani polarizáciu v nulovom limite voľnej dráhy. Prvý nenulový
quadrupól má vzniknúť iba ako malá oprava úmerná `epsilon_TCA=1/opacity`.
Overujeme presnú algebraickú povinnosť tohto tvrdenia z už auditovaného CAMB
collision bloku a z fotónovej rýchlosti `q_g` v seede 84.

## Vstupy a proveniencia

1. collision matrix `[J_gamma2,E_gamma0,E_gamma2]` zo skriptu 73,
   dokumentovane odvodená z Ma–Bertschinger/CAMB;
2. fotónová hierarchia a `polter` konvencia zo skriptu 76;
3. štandardné regularné `q_g` pre AD/CDI/BI/NID/NIV zo skriptu 84.

Žiadny K7 background, `K_MPC=0.05`, nový parameter, opacity fit ani
numerický integrátor sa nepoužije.

## Očakávaný výsledok

Pri `epsilon_TCA -> 0` má mať collision blok len nulové riešenie
`(J_gamma2,E_gamma0,E_gamma2)=0`. Pri prvom ráde má lineárny systém dať
jeden jednoznačný vektor úmerný známemu voľno-streamingovému drive z `q_g`
a metrického shear. Musí platiť:

- presné rezíduum collision rovníc je nula;
- každý multipól je `O(epsilon_TCA)` a preto mizne v TCA limite;
- žiadna divergence ani nový fitovaný koeficient nevznikne;
- výsledok sa označí iba ako **algebraický seed coefficient**, nie ako plný
  K4 seed.

## PASS / STOP / následok

| Stav | Význam | Ďalší krok |
|---|---|---|
| algebraický PASS | collision blok a prvý TCA koeficient sú jednoznačné | P5.3g5: nezávislý Einsteinov ledger; stále chýba K4 opacity a dvojštart |
| fyzikálny STOP | blok nemá regulárne riešenie alebo potrebuje voľný koeficient | P5.3 končí REVIEW/STOP s presným algebraickým dôvodom |
| technický STOP | timeout, import, parser, chýbajúci zdroj | `REVIEW_BLOCKED`; bez zmeny fyziky alebo skóre |

**Dôležitá hranica:** štandardná recombination referencia môže ukázať, že
opacity existuje v nulovej fyzike, ale nenahrádza odvodenie `opacity_K4`.
Ak po algebraickom PASS ostane jeho časová závislosť neurčená, P5.3g4 je
iba čiastkový PASS a P5.4 sa neotvorí.

