# Pravidlo archivácie mŕtvych koľají

**Platnosť od:** 2026-07-13  
**Stav:** trvalé metodické pravidlo

## 1. Základné pravidlo

Mŕtva koľaj sa nikdy nemaže. Je to zdokumentovaný negatívny výsledok, ktorý chráni projekt pred opakovaním rovnakej chyby.

Označenie **MŔTVA** sa vzťahuje na presne definovanú formuláciu a jej testovaný rozsah. Neznamená automaticky, že je mŕtva každá budúca hypotéza s podobným názvom.

## 2. Povinný archívny balík

Pred definitívnym označením koľaje za mŕtvu musí zostať zachované:

1. **identifikátor koľaje** a jej presné znenie;
2. **dátum otvorenia a uzavretia**;
3. **predpoklady a rozsah platnosti**;
4. **test alebo fyzikálny zákon**, cez ktorý neprešla;
5. **presný dôvod smrti**, nie iba výsledné slovo `MŔTVA`;
6. **vstupné parametre, jednotky a zdroje dát**;
7. **všetky použité výpočtové skripty** v `scripts`;
8. **surové alebo úplne reprodukovateľné výstupy**;
9. **verzia prostredia a tolerancie**, ak mohli ovplyvniť výsledok;
10. **SHA-256** hypotézy, skriptu a zmrazeného výstupu pri vydaní;
11. **rozsah verdiktu** — čo presne zomrelo a čo ním nebolo testované;
12. **podmienka znovuotvorenia**.

Ak bol verdikt analytický a nepotreboval výpočet, dokument musí výslovne uviesť `výpočtový skript: NEBOL POTREBNÝ` a obsahovať úplnú analytickú argumentáciu. Skript sa nevytvára iba naoko.

## 3. Pravidlá pre skripty a výpočty

- Skript, ktorý prispel k smrti koľaje, sa ponechá v `scripts` pod stabilným názvom.
- Oprava chyby pôvodný skript ticho nenahradí. Vznikne nová verzia alebo nový skript a erratum vysvetlí rozdiel.
- Skript musí mať v hlavičke účel, vstupy, jednotky, rozsah a očakávané výstupy.
- Náhodné simulácie musia ukladať seed alebo pravidlo generovania seedov.
- Externé dáta musia mať zdroj, verziu a dátum prístupu.
- Výstup použitý vo verdikte sa musí dať reprodukovať jedným zdokumentovaným príkazom.
- Ak numerika iba reprodukuje tabuľku, ale dôvod smrti je fyzikálny alebo štatistický, obe vrstvy sa musia uviesť oddelene.

## 4. Stav po smrti koľaje

Mŕtva koľaj sa označí:

- `ARCHIVOVANÁ — NEOTVÁRAŤ BEZ NOVEJ INFORMÁCIE`;
- odkazom na finálny audit;
- odkazom na skripty a výstupy;
- krátkym dôvodom smrti;
- podmienkou, za ktorej možno založiť novú koľaj.

Mŕtva koľaj sa nevracia do stavu `PREŽÍVA`. Ak pribudne nový mechanizmus, nový nositeľ, iná rovnica alebo nové dáta, založí sa **nová koľaj** s novým identifikátorom a odkazom na pôvodnú mŕtvu koľaj.

## 5. Kedy je znovuotvorenie zakázané

Nestačí:

- premenovať ten istý parameter;
- zmeniť iba cieľovú hodnotu;
- rozšíriť grid bez zmeny fyziky;
- použiť iný optimalizátor na tom istom neplatnom likelihoode;
- odstrániť nepohodlný dataset;
- zaokrúhliť výsledok inak;
- tvrdiť, že neúspech bol iba aproximácia, bez novej rovnice alebo dôkazu.

## 6. Legitímne založenie novej koľaje

Nová koľaj môže vzniknúť, ak je prítomné aspoň jedno:

- nový kovariantne uzavretý mechanizmus;
- nový fyzikálny nositeľ s vybilancovanou energiou a hybnosťou;
- opravená preukázaná chyba vo výpočte;
- nové nezávislé dáta, ktoré menia testovaný rozsah;
- nové odvodenie meniace konkrétny predpoklad, ktorý spôsobil smrť;
- presnejšia teória, ktorej nulový limit reprodukuje starú koľaj a vysvetľuje jej zlyhanie.

Nový dokument musí obsahovať sekciu `Rozdiel oproti mŕtvej koľaji`.

## 7. Minimálna šablóna finálneho záznamu

```text
ID koľaje:
Presná hypotéza:
Stav: MŔTVA — ARCHIVOVANÁ
Dátum verdiktu:
Testovaný rozsah:
Testy/fyzikálne zákony:
Dôvod smrti:
Čo verdikt nezabíja:
Vstupy a dáta:
Skripty:
Reprodukčný príkaz:
Výstupy:
Kontrolné súčty pri vydaní:
Podmienka novej koľaje:
Súvisiaci audit:
```

