# K-N2/P4b2b — exact-A1 transformácia do projektovanej K7 bázy

**Stav:** `PASS pre transformáciu a jej connection člen; species RHS v
synchronnej gauge ostáva otvorené v P4c.`

## Čo sa nemení

K7 nemení fyzikálne druhy; iba nahrádza kompenzované neutrínové premenné
projektovanými zdrojmi. Nech species báza je

```text
y=(h,eta,delta_gamma,delta_nu,delta_b,delta_c,
   U_gamma,U_nu,sigma_nu,L3,L4,delta_f,U_f),
```

a projektovaná báza je

```text
z=(h,eta,delta_gamma,D,delta_b,delta_c,
   U_gamma,M,sigma_nu,L3,L4,delta_f,U_f).
```

Definície, teraz s presnými A1 podielmi, sú

```text
D = Og delta_gamma + On delta_nu + Ob delta_b + Oc delta_c + Of delta_f,
M = Wg U_gamma + 2 On U_nu + Wf U_f,
Wg=2 Og+3 Ob/2,   Wf=3 delta Of/2.
```

Ak `On>0`, rekonštrukcia `delta_nu,U_nu` je jednoznačná. To je rovnaká
invertibilitná podmienka ako v K7a; P3 nezaviedla žiadny nový druh ani
neodstránila neutrína.

## Exact-A1 derivácie váh

Z P4b1 platí:

```text
Og,x = -ell Og,       On,x = -ell On,
Ob,x = (1-ell) Ob,
Oc,x = (beta_c-ell) Oc,
Of,x = (beta_f-ell) Of,

beta_c=1+gamma Xf/Xc,
beta_f=p-gamma,
ell=(4-3delta)Of+Ob+Oc.
```

Preto

```text
Wg,x = 2 Og,x + 3 Ob,x/2,
Wf,x = 3 delta Of,x/2.
```

Sú to všetky časovo závislé koeficienty transformácie `T(x)`.
Neobsahujú perturbatívny mód `k`.

## Povinný connection člen

Ak species systém má tvar `y_x=A_y(x)y`, potom presne, bez aproximácie,

```text
z_x = [T_x T^(-1) + T A_y T^(-1)] z.
```

Člen `T_x T^(-1)` je povinný. Bez neho by sa vynechali derivácie exact-A1
hustotných podielov a vznikol by iný systém. Toto je tá istá matematická
nutnosť, ktorú audit K7a už správne kontroloval; menia sa len hodnoty
`Og,...,Of`, `beta_c`, `beta_f`, `ell`.

## Čo z toho plynie pre skoré D a M rovnice

Po dosadení exact-A1 váh má projektovaná hustotná rovnica rovnakú
transformačnú štruktúru ako historická K7a:

```text
D_x = -ell D + Ob delta_b + beta_c Oc delta_c + beta_f Of delta_f
      -(2/3)s2 M - A_h(3D+2s2 eta) + [interaction and fuel species terms],
A_h=(2/3)(Og+On)+(Ob+Oc)/2+delta Of/2.
```

Toto je algebraický dôsledok `T_x`, nie ďalší modelový predpoklad. Výrazy v
hranatých zátvorkách však musia prísť zo synchronných species rovníc
odvodených z K4 `Q^mu`; nemožno ich potichu prebrať z 213 len nahradením
`g -> gamma`.

## Rozsudok a hranica

**Transformácia PREŠLA.** Je invertibilná za rovnakej neutrínovej podmienky
a exact-A1 `T_x` je úplne určená. **Ešte neprešla fyzikálna RHS.**

P4c musí preto najprv nezávisle odvodiť synchronné `delta_c,delta_f,U_f`
rovnice z rovníc P4b2a a gauge transformácie. Až následne sa môže strojovo
porovnať explicitný exact-A1 projected RHS s `(T_x+T A_y)T^(-1)` a s
Einsteinovými constraintmi. Nový ODE runner pred týmto krokom by bol
neoverený patch.
