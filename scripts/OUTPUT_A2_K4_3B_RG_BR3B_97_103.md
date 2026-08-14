# A2-K4.3b-RG BR3B — výstup skriptov 97 až 103

Dátum auditu: 2026-07-14  
Kanonický stav koľaje: **živá, 60/100 = G6**  
Stav G7: **neuzavretá**

## Súhrn behov

| Skript | Výsledok behu | Fyzikálny význam |
|---|---|---|
| 97 | `PASS_DIAGNOSIS_BACKGROUND_DRESSING_REQUIRED` | Izolovaný palivový stress nie je konzervovaný úplný zdroj. Toto nie je smrť K4; chýbajú povinné členy pozadia. |
| 98 | `PASS_EXACT_COMPATIBILITY_CONDITIONS_DERIVED` | Odvodené dve exaktné Bianchiho podmienky pre Einsteinovo doplnenie. Algebraický minimálny doplnok nie je vydávaný za fyziku. |
| 99 | `PASS_FULL_SOURCE_BIANCHI_IDENTITIES_DERIVED` | Bianchiho podmienky rozšírené na všetkých päť radiačných a štyri Einsteinove riadky. |
| 100 | `PASS_PHYSICAL_HX_SECTOR_BIANCHI_COMPATIBILITY` | Povinné pozadie a Eulerovo nútenie odstránili obštrukciu bez fitovaného koeficientu; oba rezíduá sú presne nula. |
| 101 | `ERROR_UNCLOSED` | Technická chyba: `SymPy BooleanTrue` nebolo JSON serializovateľné. Bez fyzikálneho rozsudku; súbor ostáva zachovaný. |
| 102 | `PASS_MULTIPOWER_ORDER_AND_COMPENSATION_LEDGER` | Opravený klon 101. Presná kompenzácia NID/NIV a poradie skorších frakčných sektorov potvrdené. |
| 103 | `PASS_MANIFEST_CREATED` | SHA-256 manifest skriptov 97–102. |

## Exaktný spoločný sektor

Pre `p=4-3 delta=3.93109`, `r=n+p`, jednotkový vedúci koeficient `h_x=a^n` a štandardný `0i` constraint

`eta_x = 2 (R_gamma U_gamma + R_fs U_fs)`

je fyzikálne odvodené doplnenie

- `J_gamma,continuity = J_fs,continuity = 0`,
- `J_gamma,Euler = p U_gamma / 2`,
- `J_fs,Euler = p U_fs / 2`,
- `C00 = 1/2`,
- `C0i = -eta_x`,
- `Ctr = -(n+1+p/2)`,
- `Ctl = -(n+1+p/2)(1+6 eta_x)`.

Po pridaní už odvodeného palivového stressu sú obidve Bianchiho kompatibility presne `0` pre AD, CDI, BI, NID a NIV. Matica aj rozšírená matica majú hodnosť `7`. Nejde o nový voľný parameter.

## Skoršie NID/NIV sektory

| Mód | Mocnina | Zdroj | Stav |
|---|---:|---|---|
| NID | 3.93109 | korekcia sklonu pozadia krát kompenzované relatívne rýchlosti pri `a^0` | celková vedúca hybnosť je presne nulová; treba hierarchiu |
| NID | 5.93109 | gradient/eta/šmyk z radiačných členov `a^2` | šmyk ešte nie je doplnený |
| NID | 6.93109 | spoločný palivový sektor z `h_x~a^3` | kompatibilný v skripte 100 |
| NIV | 2.93109 | korekcia sklonu pozadia krát kompenzované relatívne rýchlosti pri `a^-1` | celková vedúca hybnosť je presne nulová; treba hierarchiu |
| NIV | 4.93109 | hustota/eta/šmyk z NIV členov `a^1` | hustota sa presne kompenzuje; šmyk otvorený |
| NIV | 5.93109 | spoločný palivový sektor z `h_x~a^2` | kompatibilný v skripte 100 |

Záver: NID/NIV nie sú mŕtve. Ich skoršie relatívne radiačné sektory sa nesmú preskočiť a musia sa riešiť vzostupne podľa mocniny.

## Ďalší výpočet

`BR3B-2e`: doplniť neutrínový šmyk a minimálnu regulárnu rekurziu `l>=3` pre každý skorší NID/NIV sektor. Až potom možno vyriešiť celý indukovaný Puiseuxov systém a vykonať dvojhĺbkový reziduálny test.

