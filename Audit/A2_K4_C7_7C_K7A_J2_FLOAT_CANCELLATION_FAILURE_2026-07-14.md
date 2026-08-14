# A2-K4 / C7.7c / K7a-J2 — zlyhanie dvojpresnej vetvy cez `q + 1`

**Dátum:** 2026-07-14  
**Stav hlavnej koľaje A2-K4:** živá, hĺbka bez zmeny **66.5/100**  
**Stav numerickej podkoľaje J2:** **STOP pre úplné uzavretie; vysokopresná časť prešla, dvojpresná implementácia neprešla**

## Čo bolo testované

Skript `scripts/160_script_A2_K4_C7_7c_K7a_J2_high_precision_Tprime_audit.py` porovnal analytické \(T'\) s 80-cifernou centrálnou diferenciou na ploche NID/deep. Prahy boli zaregistrované pred behom a po výsledku sa nemenili.

## Výsledok NID/deep, x = -25

- Frobeniova norma \(T'\): \(8.64612412017876\times10^{-8}\).
- relatívna chyba 80-cifernej centrálnej diferencie:
  - krok \(10^{-8}\): \(1.67\times10^{-17}\),
  - krok \(10^{-12}\): \(1.67\times10^{-25}\),
  - krok \(10^{-16}\): \(1.67\times10^{-33}\).
- vysokopresné brány teda prešli.
- relatívny rozdiel oproti dvojpresnej analytickej implementácii: \(1.5091\times10^{-9}\).
- zaregistrovaný limit bol \(<10^{-14}\), preto bol celkový rozsudok `REVIEW_C7_7C_K7A_J2_TPRIME_UNCLOSED`.

## Hlavná príčina

Dvojpresná implementácia používala

\[
q=-1+\frac12\frac{B'}{B},\qquad \ell=2(q+1).
\]

Na hlbokej radiačnej ploche je \(B'/B\) malé. Výpočet `q = -1 + malé číslo` a následné `q + 1` spôsobí katastrofické odčítanie. Nejde o fyzikálny rozdiel ani o chybu vysokopresnej derivácie, ale o numericky nestabilný zápis algebraicky identickej veličiny.

Stabilný tvar je

\[
\ell=\frac{B'}{B}
\]

vypočítaný priamo ako `denominator_x / denominator`, bez prechodu cez \(q+1\).

## Rozsudok a zákaz obchádzania

1. J2 sa nesmie označiť ako plný PASS, lebo jeho kontrola dvojpresnej implementácie zlyhala.
2. Prah \(10^{-14}\) sa neuvoľňuje.
3. Dvojpresná vetva `ell = 2*(q+1)` je pre K7a na hlbokých plochách **mŕtva numerická podkoľaj**.
4. Hlavná koľaj K7a nezomrela: pokračuje J3 s priamym výpočtom \(B'/B\).
5. Žiadna ODE evolúcia sa pred uzavretím J3 nespúšťa.

## Reprodukcia

```powershell
C:\Python311\python.exe scripts\160_script_A2_K4_C7_7c_K7a_J2_high_precision_Tprime_audit.py --max-runtime-seconds 5 --mode NID --surface deep --dps 80
```

