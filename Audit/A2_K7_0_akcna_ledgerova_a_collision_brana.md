# A2-K7.0 — akčná, ledgerová a collision-sign brána mediátora

**Dátum:** 2026-07-13  
**Koľaj:** A2-K7  
**Historický alias:** `K5/K4a`  
**Stav:** `PREŽÍVA 30/100`  
**Význam skóre:** zrelosť dôkazového balíka, nie pravdepodobnosť pravdy

## 1. Problém, ktorý K7 rieši

K1, K3 a K4 presúvali energiu a hybnosť priamo medzi near-vacuum palivom a
popolom. K7 zavádza skutočný tretí dynamický nosič `M`. Jeho účelom je:

- niesť energiu a hybnosť počas konečného času;
- nahradiť algebraický energy-frame K4 fyzickým stupňom voľnosti;
- umožniť donorovo orientované rozpady bez recoil sily na near-vacuum
  palivo;
- po zániku mediátora nenechať na popole povinný dlhodosahový skalárny
  náboj K5/K6.

## 2. Prvá lokálna akčná realizácia

Ako prvý scaffold s najväčšou šancou sa volí kanonické palivo `phi`,
masívny kanonický mediátor `chi` a fermiónový popol `psi_c`:

```text
S = integral sqrt(-g) [
      Mpl^2 R/2
    - (partial phi)^2/2 - V(phi)
    - (partial chi)^2/2 - m_chi^2 chi^2/2
    - g^2(phi-phi_*)^2 chi^2/2
    + bar(psi_c)(i gamma^mu D_mu-m_c)psi_c
    - y chi bar(psi_c)psi_c
    ].
```

Pri `m_chi^2+g^2(phi-phi_*)^2>0` majú obe polia správne znamienko
kinetiky a potenciál mediátora je zdola ohraničený. Yukawov člen povoľuje
`chi -> psi_c bar(psi_c)` pri `m_chi>2m_c`. Ak `m_chi>>H`, oscilujúce
`chi` sa po časovom spriemerovaní správa ako `w_M=0`.

