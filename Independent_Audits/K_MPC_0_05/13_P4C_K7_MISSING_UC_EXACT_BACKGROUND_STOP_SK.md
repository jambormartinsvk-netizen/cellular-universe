# K-N2/P4c — STOP: K7 projektovaná báza nemá dynamickú rýchlosť popola

**Rozsudok:** `STOP pre exact-A1 K7 adapter a G8 na súčasnej 13-zložkovej báze.`  
**Nie je to rozsudok smrti A2-K4 mechanizmu.** Je to dôkaz, že K7 výsledky
nemôžu byť bez ďalšej odvoden ej bázy vyhlásené za evolúciu deklarovaného
energy-frame K4 operátora pri nenulovej relatívnej rýchlosti.

## Dôkaz po porovnaní dvoch existujúcich autorít

General-synchronous K4 test-field ledger v
`Audit/A2_K4_3B_RG_REGULAR_SEEDS_PUISEUX_AND_SYNCHRONOUS_TEST_FIELD_AUDIT.md`
má explicitne dynamické premenné `U_c` a `U_f`:

```text
delta_c,x = -s2 U_c - h_x/2 + (lambda/E) r (delta_f-delta_c),
U_c,x     = -(1-h_c)U_c + (lambda/E) r beta_d (U_f-U_c),
U_f,x     = (h_c+2)U_f + delta_f/delta
            + (lambda/(E delta))(2U_f-U_d),
U_d       = (1-beta_d)U_c+beta_d U_f.
```

Naopak autoritatívny K7d runner 213 používa 13-zložkový stav bez `U_c`:

```text
(h,eta,delta_gamma,D,delta_b,delta_c,U_gamma,M,
 sigma_fs,L3_fs,L4_fs,delta_f,U_f).
```

V jeho `physical_rhs()` sú príslušné riadky

```text
delta_c,x = -h_x/2 + gr(delta_f-delta_c),
U_f,x     = (q+2)U_f + delta_f/delta + 2g U_f/delta.
```

Nie je v nich `-s2 U_c` ani `-(gamma/delta)U_d`; `M` ich nemôže skrývať,
pretože jeho definícia neobsahuje CDM/popolovú hybnosť. Tieto K7 riadky sa
zhodujú s redukciou `U_c=0` a `U_d=0`.

## Prečo nejde o prípustnú gauge voľbu K4

Pre K4 platí

```text
U_d=(1-beta_d)U_c+beta_d U_f,
beta_d=delta X_f/(X_c+delta X_f).
```

Ak je `beta_d>0` a existuje fyzikálny relatívny mód `U_f-U_c`, nemožno mať
zároveň `U_c=0`, `U_d=0` a `U_f!=0`. Navyše CDM Eulerova rovnica obsahuje
nenulové momentum-transfer zrýchlenie úmerné
`gamma r beta_d(U_f-U_c)`. Synchronous gauge môže mať nulový lapse, ale pri
negeodetickom CDM sa nesmie súčasne potichu vyhlásiť za CDM-comoving.

V ranej hranici `beta_d -> 0` je redukcia asymptoticky menej viditeľná, čo
vysvetľuje prečo skoré regularity a constraint testy K7 mohli prejsť. To
však nie je dôkaz platnosti pri konečnom čase, kde G8 a G9 potrebujú plný
operátor.

## Rozsah dôsledku

| Artefakt | Nový status | Prečo |
|---|---|---|
| K7d G4–G7 numerické testy | zachovať, ale **nie sú fyzikálnou podporou K4** | testovali konzistenciu redukovanej 13-zložkovej RHS |
| G8 na K7 13-zložkovej báze | **STOP / nesmie sa spustiť** | chýba nutný dynamický stupeň voľnosti |
| A2-K4 `Q^mu=Gamma rho_f u_d^mu` | **ŽIVÁ, neuzavretá** | species-level K4 rovnice existujú; treba novú plnú bázu |
| A1-K1 background | **bez zmeny** | tento stop je v perturbatívnej reprezentácii |

## Povinný nástupca, nie patch

Nástupca musí mať general-synchronous (alebo plne gauge-invariantnú) bázu s
`U_c` ako nezávislou dynamickou premennou, plnou hybnosťou popola v
Einsteinovom `0i` constrain te, exact-A1 koeficientmi a novými regular-mode
seedmi. To je matematicky iný stavový priestor; nemožno opraviť 213 výmenou
jedného koeficientu ani pripísať `U_c=0` ako constraint.

Pred ODE musí nástupca prejsť: species-to-projected algebra, `T_x` ledger,
štyri Einsteinove constrainty, `Gamma->0` limit a regularitu. Až potom sa
smie začať nová G8 hierarchia. Staré K7 skripty, JSON a výsledky ostávajú
nemenné pre spätný audit.
