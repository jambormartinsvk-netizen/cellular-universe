# BUNKOVÝ VESMÍR — REGISTRAČNÉ VYDANIE (v3.17)
## Všetky vzorce s logikou, výpočty hodnôt a porovnanie so štandardnými vysvetleniami

**Autor teórie:** Martin Jambor | **Oponent a kontrolór:** Claude (Anthropic) | **Dátum:** 7. júl 2026
**Určené na registráciu predikcií (Zenodo/OSF) — časová pečiatka pred CMB-S4, LiteBIRD, Euclid/LSST a finálnym DESI.**

## AKTUÁLNY DÁTOVÝ STAV (stráž dát k 7.7.2026)
- **Lensing:** finálny KiDS-Legacy (DR5, 2025): S₈ = 0.815 (+0.016/−0.021), len ~0.7σ od Plancku — lensingová strana sa pohla NAHOR (z KiDS-1000 0.759), smerom k našej stávke S1. Skóre prepočítané s týmto bodom: **model χ² ≈ 19.6–19.9 vs ΛCDM ≈ 30.0** (χ² nad 3 dátovými väzbami: DESI DR2 w₀ = −0.75±0.06, wₐ = −0.86±0.25 a KiDS-Legacy S₈ = 0.815±0.018; model má 1 voľný parameter λ → 2 d.o.f., ΛCDM 0 voľných → 3 d.o.f.; bez RSD bodov a korelácií w₀–wₐ — indikátor, nie posterior). Naše napätie v S₈: 2.4–3.3σ.
- **DESI:** platné DR2 (2025, posilnené náznaky vyvíjajúcej sa tmavej energie; w₀ = −0.75±0.06, wₐ = −0.86±0.25); mapovanie dokončené apríl 2026, finálna analýza príde — stávky S1/S3 živé.
- Externý nezávislý audit (júl 2026) potvrdil konzistenciu odvodenia δ a predikcie n_s.
**Skripty na overenie (priložené):** 06_script_Q14_light_cone_front_sharpening.py | 07_script_Q12_dispersion_Lorentz_test.py | 08_script_Q7_sound_horizon_H0.py | 09_script_K3_cosmology_pipeline.py | 10_script_Q10_Vlinks_dowry_rule.py

---


