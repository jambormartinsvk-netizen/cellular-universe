# Doplnenie otázok a krokov po fyzikálnom audite

**Dátum:** 13. júl 2026  
**Nadväzuje na:** [otazky_a_navrh_krokov_v3.18.md](otazky_a_navrh_krokov_v3.18.md)  
**Auditný základ:** [Fyzikálny audit teórie Bunkového priestoru](../Audit/fyzikalny_audit_bunkoveho_priestoru_2026-07-13.md)

Tento súbor je doplnkom existujúceho registra v3.18. Nové otázky majú prednosť pred priamym zapracovaním priečinka `Nespracovane`, pretože audit v ňom našiel fyzikálne presilené verdikty.

---

## 1. Nové a rozšírené otázky

### Q18: Kedy vzniká gravitónová para vzhľadom na približne 1280 e-foldov?

- **Stav:** KRITICKÁ, OTVORENÁ
- **Váha:** 3
- **Povrchová stopa:** Δ(N_{\rm eff}), dnešná teplota a spektrum gravitónového pozadia.
- **Problém:** Relikt odpojený pri Planckovej genéze sa počas následnej kvázi-de Sitterovskej fázy riedi ako (a^{-4}). Po 1280 e-foldoch je pôvodná hustota prakticky nulová bez ohľadu na neprítomnosť inflatónu.
- **Kritérium uzavretia:** Odvodiť a numericky vyriešiť (\dot\rho_g+4H\rho_g=\mathcal C_g) cez zrýchlenú fázu, exit a reheating. Až výsledok smie určiť Δ(N_{\rm eff}).

### Q19: Ktorú hmotovú zložku vytvára prenos (Q)?

- **Stav:** KRITICKÁ, ROZHODNUTIE AUTORA + FYZIKÁLNY TEST
- **Váha:** 3
- **Možnosti:** iba CDM; baryóny aj CDM v pevnom pomere; iná sterilná zložka.
- **Problém:** Spoločná Ωm skrýva rozdiel medzi baryónmi a tmavou hmotou. Neskorá tvorba baryónov mení porovnanie BBN, CMB a dnešného baryónového podielu.
- **Kritérium uzavretia:** Zapísať samostatné rovnice pre (T_b^{\mu\nu}) a (T_c^{\mu\nu}), odvodiť rozdelenie (Q_b,Q_c) a otestovať BBN+CMB+BAO+klastrový baryónový podiel.

### Q20: Aký je úplný gauge-invariantný systém porúch interagujúcich zložiek?

- **Stav:** KRITICKÁ, OTVORENÁ
- **Váha:** 3
- **Problém:** (Q^\mu=Qu_c^\mu) môže odstrániť prenos hybnosti v CDM rámci, ale neurčuje δ(Q), zvukovú rýchlosť paliva, anizotropné napätie ani kontinuitu hustotných porúch.
- **Kritérium uzavretia:** Odvodiť rovnice v jednom deklarovanom gauge, overiť gauge-invariantné veličiny, stabilitu superhorizontových módov a zhodu implementácie v CLASS/CAMB s analytickými limitami.

### Q21: Čo presne je (T) vo vzťahu (T\propto H)?

- **Stav:** KRITICKÁ, rozšírenie Q11e
- **Váha:** 3
- **Otázky:** Je (T) termodynamická teplota, efektívna Hagedornova teplota, parameter šumu alebo lokálna teplota V-vrstvy? Aká je jej entropia, tepelná kapacita a rovnovážna podmienka?
- **Kritérium uzavretia:** Mikrodynamická alebo efektívna termodynamická rovnica, z ktorej vyjde (d\ln T/d\ln H=1) bez použitia nameraného (n_s).

### Q22: Ako vzniká gauge-invariantná krivostná porucha ζ z δ(E)?

- **Stav:** KRITICKÁ, OTVORENÁ
- **Váha:** 3
- **Problém:** Identifikácia Φ ∼ δ(E/R) nestačí na primordiálne spektrum. Treba vyriešiť constrainty metriky, tlakové poruchy, neadiabatický zdroj a transfer cez exit/reheating.
- **Kritérium uzavretia:** Výpočet (\mathcal P_\zeta(k)), (A_s), (n_s), αs, izokurvatúry a bispektra z jedného uzavretého systému.

### Q23: Aký mechanizmus ukončí éru paliva a reheatuje vesmír?

