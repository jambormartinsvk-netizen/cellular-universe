# Fyzikálny a numerický audit mŕtvych vetiev A2 (A2_K1 až A2_K5)

**Dátum auditu:** 13. júl 2026  
**Auditor:** Antigravity (Google DeepMind AI)  
**Rozsah:** Analýza mŕtvych koľají A2-K1 až A2-K4 a stavu A2-K5 v zložke `scripts/`  
**Cieľ:** Overiť, či skripty na disku reprezentujú korektný fyzikálny a numerický dôkaz, identifikovať prípadné chyby v starších skriptoch a overiť ich opravu v nasledovníkoch.

---

## 1. Zhrnutie auditu (Executive Summary)

Preverili sme všetkých 23 skriptov prislúchajúcich k vetvám A2_K1 až A2_K5. 
*   **Analytický verdikt:** Súhlasíme s označením koľají A2-K1, A2-K2, A2-K3 a A2-K4 za **MŔTVE**. Ich fyzikálna smrť je nevyhnutná a nezávisí od numerických chýb.
*   **Stav A2-K5/K1:** Koľaj **PREŽÍVA s hodnotením 60/100**, no jej subhorizontová rastová brána je **ČERVENÁ**. Konformná väzba $\beta(\phi)$, ktorá riadi prenos energie na pozadí, nevyhnutne vyvoláva príťažlivú piatu silu ($G_{\text{eff}}/G \approx 5.67$), ktorá zvyšuje zhlukovania hmoty o $+5.2\text{--}5.3\,\%$, čo tlačí $S_8$ nesprávnym smerom (k $0.92$ namiesto požadovaných $0.81$).
*   **Overenie skriptov a chýb:** Preverili sme, že staršie chybové verzie skriptov (ktoré zlyhali na type, konvergencii alebo preklepoch) boli v súlade s archivačnými pravidlami zachované a nahradené plne opravenými verziami. Všetky chyby boli popísané v prísnych Markdown erratách.

---

## 2. Podrobný audit koľají bod po bode

### 2.1 A2-K1: Prenos hybnosti v pokoji tmavej hmoty (CDM-frame)
*   **Hypotéza:** Výmena hybnosti $Q^\mu$ je paralelná s štvor-rýchlosťou CDM ($u_c^\mu$) s konštantným prenosovým koeficientom $\Gamma = \lambda H_0$.
*   **Fyzikálna príčina smrti (M-009):** Superhorizontová relatívna rýchlostná nestabilita. Keďže palivo vákua má rovnicu stavu $w_f = -1 + \delta$, jeho entalpia (inerciálna hustota) $1+w_f = \delta \approx 0.023$ je extrémne malá. Eulerova rovnica prenosu musí deliť prenos hybnosti touto inerciálnou hustotou, čím vzniká divergentný faktor $\Gamma/\delta$. Relatívny rýchlostný mód rastie exponenciálne so zosilnením až **$2.014 \times 10^5$** od rekombinácie po dnešok.
*   **Overenie skriptov:**
    *   `22_script_..._superhorizon_velocity_instability.py`: Obsahoval numerickú nedokonalosť (kroky $10^{-3}$ vs $5\times 10^{-4}$ nedosiahli požadovanú konvergenčnú presnosť exponentu $< 10^{-8}$, dosiahli $3.68 \times 10^{-8}$). Skript bol správne zamietnutý a ponechaný ako stopa.
    *   `23_script_..._converged.py`: **Úspešne opravený.** Použil jemnejšie kroky ($5\times 10^{-4}$ a $2.5\times 10^{-4}$), dosiahol konvergenciu $9.19 \times 10^{-9} < 10^{-8}$ a potvrdil zlyhanie koľaje.
    *   `24_script_..._audit.py`: Symbolicky overil rovnice a nulové limity $\Gamma \to 0$. Všetkých 8 brán je zelených (`PASS`).

---

### 2.2 A2-K2: Striktne barotropické palivo vákua
*   **Hypotéza:** Stotožnenie backgroundového tlakového pomeru $w_f$ s fyzikálnou pokojovou rýchlosťou zvuku paliva: $c_{s,f}^2 = dp_f/d\rho_f = w_f = -0.97703$.
*   **Fyzikálna príčina smrti (M-008):** Katastrofická gradientová nestabilita. Záporná hodnota rýchlosti zvuku na druhej ($c_{s,f}^2 < 0$) mení disperznú vlnovú rovnicu na exponenciálnu expanziu $\propto \exp(|c_s| k \eta)$. 
*   **Overenie skriptov:**
    *   `21_script_A2_barotropic_fuel_gradient_instability.py`: Skript je **fyzikálne a numericky korektný**. Výpočty preukázali, že na malej škále $k = 1.0\,h/\text{Mpc}$ je rastová miera porúch až $2963\,H_0$ (čas zdvojnásobenia poruchy je len $0.0003$ z veku vesmíru). Koľaj je neprijateľná.

