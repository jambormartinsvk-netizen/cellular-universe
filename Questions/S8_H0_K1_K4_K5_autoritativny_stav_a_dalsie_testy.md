# S8–H0: autoritatívny stav koľají K1, K4 a K5

**Dátum:** 2026-07-13  
**Zdroj verdiktu:** `../Audit/AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md`

## Register stavov

| Koľaj | Stav | Skóre | Najbližší povinný test |
|---|---|---:|---|
| K1a: konštantné trenie jednej celkovej hmotnej tekutiny | **MŔTVA** | — | nevracať sa k nej |
| K1b: covariantné trenie iba popola | **PREŽÍVA PODMIENEČNE** | 35/100 | odvodiť `Q_i^μ` a oddelené perturbácie |
| K4a: fenomenologická FLRW krivosť | **PREŽÍVA** | 63/100 | plná modelová likelihood vrátane Ωm |
| K4b: krivosť odvodená zo siete | **PREŽÍVA AKO HYPOTÉZA** | 20/100 | nezávislý diskrétny výpočet krivosti |
| K5: kombinácia K1b+K4b | **PREŽÍVA PODMIENEČNE** | 35/100 | až po nezávislom odvodení oboch parametrov |

## K1b-T1 — covariantná brána

Pred ďalším gridom treba určiť:

1. príjemcu energie z paliva;
2. nositeľa protihybnosti trenia;
3. samostatné štvor-rýchlosti baryónov, CDM/popola a sieťovej zložky;
4. rozklad `Q_i^μ = Q_i u^μ + F_i^μ` s `u_μF_i^μ=0`;
5. celkovú konzerváciu `Σ_iQ_i^μ=0`;
6. gauge a počiatočné podmienky perturbácií.

Kým K1b-T1 neprejde, ďalší grid `γ` by iba opakoval mŕtvu K1a.

## K4b-T1 — meranie krivosti zo siete

Treba zvoliť jednu fyzikálnu diskrétnu definíciu a vopred zaregistrovať mapu na `ΩK`:

- Reggeho deficitné uhly na triangulácii;
- alebo inú definíciu s dokázaným kontinuálnym FLRW limitom.

Ollivierova alebo Formanova grafová krivosť sa nesmie automaticky stotožniť s Einsteinovou priestorovou krivosťou bez derivačnej mapy.

Test musí použiť viac N, viac seedov, periodické/uzavreté hranice a extrapoláciu `N→∞`. Cieľové `ΩK=0,005` sa nesmie vložiť do kalibrácie.

## K5 — zákaz post-data predikcie

Toy cieľ `H0=68`, `S8=0,82` sa dá zasiahnuť bodom

$$
\Omega_K=0,0035564,\qquad\gamma=0,0110529.
$$

Tento bod má status **kalibrácia bez prediktívnej váhy**. Do predikčnej tabuľky môže vstúpiť iba vtedy, ak obe hodnoty vzniknú nezávisle od H0 a S8.

## Uzavreté otázky

Nasledujúce otázky už majú konečnú odpoveď:

- Sú dodané gridy numericky reprodukovateľné? **Áno.**
- Je `χ²_3front` platné celkové χ²? **Nie.**
- Je `γ=0,03` priamo 3 % brzdenie popola za e-fold? **Nie.**
- Trafí príklad `(ΩK,γ)=(0,002;0,015)` cieľ 68/0,82? **Nie.**
- Zakazuje GR otvorenú krivosť alebo tmavý prenos hybnosti? **Nie, ak sú zapísané covariantne a stabilne.**

K týmto odpovediam sa netreba vracať bez nového dôkazu alebo novej rovnice.

