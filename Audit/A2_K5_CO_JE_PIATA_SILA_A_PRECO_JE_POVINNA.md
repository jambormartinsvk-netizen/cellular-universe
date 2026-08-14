# A2-K5 — čo je piata sila a prečo je v tejto koľaji povinná

**Dátum:** 2026-07-14  
**Koľaj:** konkrétna konformná skalárna realizácia A2-K5  
**Stav koľaje:** `MŔTVA M-012`

## 1. Čo fyzici nazývajú „piata sila“

V bežnom pomenovaní poznáme štyri základné interakcie:

1. gravitáciu;
2. elektromagnetickú interakciu;
3. silnú jadrovú interakciu;
4. slabú jadrovú interakciu.

„Piata sila“ nie je názov jednej potvrdenej konkrétnej sily. Je to spoločný
názov pre akúkoľvek ďalšiu interakciu, ktorá spôsobuje zrýchlenie častíc nad
rámec štandardnej gravitácie a troch interakcií Štandardného modelu.

V K5 je nositeľom tejto dodatočnej interakcie skalárne pole paliva `phi`.
Preto ide o **skalárnu piatu silu medzi časticami popola/CDM**.

Samotná existencia piatej sily nie je porušením fyzikálneho zákona. Nová
teória ju však musí odvodiť z konzistentnej akcie a jej sila, dosah a účinky
musia prejsť pozorovaniami.

## 2. Čo bolo zvláštne na popole v K5

Častica popola nemala konštantnú hmotnosť. Jej hmotnosť závisela od hodnoty
skalárneho poľa:

```text
m_c(phi)=m_c0 A(phi),
varphi=phi/M_Pl,
beta(varphi)=d ln A/d varphi=d ln m_c/d varphi.
```

Parameter `beta` preto vyjadruje dve veci naraz:

- ako citlivo sa mení hmotnosť popola pri zmene poľa;
- aký veľký skalárny náboj má popol voči poľu `phi`.

To je jadro odpovede. V tejto akcii „závislosť hmotnosti od poľa“ a
„skalárny náboj“ nie sú dve nezávislé voľby. Sú tou istou deriváciou `beta`.

## 3. Časová zmena poľa vytvára prenos energie

V homogénnom vesmíre závisí pole iba od času. V konvencii K5 platí

```text
rho_c' + 3 mathcal_H rho_c = beta varphi' rho_c.
```

Pravá strana je energia, ktorú získava popol. K5 ju rekonštruovala tak, aby
sa rovnala registrovanému metabolickému toku

```text
beta varphi' rho_c = a Gamma rho_f,
Gamma=lambda H0.
```

Ak chceme nenulový tok a pole sa vyvíja, musí byť `beta != 0`.

Na dokonale homogénnom pozadí neexistuje priestorový gradient poľa. Preto sa
tam piata sila ešte neprejaví ako zrýchlenie. Vidíme iba časovú časť väzby —
zmenu energie a hmotnosti popola.

## 4. Priestorová zmena toho istého poľa vytvára silu

Skutočný vesmír nie je dokonale homogénny. Má prehustenia a podhustenia.
Preto píšeme

```text
varphi(x,t)=bar(varphi)(t)+chi(x,t).
```

Rovnaká kovariantná väzba, ktorej časová časť mení hmotnosť, má aj
priestorovú časť. Pohybová rovnica popola v K5 je

```text
theta_c' +(mathcal_H+beta varphi')theta_c
 -k^2(Psi+beta chi)=0.
```

Význam členov:

- `Psi` je obyčajný gravitačný potenciál;
- `beta varphi'` je trenie alebo anti-trenie meniacej sa hmotnosti;
- `beta chi` je nový skalárny potenciál;
- jeho gradient `-beta grad(chi)` je piata sila.

V časticovom obraze vznikne to isté variáciou akcie

```text
S_particle=-integral m_c(phi) ds.
```

Ak hmotnosť závisí od polohy cez `phi(x)`, častica sa pohybuje smerom, ktorý
znižuje jej akciu. Jej dráha už nie je geodetikou samotnej Einsteinovej
metriky; obsahuje člen kolmý na štvorrýchlosť úmerný
`-beta grad(varphi)`.

## 5. Prečo prehustenie popola vytvorí príťažlivosť

Prehustenie popola je zdrojom skalárnej poruchy. V kvázistatickom limite K5
vyšla rovnica

```text
chi = -3 beta X_c delta_n
      /[q^2/a^2 + m_eff^2/H0^2].
```

Keď sa toto riešenie vloží späť do Eulerovej rovnice popola, vznikne

