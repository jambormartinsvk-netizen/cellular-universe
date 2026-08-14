# 00_AUDITOR_AUDIT — EA-20260717-001-KMPC-BACKGROUND-LINEAGE

**Auditor:** externý (Claude, nezávislý beh, bez prístupu k pracovnému stromu)  
**Dátum:** 2026-07-17  
**Rola:** odporúčajúca; projektový verdikt sa týmto dokumentom nemení  
**Vstup:** 17 súborov balíka; primárne skripty (`213`, `128`) a výstup `RUN-FULL-002` **neboli** súčasťou balíka — pozri obmedzenie E-1

---

## 0. Overenie integrity

Všetkých 15 evidence súborov aj oba package-control súbory boli prehashované
SHA-256 v izolovanom prostredí. **17/17 zhôd s manifestom, žiadny rozdiel.**
Balík je autentický voči zapečatenému stavu.

---

## 1. Odpoveď na presnú otázku balíka

### 1a. Bol perturbatívny mód `k` neprípustne prenesený do K4 backgroundu?

**Áno — pre historickú fixed-K implementáciu je prenos preukázaný výpočtom,
nie iba podozrením.** Reťaz dôkazov v balíku je uzavretá:

1. `z = k·a/(H0·√Ωr0)` bola zavedená v odvodení **porúch**, kde `k` je
   komový Fourierov mód práve evolvovanej poruchy (006 §2).
2. Runner 213 vložil `K_MPC=0.05` ako pevnú konštantu, `Φ=1` implicitne,
   `fuel_piece = z^p`, a tento výraz vstúpil do backgroundového
   `denominator` (006 §5, 007).
3. Hmotné členy sa `K` zbavia, palivový člen nie: výsledok RUN-FULL-002
   `D(a,k) = 1 + Ωm·a/Ωr + k^p·A(a)` s `p=3.93109` je priama numerická
   stopa úniku poruchovej súradnice do `H(a)`.

**Klasifikácia podľa 00_SCOPE: `COMPUTED_STOP_SCOPE`** pre historické
fixed-K backgroundové použitie. STOP je správne ohraničený: zabíja
implementáciu, nie mechanizmus ani exponent `p` (konzistentné v 006, 011,
013).

Dôležitá nuansa: **zámer** hodnoty `0.05` (pivot vs. sieťová škála `k_*`)
zostáva z primárneho zdroja neodvoditeľný — zdroj ju nijako neoznačuje
(005). Táto časť je korektne vedená ako otvorený review K-N1/K-N2 a nesmie
byť klasifikovaná ako COMPUTED.

### 1b. Je mapovanie `Φ(k) = A_f·[H0√Ωr0/k]^p` matematicky nutné a bez nového skrytého fitu?

**Áno, s jednou explicitnou premisou a jedným otvoreným provenance bodom.**

*Nutnosť.* Mapovanie je algebraicky vynútené **za predpokladu**, že fyzikálny
homogénny pomer má tvar `y_f(a) = A_f·a^p` s `A_f` nezávislým od módu. Tento
predpoklad je práve požiadavka univerzálnosti backgroundu — je legitímny,
ale je to premisa, nie veta. Pri jej prijatí je porovnanie
`Φ·z^p = A_f·a^p` jednoznačné a mapovanie nemá voľnosť.

*Nezávislá kontrola auditora — zrušenie `k^p` vo VŠETKÝCH deklarovaných
hustotných členoch* (požiadavka z 02_AUDITOR_INSTRUCTIONS):

| Člen | Skladba mocnín `k` | Výsledok |
|---|---|---|
| palivo `Φ·z^p` | `k^(−p) · k^p` | `A_f·a^p` — **k sa ruší presne** |
| korekcia `Φ·z^p·(−g2·z²/2)` | `k^(−p) · k^p · k^(−2)·k^2` | `−A_f·λ·a^(p+2)/(2√Ωr0)` — **ruší sa** |
| ash zdroj `Φ·g2·z^(p+2)/(p+1)` | `k^(−p) · k^(−2) · k^(p+2)` | `A_f·λ·a^(p+2)/[(p+1)√Ωr0]` — **ruší sa** |
| `g2·z²` samostatne | `k^(−2)·k^2` | `λ·a²/√Ωr0` — **ruší sa, ale len v radiačnom limite** |

