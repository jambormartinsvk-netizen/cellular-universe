# KMPC-034 — CDI C1 výsledok a autoritatívny audit

**Dátum:** 2026-07-16  
**Koľaj:** `A1-K1 / A2-K4 / P5.3g7 / CDI C1`  
**Predregistrácia:** `57_KMPC_034_CDI_C1_PRIMARY_EXTENDED_COVERAGE_PREREGISTRATION_SK.md`  
**Exekučný ledger:** `58_KMPC_034_CDI_C1_EXECUTION_LEDGER_SK`

## 1. Nemenné artefakty

- výsledok:
  `scripts/results/k_mpc_005/RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json`;
- SHA-256 výsledku:
  `37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20`;
- base `cdi_c1_coverage.py`:
  `D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F`;
- runner 278:
  `E8C2677E590D8129C6425AABAD5D80C1746BC5EF0B1E90E055A23641040695A4`;
- povinný S-C0 passport KMPC-033:
  `4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C`.

Proces skončil `exit 0`; vnútorný runtime bol `0.75 s` pri limite
`4.8 s`. Všetky zmrazené zdrojové hashe sa zhodujú a JSON neobsahuje
`NaN` ani nekonečné numerické hodnoty.

## 2. Autoritatívny rozsudok hlavného auditora

```text
PASS_CDI_C1_CORE_AND_COMMON_COEFFICIENT_STABILITY_ONLY
/
REVIEW_CDI_C1_PRIMARY_01_INSUFFICIENT_EXTENDED_03_REMAINDER_NOT_YET_TESTED
```

Stroj navrhol kratší kandidát
`REVIEW_CDI_C1_SUPPORT_EXTENSION_REQUIRED`. Ten sa prijíma iba v
presnom význame: baseline `[0,1]` treba rozšíriť aspoň na `[0,3]`.
KMPC-034 nedokázal, že support `[0,3]` nestačí, pretože vynechané členy
`j>=4` v tomto behu neboli vypočítané.

Nie je podklad pre fyzikálny STOP CDI, P5, A2-K4 ani A1-K1.

## 3. Čo prešlo

| Brána | Výsledok | Dôkaz |
|---|---|---|
| support/count | PASS | CDI `[0,1] -> [0,3]`; F0 `4/8`, M3 `26/52`, všetko odvodené z kardinality |
| M3 rank | PASS | `26/26` a `52/52` |
| driver rovnice | PASS | primary aj extended pod zmrazenými prahmi |
| nezávislé `Einstein_00/0i` holdouty | PASS | primary max rel. `4.18e-15`, extended `3.28e-14` |
| forbidden vrstvy/stress | PASS | primary aj extended |
| production contract a `U_c` regularita | PASS | primary aj extended |
| spoločné koeficienty | PASS | max rel. drift `5.061250322927873e-15`; abs. fallback `2.914444349921253e-17` |
| podmienená S-C0 lower-moment mapa | PASS | presné nuly na skutočných primary/extended koeficientoch |

Spoločné `j=0,1` koeficienty sa pri rozšírení prakticky neprepísali.
Nové `j=2,3` členy preto nie sú prejavom kolapsu hodnosti alebo zmeny
normalizácie, ale legitímne subleading členy aktuálnej rovnicovej
formulácie.

## 4. Čo neprešlo a čo to znamená

Čistý pridaný chvost bol definovaný iba z extended riešenia:

```text
base  = c_ext[1] z
tail  = c_ext[2] z^2 + c_ext[3] z^3
full  = base + tail
```

Pri relatívnej bráne `1e-6` vyšlo:

| plocha | typické nenulové stavy | najhorší bežný stav |
|---:|---:|---:|
| `z=1e-4` | približne `1.84e-5` až `3.14e-5` | `delta_f = 3.136478085397359e-5` |
| `z=1e-2` | približne `1.84e-3` až `3.15e-3` | `delta_f = 3.14477004101659e-3` |

Tým je vyvrátená dostatočnosť supportu `[0,1]` pri zmrazených plochách
a presnosti. Nejde však o vyvrátenie supportu `[0,3]`: jeho členy
`j=2,3` po prijatí `[0,3]` patria do baseline a nemajú zmiznúť.

