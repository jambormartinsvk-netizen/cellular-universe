# K11-CS1 — výsledok úplného constrained superhorizontového symbolu

**Dátum:** 2026-07-16  
**Autorita verdiktu:** hlavný orchestrátor  
**Predregistrácia:**
`K11_CS1_FULL_CONSTRAINED_SUPERHORIZON_SYMBOL_PREREGISTRATION.md`  
**Výsledok:** `UNDETERMINED_REVIEW / FULL MULTISPECIES DAE REQUIRED`  
**Čiastkový výsledok:** `PASS_EARLY_INDICIAL_NULL_LIMIT`  
**Skórovací účinok:** žiadny; K11 zostáva `10/100 = G1`  
**Numerický beh:** žiadny

## 1. Stručný rozsudok

Úplný fyzický K11 superhorizontový symbol nemožno korektne zredukovať na
päť dark premenných na reálnom A1 backgrounde. Einsteinove constrainty a
metric slip obsahujú baryóny, fotóny, neutrína, paru a scaled anisotropic
stress. Bez nich dark-only matica nie je úplný constrained systém.

Analytika však uzavrela tri dôležité body:

1. konečný `k->0` dark blok a jeho pressure term boli presne odvodené;
2. skorý radiačný Frobeniov indiciálny symbol je pri finite proper-time
   `Gamma,gamma_*` presne štandardný `Gamma=Upsilon=0` GR symbol;
3. interaction-only K1+K11 velocity blok zostáva exact saddle a nemôže byť
   samostatným liekom.

Fixed-`delta=0.02297` stabilita od rekombinácie po dnešok zostáva
nerozhodnutá, pretože ide o časovo závislú constrained viacdruhovú DAE, nie
o jednu konštantnú charakteristickú maticu.

## 2. Bezrozmerné premenné

Použime

```text
N       = ln a,
epsilon = k/mathcal H,
W_A     = mathcal H V_A,
s       = d ln mathcal H/dN,
g       = Gamma/H,
r       = rho_f/rho_c,
d_c     = Upsilon/(H rho_c),
d_f     = Upsilon/(H delta rho_f).
```

`V_A=theta_A/k^2` sa zavádza pri konečnom `k` a až potom sa berie
`epsilon->0`. Presné homogénne `k=0` nesmie byť zamenené s limitom
regulárneho perturbatívneho módu.

## 3. Konečný dark-sector systém

Z akceptovaných K1 rovníc a pasívneho K11 dragu vyplýva

```text
delta_c,N
= -epsilon^2 W_c + 3Phi_N
  + g r(delta_f-delta_c+Psi),

delta_f,N
= -3(1-w_f)delta_f
  -delta epsilon^2 W_f
  -[9(1-w_f^2)+3g(1-w_f)]W_f
  +3delta Phi_N-gPsi,

W_c,N
= (s-1)W_c+Psi+d_c(W_f-W_c),

W_f,N
= (s+2)W_f+delta_f/delta+Psi
  +(g/delta)(2W_f-W_c)+d_f(W_c-W_f).
```

Palivový tlakový prevod, ktorý sa nesmie skrátiť, je

```text
delta p_f/rho_f
= delta_f
  +(2-delta)[3mathcal H delta+aGamma]V_f.
```

Drag na lineárnom ráde nemení continuity ani tento tlakový prevod; vstupuje
iba do Eulerových momentum riadkov.

## 4. Constraintová plocha

Po vydelení `0i` rovnice `k^2` a až potom limite:

```text
Phi_N+Psi
= (3/2) sum_A Omega_A(1+w_A)W_A.
```

`00` constraint je

```text
sum_A Omega_A delta_A
+3 sum_A Omega_A(1+w_A)W_A
+(2/3)epsilon^2 Phi
=0.
```

Pri `epsilon->0` teda

```text
delta rho_total+3mathcal H Pi_total=0.
```

To nie je dark-only vzťah: oba súčty obsahujú všetky prítomné species.
Traceless constraint navyše obsahuje scaled free-streaming shear a určuje
`Phi-Psi`.

Správna DAE architektúra je:

- `0i` alebo ekvivalentná nezávislá metrická rovnica evolvuje potenciál;
- `00` sa uloží na počiatočné dáta a zostane holdout/propagation residual;
- trace a traceless rovnice kontrolujú pressure a slip;
- CDM continuity sa po prípadnej algebraickej eliminácii `delta_c` použije
  ako Bianchi/propagation check, nie tautologický PASS.

## 5. Prečo päťstavový dark-only symbol nie je úplný

Pri umelom zero-shear dark-only truncation možno použiť

```text
(delta_c,delta_f,W_c,W_f,Phi),  Psi=Phi,
```

a eliminovať jednu hustotu cez `00`. Táto redukcia však na reálnom
radiačno-hmotovom backgrounde nie je dokázaná ako invariantná:

- metrika okamžite budí štandardné species;
- fotóny/neutrína vstupujú do `00` a `0i`;
- free-streaming shear vstupuje do `Phi-Psi`;
- baryóny a para prispievajú k density a momentum súčtom.

Dark-only vlastné číslo preto môže byť diagnostika deklarovaného truncation,
nie fyzický PASS alebo STOP celej K11.

## 6. Gauge-invariantný relatívny mód

Definujme

```text
U=V_f-V_c,
V_D=[rho_c V_c+delta rho_f V_f]/[rho_c+delta rho_f],
beta=delta rho_f/[rho_c+delta rho_f].
```

Odčítanie Eulerových rovníc dá v konformnom čase

