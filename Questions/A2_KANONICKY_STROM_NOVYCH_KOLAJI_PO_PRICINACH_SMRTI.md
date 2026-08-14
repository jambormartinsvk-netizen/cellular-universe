# A2 — kanonický strom nových koľají po analýze príčin smrti

**Dátum:** 2026-07-13  
**Nahrádza pre budúcu prácu názvy:** `K5/K3a`, `K5/K4a`, `K5/K2a`,
`K5/K6`, `A2-K6a`  
**Historické súbory a názvy sa nemažú.**

## 1. Koreň problému

Pitva A2 neurčila, že treba „opraviť K5“. Určila šesť konštrukčných príčin:

| Kód | Príčina |
|---|---|
| C1 | delenie prenosu hybnosti malou entalpiou near-vacuum paliva |
| C2 | stotožnenie backgroundového `w` s fyzikálnym `c_s^2` |
| C3 | neodvodený konštantný tok až do dneška |
| C4 | priamy dvojzložkový ledger bez fyzického nosiča |
| C5 | uzamknutie produkčného toku s trvalou príťažlivou piatou silou |
| C6 | zámena backgroundovej zhody za perturbačný alebo dátový dôkaz |

Nové koľaje sú rovnocenné odpovede na tieto príčiny.

## 2. Kanonické koľaje

| Poradie | Koľaj | Nový mechanizmus | Cielené príčiny | Stav |
|---:|---|---|---|---|
| 1 | **A2-K6** | derivatívna energy+momentum akcia | C1, C2, C4, C5; C6 povinná brána | `PREŽÍVA K6.0 — 40/100` |
| 2 | **A2-K7** | dynamický konečno-entalpický mediátor | C1, C2, C4, potenciálne C5 | `ČAKÁ` |
| 3 | **A2-K8** | lokálna produkcia počtu častíc s konštantnou hmotnosťou | C5; musí uzavrieť C1, C2, C4 | `ČAKÁ` |
| 4 | **A2-K9** | jednotný produkčno-rozptylový operátor | C1, C2, C4, C5 | `ČAKÁ` |
| 5 | **A1-K2/A2-K10** | prah, fáza alebo nukleácia vypínajúca neskorý tok | C3, C5; následne C1, C2, C4, C6 | `ČAKÁ`; backgroundová vetva |

Žiadna z týchto koľají nie je potomkom mŕtvej K5. Spoločným rodičom je
otázka Q20 a filter C1–C6.

## 3. A2-K6 — zdravá energy+momentum akcia

```text
f=-f1(phi)rho_c+eta Z^2,
Z=u_c^mu partial_mu phi.
```

K6.0 už prešla presnou reprodukciou A1 backgroundu, nulovým tlakom CDM a
high-k stabilitou. Nie je to oprava K5: `eta=0` slúži iba ako kontrolný
nulový limit na mŕtvu konformnú akciu. Pre `eta!=0` ide o inú akciu s novým
momentum transferom.

**Nasleduje K6.1:** úplné spoločné perturbácie a presné
`G_cc`, `G_cb`, `G_bc`, `G_bb`. Koľaj zomrie ako M-013, ak zdravý interval
nevytvorí `G_eff,c<=G` bez post-data rušenia.

## 4. A2-K7 — konečno-entalpický mediátor

Palivo neodovzdáva energiu ani hybnosť priamo popolu. Pole alebo prúd `M`
má vlastné `T_M^{mu nu}`, kladnú entalpiu a zdravú disperziu:

```text
rho_M+p_M>0,
c_s,M^2>=0,
Q_f->M+Q_M->c=0.
```

Koľaj zomrie, ak sa po eliminácii mediátora znovu objaví `Gamma/delta`, ak
je mediátor duch/gradientovo nestabilný alebo ak sa jeho nezanedbateľný
background potichu zahodí.

## 5. A2-K8 — produkcia počtu konštantne hmotného popola

```text
nabla_mu(n_c u_c^mu)=S_n,
m_c=constant,
Q_c=m_c S_n.
```

Po vzniku nemá popol povinný skalárny náboj K5. Koľaj však musí odvodiť
creation pressure, spätnú reakciu, šum otvoreného systému a lokálny pôvod
`S_n`. Bez nich by iba zopakovala C4.

## 6. A2-K9 — jeden operátor pre produkciu aj prenos hybnosti

Jeden bunkový mikrofyzický proces musí určiť zdroj počtu aj elastickú výmenu
hybnosti. Dva nezávislé koeficienty fitované po výsledku `S8` koľaj zabijú.
Táto koľaj sa od K8 líši tým, že jej povrchovou stopou je aj odvodená
relaxačná sadzba a Einsteinova relácia medzi šumom a disipáciou.

## 7. A1-K2/A2-K10 — prahový alebo fázový tok

Táto vetva odstraňuje C3 tým, že `Gamma_eff` vzniká z prahu alebo fázového
prechodu a pred neskorým rastom sa vypne. Mení A1-K1, preto musí znovu prejsť
backgroundovou bránou a môže patriť až do verzie 4, ak mení fundament.

## 8. Mapa príčina -> koľaje

| Príčina | Primárna odpoveď | Záložné odpovede |
|---|---|---|
| C1 malá entalpia | K7 | K6, K9 |
| C2 záporný hlavný gradient | K6 | K7, K8/K9 iba po akčnom odvodení |
| C3 konštantný neskorý tok | K10 | žiadna čistá A2 oprava |
| C4 chýbajúci nosič/ledger | K7 | K6, K8, K9 |
| C5 povinná príťažlivá sila | K8 | K6, K7, K9, K10 |
| C6 background nie je dôkaz | A3 pre každú koľaj | bez výnimky |

## 9. Poradie práce

1. dokončiť A2-K6.1;
2. ak zomrie, archivovať M-013 a začať A2-K7;
3. potom A2-K8 a A2-K9;
4. A1-K2/A2-K10 otvoriť ako samostatnú backgroundovú vetvu, nie ako záchranu
   A2-K6;
5. žiadnu mŕtvu koľaj nemať za rodiča novej koľaje iba pre podobnosť názvu.
