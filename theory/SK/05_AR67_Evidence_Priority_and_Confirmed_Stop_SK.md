# Dodatok k 05 — priorita dôkazov a potvrdený STOP (SK)

**Dátum:** 2026-07-15  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia  
**Nové pravidlo:** AR67

## Kontrola duplicity

AR30 a C7-W1 oddeľujú sekvenčnú hĺbku od váhy dôkazov. AR54 vyžaduje
predbehové očakávanie. AR66 obmedzuje numerické hľadanie na prvú
implementáciu a najviac dve technické opravy. AR67 nemení tieto pravidlá.
Dopĺňa iba poradie práce podľa fyzikálnej váhy a podmienku, za ktorej sa
numerický rozpor smie zmeniť na fyzikálny STOP.

## AR67 — Najprv vysokováhová brána; fyzikálny STOP musí byť potvrdený

Ak zostáva viac otvorených testov, prioritu majú nezávislé brány zachovania,
Einsteinových constraintov, stability, kauzality, úplnosti stupňov voľnosti
a robustnej konvergencie. Pomocné, tautologické alebo nízkováhové metriky sa
vykonajú iba vtedy, keď môžu zmeniť rozhodnutie alebo diagnostikovať presný
dôvod zlyhania. Počet zelených nízkováhových kontrol nesmie prekryť jednu
červenú vysoko váženú bránu.

Koľaj sa nesmie vyhlásiť za fyzikálne mŕtvu iba z timeoutu, parsera,
checkpointu, jedného solvera alebo jedného tolerančného nastavenia. Fyzikálny
STOP vyžaduje:

1. vopred registrované fyzikálne kill kritérium;
2. platnú provenance, konečný stav a numericky rozlíšený signál;
3. reprodukciu rozporu nezávislou metódou, toleranciou alebo analytickým
   invariantom podľa povahy testu;
4. vylúčenie už známej formálnej chyby podľa Python error ledgeru;
5. auditný záznam vzorcov, vstupov, výstupov, hashov a presného dôvodu STOP.

Potvrdenie nie je povolenie na neobmedzené pokusy. Rozpočet AR66 zostáva
záväzný. Ak sa rozpor v tomto rozpočte nedá potvrdiť ani odstrániť, výsledok
je `REVIEW_BLOCKED` a nasleduje architektonické rozhodnutie, nie ďalší suffix.

## Aplikácia na A2-K4 / K7d

Integrované C7-G4+G6+G7 dostáva prednosť pred plnou hierarchiou G8 a
likelihood G9. Základ tvoria štyri prípady NID/NIV × deep/shallow. Celý
balík smie použiť najviac dve cielené potvrdzovacie alebo technické iterácie.
Reprodukovateľný trace/traceless rozpor alebo nestabilita môže zastaviť K7;
samotný timeout zostáva technický REVIEW.