```text
U'
=(3mathcal H+aGamma/delta)V_D
 +delta_f/delta
 +[mathcal H(2-3beta)
   +(aGamma/delta)(2-beta)
   -(A_c+A_f)]U,
```

kde v tomto riadku `A_c=aUpsilon/rho_c` a
`A_f=aUpsilon/(delta rho_f)`.

`U` je fyzický gauge-invariantný mód, ale nie je autonómny: núti ho total
velocity, fuel density a cez constrainty metrika aj ostatné species. To je
presný dôvod, prečo interaction `2x2` determinant nestačí na full verdict.

## 7. Skorý Frobeniov výsledok

V radiačnej ére

```text
H proportional a^-2.
```

Pre konštantnú finite proper-time `Gamma` a finite regular `gamma_*` preto

```text
Gamma/H = O(a^2),
gamma_*/H = O(a^2),
d_c,d_f = O(a^2)
```

pre harmonický K11-R svedok. Všetky nové K1/K11 interaction členy sú o dva
rády pod vedúcim radiačným indiciálnym symbolom.

**Čiastkový verdict:**

```text
PASS_EARLY_INDICIAL_NULL_LIMIT.
```

Vedúca skorá regular basis je štandardná GR basis. K11 nevytvára nový
primordiálny Frobeniov exponent pri `a->0`.

Toto nezrušuje M-009. Obmedzuje jeho interpretáciu: ide o konečnú/neskorú
amplifikáciu po zosilnení `Gamma/H`, nie o nový vedúci singular exponent
presne na radiačnom počiatočnom bode.

## 8. Zachované scoped no-go

Interaction-only matica

```text
M_int=[[-A_c,A_c],[-G+A_f,2G-A_f]],
G=aGamma/delta
```

má

```text
det M_int=-A_c G<0.
```

Teda pre každé pasívne `Upsilon>0` ostáva jeden kladný interaction smer.
Pri uniformne regular `A_c,A_f=O(1)` a `delta->0` navyše fast K1 vetva
`O(Gamma/delta)` prežije, kým density/metric premenné sú na fast timescale
subleading.

Zostávajú preto platné scoped STOP:

- `K11-R-PASSIVE-INTERACTION-BLOCK-HURWITZ-CURE`;
- `K11-R-UNIFORM-REGULAR-EXACT-POLE-CANCELLATION`.

## 9. Prečo nie je možné vydať full PASS alebo STOP

Koeficienty `H,Omega_A,g,d_c,d_f` sa menia s `a`. Okamžité vlastné čísla
jednej zamrznutej matice nie sú globálne exponenty; ne-normalita môže navyše
vytvoriť prechodný rast.

Full fixed-`delta` rozhodnutie vyžaduje aspoň:

1. všetky štandardné species potrebné pre regular basis;
2. scaled neutrino/steam shear a rádovo odôvodnené uzavretie vyšších
   multipólov;
3. úplnú počiatočnú adiabatic/isocurvature bázu na `00/0i` constraintovej
   ploche;
4. propagáciu `00`, trace a traceless holdoutov;
5. časovo usporiadaný fundamental matrix alebo ekvivalentný globálny
   energy/Lyapunov odhad.

Tieto vstupy v CS1 ešte neboli zostavené do jedného autoritatívneho
operátora. Podľa predregistrácie je preto jediný dovolený hlavný verdict:

```text
UNDETERMINED_REVIEW / FULL MULTISPECIES DAE REQUIRED.
```

## 10. Ďalší konečný krok K11

`K11-CS2` smie byť iba jeden viacdruhový DAE/base kontrakt a jeden
ohraničený regular-basis propagátor s najviac dvoma technickými opravami.
Pred prvým Python behom musí vzniknúť samostatný Markdown s:

- ľudským opisom výpočtu;
- očakávaným rozsahom constraint residualov a transferov;
- `PASS/STOP/REVIEW` vetvami;
- vnútorným limitom `<=5 s` a vonkajším `<=10 s` pre každý beh.

Ak ani úplný CS2 nevie odlíšiť fyzický rast od constraint/gauge módu, K11
sa nesmie ďalej vetviť na CS3a/CS3b. Stav zostane REVIEW alebo sa vydá STOP
podľa vopred zmrazeného kritéria.

## 11. Vstupy a kontrolné súčty

| Vstup | SHA-256 |
|---|---|
| CS1 predregistrácia | `6C6D607CE776E6DE3438DC8303FFE36259232D440D37E25A4D8568F99A2D42B2` |
| akceptovaný K1/M-009 audit | `33E00A58D79B8004E772C5A3C8CCCBE70B0D29A96F4FC3A0DE3ACC8F21F7BB87` |
| K11 FS-GATE regularity/scoped no-go audit | `4B5CEC684B76381A65FC7D800073FA9D7481DE6EF7AB4111BE1F8A4C898FB41D` |
| centrálny feasibility ledger pred CS1 | `C6667BE9DAA02C6C47B8A959EA1DFAA34F1B1BF40E4774C7E31A13B100992912` |

## 12. Obmedzenie starších formulácií

- „K11 drag je stabilný, lebo tlmí relatívnu rýchlosť“ je neplatné: plný
  K1+K11 interaction blok je saddle.
- „M-009 je nový primordiálny Frobeniov exponent“ nie je dokázané a pre
  finite proper-time sadzbu je vedúci radiačný indiciálny symbol GR-like.
- „dark-only 5x5 constrained symbol je úplný“ je neplatné bez dôkazu
  invariantnosti alebo zahrnutia štandardných species a shear.

Staré dokumenty sa nemažú; tieto vety sú ich presné rozsahové obmedzenie.
