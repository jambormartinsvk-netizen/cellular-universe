# Fyzikálny audit položiek zo starého registra: Q4, Q8, Q11d, Q6, ε, m, C a S8

**Dátum auditu:** 2026-07-13  
**Rozsah:** starý register, aktuálny register v3.17, hlavný dokument, súvisiace skripty a priečinok `Nespracovane`  
**Pravidlo verzií:** zverejnené záznamy Zenodo sa spätne neprepisujú; opravy patria do novej verzie a changelogu.

## 1. Výsledok v jednej tabuľke

| Položka | Skutočný stav po audite | Stručný dôvod |
|---|---|---|
| Q4: ε(jazvy), ξ → 1 | **OTVORENÁ; zatiaľ matematicky nedefinovaná** | Symbol ξ sa v korpuse nachádza iba v texte otázky. Nie je definovaný jeho význam, stavový priestor ani rovnica. Aritmetika `ε_eff = λ H0 tP` sedí, ale neodvodzuje mikrofyziku jazvy ani hmotový výťažok. |
| Q8: tri roly domény I | **OTVORENÁ** | Existujú slovné identifikácie jazvy, kolapsu a šípu času, nie mikroskopický operátor. Test koľaje Q8-K1 ukazuje, že dekoherencia vie potlačiť koherencie, ale sama nevyberie jeden objektívny výsledok. |
| Záhada ε/Λ | **Aritmetika správna, fyzikálne odvodenie chýba** | Druhá mocnina rýchlosti na Planckov čas je rádovo blízka `10^-123`; súčin dvoch nezávislých pravdepodobností ani ich nezávislosť však nie sú odvodené. |
| `m = 1/2` | **Podmienené čítanie, nie veta** | Vyplýva len po prijatí `δE ∝ √T` a `T ∝ H`; premostenie na krivostné perturbácie a samotné `T ∝ H` ešte nie sú odvodené. |
| `C = 28` | **Kombinatorika sedí, selekčný mechanizmus chýba** | Počet stavov je správny pre zvolenú množinu. Prečo kapacita vyberá práve túto množinu a nie alternatívu, zostáva Q16b; platí aj look-elsewhere riziko. |
| Q11d: gaussovskosť | **OTVORENÁ a nedefinovaná, nie iba „dorazenie“** | Register neuvádza náhodnú premennú, mieru, rozdelenie, mapu na `ζ`, test ani toleranciu negaussovskosti. |
| Q6: anizotropia rastu | **ČIASTOČNÁ, publikované čísla majú obmedzený význam** | `3,4 % → 2,0 %` sa reprodukuje pre Poissonovu sieť, nie pre režim `grown`. Metrika navyše testuje BFS front z jedného zdroja, nie priamo smerovú anizotropiu rastového zákona. |
| S8 | **Riziko je reálne, ale hodnota 0,874 ešte nie je platná parameter-free predikcia** | Existujúci výpočet neobsahuje úplné perturbácie interagujúcich zložiek ani Boltzmannovu/CMB pipeline. Uvedené počty σ sú iba jednorozmerné rezíduá, nie modelová vierohodnosť. |

## 2. Kontrola pôvodu otázok

Q4 a Q8 nie sú zabudnuté iba v starom registri. Sú označené ako otvorené aj v aktuálnom súbore:

- `Old/05_Methodology_Rules_and_Question_Register_SK.md`;
- `theory/SK/05_Methodology_Rules_and_Question_Register_SK.md`;
- v aktuálnom registri je Q6 čiastočná a záverečná bilancia stále uvádza Q4, Q8, Q6 a Q11d.

Preto ich nemožno označiť za spracované. Tento audit zakladá samostatné dokumenty koľají pre Q4 a Q8.

## 3. Q4 a záhada ε

### 3.1 Čo sa dá overiť

Hlavný dokument používa

$$
\epsilon_{\rm eff}=\lambda H_0 t_P.
$$

Pri `H0 = 66,37 km s^-1 Mpc^-1`, `λ = 0,15` dá uložený skript:

- `ε_eff = 1,7394091927 × 10^-62`;
- `ε_eff² = 3,0255443395 × 10^-124`;
- voči `10^-123` ide o rozdiel faktorom `3,305`, teda o zhodu rádu, nie presnú rovnosť.

