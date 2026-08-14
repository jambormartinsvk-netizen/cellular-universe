# A2-K4 / C7.7c-K5 — evolučný dodatok

**Dátum:** 2026-07-14  
**Nadväzuje na:** `A2_K4_C7_7C_PROFILE_AND_BALANCE_AUDIT_2026-07-14.md`  
**Skóre pred/po:** `66.5/100`  
**Rozsudok:** A2-K4 ostáva **ŽIVÁ**; C7.7c-K5 je **MŔTVA numerická podkoľaj**.

## Evolučný výsledok K5a

K5a bola spustená v predregistrovanom poradí na NID/deep. Prvý beh nedal JSON pred vonkajším limitom 10 s. Opakovanie s vnútorným limitom 6 s splnilo obe lokálne vyvažovacie podmienky, ale nedokončilo segment `-25→-24`:

- redukčný faktor `max|J|`: `7.0622×10^13` — PASS;
- relatívna odchýlka spektra: `1.6936×10^-10` — PASS;
- dokončené segmenty: `0/1` — FAIL;
- RHS volania: `296 833`;
- čas: `6.015 s`;
- stav/RHS v poslednom známom bode boli konečné; fyzikálny safety cap nebol prekročený.

Podľa stop pravidla sa NIV/deep už nespustil.

## Dôvody smrti C7.7c-K5

1. Ani po dramatickom zmenšení lokálneho Jacobianu nedokončila prvý NID segment v limite.
2. Diagonála `D` zmenila efektívny komponentový chybový rozpočet. Pri NID/deep mala napríklad `D_delta_gamma=D_delta_fs≈2.84×10^-14`, ale `D_eta≈4.19×10^6`. Jednotné `atol` v transformovanej premennej preto už nezachovalo pôvodný kontrakt rovnakej komponentovej aktivity voči analytickej obálke.

K5 sa nesmie opakovať ako „úplné maticové vyváženie + jednotné normalizované atol“. Skript `153_script_A2_K4_C7_7c_K5_balanced_segment_evolution.py` zostáva zachovaný pre spätný audit.

## Nový smer C7.7c-K6

K6 ponechá stav v pôvodných fyzikálnych premenných a analytickú obálku použije iba ako vektor absolútnych tolerancií:

`atol_i = 10^-12 S_env,i`.

Tým sa stavový Jacobian nemení podobnostnou transformáciou a zachová sa zamýšľaná komponentová presnosť C7.7c.

