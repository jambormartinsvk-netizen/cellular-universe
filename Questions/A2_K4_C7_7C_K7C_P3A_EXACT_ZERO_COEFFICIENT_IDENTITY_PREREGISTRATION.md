# K7c P3a — predregistrácia exaktných nulových koeficientov

Dátum: 2026-07-15  
Stabilné ID: `SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY`  
Typ: analytická a numerická kontrola bez ODE  
Score effect: `NONE`

## Hypotéza

Dva členy `M'`, ktoré P2 identifikovalo ako zdroj float64 artefaktu, majú na
registrovanom backgrounde identicky nulové koeficienty:

\[
c_U=\frac32\Omega_b-W_\gamma\frac{R}{1+R}=0,
\]

\[
c_\delta=\frac14W_\gamma\frac1{1+R}-\frac12\Omega_\gamma=0.
\]

Nejde o fit ani nový parameter. Je to algebraické zjednodušenie už
registrovaných definícií `Omega_b`, `Omega_gamma`, `R` a `W_gamma`.

## P3a-A — identity audit bez evolúcie

Nový číslovaný skript musí:

1. načítať P2 raw JSON s presným hashom;
2. znovu odvodiť `Omega_b/Omega_gamma=4R/3` z backgroundových definícií;
3. overiť obe symbolické identity bez dosadzovania výsledku P2;
4. vyhodnotiť pôvodné a algebraicky zjednodušené koeficienty vo float64 aj
   pri 80 dps na `x=-25,-24.875,-24.75` a na registrovaných deep/shallow
   počiatočných plochách;
5. potvrdiť, že HP koeficienty sú kompatibilné s presnou nulou a že float64
   rezíduum je iba cancellation artefakt;
6. uložiť všetky hodnoty, hashe a nulové limity do nového JSON.

PASS vyžaduje exaktnú symbolickú nulu oboch koeficientov, konečné backgroundy
a žiadny dodatočný člen. Numerická malá hodnota bez symbolickej identity
nepostačuje. FAIL identity zabíja algebraickú koľaj; timeout alebo formálna
chyba je REVIEW.

## P3a-B — povolený až po PASS P3a-A

Samostatný evolučný skript smie zmeniť oproti čistému skriptu 197 iba:

- tretí a štvrtý člen `M'` sa na tomto backgrounde vyhodnotia ako exaktná
  nula podľa auditovanej identity.

Zakázané sú zmeny seedu, backgroundu, ostatných siedmich členov, state basis,
škály, closure, krokov, normy alebo prahov. Zopakujú sa mriežky 100/200/400.

Predregistrované fyzikálne brány ostávajú:

- pomer `(100/200)/(200/400)` v `8–32`;
- rozdiel 200/400 `<1e-6`;
- tri checkpointy a RHS konečné;
- presná provenance a bitová zhoda všetkých nezmenených termov.

Ak obe konvergenčné brány prejdú, algebraická koľaj pokračuje do širšieho
G4/G6 auditu. Ak nie, koľaj zomrie s uloženými výpočtami a nasleduje oddelený
audit lokálnej tuhosti/eigenmódov. Vyššia pracovná presnosť je ďalšia
samostatná koľaj, nie súčasť P3a.

