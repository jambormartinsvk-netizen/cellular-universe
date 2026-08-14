# A2-K4.3b-RG BR3B-2f-5 — audit úplného zmiešaného reťazca po common fuel

Dátum: 2026-07-14  
Rozsudok BR3B-2f-5: **PASS**  
Rozsudok A2-K4: **ŽIVÁ**  
Kanonická hĺbka A2-K4: **60/100 = G6**  
G7: **NEUZAVRETÁ**

## Rozsah brány

Skript 124 vyriešil na prvom ráde v skorom fuel pomere
`rho_f/rho_r = Phi z^p`, kde `p=4-3 delta=3.93109`, celý reťazec:

| Mód | Vyriešené Puiseuxove vrstvy | Fyzikálny význam |
|---|---|---|
| NID | `p`, `p+1`, `p+2`, `p+3` | skorá relatívna rýchlosť, matter dressing, shear, common fuel |
| NIV | `p-1`, `p`, `p+1`, `p+2` | skorá relatívna rýchlosť, matter dressing, shear, common fuel |

V každej vrstve bolo riešených deväť radiation/Einsteinových riadkov a boli
nesené baryónová a CDM spojitosť. Nepridával sa nový fit ani nový fyzikálny
parameter.

## Výsledok úplnej sústavy

| Kontrola | NID | NIV | Brána |
|---|---:|---:|---|
| Tvar zmiešanej matice | `44 x 36` | `44 x 36` | informačné |
| Hodnosť | `36/36` | `36/36` | PASS |
| Číslo podmienenosti | `94.06` | `99.09` | konečné |
| Škálované rezíduum | `1.55e-15` | `9.56e-16` | `<1e-11` |
| Maximum z 11 fyzikálnych riadkov | `7.62e-16` | `1.50e-15` | `<1e-10` |
| Povinná matter medzivrstva | `1.191e-2` | `2.985e-2` | nenulová |
| Tá istá vrstva pri `mu=0` | `3.72e-16` | `3.51e-16` | nulová |

Štandardné NID/NIV vstupy zároveň reprodukovali pomery zo skriptu 115;
fuel test field reprodukoval BR3A koeficienty s rezíduami pod `2.9e-15`.
Nulový matter limit reprodukoval skoré sektory skriptu 104 a po oprave
species mapovania aj shear sektor auditovaný nižšie.

## Common-fuel koeficienty pri fyzikálnom matter backgrounde

Koeficienty sú na jednotku `Phi` v normalizácii skriptu 124.

| Mód/power | `h_x` | `eta` | `delta_gamma` | `delta_fs` | `U_gamma` | `U_fs` | `sigma_fs` |
|---|---:|---:|---:|---:|---:|---:|---:|
| NID, `p+3=6.93109` | `-1.08156e-3` | `-3.11596e-4` | `6.37333e-3` | `-7.95277e-3` | `-2.54011e-4` | `7.09674e-4` | `1.34128e-3` |
| NIV, `p+2=5.93109` | `-7.28219e-3` | `-2.05520e-3` | `1.67344e-2` | `-1.93157e-2` | `-4.73242e-3` | `8.91982e-3` | `2.21897e-3` |

Carried baryón/CDM koeficienty sú uložené v plnom JSON výstupe skriptu 124.

## Audit nezhody so skriptom 108

Prvý fyzikálny beh, skript 121, prešiel 24 z 26 kontrol. Obe nezhody boli
výlučne v porovnaní nulového matter shear sektora so starým oraclom 108.
Samotná nová sústava bola plného ranku a všetkých 11 rovníc mala malé
rezíduá. Preto výsledok nemohol byť interpretovaný ako smrť K4.

Skript 123 aplikoval maticu skriptu 108 na nové riešenie a lokalizoval celý
rozdiel na jediný riadok `nu_shear`:

| Mód | Zdroj z plnej sústavy | Starý zdroj 108 | Rozdiel |
|---|---:|---:|---:|
| NID | `-0.0801863` | `+0.0564429` | `-0.1366292` |
| NIV | `-0.2000000` | `+0.1407793` | `-0.3407793` |

Príčina je presná: skript 108 definoval
`J_ns=(8/15)(U_gamma,e-U_gamma,l)`. Shear voľne prúdiacej zložky však musí
použiť jej vlastnú rýchlosť,
`J_ns=(8/15)(U_fs,e-U_fs,l)`. Oficiálny CLASS riadok pre ultra-relativistic
shear používa `theta_ur`, nie `theta_g`:
[CLASS `perturbations.c`](https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c).

Skript 124 zmenil iba legacy porovnávací oracle. Jedenásť fyzikálnych rovníc
zmiešanej sústavy nebolo zmenených. Po oprave prešlo všetkých **26/26** brán.

## Obmedzenie starších formulácií

1. Skript 104 ostáva PASS pre skoré relatívne rýchlostné sektory.
2. Skript 108 ostáva dôkazom, že jeho zadané matice sú plného ranku a riešené
   s malým rezíduom. Jeho publikované NID/NIV shear koeficienty však nie sú
   fyzikálnym oraclom, pretože `J_ns` použil fotónovú namiesto neutrínovej
   rýchlosti. Tieto čísla nahrádza corrected-oracle výstup skriptu 124.
3. Exact Bianchi páry skriptu 108 túto chybu nemohli odhaliť, lebo jeho
   Bianchi kontrola neobsahovala species-local shear zdroj.
4. Skripty 118 a 119 sú zachované syntakticky neplatné pokusy; nevykonali
   fyziku. Skript 120 vykonal rovnice, ale zlyhal pri JSON serializácii.
5. REVIEW skriptu 121 nebol fyzikálny fail: odhalil chybný legacy oracle.

## Čo PASS znamená a čo ešte neznamená

BR3B-2f-5 uzatvára zmiešaný matter/fuel reťazec **iba po common-fuel vrstvu**.
Neuzatvára celý G7. Ešte chýba:

- BR3B-2g: prvý neskorší `l=3` feedback a ash-transfer/ash-gravity ledger;
- BR3C: evolúcia z dvoch skorých hĺbok, štyri Einsteinove rezíduá a
  kroková/tolerančná konvergencia;
- ďalšie G7 podbrány podľa kanonického plánu.

Preto A2-K4 zostáva **živá na 60/100 = G6**. Interný PASS BR3B-2f-5 nesmie
byť započítaný ako čiastočné body G7.

## Ďalší krok

BR3B-2g má do jedného ledgeru vložiť:

- NID prvý `l=3` feedback pri `p+4`, ash korekciu `delta_c` pri `p+4` a jej
  prvý gravitačný vstup pri `p+5`;
- NIV prvý `l=3` feedback pri `p+3`, ash korekciu `delta_c` pri `p+3` a jej
  prvý gravitačný vstup pri `p+4`;
- nulové limity pre vypnutý fuel/transfer a úplný species/Einstein residual
  ledger bez nového fitu.

