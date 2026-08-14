# Doplnenie registra otázok: starý register a vetva S8–H0

**Dátum:** 2026-07-13  
**Nadväzuje na:** `otazky_a_navrh_krokov_v3.18.md`

Tento dokument vznikol ako dodatok, aby sa nové otázky dali zapracovať do registra v3.18 bez spätného prepisovania starých formulácií.

## Q4 — význam ξ a pasce #7

1. Čo presne je `ξ`: korelačný faktor, podmienená pravdepodobnosť, účinnosť trávenia alebo stavový parameter?
2. Čo znamená limit `ξ → 1`?
3. Čo označuje „pasca #7“ a aká je jej kill condition?
4. Je `ε` amplitúda, pravdepodobnosť na pokus, hazard na čas alebo hustota?
5. Prečo by mali mať zlyhanie a jazva rovnakú pravdepodobnosť `ε_eff`?
6. Koľko elementárnych pokusov prebehne a aký je energetický výťažok jednej jazvy?

**Krok:** vyplniť bránu Q4-P0 v `Q4_problem_epsilon_jazvy_kolaje_K1-K4.md`, potom pokračovať K1.

## Q8 — význam kolapsu

1. Znamená kolaps iba dekoherenciu a stabilný klasický záznam?
2. Alebo teória tvrdí objektívny jednosvetový výber jedného výsledku?
3. Ak ide o objektívny kolaps, odkiaľ pochádza náhodnosť a Bornovo pravidlo?
4. Ktorá presne definovaná entropia dáva šíp času?
5. Kam sa pri vzniku trvalej jazvy uloží energia a informácia?

**Krok:** podľa odpovede pokračovať Q8-K1/K3 alebo Q8-K2/K4 v `Q8_problem_domena_I_kolaje_K1-K4.md`.

## Q11d — gaussovskosť

1. Ktorá mikroskopická premenná sa má stať `ζ`?
2. Aká miera generuje počiatočné mikrostavy?
3. Klesajú korelácie dostatočne rýchlo na použitie centrálnej limitnej vety?
4. Aký bispektrálny tvar a `fNL` model predikuje?

**Krok:** začať K1 v `Q11d_gaussovskost_problem_a_kolaje_K1-K3.md`; bez generátora a mapy na `ζ` sa otázka nedá numericky uzavrieť.

## Q6 — anizotropia rastu

1. Má sa merať BFS front, alebo smerový zákon samotného delenia?
2. Prečo boli čísla z Poissonovho grafu interpretované ako výsledok rastovej siete?
3. Aký je priemer a interval spoľahlivosti cez viac seedov?
4. Prežije trend pri periodických hraniciach?
5. Aký je analytický exponent poklesu anizotropie s N?

**Krok:** multi-seed test K1 podľa `Q6_anizotropia_rastu_problem_a_kolaje_K1-K3.md`.

## Vetva S8–H0

### K1 — prenos hybnosti

1. Ktorá zložka preberá opačnú hybnosť popola?
2. V ktorom rámci je prenos čisto priestorový, teda bez výmeny energie na pozadí?
3. Aká mikrofyzika určuje časovú a škálovú závislosť trenia?

**Krok:** opraviť znamienko trenia a odvodiť covariantné `Q^μ` pred fitovaním veľkosti účinku.

### K2 — rozpadajúci sa popol

1. Rozpadá sa všetok popol alebo iba jeho frakcia?
2. Aké sú dcérske produkty, ich hmotnosti a rozvetvenia?
3. Ako sa súčasne rieši priebežný zdroj nového popola `S_Q`?

**Krok:** zostaviť rovnice pozadia a perturbácií zdroj + rozpad + dcéry.

### K3/K3b — raná entropia

Pôvodná K3 je mŕtva: zvýšenie viditeľného `g*` znižuje `ΔNeff` tej istej odpojenej pary. Nová K3b vyžaduje inú fyziku.

1. Existuje dôvod pre ďalšie stabilné tmavé relativistické stupne?
2. Existuje selektívny neskorý ohrev alebo ne-termálna produkcia pary?
3. Prejde mechanizmus BBN a fázovým posunom CMB píkov?

### K4 — krivosť

1. Akou diskrétnou definíciou sa krivosť meria: Reggeho deficit, Ollivier-Ricci, Forman-Ricci alebo inak?
2. Je vstupný graf vložený do euklidovského priestoru, čím sa plochosť už predpokladá?
3. Prežije priemerná krivosť limit `N → ∞`?

**Krok:** najprv odvodiť alebo zmerať `ΩK` zo siete; až potom robiť CMB+BAO fit.

Podrobný verdikt je v `S8_H0_styri_nove_kolaje_prvotny_audit_2026-07-13.md`.