Zrušenie je exaktné a párovanie fuel/ash koeficientov (`−g2/2` vs.
`g2/(p+1)`) zostáva po mapovaní zachované — nevzniká nový nezávislý
parameter v rade. Aritmetika `p = 4 − 3·0.02297 = 3.93109` sedí.

*Nový skrytý fit.* Na úrovni parameter bookkeepingu **nie**:
`A_f = 7809.270101963506` je podľa 013 odvodené z už zmrazeného A1-K1
closure bez vstupu `K_MPC` alebo `k` (P2a PASS). Otvorený zostáva P2b —
pôvod samotného closure. `A_f` teda nie je post-data parameter, ale jeho
proveniencia je podmienená; číslo sa musí niesť s provenance tagom, nie ako
konštanta prírody.

*Kritické ohraničenie.* Mapovanie **nerehabilituje** K7 background:
`g2·z² = λa²/√Ωr0` platí len v radiačnom limite (mimo neho `Γ/H = λ/E(a)`)
a skrátený K7 rad prechádza nulou pri `a ≈ 0.70896` (P3). Jediný prípustný
univerzálny background je `D_A1(a) = a^4·E²/Ωr0` (P4a). Balík toto uvádza
konzistentne; audit potvrdzuje, že „algebraický PASS mapovania" a
„platnosť K7 backgroundu" sú dve rôzne tvrdenia a nesmú sa zlievať.

---

## 2. Formula ledger (zdroj → zmena premennej → base/runner → background)

| Krok | Obsah | Nosič `k` | Dôkaz |
|---|---|---|---|
| Zdroj | A1 continuity: `y_f,x = [4−3δ−λH0/H]·y_f` ⇒ `p = 4−3δ` | žiadny — `p` pochádza z riedenia, nie z Fourierovej fyziky | 006 §1 |
| Zmena premennej | poruchové odvodenie zavádza `z = k·a/(H0√Ωr0)`, `s = k/Hconf` | `k` = mód aktuálnej poruchy | 006 §2 |
| Base | skript 128: normalizácia `(ρf/ρr)/(Φ·z^p)` + párovaný ash rad | `k` legálne, lebo jeden vybraný mód | 006 §3, proveniencia |
| Runner | skript 213: `K_MPC=0.05`, `Φ=1`, `fuel_piece=z^p`, `denominator=1+MU·z+z^p(1+TS·z²)` | `k` **fixovaný ako backgroundová konštanta** — nedokumentovaný prechod na `A_f·a^p` | 006 §5, 007 |
| Background (historický) | RUN-FULL-002: `D(a,k)=1+Ωm·a/Ωr+k^p·A(a)` | `k^p` únik — STOP | 006 §4–5 |
| Background (korektný) | `Φ(k)=A_f(H0√Ωr0/k)^p` ⇒ raný rad k-nezávislý; plný background výlučne `D_A1` | `k` iba v `s2 = k²/Hconf²` poruchového behu | 008, 013 |

---

## 3. Nezrovnalosti a chyby nájdené v balíku

