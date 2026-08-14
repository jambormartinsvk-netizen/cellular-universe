# Auditný dodatok: cieľ a vydanie v3.18 verzus v4.0

**Dátum:** 2026-07-13  
**Stav:** záväzný dodatok ku kapitolám 7 a 10 súboru `fyzikalny_audit_bunkoveho_priestoru_2026-07-13.md`  
**Nadväzuje na:** `../Questions/upresnenie_A0_verziovanie_2026-07-13.md`

## 1. Stav A0

**A0 je dokončené ako pravidlo vydávania.** Autor rozhodol, že už publikované verzie zostanú nemenné a každá ďalšia verzia publikovaná na Zenodo dostane changelog.

Mapa súborov, DOI a kontrolné súčty nie sú jednorazová úloha uzavretá iba týmto rozhodnutím. Sú opakovanou súčasťou checklistu každého budúceho vydania.

## 2. Odporúčané rozhodnutie o čísle verzie

**Odporúčanie auditora: najprv vydať v3.18 ako konsolidačnú a opravnú vedeckú verziu; v4.0 vyhradiť pre zmenu fundamentálneho modelu.**

Označenie v3.18 je vhodné, ak zostáva zachované jadro v3.17 a mení sa najmä:

- presnosť a primeranosť vedeckých tvrdení,
- konzistentnosť rovníc a označení,
- backgroundová kovariancia,
- oddelenie odvodených a podmienených predikcií,
- súlad dokumentov, kódu a tabuliek,
- reprodukovateľnosť a validačné testy.

Označenie **v4.0** je vhodné, ak nová verzia zmení vedecký význam jadra modelu aspoň v jednom z týchto bodov:

1. 3D Delaunayova sieť s globálnym tikom sa nahradí 4D kauzálnou štruktúrou alebo explicitným preferred-frame EFT.
2. Pribudne nová fundamentálna akcia alebo dynamické pravidlo, z ktorého sa nanovo odvodia (\delta), (C), gravitácia alebo vznik polí.
3. Zmení sa fyzikálny význam prenosu (Q), najmä rozhodnutie, či vzniká CDM, baryónová hmota alebo obe zložky.
4. Pôvod termálnych gravitónov, skalárnych porúch, exitu alebo reheatingu sa nahradí novým mechanizmom, ktorý mení centrálnu predikčnú logiku.
5. Nanovo sa odvodia a významne zmenia registrované hlavné predikcie, nie iba ich stav dôkazu alebo numerická presnosť.

Ak chce autor už v najbližšom vydaní tvrdiť, že tieto fundamentálne body sú vyriešené novou konštrukciou, vydanie má byť v4.0. Ak ich v3.18 ponechá ako otvorené podmienky a opraví rozsah tvrdení, nie je dôvod preskakovať na v4.0.

## 3. Cieľ verzie 3.18

**Cieľ v3.18:** vytvoriť jednoznačnú, reprodukovateľnú a fyzikálne poctivo označenú konsolidačnú verziu existujúceho modelu v3.17.

Cieľom v3.18 nemá byť vyhlásiť fundamentálnu teóriu za dokončenú. Má odstrániť známe vnútorné rozpory dokumentácie, zosúladiť rovnice, kód a tabuľky a presne oddeliť odvodené výsledky od podmienených hypotéz.

### 3.1 Minimálny obsah v3.18

1. Zapracovať opravenú backgroundovú časť A16 so zachovaním celkového tenzora energie a hybnosti. Ak poruchy ešte nie sú odvodené, výslovne napísať, že A16 uzatvára iba homogénne pozadie.
2. Jednoznačne rozdeliť baryóny, CDM, žiarenie a palivovú zložku a uviesť, ktorej zložke člen (Q^\mu) odovzdáva energiu.
3. Pri (n_s) oddeliť presný algebraický výsledok približne 0.9643 od historickej aproximácie prvého rádu 0.9656.
4. Hodnoty (r), (\Delta N_{\rm eff}) a (f_{\rm NL}) označiť ako podmienené, kým nie je uzavretý mechanizmus porúch, exitu a reheatingu.
5. Opraviť nesúlad lokálneho a publikovaného skriptu 09. Opraviť validačné nedostatky skriptov 06-10 vrátane používania (C=28), seedov, neistôt a jasného popisu aproximácií.
6. Prepracovať predikčnú tabuľku tak, aby každá položka mala pôvod, stav dôkazu, dátový test a operačnú kill condition.
7. Zapracovať iba opravené časti priečinka `Nespracovane` podľa verdiktov hlavného auditu. Pôvodné pracovné súbory ponechať ako internú stopu, nie ako automatickú súčasť teórie.
8. Zosúladiť slovenskú a anglickú verziu, README, hlavný dokument, metodiku, skripty a popularizačný dokument.
9. Priložiť changelog, manifest súborov, SHA-256 kontrolné súčty, verzie závislostí, validačné príkazy a očakávané výstupy.

### 3.2 Čo v3.18 nemusí uzavrieť

V3.18 môže ponechať otvorené:

- úplnú mikroskopickú akciu siete,
- dôkaz Lorentzovej invariancie alebo experimentálne uzavretý preferred-frame EFT,
- úplné gauge-invariantné poruchy a CLASS/CAMB implementáciu,
- odvodenie skalárneho a tenzorového spektra cez exit a reheating,
- plný spoločný kozmologický likelihood.

Tieto body však nesmú byť prezentované ako vyriešené. Verzia je vydavateľná aj s otvorenými otázkami, ak sú zreteľne označené a jej závery ich nepredpokladajú ako hotové výsledky.

