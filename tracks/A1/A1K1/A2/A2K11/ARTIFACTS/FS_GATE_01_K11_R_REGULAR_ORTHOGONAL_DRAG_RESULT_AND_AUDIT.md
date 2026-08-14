# FS-GATE-01 — K11-R: regulárny ortogonálny momentum drag

**Dátum:** 2026-07-16  
**Autorita verdiktu:** hlavný orchestrátor  
**Rozsah:** momentová, regularitná a termodynamická realizovateľnosť čistého
ortogonálneho dragu nad zmrazeným A1 energetickým tokom  
**Skórovací účinok:** žiadny; stav zostáva `10/100 = G1` a staré numerické
PASS ostávajú zrušené  
**Numerický beh:** nebol potrebný; výsledok je exaktná konštitutívna
konštrukcia a asymptotický dôkaz

## 1. Zmrazená otázka

Fuel má inerciálnu/entalpickú hustotu

```text
h_f = rho_f+p_f = delta rho_f >= 0.
```

Pri signatúre `(-,+,+,+)` definujeme

```text
h_c^{mu nu}=g^{mu nu}+u_c^mu u_c^nu,
F_c^mu=Upsilon h_c^{mu nu}u_f,nu,
F_f^mu=-F_c^mu.
```

Úplný momentový ledger je

```text
Q_c^mu = q u_c^mu + F_c^mu,
Q_f^mu = -Q_c^mu,
q = Gamma rho_f.
```

Hľadaná trieda musí mať:

- `Upsilon>=0` a tlmiace znamienko;
- `Upsilon->0` pri chýbajúcom popole, palive alebo coupling-u;
- konečné `Upsilon/rho_c` aj `Upsilon/(delta rho_f)`;
- nulovú silu a nulový ohrev na FLRW;
- presnú reakciu a nezápornú disipáciu relatívneho módu;
- PSD noise štruktúru alebo explicitne deklarovaný zero-temperature limit.

## 2. Explicitný regularitný svedok

Definujme redukovanú entalpickú hustotu

```text
mu_h = rho_c h_f/(rho_c+h_f)
```

a pri nulovom menovateli jej spojité pokračovanie `mu_h=0`. Najjednoduchší
bod bez nového čísla je

```text
Upsilon_R
= Gamma mu_h
= Gamma rho_c delta rho_f/(rho_c+delta rho_f).
```

Rozmery sú hustota energie za čas. Presne platí

```text
Upsilon_R >= 0,
Upsilon_R/rho_c
  = Gamma h_f/(rho_c+h_f) <= Gamma,
Upsilon_R/h_f
  = Gamma rho_c/(rho_c+h_f) <= Gamma.
```

Preto sila zaniká pri `rho_c->0`, `rho_f->0`, `delta->0` aj `Gamma->0` a
obe Eulerove akceleračné sadzby zostanú ohraničené. Starý pól
`gamma rho_c/(delta rho_f)` nevzniká.

Všeobecnejšia neprázdna trieda je

```text
Upsilon = gamma_*(Y) mu_h,
gamma_*(Y)>=0,
```

kde `gamma_*` je konečná lokálna proper-time sadzba miznúca so spoločným
scatter coupling-om. Jej hodnota však bez mikrofyziky nie je predikciou.

## 3. Znamienko, pasivita a vlastné módy

V lokálnom inerciálnom limite sú interaction-only Eulerove rovnice

```text
rho_c dot v_c = Upsilon (v_f-v_c),
h_f   dot v_f = Upsilon (v_c-v_f).
```

Pre `Delta v=v_c-v_f`:

```text
dot Delta v
= -Upsilon(1/rho_c+1/h_f) Delta v.
```

Pri `Upsilon=gamma_* mu_h` sa to zjednoduší na

```text
dot Delta v = -gamma_* Delta v.
```

Spoločná rýchlosť má vlastnú hodnotu nula a relatívna rýchlosť vlastnú
hodnotu `-gamma_*`. Celková hybnosť sa zachová.

Relatívna kinetická energia

```text
E_rel = (1/2) mu_h |Delta v|^2
```

má interaction-only výkon

```text
dot E_rel = -Upsilon |Delta v|^2 = -2 gamma_* E_rel <= 0.
```

Toto fixuje tlmiace znamienko. Starý mínusový projektor pri rovnakej
definícii sily na popol bol anti-drag.

## 4. Kovariantná práca a background

Ortogonalita k popolu platí presne:

```text
u_c,mu F_c^mu=0.
```

Na FLRW `u_c=u_f`, preto `F_c=0` a A1 background zostane nezmenený.
Reakcia `-F_c` nie je pri rozdielnych rýchlostiach súčasne ortogonálna k
`u_f`; to je fyzikálna práca, nie chyba. Pri
`gamma_rel=-u_c.u_f>=1` je fuel-frame heating

