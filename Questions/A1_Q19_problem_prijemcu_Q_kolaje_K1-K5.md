# A1/Q19: problém príjemcu prenosu Q — koľaje K1 až K5

**Dátum založenia:** 2026-07-13  
**Aktuálny stav problému:** OTVORENÝ; koľaj A1-K1 prežíva backgroundové testy  
**Metodika:** `00_metodika_kolaji_problemov_a_stavov_v3.18.md`  
**Nahrádza:** požiadavku na jediné okamžité rozhodnutie autora v `A1_rozhodnutie_Q19_a_kovariantny_background_v3.18.md`

## 1. Presný problém

V1 obsahuje prenos

`Q = Γ ρ_f`, kde `Γ = λ H₀ > 0`,

ktorý odoberá energiu palivovej zložke a pridáva ju do spoločnej premennej „hmota“. Spoločná premenná nerozlišuje baryóny, CDM ani prípadnú inú sterilnú zložku.

Otázka Q19 znie:

> Ktorý fyzikálny tenzor energie a hybnosti prijíma Q^μ, aké kvantové čísla nesie vytvorená zložka a v ktorom období je prenos aktívny?

Bez odpovede možno uzavrieť iba účtovníctvo celkovej backgroundovej hustoty. Nemožno korektne vypočítať CMB, rast štruktúr, baryónový podiel ani poruchy.

## 2. Vetva B1: Q priamo vytvára nerelativistickú materiálnu zložku

Táto vetva zachováva jadro V1 a spoločnú rovnicu hmoty:

`ρ_m′ + 3ρ_m = Q/H`.

Koľaje K1 až K5 predstavujú fyzikálne odlišné triedy rozdelenia zdroja. Funkčne nekonečné možnosti vetviacich funkcií patria do rovnakej koľaje, kým majú rovnaký fyzikálny obsah a rovnaké testy.

| Poradie | Koľaj | Definícia | Nové parametre | Počiatočný stav |
|---:|---|---|---:|---|
| 1 | **A1-K1** | `Q_c^μ = Q u_c^μ`, `Q_b^μ = 0`: iba CDM/popol | 0 | `PREŽÍVA` |
| 2 | **A1-K4** | Epochovo alebo stavovo riadené vetvenie: skorý baryónový kanál sa vypne pred BBN, neskôr prijíma Q iba CDM | najmenej 1 prah alebo funkcia | `ČAKÁ` |
| 3 | **A1-K5** | Q vytvára novú sterilnú zložku s, ktorá sa neskôr správa ako CDM alebo sa konvertuje | najmenej 1 nová zložka a konverzia | `ČAKÁ` |
| 4 | **A1-K2** | Pevné vetvenie `Q_b^μ = f_b Q^μ`, `Q_c^μ = (1-f_b)Q^μ`, kde `0 < f_b < 1` | f_b | `ČAKÁ` |
| 5 | **A1-K3** | `Q_b^μ = Q u_b^μ`: iba baryóny | 0, ale nová baryogenéza | `ČAKÁ` |

Poradie je určené počtom nových predpokladov, zhodou s existujúcim skriptom 08 a rizikom konfliktu s BBN/CMB. Nie je to výsledný verdikt.

Ak zomrú A1-K1 až A1-K5, zomiera vetva B1 „priama tvorba materiálnej zložky rovnicou V1“. Potom treba otvoriť novú fundamentálnu vetvu, napríklad interpretáciu Q ako efektívneho gravitačného alebo termodynamického účtovníctva. Taká zmena patrí do rozhodovania o v4.0.

## 3. Spoločné povinné podmienky

| Kód | Podmienka |
|---|---|
| C1 | `∇_μ T_tot^{μν} = 0` bez chýbajúceho alebo dvojito započítaného zdroja |
| C2 | Jednoznačný kovariantný prenosový štvorvektor a jasná znamienková konvencia |
| C3 | Nezáporné fyzikálne hustoty v celom deklarovanom časovom intervale |
| C4 | Zachovaný štandardný limit pri `λ → 0` |
| C5 | Súlad baryónovej histórie medzi baryogenézou, BBN, CMB a dneškom |
| C6 | Určené poruchy prenosu, gauge, zvukové rýchlosti a stabilita pred tvrdením o raste |
| C7 | Reprodukcia backgroundu aj referenčného ΛCDM limitu v tom istom kóde |
| C8 | Plný dátový test nesmie používať spoločnú bezštruktúrnu Ω_m tam, kde dáta rozlišujú baryóny a CDM |