```text
G_eff/G
=1+2 beta^2 q^2/(q^2+a^2 m_eff^2/H0^2).
```

Dodatočný člen je nezáporný, pretože obsahuje `beta^2`. Častice popola majú
rovnaký typ skalárneho náboja, a preto sa navzájom priťahujú.

Zmena znamienka `beta` nepomôže: zmení smer niektorých backgroundových
konvencií, ale sila medzi rovnakými časticami zostane úmerná `beta^2` a teda
príťažlivá.

## 6. Prečo je piata sila v K5 povinná

### 6.1 Rovnaká väzba má časovú aj priestorovú časť

Kovariantná bilancia K5 je

```text
nabla_mu T_c^(mu nu)
=(beta/M_Pl) T_c nabla^nu phi,

nabla_mu T_phi^(mu nu)
=-(beta/M_Pl) T_c nabla^nu phi.
```

Pre `nu=0` dostaneme prenos energie na pozadí. Pre `nu=i` dostaneme prenos
hybnosti a skalárnu silu. Nie sú to dve ľubovoľné rovnice; sú to komponenty
jednej štvorvektorovej rovnice.

Odstrániť priestorovú časť a ponechať časovú by znamenalo rozrezať
kovariantnú rovnicu podľa toho, ktorý výsledok sa nám páči.

### 6.2 Nenulový tok vyžaduje nenulové `beta`

Ak nastavíme

```text
beta=0,
```

zmizne piata sila, ale zároveň zmizne zmena hmotnosti a registrovaný tok
`palivo -> popol`. Tým by K5 prestala realizovať A1 background.

### 6.3 Popol nevyhnutne budí poruchu poľa

Mohli by sme skúsiť vyhlásiť `chi=0`. Skalárna rovnica však obsahuje zdroj

```text
-a^2 beta rho_c delta_n/M_Pl^2.
```

Pri `beta != 0` a `delta_n != 0` teda prehustenie popola samo vytvára
`chi != 0`. Nulová skalárna porucha nie je stabilné všeobecné riešenie.

### 6.4 Zachovanie energie a hybnosti spája oba účinky

Energia a hybnosť, ktorú získa popol, musí presne stratiť skalárne pole.
Vymazanie sily iba z Eulerovej rovnice popola by porušilo akciou odvodenú
bilanciu alebo by vyžadovalo nový kompenzačný operátor.

Taký operátor by už nebol pôvodnou K5, ale novou koľajou.

## 7. Analógia s kopcom, ktorého výška určuje hmotnosť

Predstavme si krajinu, kde hmotnosť vozíka závisí od výšky terénu.

- Ak sa výška celej krajiny mení s časom, mení sa hmotnosť vozíka. To je
  backgroundový prenos energie.
- Ak má krajina miestne kopce a doliny, hmotnosť vozíka závisí aj od polohy.
  Vozík preto cíti dodatočný smer pohybu. To je piata sila.

Nedá sa zachovať pravidlo „výška mení hmotnosť“, ale súčasne prikázať
vozíku, aby priestorové rozdiely výšky vôbec necítil. Na to by sme museli
zmeniť mechanizmus.

## 8. Znamená `G_eff/G približne 5.7`, že všetka gravitácia je 5.7-krát silnejšia?

Nie. V nescreenovanej limite dnes vyšlo

```text
beta_0=1.52883,
1+2 beta_0^2=5.67466.
```

Toto číslo označuje približnú **CDM–CDM skalárnu príťažlivosť na mierkach,
kde je mediátor dostatočne ľahký**. Neznamená, že:

- baryóny cítia rovnakú piatu silu;
- laboratórna gravitácia je 5.7-krát silnejšia;
- všetky kozmologické mierky majú rovnaký faktor;
- celková hustota hmoty narastie 5.7-krát.

Baryóny boli v K5 minimálne viazané a cítili pole nepriamo cez metriku.
Konečná hmotnosť skalára obmedzuje dosah sily. Pre testované dnešné
subhorizontové módy však vyšlo

| `q=k/H0` | `G_eff,cc/G` |
|---:|---:|
| 30 | `5.5654` |
| 100 | `5.6646` |
| 300 | `5.6735` |

Keďže sila pôsobila najmä neskoro a priamo iba na popol, integrovaný
hustotne vážený rast všetkej hmoty sa zvýšil približne o `5.2–5.3 %`, nie o
faktor 5.7.

## 9. Dalo sa piatej sile vyhnúť bez zabitia K5?

V rámci presne registrovanej K5 nie.

Možnosti by boli:

