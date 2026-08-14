# Povinná šablóna očakávaní pred spustením vedeckého skriptu

Dátum účinnosti: 2026-07-15  
Stav: záväzná šablóna podľa AR54

Tento dokument alebo jeho vyplnená kópia musí existovať **pred prvým fyzikálnym/numerickým behom** nového skriptu. Syntaxový `py_compile` a bezpečný CLI smoke-test môžu prebehnúť skôr, ale nesmú vytvárať vedecký výsledok.

## 1. Identita behu

- koľaj/podkoľaj:
- skript a plánované číslo:
- vedecká otázka:
- autoritatívny predchodca:
- zamrznuté vstupy, parametre, povrch/mód a checksumy:
- čo sa oproti predchodcovi smie zmeniť:
- čo sa nesmie zmeniť:

## 2. Typ očakávania

Pri každej veličine označiť práve jeden typ:

- `ANALYTIC`: hodnota alebo škálovanie odvodené pred výpočtom;
- `REGRESSION`: očakáva sa reprodukcia autoritatívneho staršieho behu;
- `EXPLORATORY`: stredná hodnota nie je známa; vopred sú známe iba invarianty, fyzikálne rozsahy alebo kill kritériá.

`EXPLORATORY` nesmie dostať vymyslenú strednú hodnotu len preto, aby tabuľka nebola prázdna.

## 3. Očakávané výsledky a prípustné odchýlky

| Veličina | Typ | Očakávaná hodnota/interval alebo trend | Zdroj očakávania | Prípustná odchýlka | Čo znamená prekročenie |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Musí sa rozlíšiť:

- numerická regresná tolerancia implementácie;
- fyzikálne prípustný interval;
- observačná neistota;
- iba diagnostické očakávanie bez PASS kreditu.

## 4. Rozhodovacia brána pred behom

- `PASS`:
- `ACCEPTABLE_WITHIN_TOLERANCE`:
- `REVIEW/UNCLOSED`:
- `DEAD` — iba fyzikálne kill kritérium:
- ktoré výsledky nesmú meniť skóre:

Blízkosť k očakávaniu sama o sebe nie je PASS. Musia prejsť aj nezávislé invarianty, constrainty a konvergencia.

## 5. Bezpečnosť a limity

- interný runtime limit:
- externý timeout:
- interval kontroly/checkpoint:
- RHS/iteration/safety cap:
- očakávaný runtime a pamäť:
- stav po timeoute: vždy `REVIEW/UNCLOSED`, nie fyzikálny FAIL.

## 6. Vyhodnotenie po behu

| Veličina | Očakávanie pred behom | Pozorovaná hodnota | Absolútna odchýlka | Relatívna/normalizovaná odchýlka | Vopred prípustná? | Verdikt |
|---|---|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |

Uviesť prvý zlyhaný nezávislý gate a oddeliť ho od tautologických alebo enforced monitorov.

## 7. Zmena očakávania po výsledku

Pôvodné očakávanie a prahy sa nikdy neprepisujú. Ak sa ukážu ako nesprávne alebo neúplné:

1. výsledok pôvodného behu zostane hodnotený podľa pôvodnej brány;
2. vytvorí sa datovaný dodatok s nezávislým fyzikálnym alebo numerickým dôvodom zmeny;
3. uvedie sa, či išlo o chybný vzorec, zlú normalizáciu, nesprávny dataset, neplatný asymptotický predpoklad alebo nový mechanizmus;
4. zmenená brána sa použije až na nový beh alebo novú podkoľaj;
5. post-hoc rozšírenie tolerancie bez nového dôkazu je zakázané.
