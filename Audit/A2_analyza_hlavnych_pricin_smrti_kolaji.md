# A2 — analýza hlavných príčin smrti koľají

**Dátum:** 2026-07-13  
**Rozsah:** A2-K1 až A2-K4 a aktuálne riziko A2-K5/K1  
**Účel:** oddeliť symptómy, bezprostredné príčiny a spoločné konštrukčné korene

## 1. Súhrnná tabuľka

| Koľaj | Stav | Bezprostredná príčina | Hlbší koreň |
|---|---|---|---|
| A2-K1 `Q paralelne u_c` | MŔTVA M-009 | relatívny mód `exp[2 Gamma Delta t/delta]`, zisk `2.014e5` | hybnosť near-vacuum fluidu sa delí malou entalpiou `rho+p=delta rho` |
| A2-K2 barotropická | MŔTVA M-008 | `c_s^2=w=-0.97703<0` | barotropická identifikácia backgroundového `w` s fyzikálnym hlavným gradientovým členom |
| A2-K3 `Q paralelne u_f` | MŔTVA M-010 | mód `exp[Gamma Delta t/delta]`, zisk `448.789` | zmena rámca znížila koeficient, ale neodstránila malú entalpiu ani anti-damping |
| A2-K4 `Q paralelne u_d` | MŔTVA M-011 | `det M<0`, plný zisk voči nulovej väzbe `1.08028e5` | dvojzložková algebraická výmena má nevyhnutný kladný relatívny eigenmód |
| A2-K5/K1 konformná akcia | PREŽÍVA 60/100 | superhorizont zdravý; subhorizontový rast `+5.2–5.3 %` | tok cez meniacu sa hmotnosť zviaže trenie s príťažlivou silou `+2 beta^2` |

## 2. Príčina C1 — malá entalpia near-vacuum paliva

Registrované palivo má

```text
rho_f+p_f=(1+w_f)rho_f=delta rho_f,
delta=0.02297.
```

Fenomenologická fluidná Eulerova rovnica musí prenos hybnosti deliť touto
inerciálnou hustotou. Preto vzniká pomer

```text
Gamma/(1+w_f)=Gamma/delta,
lambda/delta=6.5303.
```

K1 a K3 sa líšia faktorom dva, nie koreňom problému. K4 problém skryla do
entalpicky váženej matice, ktorej determinant zostal záporný pre každé
`rho_f/rho_c>0`.

**Poučenie:** ďalšia koľaj nesmie začať postulovaným `Q^mu` medzi prachom a
near-vacuum fluidom. Musí používať fundamentálne polia alebo konečno-entalpický
mediátor.

## 3. Príčina C2 — barotropická zámena pozadia a propagácie

Hodnota `w=p/rho` určuje background, ale všeobecne neurčuje pokojovú zvukovú
rýchlosť. K2 ich stotožnila:

```text
c_s^2=dp/d rho=w=-0.97703.
```

Výsledkom je záporný koeficient pri `k^2` a rastová miera úmerná `k`. Žiadny
lokálny zdroj bez vlastného kladného hlavného gradientového člena to na
krátkych škálach neopraví.

**Poučenie:** `c_s^2>=0`, kinetická matica a disperzný vzťah musia byť
odvodené z akcie pred kozmologickou integráciou.

## 4. Príčina C3 — konštantný neskorý tok

Všetky fluidné koľaje používali `Gamma=lambda H0` až do dneška. Aj keď je
`Gamma` malé v absolútnych jednotkách, integruje sa cez kozmologický čas a je
veľké voči malej entalpii. K5/K1 ukázala druhú stránku: zachovanie rovnakého
neskorého toku vyžaduje dnes veľkú väzbu `beta_0=1.5288`.

**Poučenie:** časový profil prenosu nemôže byť iba zvolená konštanta. Musí byť
odvodený z lokálneho prahu, fázy alebo hustoty a otestovaný aj na backgrounde.
Ak sa profil zmení, už nejde o čistú A2 uzáveru A1-K1, ale o novú A1 koľaj.

## 5. Príčina C4 — dvojzložkový ledger bez nosiča

K1–K4 nútili energiu a hybnosť preskočiť priamo medzi near-vacuum palivom a
tlakovým prachom. Neexistoval stupeň voľnosti, ktorý by niesol konečnú
entalpiu, relaxoval alebo určoval počiatočné módy. K4 ukázala, že ani
„priemerný“ energy-frame smer túto chýbajúcu fyziku nevytvorí.

**Poučenie:** explicitný mediátor musí mať vlastný `T_mu_nu`; nemožno ho po
odvodení potichu zahodiť, ak nesie nezanedbateľnú energiu alebo hybnosť.

## 6. Príčina C5 — uzamknutie toku a piatej sily

K5/K1 odstránila C1, C2 a C4, preto prešla K5.1. Jej konformná väzba však
realizuje tok zmenou hmotnosti popola:

```text
rho_c=m_c(varphi)n_c,
beta=d ln m_c/d varphi.
```

Tá istá `beta` dáva:

- kladné trenie `beta varphi_x`;
- príťažlivú skalárnu silu;
- `G_eff/G=1+2 beta^2 F`.

Pri pracovnom backgrounde je sila oveľa silnejšia než trenie. Nie je dovolené
ponechať iba priaznivý trecí člen.

**Poučenie:** nový mechanizmus musí oddeliť produkciu počtu častíc od ich
trvalého skalárneho náboja alebo musí odvodiť zdravý momentum-transfer člen,
ktorý dáva `G_eff<=G` bez post-data rušenia.

## 7. Príčina C6 — background nie je perturbačný dôkaz

A1-K1 prešla backgroundovou bilanciou vo všetkých koľajach. Napriek tomu štyri
fluidné uzávery zomreli a akčná uzávera má silné rastové riziko.

**Poučenie:** žiadna budúca hodnota `H0`, `S8` alebo `chi^2` z backgroundovej
pipeline sa nesmie označiť za fyzikálnu predikciu bez odvodených perturbácií a
CMB normalizácie.

## 8. Čo nie je príčina smrti

- výber Newtonovej gauge;
- normalizácia počiatočného relatívneho módu;
- hrubší integračný krok po existencii konvergentného nástupcu;
- samotná existencia energie palivo -> popol na backgrounde;
- filozofické pomenovanie „palivo“ alebo „popol“.

Tieto položky nesmú byť použité na oživenie mŕtvej koľaje.

## 9. Konštrukčný filter pre nové koľaje

Nová koľaj môže vstúpiť do výpočtu iba ak vopred ukáže:

1. žiadny koeficient prenosu hybnosti divergujúci ako `1/(1+w_f)`;
2. kladnú kinetickú maticu a `c_s^2>=0`;
3. lokálnu Bianchiho/Noetherovu bilanciu;
4. explicitný ledger všetkých nosičov;
5. regulárny nulový limit a odvodené počiatočné módy;
6. či realizuje tok zmenou počtu alebo hmotnosti častíc;
7. znamienko a veľkosť efektívnej sily pred fitovaním;
8. jasné priznanie, ak mení A1-K1 a teda patrí do novej backgroundovej vetvy.
