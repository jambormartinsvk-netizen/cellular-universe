# Pokyny auditorovi

Over manifest pred čítaním výsledku. Čítaj preregistráciu pred dokumentom
65. Skontroluj, či runner 280 importuje deklarované base moduly a či raw
JSON zodpovedá execution ledgru.

Nulové alebo machine-floor rezíduum samo nepovyšuj na PASS, ak predregistrovaný
relatívny prah neprešiel. Naopak ho neoznačuj za fyzikálnu smrť bez dôkazu
o chybe rovnice alebo o stabilnom rozpore po primeranom refinement teste.

Spusť smoke a audit podľa `03_REPRODUCTION_AND_EXPECTATIONS.md` v čerstvej
kópii `REPRO/`. Zapíš Python, NumPy, OS/architektúru, exit code, wall time a
rozdiely voči reference JSON. Bitová zhoda JSON nie je povinná; povinné je
vyhodnotenie zmrazených prahov. Externý timeout je 10 s na proces. Ak
reprodukcia neprebehne, nepouži tag `INDEPENDENTLY_RECOMPUTED`.

## Opakovaný audit R3

R2 audit odhalil chýbajúci hash-gatovaný prerequisite. R3 preto navyše
obsahuje:

- `EVIDENCE/015__KMPC035_PREREQUISITE_RAW_RESULT.json`;
- `REPRO/scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json`.

Obe kópie musia mať SHA-256
`A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`.
Najprv potvrď odstránenie pôvodného `FileNotFoundError`. Neopakuj ani
nepreberaj autoritatívny PASS/REVIEW/STOP; odovzdaj len nezávislý posudok.

Výstup ulož ako nový Markdown v pridelenom response priečinku. Ak doň
nemáš právo zapisovať, vráť celý text bez skracovania; hlavný orchestrátor
ho importuje verbatim pod novým poradovým číslom. Existujúci súbor sa nikdy
neprepisuje.