- **Stav:** KRITICKÁ, OTVORENÁ
- **Váha:** 3
- **Kritérium uzavretia:** Určiť podmienku konca zrýchlenia, reheatingovú teplotu, produkciu entropie, vznik radiačnej dominancie a počiatočné podmienky BBN.

### Q24: Je fundamentálna sieť 3D priestor s globálnym tikom alebo 4D kauzálna štruktúra?

- **Stav:** KRITICKÁ KONCEPČNÁ VOĽBA
- **Váha:** 3
- **Problém:** 3D Poisson-Delaunay na časových rezoch prirodzene vyberá foliaciu. Priestorová izotropia sama nedokazuje Lorentzove boosty.
- **Kritérium uzavretia:** Buď skonštruovať 4D Lorentzovsky invariantný model, alebo priznať preferovaný rámec a odvodiť všetky dovolené Lorentz-porušujúce operátory a ich limity.

### Q25: Ako jedna kapacita zabezpečí univerzálnu väzbu všetkých polí?

- **Stav:** OTVORENÁ
- **Váha:** 3
- **Problém:** Tvrdenie U-1 je identita vložená slovne. Treba ukázať skaláre, fermióny, gauge polia a gravitáciu na rovnakej efektívnej metrike.
- **Kritérium uzavretia:** Kontinuálna limita aspoň troch spinových sektorov, univerzálne (c), ekvivalenčný princíp a absencia birefringencie do experimentálnych limitov.

### Q26: Je krížová V-váha skutočne entanglementová entropia?

- **Stav:** OTVORENÁ
- **Váha:** 2
- **Problém:** Skript 10 simuluje klasické váhy, nie hustotné matice ani von Neumannovu entropiu.
- **Kritérium uzavretia:** Definovať Hilbertove priestory buniek, stav ρ, operáciu delenia, unitárnosť/kanál a vypočítať (S(\rho_A)). Potom porovnať exponent aj koeficient s (A/(4l_P^2)).

### Q27: Aká je lokálna réžia pri fluktuujúcom stupni (k)?

- **Stav:** OTVORENÁ
- **Váha:** 2
- **Problém:** Finále používa (1/(\langle k\rangle+C)), hoci vlastná Jensenova poznámka vyžaduje pri lokálnom pravidle ⟨1/((k+C))⟩.
- **Kritérium uzavretia:** Zmerať rozdelenie (k), lokálny energetický náklad a oba priemery na rastúcej periodickej sieti; vopred určiť, ktorý je fyzikálny.

### Q28: Aký je dynamický význam (C=28) nezávislý od (n_s)?

- **Stav:** OTVORENÁ, rozšírenie Q16b
- **Váha:** 3
- **Kritérium uzavretia:** Odvodiť (C) z lokálnej symetrie/akcie siete pred použitím CMB dát a určiť, čo sa stane pri ďalších bozónových stavoch alebo novej fyzike.

### Q29: Spĺňa bunková dynamika druhý zákon termodynamiky?

- **Stav:** OTVORENÁ
- **Váha:** 2
- **Kritérium uzavretia:** Definovať entropiu paliva, povrchu, vnútra, odpadu a pary; ukázať nezápornú celkovú produkciu entropie pri delení a prenose (Q).

### Q30: Aké sú operačné kill conditions jednotlivých predikcií?

- **Stav:** NUTNÁ METODICKÁ OPRAVA
- **Váha:** 2
- **Problém:** Súčasné podmienky majú medzery: napr. (10^{-10}<r<10^{-3}) odporuje predikcii, ale nezabíja model; (S_8) sa zabíja iba spolu s (w_a); „bez zostávajúcej systematiky“ pri (H_0) nie je rozhodnuteľný výrok.
- **Kritérium uzavretia:** Pre každú veličinu samostatne uviesť dataset, likelihood, prah, zaobchádzanie so systematikou a verziu predikcie.

### Q31: Aký je mikrofyzikálny model „popola“?

- **Stav:** OTVORENÁ, rozšírenie W5
- **Váha:** 2
- **Kritérium uzavretia:** Spin, hmotnosť, distribučná funkcia, stabilita, abundancia, voľná dráha, phase-space obmedzenia, halo a klastrové testy.

### Q32: Aká je kontinuálna limita gravitácie?

- **Stav:** OTVORENÁ
- **Váha:** 3
- **Kritérium uzavretia:** Odvodiť Poissonovu/Einsteinovu limitu, univerzálne (G), šošovkovanie, PPN parametre a dve gravitačné polarizácie. Jasne oddeliť, čo sa odvodzuje a čo sa preberá ako makroskopický postulát.

