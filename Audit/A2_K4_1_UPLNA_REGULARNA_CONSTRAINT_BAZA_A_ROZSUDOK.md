# A2-K4.1 — úplná regulárna constraintová báza a rozsudok

**Dátum:** 2026-07-14  
**Koľaj:** A1-K1 / A2-K4  
**Rozsudok brány:** **`PREŠLA K4.1`**  
**Stav koľaje:** **`PREŽÍVA K4.1 — 55/100`**  
**M-011:** historický záznam sa zachováva, jeho konečný rozsudok však zostáva
zrušený erratom  
**Ďalšia povinná brána:** **K4.2 — high-k/subhorizontový hlavný symbol a
fyzikálny rast**

## 1. Čo sa auditovalo

K4 používa nezmenený background A1-K1, `lambda=0.15`,
`delta=1+w_f=0.02297`, `c_s,f^2=1` a entalpicky vážený energy-frame

```text
(rho_c + delta rho_f) theta_d
= rho_c theta_c + delta rho_f theta_f.
```

Audit K4.1 nevyberal jeden vhodný počiatočný vektor. Odvodil celý priestor
regulárnych, Einsteinovým constraintom prípustných vedúcich módov deklarovanej
deväťpremennej sústavy s perfektnou radiáciou a numericky preniesol každú jeho
bázovú zložku. Toto je potrebné, pretože v interagujúcich tekutinách sa musia
kontrolovať aj entropické módy; samotný adiabatický mód ani ľubovoľný
constraintový vektor v konečnom čase priestor počiatočných dát neuzatvárajú.

## 2. Premenné a presný constraint

Pre limit `a -> 0`, `q=k/H0 -> 0` sa zaviedli konečné rýchlosti

```text
U_A = a E u_A,
```

a z Einsteinovho `00` constraintu v radiačnom limite vyplýva

```text
delta_r = -4 U_r.
```

Redukovaný indiciálny systém preto používa

```text
z = [delta_c,U_c,delta_f,U_f,delta_b,U_b,U_r,Phi].
```

Pri hľadaní Frobeniových módov `z ~ a^p` dá jeho presný charakteristický
polynóm

```text
p^3 (p+2)^2 (p+3)
[p^2 + (5-3 delta)p + 12-6 delta].
```

Pre `delta=0.02297` sú exponenty

```text
p = 0, 0, 0,
p = -2, -2,
p = -2.465545 +/- 2.404842584 i,
p = -3.
```

Mód s `Re(p)<0` diverguje pri `a -> 0`; nie je regulárnym primordiálnym
módom. Úplný regulárny priestor má teda presne dimenziu tri.

## 3. Tri regulárne módy

Použitá vedúca báza pozostáva z:

1. spoločného-clock adiabatického módu;
2. CDM-density izokurvatúrneho módu s nulovou vedúcou celkovou hustotou;
3. baryónového density izokurvatúrneho módu s nulovou vedúcou celkovou
   hustotou.

Pri konečnom štarte sa každý reprezentant korigoval tak, aby presne spĺňal
`00` constraint na vypočítanom A1-K1 backgrounde. Výpočet nezačína pri
rekombinácii, ale hlboko v radiačnej ére (`x=ln a=-20`); porovnávací beh
začína pri `x=-22`.

Historický seed

```text
U_f = 1, ostatné vedúce zložky = 0
```

má relatívne projekčné rezíduum `0.9789492202` voči úplnej regulárnej báze.
Nie je teda lineárnou kombináciou regulárnych primordiálnych módov. To, že
bol v konečnom čase zostavený ako constraint-kompatibilný velocity seed,
nepostačuje na jeho prípustnosť v limite `a -> 0`. Jeho transfer zostáva
platným diagnostickým výsledkom skriptu 30, ale nemôže byť kill testom
primordiálnej K4 koľaje.

## 4. Hlavný numerický výsledok

Skript 66 integroval celú trojrozmernú bázu pomocou DOP853 a oddelene
hlásil absolútny transfer od pomeru k `Gamma=0` referencii.

| Mód | Max. absolútny normový transfer |
|---|---:|
| adiabatický | `2.4672246705` |
| CDM density izokurvatúrny | `23.1987376069` |
| baryónový density izokurvatúrny | `4.3981188463` |

Najväčší singulárny transfer ľubovoľnej normalizovanej kombinácie regulárnej
bázy je

```text
T_regular,max = 26.4369073223.
```

Pri primordiálnej amplitúde `1e-5` je preto najväčšia auditná norma

```text
2.64369073223e-4 < 1.
```

V testovanom superhorizontovom rozsahu nevzniká absolútna explózia ani strata
linearity. Pomer k nulovému modelu nie je použitý ako absolútny exponent;
slúži iba ako osobitná diagnostika.

## 5. Constrainty a konvergencia

