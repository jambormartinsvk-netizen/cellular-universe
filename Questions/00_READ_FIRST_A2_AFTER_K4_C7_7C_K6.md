# READ FIRST — A2 po audite K4/C7.7c-K6

**Aktívny stav:** `A2-K4 ŽIVÁ, 66.5/100, C7.7c otvorená.`

## Mŕtve numerické podkoľaje, ktoré sa nesmú opakovať

- K1: uniformné `atol` nerozlíšilo 28 activity položiek;
- K2: normalizácia podľa počiatočného stavu timeoutovala;
- K3: Radau na extrémne škálovanom stave timeoutoval/chyboval;
- K4: analytická obálka vytvorila nenormálny Jacobian až `4.19×10^14`;
- K5: úplné diagonálne vyváženie timeoutovalo a zmenilo error metriku;
- K6: vektor `atol_i=10^-12 S_env,i` vyžadoval až `10^-36` v double RHS.

## Nový príčinný dôkaz

NID celková hustota a `h_x` majú na deep aj shallow povrchu signal/roundoff pomer pod `0.2`. NIV je v týchto zdrojoch rozlíšiteľná s rezervou `10^6–10^7`.

## Jediný povolený ďalší krok

`C7.7c-K7a`: analyticky odvodiť projektované kompenzované gravitačné zdroje `D` a `M`. Zatiaľ nespúšťať ODE evolúciu a nepridávať body.

## Autoritatívne nové dokumenty

- `Audit/A2_K4_C7_7C_K5_K6_CORRECTION_AND_DEATH_AUDIT_2026-07-14.md`;
- `Audit/A2_K4_C7_7C_INITIAL_RHS_CONDITION_MAP_AUDIT_2026-07-14.md`;
- `Questions/A2_K4_C7_7C_K7_PROJECTED_COMPENSATED_BASIS_PREREGISTRATION.md`;
- `Questions/00_AKCNY_PLAN_v3.18_ADDENDUM_AFTER_K4_C7_7C_K6.md`.
