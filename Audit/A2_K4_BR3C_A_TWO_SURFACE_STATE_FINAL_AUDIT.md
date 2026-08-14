# A2-K4 BR3C-a — konečný audit dvoch počiatočných povrchov

**Dátum:** 2026-07-14  
**Rozsudok:** `C7.7a PASS`  
**Nová jemná hĺbka:** `66.2/100`  
**K4:** živá; `G6 PASS`, `G7 OTVORENÁ`

## Audítorský záver

K4 má pre NID aj NIV jeden spoločný coefficient-normalized analytický stav,
ktorý sa dá bez skrytého fitu vyhodnotiť na `x=-25` aj `x=-23`. Export
obsahuje aktuálne registrovanú metriku, species, fuel, total produced ash/CDM
sektor a `L3/L4/F3/F4`.

Prvý export 130 nebol prijatý iba podľa vlastného machine PASS. Skript 131
odhalil, že surové least-squares round-off hodnoty v **presne nulových**
hierarchických slotoch sa pri `F3=L3/s` a `F4=L4/s^2` zosilňovali. Táto
negatívna kontrola zabránila falošnému PASS.

Oprava 132 nepoužila dodatočný numerický prah. Projektovala iba sloty, ktoré
ledger 119/127 už pred výpočtom fixoval na nulu. Najväčšia odstránená hodnota
bola `1.90e-15`. Následný nezávislý audit 134 prešiel `15/15` s maximálnym
škálovaným rozdielom rádov 5/6 `2.50e-11`.

Preto je korekcia numerickou implementáciou existujúcej regularity, nie
novou fyzikou ani post-data fitom.

## Čo presne prešlo

1. zdrojový motor 127 zostal nemenný a každý transformačný zásah mal
   exact-count podmienku;
2. oba módy majú celý povinný stav na oboch povrchoch;
3. `0<z_deep<z_shallow<1e-3` a všetky hodnoty sú konečné;
4. backgroundové `Omega_A` sa sčítajú na jednu pod `2e-12`;
5. rescalované hierarchické identity prešli;
6. seed anchor, seed amplitude a fuel coefficient sú spoločné;
7. rády 5 a 6 prešli pôvodným absolútnym aj škálovaným testom;
8. všetky behy skončili hlboko pod časovými limitmi.

## Čo ešte neprešlo

- C7.7b: obe skoré evolúcie;
- C7.7c: úplný evolučný species/mode ledger bez placeholdera;
- C7.7d: zhoda oboch štartov na spoločnom neskoršom bode;
- C7.8: štyri Einsteinove rezíduá a konvergencie;
- C7.9–C7.10: plný backend, fyzické transfery a integrovaný G7 rozsudok.

## Skóre

```text
pred BR3C-a: 66.0/100
C7.7a PASS: +0.2
aktuálne:    66.2/100
```

Celá G7 zostáva otvorená. Nasleduje časovo obmedzená BR3C-b evolúcia z oboch
exportovaných povrchov.

## Reprodukcia

Výsledky, zachované neúspechy a SHA-256 sú v
`scripts/OUTPUT_A2_K4_3B_RG_BR3C_A_130_135.md`.

