# A2 — aktuálny stav koľají a odporúčanie

**Pôvodný dátum dokumentu:** 2026-07-15  
**Aktualizácia stavu:** 2026-07-16  
**Priorita:** A2-K4 / P5.3g7  
**Poznámka:** hĺbka nie je pravdepodobnosť pravdy

## Hlavné koľaje

| Koľaj | Stav | Max. hĺbka | Hlavná stena / ďalší krok |
|---|---|---:|---|
| A2-K1 | STOP M-009 | `45/100` | near-vacuum recoil `~2.014e5`; iba nový mechanizmus |
| A2-K2 | STOP M-008 | `25/100` | `c_s^2=w<0`; striktne barotropická vetva mŕtva |
| A2-K3 | STOP M-010 | `45/100` | relatívny mód `448.789`; gauge zmena nestačí |
| **A2-K4** | **ŽIVÁ / REVIEW_BLOCKED** | **`60/100` fyzikálne** | P5.3g7: K4 metrický seed + explicitný S1 seed |
| A2-K5 | STOP M-012 | `75/100` | povinná príťažlivá piata sila a vysoké S8 |
| A2-K6 | STOP M-013 | `30/100` | zdravý interval ponechal `mu_cc>1` |
| A2-K7 | živý rodič | `20/100` | chýba pozitívny lokálny kernel |
| A2-K8 | čaká / živá trieda | `10/100` | chýba collision kernel/noise |
| A2-K9 | čaká / živá trieda | `10/100` | chýba jeden produkčno-rozptylový operátor |
| A1-K2/A2-K10 | iná route | `10/100` historicky | najprv audit A1-K2 backgroundu |
| A2-K11 | živá hypotéza | `10/100` | chýba regulárny ortogonálny operátor |
| A2-K12 | živý rodič | `10/100` | chýba konkrétny párový kernel |

## Obmedzenie staršieho stavu K7

Staršia revízia tohto súboru uvádzala A2-K4 na `66.5/100`, K7 G0–G7 ako
fyzický PASS a G8 ako najbližší krok. Neskorší lineage audit tento výklad
obmedzil: K7 RHS nemala dynamické `U_c` a používala fixed-`K_MPC`
background. `66.5/100` zostáva historická technická hĺbka K7; G8 je na nej
zakázaná. Nejde o vymazanie K7 výsledkov, ale o opravu ich fyzikálneho
dosahu.

## Odporúčanie

1. pokračovať iba P5.3g7-M3/S1 podľa kontraktu;
2. po úplnom seede vykonať P5.4;
3. G8 otvoriť až po P5.4 PASS;
4. po prvej implementácii a najviac dvoch technických opravách vydať PASS,
   fyzikálny STOP alebo `REVIEW_BLOCKED`;
5. ak K4 zomrie, prejsť na najperspektívnejšiu živú triedu s už odvodeným
   kernelom; nevyrábať ďalší suffix bez novej fyziky.

Kanonický navigačný register:
`tracks/A1/A1K1/A2/00_TRACK_REGISTER.md`.

