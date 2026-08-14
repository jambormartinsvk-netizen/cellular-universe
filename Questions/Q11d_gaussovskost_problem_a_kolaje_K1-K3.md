# Q11d — gaussovskosť primárnych fluktuácií: problém a koľaje

**Dátum založenia:** 2026-07-13  
**Stav:** OTVORENÁ A NEDEFINOVANÁ

## 1. Audit stavu

Q11d sa v registri objavuje iba v záverečnej bilancii ako „dorazenie gaussovskosti“. V dokumentoch neexistuje definícia náhodnej premennej, generátor mikrostavov, mapa na krivostnú perturbáciu `ζ`, bispektrum ani testovací prah.

Preto zatiaľ nebola auditovaná fyzikálna predikcia; auditovaný bol iba fakt, že predikcia chýba.

## 2. Minimálna špecifikácia

Treba definovať:

$$
\zeta(\mathbf{k})=\mathcal{M}[\text{stav siete}],
$$

a odvodiť aspoň `Pζ(k)`, trojbodovú funkciu a zodpovedajúce `fNL` v relevantných tvaroch. Samotný histogram lokálnej energie nestačí.

## 3. K1 — centrálna limitná veta z mnohých slabo korelovaných buniek

### Hypotéza

Pozorovateľný mód je normalizovaný súčet veľkého počtu príspevkov s konečnou varianciou a dostatočne rýchlo klesajúcimi koreláciami.

### Testy

- určiť počet efektívne nezávislých príspevkov na mód;
- zmerať korelačnú funkciu a mixing podmienku;
- zmerať šikmosť a exces ako funkciu N;
- overiť škálovanie kumulantov `κ_n ∝ N^{1-n/2}`;
- preniesť výsledok na `ζ`, nie iba na pomocnú sieťovú premennú.

### Stav

**NAJSĽUBNEJŠIA; NA STENE CHÝBAJÚCEHO GENERÁTORA A MAPY NA ζ.**

## 4. K2 — termálny takmer Gaussovský stav

### Hypotéza

Kvadratická časť efektívneho voľnoenergetického funkcionálu dominuje a vyššie interakcie sú malé, takže pole má približne Gaussovskú mieru.

### Testy

- odvodiť efektívny funkcionál zo siete;
- spočítať kubické a kvartické väzby;
- odvodiť bispektrum a trispektrum;
- preveriť, či Hagedornovský/critical režim vôbec dovoľuje malú negaussovskosť.

### Stav

**PREŽÍVA FORMÁLNE; BEZ EFEKTÍVNEJ AKCIE.**

## 5. K3 — kritická sieť s vlastnou negaussovskou predikciou

### Hypotéza

Primárne fluktuácie nie sú presne Gaussovské; sieť predikuje malý, špecifický tvar bispektra kompatibilný s dátami.

### Testy

- odvodiť tvar a amplitúdu bez fitu na aktuálne limity;
- preveriť lokálny, ekvilaterálny a ortogonálny limit;
- hľadať škálovú závislosť a sieťovú anizotropiu;
- porovnať spoločnou CMB likelihood.

### Stav

**PREŽÍVA AKO FALZIFIKOVATEĽNEJŠIA ALTERNATÍVA.**

## 6. Poradie

Začať K1. Ak korelácie neklesajú alebo kumulanty neškálujú podľa CLT, K1 zomrie a pokračuje K2/K3. Q11d možno uzavrieť až po teste na simulovaných mikrostavoch a po mape na `ζ`.

