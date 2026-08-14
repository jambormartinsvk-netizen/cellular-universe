# A2-K5 — stav po K5.0 a akčný plán

**Dátum:** 2026-07-13  
**Aktívna koľaj:** A2-K5/K1  
**Stav:** `PREŽÍVA IBA K5.0 — 45/100; RASTOVÁ BRÁNA ČERVENÁ`

## Rozhodnutie

- A2-K1 až A2-K4 zostávajú mŕtve M-009, M-008, M-010 a M-011;
- K5/K1 má lokálnu kanonickú skalárnu akciu a presne reprodukuje A1-K1;
- ghostová, gradientová a backgroundová tachyonická brána prešli;
- kvázistatický test zvýšil vážený rast hmoty o `5.20–5.30 %`;
- diagnostická projekcia posunula `S8` na približne `0.920`, ale nie je
  plnohodnotnou predikciou;
- koľaj sa preto ešte nearchivuje ako mŕtva, no nesmie sa označovať za
  observačne životaschopnú.

## Akčný plán A2-K5.1

| Poradie | Krok | Výstup | Kill/pass brána |
|---:|---|---|---|
| 1 | variovať akciu do prvého rádu v Newtonovej gauge | úplná KG, CDM kontinuita/Euler, baryóny, žiarenie a Einsteinove rovnice | algebraická bilancia a znamienka |
| 2 | zostaviť gauge-invariantné premenné | nezávislý opis relatívnej rýchlosti a entropie | žiadna gauge-dependentná predikcia |
| 3 | odvodiť radiačné počiatočné podmienky | séria v `k eta` vrátane skalára a CDM | regulárny adiabatický mód bez ručného ladenia |
| 4 | numerický superhorizontový test | nový uložený skript, constraint residualy, kroková a `k` konvergencia | žiadny nekontrolovaný mód |
| 5 | subhorizontový relativistický cross-check | porovnanie s limitom skriptu 33 | zhoda tam, kde `k/(aH)>>1` |
| 6 | implementácia v CLASS/CAMB | CMB TT/TE/EE, lensing, `P(k)`, `f sigma8`, `S8` | CMB-normalizovaný rozsudok |
| 7 | rozhodnutie | `PREŽÍVA N/100` alebo `MŔTVA M-012` | bez posúvania steny po výsledku |

## Predregistrovaný rozhodovací bod

Ak plný CMB-normalizovaný výpočet potvrdí zosilnenie rastu na škálach `S8`
a dáta ho nekompenzujú povolenou zmenou primordiálnej normalizácie, K5/K1
zomrie ako M-012. Nezavádza sa nový voľný parameter na nezávislé potlačenie
piatej sily, pretože by už nešlo o test tejto koľaje.

Ak zomrie, všetky dokumenty, skripty 32–36, výstupy a hash manifest zostanú.
Potom sa otvorí A2-K5/K2.

## Verzia

Do v3.18 možno K5/K1 zaradiť iba ako auditovaného kandidáta mikrofyzikálneho
dokončenia. Prijatie konformne viazaného skalárneho poľa za nový fundament bez
odvodenia z bunkovej siete je zmena fundamentu a patrí do verzie 4.
