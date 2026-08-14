# Q8 — tri roly domény I: problém, stav a koľaje

**Dátum založenia:** 2026-07-13  
**Stav vetvy:** OTVORENÁ  
**Pracovné roly:** trvalá jazva/pamäť, kolaps, šíp času

## 1. Problém

Teória slovne pripisuje doméne I tri roly:

1. fyzicky trvalá jazva alebo záznam v sieti;
2. kolaps kvantového stavu na jeden výsledok;
3. mikroskopický pôvod termodynamického šípu času.

Nie je dokázané, že tieto tri tvrdenia opisujú jeden mechanizmus. Na uzavretie Q8 treba definovať stavový priestor, evolučnú mapu, preferovanú bázu, pravdepodobnosť výsledku, energetickú bilanciu a entropickú veličinu.

## 2. Spoločné testy Q8-T0

Každá koľaj musí odpovedať:

- je evolúcia lineárna a úplne pozitívna, alebo nelineárna/stochastická;
- zachováva stopu a pravdepodobnosť;
- neumožňuje nadsvetelné signalizovanie;
- vyberá iba bázu, alebo aj jeden výsledok;
- odvodzuje Bornovo pravidlo, alebo ho vkladá;
- kde sa ukladá energia a informácia;
- ktorá entropia monotónne rastie a za akých počiatočných podmienok.

## 3. K1 — otvorený systém: dekoherencia plus stabilný záznam

### Hypotéza

Doména I je prostredie alebo absorpčný register. Interakcia potláča koherencie v lokálne vybranej báze a korelácia sa zapíše do stabilnej jazvy.

### Vykonaný test

`scripts/15_script_Q8_K1_decoherence_record_channel_audit.py` testuje dephasing kvbitového kanála.

| Test | Výsledok |
|---|---|
| Krausova úplnosť, zachovanie stopy | PASS |
| Hermitovskosť a pozitivita | PASS |
| Potlačenie mimodiagonálnych členov | PASS |
| Nárast entropie `|+>` pri úplnom dephasingu na 1 bit | PASS |
| Lokálne pôsobenie bez zmeny vzdialeného redukovaného stavu | PASS |
| Výber jedného objektívneho výsledku | **NOT PROVIDED** |
| Bornovo pravidlo pre jednu udalosť | **NOT PROVIDED** |
| Mikroskopická identifikácia s doménou I | **NOT TESTED** |

Úplne dekoherovaný stav je zmes s vlastnými číslami `(0,5; 0,5)`, čistotou `0,5` a hodnosťou `2`. Nie je to jeden výsledok.

### Stav

**PREŽÍVA pre stabilný záznam, efektívnu klasickosť a coarse-grained šíp.**  
**NARÁŽA NA STENU**, ak Q8 vyžaduje doslovný objektívny kolaps.

## 4. K2 — objektívny stochastický kolaps

### Hypotéza

Doména I indukuje GRW/CSL-podobný stochastický a nelineárny člen, ktorý skutočne vyberie jeden výsledok.

### Výhoda

Jedna dynamika môže priamo spojiť vznik jazvy s objektívnou udalosťou a časovou asymetriou.

### Riziká a testy

- parameter rýchlosti a lokalizačnej škály nesmie byť ďalší neodvodený fit;
- treba preveriť ohrev/porušenie energie;
- treba zabrániť nadsvetelnému signalizovaniu;
- model musí prežiť interferometriu, spontánne žiarenie a kozmologické limity;
- Bornovo pravidlo musí nasledovať zo šumu alebo byť jasne priznaný axióm.

### Stav

**PREŽÍVA FORMÁLNE; VYSOKÉ EXPERIMENTÁLNE A PARAMETRICKÉ RIZIKO.** Ide druhá iba vtedy, ak autor trvá na objektívnom kolapse.

## 5. K3 — unitárne dekoherentné histórie bez fyzického kolapsu

### Hypotéza

Celok sa vyvíja unitárne. Doména I je robustný záznam jednej dekoherentnej histórie; slovo „kolaps“ označuje aktualizáciu podmieneného opisu, nie nový fyzikálny proces.

### Výhoda

Nevyžaduje nelineárnu dynamiku ani energeticky problematický kolaps.

### Stena

Nevyberá jednu ontologicky privilegovanú vetvu bez ďalšej interpretačnej podmienky. Ak teória tvrdí objektívny jednosvetový kolaps, K3 túto požiadavku nesplní.

### Stav

**PREŽÍVA, AK SA ZMENÍ TVRDENIE TEÓRIE NA EFEKTÍVNY KOLAPS.**

## 6. K4 — absorpčný sieťový prechod a superselekcia

### Hypotéza

Doména I je absorpčný stav lokálnej Markovovej alebo kvantovej siete. Po prechode sa amplitúdy medzi sektorom bez jazvy a sektorom s jazvou dynamicky odpoja.

### Povinné testy

- explicitný lokálny generátor/Lindbladián alebo unitárne rozšírenie;
- dôkaz úplnej pozitivity a lokálnosti;
- vznik preferovanej bázy zo sieťovej väzby;
- jednoznačné rozlíšenie absorpcie záznamu od výberu výsledku;
- entropická veta pre určenú coarse-graining mapu.

### Stav

**PREŽÍVA AKO NAJPRIAMEJŠIA SIEŤOVÁ MIKROFYZIKA; ZATIAĽ BEZ OPERÁTORA.**

## 7. Rozhodovací bod po K1

Autor musí určiť význam slova „kolaps“:

- ak stačí efektívna dekoherencia a stabilná klasická stopa, pokračuje **K1** a K3;
- ak ide o doslovný objektívny výber jedného výsledku, K1 sama nestačí a pokračuje **K2** alebo K4 s dodatočným výberovým pravidlom.

Kým toto nie je rozhodnuté, tvrdenie „tri roly = jeden mechanizmus“ zostáva hypotézou.