---

### 2.3 A2-K3: Prenos hybnosti v pokoji paliva (Fuel-frame)
*   **Hypotéza:** Výmena hybnosti $Q^\mu$ je paralelná s rýchlosťou paliva $u_f^\mu$.
*   **Fyzikálna príčina smrti (M-010):** Zmena referenčného rámca znížila superhorizontový exponent na polovicu ($\Gamma/\delta$), no neodstránila pól malej inerciálnej hustoty paliva $\delta$. Výsledné zosilnenie od rekombinácie je stále neprijateľných **$448.8$**.
*   **Overenie skriptov:**
    *   `25_script_..._superhorizon_velocity_instability.py`: Fyzikálne aj numericky správny, konvergencia dosiahla $9.19 \times 10^{-9} < 10^{-8}$.
    *   `26_script_..._audit.py`: Symbolicky overil algebraickú bilanciu a limity. Všetkých 10 kontrol je zelených (`PASS`).

---

### 2.4 A2-K4: Smer celkovej hybnosti tmavého sektora (Joint energy-frame)
*   **Hypotéza:** Výmena hybnosti $Q^\mu$ je usmernená podľa entalpicky váženého spoločného rámca $u_d^\mu$, kde $(\rho_c + \delta \rho_f) \theta_d = \rho_c \theta_c + \delta \rho_f \theta_f$.
*   **Fyzikálna príčina smrti (M-011):** Determinant dvojrozmernej interakčnej matice relatívnych rýchlostí je striktne záporný: $\det M = -r^2/(1+\delta r) < 0$ pre akýkoľvek hustotný pomer $r = \rho_f/\rho_c > 0$. To garantuje prítomnosť kladného (rastúceho) eigenmódu na superhorizonte. Zosilnenie relatívnej rýchlosti dosahuje **$1.08 \times 10^5$** voči prípadu bez interakcie.
*   **Overenie skriptov:**
    *   `28_script_..._relative_mode.py`: Zlyhal iba pri pokuse o zápis výsledkov do JSON kvôli prítomnosti `numpy.bool_` typov vo výstupe. Rovnice a simulácia prebehli správne.
    *   `29_script_..._serialized.py`: Opravil typy pre JSON. Avšak pre krokovú mriežku $5\times 10^{-4}$ nedosiahol prísnu konvergenčnú bránu $10^{-7}$ (dosiahol $1.39 \times 10^{-6}$) a vyhodnotenie Einsteinovho constraintu v bodoch prechodu cez nulu bolo zle podmienené.
    *   `30_script_..._converged.py`: **Úspešne opravený.** Použil extrémne jemné kroky ($1.25\times 10^{-4}$ a $6.25\times 10^{-5}$), zaviedol globálnu normu constraintov namiesto bodovej a úspešne dokonvergoval na úroveň $8.68 \times 10^{-8} < 10^{-7}$ so splnením všetkých 6 brán.
    *   `31_script_..._frame_endpoint_crosscheck.py`: Správne overil algebraickú zhodu na oboch koncoch vývoja.

---