1. **`beta=0`:** sila zmizne, ale zmizne aj požadovaný tok energie;
2. **veľmi ťažké pole:** sila sa Yukawovsky odtieni, ale treba znovu
   rekonštruovať akciu a dokázať, že rovnaké pole stále vytvára požadovaný
   tok na celom backgrounde;
3. **screening alebo nový momentum operátor:** môže byť fyzikálne možný, ale
   mení akciu a zakladá novú koľaj;
4. **produkcia počtu častíc namiesto zmeny ich hmotnosti:** tiež je nový
   mechanizmus a nová koľaj;
5. **ručne vymazať `beta chi`:** nie je dovolené, pretože poruší rovnice
   odvodené z akcie.

Preto hovoríme, že piata sila bola **povinná v K5**, nie že je povinná v
každej možnej teórii bunkového priestoru.

## 10. Prečo K5 nezomrela iba za „existenciu novej sily“

Piata sila sama osebe nebola automatický kill test. K5 zomrela až preto, že

1. jej veľkosť bola určená tokom energie;
2. mala príťažlivé znamienko;
3. priaznivé trenie bolo slabšie než jej rastový účinok;
4. výsledný rast štruktúr sa posunul opačne od cieľa pre `S8`;
5. konzervatívna CMB-kotvená brána zostala ďaleko nad registrovaným rozsahom.

Iná akcia môže obsahovať slabšiu, kratšiu, odpudivú medzi odlišnými nábojmi
alebo momentum-transferovú interakciu. Musí však byť odvodená a otestovaná
ako samostatná koľaj.

## 11. Jednovetová odpoveď

> Piata sila v K5 je dodatočná príťažlivosť popola sprostredkovaná skalárnym
> poľom; je povinná preto, že tá istá závislosť hmotnosti popola od poľa,
> ktorá časovou zmenou poľa vytvára požadovaný tok energie, dáva popolu aj
> skalárny náboj reagujúci na priestorové zmeny poľa.

## 12. Primárne opory a reprodukcia

- [Kase a Tsujikawa — všeobecná akcia a perturbácie skalára viazaného na CDM](https://arxiv.org/abs/2005.13809)
- [Pettorino — coupled dark energy a piata sila medzi časticami tmavej hmoty](https://arxiv.org/abs/1305.7457)
- `Audit/A2_K5_1_uplne_relativisticke_perturbacie_a_superhorizontovy_test.md`
- `scripts/37_script_A2_K5_1_action_equations_sign_null_audit.py`
- `scripts/42_script_A2_K5_1_quasistatic_limit_crosscheck.py`


## 13. Oprava možného nedorozumenia: pomohla piata sila K5 dostať sa ďaleko?

**Nie priamo.** K5 sa dostala ďaleko preto, že bola odvodená z jednej
kovariantnej akcie, mala uzavreté rovnice pozadia aj porúch, správny nulový
limit a prešla skorými konzistenčnými a superhorizontovými kontrolami. To je
metodický úspech koľaje, nie priaznivý účinok piatej sily na `S8`.

V koľaji pôsobili dva odlišné efekty:

1. člen úmerný relatívnej rýchlosti mohol tlmiť rýchlostný mód a správať sa
   ako trenie;
2. skalárna piata sila medzi časticami popola bola príťažlivá a zosilňovala
   ich zhlukovanie.

Pre cieľ `S8` rozhoduje ich **čistý súčet**. V K5 prevládla príťažlivá piata
sila, takže rast štruktúr sa zrýchlil namiesto požadovaného spomalenia.

Nie je správne povedať, že stačí otočiť znamienko `beta`. Sila medzi dvoma
rovnako skalárne nabitými časticami obsahuje `beta^2`, a preto obyčajná zmena
`beta -> -beta` nemení jej príťažlivý charakter. Potrebujeme novú koľaj, v
ktorej bude splnená aspoň jedna z možností:

- piata sila bude na relevantných škálach zoscreenovaná alebo krátkodosahová;
- nezávislý, konzistentný prenos hybnosti vytvorí silnejšie tlmenie než
  dodatočná príťažlivosť;
- popol nebude získavať energiu cez poľovo závislú hmotnosť, takže energia sa
  môže prenášať bez rovnakého skalárneho náboja;
- vznikne fyzikálne odvodená odpudivá zložka bez ghostov, gradientovej
  nestability a porušenia zachovania energie a hybnosti.

Požiadavka teda nie je „otočiť znamienko piatej sily za každú cenu“, ale
dosiahnuť, aby **výsledný príspevok novej interakcie k rastu štruktúr bol
tlmiaci**, pričom pozadie, perturbácie a stabilita zostanú konzistentné.
