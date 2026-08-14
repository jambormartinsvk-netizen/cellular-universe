# A2-K5.1 — úplné relativistické perturbácie a superhorizontový test

**Dátum:** 2026-07-13  
**Koľaj:** A2-K5/K1 — kanonické skalárne palivo a konformne viazané CDM  
**Verdikt:** `PREŽÍVA A2-K5.1 — 60/100; A3 RASTOVÁ BRÁNA ČERVENÁ`  
**Rozsah:** skalárne módy, Newtonova gauge, perfektná radiácia; bez plnej
fotónovej/neutrínovej Boltzmannovej hierarchie

## 1. Čo bolo potrebné rozhodnúť

K5.0 dokázala existenciu lokálnej akcie a presnú rekonštrukciu backgroundu,
ale nie úplný perturbačný systém. K5.1 mala rozhodnúť, či akciou odvodená
dynamika:

1. zachová Einsteinove constrainty;
2. má regulárny `lambda->0` limit;
3. odstráni starý pól `Gamma/(1+w_f)`;
4. pripúšťa regulárny adiabatický mód;
5. nemá nekontrolovaný gauge-invariantný superhorizontový relatívny mód;
6. reprodukuje už vypočítaný kvázistatický limit.

## 2. Akcia a kovariantná bilancia

```text
S = integral sqrt(-g) [Mpl^2 R/2 -(partial phi)^2/2 -V(phi)]
    + S_c[A(phi)^2 g, psi_c] + S_b[g] + S_r[g].
```

Pri `varphi=phi/Mpl`, `beta=d ln A/d varphi` platí

```text
nabla_mu T_c^(mu nu)=(beta/Mpl) T_c nabla^nu phi,
nabla_mu T_phi^(mu nu)=-(beta/Mpl) T_c nabla^nu phi.
```

Pre prach `T_c=-rho_c` to dáva

```text
rho_c' + 3 Hc rho_c = + beta varphi' rho_c,
varphi''+2 Hc varphi' + a^2 U_,varphi = -a^2 beta rho_c/Mpl^2,
U=V/Mpl^2.
```

Znamienka presne zodpovedajú toku palivo -> CDM. V opačnej konvencii často
používanej v coupled-quintessence literatúre treba mapovať `beta_ref=-beta`.

## 3. Premenné, ktoré neobsahujú umelý fluidný pól

CDM počet častíc je zachovaný. Jeho Einstein-frame hmotnosť je
`m_c(varphi)=m_c0 A(varphi)/A0`. Preto je vhodnou fundamentálnou premennou
kontrast počtu `delta_n`, nie samostatne postulovaný interagujúci fluidný
kontrast:

```text
delta_c = delta_n + beta delta_varphi.
```

Táto identita presne oddeľuje zmenu počtu a zmenu hmotnosti. Nikde sa nedelí
číslom `1+w_f=delta`.

## 4. Úplné nové rovnice v Newtonovej gauge

Používame

```text
ds^2=a^2[-(1+2 Psi)deta^2+(1-2 Phi)dx^2],
theta=-k^2 v,
chi=delta varphi.
```

### 4.1 CDM

```text
delta_n' = -theta_c + 3 Phi',

theta_c' +(Hc+beta varphi')theta_c
 -k^2(Psi+beta chi)=0.
```

Prvý väzbový člen je trenie meniacej sa hmotnosti. Druhý je skalárna sila.

### 4.2 Skalárne palivo

Pri kontraste počtu `delta_n` je presná lineárna Kleinova–Gordonova rovnica

```text
chi''+2 Hc chi'
 +[k^2+a^2 m_eff^2]chi
 -varphi'(Psi'+3 Phi')
 +2a^2[U_,varphi+beta rho_c/Mpl^2]Psi
 =-a^2 beta rho_c delta_n/Mpl^2,
```

kde

```text
m_eff^2 = U_,varphivarphi
 +(rho_c/Mpl^2)(beta_,varphi+beta^2).
```

Člen `beta^2` vzniká preto, že pri pevnom počte častíc sa mení aj ich hmotnosť.

### 4.3 Skalárny tenzor energie a hybnosti

```text
delta rho_phi = Mpl^2/a^2(varphi' chi'-varphi'^2 Psi)
                +V_,varphi chi,

delta p_phi   = Mpl^2/a^2(varphi' chi'-varphi'^2 Psi)
                -V_,varphi chi,

theta_phi = k^2 chi/varphi',
pi_phi=0.
```

Gauge-invariantná relatívna rýchlosť je

```text
V_phi-V_c = chi/varphi' - theta_c/k^2.
```

### 4.4 Baryóny a perfektná radiácia

```text
delta_b'=-theta_b+3Phi',
theta_b'+Hc theta_b-k^2 Psi=0,

delta_r'=-(4/3)theta_r+4Phi',
theta_r'=k^2(delta_r/4+Psi).
```

Plná fotónová polarizácia, Thomsonov člen a neutrínové multipóly zostávajú
štandardné a patria do A3.

## 5. Einsteinove constrainty

Použité znamienka sú rovnaké ako v starom A2 audite:

```text
k^2 Phi+3Hc(Phi'+Hc Psi)=-4 pi G a^2 delta rho,

k^2(Phi'+Hc Psi)=4 pi G a^2(rho+p)theta,

k^2(Phi-Psi)=12 pi G a^2(rho+p)sigma.
```

V prvom teste bola radiácia perfektná, teda `Phi=Psi`. 0i constraint vyvíjal
`Phi`; 00 constraint sa po počiatočnom povrchu už nevynucoval a slúžil ako
nezávislá kontrola.

## 6. Nulový a hlavnosymbolový test

