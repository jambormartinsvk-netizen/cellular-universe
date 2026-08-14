# A2-K4 / C7.7c-K7a — odvodenie projektovaných zdrojov D a M

**Dátum:** 2026-07-14  
**Stav:** analytické odvodenie pred Jacobianovým testom; bez ODE evolúcie  
**Skóre:** bez zmeny, `66.5/100`

## 1. Definície a stavová báza

Backgroundový menovateľ zo skriptu 136 označujeme `B`, aby sa nezamieňal s projektovanou hustotou.

Projektované zdroje sú

`D = Omega_gamma delta_gamma + Omega_fs delta_fs + Omega_b delta_b + Omega_c delta_c + Omega_f delta_f`,

`M = (2 Omega_gamma + 3 Omega_b/2) U_gamma + 2 Omega_fs U_fs + (3 delta Omega_f/2) U_f`.

V novej báze sa `delta_fs,U_fs` nahradia `D,M`:

`z=(h,eta,delta_gamma,D,delta_b,delta_c,U_gamma,M,sigma_fs,L3_fs,L4_fs,delta_f,U_f)`.

Rekonštrukcia je

`delta_fs = (D-Omega_gamma delta_gamma-Omega_b delta_b-Omega_c delta_c-Omega_f delta_f)/Omega_fs`,

`U_fs = (M-W_gamma U_gamma-W_f U_f)/(2 Omega_fs)`,

kde

`W_gamma=2 Omega_gamma+3 Omega_b/2`, `W_f=3 delta Omega_f/2`.

Transformácia je invertibilná iba pre `Omega_fs != 0`; táto podmienka musí byť samostatnou bránou.

## 2. Backgroundové derivácie

Nech

`ell = B'/B = 2(q+1)`.

Potom

- `Omega_gamma'=-ell Omega_gamma`;
- `Omega_fs'=-ell Omega_fs`;
- `Omega_b'=(1-ell)Omega_b`;
- `Omega_c'=(beta_c-ell)Omega_c`;
- `Omega_f'=(beta_f-ell)Omega_f`.

Pri `g=g2 z^2`:

`beta_f = p - g/(1-g/2)`.

Ak `C_c=fc mu z + g2 z^(p+2)/(p+1)`, potom

`beta_c = [fc mu z + (p+2)g2 z^(p+2)/(p+1)]/C_c`.

Pomocné derivácie: `g'=2g`, `gr'=(p+1)gr`, `(s^2)'=-2q s^2` a `loading'=loading`.

## 3. Projektovaná rovnica D'

Definujme

`A_h = (2/3)(Omega_gamma+Omega_fs) + (1/2)(Omega_b+Omega_c) + (delta/2)Omega_f`.

Pri použití `h'=3D+2s^2 eta` a presnej rekonštrukcie `delta_fs` sa všetky vedúce radiačné kompenzačné členy zrušia algebraicky. Výsledok je

```text
D' = -ell D
     + Omega_b delta_b
     + beta_c Omega_c delta_c
     + beta_f Omega_f delta_f
     - (2/3)s^2 M
     - A_h(3D+2s^2 eta)
     + Omega_c gr(delta_f-delta_c)
     + Omega_f[-3(2-delta)delta_f
               -9 delta(2-delta)U_f
               -3(2-delta)g U_f].
```

Rovnica už nevytvára `D` odčítaním `Omega_gamma delta_gamma` a `Omega_fs delta_fs`.

## 4. Projektovaná rovnica M'

Nech `r_L=loading/(1+loading)` a `r_I=1/(1+loading)`. Po derivovaní časovo závislých váh, použití Eulerových rovníc a rekonštrukcii `delta_fs,U_fs` vyjde

```text
M' = (-q-2)M + (1/2)D
     + [(3/2)Omega_b-W_gamma r_L]U_gamma
     + [(1/4)W_gamma r_I-(1/2)Omega_gamma]delta_gamma
     - (1/2)Omega_b delta_b
     - (1/2)Omega_c delta_c
     + Omega_f delta_f
     - 2 Omega_fs sigma_fs
     + [(3/2)delta Omega_f(beta_f+2)+3 Omega_f g]U_f.
```

Táto forma nevytvára `M` priamym odčítaním veľkých fotónových a free-streaming momentov.

## 5. Ostatné rovnice v projektovanej báze

- `h'=3D+2s^2 eta`;
- `eta'=M`;
- `delta_gamma'=-(4/3)s^2 U_gamma-(2/3)h'`;
- `delta_b'=-s^2 U_gamma-h'/2`;
- `delta_c'=-h'/2+gr(delta_f-delta_c)`;
- Eulerova rovnica `U_gamma`, rovnice `L3,L4,delta_f,U_f` ostávajú fyzikálne nezmenené;
- `sigma_fs'` používa rekonštruované `U_fs` a `eta'=M`.

Rovnice pre pôvodné `delta_fs,U_fs` sa nemenia na fyzikálne tvrdenia; v projektovanej báze sa používajú ako nezávislý consistency ledger rekonštrukcie.

## 6. Povinný Jacobianový člen

Pôvodná lineárna sústava je `y'=A_y(x)y` a `z=T(x)y`. Preto

`z'=[T' T^-1 + T A_y T^-1]z = (T'+T A_y)T^-1 z`.

Vynechanie `T'T^-1` by zahodilo derivácie `Omega_A`, zmenilo rovnice `D',M'` a mohlo vytvoriť falošný spektrálny alebo stabilitný výsledok.

Zmrazená časť `T A_y T^-1` musí mať rovnaké spektrum ako `A_y`. Úplný projected Jacobian vo všeobecnosti nemusí mať rovnaké okamžité vlastné čísla, pretože časovo závislá zmena súradníc pridáva connection člen `T'T^-1`.

## 7. Radiačný nulový limit

Pre `Omega_b=Omega_c=Omega_f=loading=g=gr=0`, `Omega_gamma+Omega_fs=1`, `q=-1`, `ell=0`:

```text
D' = -2D -(4/3)s^2 eta -(2/3)s^2 M,
M' = -M +(1/2)D -2 Omega_fs sigma_fs.
```

Navyše `h'=3D+2s^2 eta`, `eta'=M`. Tento limit je predregistrovaná znamienková brána.

## 8. Otvorený stav

Odvodenie ešte nie je PASS K7a. Pred evolúciou sa musí strojovo overiť:

1. analytická `T'` proti FD backgroundu;
2. explicitný projected Jacobian proti `(T'+TA)T^-1`;
3. invertibilita a condition transformácie;
4. nulový limit a všetky znamienka;
5. numerical conditioning na deep aj shallow pre NID/NIV.