---

## 2. Tri bezprostredné otázky pre autora

Tieto odpovede určia vetvenie ďalšej práce:

1. **Vytvára člen (Q) iba tmavú hmotu, alebo aj baryóny/obyčajnú hmotu?**
2. **Vzniká gravitónová para pred, počas alebo až na konci približne 1280 e-foldov zrýchlenej fázy?**
3. **Je 3D Delaunayova sieť fundamentálny objekt s preferovaným kozmickým časom, alebo iba priestorový rez ešte nedefinovanej 4D kauzálnej siete?**

Bez týchto troch rozhodnutí sa nedá bezpečne navrhnúť nová verzia rovníc ani pipeline.

---

## 3. Revidovaný plán krokov po audite

| Nový krok | Úloha | Výstup | Podmienka pokračovania |
|---|---|---|---|
| A0 | Zmraziť v3.17/Zenodo v2 a založiť changelog | Jedna mapa verzií a kontrolných súčtov | Žiadne tiché prepisovanie registrovaných čísel |
| A1 | Rozhodnúť Q19 a prepísať A16 | Kovariantné (T_f,T_b,T_c,T_r), (Q^\mu) | Background aj celkové zachovanie energie sedia |
| A2 | Odvodiť poruchy Q20 | Gauge-invariantné rovnice + test stability | Žiadne ghost/gradient/superhorizontové nestability |
| A3 | Implementovať CLASS/CAMB | CMB, matter power, lensing, (f\sigma_8) | Reprodukcia ΛCDM v tom istom kóde |
| A4 | Vyriešiť Q18 a Q23 | História pary, exit a reheating | Δ(N_{\rm eff}) vznikne výpočtom, nie dosadením |
| A5 | Vyriešiť Q21-Q22 | (A_s,n_s,r,\alpha_s,f_{\rm NL}) | Jedna konzistentná normalizácia skalárov aj tenzorov |
| A6 | Rozhodnúť Q24-Q25 | 4D kauzálny model alebo preferred-frame EFT | Experimentálne limity Lorentza a ekvivalencie splnené |
| A7 | Opraviť skripty 06-10 | Testy, seedy, neistoty, (C=28), periodické hranice | README validačné hodnoty prejdú automaticky |
| A8 | Plný dátový fit | Verejný likelihood a posterior | Až potom nová tabuľka predikcií a kill conditions |

### Zmena verdiktu k pôvodným krokom A-E

- **Pôvodný krok A (A16):** nevkladať v aktuálnej podobe; opraviť poruchy a baryón/CDM rozdelenie.
- **Pôvodný krok B (BAO):** ponechať ako interný backgroundový smoke test; archivovať chýbajúci kód a kovarianciu; nevydávať ako plný dátový verdikt.
- **Pôvodný krok C ((n_s)):** nevkladať ako hotové odvodenie; presný vzťah znamená 0.9643 a Q11e/Q21/Q22 zostávajú kritické.
- **Pôvodný krok D (register):** E2 neklasifikovať ako zamietnuté; E1 a E3 znížiť na čiastkové verdikty; Q17 ponechať otvorenú.
- **Pôvodný krok E:** nemožno iba vybrať prvý alebo druhý rád. Ak sa používa presná rovnica, hodnota 0.9643 je matematický dôsledok; 0.9656 môže zostať iba historickou registrovanou aproximáciou v changelogu.

---

## 4. Verdikt pre každý súbor v `Nespracovane`

| Súbor | Verdikt |
|---|---|
| `A16_kovariantne_zobrazenie_SK.md` | Vložiť až po oprave porúch a rozdelení baryóny/CDM. |
| `A16_covariant_embedding_EN.md` | Rovnaký verdikt; až potom overiť preklad proti SK. |
| `derivacia_ns_opravena_C.tex` | Nevkladať ako hotové odvodenie; (T\propto H), ζ, exit a tenzory nie sú odvodené. |
| `verdikt_B_BAO_DESI_DR2.md` | Ponechať ako interný backgroundový test; archivovať kód/dáta/kovarianciu. |
| `sud_14_slabin_a_latex_ns.md` | Prepísať; námietka k reliktu je legitímna a A16 nerieši poruchy. |
| `krok_D_registrovy_balik.md` | Preklasifikovať E1-E3; E2 nesmie byť označená za zamietnutú. |
| `Kozmologická pipeline 09.txt` | Aktualizovať opis slučiek, (z_*) verzus (z_d), aproximácie a odstrániť konverzačný záver. |