```text
-u_f.F_f
= Upsilon(gamma_rel^2-1)
= Upsilon |Delta v|^2 + O(|Delta v|^4) >= 0.
```

Je presne nulový na backgrounde a na lineárnom energetickom ráde; objaví sa
až kvadraticky a musí zostať v úplnom druhorádovom ledgeri.

Požiadavka, aby rovnaká nenulová disipujúca sila bola súčasne ortogonálna k
obom rozdielnym rýchlostiam, by bola nesprávna: odstránila by potrebnú
prácu alebo vyžadovala ďalší energetický člen.

## 5. PSD mobility a noise

Friction/Onsagerova matica v priestore dvoch prúdov je

```text
L = Upsilon [[1,-1],[-1,1]].
```

Má vlastné čísla `0` a `2Upsilon>=0`, teda je pozitívna semidefinitná. V
lokálnom Markovskom limite pri spoločnej efektívnej teplote `T_*>=0` možno
zvoliť

```text
<xi_A^i(t) xi_B^j(t')>
= 2 T_* L_AB delta^ij delta(t-t').
```

Ekvivalentne `xi_f=-xi_c`, takže noise zachováva celkovú hybnosť. Zaniká
pri každom missing-medium/coupling limite a pri `T_*=0`.

Tento blok dokazuje PSD-kompatibilitu, nie pôvod `T_*`, Markovskosť ani
FDT near-vacuum paliva. Pri ne-Markovskom opise treba odvodiť retarded
kernel aj noise z jednej pozitívnej spektrálnej hustoty.

## 6. Autoritatívny momentový verdikt

```text
NONEMPTY_WITNESS_K11_R_CONSTITUTIVE_CLASS / REVIEW
```

Explicitný `Upsilon_R` vyvracia všeobecné tvrdenie, že každý ortogonálny
drag musí mať `1/delta` pól alebo anti-drag znamienko. Spĺňa ortogonalitu,
reakciu, pozitivitu, regularitu, pasivitu, nulový FLRW účinok a pripúšťa
PSD noise blok.

Nie je to plný `F_K11^(3)` ani G2/G3 PASS, pretože chýba:

- lokálna akcia alebo collision kernel odvodzujúci `gamma_*`;
- dôkaz, že potrebná veľkosť nevznikla fitom na `S8`;
- úplné `delta Q`, kontinuity, Eulery, Bianchiho identita a constraints;
- mikrofyzický memory/noise/FDT ledger;
- superhorizontová a high-`k` stabilita;
- CMB-normalizovaný `S8` výpočet.

## 7. Rozhodujúca hranica účinnosti voči M-009

Existencia zdravého dragu ešte neznamená, že zachráni K1. M-009 má vedúcu
relatívnu sadzbu

```text
nu_M009 = O(Gamma/delta).
```

Najjednoduchší regularitný svedok má

```text
nu_drag
= Upsilon_R(1/rho_c+1/h_f)
= Gamma.
```

Pre `delta<<1` je teda parametricky slabší. Ak by drag mal rušiť celý
vedúci pól **uniformne pre ľubovoľne malé delta**, potreboval by

```text
nu_drag = O(Gamma/delta).
```

To je v rozpore s požiadavkou, že `nu_drag` zostáva pri `delta->0`
ohraničené.

Definujeme scoped podtriedu

```text
K11-R-UNIFORM-REGULAR-EXACT-POLE-CANCELLATION.
```

Jej súčasné požiadavky sú:

1. čistý momentum drag;
2. uniformne konečné akceleračné sadzby pri `delta->0`;
3. zrušenie celého vedúceho `Gamma/delta` módu pre všetky dostatočne malé
   `delta`.

Požiadavky 2 a 3 sú asymptoticky nezlučiteľné.

**Scoped verdikt:**

```text
EMPTY_CERTIFIED_SCOPE /
STOP K11-R-UNIFORM-REGULAR-EXACT-POLE-CANCELLATION.
```

Tento STOP neplatí automaticky pri jednej pevnej hodnote
`delta=0.02297`. Konečná, mikrofyzicky odvodená sadzba môže pri tomto bode
zmeniť vlastné módy. Musí sa však odvodiť pred numerickým testom; faktor
zvolený tak, aby trafil `1/delta` alebo `S8`, by bol nový fit.

## 8. Ďalšie mŕtve podtriedy

| Podtrieda | Dôvod scoped smrti |
|---|---|
| `Upsilon=gamma rho_c` | nezaniká s palivom; `Upsilon/(delta rho_f)` diverguje |
| `Upsilon=gamma delta rho_f` | nezaniká s popolom; `Upsilon/rho_c` diverguje |
| density-independent `Upsilon` | poruší oba missing-medium limity |
| `Upsilon<0` | anti-drag a záporná mechanická entropická produkcia |
| `F_f!=-F_c` | porušenie celkovej momentum conservation |
| finite-`T` Markov drag s presne nulovým noise/diffusion | porušenie FDT |
| post-data `C_S8 mu_h` | porušenie predikčnosti |

