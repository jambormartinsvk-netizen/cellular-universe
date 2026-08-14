# A2-K4 / C7.7c / K7b — preregistrácia koeficientovej a constraintovej brány

**Dátum registrácie:** 2026-07-14  
**Predpoklad:** K7a-J4b PASS na všetkých štyroch plochách  
**Rozsah:** bez ODE evolúcie a bez zmeny skóre

## Otázka

Sú projektované počiatočné stavy `D,M` pre NID a NIV skutočne koeficientovo konzistentné s registrovanými Puiseuxovými radmi a Einsteinovými constraintmi, alebo K7a iba ukázala správnu maticovú transformáciu mimo konkrétnych seedov?

## Povinné vstupy

- autoritatívny stav zo skriptu 146;
- tie isté konvencie, poradie 13 komponentov a parametre ako K7a;
- NID/deep, NID/shallow, NIV/deep, NIV/shallow;
- 80-ciferná referencia pre kompenzované súčty a ich derivácie;
- priamy bezpečný výpočet `ell=denominator_x/denominator`.

## Brány

1. `D,M` sa vytvoria z registrovaných analytických koeficientov vo vysokej presnosti, nie z numericky vyrušeného double súčtu.
2. Rekonštrukcia `delta_fs,U_fs` je konečná a zhodná s autoritatívnym stavom v škálovo primeranej norme.
3. `00` identita `h_x = 3D + 2s^2 eta` a `0i` identita `eta_x = M` majú správne znamienka a prejdú absolútnou aj škálovanou kontrolou.
4. Explicitný projektovaný RHS a derivácia analytickej série sa porovnajú po komponentoch.
5. Pre signál pod forward-roundoff hranicou je rozhodujúca absolútna/high-precision kontrola; relatívna chyba delená takmer nulou nesmie zabiť koľaj.
6. Nulové koeficienty sa musia rozlíšiť od neaktívneho alebo nevyhodnoteného komponentu.
7. Všetky hodnoty, vstupné mená a povrchy sú konečné a jednoznačne reportované.
8. Každý skript má povinný vnútorný aj vonkajší časový limit.

## Rozhodovanie

- **PASS K7b:** všetky štyri povrchy prejdú všetkými bránami.
- **REVIEW:** prvý neúspech zastaví postup a musí sa zapísať pred ďalšou podkoľajou.
- **Smrť K4:** iba fyzikálny/rovnicový rozpor, ktorý nemožno odstrániť bez zmeny mechanizmu; numerický alebo parserový neúspech sám osebe nestačí.
- ODE evolúcia a zvýšenie hĺbky sú zakázané pred PASS K7b.

