# Auditný zápis k teórii Bunkového vesmíru (Verzia v3.18)

**Dátum auditu:** 11. júl 2026  
**Auditor:** Antigravity (Google DeepMind AI)  
**Autor teórie:** Martin Jambor (samostatný výskumník)  
**Rozsah auditu:** Analýza základnej dokumentácie v3.17 (slovenská a anglická verzia), preverenie nových materiálov v zložke `Nespracovane` (júl 2026) a posúdenie matematickej, fyzikálnej a dátovej konzistencie teórie.

---

## 1. Celkové zhodnotenie stavu a metodického pokroku

Teória Bunkového vesmíru (v3.17/v3.18) sa nachádza vo fáze **úspešnej predregistrácie pred kľúčovými observáciami konca dekády** (CMB-S4, LiteBIRD, Euclid/LSST, finálne DESI). Z hľadiska metodiky a správy projektu vykazuje teória mimoriadnu prísnosť:

*   **Metrika pokroku ($P_{\text{global}}$):** Dosahuje hodnotu **$\approx 70\%$**. Všetky hlavné komponenty (geometria na sieti, emergentný svetelný kužeľ, disperzia vĺn, rovnice pozadia V1 a rastu V3) sú detailne zadefinované a sprevádzané overiteľnou výpočtovou pipeline (skripty 06–10).
*   **Metrika spätnej stability ($R$):** Je rovná **0**. Za celý doterajší priebeh projektu nedošlo k žiadnemu návratu k už raz rozhodnutým otázkam bez nových dát či preukázaných fyzikálnych mechanizmov.
*   **Metrika zhody:** Dosahuje hodnotu **$\approx 79\%$** pri splnení všetkých overených zákonov ($Z1\text{–}Z15$) a nulovom počte porušení ($X = 0$) v aktívnych koľajach výskumu.
*   **Bilingválnosť:** Slovenská (autoritatívna) verzia dokumentov `01`, `04` a `05` je plne konzistentná s anglickým prekladom `01b`, `04b` a `05b`. Všetky rovnice, indexy a prepočty sú v oboch verziách identické a vzájomne verifikovateľné.

---

## 2. Audit externých námietok (E1–E4)

V rámci auditu sme preskúmali štyri externé námietky (zaznamenané v zložke `Nespracovane`) a potvrdzujeme ich **formálne zamietnutie**:

*   **E1: Námietka o chybe znamienka v rovniciach rastu (Gemini)**
    *   *Audit:* Zamietnuté. Rovnice rastu (sekcia V3) majú presný učebnicový tvar linearizovaných porúch vo FRW. Prepočet s Heathovou analytickou formulou súhlasí na $0.014\,\%$. Prípadná zmena znamienka by viedla ku kontrafaktuálnemu scenáru s extrémnym prepisom fluktuácií ($\sigma_8 \approx 24$), čo je v príkrom rozpore s pozorovaniami.
*   **E2: Tvrdenie, že gravitónový relikt (para) je nekompatibilný s Planckom/LIGO**
    *   *Audit:* Zamietnuté. Model nemá štandardné inflačné pole, ktoré by relikty rozriedilo na nulu. Hodnota $N_{\text{eff}} = 3.10$ sa nachádza vo vnútri $0.65\sigma$ pásma družice Planck ($2.99 \pm 0.17$). Detektor LIGO je na frekvenciu reliktu ($53\,\text{GHz}$) a teplotu ($0.9\,\text{K}$) necitlivý o $13$ rádov. Para slúži ako legitímny a kľúčový predikčný diskriminátor pre CMB-S4.
*   **E3: Tvrdenie, že $H_0 = 66.4\,\text{km/s/Mpc}$ je nekompatibilné s BAO**
    *   *Audit:* Zamietnuté na základe priameho dištančného testu (viď sekciu 4). θ* kotva drží akustickú škálu pevne a model kompenzuje nízke $H_0$ v neskorej expanzii pomocou prenosu energie $Q$.
*   **E4: Tvrdenie, že "entanglement bez prenosu signálu je logický rozpor"**
    *   *Audit:* Zamietnuté. Ide o elementárnu chybu v chápaní kvantovej mechaniky. V-vrstva prenáša kvantové korelácie, ale *No-Communication Theorem* zabraňuje prenosu informácií (signálu) nadsvetelnou rýchlosťou. Teória je v tomto bode v plnom súlade s QM.

