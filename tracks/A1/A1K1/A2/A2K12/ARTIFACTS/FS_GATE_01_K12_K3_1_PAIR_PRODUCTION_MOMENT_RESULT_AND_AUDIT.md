# FS-GATE-01 — K12-K3.1: neutrálna párová produkcia a separačný mód

**Dátum:** 2026-07-16  
**Autorita verdiktu:** hlavný orchestrátor  
**Rozsah:** pozitívne mass-shell birth miery `c_+,c_-`, presný frozen A1
pressureless background, korelovaný pair noise a symetrická vnútorná
opačne-nábojová sila  
**Skórovací účinok:** žiadny; rodič zostáva `10/100 = G1`  
**Numerický beh:** nebol potrebný; rozhodujú pozitivitné momentové identity,
pair covariance a exaktné center/separation rozdelenie

## 1. Zmrazená otázka

Pre pozitívne produkčné miery `mu_+,mu_-` na budúcich mass shell definujeme

```text
S_+/-       = integral dmu_+/-,
Q_+/-^mu    = integral p^mu dmu_+/-,
R_+/-^{mu nu}= integral p^mu p^nu dmu_+/-.
```

Pri presnej neutrálnej párovej produkcii s nábojmi `+beta,-beta` musí
jedna udalosť vytvoriť oba druhy a

```text
S_+=S_-=S_pair,
beta S_+ - beta S_-=0,
Q_+^mu+Q_-^mu=q u_c^mu,
Q_f^mu=-(Q_+^mu+Q_-^mu),
q=Gamma rho_f.
```

Audit oddeľuje:

1. existenciu pozitívneho cold párového momentu;
2. možnosť nenulovej párovej disperzie pri presnom A1 tlaku nula;
3. účinok vnútorných opačných síl na total a separation mód;
4. existenciu finite-rate mikrofyzického cold produkčného kernelu.

## 2. Explicitný cold párový svedok

Pre rovnaké hmotnosti `m_+=m_-=m` zvoľme

```text
S_pair = q/(2m),
dmu_+  = S_pair delta(p-mu_c)dPi,
dmu_-  = S_pair delta(p-mu_c)dPi.
```

Potom

```text
Q_+^mu=Q_-^mu=(q/2)u_c^mu,
Q_+^mu+Q_-^mu=q u_c^mu,
P_+=P_-=0,
net charge source=0.
```

Pre rozdielne hmotnosti platí `q=(m_++m_-)S_pair`. Druhé momenty cold
delta mier sú PSD. Tým je okamžitý momentový kužeľ neprázdny.

### Korelovaný pair noise

Jedna Poissonova pair udalosť má number inkrement `(1,1)`, preto

```text
N_N = S_pair [[1,1],[1,1]] >= 0.
```

V center/charge báze je total number noise nenulový, ale charge number
noise presne nulový. Fuel reaction noise musí byť event-by-event opačný k
súčtu oboch ash inkrementov. Dve nezávislé Poissonove produkcie by síce
mohli mať nulový stredný náboj, ale nenulový charge shot noise; neboli by
presne neutrálnym pair kernelom.

**Čiastkový verdikt:**

```text
NONEMPTY_WITNESS_K12_K3_1_PAIR_MOMENT_CONE.
```

Nie je to plný `F_K12^(3)` ani G2 PASS.

## 3. Prečo opačné náboje nezrušia tlak

Pre každú pozitívnu masívnu distribúciu

```text
P_+/-=(1/3) integral d^3p [p^2/E_+/-] f_+/- >=0.
```

Preto `P_total=P_++P_-=0` vynúti `P_+=P_-=0`. Nábojové znamienko v tomto
integrále nevystupuje.

Pri back-to-back evente

```text
p_+^mu=E u^mu+k e^mu(n),
p_-^mu=E u^mu-k e^mu(n)
```

sa celková priestorová hybnosť zruší, ale izotropný tlak je

```text
P_total=2 S_pair k^2/(3E)>0
```

pre každé `k>0`. Zrušenie momenta teda nie je zrušenie tlaku.

Frozen A1 a kinetická continuity pre tú istú `rho_c,q` dávajú

```text
dot rho_c+3H rho_c=q,
dot rho_c+3H(rho_c+P_total)=q,
```