## 4. Brány pripravenosti verzie 3.18

V3.18 je pripravená na vydanie až po splnení všetkých nasledujúcich brán:

| Brána | Kontrola | Kritérium úspechu |
|---|---|---|
| R0 Rozsah | Cieľ, zahrnuté a nezahrnuté témy | Jeden schválený scope dokument; počas release candidate sa nepridávajú nové fyzikálne tvrdenia |
| R1 Konzistentnosť | Rovnice, rozmery, znamienka, zachovanie energie a limity | Žiadny známy rozpor v rámci deklarovaného efektívneho modelu; otvorené fundamentálne otázky sú označené, nie vydávané za dôkaz |
| R2 Reprodukovateľnosť | Skripty, vstupy, seedy, závislosti a očakávané výstupy | Čistý beh reprodukuje všetky publikované numerické tabuľky v uvedenej tolerancii |
| R3 Zhodnosť dokumentov | SK/EN, README, hlavný text, predikcie a popularizácia | Rovnaké čísla, rovnaký stav dôkazu a funkčné relatívne odkazy |
| R4 Evidencia zmien | Changelog, manifest, SHA-256 a mapa verzií | Každý publikovaný súbor je v manifeste a každá zmena registrovaného tvrdenia je vysvetlená |
| R5 Nezávislá kontrola | Audit release candidate | Všetky P0 položky určené pre v3.18 sú opravené alebo explicitne presunuté do registra otvorených otázok bez presileného tvrdenia |

Formulácia „žiadny známy rozpor“ v R1 nie je dôkazom, že teória je fundamentálne správna. Znamená len, že vydaný text neprotirečí známym zákonom v rozsahu, ktorý sám deklaruje, a nezakrýva nevyriešené podmienky.

## 5. Kroky na vydanie verzie 3.18

1. Vytvoriť `SCOPE_v3.18.md` s jednou vetou cieľa, zoznamom povolených zmien a zoznamom tém presunutých do v4.0.
2. Vytvoriť čistý release-candidate snapshot oddelený od pracovného priečinka `Nespracovane`.
3. Nastaviť jednotné označenia: vedecký model `3.18`, samostatná verzia kódu, verzia sprievodcu a nové poradové číslo Zenodo záznamu. Tieto štyri čísla nezamieňať.
4. Dokončiť `CHANGELOG_v3.18.md`. Pri zmenených číslach a rovniciach uviesť starý stav, nový stav, dôvod a vplyv na závery.
5. Vygenerovať `MANIFEST_v3.18.sha256` zo všetkých súborov určených na publikovanie a uložiť informáciu o zdrojovom commite alebo identifikátore snapshotu.
6. Spustiť všetky validačné skripty v čistom prostredí. Uložiť príkazy, verzie závislostí, tolerancie a výsledný validačný protokol v Markdown súbore.
7. Skontrolovať SK/EN numerickú zhodu, bibliografiu, relatívne odkazy, názvy súborov, jednotky, tabuľky a tvrdenia v popularizačnom texte.
8. Uzavrieť register otázok: pri každej položke uviesť `uzavretá vo v3.18`, `otvorená pre v4.0` alebo `vyradená` s dôvodom.
9. Vykonať finálny audit nemenného release candidate podľa brán R0-R5. Po začatí tejto kontroly povoľovať iba opravy blokujúcich chýb; každá oprava vynúti opakovanie dotknutého testu a nový manifest.
10. Označiť zdrojový snapshot tagom, napríklad `theory-v3.18`, a zapísať dátum vydania.
11. Na Zenodo použiť funkciu vytvorenia **novej verzie** existujúceho záznamu. Nevymieňať súbory v publikovanej v2.
12. Do metadát vložiť číslo vedeckej verzie, stručný rozsah, väzbu na predchádzajúcu verziu a odporúčanú citáciu konkrétneho version DOI.
13. Po publikovaní stiahnuť súbory cez verejný záznam, prepočítať SHA-256, overiť DOI, licenciu, poradie súborov a funkčnosť odkazov.
14. Výsledný Zenodo snapshot zmraziť. Ak sa nájde chyba, zapísať erratum a opraviť ju v ďalšej verzii; publikované súbory spätne neprepisovať.

## 6. Definícia hotovej verzie 3.18

V3.18 je hotová vtedy, keď nový čitateľ dokáže z publikovaného balíka bez súkromných súborov:

1. určiť presné rovnice a rozsah efektívneho modelu,
2. rozlíšiť odvodené, podmienené a fenomenologicky fitované výsledky,
3. reprodukovať publikované numerické výstupy,
4. nájsť všetky kritické otvorené otázky,
5. identifikovať rozdiely oproti v3.17 a overiť integritu každého súboru.

## 7. Praktický verdikt

Najbližšie vydanie odporúčam označiť **v3.18**, ak bude jeho vedecký sľub znieť približne takto:

> Konsolidovaná a auditovaná verzia efektívneho modelu v3.17 s opravenou evidenciou tvrdení, reprodukovateľným kódom a explicitným registrom otvorených fundamentálnych podmienok.

Označenie **v4.0** odporúčam použiť až pre vydanie, ktoré prinesie novú fundamentálnu konštrukciu a nanovo odvodí podstatnú časť centrálnej predikčnej reťaze. Takéto oddelenie umožní vydať poctivú v3.18 bez čakania na úplné vyriešenie celej teórie a zároveň nezmenší význam budúcej v4.0.