| ID | Nález | Závažnosť | Detail |
|---|---|---|---|
| N-1 | Terminologický konflikt 005 vs. 013 | stredná | 005: „`k` nie je označené ani odovzdané ako perturbatívny mód; vystupuje ako pevne zvolená škála." 013 (záväzná formulácia): „Je to pevne vložená hodnota perturbatívneho `k`." Vecne zlučiteľné (implementačný label vs. odvodzovacia proveniencia), ale doslovné znenia si protirečia a otvárajú priestor na spätný interpretačný spor — presne ten, ktorý má záväzná formulácia zavrieť. |
| N-2 | Duplicitný blok v 005 | nízka | Rovnica `z = K_MPC·a/(H0√Ωr)` a sprievodný odsek sa v dokumente opakujú dvakrát s čiastočne odlišným rámovaním. Editorial, ale v „human explanation" dokumente to znižuje jednoznačnosť. |
| N-3 | Nedeklarovaná jednotková konvencia pre `z` | stredná | `z = k·a/(H0√Ωr0)` je bezrozmerné len pri `H0` vyjadrenom v Mpc⁻¹ (t. j. `H0/c`). Pri necelom `p` je bezrozmernosť `z` **nutná podmienka** zmysluplnosti `z^p`. Konvencia `c=1`/jednotky nie je v balíku nikde explicitná. Nejde o chybu matematiky, ale o medzeru presne v bode, ktorý 02_AUDITOR_INSTRUCTIONS káže kontrolovať. |
| N-4 | `A_f` bez provenance tagu a jednotkového výroku | stredná | Hodnota na 16 platných číslic bez odkazu na konkrétny run/hash a bez poznámky „podmienené P2b". `A_f` je bezrozmerné (pomer hustôt pri bezrozmernom `a`) — aj to treba raz napísať. |
| N-5 | Kolízia symbolu `z` | nízka | `z` = palivová premenná (006), `z` = projektovaný stavový vektor (010), `z=.01` v KMPC-035 (003) — pravdepodobne hodnota premennej, ale bez kontextu čitateľné aj ako redshift. Pri formula-lineage projekte je to zbytočné riziko. |
| N-6 | Znamienková konvencia `Q^mu` | nízka | 007/008 píšu `Q^mu=Γρf·u_d^mu` bez subscriptu; 009 rozpisuje `Q_f^mu=−Γρf·u_d^mu`, `Q_c^mu=+Γρf·u_d^mu`. Nie je to rozpor (generický zápis = tok do popola), ale konvencia by mala byť deklarovaná raz a záväzne. |
| E-1 | Chýbajúce primárne zdroje | stredná | Skripty `213`, `128` ani JSON RUN-FULL-002 nie sú v EVIDENCE; citované riadky 63–123 nemožno nezávisle overiť. Podľa AR66.2 preto tento audit smie byť maximálne `PASS_MAPY` úrovne dôkazu — mapa je vnútorne konzistentná naprieč 6 dokumentmi, ale nie je to primárna verifikácia kódu. |

Pozitívne kontroly, ktoré prešli: redukcia general-synchronous `U_f,x`
rovnice pri `U_c=U_d=0` presne reprodukuje K7 riadok `(q+2)U_f+δf/δ+2gU_f/δ`
(011 — dôkaz STOP je vnútorne konzistentný); `β_f = p−γ` a `β_c = 1+γXf/Xc`
plynú korektne z A1 continuity (008); radiačný limit `γ → g = G2z²` sedí.

---

## 4. Riziká

1. **R-1 (interpretačné):** kým N-1 nie je uzavreté erratou, existuje cesta
   spätne prehlásiť `0.05` za „vždy zamýšľaný pivot" alebo „vždy zamýšľanú
   škálu siete". Záväzná formulácia z 013 je správna obrana, ale musí byť
   jediná.
2. **R-2 (proveniencia `A_f`):** ak P2b zmení A1 closure, zmení sa `A_f` a
   s ním celá normalizácia raného radu. Downstream artefakty musia `A_f`
   referencovať cez hash zdrojového runu, nie hodnotou.
3. **R-3 (rehabilitačné pokušenie):** algebraický PASS mapovania sa dá
   omylom komunikovať ako záchrana K7. Nie je: P3 nulový prechod a nezávislý
   P4c STOP (chýbajúce `U_c`) držia K7 v `DO_NOT_USE_PHYSICS` z dvoch
   samostatných dôvodov. Oprava K_MPC neopravuje ani jeden z nich.
4. **R-4 (dôkazová úroveň):** bez primárnych skriptov je lineage overená
   len sekundárne (E-1). Pri budúcom spore o riadok 213 nebude tento balík
   stačiť.
5. **R-5 (rozmerová):** necelý exponent + nedeklarovaná `c` konvencia je
   presne typ chyby, ktorá prežije roky, lebo numericky „funguje" pri
   konzistentných jednotkách a exploduje pri prenose do CLASS/CAMB, kde sú
   konvencie iné.