odkiaľ pri `H>0` vyplýva `P_total=0`.

Definujeme

```text
K12-K3.1-DISPERSIVE-PRESSURELESS-A1.
```

Táto podtrieda požaduje pozitívne `c_+,c_-`, nenulovú trvalú vnútornú
alebo counter-stream disperziu, presný A1 tlak nula a nijaký kompenzačný
rezervoár.

**Scoped verdikt:**

```text
EMPTY_CERTIFIED_SCOPE /
STOP K12-K3.1-DISPERSIVE-PRESSURELESS-A1.
```

Warm zložka, cooling alebo field pressure môžu meniť ledger, ale nie sú
loophole v tomto presne deklarovanom dôkaze.

## 4. Center-of-mass a separation mód

Pri symetrickom backgrounde definujeme

```text
delta_m=(delta_++delta_-)/2,
delta_q=(delta_+-delta_-)/2,
theta_m=(theta_++theta_-)/2,
theta_q=(theta_+-theta_-)/2.
```

Presné vnútorné sily `F_+=-F_-` sa v súčtovej Eulerovej rovnici zrušia.
Pôsobia iba v rozdielovej/separačnej rovnici.

V auditovanej ľahko-skalárnej realizácii je normalizovaná matica

```text
G = (1/2) [[1+2beta^2,1-2beta^2],
           [1-2beta^2,1+2beta^2]].
```

Má vlastné módy

```text
center:     (1,1),  eigenvalue 1,
separation: (1,-1), eigenvalue 2 beta^2.
```

Pre pracovné `beta=1.52883` je separation hodnota približne `4.6746`.
Kladná hodnota sama nie je ghost certifikát, ale predstavuje silné riziko
segregácie; nejde o termálny tlak.

Cold symetrický total source je

```text
Q_c,total^mu=q u_c^mu.
```

Ak sila ostane iba vnútorná, total/fuel blok je presne K1-like. Nový
separation mód preto sám neopraví M-009 v total/fuel móde.

Definujeme

```text
K12-K3.1-SYMMETRIC-INTERNAL-FORCE-COM-CURE.
```

Jej požiadavka, aby presne symetrická vnútorná sila priamo tlmila total COM
mód, odporuje `F_++F_-=0`.

**Scoped verdikt:**

```text
EMPTY_CERTIFIED_SCOPE /
STOP K12-K3.1-SYMMETRIC-INTERNAL-FORCE-COM-CURE.
```

To nevylučuje asymetriu K12-K2 ani externý momentum/field operátor. Tie však
zapnú net force alebo nový ledger a nie sú bezplatnou symetrickou K3.1
opravou.

## 5. Separation rozptyl a energia

Na lineárnom ráde môže existovať `theta_q!=0`, kým jeho kinetická energia
je `O(theta_q^2)`. Preto okamžite nemení FLRW background. Na druhom ráde sa
však kladná energia a tlak musia účtovať.

Ak opačná sila urýchli oba druhy, energia pochádza z mediátorového poľa.
Úplný ledger musí mať

```text
Q_+^mu+Q_-^mu+Q_field^mu+Q_f^mu=0.
```

Zahodenie field reakcie by porušilo conservation. Nenulový homogénny field
stress-energy by zasa menil frozen A1.

Pasívna friction matica môže tlmiť separation velocity:

```text
L=K[[1,-1],[-1,1]] >=0.
```

Taký friction kernel však nevyplýva zo samotného opačného náboja; je novou
mikrofyzickou zložkou K12-K3 alebo spoločného K9 typu.

## 6. Prahová stena

Pre bežný hladký perturbatívny rozpad

```text
parent -> c_+ + c_-
```

je dcérska hybnosť úmerná dvojtelesovému fázovému priestoru. Presne cold pár
vyžaduje `M_parent=m_++m_-`, kde `k=0` a pre konečný regulárny maticový
element zanikne aj šírka. Nad prahom je produkcia konečná, ale `k>0` a vzniká
kladný tlak.

Definujeme

```text
K12-K3.1-1TO2-EXACT-THRESHOLD-FINITE-RATE.
```

**Scoped verdikt:**

```text
EMPTY_CERTIFIED_SCOPE /
STOP K12-K3.1-1TO2-EXACT-THRESHOLD-FINITE-RATE.
```

