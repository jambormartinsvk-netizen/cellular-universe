# A2-K7 — stav a akčný plán po bráne K7.0

**Dátum:** 2026-07-13  
**Aktuálny stav:** `PREŽÍVA 30/100`  
**Aktívny nasledujúci krok:** K7.1

## Čo je už uzavreté

- mediátor je skutočný tretí komponent, nie algebraický priemer K4;
- pozitívna `rho_M` je zahrnutá do registrovanej `rho_F`, nie pridaná nad
  A1 background;
- pre prachový mediátor platí presný rozsah `0<epsilon<delta=0.02297`;
- existujú kladné `Q1,Q2`, ktoré presne reprodukujú A1 ledger;
- donorovo orientovaná collision matica má eigenhodnoty `-R1,-R2<0`;
- K7.0 tým prešla, ale úplná stabilita a rast zostávajú otvorené.

## Čo sa nesmie tvrdiť

- `PREŽÍVA 30/100` nie je dôkaz správneho `S8`;
- záporné collision eigenhodnoty nie sú dôkaz superhorizontovej stability;
- rekonštruované `Q1` nie je odvodené z lokálnej akcie;
- `epsilon->0` nie je zdravý nulový limit, pretože `R1` diverguje;
- 9 % collision tlmenie relatívnej rýchlosti popola sa nesmie zameniť za
  9 % pokles `S8`.

## K7.1 — mikrofyzická a úplná perturbačná brána

### K7.1a — effective-action pôvod sadzieb

1. pre lokálnu akciu `phi,chi,psi_c` odvodiť kinematické podmienky
   `phi -> chi` a `chi -> psi_c bar(psi_c)`;
2. zapísať CTP/2PI alebo Boltzmannovu aproximáciu, z ktorej vzniknú
   `Q1,Q2`, ich pamäťové jadrá a šum;
3. určiť podmienky Markovovského limitu voči `H`, `m_chi` a šírke
   `Gamma_chi`;
4. porovnať odvodené sadzby s presne potrebným
   `Q1=(1-epsilon)Gamma rho_F+3H epsilon(1-delta)rho_F`;
5. ak sa tvar nedá získať bez časovo doladeného coupling parametra, K7
   zomrie ako M-014.

### K7.1b — gauge-invariantný systém

1. odvodiť kontinuity `phi,M,c` vrátane `delta Q1`, `delta Q2`;
2. odvodiť Eulerove rovnice z priestorových projekcií presných `Q_A^mu`;
3. pridať Einsteinove Hamiltonove a momentové constrainty;
4. vytvoriť gauge-invariantné relatívne rýchlosti a entropie
   `S_phiM,S_Mc`;
5. overiť všeobecný adiabatic mode a oba fyzikálne relatívne módy pre
   `k/(aH)->0`;
6. overiť kinetickú a gradientovú maticu pre `k/(aH)->infinity`.

### K7.1c — predregistrované testy

- zachovať grid `epsilon/delta={0.01,0.05,0.10,0.25,0.50,0.90}`;
- nepridávať nový bod podľa výsledku `S8` bez označenia exploratory behu;
- kill pri duchovi, `c_s^2<0`, kladnom superhorizontovom exponente,
  zápornom `rho_M`, neodvodenom `delta Q`, alebo potrebe vyhodiť šum;
- pri prežití až potom spustiť K7.2 CMB-normalizovaný rast.

## Paralelná dokumentačná úloha

Pri každom K7 skripte zachovať vstupy, verziu rovníc, výstup v MD a SHA-256.
Starý stav `ČAKÁ` v katalógu sa nemaže; tento dokument ho obmedzuje novším
stavom `PREŽÍVA K7.0 — 30/100`.