Pri `λ = 0,10` je `ε_eff² = 1,3446863731 × 10^-124`, teda faktor `7,437` pod `10^-123`. Číselná „zhoda“ preto nie je invariantná voči zmene jediného fitovaného parametra.

Výpočet je v `scripts/14_script_legacy_Q4_epsilon_S8_arithmetic_audit.py`.

### 3.2 Čo sa tým neoverilo

Rozmerovo je `H0 tP` bezrozmerná rýchlosť na jeden Planckov čas. Jej umocnenie na druhú však samo osebe nedokazuje:

1. že existujú dva štatisticky nezávislé Bernoulliho deje;
2. že prvý dej je zlyhanie a druhý vytvorenie jazvy;
3. že pravdepodobnosti oboch dejov sú rovnaké;
4. že jeden úspešný súbeh vytvorí konkrétnu energiu alebo hmotnosť;
5. že počet pokusov a expanzia siete dávajú pozorovanú hustotu hmoty či vákuovej energie.

Navyše `ξ` nie je v dokumentoch definované mimo samotnej otázky Q4. Výraz `ξ → 1` preto zatiaľ nemá testovateľný fyzikálny význam.

### 3.3 Väzba na A1

V koľaji A1-K1 sa neskorý zdroj Q interpretuje ako tvorba CDM, kým baryogenéza musí byť samostatný skorý mechanizmus. Identifikovať rovnaké neskoré `λ` alebo `ε_eff` s pravdepodobnosťou vzniku baryónovej hmoty by preto bolo nové, zatiaľ nezdôvodnené lešenie.

**Verdikt Q4:** koľaj nie je mŕtva, ale stojí pred definičnou a mikrodynamickou stenou. Najprv treba definovať `ξ`, elementárny dej, mieru pravdepodobnosti, počet pokusov a energetický výťažok.

## 4. Q8: doména I, kolaps a šíp času

Repozitár používa tri interpretácie domény I:

1. nevratná jazva alebo pamäť siete;
2. fyzikálny kolaps vlnovej funkcie;
3. pôvod šípu času.

Chýba však mapa stavov, operátor evolúcie, pravidlo výberu výsledku, Bornova pravdepodobnosť a dôkaz monotónnej entropickej veličiny.

### 4.1 Prvý test najsľubnejšej koľaje Q8-K1

Skript `scripts/15_script_Q8_K1_decoherence_record_channel_audit.py` testuje úplne pozitívny, stopu zachovávajúci dephasing kanál kvbitu.

Výsledky:

- Krausova úplnosť, stopa, hermitovskosť a pozitivita: **PASS**;
- úplné potlačenie mimodiagonálnych členov pri `p = 1`: **PASS**;
- entropia stavu `|+>` narastie z `0` na `1 bit`: **PASS**;
- lokálny kanál nezmení vzdialený redukovaný stav pre Bellov pár: **PASS**, chyba `0`;
- konečný stav má vlastné čísla `(0,5; 0,5)`, čistotu `0,5` a hodnosť `2`.

Posledný bod znamená, že vznikla klasická zmes vo vybranej báze, nie jeden vybraný objektívny výsledok. Dekoherencia preto vie pokryť stabilnú stopu a efektívnu klasickosť, ale sama nedodáva doslovný kolaps ani Bornovo pravidlo pre jednotlivú udalosť.