Skript 37 overil `13/13` algebraických brán:

- `lambda->0` dáva `beta=0`, nulový tok a nulovú piatu silu;
- zostane nezávislé kanonické pole a štandardné CDM;
- skalárny časový aj gradientový hlavný člen majú kladné znamienko;
- `delta_c=delta_n+beta chi` a backgroundový zdroj sú presné;
- `m_eff^2>0` na celom testovanom backgrounde.

Limit `delta->0` pri pevnom `lambda` zostáva singulárny. To je obmedzenie
modelu, nie príčina smrti na registrovanom bode `delta=0.02297`.

## 7. Superhorizontový relatívny mód

Počiatočný mód pri `z*=1089.9` mal

```text
u_phi-u_c=1,
X_c u_c+delta X_f u_phi=0,
delta rho_total=0,
Phi=0.
```

Je to fyzický velocity-isocurvature mód s nulovou celkovou tmavosektorovou
hybnosťou a splnenými 00/0i constraintmi.

Opravený skript 39 dal pri `q=k/H0=1e-5`:

```text
|Delta u_0/Delta u_*| = 6.9778803e-6,
lambda=0 transfer     = 1.4693472e-5,
coupled/null gain     = 0.4748966,
ln gain               = -0.7446581.
```

Interakcia teda mód netlmí iba absolútne, ale tlmí ho viac než nulová väzba.

| Brána | Výsledok | Prah | Stav |
|---|---:|---:|---|
| kroková konvergencia | `2.3682e-9` | `<1e-6` | PASS |
| `k` konvergencia | `6.9452e-13` | `<1e-6` | PASS |
| globálne 00 rezíduum | `1.4754e-9` | `<1e-5` | PASS |
| interakčný zisk | `0.4749` | `<e` | PASS |

Tým K5/K1 odstránila konkrétnu superhorizontovú príčinu smrti K1, K3 a K4.

## 8. Regulárny adiabatický mód

Skript 41 zostavil počiatočné podmienky z rovností

```text
delta rho_A/rho_A,x = spoločná hodnota,
u_c=u_phi=u_b=u_r,
```

pričom spoločnú hustotnú časovú zmenu a rýchlosť vypočítal priamo z 00 a 0i
constraintov. Relatívna rýchlosť nebola ručne potlačená počas evolúcie; bola
nulová iba ako definícia adiabatického počiatočného módu.

Jemný beh:

```text
max |u_phi-u_c|/|u_initial| = 9.4420e-8,
final relative ratio        = -8.8904e-8,
global 00 residual          = 1.2173e-10,
step difference             = 2.8603e-7,
k difference                = 6.9313e-10.
```

Zvyšok klesá približne so štvrtou mocninou? Nie: pozorovaný faktor približne
štyri pri polovičnom kroku je numerický diskretizačný trend tohto monitoru.
Audit preto tvrdí iba konvergenciu k nule, nie poradie celej RK schémy.

## 9. Zachované neúspešné behy

### Skript 38

Použil nesprávnu skalárnu entalpiu `X_f E^2 varphi_x^2/3` namiesto
`E^2 varphi_x^2/3=delta X_f`. Povinný 00 test ho odmietol rezíduom `0.1066`.
Jeho fyzikálny transfer sa nesmie citovať. Oprava je zdokumentovaná v
`scripts/ERRATUM_38_39_A2_K5_1_SCALAR_ENTHALPY.md`.

### Skript 40

Prešiel fyzikálnymi bránami, ale krokový rozdiel `1.1441e-6` tesne nesplnil
prah `1e-6`. Skript 41 iba zjemnil kroky a prah nezmenil. Pozri
`scripts/ERRATUM_40_41_A2_K5_1_ADIABATIC_CONVERGENCE.md`.

## 10. Kvázistatický cross-check a zostávajúce riziko

Skript 42 odvodil z plnej skalárnej rovnice

```text
G_eff/G = 1+2 beta^2 q^2/(q^2+a^2 m_eff^2/H0^2)
```

a porovnal nezávislé histórie `E`, `E_x/E`, `varphi_x`, `beta` a `m_eff^2`
so skriptom 33. Všetky rozdiely boli numericky `0.0`.

Dnešné hodnoty:

| `q` | `G_eff/G` |
|---:|---:|
| 30 | `5.5654` |
| 100 | `5.6646` |
| 300 | `5.6735` |

K5.1 teda potvrdzuje, nie ruší, skorší subhorizontový rastový alarm.

## 11. Verdikt

K5/K1 **nie je mŕtva v A2-K5.1**. Prežila lokálnu akciu, nulový limit,
hlavný symbol, úplné prvé relativistické rovnice, constrainty, fyzický
izokurvatúrny mód, adiabatický mód a kvázistatický cross-check.

Stav je

```text
PREŽÍVA A2-K5.1 — 60/100;
A3/CMB-normalizovaná rastová brána zostáva červená.
```

Koľaj sa nesmie vyhlásiť za observačne životaschopnú. Ak plná implementácia
potvrdí, že povinná piata sila zvyšuje `S8` mimo povoleného rozsahu bez
kompenzácie dovolenej CMB dátami, vznikne `MŔTVA M-012`.

## 12. Primárne opory

- [Kase a Tsujikawa — všeobecná akcia skalára viazaného na CDM](https://arxiv.org/abs/2005.13809).
- [Pourtsidou, Skordis a Copeland — akčné triedy couplingov](https://arxiv.org/abs/1307.0458).
- [Barros et al. — competing friction/fifth-force effects](https://arxiv.org/abs/1802.09216).
- [Ma a Bertschinger — štandardné perturbácie a Einsteinove rovnice](https://arxiv.org/abs/astro-ph/9506072).
