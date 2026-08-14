# Plán pripravenosti na výskumné financovanie EÚ

**Dátum:** 2026-07-17  
**Stav:** pracovný plán; nejde o žiadosť ani o tvrdenie, že existuje vhodná
aktuálna mikro-výzva.  
**Rozsah:** premeniť už vykonávanú nezávislú prácu na auditovateľný výskumný
projekt, ktorý sa dá v budúcnosti spojiť s vhodnou výzvou, hostiteľom alebo
konzorciom.

## Realistický východiskový bod

Živnosť môže byť použiteľnou právnou afiliáciou, ale konkrétna výzva vždy
určuje, či je oprávneným žiadateľom. Pri COST je samostatne zárobkovo činná
osoba uznaná ako afiliovaná, ak je jej status uznaný vnútroštátnym právom;
COST však financuje najmä spoluprácu a mobilitu, nie samotný výpočtový výskum.

V Horizon Europe môžu mať náklady práce podobu personálnych nákladov alebo,
podľa schémy, vopred dohodnutej dennej jednotkovej sadzby. To **neznamená**,
že každá živnosť automaticky dostane preplatený čas: právna forma, finančná
spôsobilosť a rozpočet musia prejsť pravidlami konkrétnej výzvy a grantovou
zmluvou.

Zdrojové pravidlá:

