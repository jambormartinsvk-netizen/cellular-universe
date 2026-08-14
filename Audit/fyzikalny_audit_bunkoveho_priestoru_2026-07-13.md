# Fyzikálny audit teórie Bunkového priestoru

**Dátum:** 13. júl 2026  
**Auditor:** Codex (OpenAI), fyzikálny a metodický audit  
**Autor teórie:** Martin Jámbor  
**Auditovaná publikovaná verzia:** Zenodo record 2.0, DOI [10.5281/zenodo.21297228](https://doi.org/10.5281/zenodo.21297228), publikované 10. júla 2026  
**Auditované lokálne verzie:** dokumenty v3.17, sprievodca deklarujúci v3.18, existujúci audit v3.18, všetky skripty 06-10 a celý priečinok `Nespracovane`

---

## 1. Účel a význam verdiktov

Cieľom nie je rozhodnúť, či je základná predstava „bunkového priestoru“ esteticky príťažlivá. Cieľom je určiť, ktoré tvrdenia:

1. sú kompatibilné s overenou fyzikou,
2. sú zatiaľ iba hypotézami bez odvodenia,
3. sú v napätí s dátami alebo so štandardnou teoretickou požiadavkou,
4. sú v súčasnej formulácii vnútorne nekonzistentné.

Použité značky:

- **PREŠLO:** tvrdenie je v danom rozsahu matematicky a fyzikálne konzistentné.
- **PODMIENEČNE PREŠLO:** platí iba po explicitne uvedených predpokladoch.
- **OTVORENÉ:** nie je dokázané ani vyvrátené; model zatiaľ nemá potrebnú dynamiku.
- **VÁŽNY NÁLEZ:** tvrdenie sa nesmie prezentovať ako odvodený výsledok, kým nebude opravené.
- **ROZPOR:** dve časti súčasnej teórie nemožno súčasne udržať bez nového mechanizmu.

## 2. Výkonný súhrn

### Celkový verdikt

Teória v súčasnom stave **nie je preukázateľne v rozpore so zachovaním celkovej energie na homogénnom FRW pozadí**, pretože rovnice V1 možno zapísať ako interagujúce tekutiny s opačnými zdrojmi (+Q) a (-Q). To je dobrý a zachovateľný základ.

Zároveň však **nemožno potvrdiť tvrdenie, že teória už neporušuje žiadny známy fyzikálny zákon**. Dôvodom nie je jedna definitívna experimentálna poprava, ale chýbajúci alebo chybný most medzi bunkovou mikrodynamikou a:

- Lorentzovou invarianciou a všeobecnou kovarianciou,
- kozmologickými poruchami interagujúcich zložiek,
- kvantovou mechanikou a kvantovou teóriou poľa,
- termodynamikou ranej zrýchlenej fázy,
- úplným CMB, BAO, supernovovým a rastovým likelihoodom.

Najvážnejšie nálezy sú:

1. **Tepelný gravitónový relikt je v rozpore s deklarovanými približne 1280 e-foldmi.** Neprítomnosť inflatónu neznamená neprítomnosť inflačného riedenia. Každý voľný relikt vytvorený a odpojený pred dlhou kvázi-de Sitterovskou fázou sa zriedi ako (a^{-4}). Hodnota Δ(N_{\rm eff}=0.0535) je správna iba podmienene: ak boli dva gravitónové stupne voľnosti naozaj termalizované a naposledy odpojené po poslednej veľkej produkcii entropie. Súčasná teória tento časový sled nemá.
2. **Kovariantný zápis A16 uzatvára iba pozadie, nie poruchy.** Voľba (Q^\mu=Qu_m^\mu) odstráni prenos hybnosti v pokojovej sústave CDM, ale všeobecne neodstráni zdrojové členy z rovnice kontinuity hustotných porúch. Treba určiť δ(Q), zvukovú rýchlosť paliva, anizotropné napätie, gauge a počiatočné podmienky. Štandardná rastová rovnica V3 preto zatiaľ nie je odvodená.
3. **Lorentzova invariancia nie je dokázaná paritou disperzie.** Parita zakáže nepárne mocniny (k), ale nie preferovanú kozmickú foliaciu, porušenie boostov, birefringenciu, rozdielne väzby polí ani vyššie operátory. Konečne-valentný graf na 3D euklidovskej vrstve nie je to isté ako Lorentzovsky invariantné 4D Poissonovo „sprinkling“.
4. **Predikcia (n_s=0.9656) nie je v súčasnosti odvodená.** Stojí na neodvodených vzťahoch δ(E\propto\sqrt{T E_P N}), (T\propto H) a na neodvodenom prevode lokálnej termálnej fluktuácie na gauge-invariantnú ζ. Navyše vlastný „presný“ vzťah dáva (n_s\simeq0.9643), nie 0.9656.
5. **Skript 09 nie je Boltzmannovský ani globálny kozmologický fit.** Reprodukuje vlastné backgroundové čísla, ale nemôže zatiaľ potvrdiť (S_8), (w_0,w_a), CMB konzistenciu ani relatívnu χ² výhodu modelu.
6. **Tvorba hmoty nie je fyzikálne špecifikovaná.** Model musí rozhodnúť, či (Q) vytvára iba studenú tmavú hmotu, alebo aj baryóny. Druhá možnosť zasahuje baryónovú hustotu medzi BBN, CMB a dneškom a vyžaduje osobitný test; prvá možnosť odporuje popularizačnému tvrdeniu, že priebežne vzniká obyčajná hmota.

### Čo možno bezpečne zachovať

- Presná stredná valencia 3D Poissonovej-Voronoiovej/Delaunayovej siete ⟨(k)⟩ ≈ 15.535 ako geometrický výsledok.
- Algebraické spočítanie 28 bozónových stupňov voľnosti Štandardného modelu pri vysokej teplote.
- Fenomenologické FRW rovnice V1 ako konkrétny model interagujúcej tmavej zložky.
- Skutočnosť, že efektívne rekonštruované (w<-1) nemusí znamenať fundamentálne porušenie NEC.
- Paritu skalárneho grafového Laplaciánu a neprítomnosť nepárnych členov v jeho konkrétnej disperzii.
- No-signalling princíp: kvantová previazanosť sama osebe neprenáša riaditeľný nadsvetelný signál.
- Ochotu teórie registrovať falzifikačné podmienky, ak sa preformulujú na operačné a jednoznačné testy.

## 3. Audit voči overeným fyzikálnym princípom

| Oblasť | Verdikt | Auditný záver |
|---|---|---|
| Zachovanie energie-hybnosti na FRW pozadí | **PREŠLO** | Opačné zdroje ±(Q) dávajú ∇μ(T_{\rm tot}^{\mu\nu}=0). |
| Kovariantnosť porúch | **VÁŽNY NÁLEZ** | A16 neurčuje úplný perturbačný systém; V3 nie je odvodené z A16. |
| Všeobecná relativita | **OTVORENÉ** | Einsteinove rovnice sa v A16 preberajú ako makroskopický zákon. Simulácia Newtonovho (1/r) nie je odvodením GR. |
| Lorentzova invariancia | **VÁŽNY NÁLEZ** | Rotácie a parita nie sú boostová invariancia. 3D graf s globálnym tikom prirodzene definuje preferovaný rámec. |
| Kvantová mechanika | **OTVORENÉ** | Metafora V-spojov neobsahuje Hilbertov priestor, Bornovo pravidlo, unitárny vývoj ani kvantové operátory. |
| No-signalling | **PODMIENEČNE PREŠLO** | „Korelácia bez signálu“ je kompatibilná s QM; model však ešte neodvodzuje kvantové korelácie. |
| Druhý zákon termodynamiky | **OTVORENÉ** | Chýba definícia entropie buniek, paliva, odpadu a celkovej produkcie entropie počas delenia. |
| Gauge symetrie a SM | **OTVORENÉ** | Číslo (g_B=28) je správne spočítané, ale nevytvára gauge dynamiku ani fermióny. |
| BBN/CMB konzistencia | **VÁŽNY NÁLEZ** | Chýba reheating, vznik baryónov, presná história gravitónového reliktu a plná Boltzmannova evolúcia. |
| Kauzalita | **OTVORENÉ** | BFS front na grafe dá konečnú rýchlosť, nie však ešte Lorentzovsky kovariantný svetelný kužeľ pre všetky polia. |

### 3.1 Geometria, ⟨(k)⟩ a réžia δ

Vzorec

\[
\langle k\rangle=\frac{48\pi^2}{35}+2\simeq15.535
\]

je legitímny geometrický výsledok pre ideálnu stacionárnu 3D Poissonovu-Voronoiovu mozaiku. Z neho však automaticky neplynie, že reálny dynamicky rastúci časopriestor musí mať rovnakú lokálnu štatistiku pri každom čase a zakrivení.

Vzťah

\[
\delta=\frac{1}{\langle k\rangle+C}
\]

je **modelový postulát**, nie odvodenie energie prestavby. Počet povrchových hrán a počet interných kvantových stavov možno sčítať až po definovaní spoločnej fyzikálnej jednotky nákladu. Teória zatiaľ nemá Hamiltonián ani akciu, z ktorej by energia jednej novej hrany a jedného interného kanála vyšla rovnaká.

Ďalší problém je Jensenova korekcia. Dokument správne upozorňuje, že ⟨1/(k)⟩ ≠ 1/⟨(k)⟩, ale finálna hodnota používa (1/(\langle k\rangle+C)), nie ⟨1/((k+C))⟩. Ak lokálna réžia závisí od lokálneho stupňa, správny priemer sa musí zmerať priamo na distribúcii (k) vrátane (C).

Tvrdenie v sprievodcovi, že 1 % zmena δ posunie (n_s) o 1.5σ, je numericky nesprávne. Jednopercentná zmena δ dá na prvom ráde Δ(n_s\approx3.45\times10^{-4}), teda približne 0.08σ Planckovej chyby 0.0042 alebo 0.22 z deklarovanej teoretickej chyby 0.0016.

### 3.2 Kapacita (C=g_B=28)

Počet 28 je aritmeticky správny počet vysoko-teplotných bozónových stupňov voľnosti minimálneho Štandardného modelu:

- 16 gluónových polarizácií,
- 8 elektroslabých gauge polarizácií,
- 4 reálne stupne Higgsovho dubletu.

**Neodvodené zostáva**, prečo sa tento počet rovná kapacite jednej bunky, prečo fermióny neprispievajú, prečo sa kapacita nemení pri novej fyzike pod Planckovou škálou a prečo je každý stav jednotkou rovnakej „V-kapacity“.

Porovnanie viacerých kandidátskych počtov s už známym (n_s) vytvára look-elsewhere efekt. Kým nebude mechanizmus (C=28) odvodený nezávisle od kozmologických dát, (n_s) nie je bezparametrická predikcia v silnom štatistickom zmysle.

### 3.3 Lorentzova invariancia a kauzalita

Skript 07 používa skalárny grafový Laplacián, pre ktorý je

\[
\omega^2(k)\propto\sum_e[1-\cos(k\cdot d_e)]
\]

presne párny v (k). To legitímne zakazuje nepárny člen pre tento operátor. Nezakazuje však:

- preferovaný rámec daný globálnym „tikom“ delenia,
- rôzne efektívne metriky pre rôzne polia,
- spinovo závislé a birefringenčné členy,
- porušenie boostov pri zachovaní priestorovej izotropie,
- nelokálne alebo stochastické efekty siete.

Relevantný matematický výsledok pre kauzálne množiny je ešte ostrejší: 4D Lorentzovsky invariantné Poissonovo sprinkling nevyberá preferovaný smer, ale zároveň z neho nemožno Lorentzovsky invariantne vytvoriť lokálny graf s konečnou valenciou. To priamo znamená, že 3D konečne-valentná Delaunayova sieť nemôže používať výsledky kauzálnych množín ako hotový dôkaz boostovej invariancie. Pozri [Bombelli, Henson a Sorkin](https://arxiv.org/abs/gr-qc/0605006).

Meranie GW170817 obmedzuje rozdiel rýchlosti gravitácie a svetla približne na interval (-3\times10^{-15}) až (+7\times10^{-16}) v jednotkách (c), ale zhodná rýchlosť dvoch sektorov v jednom pásme nie je dôkazom celej Lorentzovej grupy. Pozri [spoločnú analýzu LIGO/Virgo/Fermi/INTEGRAL](https://arxiv.org/abs/1710.05834).

**Požadovaná oprava:** teória musí zvoliť jednu z dvoch ciest:

1. fundamentálna 4D Lorentzovská kauzálna štruktúra bez preferovanej foliácie, alebo
2. preferovaný kozmický rámec ako efektívna teória poľa so všetkými dovolenými Lorentz-porušujúcimi operátormi a ich experimentálnymi limitmi.

### 3.4 Gravitácia a ekvivalenčný princíp

Tvrdenie „Newton emergoval s (R^2=0.999)“ je validačný výsledok konkrétneho numerického fitu, nie odvodenie gravitácie. Na potvrdenie súladu s GR treba minimálne:

- odvodiť väzbu všetkých foriem energie na jednu efektívnu metriku,
- získať Poissonovu rovnicu s kalibrovaným (G),
- overiť gravitačné šošovkovanie a rovnosť dynamickej a šošovkovej hmotnosti,
- odvodiť post-Newtonovské parametre, Shapirov delay a perihelový posun,
- odvodiť dve tenzorové polarizácie a ich spätnú reakciu,
- ukázať kontinuálnu limitu k Einsteinovým rovniciam alebo presne priznať, že Einsteinove rovnice sú nezávislý makroskopický postulát.

A16 momentálne používa druhú možnosť: Einsteinove rovnice predpokladá. Preto nemožno súčasne tvrdiť, že GR bola odvodená z bunkovej siete.

### 3.5 Kvantová previazanosť a plošný zákon

Zamietnutie výroku „entanglement bez signálu je logický rozpor“ je správne. Kvantová previazanosť neslúži na riadený nadsvetelný prenos správy.

Z toho však neplynie, že V-spoje realizujú kvantovú mechaniku. Simulácia počíta klasické nezáporné váhy na grafe. Neobsahuje:

- komplexné amplitúdy a fázy,
- tenzorový súčin Hilbertových priestorov,
- unitárny vývoj,
- meracie operátory a Bornovo pravidlo,
- entanglementovú entropiu ani jej monogamiu.

Exponent krížovej grafovej váhy (p\simeq1.97) ukazuje približne plošné škálovanie danej klasickej konštrukcie. Nie je to dôkaz Bekensteinovho-Hawkingovho zákona (S=A/(4l_P^2)): chýba identifikácia váhy s von Neumannovou entropiou aj koeficient (1/4).

## 4. Raný vesmír: (n_s), (r), (N_{\rm eff}) a termodynamika

### 4.1 Presná hodnota (n_s)

Pri deklarovaných hodnotách

\[
\delta=\frac{1}{15.535+28}\simeq0.02297,\qquad
\epsilon=\frac32\delta\simeq0.03446
\]

a pri vlastnom presnom vzťahu teórie

\[
n_s-1=-\frac{\epsilon}{1-\epsilon}
\]

vychádza

\[
n_s\simeq0.9643,
\]

nie 0.9656. Hodnota 0.9656 je iba prvý rád (1-\epsilon). Ak sa menovateľ (1-\epsilon) označuje ako presný, predikcia sa musí verzovane zmeniť; rozdiel nemožno nazvať iba neurčitosťou po skrátení, keď je presný výraz už zvolený.

Ešte dôležitejšie: sklon stojí na týchto neodvodených krokoch:

1. δ(E\propto\sqrt{T E_P}\sqrt N) v údajnom nasýtenom Hagedornovom kanáli,
2. (T\propto H) pri výstupe módu,
3. identifikácia Φ alebo energetickej fluktuácie s gauge-invariantnou krivostnou poruchou ζ,
4. zachovanie poruchy cez koniec zrýchlenej fázy a reheating.

Kým tieto kroky nevyplynú z mikrodynamiky alebo aspoň z uzavretej efektívnej akcie, (n_s) treba označiť ako **podmienený fit mechanizmu**, nie ako odvodenú predikciu.

### 4.2 Exponenciálny potenciál

Kanonické skalárne pole s exponenciálnym potenciálom môže mať pri dominancii poľa škálovacie riešenie s konštantným (w=-1+\lambda_\phi^2/3). To je legitímny efektívny backgroundový model.

V nespracovanom LaTeXu však vzniká konflikt označenia: symbol λ už znamená mieru trávenia 0.10-0.15, kým sklon potenciálu je λφ ≈ 0.262. Musia mať odlišné symboly.

Toto pole navyše nereprodukuje automaticky termálne spektrum V-vrstvy. Ak je iba „dekoratívnym“ backgroundovým ekvivalentom, nesmie sa používať ako dôkaz mikrodynamiky siete.

### 4.3 Kritický rozpor: gravitónová para verzus 1280 e-foldov

Vzorec

\[
\Delta N_{\rm eff}=\frac87\left(\frac{10.75}{g_{*s,\rm dec}}\right)^{4/3}
\]

je štandardný entropický prepočet pre **dva termalizované, bezhmotné bozónové stupne voľnosti**, ktoré sa odpojili pri (g_{*s}=106.75). Pod týmito predpokladmi dá približne 0.0535.

Problém je kozmologická história. Dokument súčasne tvrdí:

- gravitóny sa termalizovali pri Planckovej genéze a okamžite sa odpojili,
- potom nasledovalo približne 1280 e-foldov kvázi-de Sitterovskej éry paliva.

Po odpojení platí ρg ∝ (a^{-4}). Po 1280 e-foldoch by pôvodná zložka bola potlačená faktorom (e^{-5120}), teda prakticky na nulu. Tento výsledok nezávisí od existencie inflatónu; závisí od zrýchlenej expanzie. Aj odborná literatúra o termálnych gravitónoch počas teplej inflácie nachádza dominantnú produkciu pri prechode do radiačnej éry, nie jednoduché prežitie počiatočného kúpeľa; pozri [Montefalcone et al.](https://arxiv.org/abs/2507.08739).

**Verdikt:** E2 v `Nespracovane/krok_D_registrovy_balik.md` sa nesmie zapísať ako zamietnutá námietka. Námietka je fyzikálne legitímna. Predikciu možno zachrániť iba jedným z týchto mechanizmov:

1. para sa vytvorí alebo znovu termalizuje pri konci zrýchlenej fázy,
2. počas celej fázy existuje zdrojový kolízny člen, ktorého riešenie zanechá konečnú reliktnú hustotu,
3. deklarovaných 1280 e-foldov alebo čas odpojenia je nesprávny.

Treba vyriešiť Boltzmannovu rovnicu

\[
\dot\rho_g+4H\rho_g=\mathcal C_g(T,H,\ldots)
\]

cez celú genézu, koniec zrýchlenej fázy a reheating. Bez toho (N_{\rm eff}=3.10), teplota 0.9 K aj 53 GHz nie sú odvodené.

### 4.4 Tenzorový pomer (r)

Odhad Δ(h^2\simeq0.4HT) a následné (r\sim10^{-21}-10^{-19}) nie sú odvodené z kvadratickej akcie tenzorových módov siete. Chýba normalizácia módov, spektrum zdroja, transfer cez reheating a vzťah ku skalárnemu (A_s).

Formulácia „štandardná inflácia predpovedá (r\sim10^{-3}-10^{-2})“ je nepresná. Mnohé inflačné modely dovoľujú podstatne menšie (r). Porovnanie má byť s konkrétnymi modelmi, nie s infláciou ako celkom.

Kill condition je logicky nekonzistentná s tvrdením (r<10^{-10}): potvrdené (r=10^{-6}) by vyvrátilo deklarovanú predikciu o štyri rády, ale nesplnilo by registrovanú smrť (r\ge10^{-3}). Podmienka smrti sa má viazať na horný teoretický limit vrátane neistoty, nie iba na dosah plánovaného experimentu. CMB-S4 cieli na detekciu (r>0.003) pri viac než 5σ alebo limit približne (r<0.001) pri 95 % CL; pozri [CMB-S4 forecast](https://arxiv.org/abs/2008.12619).

### 4.5 Graceful exit, reheating, BBN a baryogenéza

Teória má približný počet e-foldov, ale nemá uzavretý prechod:

- kedy presne skončí (w\simeq-1+\delta),
- ako sa energia paliva zmení na radiačný kúpeľ,
- aká je reheatingová teplota a entropia,
- ako vznikne baryónová asymetria,
- či sa zachová pomer baryónov k fotónom medzi BBN a CMB,
- aké izokurvatúrne módy vzniknú.

Toto nie je detail. Bez uvedeného prechodu nemožno súčasne počítať (A_s), (N_{\rm eff}), BBN ani počiatočné podmienky skriptu 09.

## 5. Neskorá kozmológia a dáta

### 5.1 Čo A16 skutočne dokazuje

Rovnice

\[
\nabla_\mu T_f^{\mu\nu}=-Q^\nu,\qquad
\nabla_\mu T_m^{\mu\nu}=+Q^\nu
\]

zabezpečia celkové zachovanie energie-hybnosti. FRW limita pre (Q=\lambda H_0\rho_f) reprodukuje V1. Toto **prešlo**.

Nevyplýva z toho, že poruchy rastú iba cez zmenu pozadia. Literatúra interagujúcej tmavej energie výslovne ukazuje, že rozličné voľby interakcie dávajú rozličné zvukové rýchlosti, kontinuity porúch a pozorovateľné spektrá; pozri [De-Santiago, Wands a Wang](https://arxiv.org/abs/1209.0563). Pre modely s prenosom úmerným hustote tmavej energie sa rastová funkcia musí korigovať aj cez modifikovanú kontinuitnú rovnicu; pozri [Marcondes et al.](https://arxiv.org/abs/1605.05264).

Treba určiť:

- či (Q^\mu\parallel u_c^\mu) pre CDM alebo spoločnú hmotu,
- δ(Q) v zvolenom gauge,
- (c_{s,f}^2) a anizotropné napätie paliva,
- či palivo klastruje,
- adiabaticitu/izokurvatúru,
- počiatočné podmienky v radiačnej ére.

### 5.2 Ktorá hmota vzniká

V1 má iba spoločnú Ωm, ale fyzika vyžaduje oddeliť minimálne baryóny a CDM:

\[
\nabla_\mu T_b^{\mu\nu}=?,\qquad
\nabla_\mu T_c^{\mu\nu}=?
\]

Odporúčaný konzervatívny variant je:

\[
\nabla_\mu T_b^{\mu\nu}=0,\qquad
\nabla_\mu T_c^{\mu\nu}=+Q^\nu,
\]

aby sa po BBN netvorili nové baryóny. Ak má (Q) tvoriť aj obyčajnú hmotu, treba otestovať baryónovú hustotu z BBN, akustické píky CMB, baryónový podiel v kopách, metalicitu a difúzne žiarenie z vytvorenej hmoty.

### 5.3 Hubbleova konštanta

Skript dáva (H_0\simeq66.37\) km/s/Mpc pre pracovný bod s parou. Toto je reprodukovateľný výsledok jeho zjednodušeného backgroundu, ale nie plného CMB fitu.

Planck v základnom ΛCDM dáva (67.4\pm0.5) km/s/Mpc; pozri [Planck 2018](https://arxiv.org/abs/1807.06209). Lokálna SH0ES vetva dáva (73.17\pm0.86) km/s/Mpc; pozri [Breuval et al.](https://arxiv.org/abs/2404.08038). Novší prehľad viacerých lokálnych trás uvádza kombináciu (73.30\pm0.92) km/s/Mpc, pričom stále žiada ďalšiu kontrolu kovariancií a systematík; pozri [Chen a Wang 2026](https://arxiv.org/abs/2606.26831).

Model je preto v súčasnosti v silnom napätí s lokálnym rebríkom. Formulácia „bez zostávajúcej systematiky“ nie je operačná kill condition, lebo nulovú systematiku nemožno dokázať. Treba vopred určiť konkrétny kombinovaný dataset, likelihood, prah Bayesovho faktora alebo Δχ² a pravidlo pre aktualizácie dát.

### 5.4 (S_8)

KiDS-Legacy meria (S_8=0.815^{+0.016}_{-0.021}) a samo ho označuje za zhodné s Planckom na 0.73σ; pozri [Wright et al.](https://arxiv.org/abs/2503.19441). Modelových 0.859-0.874 je preto stále napätý smerom nahor.

Skript 09 navyše odvodzuje σ₈ iba prenásobením referenčného 0.811 pomerom zjednodušených rastových faktorov. Pri odlišnom (N_{\rm eff}), tvorbe CDM a možných poruchách paliva sa mení prenosová funkcia aj normalizácia. (S_8) treba vypočítať v upravenom CLASS/CAMB od primordiálneho spektra po dnešok.

Kill condition „(S_8\le0.78) A ZÁROVEŇ (w_a\le-0.6)“ umožňuje modelu prežiť aj jasné samostatné vylúčenie jeho predikcie (S_8=0.86-0.87). Každá registrovaná veličina musí mať vlastný test.

### 5.5 DESI, (w_0,w_a) a BAO

Čísla (w_0=-0.752\pm0.057), (w_a=-0.86^{+0.23}_{-0.20}) sú reálne výsledky, ale patria konkrétne kombinácii **DESI DR2 + CMB + DESY5 supernovy**, nie samotnému DESI. Sú silno korelované; nemožno ich vložiť ako dve nezávislé Gaussovské položky do súčtu χ². Pozri [DESI DR2 Results II](https://arxiv.org/abs/2503.14738).

DESI DR2 uvádza, že samotné BAO sú dobre opísané plochým ΛCDM a že preferencia dynamickej tmavej energie vzniká pri kombináciách s CMB a supernovami. To je kompatibilné s opatrnejšou časťou `verdikt_B_BAO_DESI_DR2.md`, ale nie s tvrdením, že jednoduché „3-frontové χ²“ dokazuje prevahu modelu.

DESI dokončil plánované pozorovania 15. apríla 2026; prvé výsledky plného päťročného súboru sa očakávajú v roku 2027, nie už v roku 2026. Pozri [oficiálnu správu DESI](https://www.desi.lbl.gov/2026/04/15/desi-reaches-mapping-milestone-surpassing-expectations/).

### 5.6 Tmavá hmota

Čisto gravitačne interagujúca studená zložka nie je sama osebe v rozpore so známym zákonom. „Popol“ však zatiaľ nie je fyzikálny model častice alebo excitácie. Chýba:

- spin, hmotnostné spektrum a distribučná funkcia,
- mechanizmus produkcie a reliktná abundancia,
- voľná dráha a Tremaine-Gunn/phase-space testy,
- halo a subhalo fenomenológia,
- správanie pri zrážkach kôp,
- dôkaz stability.

Kill condition „akákoľvek negravitačná interakcia tmavej hmoty“ je príliš široká. Detekcia subdominantnej zložky by nevyvrátila automaticky gravitačný popol ako zvyšok DM. Treba definovať, či model tvrdí 100 % DM v jedinej zložke a aký minimálny podiel detekovaného negravitačného komponentu ho vylučuje.

## 6. Audit skriptov 06-10

Skripty boli spustené 13. júla 2026 s Python 3.11, NumPy 2.4.4 a SciPy 1.17.1.

### 6.1 Výsledky behov

| Skript | Reprodukovaný výsledok | Auditný verdikt |
|---|---|---|
| 06 Q14, Poisson 30 000 | χ = 0.322 ± 0.031, iba 2 použité zdroje; ⟨(k)⟩ = 15.3997 | Exponent sedí s deklarovaným oknom, ale README validačné ⟨(k)⟩=15.54-15.58 **neprešlo**. Neperiodická hranica znižuje valenciu. |
| 07 Q12, 100 000 | ⟨(k)⟩ = 15.53468; formula nadhodnotila evolučnú frekvenciu o 6.7-9.4 % | Periodické zošitie prešlo. Parita je vstavaná do kosínusového operátora; test nedokazuje boostovú invarianciu ani univerzálnosť pre SM polia. |
| 08 Q7 | ΛCDM (r_s=144.32) Mpc, (h=0.673); správne znamienko neskorej tvorby | Numerická hračka pre znamienko prešla. Stále obsahuje δ=0.03 a nie je totožná s v3.18 modelom. |
| 09 K3 | ΛCDM 67.30/0.3157; model s parou 66.37/0.3517/(-0.919,-0.612)/0.8745 | Interné backgroundové čísla sa reprodukujú. Nie je to plný CMB/BAO/SN/RSD likelihood ani správny perturbačný výpočet. |
| 10 Q10 | (C=27); spodný štart skončil na 19.98, horný na 27.34; priestorový priemer 24.76; (p=1.97) | Skript nepoužíva deklarované (C=28). Spodná vetva v danom čase nekonvergovala. Fit je z 5 polomerov a krížová váha nie je monotónna (398.9 pri R=0.14, 378.3 pri R=0.18). |

### 6.2 Metodické obmedzenia

**Skript 06:** používa malý počet zdrojov, neperiodickú kocku a fituje mocninu v krátkom okne. Treba periodické hranice, desiatky až stovky zdrojov, bootstrap, viac veľkostí (N) a explicitnú finite-size extrapoláciu.

**Skript 07:** výsledok ω((k))=ω(−(k)) je analytická vlastnosť zvoleného kosínusového Laplaciánu. Fit len na kladných (k) dokonca vracia nenulový efektívny lineárny koeficient 0.0085, lebo lineárny a kvadratický člen sú v krátkom okne korelované. Dôkaz parity má byť analytický; numerika má testovať veľkosť (k^4), izotropiu, scattering a konvergenciu.

**Skript 09:** používa iba θ* kotvu, štandardný (r_s), zjednodušený rast od (z=1000), rovnakú primordiálnu normalizáciu a diagonálne „3-frontové“ χ². Chýba CMB damping tail, lensing, neutrínová hierarchia, baryónová fyzika, supernovy, RSD, korelácie (w_0-w_a), perturbácie interakcie a dôkaz stability.

**Skript 10:** pravidlo je naprogramované tak, aby vkladalo (C/2) medzi dcéry; atraktor preto z veľkej časti testuje vlastnú rekurziu. Priestorová lokalita je genealogická a nie je previazaná s Delaunayovým grafom. Výstup nemožno interpretovať ako kvantovú entanglementovú entropiu.

## 7. Verziovanie a reprodukovateľnosť Zenodo

Read-only Zenodo API 13. júla 2026 potvrdilo:

- názov záznamu: *Quantum Cell Theory of Space: Cosmological Predictions of a Dividing Causal Network Prior to CMB-S4 and DESI Final Results*,
- verzia metadát: **2.0**,
- stav: publikované, otvorený prístup,
- publikácia: 10. júla 2026,
- record DOI: 10.5281/zenodo.21297228,
- concept DOI: 10.5281/zenodo.21286128.

Lokálne kontrolné súčty všetkých 15 publikovaných súborov sa zhodujú so Zenodo **okrem aktuálneho `scripts/09_script_K3_cosmology_pipeline.py`**. Lokálny skript 09 má 4694 bajtov a MD5 `d0cc3a0a842d34558eb66072f14dcada`; Zenodo verzia má 4566 bajtov a MD5 `e3bd9779b6744d00b48140f5ed97ca4b`.

Porovnanie s `Old/09_script_K3_cosmology_pipeline.py` potvrdilo, že po publikácii boli urobené tieto zmeny:

- δ: 0.03 → 0.02297,
- (S_8) kotva: 0.759 ± 0.024 → 0.815 ± 0.019,
- komentáre ku KiDS-Legacy a pôvodu δ.

To znamená, že lokálne výsledky 09 nie sú reprodukciou publikovanej Zenodo pipeline v2. Nová verzia musí mať explicitný changelog a nový Zenodo version DOI.

V repozitári sa súčasne používajú označenia:

- Zenodo metadata 2.0,
- `theory/README.md` v3.17,
- `00_README_EN.md` „record v2“,
- sprievodca „v1.3 zodpovedá teórii v3.18“,
- audit a otázky v3.18.

Odporúčanie: oddeliť **verziu vedeckého modelu**, **verziu Zenodo záznamu**, **verziu kódu** a **verziu popularizačného sprievodcu**.

## 8. Samostatný audit priečinka `Nespracovane`

### 8.1 Súborový verdikt

| Súbor | Verdikt | Podmienka zapracovania |
|---|---|---|
| `A16_kovariantne_zobrazenie_SK.md` | **VLOŽIŤ AŽ PO OPRAVE** | Zachovať background a Bianchiho súčet. Prepísať A16.4: geodetický transfer nemení Eulerovu rovnicu hybnosti, ale všeobecne mení kontinuitu porúch. Doplniť δ(Q), (c_s^2), gauge a baryón/CDM rozdelenie. |
| `A16_covariant_embedding_EN.md` | **VLOŽIŤ AŽ PO OPRAVE** | Rovnaké zmeny ako SK; potom skontrolovať presnú bilingválnu zhodu. |
| `derivacia_ns_opravena_C.tex` | **NEVLOŽIŤ AKO HOTOVÉ ODVODENIE** | Opraviť symbol λφ, používať (n_s=0.9643) pri „presnom“ vzťahu a odvodiť (T\propto H), termálnu kapacitu, ζ, reheating a tenzorovú akciu. |
| `verdikt_B_BAO_DESI_DR2.md` | **PONECHAŤ AKO INTERNÝ PREDBEŽNÝ TEST** | Neoznačovať námietku za „mŕtvu“. Archivovať kód, 13 dátových bodov, plnú kovarianciu a verzie zdrojov. Potom vykonať spoločný BAO+CMB+SN likelihood. |
| `sud_14_slabin_a_latex_ns.md` | **NEVKLADAŤ BEZ PREPÍSANIA** | E2 je nesprávne zamietnutá; GR/QFT námietky nie sú vyriešené registráciou; A16 nerieši poruchy; tvrdenie o štandardnom raste je presilené. |
| `krok_D_registrovy_balik.md` | **PREKLASIFIKOVAŤ** | E1 označiť „znamienko algebraicky správne, rovnica fyzikálne neúplná“; E2 zmeniť na kritickú otvorenú otázku; E3 na predbežný backgroundový test; E4 možno ponechať len ako všeobecný no-signalling fakt. |
| `Kozmologická pipeline 09.txt` | **AKTUALIZOVAŤ** | Opraviť opis vnútornej slučky, odlíšiť (z_*) od drag epochy (z_d), uviesť aproximácie a odstrániť záverečnú konverzačnú otázku. |

### 8.2 Konkrétne chyby, ktoré sa nesmú preniesť do novej verzie

1. „Model nemá infláciu, preto relikt prežije.“ Model má dlhú zrýchlenú kvázi-de Sitterovskú fázu; pre riedenie je rozhodujúce (a(t)), nie názov poľa.
2. „Geodetický prenos nechá lineárne rovnice rastu štandardné.“ Bez prenosu hybnosti zostáva Eulerova časť jednoduchšia, ale kontinuita hustoty a δ(Q) zostávajú.
3. „Bianchiho identita odstránila najväčšiu formálnu slabinu.“ Odstránila iba backgroundovú nekonzistenciu zdrojov; neodvodila akciu siete ani poruchy.
4. „(n_s) je odvodené.“ Nie, kým Q11e a termálno-gauge-invariantný most zostávajú predpokladmi.
5. „BAO námietka zomrela.“ Predbežný test ukazuje, že nízke (H_0) nemusí automaticky zničiť BAO vzdialenosti; bez archivovaného modulu a plného likelihoodu je silnejší výrok neprimeraný.
6. „(f_{\rm NL}\) prvý prechod úspešný.“ Odhad (2/\sqrt{C_V}) nie je výpočet bispektra ζ; Q17 musí zostať otvorená.

## 9. Popularizačný dokument `Bunkovy_Vesmir_Ludskou_Recou.md`

Pred ďalším vydaním treba opraviť najmä:

- „štandardná inflácia predpovedá zistiteľné (r\sim10^{-3}-10^{-2})“ → iba niektoré modely,
- „WIMPy/axióny by mali interagovať s jadrami“ → väzby sú modelovo závislé; DM kandidátov je viac,
- „náhodný 3D graf obchádza Lorentzov problém“ → zatiaľ iba zlepšuje priestorovú izotropiu,
- tabuľka disperzie označuje (N) ako počet hrán, hoci kód normalizuje počtom uzlov,
- párna disperzia neznamená nulovú farebnú disperziu; zostáva kvadratická korekcia,
- presný vzťah pre (n_s) nemožno kombinovať s hodnotou prvého rádu,
- plošný exponent grafovej váhy nie je „presne Bekensteinov limit“,
- Bianchiho identita nezaručuje „bezchybnú integráciu“ celej teórie do GR,
- súbor obsahuje lokálne `file:///d:/...` odkazy, ktoré nefungujú na Zenodo/GitHube; použiť relatívne odkazy,
- tvrdenie o „jednej chybe na (10^{123}) delení“ nemá odvodenú väzbu na pozorovanú baryónovú abundanciu.

## 10. Odporúčaný postup k fyzikálne obhájiteľnej novej verzii

### Fáza 0 - zmrazenie tvrdení a verzií

1. Nevkladať súbory z `Nespracovane` priamo do 04/05.
2. Založiť changelog: publikované v2/v3.17 verzus pracovná v3.18/v3.19.
3. Každú predikciu označiť ako `fundamentálna`, `podmienená mechanizmom`, `fenomenologický fit` alebo `numerická indikácia`.

### Fáza 1 - uzavretý efektívny kozmologický model

1. Rozdeliť (T_m^{\mu\nu}=T_b^{\mu\nu}+T_c^{\mu\nu}).
2. Rozhodnúť, ktorá zložka prijíma (Q^\mu).
3. Určiť δ(Q), (c_{s,f}^2), anizotropné napätie a počiatočné podmienky.
4. Implementovať background aj poruchy v CLASS alebo CAMB.
5. Urobiť stabilitnú analýzu superhorizontových módov, gradientov a ghostov.

### Fáza 2 - raný vesmír

1. Definovať začiatok a koniec zrýchlenej fázy.
2. Odvodiť reheating a entropickú bilanciu.
3. Riešiť Boltzmannovu rovnicu termálnych gravitónov cez celú históriu.
4. Odvodiť kvadratickú akciu/štatistiku skalárnych a tenzorových módov.
5. Vypočítať (A_s,n_s,\alpha_s,r,f_{\rm NL}) a izokurvatúru z jedného mechanizmu.

### Fáza 3 - časopriestor a polia

1. Zvoliť 4D kauzálnu štruktúru alebo explicitný preferovaný rámec.
2. Ukázať kontinuálnu limitu pre aspoň skalár, fermión a gauge pole.
3. Odvodiť univerzálnu metriku, ekvivalenčný princíp a prípustné Lorentz-porušujúce operátory.
4. Oddeliť klasickú grafovú váhu od skutočnej kvantovej entropie.

### Fáza 4 - štatistický audit dát

1. Použiť verejné likelihoody Planck/ACT/SPT, DESI DR2, supernovy, KiDS/DES, RSD a BBN.
2. Zahrnúť kovariancie a nuisance parametre.
3. Porovnať rovnaký dataset a rovnaké priory pre model aj ΛCDM.
4. Zverejniť posterior, evidence/AIC/BIC a posterior predictive checks.
5. Až potom aktualizovať predikčnú tabuľku a kill conditions.

## 11. Prioritný zoznam nálezov

| Priorita | Nález | Podmienka uzavretia |
|---|---|---|
| **P0** | Relikt po 1280 e-foldoch | Boltzmannova história preukáže konečné Δ(N_{\rm eff}). |
| **P0** | Neúplné poruchy A16/V3 | Odvodený gauge-invariantný systém a implementácia v Boltzmannovom kóde. |
| **P0** | Nejasné baryóny verzus CDM | Jednoznačné rovnice (T_b,T_c) a dátový test. |
| **P0** | (n_s) a (r) bez uzavretého mechanizmu | Odvodenie ζ a tenzorov cez exit/reheating. |
| **P1** | 3D graf verzus Lorentz boosty | 4D model alebo preferovaný-frame EFT s limitmi. |
| **P1** | Pipeline 09 nie je likelihood | CLASS/CAMB + verejné dáta a kovariancie. |
| **P1** | V-link nie je kvantový entanglement | Hilbertovský model a entropická veličina. |
| **P2** | Simulačné finite-size a C=27 | Opravené skripty, testy, viac seedov a neistoty. |
| **P2** | Nejednotné verzie | Changelog a nový Zenodo version DOI. |

## 12. Konečný auditný verdikt

Teória Bunkového priestoru má hodnotný fenomenologický základ v podobe interagujúceho FRW backgroundu a užitočnú kultúru evidencie vlastných slepých vetiev. Jej najsilnejšou stránkou je snaha prepojiť viac pozorovateľných veličín jednou štruktúrou.

Vedecká sila tejto väzby je však zatiaľ menšia, než tvrdí dokumentácia. Hodnoty δ a (C) nie sú odvodené z dynamickej akcie; (n_s), (r) a (N_{\rm eff}) stoja na neuzavretých mechanizmoch; rast štruktúr ignoruje povinné poruchy interakcie; Lorentzova invariancia a kvantová mechanika sú zatiaľ analógie, nie vety.

**Odporúčanie auditora:** novú verziu nevydávať ako „dokončenú teóriu bez porušenia známych zákonov“. Vydať ju možno ako **pracovný efektívny model s explicitným registrom kritických otvorených podmienok**, ak sa opraví A16, stiahne sa tvrdenie o odvodenom gravitónovom relikte, (n_s) a (r) sa označia ako podmienené a štatistické tvrdenia sa znížia na úroveň, ktorú skutočne podporujú skripty.

## 13. Primárne zdroje použité pri audite

- [Zenodo record 21297228](https://zenodo.org/records/21297228)
- [Planck 2018 VI - Cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 Results II](https://arxiv.org/abs/2503.14738)
- [KiDS-Legacy cosmic shear](https://arxiv.org/abs/2503.19441)
- [GW170817/GRB170817A speed comparison](https://arxiv.org/abs/1710.05834)
- [Inhomogeneous and interacting vacuum energy](https://arxiv.org/abs/1209.0563)
- [Growth in interacting dark energy](https://arxiv.org/abs/1605.05264)
- [Discreteness without symmetry breaking](https://arxiv.org/abs/gr-qc/0605006)
- [Thermal gravitons from warm inflation](https://arxiv.org/abs/2507.08739)
- [CMB-S4 primordial-wave forecast](https://arxiv.org/abs/2008.12619)
- [SH0ES SMC anchor](https://arxiv.org/abs/2404.08038)
- [DESI survey completion notice](https://www.desi.lbl.gov/2026/04/15/desi-reaches-mapping-milestone-surpassing-expectations/)

