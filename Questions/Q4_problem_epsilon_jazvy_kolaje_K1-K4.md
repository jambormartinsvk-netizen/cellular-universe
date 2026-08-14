# Q4 — ε jazvy pri ξ → 1: problém, stav a koľaje

**Dátum založenia:** 2026-07-13  
**Stav vetvy:** OTVORENÁ; pred fyzikálnym testom chýba definícia  
**Pôvod:** starý aj aktuálny register otázok

## 1. Presné znenie problému

Register uvádza: „Aké ε (jazvy) dá ξ → 1 bez pasce #7?“ Sprievodná interpretácia spája otázku so súbehom zlyhania a vzniku jazvy, trávením paliva a pôvodom hmoty.

V korpuse však nie je definované:

- čo je `ξ` a v akom intervale leží;
- čo znamená limit `ξ → 1`;
- čo presne je „pasca #7“;
- či `ε` označuje amplitúdu, pravdepodobnosť, rýchlosť alebo hustotu;
- čo je elementárny pokus a koľko pokusov prebehne;
- akú energiu nesie jedna jazva.

Bez týchto definícií pôvodná otázka nemá jednoznačnú matematickú odpoveď.

## 2. Overený numerický fakt

Pre fitované `λ = 0,15` a `H0 = 66,37 km s^-1 Mpc^-1`:

$$
\epsilon_{\rm eff}=\lambda H_0t_P
=1,7394091927\times10^{-62},
$$

$$
\epsilon_{\rm eff}^2
=3,0255443395\times10^{-124}.
$$

Ide o rovnaký rád ako `10^-123`, ale nie o vnútorné odvodenie. Výpočet je reprodukovateľný v `scripts/14_script_legacy_Q4_epsilon_S8_arithmetic_audit.py`.

## 3. Povinná definičná brána Q4-P0

Pred výberom koľaje sa musia v jednej tabuľke určiť:

| Symbol | Povinná definícia |
|---|---|
| `F` | elementárne zlyhanie: vstupný stav, výstupný stav, trvanie |
| `I` | elementárna jazva: stavová zmena a kritérium trvalosti |
| `p_F` | pravdepodobnosť alebo hazard zlyhania na presne určený pokus |
| `p_I` alebo `p(I|F)` | pravdepodobnosť jazvy a jej podmienenie |
| `ξ` | korelácia, podmienená pravdepodobnosť, účinnosť alebo stavový parameter |
| `E_I` | energia/hmotnosť jednej jazvy |
| `N_trial` | počet pokusov na bunku, objem a kozmický čas |
| pasca #7 | explicitná zakázaná degenerácia alebo nekonzistentnosť |

Kým brána Q4-P0 nie je splnená, žiadna koľaj nemôže dostať stav „overená“.

## 4. Koľaj K1 — dva zriedkavé deje s korelačným faktorom

### Hypotéza

Nech `F` je zlyhanie a `I` vytvorenie jazvy. Zaveďme

$$
P(F\cap I)=\xi\,p_Fp_I,
$$

kde `ξ → 1` znamená štatistickú nezávislosť v tomto konkrétnom parametrizovaní. Ak navyše `p_F = p_I = ε_eff`, dostaneme `P(F∩I)=ε_eff²`.

### Testy

- K1-T1 bezrozmernosť `H0tP`: **PASS**;
- K1-T2 aritmetika `ε_eff²`: **PASS**;
- K1-T3 normalizácia pravdepodobnosti: **PODMIEŇENE PASS**, ak `0 ≤ ξ p_Fp_I ≤ min(p_F,p_I)`;
- K1-T4 dôvod `p_F = p_I`: **NEOVERENÉ**;
- K1-T5 nezávislosť pri `ξ → 1`: **DEFINIČNÁ VOĽBA, NIE PREDIKCIA**;
- K1-T6 mapa na hustotu hmoty/vákua: **NEOVERENÉ**;
- K1-T7 kompatibilita s A1, kde neskorý Q tvorí CDM a baryogenéza je skorá: **OTVORENÉ**.

### Stav

**PREŽÍVA ARITMETIKU; NA STENE MIKRODYNAMIKY.** Je to najsľubnejšia koľaj, lebo najvernejšie rekonštruuje staré čítanie `ε²`, ale zatiaľ iba premenúva predpoklady.

## 5. Koľaj K2 — ξ ako podmienená pravdepodobnosť jazvy

### Hypotéza

$$
P(I|F)=\xi,\qquad P(F\cap I)=\xi p_F.
$$

Pri `ξ → 1` každé zlyhanie zanechá jazvu.

### Prvý test

Táto interpretácia je pravdepodobnostne prirodzená, ale dáva v limite `P(F∩I) → p_F`, nie `ε²`. Preto nie je zlučiteľná so starým numerickým čítaním bez predefinovania `ε`.

### Stav

**NA STENE KOMPATIBILITY SO STARÝM ČÍTANÍM; NIE JE MŔTVA.** Môže byť fyzikálne lepšia než K1, ak sa ukáže, že `ε²` nebolo základnou požiadavkou.

## 6. Koľaj K3 — jazvami modulovaný Poissonov hazard

### Hypotéza

Jazvy menia lokálny hazard ďalšieho zlyhania:

$$
\Gamma_F(x,t)=\Gamma_0\,f[n_I(x,t),\xi(x,t)].
$$

Limit `ξ → 1` by označoval kritické nasýtenie alebo úplné trávenie.

### Povinné testy

- odvodiť `f`, nie ju fitovať na `10^-123`;
- dokázať `Γ_F ≥ 0` a stabilitu siete;
- simulovať distribúciu jaziev a jej škálovanie s objemom;
- vypočítať hmotový výťažok a porovnať s A1.

### Stav

**PREŽÍVA AKO MODELOVÁ TRIEDA; NEMÁ ROVNICE.**

## 7. Koľaj K4 — nukleácia alebo tunelovanie

### Hypotéza

Jazva vzniká zriedkavým prechodom s amplitúdou alebo rýchlosťou

$$
\Gamma_I\sim A e^{-B},
$$

kde `B` je bezrozmerná akcia bariéry siete.

### Povinné testy

- definovať stupne voľnosti a akciu;
- nájsť sedlové riešenie/bounce;
- odvodiť prefaktor `A` a zabrániť dvojitému fitu;
- preveriť energetickú konzerváciu a spätnú reakciu.

### Stav

**PREŽÍVA FORMÁLNE; NA STENE CHÝBAJÚCEJ AKCIE.**

## 8. Rozhodnutie vetvy Q4

Poradie preverovania: **K1 → K2 → K3 → K4**.

Bez odpovede autora na význam `ξ` a „pasce #7“ sa dá dokončiť iba K1-T1 až K1-T3. Najbližší krok je teda doplniť bránu Q4-P0, nie hľadať ďalšiu číselnú zhodu.