Coherent zero-mode, medium-assisted, off-shell alebo kolektívna produkcia
tým nie je vylúčená, ale potrebuje nový kernel a úplný energy/noise ledger.

## 7. Stav K12 po audite

| Rozsah | Stav | Dôvod |
|---|---|---|
| cold neutral pair moment cone | `NONEMPTY` | explicitné pozitívne delta miery, conservation a PSD pair noise |
| warm/dispersive exact-A1 K3.1 | `EMPTY_CERTIFIED_SCOPE` | pozitívne tlaky sa sčítajú |
| symmetric internal-force cure total COM/K1 | `EMPTY_CERTIFIED_SCOPE` | vnútorné sily sa v súčte zrušia |
| smooth 1->2 exact-cold finite-rate | `EMPTY_CERTIFIED_SCOPE` | nulový prahový fázový priestor |
| coherent/cold pair kernel | `UNDETERMINED_REVIEW` | chýba konkrétny finite-rate operátor |
| separation stabilita | `UNDETERMINED_REVIEW` | chýbajú úplné rovnice, scalar field, constraints a high-k symbol |

K12-K1 zostáva osobitne mŕtva `M-016`; nový audit ju neprepisuje. Rodič K12
zostáva otvorený cez K12-K2 alebo rozšírenú K12-K3 s novým externým
momentum/field ledgerom. Čistá symetrická K3.1 však neposkytla source-only
opravu K1 total módu.

## 8. Ďalší krok

Pred solverom treba rozhodnúť, či sa vôbec oplatí mikrofyzicky stavať
coherent cold pair kernel, keď jeho symetrický internal-force total mód
zostáva K1-like. Pokračovanie má význam iba ak vopred deklaruje jeden nový
mechanizmus, ktorý:

1. dá finite-rate cold páry bez skrytého tlaku;
2. stabilizuje separation mód;
3. vytvorí dovolený total momentum moment bez net charge/asymetrického
   fifth-force problému;
4. odvodí field reaction a noise bez nového `S8` fitu.

Ak bod 3 chýba, K12-K3.1 nemôže byť samostatnou cestou na záchranu A1-K1;
ostáva iba nový skrytý sektor bez opravy M-009.

## 9. Obmedzenie starších formulácií

Starší audit správne identifikoval neutrálne pozadie a separation mód, ale
slovnú možnosť „väčší rozptyl“ treba týmto výsledkom obmedziť:

- ako lineárny/nelineárny separation pohyb je možná;
- ako pressureless backgroundová disperzia je nemožná;
- pri presnej symetrii nemení priamo total COM mód;
- jej energia musí byť v field/recipient ledgeri.

## 10. Vstupy a auditná stopa

| Vstup | SHA-256 |
|---|---|
| `Audit/A2_K12_0_DVOJZLOZKOVY_POPOL_OPACNE_SKALARNE_NABOJE.md` | `A08129000B4B15ED803324B4016473F36FF6FE4C4673F4E4245DF4A1BBCEDBCA` |
| `Audit/A2_K12_REENTRY_AFTER_PARTICLE_MOMENT_RULE.md` | `3566E29372B6C64E11B5D3E8E51EB5FDA67DCCF765E24EAC25EE7D43EA698A33` |
| `Questions/A2_K12_PROBLEM_KOLAJE_A_DALSI_POSTUP.md` | `A6A0463E5E8FB97683E0CF9B69636F463547F36D4E2B859581EDFE7926C56C3D` |
| `scripts/65_script_A2_K12_two_opposite_charge_ash_analytic_gate.py` | `E85C3A8ED3EB34B53B2FBE1EBE356719D183D5ADEC3BE18F646B10E0DEDE539F` |
| M-016 register | `AD02566311A9889410CB51650F93FB8D34297040156B39C8B96909BE7A89E12E` |
| K8 pressureless-A1 audit | `F755539E88AFFACC3605867E1268F639D1322FB14B419AC93295A5CFC2B15249` |

Skript 65 nebol znovu spustený. Jeho exaktnú force maticu a M-016 nový
audit nemení; skript navyše neobsahuje nový pair collision kernel ani
pressure/noise test. Opakovanie by neoverilo nový výsledok.
