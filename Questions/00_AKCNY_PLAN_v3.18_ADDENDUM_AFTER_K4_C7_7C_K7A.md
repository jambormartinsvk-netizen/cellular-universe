# Akčný plán v3.18 — po PASS C7.7c-K7a

**Dátum:** 2026-07-14  
**Aktívna koľaj:** A2-K4  
**Jemná hĺbka:** `66.5/100`  
**Stav:** živá; K7a PASS, C7.7c otvorená

## Dokončené

1. K7a.1 — odvodenie `D'` z kontinuitných rovníc a backgroundových derivácií.
2. K7a.2 — odvodenie `M'` z Eulerových rovníc a backgroundových derivácií.
3. K7a.3 — úplná transformácia `(T' + T A_y) T^-1`.
4. K7a.4 — nulový limit, znamienka, invertibilita a podmienenosť na štyroch plochách.
5. J1/J2 — zdokumentované numerické zlyhania konečnej diferencie a `q+1`.
6. J3/J4b — vysokopresná oprava a zložený PASS na NID/NIV deep/shallow.
7. Skript 163 — zachovaný ako mŕtva parserová podkoľaj s presným dôvodom.

## Bezprostredný postup

1. **K7b.1:** vytvoriť 80-ciferné počiatočné `D,M` z registrovaných NID/NIV Puiseuxových koeficientov bez druhového double odčítania.
2. **K7b.2:** overiť rekonštrukciu `delta_fs,U_fs` a identitu fyzikálnych zdrojov proti autoritatívnemu stavu.
3. **K7b.3:** overiť Einsteinove `00` a `0i` constrainty (`h_x=3D+2s^2 eta`, `eta_x=M`) a príslušné znamienka na štyroch plochách.
4. **K7b.4:** porovnať derivácie počiatočnej série s projektovaným RHS koeficient po koeficiente; nulový alebo pod-roundoff signál sa nesmie hodnotiť obyčajnou relatívnou chybou.
5. **K7b.5:** vydať PASS/REVIEW bez ODE a bez bodov.
6. **K7c až po PASS K7b:** preregistrovať prvý krátky, segmentovaný projektovaný evolučný test s vnútorným aj vonkajším limitom.

## Skórovací stav

K7a nepridáva body, lebo ešte nepreukázala evolučný pokrok. Najbližšie možné zvýšenie hĺbky nastane až pri skutočne úspešnej evolučnej bráne po K7b.

