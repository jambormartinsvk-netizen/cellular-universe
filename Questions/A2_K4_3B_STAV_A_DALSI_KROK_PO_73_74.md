# A2-K4.3b — stav a ďalší krok po skriptoch 73/74

**Stav:** `NEUZAVRETÁ, NIE MŔTVA`  
**Skóre K4:** `60/100`  
**Aktívny pracovný balík:** `K4.3b-RG`

## K4.3b-RG — poradie práce

1. **RG1 — voľba gauge:** použiť regular total-matter alebo všeobecnú
   synchronous gauge, ktorá po zapnutí momentum transferu nevynucuje
   neplatné trvalé `theta_c=0`.
2. **RG2 — vedúce seed vectors:** AD, CDI, BI, collective-FS density,
   internal nu-steam density, collective-FS velocity, internal nu-steam
   velocity.
3. **RG3 — Frobeniove rady:** vypočítať koeficienty do rádu, v ktorom sa
   súčasne uzavrú `00`, `0i`, slip a `ij`; zahrnúť `lambda/E=O(a^2)`.
4. **RG4 — konečný Newtonov štart:** mapovať až pri `k tau > 0`, nikdy nie
   priamym dosadením singulárneho velocity seedu do K4.1 premennej `U`.
5. **RG5 — reziduálny skript:** pre každý mód a dve štartové hĺbky overiť
   všetky štyri Einsteinove rovnice, energy/momentum ledger a očakávaný rád
   rezídua.
6. **RG6 — rozsudok:** PASS otvorí K4.3c; invariantná divergencia alebo
   nemožnosť spoločných constraintov vydá nový presne ohraničený dôvod
   smrti. TIMEOUT zostáva neuzavretý.

## Limity

- symbolický skript: interne najviac 30 s, externe 40 s;
- numerický reziduálny skript: interne najviac 50 s, externe 60 s;
- polling najviac 10 s;
- každý skript a výstup zostáva v `scripts`, aj keby koľaj neskôr zomrela.

