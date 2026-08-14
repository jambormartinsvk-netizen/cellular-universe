# A2-K4 / C7.7c / K7c.3 — REVIEW skriptu 180 na strope RHS volaní

Dátum: 2026-07-15  
Stav skriptu 180: **REVIEW — technicky neuzavretá evolúcia**  
Stav A2-K4: **ŽIVÁ, 66.5/100**

Po oprave výlučne poradia JSON kľúčov sa projektovaná ODE skutočne spustila. Beh NID/deep `x=-25 -> -24.75` však pred dokončením narazil na preregistrovaný limit 200 000 volaní RHS a skončil za približne 24 s s `TIMEOUT_UNCLOSED`.

## Čo z toho nevyplýva

- Nejde o fyzikálnu smrť: solver nedodal konvergovaný koncový stav ani constraint failure.
- Limit sa nebude zvýšovať naslepo.
- Prahy, rovnice ani segment sa po výsledku neuvoľňujú.
- K7a namerala fyzikálny projektovaný spektrálny polomer približne 3.44, preto samotný počet volaní nestačí na tvrdenie o fyzikálnej tuhosti.

## Povinný ďalší krok

Pred výberom iného solvera sa vykoná nulová integrácia:

1. počiatočný normalizovaný RHS po komponentoch;
2. presný lineárny stĺpcový operátor `A[:,j]=f(e_j)-f(0)` bez FD kroku;
3. fyzikálny a envelope-škálovaný operátor, spektrálny polomer a najväčšie couplingy;
4. žiadna SVD condition proxy pod numerickým noise floorom;
5. pevný časový limit.

Skript 180 a jeho timeout výstup sa zachovávajú. Ďalšia evolučná podkoľaj sa smie zvoliť až podľa tejto diagnostiky.
