# A2-K4 / C7.7c-K3 — audit normalizovaného behu Radau

## Rozsudok

**TECHNICKY NEUZAVRETÉ; nie fyzikálna smrť K4.**

Podkoľaj C7.7c-K3 zmenila oproti K2 iba integrátor z DOP853 na implicitný Radau. Rovnice, počiatočné stavy, normalizácia `w_i = y_i / |y_i(x_start)|`, tolerancie a brána aktivity ostali nezmenené. Beh sa neuzavrel v povinnom časovom limite.

## Reprodukovateľný výsledok

- evolučný skript: `scripts/144_script_A2_K4_3b_RG_C7_7c_K3_normalized_radau.py`
- nezávislý audit: `scripts/145_script_A2_K4_3b_RG_C7_7c_K3_radau_activity_audit.py`
- interný limit evolúcie: 45 s
- obalový limit auditu: 50 s
- externý limit spustenia: 60 s
- výsledok auditu: `ERROR_UNCLOSED`
- skrátený diagnostický beh s limitom 5 s: `TIMEOUT_UNCLOSED`
- diagnostika SciPy Radau: varovania pretečenia pri zostavení alebo úprave numerického Jacobianu

## Hlavná príčina

Normalizačná mierka K2/K3 bola iba absolútna počiatočná hodnota každej premennej. V registrovaných stavoch nie sú presné nuly, ale počiatočné amplitúdy majú extrémny dynamický rozsah. Napríklad pri hlbokom NIV stave je `|U_fs| ≈ 2.34e6`, kým `|L4_fs| ≈ 3.24e-35`; pomer je približne `7.2e40`. Pri hlbokom NID stave klesá `|L4_fs|` až na približne `1.04e-42`. Naprieč zložkami a módmi preto vznikajú normalizačné faktory s rozsahom približne do `1e48`.

Takáto diagonálna transformácia síce nastaví všetky počiatočné hodnoty blízko jednotky, ale nezaručuje, že zostanú blízko jednotky počas evolúcie. Najmä vyššie multipóly začínajú na veľmi vysokom ráde série a neskôr môžu narásť o mnoho rádov. To zle podmieňuje numerický Jacobian implicitného riešiča.

## Čo tento výsledok nedokazuje

- Nedokazuje nestabilitu fyzikálnych porúch.
- Nedokazuje porušenie Einsteinových constraintov.
- Nedokazuje smrť A2-K4.
- Nedokazuje, že Radau je všeobecne nevhodný; zamieta iba konkrétnu kombináciu Radau a škálovania výhradne počiatočnou amplitúdou.

## Stav podkoľaje

`C7.7c-K3 = TECHNICKÁ SLEPÁ PODKOĽAJ / ERROR_UNCLOSED`.

Skripty ani výsledok sa nemažú. Bránia opakovaniu tej istej zle podmienenej normalizácie.

## Dopad na hĺbku K4

Žiadne body. K4 ostáva živá na **66,5/100** a posledná úplne prejdená hlavná brána ostáva G6. C7.7c-K3 nevytvorila uzavretý kladný ani fyzikálne záporný dôkaz.

