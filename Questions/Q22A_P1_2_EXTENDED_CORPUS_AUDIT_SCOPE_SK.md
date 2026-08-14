# Q22a/Q18 P1.2 — predregistrácia rozšíreného korpusového auditu

**Dôvod:** P1.1 auditoval Q4, Q8, Q18/Q23 a A2.0. Pred definitívnym prijatím
jeho P1 STOP treba preveriť, či lokálny clock, rezervoár alebo exitový zákon
nie je už pomenovaný v hlavnom dokumente alebo v `Nespracovane`.

**Rozsah:** read-only textový audit `theory/SK`, `theory/EN`, `Nespracovane`
a relevantných auditov. Nevykoná sa Python, numerika ani tvorba novej koľaje.

**Hľadané dôkazy:** explicitná definícia aspoň jedného z:

1. lokálny stav/clock s jednotkami a evolúciou;
2. rezervoár s hustotou alebo `T^(mu nu)`;
3. párový zdroj `-S^mu/+S^mu` smerujúci do pary;
4. dynamický exit/reheatingový zákon a jeho mechanizmus vypnutia.

**PASS:** nájde sa objekt, ktorý vyplní chýbajúce P1 pole a má presnú
provenienciu; potom sa P1.1 opraví iba dodatkom a otvorí sa presne určená P2
koľaj.  
**STOP:** nájdu sa iba slovné interpretácie, odvodené pozorovateľné čísla,
alebo voľné časy/funkcie bez vyššie uvedených polí; P1 STOP sa potvrdí.  
**Nesprávne čítanie:** samotné slovo „para“, „exit“, „jazva“ alebo „energia"
bez rovnice, jednotiek a ledgeru nie je PASS.

