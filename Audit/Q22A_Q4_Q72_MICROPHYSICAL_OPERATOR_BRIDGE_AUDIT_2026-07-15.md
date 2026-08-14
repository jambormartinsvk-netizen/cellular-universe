# Q22a — mostový audit Q4, Q22a a Q72: čo už určuje mikrofyziku delenia

**Dátum:** 15. júl 2026  
**Typ:** analytický/provenienčný audit; výpočtový skript nebol potrebný.  
**Otázka:** dá sa z existujúcich odvodení `delta`, `lambda` a jaziev už
odvodiť operátor, ktorý rozhodne paralelný alebo sekvenčný vznik popola a
pary?

## Auditovaná evidencia

| Evidencia | Čo naozaj určuje | Čo neurčuje |
|---|---|---|
| Hlavný dokument A2, `delta=1/(<k>+C)` | energetickú réžiu prestavby väzieb a efektívne `w_f=-1+delta` | príjemcu prenesenej energie, podiel popola/pary ani ich hybnosť |
| Hlavný dokument A7 | tvar efektívneho backgroundového transferu `q=Gamma rho_f` a mapu `lambda(H0/H)` pri prechode na e-foldy | lokálny maticový element, collision kernel, `delta Q_A` a priestorovú časť `Q_A^mu` |
| Hlavný dokument A7/A8 | `lambda=0.15` je výslovne jediný fit; `epsilon_eff=lambda H0 t_P` je aritmetické čítanie | odvodenie `epsilon`, pravdepodobnosti jazvy alebo vetvenia produktov |
| Q4, `Q4_problem_epsilon_jazvy_kolaje_K1-K4.md` | zoznam nutných definícií `F,I,p_F,p(I|F),E_I,N_trial`; K1 reprodukuje rád `epsilon^2` | definíciu elementárnej udalosti, energiu jazvy a mapu na hustoty; Q4-P0 je stále otvorená |
| Q72 a A2-K8.1 | skalárny zdroj počtu dá energetickú projekciu vo FLRW | pôrodný frame, tlak, šum a úplný `Q_c^mu`; vyžaduje `C[f]` |

## Presný rozsudok

**Nie, z dnešného korpusu sa taký operátor ešte neodvodí.** Najsilnejší
existujúci výsledok je efektívna backgroundová bilancia
`q=Gamma rho_f`, nie mikroskopická udalosť. Ani geometrická réžia `delta`,
ani numerická zhoda `epsilon_eff^2` neurčujú, či `q` končí v `C`, `R`, v oboch
alebo cez medzistav.

Toto nie je smrť hypotézy spoločného pôvodu. Je to presná hranica jej
súčasného rozsahu:

```text
Q4-P0 (definícia zlyhania/jazvy)
      +
Q72 / K8-Fkin (momenty a collision kernel)
      ->
Q22a-G0 (Q_F^mu,Q_C^mu,Q_R^mu, poradie a P_AB(k)).
```

Bez oboch vstupov by sa výber K2–K7 rovnal voľbe produktového podielu alebo
oneskorenia po prezretí dát.

## Nová spoločná brána Q22a-G0 — bez nového parametra

Pred ďalšou fyzikálnou koľajou musí jeden dokument/odvodenie poskytnúť:

1. definíciu elementárnej udalosti, jej energie a invariantnej miery;
2. úplný štvorvektorový ledger všetkých produktov so súčtom nula;
3. odvodený podiel produktov alebo dôkaz, že jeden z nich je nulový;
4. ak je poradie sekvenčné, odvodený kernel alebo explicitný medzistav;
5. z rovnakého mechanizmu `delta Q_A`, tlak, šum a spoločný zdroj `P_AB(k)`.

Brána nevytvára novú fyzikálnu koľaj ani nový fit. Je to spoločná vstupná
podmienka, ktorá zabráni, aby K3–K7 potajomky nahradili chýbajúcu mikrofyziku
parametrom.

## Overenie pokrytia Q4-P0 v korpuse

Statické vyhľadanie z 15. júla 2026 našlo symbol `xi`/`ξ`, `E_I`, `N_trial` a
„pasca #7“ iba v registri otázky Q4, v jeho vlastnom probléme a v starších
auditoch, ktoré oznamujú tú istú chýbajúcu definíciu. Nenašla sa definujúca
rovnica, stavový priestor ani implementácia elementárnej udalosti.

Preto je stav brány presne

```text
Q22a-G0 = REVIEW_BLOCKED_BY_Q4-P0_DEFINITIONAL_INPUT.
```

To nie je fyzikálny FAIL K1–K7 ani dôvod na ich vymazanie. Je to stop bod:
bez definície by každá konkrétna voľba produktu iba pridala nový postulát.

## Najkratší ďalší postup

1. Doplniť Q4-P0 definíciami `F`, `I`, `E_I`, `N_trial`, významom `xi` a
   explicitným významom „pasce #7“.
2. Zistiť, či z takto definovanej udalosti vie vzniknúť úplný kinetický
   `C[f]`; ak nie, pomenovať nový postulát ako hypotézu.
3. Až po G0 otvoriť jednu z K2–K7, najprv tú, ktorú operátor jednoznačne
   vynúti. Žiadne pozorovania sa nepoužijú na výber parametra pred krokom 2.
