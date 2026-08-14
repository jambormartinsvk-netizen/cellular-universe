# Metodika koľají problémov a stavov

**Zavedené:** 2026-07-13  
**Platnosť:** pracovná príprava teórie v3.18 a ďalších verzií  
**Rozhodnutie autora:** ak má problém viac fyzikálne odlišných riešení, riešenia sa nesmú zlúčiť ani vybrať bez testu; založia sa samostatné koľaje K1 až Kn.

## 1. Účel

Metodika bráni trom chybám:

1. tichému výberu možnosti iba preto, že vyzerá priaznivo,
2. miešaniu predpokladov viacerých možností do jedného nefalzifikovateľného modelu,
3. zabudnutiu slepých vetiev a opakovaniu už zamietnutých pokusov.

Každý problém s viac než jedným fyzikálne odlišným riešením dostane vlastný Markdown dokument. Dokument obsahuje stav problému, zoznam koľají, poradie testovania, vopred určené testy a podmienky smrti.

## 2. Hierarchia

- **Problém P:** presne formulovaná otázka, ktorú treba uzavrieť.
- **Vetva B:** rodina riešení so spoločným fundamentálnym predpokladom.
- **Koľaj K1 až Kn:** konkrétna fyzikálna možnosť v danej vetve.
- **Test T1 až Tn:** kontrola zákona, matematiky, numeriky alebo dát.
- **Stena W1 až Wn:** vopred definovaná podmienka, pri ktorej koľaj nemôže pokračovať.

Identifikátor koľaje musí obsahovať problém, napríklad `A1-K1`, aby sa nezamieňal s koľajou K1 iného problému.

Ak zomrú všetky koľaje jednej vetvy, vetva je mŕtva. Ak zomrú všetky fyzikálne prípustné vetvy problému, problém nemá riešenie v danom fundamente. Vtedy sa musí zmeniť fundament, znížiť rozsah tvrdenia alebo ukončiť príslušná časť teórie.

## 3. Povinná osnova problémového dokumentu

Každý dokument musí obsahovať:

1. presnú otázku a dôvod, prečo je fyzikálne dôležitá,
2. nemenné zákony a pozorovania, ktoré musí spĺňať každá koľaj,
3. úplný zoznam fyzikálne odlišných tried možností,
4. poradie testovania a dôvod poradia,
5. predpoklady každej koľaje,
6. testy a ich prah úspechu,
7. steny a kill conditions určené pred rozhodujúcim výpočtom,
8. dátum, vstupy, kód, výsledky a neistoty každého behu,
9. aktuálny stav koľaje,
10. rozhodnutie, čo sa testuje ďalej.

Ak sa počas práce objaví nová fyzikálne odlišná možnosť, pridá sa ako nová koľaj. Nesmie sa spätne vydávať za súčasť starej koľaje.

## 4. Stavy koľaje

| Stav | Význam |
|---|---|
| `NAVRHNUTÁ` | Možnosť je pomenovaná, ale ešte nemá úplný testovací plán |
| `ČAKÁ` | Testovací plán existuje, no testovanie ešte nezačalo |
| `AKTÍVNA` | Práve prebieha jej najbližší test |
| `PREŽÍVA` | Prešla doterajšími testami, ale nie všetkými bránami |
| `NA STENE` | Objavil sa potenciálne smrteľný rozpor; musí sa potvrdiť kontrolným výpočtom alebo nezávislou kontrolou |
| `MŔTVA` | Vopred registrovaná kill condition bola potvrdená a výsledok je reprodukovateľný |
| `VYBRANÁ` | Prešla všetkými testami požadovanými pre cieľovú verziu a bola zapracovaná |
| `ZMRAZENÁ` | Stav a obsah koľaje boli publikované; meniť ich možno iba v novej verzii s changelogom |

Koľaj sa nesmie označiť `MŔTVA` iba preto, že prvý program spadol, solver nekonvergoval alebo výsledok nezodpovedal očakávaniu. Najprv musí prejsť kontrola implementácie, jednotiek, konvencií, numerickej konvergencie a referenčného modelu.

