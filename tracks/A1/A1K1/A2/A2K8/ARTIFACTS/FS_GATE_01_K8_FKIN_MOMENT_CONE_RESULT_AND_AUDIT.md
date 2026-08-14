# FS-GATE-01 — K8-Fkin: momentový kužeľ a kompatibilita s presným A1 backgroundom

**Dátum:** 2026-07-16  
**Autorita verdiktu:** hlavný orchestrátor  
**Rozsah:** pozitívna produkcia konštantne hmotného popola na budúcej mass
shell; presný zmrazený A1-K1 background; bez dodatočného rezervoára alebo
relaxačného operátora, ak nie je výslovne uvedený  
**Skórovací účinok:** žiadny  
**Numerický beh:** nebol potrebný; rozhodujúci výsledok je exaktná
pozitivitná nerovnosť a odčítanie dvoch continuity rovníc

## 1. Otázka a predregistrovaný rozhodovací rámec

Audit oddeľuje dve otázky, ktoré sa nesmú zliať:

1. existuje pozitívna on-shell birth miera s daným počtovým a energeticko-
   hybnostným momentom;
2. môže takto vytvorená **teplá/disperzná** populácia zároveň reprodukovať
   presne beztlakový A1 background s tým istým `rho_c` a tým istým zdrojom
   `q=Gamma rho_f`.

Možné výstupy boli:

- `NONEMPTY_WITNESS_MOMENT_CONE`, ak existuje explicitný pozitívny
  momentový svedok;
- `EMPTY_CERTIFIED_SCOPE`, ak presne deklarovaný prienik mantinelov vedie k
  analytickému rozporu;
- `UNDETERMINED_REVIEW`, ak ani jeden výsledok nemožno dokázať.

## 2. Auditovaný priestor a momenty

Nech `mu>=0` je konečná miera na budúcej masívnej mass shell

```text
p_mu p^mu = -m_c^2,
p^0 > 0,
m_c > 0.
```

Jej nultý a prvý moment sú

```text
S_n    = integral dmu,
Q_c^mu = integral p^mu dmu.
```

Pre `S_n>0` existuje takáto pozitívna miera práve vtedy, keď `Q_c^mu` je
budúci časupodobný vektor a

```text
-Q_c,mu Q_c^mu >= m_c^2 S_n^2.
```

V ľubovoľnom birth rámci `u_B` zapíšme

```text
q_B = -u_B,mu Q_c^mu,
Q_c^mu = q_B u_B^mu + j_B^mu,
u_B,mu j_B^mu = 0.
```

Podmienka sa zmení na

```text
q_B^2 - |j_B|^2 >= m_c^2 S_n^2.
```

Pre `S_n=0` pozitivita vynúti aj `Q_c^mu=0`.

### Explicitný izotropný svedok

Definujme

```text
M       = sqrt(-Q_c^2)/S_n,
p_star  = sqrt(M^2-m_c^2),
u_Q^mu  = Q_c^mu/sqrt(-Q_c^2).
```

Rovnomerná miera na sfére momentov

```text
p^mu(n) = M u_Q^mu + p_star e^mu(n)
```

má požadované `S_n` a `Q_c^mu`. Jej druhý moment je

```text
R^{mu nu}
= S_n [M^2 u_Q^mu u_Q^nu + (p_star^2/3) h_Q^{mu nu}],
```

a centrálna kovariancia je pozitívna semidefinitná. Tým je momentový kužeľ
skutočne neprázdny; nejde iba o neúspešný alebo úspešný grid.

V izotropnom rámci, kde `j_B=0`, platí

```text
0 < S_n <= q_B/m_c,
E_B = q_B/S_n,
p_B = sqrt(E_B^2-m_c^2).
```

Pre monoenergetického svedka je tlak vloženej populácie

```text
P_src = q_B/3 [1-(m_c S_n/q_B)^2].
```

Pre všeobecnú pozitívnu izotropnú distribúciu s rovnakými `q_B,S_n`
postačuje ostrý bezpečný obal

