# Q22a — audit proveniencie: efektívny ledger nie je mikroskopická postupnosť

**Dátum:** 15. júl 2026  
**Rozsah:** Q22a-K1 až K7; žiadny nový numerický fit ani zmena backgroundu.

## Otázka

Má už teória zapísaný mechanizmus, z ktorého možno vypočítať, či pri delení
vzniknú palivo, popol a para naraz alebo po sebe?

## Zdroje a presný nález

1. `Nespracovane/A16_K1_kovariantne_zobrazenie_SK_v3.18_NAVRH.md`, riadky
   52–80, definuje `Q=Gamma rho_f`, volí `Q^nu=Q u_c^nu` a zapisuje iba
   `nabla T_f=-Q`, `nabla T_c=+Q`. Baryóny a radiácia majú štandardné
   kolízne členy `C_b,C_r`, ktorých súčet je nulový.
2. Ten istý zdroj výslovne uvádza, že `C_b,C_r` **nie sú súčasťou bunkového
   prenosu Q** a ich čistá backgroundová energetická výmena je vo V1
   zanedbaná.
3. Riadky 150–162 zhodného dokumentu potvrdzujú, že A1 rovnica
   `X_m'=-3X_m+lambda X_f/E` je iba pôvodný backgroundový výpočet a že
   neskorý `Q` vytvára CDM/popol, nie baryóny.
4. `Nespracovane/Kozmologická pipeline 09.txt`, riadky 16–23, rovnako vedie
   úbytok paliva presne iba do hmoty. Radiácia/parná zložka je v tejto
   pipeline samostatný zadaný obsah, nie produkt prenosu `Q`.

## Rozsudok

**Existujúca formulácia neurčuje mikroskopické poradie produktov.** Určuje
len efektívnu neskorú backgroundovú bilanciu `F->C`. Neobsahuje lokálnu akciu,
collision kernel, branching rule ani oneskorovací kernel, ktorý by určoval
priamy tok do `R` alebo následnú premenu `C<->R`.

Z toho nevyplýva, že paralelný alebo sekvenčný vznik je zakázaný. Vyplýva iba,
že ho nemožno deklarovať ako dôsledok dnešného A1 alebo pipeline 09.

| Koľaj | Stav po provenienčnom audite | Presný dôvod |
|---|---|---|
| Q22a-K1 | `BASELINE EFFECTIVE PASS` | Explicitne implementovaný `F->C`; nie mikroverdikt. |
| Q22a-K2 | `ČAKÁ` | Vyžadovala by priamy `F->R`, ktorý A1 neobsahuje. |
| Q22a-K3 | `REVIEW BLOCKED` | Conservation dovolí podiel `b`, ale žiadny existujúci operátor ho neurčuje. |
| Q22a-K4 až K7 | `NEOTVÁRAŤ` | Vyžadujú navyše odvodený časový/konverzný kernel. |

## Čo môže rozhodnúť poradie

Matematika a pozorovania môžu rozhodnúť, ale iba v tomto poradí:

1. nový mikrofyzický operátor udalosti delenia dá z existujúcich veličín
   konkrétne `Q_A^mu`, prípadný podiel a prípadnú dobu oneskorenia;
2. z neho sa odvodia background, `delta Q_A`, hybnosti a korelácie;
3. až potom BBN, CMB, `N_eff`, izokurvatúry, rast a lensing vyberú alebo
   vylúčia predregistrované koľaje.

Samo prispôsobenie podielu dátam nie je krok 1; je to nový fit a nemá
predikčnú váhu.

## Stav a ďalší krok

Toto je **analytický/provenienčný audit**, preto výpočtový skript nebol
potrebný. Najbližší platný krok je špecifikovať minimálny operátor `J` alebo
jasne označiť, že taký predpoklad zatiaľ chýba. Dovtedy sa K3–K7 numericky
neprehľadávajú: ich parametre by boli neodvodené.