`sigma_fs` pri `z=1e-2` má relatívnu metriku blízku `1`, pretože jeho
nižší základ je takmer nulový a prvý relevantný člen vzniká až v novom
supporte. Tento pomer sa neberie ako samostatný dôvod. REVIEW ostáva
platné aj po úplnom vyradení `sigma_fs`, lebo zlyháva viacero normálne
nenulových hustôt a rýchlostí.

## 5. Nezávislé audity a obmedzenia dôkazu

- fyzikálny auditor odporučil čiastkový core/common PASS a REVIEW
  neznámeho remainderu `[0,3]`;
- matematicko-skriptový auditor overil rovnakú normalizáciu, čistý tail,
  počty, hashe a nezávislé holdouty a vylúčil falošný FAIL z
  `sigma_fs`;
- dokumentačný/release auditor potvrdil immutable výsledok a nulový
  release dopad.

`00/0i` sú skutočne nepoužité vo fitte, ale používajú spoločný equation
engine; nejde o druhú nezávislú implementáciu vzorcov. S-C0 guard je
podmienená presná lift/collapse identita, nie dôkaz mikrofyzikálneho
vzniku pary ani jej samostatnej dynamiky.

## 6. Rozsah, ktorý sa nesmie tvrdiť

KMPC-034 netestuje BI/NID/NIV, iné `k`, `gamma0/af0`, S-M
mikrofyziku, species-resolved `F_l>=3`, konečnú opacity, ODE, plnú
Boltzmannovu hierarchiu, G8/G9, CLASS, BBN/CMB ani `S8/H0`.

## 7. Jediný povolený ďalší atóm

Predregistrovať `KMPC-035 / GLOBAL-C1 CDI support-step-2 ladder`
(výslovne nie globálnu Fourier C2):

```text
accepted-candidate baseline [0,3]
vs audit support [0,5]
```

Povinné body:

1. bez zmeny rovníc, parametrov, `k=0.05`, nominal a prahov;
2. odvodiť F0 `8/12` a M3 `52/78`;
3. pred solve reprodukovať immutable KMPC-034 koeficienty `[0,1]` a
   `[0,3]` s rel. `<=1e-12`, abs. `<=1e-14`;
4. zopakovať rank/driver/`00/0i`/forbidden/regularity/finite/S-C0;
5. common bridge porovná iba powers `0..3` medzi `[0,3]` a `[0,5]`;
6. nový tail je iba powers `4,5` voči baseline `1..3`, pri rovnakých
   `z` a prahoch;
7. exportovať pokles tailu `2,3 -> 4,5` iba ako diagnostiku, nie ako
   náhradu absolútnej brány;
8. pri neúspechu nevytvoriť automaticky ďalší support ani fyzikálny
   STOP; najprv samostatný audit konvergencie a conditioning.

Ak nový tail prejde a powers `0..3` ostanú stabilné, support `[0,3]`
môže byť prijatý ako minimálny CDI support.

## 8. Stav po rozsudku

- CDI C1: core/common `PASS`, baseline `[0,1]` `REVIEW/INSUFFICIENT`,
  `[0,3]` remainder otvorený;
- A2-K4: `LIVE / 60/100`;
- P5: `3.5/6`;
- technické počítadlo CDI: historical packages `1`, active `0/10`;
- skóre/hĺbka: bez zmeny;
- `theory/`, predikčná tabuľka, SK/EN 05, release, Zenodo a changelog:
  bez triggera.

## 9. Neskoršie obmedzenie staršieho formulovania

KMPC-035 neskôr vykonal presne vyššie predpísaný `[0,3]→[0,5]` audit.
Core/common stabilita prešla, ale powers `4,5` pri `z=.01` prekročili
zmrazený tail prah pre F0 `delta_f` a M3 `sigma_fs`. Preto historická veta
„`[0,3]` remainder otvorený“ už neznamená neotestovaný stav: aktuálne je
`[0,3]` **nedostatočný/REVIEW**. Dôkaz, hashe a nonclaims sú v dokumente 62;
pôvodný rozsudok KMPC-034 sa tým spätne nemaže.