```text
0 <= P_src <= q_B/3 [1-(m_c S_n/q_B)^2].
```

Rovnosť `P_src=0` je možná iba pri podpore na nulovej fyzickej hybnosti,
teda pri `q_B=m_c S_n`.

**Čiastkový verdikt:** `NONEMPTY_WITNESS_MOMENT_CONE`. Tento verdikt je iba
kinematický; nie je G2/G3 PASS ani svedok presného A1 backgroundu.

## 3. Rozhodujúci A1 mantinel

Zmrazený A1-K1 background definuje popol ako prach:

```text
p_c = 0,
dot rho_c + 3 H rho_c = q,
q = Gamma rho_f.
```

Homogénna energia pozitívnej masívnej kinetickej populácie však spĺňa
presnú momentovú identitu

```text
dot rho_c + 3 H (rho_c + P_c) = Q_c,
```

kde

```text
P_c = (1/3) integral d^3p (p^2/E_p) f_c(p) >= 0.
```

Ak K8 používa tú istú celkovú energiu `rho_c` a ten istý A1 zdroj
`Q_c=q`, odčítanie rovníc dá

```text
3 H P_c = 0.
```

V auditovanom expandujúcom rozsahu `H>0`, preto

```text
P_c=0.
```

Integrand tlaku je nezáporný a pri `m_c>0` mizne iba pre `p=0`. Teda

```text
support(f_c) subset {p=0},
q = m_c S_n,
u_B^mu = u_c^mu,
Q_c^mu = q u_c^mu.
```

Nenulová cold populácia je v presnom limite distribučná delta miera;
obyčajná absolútne spojitá funkcia podporená na jedinom bode by mala nulovú
mieru.

## 4. Certifikovane prázdna podkoľaj

Definujeme stabilné označenie:

```text
K8-Fkin-WARM-A1-SOURCE-ONLY
```

Jej priestor obsahuje súčasne:

- pozitívnu masívnu birth distribúciu s nenulovou disperziou `P_c>0`;
- presne ten istý A1 energetický zdroj `Q_c=q`;
- presnú A1 trajektóriu `dot rho_c+3H rho_c=q`;
- jeden popolový sektor s `p_c=0`;
- žiadny ďalší energetický recipient, cooling alebo momentum-relaxation
  operátor.

Tento prienik je prázdny, pretože vyžaduje naraz `P_c>0` a z presnej
identity `P_c=0`.

**Autoritatívny scoped verdikt:**
`EMPTY_CERTIFIED_SCOPE / STOP K8-Fkin-WARM-A1-SOURCE-ONLY`.

Nejde o výsledok numerického gridu. Certifikátom prázdnosti je rovnica
`3HP_c=0` spolu s pozitivitou `P_c`.

## 5. Čo zostáva a kam to taxonomicky patrí

| Možnosť | Výsledok |
|---|---|
| cold comoving source-only produkcia | backgroundovo kompatibilná, ale presne sa mapuje na A2-K1 a dedí `M-009` |
| warm final ash s rovnakým `q` | mení A1 continuity; scoped STOP vyššie |
| warm medzistav s okamžitým cooling/number-changing procesom | potrebuje nový účtovaný operátor a recipient; nie je čistý source-only K8 |
| cold produkcia plus rozptyl z toho istého mikrofyzického procesu | patrí do K9; backgroundový energetický moment môže byť nulový, kým lineárny momentum moment tlmí relatívnu rýchlosť |
| cold produkcia plus nezávislý ortogonálny drag | obsahovo K11 |
| warm nosič s vlastným `T^{mu nu}` a následným coolingom | obsahovo mediátorová/bath trieda K7 |
| oddelená warm zložka, premenlivá hmotnosť alebo záporný väzbový tlak | mení alebo rozširuje A1 a vyžaduje nový ledger; nie je loophole v scoped dôkaze |

Ak by sa warm popol nútil sledovať tú istú `rho_c(a)`, kinetická rovnica by
musela používať

