# P5.3g7-M3/TCA0 RERUN2 — predregistrácia tvrdého M1 anchoru

**Dátum:** 2026-07-16  
**Typ:** druhá a posledná technická/formula-väzbová oprava balíka 261  
**Fyzika:** bez zmeny  
**Skóre/hĺbka:** bez zmeny pred výsledkom

## Opravovaná chyba

RERUN1 vyriešil 77 štandardných koeficientov z matice hodnosti 76 a prijatú
M1 amplitúdu kontroloval až po riešení. RERUN2 musí M1 hodnotu použiť ako
externú normalizačnú podmienku, presne podľa dokumentu 26 a predregistrácie
27.

## Jediná povolená matematická zmena

Pre M1 premennú `x_a=h[target_power]` sa nastaví presná hodnota
`x_a=h_M1`. Jej stĺpec sa odpočíta od pravej strany a lineárna sústava sa
vyrieši iba pre zostávajúcich 76 neznámych:

```text
M_rest x_rest = -c - M_anchor h_M1.
```

Potom sa vloží `h_M1` späť do úplného vektora. Anchor sa nesmie pridať ako
mäkký least-squares riadok ani vynútiť veľkou váhou. `00` a `0i` ostávajú
nezávislé holdouty.

V1 modul sa neprepisuje. Nový malý versioned overlay musí exportovať presnú
provenienciu V1, opraveného solvera a vykonanej cesty. RERUN2 smie zároveň
opraviť stale embedded run label `KMPC-022` na vlastný identifikátor; nejde
o zmenu výsledku ani fyziky.

## Zmrazené očakávania pred behom

| Kontrola | PASS | Ak neprejde |
|---|---|---|
| M1 anchor | absolútny rozdiel `<1e-14` vo všetkých 15 prípadoch | technický STOP solvera |
| redukovaná hodnosť | `76/76` vo všetkých 15 prípadoch | REVIEW neodstránenej null/gauge vetvy |
| štandardný driver | `<1e-10` s presne ukotveným M1 | REVIEW/STOP rovníc alebo truncation |
| štandardné `00/0i` holdouty | `<1e-10` | REVIEW/STOP štandardnej mapy; frakčnú fyziku nehodnotiť |
| exact identity/background/S-C | rovnaké prahy ako v dokumente 27 | STOP implementácie pri regresii |
| frakčná hodnosť a driver | rovnaké prahy ako v dokumente 27 | REVIEW/STOP M3 |
| frakčné `00/0i`, vrstvy, dva štarty | rovnaké prahy ako v dokumente 27 | fyzikálny REVIEW/STOP podľa invariantnosti |

Očakáva sa, že M1 ukotvenie odstráni spoločný `76/77` podpis a výrazne zníži
štandardné holdouty. Nepreregistruje sa očakávaný frakčný PASS; ten musí
rozhodnúť výpočet.

## Prevádzkové brány

- nový overlay aj runner musia prejsť error-ledger kontrolou;
- `version`, `py_compile`, `--help`, smoke a plný beh sa spúšťajú oddelene;
- interný deadline `<=5 s`, každý vonkajší timeout `<=10 s`;
- smoke musí zvlášť overiť tvrdú elimináciu na malej rank-1 deficientnej
  lineárnej sústave a JSON serializáciu NumPy skalárov;
- výsledok je nový immutable `RERUN2` JSON;
- po RERUN2 nie je povolený automatický RERUN3.

## Neskoršie obmedzenie rozsahu zákazu

Zákaz automatického RERUN3 platí naďalej pre legacy 11-zložkovú
KMPC-022/023/024 implementáciu. Neskoršie pravidlo cap `10` povoľuje až po
B1 samostatnú úplnú R-A realizáciu ako spoločný technický pokus `4/10`.
Nejde o tretí patch tohto runnera ani o zmenu fyziky.