## 4. Predregistrované steny vetvy B1

| Stena | Podmienka |
|---|---|
| W1 Zachovanie | Zdroj sa nevyruší v súčte tenzorov alebo vyžaduje externý nezapočítaný rezervoár |
| W2 Kladnosť | Niektorá fyzikálna hustota sa stane zápornou v deklarovanom intervale pri parametroch potrebných teóriou |
| W3 Baryóny | Koľaj nedokáže súčasne rešpektovať BBN a CMB baryónovú hustotu bez nového neregistrovaného mechanizmu |
| W4 Poruchy | Potvrdená ghostová, gradientová alebo nekontrolovaná superhorizontová nestabilita |
| W5 Dáta | Plný spoločný CMB+BAO+SN+RSD+lensing test vylúči parameter potrebný pre registrované tvrdenia koľaje pri vopred zvolenom štatistickom prahu |
| W6 Mikrofyzika | Vytvorená zložka nemôže niesť požadované kvantové čísla, stabilitu alebo chladnosť bez zmeny definície koľaje |

Presný štatistický prah W5 sa musí zaregistrovať pred plným fitom v kroku A8. Dovtedy nemožno koľaj z dát vyhlásiť ani za vybranú, ani za mŕtvu.

## 5. Aktívna koľaj A1-K1: Q vytvára iba CDM

### 5.1 Definícia

```text
∇_μ T_f^{μν} = -Q^ν
∇_μ T_c^{μν} = +Q^ν
∇_μ T_b^{μν} = C_b^ν
∇_μ T_r^{μν} = C_r^ν

Q^ν = Γ ρ_f u_c^ν
C_b^ν + C_r^ν = 0
```

Členy `C_b^ν`, `C_r^ν` sú iba štandardné kolízne členy baryónov a žiarenia. Bunkový prenos prijíma výhradne CDM.

### 5.2 FRW rovnice

Pre `x = ln a`:

```text
ρ_f′ = -3δρ_f - λ(H₀/H)ρ_f
ρ_c′ = -3ρ_c + λ(H₀/H)ρ_f
ρ_b′ = -3ρ_b
ρ_r′ = -4ρ_r
```

Súčet dáva `ρ_tot′ = -3(ρ_tot + p_tot)`, takže prenos sa vyruší identicky.

### 5.3 Testy A1-K1 vykonané 13. júla 2026

| Test | Metóda | Výsledok | Verdikt |
|---|---|---|---|
| K1-T0 Definícia | Rozdelenie `T_m = T_b + T_c`, `Q^μ ∥ u_c^μ` | Príjemca, smer toku a znamienka sú jednoznačné | **PREŠIEL** |
| K1-T1 Zachovanie | Analytický súčet štyroch kontinuitných rovníc | Zdroj `-Q + Q` sa presne vyruší | **PREŠIEL** |
| K1-T2 Rozmery | `Γ = λH₀`, `Q = Γρ_f` | `[Q] = [ρ]/[t]` | **PREŠIEL** |
| K1-T3 Limita | Nastavenie `λ = 0` | `ρ_c,ρ_b ∝ a^-3`; štandardná neinteragujúca limita | **PREŠIEL** |
| K1-T4 Zhoda s kódom | Porovnanie so skriptmi 08 a 09 | Skript 08 už tvorí iba CDM; pre `X_m = X_b + X_c` zostáva rovnica skriptu 09 presne rovnaká | **PREŠIEL** |
| K1-T5 Kladnosť | RK4, 25 001 bodov, `x ∈ [0,-25]` | `X_f,X_c,X_b,X_r > 0` až po `z ≈ 7.2×10^10` | **PREŠIEL** |
| K1-T6 Baryónové účtovníctvo | Samostatné `X_b′ = -3X_b` | Po skorom vzniku sa komohybné baryónové číslo neskorým Q nemení | **PREŠIEL ŠTRUKTURÁLNE** |
| K1-T7 Poruchy | Vyžaduje A2 | Ešte nebol vykonaný | **ČAKÁ** |
| K1-T8 Plný likelihood | Vyžaduje CLASS/CAMB a A8 | Ešte nebol vykonaný | **ČAKÁ** |

### 5.4 Numerický protokol K1-T5

Použité rovnice sú identické s backgroundom `scripts/09_script_K3_cosmology_pipeline.py`. Spoločná hmota bola algebraicky rozdelená:

