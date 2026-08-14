# Akčný plán po K7c P3b

Dátum: 2026-07-15

## Aktuálny rozsudok

P3b prešla oboma zmrazenými krokovými bránami. Kanonizácia dvoch presných
nulových koeficientov odstránila ne-RK4 správanie P1. A2-K4 ostáva
`66.5/100`; celý C7-G5 ešte nie je uzavretý.

## Povinné poradie ďalšej práce

### P4a — dokončenie šírky C7-G5

1. Zmraziť skript 205, P3b raw a tri checkpointy hashmi.
2. Zachovať kanonické nuly, stav, background, interval a normu.
3. Predregistrovať aspoň jeden nezávislý metódový cross-check a tolerančný
   sweep; žiadny prah sa nesmie odvodiť až z výsledku.
4. Vyžadovať paritu endpointu s konvergovaným RK4 v preregistrovanej norme.
5. Technický timeout je REVIEW; platný metódový nesúlad je STOP iba pre
   danú integračnú formuláciu, nie automaticky smrť K4.

### P4b — C7-G4 bez tautológií

1. Pred výpočtom označiť každý constraint ako nezávislú bránu, vynútenú
   identitu alebo cancellation monitor.
2. Skóre smú ovplyvniť iba nezávislé rezíduá, ktoré RHS nedefinuje tým istým
   výrazom a ktoré neboli eliminované projekciou.
3. Overiť aktivitu všetkých 13 komponentov na viacerých checkpointoch,
   nie iba konečný stav.

### P4c — C7-G6 štyri plochy

1. Až po P4a/P4b PASS spustiť NID-deep, NID-shallow, NIV-deep a NIV-shallow.
2. Každá plocha má vlastný interný a externý timeout, immutable raw JSON a hash.
3. Výpadok jednej plochy sa nesmie zakryť agregátom ostatných troch.
4. Až štyri platné PASS umožnia zvažovať bodový/skórový účinok podľa C7-W1.

## Zakázané skratky

- neoznačiť celý G5 PASS iba z P3b;
- neprideliť G4 body za tautologický constraint;
- nepoužiť staré P1 čísla ako blocker opravených rovníc;
- neoživiť fsum-only vetvu;
- nespúšťať CMB/S8 ani plnú hierarchiu pred uzavretím P4a–P4c.

