# K-N1a — spektrum energeticky náročných delení ako zdroj porúch

**Stav:** `ŽIVÁ HYPOTÉZA / bez prideleného skóre`  
**Rodič:** K-N1, Q22.  
**Nie je:** oprava starého `K_MPC=0.05` backgroundu.

## Fyzikálny obsah hypotézy

Každé delenie bunky potrebuje lokálnu energiu, mení väzby siete a podľa
teórie súvisí s tvorbou paliva, popola a pary. Fluktuácie počtu, polohy,
energie a časovania týchto delení preto môžu byť spoločným **zdrojom
porúch** všetkých rezervoárov.

## Spresnenie: čo znamená „`k` kopíruje rozloženie potravy“

Nech `delta rho_food(x,t)` je lokálna odchýlka dostupnej potravy. V
translačne invariantnom lineárnom limite sa jej Fourierova zložka s vlnovým
vektorom `k` nemieša s iným `k`. Preto je fyzikálne prípustné očakávať

```text
delta rho_A(k,t) = T_Af(k,t) delta rho_food(k,t) + xi_A(k,t),
```

kde `A` je palivo, popol alebo para, `T_Af` je odvodený prenos a `xi_A` je
prípadný nový šum delenia. **Teda rovnaké `k` môže byť odtlačkom tej istej
nerovnosti potravy vo všetkých zložkách.** Nemusí však mať rovnakú amplitúdu
ani znamienko: napríklad lokálne minutie paliva a vznik popola môžu byť
antikorelované, kým para môže niesť vlastný oneskorený prenos.

Pozorovateľným obsahom nie je jedno `k`, ale matica korelácií

```text
P_AB(k) = <delta rho_A(k) delta rho_B*(k)>.
```

Korelačná dĺžka potravy by sa prejavila ako peak, cutoff alebo prechod v
`P_food(k)`; až takýto odvodený znak môže definovať `k_*`. Konkrétny mód,
ktorý si numerický runner vyberie (napr. `0.05 Mpc^-1`), zostáva iba jedným
vzorkovaným bodom tohto spektra.

Po coarse-grainingu však konkrétne Fourierovo `k` stále len indexuje jednu
vlnu. Mikrodynamika môže predpovedať distribúciu výkonu `P_S(k)`, korelačnú
dĺžku `ell_*` alebo charakteristický `k_*=1/ell_*`; nesmie vložiť konkrétny
evolvovaný mód `k=0.05 Mpc^-1` do homogénneho `H(a)`.

## Čo by hypotéza musela odvodiť

1. lokálny stochastický zdroj `S(x,t)` pre energetický náklad delenia a
   jeho mapu na `delta rho_f`, `delta rho_ash`, `delta rho_steam`;
2. dvojbodovú koreláciu alebo priamo `P_S(k)`, vrátane amplitúdy, sklonu,
   korelačnej dĺžky a závislostí medzi rezervoármi;
3. gauge-invariantný transfer `S -> zeta` na exact-A1 backgrounde;
4. bezfitové odvodenie každého `k_*`, ak existuje, z konštánt siete a nie
   z výberu pivotu alebo CMB fitu;
5. predikcie `A_s`, `n_s`, running, izokurvatúr, `f_NL`, BBN/CMB a rastu
   štruktúr s jedným zmrazeným súborom vstupov.

## Testy smrti

K-N1a zomrie, ak potrebuje voľne nastaviť `k_*`, amplitúdu alebo koreláciu
len preto, aby trafil CMB; ak dá background závislý od realizovaného `k`; ak
poruší energetický ledger medzi palivom, popolom a parou; alebo ak po
gauge-invariantnom transfere neprejde CMB/BBN/LSS limitmi.

## Vzťah k súčasnému stavu

K-N1a môže dať fyzikálny význam **spektru** porúch a prípadnému odvodenému
scale `k_*`. Nemôže spätne zmeniť historický verdict: staré
`K_MPC=0.05, Phi=1` v K7 používalo pevný mód v backgrounde bez preukázaného
zdrojového spektra, preto zostáva `DO_NOT_USE_PHYSICS`.

Najprv sa táto hypotéza vedie pod Q22; neotvára P5.4 ani G8 a nemení
univerzálny exact-A1 background `D_A1(a)`.

Kauzálne alternatívy „paralelne alebo reťazcovo“ sú explicitne rozdelené na
Q22a-K1 až K7 v `Questions/Q22A_DIVISION_PRODUCT_SEQUENCE_TRACKS_SK.md`.
