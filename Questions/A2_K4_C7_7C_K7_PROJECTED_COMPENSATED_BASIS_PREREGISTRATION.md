# A2-K4 / C7.7c-K7 — predregistrácia projektovanej kompenzovanej bázy

**Dátum:** 2026-07-14  
**Stav:** A2-K4 živá `66.5/100`; C7.7c-K1 až K6 neuzavreli aktivitu.  
**Motivácia:** NID celková hustota a `h_x` sú na oboch počiatočných povrchoch pod double-precision roundoff hranicou.

## 1. Odlišnosť od starších podkoľají

- K1: fyzikálny stav + jedno uniformné `atol`;
- K2/K4: diagonálne normalizovaný stav;
- K3: implicitný solver na zle škálovanom stave;
- K5: maticovo vyvážený stav so zmeneným error metrikom;
- K6: fyzikálny stav + extrémny vektor `atol_i`;
- **K7:** zavádza prirodzené kompenzované gravitačné zdroje ako odvodené premenné, aby sa NID zdroj nevytváral odčítaním veľkých species hodnôt.

K7 nesmie iba premenovať ten istý double súčet ani uvoľniť toleranciu.

## 2. K7a — analytické odvodenie bez evolúcie

Odvodiť samostatné rovnice pre:

`D = sum_A Omega_A delta_A`,

`M = 2 Omega_gamma U_gamma + 2 Omega_fs U_fs + 1.5 Omega_b U_gamma + 1.5 delta Omega_f U_f`.

Povinné podmienky:

1. `D'` a `M'` sa odvodia z registrovaných species rovníc a derivácií `Omega_A`; nesmú sa fitovať.
2. NID počiatočné hodnoty `D` a `M` sa získajú priamo z Puiseuxových koeficientov vo vyššej presnosti alebo z algebraickej kompenzačnej podmienky, nie odčítaním zaokrúhlených double species.
3. Nulový limit a všetky znamienka sa overia samostatne.
4. Pri NIV, kde je priamy súčet rozlíšiteľný, musí projektovaný a priamy zdroj súhlasiť s relatívnou odchýlkou `<10^-10` na deep aj shallow povrchu.
5. K7a nepridáva body.

## 3. K7b — koeficientový a constraintový audit

Pred evolúciou musí projektovaná dvojica `D,M` reprodukovať:

- vedúce NID/NIV Puiseuxove rády na oboch povrchoch;
- registrované `h_x=3D+2s^2 eta` a `eta_x=M`;
- Hamiltonov a momentum constraint v presnosti určenej AR34–AR36;
- rovnaké fyzikálne species koeficienty ako pôvodná 13-zložková sústava.

Ak niektorá podmienka zlyhá, K7 je mŕtva a evolúcia sa nespustí.

## 4. K7c — evolučná reprezentácia

Až po PASS K7a/K7b možno vytvoriť evolučný stav s projektovanými `D,M`. Musí byť explicitne uvedené, či:

- `D,M` nahradia dva numericky degenerované kombinované smery, alebo
- sa vedú ako auditné pomocné premenné s presným consistency ledgerom.

Nesmie vzniknúť dodatočný fyzikálny stupeň voľnosti. Počet nezávislých módov sa musí zachovať.

## 5. K7d — návrat k C7.7c

Úplný activity PASS vyžaduje:

- numerickú aktivitu rozlíšiteľných komponentov;
- vyššie-presný alebo projektovaný certifikát komponentov pod double condition hranicou;
- deep/shallow zhodu, konečnosť, safety cap a plný stavový ledger;
- nezmenené vopred stanovené prahy aktivity.

Skóre ostáva `66.5/100`; `+0.2` sa smie udeliť až po úplnom K7d PASS.

## 6. Stop pravidlo

Prvý ďalší krok je iba symbolické/koeficientové K7a. Žiadny ďalší ODE proces sa nesmie spustiť, kým nie je odvodenie zapísané a zauditované.