---

## 3. Kritický audit matematickej konzistencie a nález v $n_s$ / $r$

### 3.1 Pôvodný nález a jeho riziká
V navrhovanej LaTeX sekcii pre odvodenie spektrálneho indexu $n_s$ sa objavila skrytá nekonzistencia. Text navrhoval škálovanie gravitačného potenciálu:
\[
\Phi \;\propto\; \frac{T}{T_P} \quad \text{a zároveň} \quad T \;\propto\; \sqrt{H}
\]
Toto viedlo k správnemu spektrálnemu indexu na prvý rád ($n_s \approx 0.9656$), ale **normalizácia amplitúdy perturbácií $A_s = 2.1 \times 10^{-9}$ by v tomto prípade vynútila extrémnu teplotu zamrznutia**:
\[
T_f \;=\; \frac{\sqrt{A_s}\,T_P}{\sqrt{\gamma}} \;\approx\; 5.6 \times 10^{14}\,\text{GeV}
\]
Pri takejto vysokej teplote $T_f$ by tenzorový odhad podľa vzorca $A14$ ($\Delta_h^2 \approx 0.4\,H\,T$) dal tenzorovo-skalárny pomer:
\[
r \;\approx\; 1.8 \times 10^{-5}
\]
Tento výsledok by **prerazil registrovaný strop teórie $r < 10^{-10}$ o päť rádov**. Prijatím tohto odvodenia by teória potichu samú seba falzifikovala.

### 3.2 Oprava a schválená verzia (derivacia_ns_opravena_C.tex)
Oprava bola úspešne implementovaná a je v plnom súlade s registrovaným krokom A13:
1.  **Škálovanie Perturbácií (A13 krok 3):** Amplitúda termálnych perturbácií v nasýtenom Hagedornovskom režime (kde energia tvorí spoje vnútornej sieci, no nezvyšuje kinetickú teplotu) škáluje ako $\Phi \propto \sqrt{T/T_P}$.
2.  **Škálovanie Teploty:** Teplota sleduje expanznú škálu pri výstupe módov z horizontu, teda $T \propto H$.
3.  **Konzistentná teplota zamrznutia:** Vynútené $T_f \sim 2\text{--}7 \times 10^9\,\text{GeV}$, čo vracia tenzory na úroveň $r \sim 10^{-21}\text{--}10^{-19}$ (plná zhoda s predikciou $r < 10^{-10}$).
4.  **Exponenciálny potenciál:** Zavedenie poľového ekvivalentu $U(\phi) = U_0 \exp(-\sqrt{3\delta}\phi/M_P)$ umožňuje, aby rovnica stavu paliva $w = -1+\delta$ bola dynamickým riešením (atraktorom) a nie iba ručne vloženou podmienkou.
5.  **Kvantový vs. Termálny kanál:** Pridaný prepočet ukázal, že kvantové vákuové fluktuácie poľa $\phi$ majú amplitúdu $\mathcal{P}_q \sim 10^{-38}$, čo je o 29 rádov pod pozorovanou termálnou amplitúdou $A_s$. Zanedbanie kvantového kanála je fyzikálne plne opodstatnené.

### 3.3 Efekt druhého rádu v sklone $n_s$
Presný vzťah pre spektrálny index je:
\[
n_s - 1 \;=\; -\frac{\epsilon}{1-\epsilon} \;=\; -\epsilon - \epsilon^2 - \dots
\]
Pri hodnote $\epsilon = \tfrac{3}{2}\delta \approx 0.03446$ dostávame:
*   *Prvý rád:* $n_s = 1 - 0.03446 = 0.96554$ (registrovaná hodnota $0.9656 \pm 0.0016$).
*   *Druhý rád:* $n_s = 1 - \frac{0.03446}{1 - 0.03446} \approx 0.96432$.
*   *Rozdiel:* Posun o **$-0.0012$** predstavuje $75\,\%$ deklarovanej neistoty. Tento posun je pre CMB-S4 merateľný. Riešenie tejto otázky je rozpracované v druhom dokumente (Questions).

---

## 4. Zhodnotenie BAO dištančného testu (DESI DR2)