## 5. Čo sa považuje za stenu

Koľaj narazila na stenu, ak nastane aspoň jedna vopred registrovaná podmienka:

1. porušenie overeného fyzikálneho zákona v deklarovanom rozsahu,
2. vnútorný matematický rozpor alebo neexistencia riešenia,
3. ghost, gradientová alebo nekontrolovaná superhorizontová nestabilita,
4. záporná fyzikálna hustota alebo pravdepodobnosť bez prípustnej interpretácie,
5. reprodukovateľný rozpor s dátami nad vopred zvoleným prahom,
6. zlyhanie predikcie na vlastnej registrovanej kill condition,
7. potreba dodatočného voľného parametra alebo mechanizmu, ktorý ruší definíciu danej koľaje,
8. redukcia na už mŕtvu koľaj po presnom matematickom zobrazení.

Nový pomocný parameter sa nesmie pridať iba na záchranu koľaje. Taká zmena vytvára novú koľaj s novým identifikátorom.

## 6. Poradie testovania

Ako prvá sa testuje koľaj s najvyššou predbežnou šancou na úspech. Poradie sa určuje pred rozhodujúcimi testami podľa:

1. najmenšieho počtu nových predpokladov a parametrov,
2. zhody s už publikovaným jadrom a existujúcim kódom,
3. zjavnej kompatibility s overenými zákonmi,
4. kompatibility s doterajšími dátami,
5. jasnej falzifikovateľnosti,
6. možnosti vykonať rozhodujúci test.

Poradie nie je dôkaz ani zvýhodnenie vo výslednom verdikte. Menej sľubná koľaj môže prežiť a prvá koľaj môže zomrieť.

## 7. Minimálna testovacia pyramída

Každá koľaj postupuje od lacnejších a tvrdších kontrol k drahším:

1. **T0 Definícia:** jednoznačné veličiny, jednotky, znamienka a rozsah.
2. **T1 Zákony:** kovariancia, zachovanie, kauzalita, termodynamika a príslušné symetrie.
3. **T2 Matematika:** existencia, kladnosť, stabilita a správne limity.
4. **T3 Kód:** referenčný limit, konvergencia, viac implementácií alebo analytická kontrola.
5. **T4 Interné dáta:** reprodukcia už registrovaných hodnôt projektu.
6. **T5 Verejné dáta:** rovnaký likelihood, priory a nuisance parametre ako referenčný model.
7. **T6 Predikcia:** nový test mimo dát použitých na nastavenie koľaje.

Koľaj môže byť `PREŽÍVA` po nižších stupňoch, ale `VYBRANÁ` iba po stupňoch potrebných pre tvrdenia cieľovej verzie.

## 8. Pravidlá evidencie

1. Každý výsledok sa zapisuje do Markdownu aj vtedy, keď je negatívny.
2. Číselný výsledok musí uvádzať kód, vstupy, verziu prostredia, toleranciu a dátum.
3. Pri zmene testu sa zachová pôvodný test a pridá nový; prah sa spätne neposúva.
4. Mŕtva koľaj zostáva v registri s príčinou smrti.
5. Oživenie mŕtvej koľaje vyžaduje novú evidenciu, nový variant koľaje a vysvetlenie, prečo pôvodná stena už neplatí.
6. Publikované stavy koľají sú nemenné. Aktualizácia patrí do novej verzie a changelogu.

## 9. Pravidlo pre vydanie v3.18

V3.18 môže použiť koľaj, ktorá prešla všetkými testami potrebnými pre presne obmedzené tvrdenie v3.18. Nemusí čakať na fundamentálne testy plánované pre v4.0, ale musí tieto testy uviesť ako otvorené a nesmie predstierať ich výsledok.

Ak koľaj prešla iba backgroundovou kontrolou, v3.18 ju môže použiť iba ako backgroundový efektívny model. Nesmie z nej bez ďalších testov vyvodzovať správnosť porúch, CMB spektier alebo fundamentálnej mikrofyziky.