- [Horizon Europe: personnel unit costs](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/programmes/horizon/personnel-unit-costs/overview)
- [COST: čo financuje](https://www.cost.eu/what-do-we-fund/)
- [COST FAQ: afiliácia a živnosť](https://www.cost.eu/cost-actions/annotated-rules-qa/)

## Čo sa nemá meniť

1. Fyzikálne verdikty nesmú byť upravované podľa želaného výsledku alebo témy
   výzvy.
2. `PASS`, `REVIEW` a `STOP` zostávajú autoritatívne iba po internom audite;
   grantová žiadosť nemôže povýšiť hypotézu na výsledok.
3. Nezverejnené alebo neoverené predpovede sa nesmú prezentovať ako potvrdená
   nová fyzika.
4. Externý audit musí mať možnosť projekt vyvrátiť. To je vedecká sila návrhu,
   nie jeho slabina.

## Čo treba doplniť

| Oblasť | Minimálny stav pripravenosti | Konkrétny výstup |
|---|---|---|
| Výskumná otázka | Nehovoriť „dokážeme teóriu“, ale „testujeme, či diskrétny model prejde presne určenými bránami GR, CMB a rastu štruktúr“. | 2-stranový `Concept Note` |
| Pracovné balíky | Rozdeliť prácu na nezávisle hodnotiteľné balíky: formula provenance, lineárne poruchy, numerická reprodukovateľnosť, porovnanie s referenčným modelom, externý audit. | WP mapa s míľnikmi a STOP podmienkami |
| Merateľné výstupy | Každý balík má reprodukovateľný skript, vstup, hash, očakávaný výsledok, toleranciu, výsledný rozsudok. | register deliverables |
| Riadenie rizík | Oddeliť fyzikálny STOP, referenčný nesúlad, technický problém a otvorený REVIEW. | risk register s vlastníkmi a ďalším krokom |
| Nezávislosť | Aspoň dvaja externí odborníci: jeden fyzik/kozmológ, jeden numerik alebo metodológ. Ich úloha je kontrola, nie propagácia. | advisory/audit charter |
| Otvorená veda | Verejný repozitár, nemenné release, DOI, otvorené skripty, prostredie, licencie a Data Management Plan. | DMP v1 + release checklist |
| Etika a integrita | Sebahodnotenie: bez ľudských subjektov a osobných dát, ale s jasným postupom pre autorstvo, konflikty záujmov, správu chýb a opravy. | integrity & ethics note |
| Rozpočet a čas | Evidovať hodiny podľa pracovného balíka, úlohy a výstupu; oddeliť čas autora, externý audit, cloud/výpočty, publikovanie a cestovné. | timesheet + budget assumptions |
| Partnerstvo | Hostiteľ z univerzity/SAV alebo odborné SME; pri väčších Horizon výzvach aj zahraniční partneri. | one-page partner brief |
| Dopad a komunikácia | Primárny dopad nie je „nahradiť ΛCDM“, ale otvorený, opakovateľný spôsob testovania odvodených kozmologických hypotéz. | communication/exploitation note |

## Navrhovaná štruktúra projektu

```text
WP1  Formula provenance a k-nezávislý background
     -> merateľný výsledok: preverený formula ledger + nulový limit

WP2  Lineárne poruchy a konzervácia
     -> merateľný výsledok: constrainty, gauge testy, stabilita

WP3  Numerická reprodukovateľnosť
     -> merateľný výsledok: nezávislá implementácia, konvergencia, hashované vstupy

WP4  Observačné falzifikačné brány
     -> merateľný výsledok: porovnanie s CMB/BBN/rastom; aj negatívny výsledok je validný

WP5  Nezávislý audit, otvorené vydanie a opravy
     -> merateľný výsledok: externé posudky, odpovede, Zenodo/Git release
```

Ak WP1 alebo WP2 skončí fyzikálnym `STOP`, projekt stále splnil cieľ: vytvoril
reprodukovateľný falzifikačný výsledok. To je pre hodnotiteľa oveľa dôveryhodnejšie
než projekt, ktorý pripúšťa iba úspech.

## Evidencia tvojho času odteraz

Odporúčaný minimálny zápis pre každú relevantnú pracovnú reláciu:

| Dátum | WP/koľaj | Činnosť | Hodiny | Výstup/odkaz | Stav |
|---|---|---:|---:|---|---|
| YYYY-MM-DD | WP1 / A2-K4 | napr. formula audit | 1.5 | hashovaný MD alebo výsledok | dokončené/review |

Nezapisovať spätne odhadnuté hodiny ako účtovný doklad pre grant. Dá sa však
transparentne uviesť ako historický vlastný vklad. Pre budúci grant viesť čas
od jeho začiatku podľa pravidiel danej zmluvy a účtovníctva.

## Postup v troch horizontoch

### Teraz — bez čakania na výzvu

1. Udržať existujúci systém koľají, externých auditných balíkov a hashov.
2. Založiť timesheet vlastného času a tabuľku priamych nákladov.
3. Vytvoriť stručný `Concept Note` bez veľkých tvrdení: problém, metóda,
   falzifikačné brány, stav, rozpočet, požadovaná expertíza.
4. Dokončiť najkritickejšie externé audity, aby projekt nestál iba na vlastnom
   posúdení autora.

### 3–6 mesiacov — vedecká dôveryhodnosť

1. Nájsť hostiteľa alebo spoluautora so skúsenosťou v kozmológii/numerike.
2. Urobiť nezávislú reprodukciu aspoň jedného rozhodujúceho výpočtu.
3. Pripraviť stručný Data Management Plan a verejný release proces. Horizon
   Europe vyžaduje, aby príjemcovia vytvorili a udržiavali DMP a sprístupnili
   výstupy potrebné na overenie publikovaných záverov.
4. Prejsť konzultáciou Národného kontaktného bodu Horizon Europe v CVTI SR.

### Keď sa objaví vhodná výzva

1. Najprv overiť tematickú zhodu a oprávnenosť; netlačiť projekt do výzvy,
   ktorá nevie financovať základný výskum.
2. Prispôsobiť formu, nie fyzikálny záver: WP, míľniky, rozpočet, partnerov,
   otvorenú vedu a dopad.
3. Urobiť povinné etické self-assessment a realistický plán rizík. Horizon
   Europe vyžaduje etické sebahodnotenie pri každom návrhu.

## Reálne cesty EÚ

- **COST:** najnižšia vstupná bariéra na získanie siete, odborných kontaktov,
  mobility a neskôr konzorcia. Nie je náhradou mzdy ani výpočtového rozpočtu.
- **WIDERA / ERA:** Slovensko patrí medzi krajiny, pre ktoré Horizon Europe
  explicitne podporuje budovanie výskumnej kapacity a prístup k excelentnosti;
  spravidla však cez inštitúcie a partnerstvá.
- **Horizon Europe RIA/CSA:** až po vytvorení tímu a jasného verejného prínosu.
  Väčšina výziev vyžaduje najmenej tri organizácie z troch krajín.
- **MSCA/ERC:** možné len pri splnení osobitných kariérnych a hostiteľských
  podmienok; nie sú plánom na rýchle pokrytie malých nákladov.

Zdrojové pravidlá:

- [WIDERA 2026–2027](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/widening-participation-and-spreading-excellence_en)
- [Otvorená veda a DMP](https://rea.ec.europa.eu/open-science_en)
- [Etické hodnotenie](https://research-and-innovation.ec.europa.eu/document/download/bc9897a4-7053-45ae-ac35-5b3d3dc26f21_en?filename=ec_rtd_ethics-appraisal-procedure.pdf)
- [Kto môže žiadať v Horizon Europe](https://rea.ec.europa.eu/horizon-europe-who-should-apply_en)

## Prvý externý krok

Národná kancelária Horizon Europe sídli v CVTI SR. Kontakt `horizont@cvtisr.sk`
vie bezplatne usmerniť oprávnenosť, NCP a partner search; kontakt nie je
záväzkom podať žiadosť. Pred stretnutím stačí poslať `Concept Note`, nie celý
archív teórie.

## Rozhodnutie

**Odporúčanie:** budovať pripravenosť popri audite A2-K4, nie namiesto neho.
Najbližší zmysluplný administratívny výstup je `Concept Note` a evidencia času;
žiadosť o veľký grant má zmysel až s nezávislým odborným partnerom a aspoň
jedným uzavretým, reprodukovateľným výsledkom.