Starý `Upsilon=gamma rho_c` a staré znamienko zostávajú mŕtve. Nový
harmonický svedok ich neoživuje.

## 8.1 Exaktný interaction-only determinant

Pre akceptovaný K1 fuel recoil definujme

```text
G   = Gamma/delta > 0,
A_c = Upsilon/rho_c > 0,
A_f = Upsilon/(delta rho_f) > 0.
```

Interaction-only rýchlostné rovnice majú maticu

```text
M = [[-A_c,       A_c],
     [-G+A_f, 2G-A_f]].
```

Jej invarianty sú

```text
trace(M)=2G-A_c-A_f,
det(M)=-A_c G < 0.
```

Pre každé pasívne `Upsilon>0` a `Gamma>0` má preto dve reálne vlastné
hodnoty opačného znamienka:

```text
lambda_+>0>lambda_-.
```

Výsledok nezávisí od veľkosti ani hustotnej závislosti `A_f`. Pasívny
exact-reaction drag môže presúvať K1 pump medzi oboma prúdmi, ale samotný
interaction blok nikdy neurobí kontraktívny.

Definujeme

```text
K11-R-PASSIVE-INTERACTION-BLOCK-HURWITZ-CURE.
```

**Scoped verdikt:**

```text
EMPTY_CERTIFIED_SCOPE /
STOP K11-R-PASSIVE-INTERACTION-BLOCK-HURWITZ-CURE.
```

Tento determinant sám nezabíja plný kozmologický K11 systém. Pri `H!=0`
nie je izolovaný rýchlostný blok invariantne uzavretý: fuel continuity,
tlak, density a metric/Einsteinove väzby môžu meniť vlastné módy. Aj
frozen-density matica s Hubbleovými členmi už nemá sign-definitný
determinant. Plná stabilita preto zostáva `REVIEW`, ale nesmie sa odvodiť zo
slovného tvrdenia „drag tlmí“; musí ju dokázať úplná constrained
superhorizontová báza.

## 9. Rozdiel voči K9

K11 preberá A1 tok `q=Gamma rho_f` ako hotový energetický operátor a pridáva
samostatný ortogonálny drag. Aj keď pre najjednoduchší svedok zvolíme
`gamma_*=Gamma`, ide bez mikrofyzického odvodenia o konštitutívnu K11
voľbu, nie dôkaz jednej interakcie.

Ak tá istá akcia alebo collision kernel odvodí súčasne A1 produkciu aj
`gamma_*/Gamma`, realizácia sa taxonomicky zlieva s K9 a nesmie sa počítať
ako druhá nezávislá koľaj.

## 10. Ďalší krok

K11 má teraz dva oddelené blockery:

1. **pôvod:** odvodiť `gamma_*(Y)` z lokálnej mikrofyziky a jej noise;
2. **účinnosť:** keďže interaction-only matica je presne saddle, pri
   zmrazenom `delta=0.02297` zostaviť celý constrained superhorizontový
   symbol A1+K11 vrátane density, pressure, metric a Hubble členov a určiť,
   či vôbec existuje odvodený interval `gamma_*/Gamma` bez rastúceho
   fyzického módu.

Numerický solver sa smie otvoriť až po oboch bodoch. Zdravý `Upsilon_R` s
`gamma_*=Gamma` je kontrolný nulovo-parametrový kandidát, nie predpokladaný
víťaz.

## 11. Vstupy a auditná stopa

| Vstup | SHA-256 |
|---|---|
| `Audit/A2_K11_audit_opraveneho_scriptu_45_a_momentum_drag.md` | `9B2C190988480986A68D043EE440D31F6A905C63145011A02EF1CD1EF7D3B193` |
| `Audit/A2_K11_REENTRY_AFTER_K8_K9_NO_NEW_OPERATOR.md` | `F9F10BEFA06CB4F257341F5B83769042542F8603ABC65105DD918601614291C0` |
| M-009 audit | `33E00A58D79B8004E772C5A3C8CCCBE70B0D29A96F4FC3A0DE3ACC8F21F7BB87` |
| `tracks/A1/A1K1/A2/A2K1/00_TRACK.md` | `B442F3C144D7C8E32618603BCE28E89115E526AB58160E6E86FDFC9050667F52` |
| K9 FS-GATE audit | `8F85182729785099BE78347A871E7441A35A226BAF18BF2CA835CC13879A826A` |

Historické skripty 45–54 a 68 neboli spustené. Ich implementovaný operátor
mal chybné znamienko, neregulárnu hustotnú závislosť a zrušený fyzikálny
PASS; nový `Upsilon_R` v nich nie je implementovaný. Opakovaný beh by bol
zavádzajúci a porušil by pravidlo nevracať sa k známej neplatnej fyzike.
