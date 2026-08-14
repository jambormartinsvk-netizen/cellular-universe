# A2-K4 / C7.7c / K7a-J3 — preregistrácia stabilného výpočtu T-prime

**Dátum registrácie:** 2026-07-14, pred prvým behom J3  
**Nadväzuje na:** zlyhanie J2 pri dvojpresnom výpočte `ell = 2*(q+1)`

## Otázka

Odstráni priamy, algebraicky totožný výpočet

\[
\ell=\frac{B'}{B}=\frac{\text{denominator\_x}}{\text{denominator}}
\]

stratu platných cifier bez zmeny fyzikálnych rovníc a bez uvoľnenia tolerancií?

## Nemenný rozsah

- 80 desatinných miest cez `mpmath`.
- Povrchy: NID/deep, NID/shallow, NIV/deep, NIV/shallow.
- J3 nemení \(T\), \(T'\), background ani fyzikálne koeficienty; mení iba numerické vyhodnotenie \(\ell\).
- Žiadna ODE integrácia.
- Každý beh má vnútorný aj vonkajší časový limit.

## Brány pre každý povrch

1. všetky reportované hodnoty sú konečné;
2. relatívna chyba stabilného dvojpresného \(T'\) voči 80-cifernej analytickej referencii je \(<10^{-14}\);
3. relatívna chyba stabilného dvojpresného \(\ell\) voči 80-cifernej referencii je \(<10^{-14}\);
4. stabilná cesta musí mať menšiu chybu než stará cesta cez \(q+1\);
5. na hlbokom povrchu sa musí reprodukovať už pozorované zlyhanie starej cesty nad \(10^{-14}\), inak sa výsledok preverí ako možná zmena prostredia.

## Rozhodovanie

- **PASS J3:** všetky štyri povrchy splnia brány. Potom možno vytvoriť novú nemennú revíziu projektovaného Jacobiánu, ktorá použije priamo \(B'/B\).
- **STOP/REVIEW:** prvý neúspešný povrch zastaví postup. Najprv sa zdokumentuje príčina; ďalšie povrchy ani evolúcia sa nepreskakujú.
- Výsledok J3 sám o sebe nepridáva body hĺbky a neuzatvára C7.7c.