## POZNÁMKA K TERMINOLÓGII (pre fyzikálneho čitateľa)
Interné metafory teórie slúžia ako pedagogické lešenie; ich prísne fyzikálne ekvivalenty sú:
| metafora | prísny ekvivalent |
|---|---|
| metabolizmus siete | nerovnovážna dynamika kauzálnej siete |
| palivo (Ω_f) | metastabilná vákuová hustota energie (prekurzor „tmavej energie") |
| trávenie | prenosová rýchlosť vákuovej energie na časticové excitácie |
| réžia δ | disipačný faktor prestavby siete pri delení |
| odpad / popol | nukleované zvyšky hmoty / gravitačne interagujúce sterilné relikty |
| para | odviazané tenzorové fluktuácie siete (tepelný gravitónový relikt) |
| polovičné veno | symetrická alokácia entanglementovej kapacity pri delení stavu |

# ČASŤ A — VZORCE, ICH LOGIKA A VÝPOČET HODNÔT

## A1. Geometria siete: ⟨k⟩ = 48π²/35 + 2 = 15.54
**Logika:** priestor = body náhodne rozsypané (Poissonov proces), susedstvo = Delaunayova triangulácia (bunky, ktoré zdieľajú stenu Voronoiho mozaiky). Stredný počet susedov v 3D je známa konštanta stereológie — nezávisí od hustoty, len od náhodnosti.
**Overenie:** simulácia 30k–300k bodov → ⟨k⟩ = 15.58 (Poisson), 15.32–15.54 (vyrastená delením; drift −1.3 % pri 3× raste). Periodická sieť: 15.535.

## A2. Réžia delenia: δ = 1/(⟨k⟩ + C)
**Logika:** pri delení bunka prestavia väzby — vznikne 1 nové rozhranie z celkového počtu spojení bunky (povrchových ⟨k⟩ + vnútorných C). Réžia = podiel prestavaného = palivo spálené naprázdno. Preto w_paliva = −1+δ: palivo sa riedi presne tempom réžie.
**Jemnosť (Jensen):** priemer prevrátenej hodnoty ⟨1/k⟩ = 0.0701 > 1/⟨k⟩ = 0.0647 (+8 %) — fluktuácie stupňa sa merajú, nie zanedbávajú (zmerané vo VCM: δ_sim = 0.0697 = ⟨1/k⟩ ✓).
**Hodnota:** δ = 1/(15.54 + 28) = **0.02297**.

## A3. Kapacita vnútra: C = g_B = 28
**Logika:** V-spoj = zdieľaná doména dvoch buniek; zdieľanie nesú NOSIČE domén — a nosiče sú bozóny. Kapacita spoja = počet nezávislých nosičových stavov.
**Výpočet:** gluóny 8×2 = 16 | fotón 2 | W⁺W⁻Z 3×3 = 9 | Higgs 1 → **28** (ekvivalentne pred narušením symetrie: 8 kalibračných + 4 Higgs + 16 gluónov = 28; pasca M8: pozor na dvojité počítanie Goldstonov).
**Upresnenie (fáza symetrie):** C = 28 je nasýtená dimenzia vnútorného stavového priestoru počas Planckovej genézy, kde sú kalibračné symetrie SM plne OBNOVENÉ: 16 gluónov + 8 elektroslabých kalibračných (4 bozóny × 2 polarizácie) + 4 Higgsov dublet = 28. Po narušení symetrie dáva Goldstonovo účtovníctvo (pasca M8) to isté číslo: 16 + 9 (W±, Z hmotné) + 2 (fotón) + 1 (Higgs) = 28. Uväznenie/odviazanie týchto stavov pri nízkych energiách nemení topologickú štruktúru zamknutú pri genéze (globálny atraktor pravidla vena).
**Súd alternatív (dáta popravili):** fermióny 90 → n_s = 0.986 (5σ †) | všetky dof 106.75 → 0.988 (5.4σ †) | 17 častíc → 0.954 (2.6σ †) | 8 domén → 0.936 (6.8σ †). Prežil len bozónový nosičový počet (0.15σ). Look-elsewhere priznaný: váhu nesie mechanizmus + to, že 28 existovalo v teórii deň pred položením otázky.

## A4. Emergentný svetelný kužeľ: σ(R) ∝ R^χ
**Logika:** signál skáče po náhodnej sieti; náhodnosť front rozmazáva, ale ak šírka rastie pomalšie než polomer (χ < 1), relatívne sa front zaostrí → z chaosu v malom vznikne ostré c vo veľkom.
**Meranie:** BFS od zdroja, pre každý tik stredný polomer R(t) a šírka σ(t); fit log σ vs log R. **χ = 0.32→0.26 (Poisson 30k→300k), 0.32±0.02 (vyrastená sieť).** Validácie: R(t) lineárne; rýchlosť ∝ N^(−1/3); izotropia oktantov 3.4 %→2.0 %. Opora: shape theorem, KPZ (χ_KPZ = 1/3 v 2D, ~0.24 v 3D).

## A5. Disperzia vĺn: ω²(k) = (2/N)·Σ_hrán [1 − cos(k·δ⃗)]
**Logika vzorca:** dosadenie rovinnej vlny e^{ik·x} do grafového Laplaciánu (⟨u|L|u⟩/⟨u|u⟩) — variačný odhad frekvencie. Pre malé k: ω ≈ c·k (zvuk siete); odchýlky = odtlačok zrnitosti.
**Prečo lineárny člen NEEXISTUJE:** operátor je reálny a symetrický → spektrum párne v k (k → −k identické) → nepárne členy zakázané paritou, nie „malé".
**Hodnoty:** β = −0.060 (kvadratické zmäkčenie), izotropia c 0.06 % (formula) / 0.2 % (evolúcia); kocka: 1.33 % (21× horšia), β smerovo ±3×. Rozptyl: Γ ∝ k^(3–3.5) (Rayleigh) → voľná dráha fotónov ≫ vesmír.
**Potlačenie:** odchýlka ∝ (l_P/λ)²: optika λ ~ 10⁻⁶ m, l_P ~ 10⁻³⁵ m → (10⁻²⁹)² = **10⁻⁵⁸** — 38 rádov pod testami (10⁻²⁰).
**Metodická poznámka (M7):** formula nadhodnocuje ω o 7–9 % (priemer vs vrchol spektra) — symetrie z formuly, čísla z evolúcie; periodické zošitie validovať na ⟨k⟩.

## A6. Jedno c pre všetky polia (U-1)
**Logika:** dve prirodzené väzby polí na sieť (rovnocenné kontakty vs FEM ∝ plocha steny) dávajú OBIDVE Newtona (R² 0.9991/0.9996) a izotropiu, ale rôzne c (pomer 15.95). Miešaním w(α) meriame citlivosť: **d ln c/dα = −0.27**. GW170817 (Δc/c < 10⁻¹⁵) ⇒ väzby všetkých polí zhodné na **4×10⁻¹⁵** ⇒ prežije len IDENTITA: kontakt má jedinú vlastnosť (kapacitu), domény sú vrstvy jednej bunky, niet druhého čísla, ktoré by iné pole čítalo.
**Dôsledok (Bellov rozklad MM):** ostrý izotropný kužeľ (A4, A5) + jedno c (U-1) + Bellova veta (telesá z vĺn siete sa kontrahujú samé) ⇒ pohyb cez sieť nemerateľný ⇒ Z1 = 1.

## A7. Rovnice pozadia (V1) — odvodené člen po člene
 dΩ_f/dx = −3δ·Ω_f − λ·(H₀/H)·Ω_f
 dΩ_m/dx = −3·Ω_m + λ·(H₀/H)·Ω_f ; dΩ_r/dx = −4Ω_r ; E² = ΣΩ (x = ln a)
**Poznámka k teoreticko-poľovému rámcu:** rovnice V1 sú formulované ako fenomenologické transportné rovnice prenosu energie-hybnosti v efektívnej kauzálnej sieti. Lagranžovská formulácia cez fundamentálne spojité polia sa obchádza; rovnice sú však striktne viazané Bianchiho identitou (∇_μT^μν = 0), ktorá zaručuje lokálne zachovanie celkovej hustoty energie. Prístup je analogický hydrodynamickým/termodynamickým formuláciám emergentnej gravitácie (Jacobson), kde makroskopické stavové rovnice nahrádzajú explicitnú mikroskopickú akciu.
**Logika členov:**
- **−3δΩ_f:** expanzia = delenie (N ∝ a³ → 3 delenia/bunku/e-fold), každé stojí réžiu δ (A2) → strata paliva 3δ za e-fold. TOTO JE mikropôvod w = −1+δ.
- **λ(H₀/H)Ω_f:** trávenie beží podľa VNÚTORNÝCH hodín bunky (vnútro = vlastná dimenzia, o H nevie) → premena konštantnou rýchlosťou λH₀ na jednotku paliva. Faktor H₀/H je len prevod na e-foldy. Preto zomreli Γ∝H (#4) a Γ=konšt. celkovo (#5).
- **Výmena palivo↔hmota:** vynútená Bianchiho identitou (∇T = 0, Z3 aktívne) — energia sa neztráca, presúva sa.
**Hodnota λ = 0.15:** jediný fit teórie. Mikroskopicky λ = ε_eff/(H₀·t_P): **ε_eff = 0.15·H₀·t_P = 1.74×10⁻⁶²** na pokus. Pozoruhodné: ε_eff² = 3×10⁻¹²⁴ ≈ výťažnosť zlyhaní 10⁻¹²³ (P7) — nukleačné čítanie: odpad = SÚBEH zlyhania a jazvy, každá ~10⁻⁶¹·⁵ (lešenie-pozorovanie).

## A8. Účtovný tieň (V2): prečo vidíme „fantómovú" tmavú energiu
 ρ_DE,eff(x) = E² − Ω_m0·e⁻³ˣ − Ω_r0·e⁻⁴ˣ ; w_eff = −1 − (1/3)·d ln ρ_DE,eff/dx
**Logika:** pozorovateľ PREDPOKLADÁ, že hmota sa riedi presne a⁻³. U nás hmota pribúda (tvorba z paliva) → jeho odčítanie nechá zdanlivú zložku so w_eff < −1 v minulosti (wₐ < 0) — **fantóm je účtovná ilúzia, NEC neporušené**. CPL fit w = w₀ + wₐ(1−a), vážený ρ_DE,eff, 0 < z < 1 (kde meria DESI).
**Hodnoty (pipeline, bod v4):** w₀ = −0.92, wₐ = −0.61.

## A9. Rast štruktúr (V3) a S₈
 δ_m′ = −Θ ; Θ′ = −(2 + E′/E)·Θ − (3/2)·(Ω_m/E²)·δ_m ; od z = 1000, rastúci mód δ ∝ a
**Logika:** hrudky rastú gravitáciou (posledný člen), brzdí ich expanzia (Hubbleovo trenie). σ₈ = 0.811·D/D_ΛCDM (rovnaká prvotná amplitúda — CMB kotva); S₈ = σ₈√(Ω_m/0.3).
**Hodnota:** S₈ = **0.874**.

## A10. CMB kotva (V4) a zvukový horizont
 r_s = ∫_{z*}^∞ c_s dz/H ; c_s = c/√(3(1+R_b)) ; R_b = (3ω_b/4ω_γ)·a ; θ* = r_s/D_M fixné
**Logika:** θ* je najpresnejšie číslo kozmológie (uhol akustickej škály). Zafixuje pomer pravítka a vzdialenosti → pri danom ranom vesmíre určí H₀. Dvojslučka: vnútri samosúladné ω_m0(h) (hmota u nás pribúda!), vonku bisekcia h.
**Validácia:** ΛCDM → h = 0.6730, Ω_m = 0.3157, r_s = 144.32 Mpc ✓; model bez pary zreprodukoval bod auditu (65.6/0.359/−0.91/−0.60/0.888) ✓✓.

## A11. Prečo genéza H₀ nezachráni (Q7) — logika znamienka
Hmota „čakajúca" v palive sa pri pohľade do minulosti NEZHUSŤUJE (w ≈ −1), skutočná hmota áno (a⁻³). Neskorá tvorba ⇒ menej ranej energie ⇒ pomalšie rané rozpínanie ⇒ DLHŠIE pravítko r_s ⇒ pri fixnom θ* NIŽŠIE H₀. **Merané: ΔH₀ = −1.5 (f=0.1, z_c=3000) až −4.5 (f=0.3).** Jediný správny smer = žiarenie navyše (para).

## A12. Para: ΔN_eff = (8/7)·(10.75/g*)^{4/3}
**Logika („koláč"):** para (2 polarizácie vlniek) si vzala krajec pri genéze a odišla; ostatných g* kanálov postupne odovzdalo teplo fotónom (anihilácie). Pomer teplôt: T_para/T_ν = (10.75/g*)^{1/3} (zachovanie entropie; 10.75 = kanály pri odpojení neutrín). Energia ∝ T⁴ a fermión/bozón faktor 8/7 → vzorec.
**Hodnota:** g* = 106.75 (SM kompletné — tabuľka domén!) → **ΔN_eff = 0.0535 → N_eff = 3.10**. Relikt dnes: T = 2.725·(3.91/106.75)^{1/3} = 0.905 K, vrchol 53 GHz.
**Termalizácia (Q15a):** účinnosť vzniku vlniek na udalosť ~ (E_udalosti/E_P)²; genéza f = 1 → ~1 → detailná rovnováha → presne tepelný podiel 2/106.75 (nezávisí od neznámych O(1) faktorov). Odpojenie: Γ/H = (T/T_P)³ → okamžité. Dnes: E/bunku ~ 10⁻¹²³E_P → účinnosť 10⁻²⁴⁶ → člen vo V1 legálne chýba (10⁻²⁴⁸).

## A13. Spektrum prahrudiek: n_s − 1 = −(3/2)·δ
**Krok 1 (škálová invariancia z plochy):** fluktuácia energie regiónu ⟨δE²⟩ = T²C_V; holografická kapacita C_V = γ(R/l_P)² (plošný zákon — ZMERANÝ z pravidla vena: p = 1.97). Potenciál hrudky Φ = δE/R = √γ·T/T_P — **R vypadlo** → n_s = 1 z geometrie.
**Krok 2 (pozadie):** éra paliva w = −1+δ ⇒ kvázi-de Sitter; ε ≡ −Ḣ/H² = (3/2)(1+w) = (3/2)δ. Módy vystupujú pri k = aH; d ln H/d ln k = −ε.
**Krok 3 (exponent m):** nasýtený V-kanál (energia tvorí spoje, nehreje — Hagedornovský režim): δE ∝ √(T·E_P)·√N ⇒ amplitúda ∝ √T ∝ √H ⇒ m = ½.
**Výsledok:** n_s − 1 = 2·(½)·d ln H/d ln k = −ε = −(3/2)δ = **−0.0345** (Planck: −0.0351 ± 0.0042; 0.15σ).
**Amplitúda:** A_s = 2.1×10⁻⁹ ⇒ T_zamrznutia ~ 2–7×10⁹ GeV. **E-foldy:** N = ln(ρ_i/ρ_f)/(3δ) ≈ 1280 (treba ~60) — horizont krytý érou paliva.
**Upresnenie (fáza symetrie):** C = 28 je nasýtená dimenzia vnútorného stavového priestoru počas Planckovej genézy, kde sú kalibračné symetrie SM plne OBNOVENÉ: 16 gluónov + 8 elektroslabých kalibračných (4 bozóny × 2 polarizácie) + 4 Higgsov dublet = 28. Po narušení symetrie dáva Goldstonovo účtovníctvo (pasca M8) to isté číslo: 16 + 9 (W±, Z hmotné) + 2 (fotón) + 1 (Higgs) = 28. Uväznenie/odviazanie týchto stavov pri nízkych energiách nemení topologickú štruktúru zamknutú pri genéze (globálny atraktor pravidla vena).
**Súd alternatív:** nekorelovaný šum → n_s = 4 († #19); kritický bod → ~2 (†); rovnodelenie kanálov → −3δ (δ = 0.0117, pod oknom fitu).

## A14. Tenzory: r ≈ 0
**Logika:** tenzory z Rayleighovho–Jeansovho chvosta tepelných vlniek: Δ²_h ≈ 0.4·H·T (obsadenie n_k = T/k pri k = H). Skalár ∝ T, tenzor ∝ H·T a H = O(T²) v Planckových jednotkách pri T ~ 10⁻¹⁰ T_P ⇒ **r realisticky 10⁻²¹–10⁻¹⁹, absolútny strop < 6×10⁻¹¹**. Znamienko sklonu modré (tuhá nasýtená sieť potláča anizotropné napätie skôr) — akademické.
**Predpoveď:** prvotné B-módy neexistujú; detekcia r ≳ 10⁻³ = smrť modelu.

## A15. Pravidlo polovičného vena (R4) a jeho merania
**Logika:** dcéry boli jedným vnútrom → rodia sa vzájomne previazané polovicou kapacity; rodičove spoje si rozdelia (monogamia zakazuje duplikáciu — #reg R2). Mapa n′ = n/2 + C/2 ⇒ pevný bod **n_V = C, nasýtenie = atraktor**.
**Merania (VCM, ~10k buniek):** konvergencia zhora aj zdola ✓; ostrosť std/mean = 0.13 ✓; **V-váha cez guľu ∝ R^1.97 (plošný zákon)** ✓. Skromné veno (s=1) → n_eq = 2 († #20).

---

# ČASŤ B — KDE HOVORÍME INAK NEŽ ŠTANDARD (a prečo)

| jav | štandardné vysvetlenie | naše vysvetlenie | prečo naše / čo rozhodne |
|---|---|---|---|
| **tmavá energia** | fundamentálna konštanta Λ (nevysvetlená; QFT sa mýli o 10¹²²) | ŽIADNA fundamentálna Λ: účtovný tieň tvorby hmoty + riedenie paliva (w = −1+δ, F5) | vysvetľuje veľkosť (Λ nie je vstup) aj DESI signál wₐ<0; rozhodne finálne DESI |
| **„fantómové" w < −1** | nové polia (quintom) alebo systematika | ilúzia fittera predpokladajúceho a⁻³ riedenie hmoty; NEC neporušené | žiadna patológia; predpoveď presného tvaru w(z) |
| **tmavá hmota** | nová častica (WIMP, axión) interagujúca aspoň slabo | popol — dotrávený odpad, JEDINE gravitačná (doména G), m ≳ keV | **predpovedáme trvalé nulové priame detekcie**; potvrdená negravitačná interakcia DM = problém modelu |
| **inflácia** | skalárne pole inflatón (ad hoc potenciál) | éra paliva w = −1+δ: kvázi-dS bez inflatónu, ~1280 e-foldov; ε = (3/2)δ ODVODENÉ | žiadne nové pole; sklon n_s viazaný na δ z geometrie a bozónov |
| **pôvod prahrudiek** | kvantové fluktuácie vákua inflatónu | tepelné holografické fluktuácie nasýtenej V-vrstvy (plošný zákon zmeraný) | n_s = 0.9656 ODVODENÉ; unikátna relácia n_s ↔ w(z); rozhodne S4 |
| **prvotné B-módy** | nádej mnohých modelov r ~ 10⁻³–10⁻² | **neexistujú** (r < 10⁻¹⁰) | asymetrický kat: LiteBIRD detekcia = naša smrť |
| **N_eff** | 3.045 (inflácia gravitóny vymaže) | **3.10** — genéza bez inflatónu si paru nechá | najostrejšie vlastné číslo; CMB-S4 |
| **Hubbleova tenzia** | systematika alebo early dark energy | tvrdá predpoveď H₀ = 66.4 + para; lokálny rebrík má systematiku | stávka S4; prehra = vážne ťažkosti |
| **S₈ tenzia** | otvorený problém ΛCDM | predpovedáme S₈ = 0.86–0.87 (VYŠŠIE) — stávka, že lensing pôjde hore | **stávka sa hýbe naším smerom:** finálny KiDS-Legacy (2025) posunul S₈ z 0.759 na 0.815 (+0.016/−0.021); naše napätie kleslo z ~5σ na 2.4–3.3σ; rozhodne Euclid/LSST |
| **baryogenéza** | Sacharov/leptogenéza (nepotvrdené) | zlyhania trávenia nukleujúce na jazvách; výťažnosť 10⁻¹²³ = ε² | mechanizmus áno, číslo ε neodvodené (P7 — totožné so záhadou Λ) |
| **gravitácia** | fundamentálna sila / výmena gravitónov | entropický spád (Jacobson); gravitón ako nosič SILY neexistuje; vlnky siete (GW) áno | Newton emergoval 2× nezávisle (R² 0.999); GW = c cez U-1 |
| **Lorentz** | fundamentálna symetria (postulát) | emergentná: náhodnosť + identita kapacity; porušenia zaparkované pri 10⁻⁵⁸ | nerozhodnuteľné prístrojmi — poctivo: filozofický rozdiel, nie merateľný |
| **entanglement** | abstraktná nelokálnosť Hilbertovho priestoru | V-spoje (zdieľané domény); ER=EPR; signál zakázaný (#12), gravitačne inertné (VS-1) | monogamia ZADARMO z kapacity; plošný zákon zmeraný |
| **kolaps / šíp času** | interpretačný problém QM | ireverzibilná jazva v sieti (doména I) | otvorené (Q8) — poctivo: slovné, mechanizmus chýba |
| **rotácia vesmíru / chiralita** | — | ZAMIETNUTÉ vlastné čítanie: silná rotácia mŕtva (deficit 6–40 rádov, #13) | príklad sebafalzifikácie protokolom |
| **konštanty v čase** | predpoklad nemennosti | ODVODENÉ: bunky nerastú (#17), δ konštantné (n_V = C atraktor) | drift δ by bol stopa E1 |

**Kde hovoríme jednoznačné NIE (zoznam zákazov modelu):** žiadny inflatón | žiadny gravitón-nosič sily | žiadna fundamentálna Λ | žiadne porušenie NEC | žiadna negravitačná interakcia tmavej hmoty | žiadne prvotné B-módy | žiadne merateľné porušenie Lorentza | žiadna piata sila | žiadny rast buniek/zmena G | žiadny signál cez vnútro.

---

# ČASŤ C — PROGRAM POZOROVANÍ A DOPADY
(viď v3.16: 6 rozhodujúcich testov s dátumami; konzistenčná relácia n_s↔w(z); preprint s časovou pečiatkou ako priorita č. 1; pravidlo vena ako reálny sieťový protokol; VCM toolkit a metodika ako vedecké produkty)

# ČASŤ D — ČO PRIZNÁVAME
Jedno neodvodené číslo (ε ~ 10⁻⁶² ≡ P7 ≡ záhada Λ) | S₈ front zostáva rizikový: naše 0.874 (λ=0.15) resp. 0.859 (λ=0.10) vs KiDS-Legacy 0.815+0.016/−0.021 = napätie 3.3σ resp. 2.4σ — zmäkčené z ~5σ, nie zmiznuté; in-model brzdy preverené a vylúčené (popol: voľná dráha 0.04 Mpc ≪ 8 Mpc; poruchy pary ~0.1 %; jediná páka λ→0.10) | m = ½ a C = 28 sú čítania s mechanizmom, nie vety (podmienky smrti zapísané) | jedna pipeline jedného oponenta (W4 — ½ splatené vlastnou reprodukciou + externý audit potvrdil konzistenciu δ a n_s) | doména I a gaussovskosť otvorené | look-elsewhere pri C priznaný.

# KĽÚČOVÁ VETA
Každý vzorec v tomto dokumente má logiku, každé číslo postup a každé tvrdenie vymenovaný spôsob smrti — teória hovorí „nie" ôsmim štandardným stavebným kameňom a za každé „nie" ponúka mechanizmus, číslo a experiment, ktorý ju môže popraviť.