Toto zodpovedá štandardnému rozlíšeniu medzi dekoherenciou a problémom jedného výsledku; pozri [Zurek – decoherence and einselection](https://arxiv.org/abs/quant-ph/0105127) a [Schlosshauer – decoherence, measurement problem and interpretations](https://arxiv.org/abs/quant-ph/0312059).

**Verdikt Q8:** Q8-K1 prežíva ako mechanizmus efektívnej klasickej jazvy. Pre doslovný objektívny kolaps je nedostatočná; vtedy treba prejsť na koľaj so stochastickou nelineárnou dynamikou alebo preformulovať význam slova „kolaps“.

## 5. Status exponentu m = 1/2

Argument v hlavnom dokumente má tvar:

$$
\delta E \propto \sqrt{T E_P}\sqrt{N}, \qquad T\propto H,
$$

z čoho sa číta amplitúda úmerná `√H` a teda `m = 1/2`.

Audit potvrdzuje iba logickú implikáciu: **ak** platí zvolený fluktuačný zákon, **ak** platí `T ∝ H` a **ak** sa `δE` správne prenesie na normalizovanú krivostnú perturbáciu, potom exponent `1/2` nasleduje. Tieto predpoklady zatiaľ nie sú vetami modelu.

**Korektný status pre v3.18:** „podmienené termodynamické čítanie“, nie odvodená predikcia.

## 6. Status kapacity C = 28

Kombinatorické spočítanie je overiteľné a pre deklarovanú voľbu stavov správne. Fyzikálny problém je selekčný:

- prečo mikrobunka počíta práve bosonické nosiče;
- prečo nepoužiť fermiónové stavy alebo inú záťaž;
- či je kapacita lokálna, globálna alebo efektívna;
- či rovnaký výber prežije test bez použitia pozorovaného `n_s`.

Keďže číslo 28 existovalo pred formuláciou konkrétnej otázky, treba zachovať priznaný look-elsewhere efekt. Bez nezávislej predikcie nie je zhoda dôkazom.

**Korektný status pre v3.18:** „mechanizmom motivovaná kandidátska hodnota; Q16b otvorená“.

## 7. Q11d: gaussovskosť primárnych fluktuácií

Vyhľadanie Q11d a výrazov pre gaussovskosť našlo iba registračné zmienky. Chýba:

- definícia primárnej náhodnej premennej;
- pravdepodobnostná miera nad mikrostavmi;
- korelačná dĺžka a počet nezávislých príspevkov;
- mapa zo sieťových premenných na `ζ(k)`;
- dvojbodová a trojbodová funkcia;
- test `f_NL` a tolerancia odchýlky od Gaussovho rozdelenia.

Preto označenie „dorazenie Q11d“ zľahčuje stav. Centrálna limitná veta sa nedá použiť iba slovne: treba preukázať nezávislosť alebo dostatočne rýchly zánik korelácií a existenciu konečnej variancie.

**Verdikt:** Q11d je samostatný otvorený problém a musí dostať vlastnú definíciu a koľaje.

## 8. Q6: anizotropia siete pri raste

Existujúci skript `scripts/06_script_Q14_light_cone_front_sharpening.py` bol spustený bez úprav.

### 8.1 Reprodukcia publikovaných čísel

| Režim | Žiadané N | Skutočné N | Izotropická metrika |
|---|---:|---:|---:|
| `poisson` | 30 000 | 30 000 | `0,0343253812` |
| `poisson` | 300 000 | 300 000 | `0,0203103163` |
| `grown` | 30 000 | 29 988 | `0,0520197011` |
| `grown` | 300 000 | 299 989 | `0,0326353448` |

Čísla `3,4 % → 2,0 %` sa teda reprodukujú iba v režime `poisson`. Pre rastovú sieť sú v tomto jednom behu približne `5,2 % → 3,26 %`.

### 8.2 Metodické obmedzenia

1. Smery sú v generátore vzorkované izotropne už vstupným rozdelením. Test preto čiastočne overuje vlastný predpoklad.
2. Metrika používa prvý zdroj, jednu pevnú hopovú škrupinu a priemery v oktantoch.
3. Ide o izotropiu BFS signálového frontu, nie priamo o anizotropiu pravdepodobnosti delenia buniek.
4. Použitý je jediný seed a neperiodická kocka s okrajovými efektmi.
5. Malý beh `grown` nenašiel platný zdroj pre štatistiku `χ` (`n_sources_used = 0`), takže časť diagnostiky zlyhala.

**Verdikt:** trend s N je indícia, nie analytický limit. Q6 ostáva čiastočná a publikovaný text musí jasne označiť, že `3,4 % → 2,0 %` patrí Poissonovmu kontrolnému grafu.

## 9. S8: čo je a nie je dnes overené

### 9.1 Pozorovanie

KiDS-Legacy uvádza `S8 = 0,815^(+0,016)_(-0,021)`; pozri [primárnu analýzu KiDS-Legacy](https://arxiv.org/abs/2503.19441). Spoločná analýza KiDS-Legacy + DES Y3 shear + Pantheon+ + DESI Y1 BAO uvádza `S8 = 0,814^(+0,011)_(-0,012)`; pozri [spoločnú analýzu](https://arxiv.org/abs/2503.19442).

### 9.2 Aritmetické rezíduá

Pre KiDS-Legacy a modelové číslo `0,874`:

- delenie hornou chybou `0,016`: `3,69 σ`;
- delenie priemerom asymetrických chýb `0,0185`: `3,19 σ`;
- pri ručne symetrizovanej chybe `0,018`: `3,28 σ`.

Pre číslo `0,859` sú výsledky `2,75 σ`, `2,38 σ` a `2,44 σ`.

To sú iba surové jednorozmerné rozdiely. Nie sú to významnosti získané zo spoločnej likelihood s kovarianciami, nuisance parametrami a parametrami bunkového modelu.

### 9.3 Teoretický status

Existujúca kozmologická pipeline počíta zjednodušený rast na pozadí. Neobsahuje kompletné perturbácie zdroja Q, perturbácie popola a pary, prenosové funkcie ani CMB/BAO/lensing likelihood. Preto zatiaľ nemožno tvrdiť:

- že `S8 = 0,874` je uzavretá predikcia teórie;
- že posun `λ → 0,10` je jediná povolená páka;
- že ostatné vnútromodelové brzdy boli definitívne vylúčené.

Nová vetva štyroch možností S8/H0 je auditovaná samostatne v `Questions/S8_H0_styri_nove_kolaje_prvotny_audit_2026-07-13.md`.

### 9.4 Budúce dáta

K dátumu auditu ešte neexistuje konečný kozmologický výsledok Euclid/LSST, ktorý by túto konkrétnu predikciu rozhodol. Euclid DR1 je plánované na 21. októbra 2026 a termín je označený ako predbežný v [oficiálnom harmonograme Euclid](https://www.cosmos.esa.int/web/euclid/timeline). Rubin LSST začal 30. júna 2026, ale EDP2 je plánované na 27. júla 2026; pozri [začiatok LSST](https://rubinobservatory.org/news/action-rubin-lsst-begins) a [EDP2](https://rubinobservatory.org/events/edp2-release).

## 10. Priorita ďalšej práce

Pôvodné zhrnutie správne upozorňuje, že Q4 a Q8 nie sú vyriešené. Nie je však fyzikálne odôvodnené tvrdiť, že samotné vyriešenie Q4 a Q8 automaticky zvýši globálny pokrok nad konkrétne percento. `P_global ≈ 70 %` nemá definovanú metriku ani neistotu.

Odporúčané poradie:

1. dokončiť A1 a perturbatívnu konzerváciu A2/A3, lebo bez nich sa nedá platne súdiť S8;
2. súbežne otvoriť Q4-P0: presná definícia `ξ`, jazvy a elementárneho deja;
3. preveriť Q8-K1 a rozhodnúť, či „kolaps“ znamená efektívnu dekoherenciu alebo objektívny fyzikálny kolaps;
4. preformulovať Q11d na merateľný problém `P(ζ)`, bispektrum a `f_NL`;
5. zopakovať Q6 s viacerými seedmi, periodickými hranicami a metrikou anizotropie samotného rastového pravidla.

Q4 a Q8 nemusia byť predstierané ako uzavreté pre úzko zameranú v3.18, ale musia byť explicitne označené ako otvorené podmienky platnosti. Ak by v3.18 tvrdila mikroskopické odvodenie hmoty, objektívny kolaps alebo pôvod šípu času, bez ich vyriešenia by bolo tvrdenie neoprávnené.

## 11. Reprodukovateľnosť

Použité uložené skripty:

- `scripts/06_script_Q14_light_cone_front_sharpening.py` — reprodukcia Q6;
- `scripts/14_script_legacy_Q4_epsilon_S8_arithmetic_audit.py` — ε a aritmetika S8;
- `scripts/15_script_Q8_K1_decoherence_record_channel_audit.py` — prvý test Q8-K1;
- `scripts/16_script_S8_H0_four_tracks_screening.py` — prvotné preverenie štyroch nových koľají S8/H0.

Výpočty skriptov 14 až 16 sú aritmetické alebo toy-model testy. Nenahrádzajú Boltzmannov riešič ani štatistickú analýzu dát.