Toto je UV scaffold, nie dôkaz požadovaných konštantných sadzieb. Lokálna
hermitovská akcia je reverzibilná. Nevratné `Q_1,Q_2` vznikajú až po
coarse-grainingu produkovaných kvánt. Výpočty nonequilibrium skalárnych
teórií ukazujú, že disipácia môže byť ne-lokálna a pri nulovej teplote
nemusí mať jednoduchý Markovovský limit
([Boyanovsky et al.](https://arxiv.org/abs/hep-ph/9408214)). CTP/2PI
redukcia zároveň prináša disipáciu aj šum spojené fluctuation-dissipation
vzťahom ([Ramsey](https://arxiv.org/abs/gr-qc/0209010)). K7 preto nesmie
neskôr ponechať tlmenie a vyhodiť šum.

## 3. Kovariantný coarse-grained ledger

Donorovo orientovaná reťaz je

```text
Q_phi^mu = -Q1 u_phi^mu,
Q_M^mu   = +Q1 u_phi^mu - Q2 u_M^mu,
Q_c^mu   = +Q2 u_M^mu,
sum_A Q_A^mu = 0.
```

Každý rozpad je izotropický v rámci svojho donora. Projekcia prvého člena
kolmo na `u_phi` je nulová a projekcia druhého odtoku kolmo na `u_M` je
nulová. Preto donor nedostáva ručný recoil. Ide o fyzicky inú konštrukciu
než algebraický energy-frame K4.

Gauge-invariantné multi-fluidné rozklady a zachovanie adiabaticity na
veľkých škálach sú známe, ale musia sa aplikovať na konkrétne transferové
poruchy
([Malik, Wands & Ungarelli](https://arxiv.org/abs/astro-ph/0211602)).
Samotný background nestačí: jednoduché interakcie s `w` blízko `-1` môžu
mať superhorizontový blow-up
([Valiviita, Majerotto & Maartens](https://arxiv.org/abs/0804.0232)).

## 4. Presné zachovanie A1 backgroundu

Registrovaná A1 veličina `rho_F` musí byť celým ne-CDM sektorom, nie iba
`rho_phi`. Preto sa volí

```text
rho_M=epsilon rho_F,
rho_phi=(1-epsilon)rho_F,
p_M=0,
p_phi=w_F rho_F,
w_F=-1+delta,
0<epsilon<delta.
```

Celkové `rho_F,p_F,H(z)` sa nemenia. Kladný entalpický rozpočet dáva

```text
rho_F+p_F=delta rho_F
            =(rho_phi+p_phi)+(rho_M+p_M),
rho_phi+p_phi=(delta-epsilon)rho_F,
rho_M+p_M=epsilon rho_F.
```

Preto je nevyhnutné

```text
epsilon<delta=0.02297.
```

Endpoint `epsilon=delta` nie je povolený: palivo by malo nulovú entalpiu a
jeho donorová štvor-rýchlosť by pri nenulovom `Q1` nebola definovaná.
Kladná hustota mediátora sa teda nedá pridať „zadarmo“; musí znížiť hustotu
paliva. Maximálny príspevok na dnešnom backgrounde je
`Omega_M0<delta Omega_F0`, približne `0.0149`.

## 5. Sadzby vynútené presným A1 rozkladom

Pre konštantné `epsilon` a požadovaný net tok do popola

```text
Q2=Gamma rho_F
```

musí mediátorova rovnica vynútiť

```text
Q1=(1-epsilon)Gamma rho_F
   +3H epsilon(1-delta)rho_F.
```

Potom presne platí

```text
dot(rho_phi)+3H(rho_phi+p_phi)=-Q1,
dot(rho_M)+3H rho_M=Q1-Q2,
dot(rho_c)+3H rho_c=Q2.
```

Maximálne numerické ledgerové rezíduum bolo `2.220e-16`. Člen `Q1`
úmerný `H` je však zatiaľ rekonštrukcia potrebná na konštantné `epsilon`,
nie výstup lokálnej akcie. Toto je hlavná otvorená stena K7.1.

## 6. Interaction-only rýchlostný operátor

V lokálne inerciálnom limite a na prvom ráde v relatívnych rýchlostiach
donorovo orientovaný ledger dáva

```text
dot(v_M)=R1(v_phi-v_M),       R1=Q1/(rho_M+p_M)>0,
dot(v_c)=R2(v_M-v_c),         R2=Q2/rho_c>0.
```

Pre `Delta_Mphi=v_M-v_phi` a `Delta_cM=v_c-v_M` má collision časť maticu

```text
[dot Delta_Mphi]   [-R1   0 ][Delta_Mphi]
[dot Delta_cM  ] = [ R1 -R2][Delta_cM  ].
```

Vlastné hodnoty sú `-R1` a `-R2`; na celom auditovanom intervale boli
záporné. K1/K3/K4 typ interaction-only anti-dampingu sa v tejto bráne
neobjavil.

To ešte nie je úplný superhorizontový dôkaz. Tlakové, metrické, hustotné a
intrinsic/non-adiabatic transferové členy môžu vytvoriť iný mód. Preto sa
stav nesmie označiť ako „stabilná K7“.

## 7. Numerický grid a riziko slabého účinku

Pred výsledkom bol zapísaný grid

```text
epsilon/delta={0.01,0.05,0.10,0.25,0.50,0.90}.
```

Všetky body prešli ledgerom, kladnosťou entalpie a collision znamienkom.
Mediátorový mód sa silno prilepí k palivu:
`log10 D_Mphi=-274.05` až `-11.79`.

Odozva celého popola je však slabá a nezávislá od `epsilon`:

```text
alpha2(0)=0.323115,
log10 D_cM=-0.040953,
D_cM=0.9100.
```

Collision-only prenos teda od rekombinácie tlmí existujúci relatívny mód
iba približne o 9 %. To je vážne riziko pre cieľ `S8`, nie zatiaľ kill:
hustotné zdroje, novovytvorená frakcia popola a metrická odozva ešte neboli
integrované.

## 8. Nulový limit a silná relaxácia

Pri pevnom net toku je

```text
R1/H ~ Gamma/(epsilon H).
```

Limit `epsilon->0` je preto singulárny. Nejde o regulárny návrat ku K4;
mediátor sa mení na okamžite eliminovaný pomocný stupeň voľnosti. K7.1 musí
určiť hranicu platnosti fluidného/Markovovského opisu a nesmie vyhlásiť
nekonečne rýchly mediátor za fyzické riešenie.

## 9. Rozsudok K7.0

**`PREŽÍVA 30/100`.** Presný A1 ledger s kladnou energiou existuje a
donorovo orientovaná collision časť je kontraktívna. Tým K7 odstránila
konkrétnu chybu algebraického K4: nosič má vlastnú hustotu, entalpiu a
relaxačný čas.

Koľaj zatiaľ neprešla:

- odvodením `Q1,Q2` a ich porúch z lokálnej akcie;
- kontrolou noise-dissipation páru;
- úplnými gauge-invariantnými tromi kontinuitami a Eulerovými rovnicami;
- superhorizontovou adiabaticitou;
- high-k kinetickou/gradientovou maticou;
- CMB-normalizovaným rastom a `S8`.

## 10. Nasledujúca kill brána K7.1

1. odvodiť alebo explicitne aproximovať CTP/Boltzmannove jadrá pre
   `phi -> chi -> psi_c`;
2. dokázať rozsah, v ktorom sú lokálne kladné `Q1,Q2` a biely/Markovovský
   šum oprávnené;
3. odvodiť `delta Q1`, `delta Q2` a momentum potentials, nie ich nastaviť
   po výsledku;
4. zostaviť úplný gauge-invariantný trojzložkový systém;
5. zabiť koľaj ako M-014, ak sa vráti rastúci relatívny/entropický mód,
   ak je potrebná záporná entalpia alebo ak lokálna akcia nevie vytvoriť
   požadovaný neskorý tok.

## 11. Dôkaz

- `scripts/50_script_A2_K7_0_mediator_ledger_collision_gate.py`;
- `Audit/A2_K7_0_NUMERICAL_OUTPUT.md`.