| Kontrola | Výsledok | Prah | Stav |
|---|---:|---:|---|
| globálne relatívne `00` rezíduum | `2.19098e-12` | `<1e-6` | PASS |
| posun štartu `-20 -> -22` | `5.84722e-6` | `<1e-5` | PASS |
| zmena `q -> q/2` | `1.48606e-9` | `<1e-6` | PASS |
| sprísnenie tolerancií | `1.61898e-7` | `<1e-6` | PASS |
| zmena kroku backgroundu | `9.41006e-7` | `<1e-6` | PASS |

Všetkých jedenásť predregistrovaných kontrol skriptu 66 prešlo.

## 6. Nezávislá krížová kontrola

Skript 67 neimportuje integrátor porúch zo skriptu 66. Samostatne zostavil
indiciálnu maticu a použil pevno-krokový RK4 na dvoch mriežkach. Po oprave
zdokumentovanej v `ERRATUM_67B` sa background v strede kroku počíta vlastným
polkrokom RK4, aby sa nedegradoval rád integrácie.

| Kontrola | Výsledok |
|---|---:|
| dimenzia regulárneho jadra | `3` |
| rezíduum explicitnej bázy v jadre | `2.77556e-17` |
| globálne `00` rezíduum, hrubý RK4 | `3.42023e-14` |
| globálne `00` rezíduum, jemný RK4 | `2.49060e-15` |
| rozdiel hrubý/jemný RK4 | `2.34544e-8` |
| rozdiel voči DOP853, hrubý RK4 | `3.94627e-7` |
| rozdiel voči DOP853, jemný RK4 | `3.71173e-7` |

Všetkých sedem nezávislých kontrol prešlo. Výsledok preto nie je artefaktom
jedného adaptívneho integrátora ani lineárnej interpolácie backgroundu.

## 7. Rozsudok a presný rozsah

**K4.1 prešla. A2-K4 prežíva na maximálnej hĺbke `55/100`.**

Tento rozsudok znamená iba:

- deklarovaný deväťpremenný perfect-radiation systém má úplne spočítanú
  trojrozmernú regulárnu superhorizontovú bázu;
- žiadna jej kombinácia v testovanom rozsahu nevytvára absolútnu
  superhorizontovú stratu linearity;
- historický seed M-011 neleží v regulárnom primordiálnom priestore;
- historické čísla a skripty M-011 sa nemažú, ale ich starý konečný výklad
  zostáva obmedzený.

Tento rozsudok **neznamená**:

- high-k gradientovú alebo kinetickú stabilitu;
- stabilný subhorizontový rast;
- úplnú fotónovú a neutrínovú Boltzmannovu hierarchiu;
- CMB-normalizované `S8`;
- observačné schválenie K4 ani celej A1-K1.

Skóre `55/100` je hĺbka dokončenej superhorizontovej polovice pásma
`50–59`, nie pravdepodobnosť pravdivosti. K4 sa smie posunúť vyššie iba po
K4.2.

## 8. Ďalší krok K4.2

Pred ďalšou A2 koľajou treba pre ten istý uzáver:

1. odvodiť high-k hlavný symbol úplných lineárnych rovníc;
2. skontrolovať znamienka kinetickej a gradientovej matice a nulový limit;
3. oddeliť fyzické vlastné módy od constraintových/gauge módov;
4. integrovať reprezentatívne subhorizontové `k` bez ladenia na `S8`;
5. predregistrovať stenu pre gradientový rast, stratu linearity a
   nekontrolovaný rast hustotných alebo relatívnych módov;
6. zachovať všetky skripty a výstupy aj pri smrti K4.2.

Ak K4.2 zomrie, K4 sa označí novým dôvodom smrti; M-011 sa spätne
neobnoví ako dôvod. Ak K4.2 prejde, až potom sa pripraví plná
fotónovo-neutrínová/A3 brána.

## 9. Reprodukčné artefakty

- `scripts/66_script_A2_K4_1_complete_regular_mode_basis.py`;
- `scripts/67_script_A2_K4_1_independent_fixed_RK4_crosscheck.py`;
- `scripts/OUTPUT_A2_K4_1_66_67.md`;
- errata 66, 66B, 67 a 67B v adresári `scripts`;
- `Audit/A2_K4_1_MANIFEST_SHA256.md`.

## 10. Primárne metodické zdroje

- [Malik & Wands — adiabatic and entropy perturbations with energy transfer](https://arxiv.org/abs/astro-ph/0411703);
- [Malik, Wands & Ungarelli — interacting fluids and adiabatic perturbations](https://arxiv.org/abs/astro-ph/0211602);
- [Valiviita, Majerotto & Maartens — large-scale instability in interacting dark energy](https://arxiv.org/abs/0804.0232).

## 10. Následný výsledok K4.2

K4.2 bola 2026-07-14 dokončená a prešla v deklarovanom perfect-radiation rozsahu. K4 sa posúva z `55/100` na `59/100`. Historický M-011 zostáva zachovaný, ale všeobecný rozsudok ďalej obmedzuje výsledok úplnej regulárnej subhorizontovej bázy. Autoritatívny následný audit je `Audit/A2_K4_2_HIGH_K_SUBHORIZONTOVY_AUDIT_A_ROZSUDOK.md`; ďalšia brána je K4.3.

