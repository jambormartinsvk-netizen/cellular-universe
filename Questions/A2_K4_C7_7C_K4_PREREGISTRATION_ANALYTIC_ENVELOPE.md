# A2-K4 / C7.7c-K4 — predregistrácia analytického obálkového škálovania

## Otázka

Sú všetky 13 zložiek BR3C-b skutočne dynamicky aktívne, keď sa numerická mierka každej zložky neurčí iba z extrémne malej počiatočnej hodnoty, ale z vopred známej analytickej obálky registrovaného Puiseuxovho riešenia?

## Dôvod novej podkoľaje

- K1 s jednotnou absolútnou toleranciou nerozlíšil fyzikálne malé zložky od numerickej nuly.
- K2 s DOP853 a K3 s Radau použili `scale_i = |y_i(x_start)|`; vyššie multipóly však začínajú na veľmi vysokom ráde série a škála sa počas segmentu zmení o mnoho rádov.
- K4 preto odstráni práve tento identifikovaný dôvod zlyhania. Nemení fyzikálne rovnice ani počiatočné módy.

## Zmrazené nastavenie

### Fyzika

Bez zmeny oproti BR3C-b:

- 13-zložkový vektor v synchrónnej gauge,
- NID a NIV, každý v hlbokej a plytkej vetve,
- `U_c = 0` v rozsahu tejto brány,
- bez fotónového šmyku,
- bez voľnej hierarchie nad `L4_fs`; uzáver `L5_fs = 0`,
- rovnaké backgroundy, constraintové definície metrík a interval do `x_final = -18`.

### Analytická referenčná plocha

Koeficientový motor registrovaného rádu vyhodnotí ten istý analytický stav aj na tretej ploche

`x_ref = -18`.

Táto hodnota sa používa **iba na numerickú mierku**, nie ako náhrada numerickej evolúcie, nie ako údaj pre fit a nie ako dôkaz zhody riešenia v koncovom bode.

Pre každú zložku a trajektóriu sa pred behom zmrazí

`scale_i = max(|y_i(x_start)|, |y_i^series(x_ref)|, 1e-300)`.

Integruje sa `w_i = y_i / scale_i`.

### Integrátor a limity

- integrátor: DOP853,
- `rtol = 1e-10`,
- `atol = 1e-12` v normalizovaných premenných,
- rovnaké kontrolné body a `max_step` ako BR3C-b,
- interný limit: 45 s,
- obalový limit auditu: 50 s,
- externý limit: 60 s.

Ak sa limit prekročí, výsledok je `TIMEOUT_UNCLOSED`, nie PASS a nie fyzikálna smrť.

## Brána aktivity

Pre každú z 13 zložiek a každú zo 4 trajektórií musí platiť oboje:

1. `max_checkpoint_abs_rhs_normalized > floor_i`,
2. `max_checkpoint_abs_change_normalized > floor_i`,

kde

`floor_i = max(10*atol, 10*rtol*max_checkpoint_abs_w_i)`.

Musia byť tiež konečné všetky stavy, derivácie, mierky a diagnostiky. Kontroluje sa presný počet aj množina názvov zložiek, nie ich poradie v JSON.

## Nezávislosť tvrdení

- Referenčný seriál určuje iba mierku a nesmie sa započítať ako evolučný PASS.
- Einsteinove `00` a `0i` constrainty použité na definovanie `h_x` a `eta_x` nie sú nezávislé constraintové testy.
- Kladný výsledok C7.7c-K4 znamená iba to, že implementácia dynamicky rieši všetkých 13 deklarovaných zložiek na tomto skorom intervale.
- Neznamená prejdenie G7, plnej Boltzmannovej hierarchie, CMB likelihoodu ani neskorého rastu.

## Vopred stanovené skóre

- úplný PASS všetkých aktivít: **+0,2 bodu**,
- timeout, chyba alebo neúplný výsledok: **+0,0 bodu**,
- fyzikálne nekonečné riešenie alebo prekročenie zmrazeného fyzikálneho stropu: samostatný audit možnej smrti; bez automatického rozsudku.

