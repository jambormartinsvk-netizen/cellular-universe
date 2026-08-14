# Q22a/Q18 — ako z mantinelov odvodiť funkciu, nie ju fitovať

**Účel:** premeniť register mantinelov na matematický problém existencie a
jednoznačnosti pre zdroj pary alebo iný produkt delenia.  
**Stav:** `METODICKÝ PROTOKOL; nepridáva žiadny fyzikálny predpoklad`.

## Základná myšlienka

Nehľadáme najprv „peknú“ funkciu `C_s(t)` a potom ju neobhajujeme. Hľadáme
prienik rovníc, nerovností a okrajových podmienok. Ten môže mať iba tri
výsledky:

| Výsledok prieniku | Význam |
|---|---|
| jedna trajektória | funkcia je odvodená, ak sú aj vstupné konštanty odvodené |
| neprázdna rodina trajektórií | teória povoľuje triedu; ďalšie fyzikálne zákony alebo nezávislé dáta ju majú zúžiť |
| prázdna množina | taký mechanizmus je fyzikálne nemožný a koľaj zomiera |

Toto je priamo testovateľné tvrdenie. Ak po zavedení všetkých mantinelov
zostane ľubovoľná šírka, čas a amplitúda, nejde o predikciu, aj keby jedna
voľba prešla dátami.

## Matematický objekt, ktorý sa má riešiť

Pre lokálne stavy produktu a rezervoára zaveďme iba abstraktne

```text
Y = (rho_s, rho_e, chi, I_1, ...),
dY/dtau = F(Y),
nabla_mu T_s^(mu nu) = +S_s^nu(Y),
nabla_mu T_e^(mu nu) = -S_s^nu(Y).
```

V homogénnej limite sa výsledná funkcia nevkladá samostatne, ale vyjde ako

```text
C_s(tau) = C_s(chi(tau), I_1(tau), ...).
```

Ak fyzika obsahuje viac naozaj odlišných procesov, výsledok môže byť
`C_s=sum_j C_s,j`; každý člen však musí mať vlastný rezervoár a nesmie dvakrát
odpočítať tú istú energiu. Neznámy súčet voľných bumpov nie je odvodenie.

## Ako každý mantinel prispeje k výslednej funkcii

| Trieda mantinelu | Matematický účinok | Čo môže určiť |
|---|---|---|
| M0 lokálnosť | dovolené argumenty `chi,I_i`, evolúcia `dchi/dtau` | kde sa zdroj smie zapnúť/vypnúť; zakazuje voľný kozmický čas |
| M1 ledger | párové zdroje a `sum Q_A^mu=0` | znamienko, maximálny energetický rozpočet a väzbu na rezervoár |
| M2 pozitivita | `rho_A>=0`, `H²>0` | neprípustné amplitúdy a trajektórie |
| M3–M5 časovanie/relikt | BBN/CMB hranice, `rho_s∝a^-4` po zdroji | povinný skorý koniec, prípustnú integrovanú plochu zdroja |
| M6 termodynamika | druhý zákon, teplota, `g_*` | znamienka a prípustné prechody medzi stavmi |
| M7 poruchy | `delta S_s`, frame, šum a korelácie | či je daný background vôbec kompatibilný s izokurvatúrou a `P(k)` |
| M8 stabilita/causalita | charakteristiky, kinetická matica, sadzby | zakáže runaway, ghost a nekauzálny tvar |
| M9 predikčnosť | počet odvodených vs. voľných konštánt | či ide o teóriu alebo fit |
| M10 bez `k` v backgrounde | nezávislosť homogénnej vetvy od realizovaného módu | oddeľuje backgroundovú funkciu od perturbatívnych transferov |

## Poradie riešenia

1. **Existencia stavov:** z M0–M1 určiť `Y`, rezervoár a lokálny operátor.
   Bez toho neexistuje fundamentálna funkcia, iba efektívna história.
2. **Diferenciálne jadro:** z conservationu, rovnice stavu a mikrofyziky
   zostaviť `F(Y)` bez voľného profilu v čase.
3. **Tvrdý obal:** M2–M6 premeniť na nerovnosti a okrajové podmienky.
4. **Poruchový filter:** M7–M8 vyhodiť backgroundy, ktoré nedajú zdravé
   perturbácie.
5. **Rozsudok predikčnosti:** M9 spočíta zvyšné nedourčené konštanty.
   Pozorovania ich smú testovať; nesmú ich potichu nahradiť.
6. **Až potom dáta:** BBN/CMB/lensing vyberajú medzi vopred prípustnými
   riešeniami alebo celú neprázdnu množinu vyvrátia.

## Čo už vieme pre paru

Súčasné M1–M5 ukazujú, že efektívna skorá ukončená trieda nie je prázdna.
M0 však ešte neurčuje stav `chi`, rezervoár ani `F(Y)`. Preto zatiaľ nevieme,
či mantinely povedú k jednej funkcii, konečnej rodine alebo k nule. Táto
neistota je presne a merateľne lokalizovaná — nie je dôvod robiť voľný sken
bumpov.

## Povinný výstup každej budúcej koľaje

Každý nový mechanizmus musí pridať tabuľku:

| Mantinel | Zapísaná rovnica/nerovnosť | Dôsledok pre funkciu | Stav |
|---|---|---|---|

Na konci musí explicitne uviesť počet zostávajúcich voľných konštánt,
funkcií a počiatočných podmienok. Iba tak sa dá objektívne povedať, či
mantinely funkciu odvodili.