```text
X_b = (ω_b/h²) a^-3
X_c = X_m - X_b
```

Vstupy:

| Parameter | Hodnota |
|---|---:|
| H₀ | 66.37 km s^-1 Mpc^-1 |
| h | 0.6637 |
| Ω_m0 | 0.3517 |
| ω_b | 0.02237 |
| λ | 0.15 |
| δ | 0.02297 |
| ΔN_eff | 0.0535 |
| Integrátor | explicitný RK4 |
| Interval | `x = 0` až `-25` |
| Krok | 0.001 |

Výsledky:

| Veličina | Výsledok |
|---|---:|
| X_b0 | 0.0507835 |
| X_c0 | 0.3009165 |
| Dnešný podiel baryónov v celkovej hmote | 0.144394 |
| Podiel baryónov v hmote pri `z_* = 1089.9` | 0.156439 |
| Podiel dnešného CDM vytvorený od z_* do dneška | 0.08995 |
| Asymptotické komohybné CDM pri `x = -25` | 0.273838 |
| Najmenšia hodnota X_c na intervale | 0.300917 |
| Všetky štyri hustoty kladné | áno |

Pri samostatnej kontrole Bianchiho súčtu bol maximálny absolútny zvyšok z plávajúcej aritmetiky `7.63×10^-6` pri raných členoch približne o pätnásť rádov väčších. Relatívna horná hranica zvyšku bola `4.6×10^-15`. Ide o numerické zaokrúhlenie, nie fyzikálny zdroj.

### 5.5 Fyzikálny výsledok prvého kola

A1-K1 **nenarazila na backgroundovú stenu**. Má nulový nový parameter, zachováva baryóny po BBN, je algebraicky kompatibilná s backgroundom skriptu 09 a zhoduje sa s explicitným CDM čítaním skriptu 08.

Numerický test zároveň odhalil merateľný dôsledok: pri aktuálnom modelovom bode vznikne po rekombinácii približne 9 % dnešnej komohybnej CDM hustoty. Kozmický baryónový podiel sa preto zníži približne z 0.1564 pri rekombinácii na 0.1444 dnes. Toto je predikcia koľaje, ktorú treba neskôr otestovať cez CMB, BAO, rast a baryónový podiel v systémoch; zatiaľ nejde ani o potvrdenie, ani o stenu.

### 5.6 Otvorené riziká A1-K1

1. `Q^μ ∥ u_c^μ` odstraňuje kolmý prenos hybnosti do CDM, ale neodstraňuje zdrojové členy z kontinuity porúch.
2. Palivová zložka má `w_f = -1 + δ`, nie presne vákuové `w = -1`; treba určiť jej tlakové poruchy a efektívnu zvukovú rýchlosť.
3. Treba overiť stabilitu a plné CMB/matter-power spektrá.
4. „Popol“ musí mať mikrofyziku dostatočne chladnej, stabilnej a bez zakázaných interakcií.
5. Približne 9 % neskoro vytvoreného CDM musí prejsť dátovým fitom, nie iba backgroundovou kontrolou.

## 6. Aktuálny stav koľají

| Koľaj | Stav | Posledný výsledok | Nasledujúci krok |
|---|---|---|---|
| A1-K1 | **PREŽÍVA** | Prešla T0-T6 na úrovni backgroundu | Zapísať kandidáta A16; potom A2 poruchy |
| A1-K4 | `ČAKÁ` | Netestovaná | Otvoriť, ak K1 narazí na stenu alebo pri neskoršom porovnaní |
| A1-K5 | `ČAKÁ` | Netestovaná | Definovať sterilnú zložku a jej konverziu |
| A1-K2 | `ČAKÁ` | Netestovaná | Predregistrovať f_b a BBN/CMB test |
| A1-K3 | `ČAKÁ` | Netestovaná | Najvyššie riziko BBN/CMB a kvantových čísel |

## 7. Priebežný verdikt

Koľaj A1-K1 sa môže použiť ako **pracovný backgroundový kandidát v3.18**. Ešte nie je `VYBRANÁ`, pretože neprešla poruchami a plným dátovým testom.

Najbližšia práca pokračuje v A1-K1: pripraviť opravenú A16 SK/EN s jasným označením, že koľaj uzatvára iba background. Potom sa otvorí A2-K1 pre gauge-invariantné poruchy tejto konkrétnej koľaje.