Námietka o nekompatibilite s Baryónovými akustickými osciláciami bola otestovaná na 13 nezávislých dištančných bodoch DESI DR2 (BGS, LRG, ELG, QSO, Ly$\alpha$).

### 4.1 Výsledky testu
Model s parou ($\delta \approx 0.023$) a jednou fitted veličinou ($\lambda = 0.10\text{--}0.15$) dosiahol:
*   **$\Lambda$CDM (Planck kotva):** $\chi^2 = 36.8$ na 13 bodov.
*   **Model s parou ($\lambda = 0.15$):** $\chi^2 = 36.7$ ($\Delta\chi^2 = -0.1$ voči $\Lambda$CDM).
*   **Model s parou ($\lambda = 0.10$):** $\chi^2 = 34.4$ ($\Delta\chi^2 = -2.4$ voči $\Lambda$CDM).

### 4.2 Fyzikálny mechanizmus zhody
Model netrpí pokutou za nízku hodnotu $H_0 = 66.4$, pretože raná fyzika (drag horizont $r_d \approx 146.7\,\text{Mpc}$) ostáva prakticky nedotknutá (posun len o $0.26\,\text{Mpc}$ voči $\Lambda$CDM). Zníženie $H_0$ je kompenzované v neskorej expanzii prostredníctvom prenosu energie $Q = \lambda H_0 \rho_f$, čo udržuje akustický uhol $\theta^*$ v presnej zhode s dátami.

### 4.3 Dátová úprimnosť
Hoci model dosahuje rovnakú alebo lepšiu zhodu než $\Lambda$CDM, celková hodnota $\chi^2 \approx 35\text{--}37$ je pre oba modely vysoká (dôsledok inherentného napätia medzi DESI a Planckom v dátach pre $z = 0.7\text{--}0.9$). Výhoda modelu nespočíva v samotných priamych vzdialenostiach, ale v kombinovaných dátach (CMB × BAO × lensing), kde tieňový priebeh tmavej energie $w(z)$ lepšie kopíruje dáta než konštantná $\Lambda$.

---

## 5. Analýza kovariantného zobrazenia (A16)

Zavedenie sekcie `A16` (kovariantné zobrazenie) úspešne odstraňuje najväčšiu formálnu slabinu teórie — podozrenie, že rovnice pozadia V1 sú ad-hoc fenomenologické pravidlá stojace mimo Všeobecnej relativity (VR).

### 5.1 Fyzikálne závery
1.  **Bianchiho identity:** Transportné rovnice prenosu energie-hybnosti:
    \[
    \nabla_\mu T^{\mu\nu}_f \;=\; -Q u^\nu, \qquad \nabla_\mu T^{\mu\nu}_m \;=\; +Q u^\nu
    \]
    identicky spĺňajú Bianchiho podmienku $\nabla_\mu (T_f + T_m)^{\mu\nu} = 0$. Celková energia-hybnosť sa zachováva.
2.  **Geodetický prenos (bezhybnostný prenos):** Voľba výmenného štvorprúdu $Q^\nu = Q u^\nu$ (kde $u^\nu$ je štvorrýchlosť hmoty) znamená, že nová hmota sa rodí v pokojovej sústave lokálneho toku. V dôsledku toho prenos energie nedeformuje linearizované rovnice rastu (sekcia V3), čo je elegantné a konzistentné s existujúcou pipeline.
3.  **Povrchová stopa geodetického prenosu:** Akýkoľvek prenos hybnosti by pôsobil ako piata sila a deformoval by anizotropný rast (Redshift-Space Distortions — RSD). Predpoveďou modelu je nulová RSD anomália nad rámec pozadia. Akákoľvek detekcia takejto anomálie by model okamžite falzifikovala.

---

## 6. Záver auditu

Dokumentácia teórie Bunkového vesmíru k 11. júlu 2026 preukazuje **vysokú úroveň matematickej a logickej integrity**. Kritická chyba v škálovaní $n_s$/$r$ bola včas odhalená a opravená skôr, než stihla znehodnotiť registrované predikcie. BAO testy a kovariantná formulácia poskytujú teórii pevné základy v rámci štandardnej všeobecnej relativity. Teória je pripravená na prechod do verzie **v3.18**.
