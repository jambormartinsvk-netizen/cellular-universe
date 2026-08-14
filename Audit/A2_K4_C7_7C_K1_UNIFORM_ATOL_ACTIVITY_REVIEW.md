# A2-K4 C7.7c-K1 — smrť uniformného `atol` activity dôkazu

**Dátum:** 2026-07-14  
**Skripty:** 139, 140, 141  
**Rozsudok podkoľaje K1:** `MŔTVA AKO NUMERICKÝ DÔKAZ / UNRESOLVED`  
**K4:** živá; jemná hĺbka zostáva `66.5/100`

## Výsledok

Skript 140 dal `84/116`. Štyri FAIL položky vznikli iba preto, že
`json.dumps(sort_keys=True)` zmenil poradie úplnej množiny kľúčov. Skript
141 túto technickú chybu opravil porovnaním množiny aj počtu a dal:

```text
REVIEW_C7_7C_UNRESOLVED_COMPONENTS_FIXED_KEYS
88/116 PASS
28 activity FAIL
```

Zostávajúce FAIL sú fyzicky relevantné numerické nerozlíšenie:

| Mód | Nerozlíšené komponenty na deep aj shallow |
|---|---|
| NID | `h`, `delta_c`, `delta_f`, `U_f`, `L3`, `L4` |
| NIV | `L4` |

## Rozsahy

Uniformný beh používal `atol=1e-14`; predregistrovaný activity floor mal
minimum `10*atol=1e-13`.

| Komponent | Maximum | Max. RHS | Max. checkpointová zmena | Floor |
|---|---:|---:|---:|---:|
| NID/deep `h` | `1.79e-14` | `5.37e-14` | `1.68e-14` | `1e-13` |
| NID/deep `delta_c` | `8.96e-15` | `2.68e-14` | `8.40e-15` | `1e-13` |
| NID/deep `delta_f` | `3.49e-17` | `1.04e-16` | `3.29e-17` | `1e-13` |
| NID/deep `U_f` | `7.49e-16` | `2.27e-15` | `7.11e-16` | `1e-13` |
| NID/deep `L3` | `1.31e-16` | `5.25e-16` | `1.29e-16` | `1e-13` |
| NID/deep `L4` | `1.80e-24` | `1.08e-23` | `1.80e-24` | `1e-13` |
| NIV/deep `L4` | `5.14e-20` | `2.57e-19` | `5.10e-20` | `1e-13` |

Shallow výsledky sú rovnakého rádu. Signál nie je dokázateľne dynamický pri
uniformnej absolútnej podlahe, hoci rovnice ho analyticky generujú.

## Dôvod smrti K1

Jedna absolútna tolerancia pre premenné s amplitúdami od `10^6` po
`10^-24` nemôže byť dôkazom aktivity každej z nich. Dobehnutie solvera
zostáva platným C7.7b PASS, ale uniformný beh nemôže uzavrieť C7.7c.

Podkoľaj ani skripty sa nemažú. Dôvod smrti je numerické nerozlíšenie, nie
ghost, runaway ani porušenie fyzikálneho zákona.

## Nová podkoľaj K2

C7.7c-K2 integruje všetkých 13 premenných v bezrozmernom tvare

```text
w_i = y_i / scale_i,
scale_i = max(abs(y_i(x_start)), 1e-300).
```

Voľba sa aplikuje na všetky zložky, nie iba na tie, ktoré zlyhali. Je určená
výlučne auditovaným počiatočným stavom pred novým behom; nepoužíva konečný
výsledok ani post-data threshold.