### 2.5 A2-K5/K1: Kanonická skalárna akcia a konformná väzba
*   **Hypotéza:** Výmena paliva na popol je sprostredkovaná kanonickým skalárnym poľom $\phi$ a meniacou sa hmotnosťou popola $m_c(\phi) = m_c0 A(\phi)$.
*   **Fyzikálny stav (60/100, prežíva s výstrahou):** Superhorizontové relatívne módy sú stabilné, pole $\phi$ má zdravú pokojovú zvukovú rýchlosť $c_s^2 = 1$ a efektívne hmotnosti sú kladné ($m_{\text{eff}}^2 > 0$).
*   **Červená rastová brána:** Conformal coupling $\beta(\phi)$ vyžaduje pre udržanie prenosu dnešnú silnú väzbu $\beta_0 \approx 1.53$. Táto väzba však generuje príťažlivú **piatu silu**, ktorá zosilňuje gravitačné zhlukovania o faktor $1 + 2\beta^2 \approx 5.67$ na subhorizonte. Kvázistatické integrácie ukazujú, že celková hmota rastie o **$+5.2\text{--}5.3\,\%$** rýchlejšie, čo tlačí odhad $S_8$ nahor (k $0.92$ namiesto k pozorovaným $0.81$).
*   **Overenie skriptov a závažné chyby:**
    *   `32_script_..._canonical_scalar_reconstruction.py`: V poriadku. Rekonštrukcia backgroundu je presná s chybou zdroja $< 7\times 10^{-16}$.
    *   `33_script_..._quasistatic_growth_gate.py`: V poriadku. Implementuje a potvrdzuje alarm subhorizontového rastu.
    *   `34_script_..._projection.py`: Obsahoval drobnú nesúvisiacu nezrovnalosť — pri asymetrických chybách KiDS-Legacy zamenil pomenovanie horného a dolného pásma vo výstupe (hoci na samotné počítanie to nemalo vplyv).
    *   `36_script_..._corrected_labels.py`: **Úspešne opravený.** Explicitne rozdelil výstup na formálnu asymetrickú šírku a konzervatívnu širšiu variantu.
    *   `38_script_..._relative_mode.py`: **Odhalil skutočnú chybu v implementácii.** V $0i$ Einsteinovom zdroji a v počiatočnej celkovej hybnosti započítal premennú $X_f$ dvakrát (výraz `X_f E^2 varphi_x^2 / 3` namiesto správneho `E^2 varphi_x^2 / 3 = delta X_f`). Táto chyba viedla k zlyhaniu globálneho 00 constraintu s veľkým rezíduom $0.1066 > 10^{-5}$. Skript bol oprávnene zamietnutý a označený za neplatný.
    *   `39_script_..._enthalpy_fixed.py`: **Úspešne opravený.** Odstránil dvojité započítanie $X_f$, čím stlačil globálne relative rezíduum na bezpečných $1.47 \times 10^{-9} < 10^{-5}$ a potvrdil stabilitu superhorizontových módov pre K5.
    *   `40_script_..._adiabatic_mode.py`: Fyzikálne správny, no krokový rozdiel $1.14 \times 10^{-6}$ mierne nesplnil prísny konvergenčný limit $10^{-6}$.
    *   `41_script_..._adiabatic_mode_converged.py`: **Úspešne opravený.** Zjemnením krokov na $6.25\times 10^{-5}$ a $3.125\times 10^{-5}$ stlačil krokový rozdiel na $2.86 \times 10^{-7}$, čím úspešne prešiel konvergenčnou bránou.
    *   `42_script_..._quasistatic_limit_crosscheck.py`: Potvrdil exaktnú zhodu plných kmitavých koeficientov s kvázistatickým limitom.
    *   `43_script_..._singular_limit.py`: Zlyhal na pythonovskej `AttributeError` chybe kvôli volaniu neexportovanej internej funkcie.
    *   `44_script_..._singular_limit_fixed.py`: **Úspešne opravený.** Použil validované rozhranie `initial_state` a úspešne zreprodukoval analytické škálovanie $\beta \propto \delta^{-1/2}$ pri $\delta \to 0$.

---

## 3. Zoznam kontrolných súčtov a auditná stopa

Všetky preverené erratá a opravy sú zaznamenané s kontrolou SHA-256 v súbore [A2_00_MANIFEST_A_STAV_BALIKA.md](file:///d:/Teoria/Audit/A2_00_MANIFEST_A_STAV_BALIKA.md) a [A2_K5_1_MANIFEST_SHA256.md](file:///d:/Teoria/Audit/A2_K5_1_MANIFEST_SHA256.md).

---

## 4. Záver a fyzikálne odporúčanie auditora

Skripty pre mŕtve koľaje A2-K1 až A2-K4 boli úspešne zreprodukované a **neobsahujú žiadnu skrytú matematickú ani fyzikálnu chybu**, ktorá by zvrátila ich status mŕtvych vetiev. Ich nestability (rýchlostná superhorizontová, resp. gradientová) sú hlbokými vlastnosťami inerciálnej hustoty near-vacuum paliva a barotropického tlaku.

Prevetranie vetvy A2-K5/K1 odhalilo jednu implementačnú chybu v entalpii (skript 38), ktorá však bola úspešne odhalená ochranným 00 constraintom, popísaná v errate a opravená v skripte 39. Upozorňujem však, že koľaj K5/K1 **má pretrvávajúce riziko príliš rýchleho rastu subhorizontových porúch** ($S_8 \to 0.92$) kvôli povinnej piatej sile, čo zrejme povedie k jej budúcej eliminácii, ak CMB likelihood nepreukáže opak.
