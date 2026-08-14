# G8 RUN-000 — audit výsledku

**Výsledok:** `PASS SCREEN-S0`  
**Fyzikálny G8 stav:** `NOT RUN`  
**Support/WBS:** bez zmeny, `90/100`

Skript 76 vrátil CAMB `1.6.6`, 22/22 pravdivých kontrol a presne nulové
symbolické rezíduum pre každú rovnicu `J_l`, `G_l`, `E_l` (`l=2..8`) aj
polarizačný zdroj. Interný runtime bol `1.109 s` pod limitom `10 s`; proces
sa uzavrel v externom limite `15 s`.

Výsledok sa zhoduje s predregistráciou. Nie je potrebná zmena očakávania.
RUN-000 potvrdzuje iba dostupnosť a rovnicovú paritu zmrazeného štandardného
sektora. Netestoval K4 operátor, tight coupling, rekombináciu, evolúciu,
constrainty, CMB ani S8.

**Rozhodnutie:** povoliť skript 221 (`SCREEN-S0+S1`). G8 body sa
neprideľujú.

