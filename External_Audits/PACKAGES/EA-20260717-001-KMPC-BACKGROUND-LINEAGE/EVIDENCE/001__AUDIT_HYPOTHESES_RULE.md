# Záväzné pravidlo fyzikálneho auditu: vstupy autora sú hypotézy

**Platnosť od:** 2026-07-13  
**Rozsah:** všetky budúce audity Bunkového priestoru

## 1. Základné pravidlo

Každé fyzikálne tvrdenie, číslo, mechanizmus, interpretácia alebo výsledková tabuľka dodaná autorom sa pri vstupe označí ako **HYPOTÉZA**. Samotné dodanie tvrdenia nie je dôkaz ani výsledok teórie.

Audit musí oddeliť najmenej štyri úrovne:

1. **aritmetická reprodukcia** — či rovnaké rovnice a vstupy dajú rovnaké čísla;
2. **matematická konzistencia** — rozmery, znamienka, normalizácia, konvergencia;
3. **fyzikálna konzistencia** — lokálna a covariantná konzervácia, stabilita, kauzalita a známe zákony;
4. **observačná životaschopnosť** — porovnanie s pôvodnými dátami a ich likelihood, nie iba s vybranými centrálnymi hodnotami.

Prechod nižšou úrovňou neznamená automatický prechod vyššou úrovňou.

## 2. Povolené konečné stavy

Každá konkrétna hypotéza musí dostať jeden z dvoch konečných stavov:

- **PREŽÍVA — N/100:** nebol nájdený rozpor s potvrdeným zákonom alebo rozhodujúcim rozsahom, ale hodnotenie vyjadruje stupeň pripravenosti;
- **MŔTVA:** tvrdenie je matematicky chybné, porušuje potvrdený zákon, je mimo záväzného experimentálneho rozsahu alebo používa neplatnú štatistickú interpretáciu.

Ak zomrie konkrétna implementácia, širšia trieda mechanizmov môže prežiť ako nová koľaj. Musí však dostať nový identifikátor; nesmie sa spätne tvrdiť, že pôvodná implementácia prešla.

## 3. Hodnotenie prežívajúcich koľají

| Oblasť | Maximum |
|---|---:|
| Reprodukovateľnosť a numerická kontrola | 20 |
| Konzervácia a súlad s potvrdenými zákonmi | 25 |
| Stabilita, kauzalita a dobre položené perturbácie | 20 |
| Zhoda s observačnými dátami cez platnú likelihood | 25 |
| Vnútorné odvodenie bez post-data fitu | 10 |
| **Spolu** | **100** |

Skóre nie je pravdepodobnosť pravdivosti. Je to auditná pripravenosť koľaje.

## 4. Štatistické pravidlá

Za platné zlepšenie fitu sa nesmie označiť:

- súčet rezíduí bez známych kovariancií;
- skóre, ktoré neobsahuje veličinu, o ktorej sa tvrdí, že sa zlepšila;
- trafenie centrálnej hodnoty parametrom vybraným po prezretí dát;
- porovnanie modelov bez započítania nových parametrov a look-elsewhere efektu;
- porovnanie odvodených parametrov namiesto likelihood pôvodných dát.

Výrazy „presný fit“, „dokonalá zhoda“, „vyriešenie napätia“ a „zlepšenie χ²“ sú povolené až po plnom dátovom výpočte.

## 5. Reprodukovateľnosť

Každý použitý výpočet musí mať skript v `scripts`, Markdown protokol so vstupmi a výstupmi a jasné obmedzenie interpretácie. Neúspešné alebo prekonané skripty sa zachovajú ako auditná stopa.

Publikované verzie Zenodo sa neprepisujú. Oprava patrí do novej verzie a changelogu.