```text
Q_c = q + 3 H P_c.
```

Dodatočný člen musí mať fyzický pôvod a opačnú reakciu. Nemožno ho skryť v
rovnakej značke `q` bez zmeny palivovej rovnice alebo pridania rezervoára.

K9 preto nie je týmto dôkazom vylúčená. Musí však odvodiť z jedného procesu:

```text
background: q=m_c S_n, P_c=0,
linear order: delta Q_el^i = -K_derived (v_c^i-v_f^i),
```

so správnou reakciou, nulovým FLRW teplom, bez druhého voľného
`gamma_drag` a bez opätovného zavedenia homogénnej disperzie.

## 6. Obmedzenie staršej formulácie

Starší audit `Audit/A2_K8_1_G2_NUMBER_SOURCE_MOMENT_AUDIT.md` správne
ukázal, že samotný `S_n` neurčuje celý momentum/pressure/noise ledger.
Jeho veta, že všeobecný kinetický kernel môže niesť tlak a preto zostáva
živý, sa týmto auditom **obmedzuje**:

- ako okamžitá on-shell momentová projekcia je pravdivá;
- ako presný svedok zmrazeného A1-K1 backgroundu s rovnakým `q` je
  nepravdivá pre každý `P_c>0`;
- cold hranica sa zlieva s K1 a neprináša nový source-only únik z `M-009`.

Starý audit sa nemaže. Tento dokument je jeho rozsahovým dodatkom a
presným dôvodom zmeny interpretácie.

## 7. Stav rodiča a ďalší krok

Rodič A2-K8 zostáva `REVIEW_BLOCKED_PARENT` iba v širšom taxonomickom
zmysle, kým sa formálne uzavrie, či povoľuje aj interný relaxačný kernel.
Jeho čistá source-only trieda nemá v presnom A1 novú dcéru odlišnú od K1:
warm dcéra je mŕtva a cold dcéra sa zlieva s K1.

Najinformatívnejší ďalší audit je preto K9: preveriť, či jeden lokálny
mikrofyzický proces môže dať cold/threshold produkciu a súčasne nenulový
lineárny momentum-relaxation moment s nulovým FLRW ohrevom. Ak nie, treba
vydať samostatný dôvod smrti K9; ak áno, vznikne skutočne nový svedok.

## 8. Vstupy a auditná stopa

| Vstup | SHA-256 |
|---|---|
| `Questions/A1_rozhodnutie_Q19_a_kovariantny_background_v3.18.md` | `53006B8B808A5ED73E883EB9EC2AC5839A42B222B29C0194BDE47FA85F418E3A` |
| `Questions/A2_K8_1_PREREGISTRATION_NUMBER_SOURCE_MOMENT_LEDGER.md` | `E5C6D08C6A3C1229AB95448FC8EA50F0F0924F643899768B970A986AD72B0DA8` |
| `Audit/A2_00_kovariantny_ledger_zloziek_a_interakcii.md` | `2959287A7E94BD5E9861AD208F2075F20BD7869CD312D3863AD9F33991083BF2` |
| `Audit/A2_K8_1_G2_NUMBER_SOURCE_MOMENT_AUDIT.md` | `5C5FDD9E23AE6E0FFF1F78A4F44A28AFE453EDFAF3B0F436CE16A5B4B9C10FDA` |
| `scripts/150_script_A2_K8_1_number_source_covariant_moment_ledger.py` | `B1E55CCD58C8E3533CD33210069FA9CB0EBCDEC0C3F899C6DA078894127779B3` |
| `scripts/151_script_A2_K8_1_independent_frame_mapping_audit.py` | `EE7C18E7DAEF2D82A38C1F710654B7ACC05B413A0122A92881F3FD431809A0A6` |

Skripty 150/151 neboli znovu spustené: overujú skorší cold momentový ledger,
nie nový tlakový no-go. Exaktný dôkaz vyššie je silnejší než numerická
regresia a nemá tolerančný parameter.