---

## 5. Navrhované riešenia a odporúčaný postup

1. **Errata, nie prepis** (podľa AR66.2): do 005 pridať erratum zjednocujúce
   formuláciu s 013 — navrhované znenie: *„V odvodení je `k` perturbatívny
   mód; v implementácii 213 bol vložený ako neoznačená pevná konštanta.
   Zámer hodnoty nie je zo zdroja odvoditeľný."* Zachovať pôvodný hash,
   priložiť nový.
2. **Jednotkový dodatok:** jeden krátky dokument deklarujúci `c=1`,
   jednotky `k` [Mpc⁻¹], `H0` [Mpc⁻¹] a dôkaz bezrozmernosti `z`; odkázať
   naň z 006 a z budúceho P5 coefficient manifestu. Zaradiť ako povinný
   riadok do AR66.2 kontroly „Limity/rozmery".
3. **Provenance tag `A_f`:** `A_f = 7809.270101963506
   [zdroj: P2a run <hash>; podmienené: P2b OPEN; bezrozmerné]` všade, kde sa
   hodnota cituje.
4. **Doplniť EVIDENCE addendum** s frozen kópiami `213`, `128` a
   RUN-FULL-002 JSON (alebo aspoň ich hashmi + citovanými riadkami ako
   samostatný súbor), aby budúci audit mohol byť `FORMULA PASS`, nie len
   `PASS_MAPY`.
5. **Symbolová hygiena:** v nových P5 dokumentoch rezervovať `z` výlučne pre
   palivovú premennú, stavový vektor premenovať, redshift písať `z_red`.
6. **Pokračovať v P5 bez odbočky:** otázka „význam 0.05" je pre background
   uzavretá správnym smerom (K-N3/K-N4/K-N5 mŕtve, K-N1 review). Žiadna nová
   práca na nej nemá pre `H(a)` hodnotu; `k` patrí výlučne do `s2` vstupu
   poruchového behu podľa 008. Toto odporúčanie je v súlade s aktívnym
   krokom KMPC-036 → M1 precision/boundary closure.
7. Poznámka k plánu: podľa 002 platí tokenová pauza do 2026-07-24 — tento
   audit je povolená read-only práca a nemení žiadny PASS/REVIEW/STOP.

---

## 6. Záver a celkové hodnotenie

**Odpoveď na otázku balíka:** (1) Prenos perturbatívneho `k` do homogénneho
backgroundu v historickej K7 línii **nastal a je výpočtovo doložený** —
klasifikácia `COMPUTED_STOP_SCOPE`, správne ohraničená na implementáciu.
(2) Mapovanie `Φ(k)=A_f(H0√Ωr0/k)^p` **je matematicky nutné** za explicitne
menovanej premisy univerzálnosti a **nezavádza nový post-data fit** na
úrovni bookkeepingu (P2a); mikrofyzikálny pôvod `A_f` zostáva otvorený
(P2b). Zrušenie `k^p` bolo nezávisle overené vo všetkých troch deklarovaných
hustotných členoch vrátane párovaného ash radu.

**Kvalita balíka:** logická stavba STOP-ov je nadpriemerne disciplinovaná —
smrť implementácie sa nikde nezamieňa so smrťou mechanizmu, skóre sa
neprenášajú, immutable história sa nepatchuje. Nájdené nedostatky sú
dokumentačné a provenienčné (N-1 až N-6, E-1), nie matematické; žiaden
z nich nemení verdikt, ale N-1, N-3 a E-1 treba uzavrieť pred G8, lebo
každý z nich je potenciálny zdroj budúceho sporu presne v bode, kde projekt
dnes stojí na svojej najsilnejšej stránke — na auditovateľnosti.

**Dôkazová úroveň tohto auditu podľa AR66.2:** `PASS_MAPY` (konzistencia
mapy naprieč dokumentmi + nezávislé algebraické kontroly auditora);
`FORMULA PASS` je dosiahnuteľný po doplnení primárnych zdrojov podľa bodu
5.4.
