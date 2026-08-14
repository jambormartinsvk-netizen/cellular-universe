# Q22a-K2 — výsledok priameho limitu `F -> R`

**Verdikt:** `NOT_COMPATIBLE_WITH_FROZEN_A1_K1_BACKGROUND; SEPARATE_A1_BRANCH_REQUIRED`  
**Algebraický stav:** `PASS_BACKGROUND_FORK_REQUIRED`  
**Skóre:** `bez fyzikálneho skóre`  
**Skript a príloha:** `scripts/257_script_Q22A_K2_direct_steam_background_fork_audit.py`,
`scripts/results/q22a/RUN_Q22A_003_K2_DIRECT_STEAM_BACKGROUND_FORK_AUDIT.json`.

## Výsledok

Pri priamom vzniku pary sú zdroje

```text
Q_F=-Gamma rho_F,  Q_C=0,  Q_R=+Gamma rho_F.
```

Súčet je presne nulový a limit `Gamma=0` je zdravý. To teda **nie je**
porušenie zachovania energie.

Voči zmrazenému A1-K1 však platí

```text
(Q_F,Q_C,Q_R)_K2 - (Q_F,Q_C,Q_R)_K1
= (0,-Gamma rho_F,+Gamma rho_F).
```

Pri nenulovom prenose sa preto súčasne zmení hustota popola a radiácie. K2
nemôže použiť A1-K1 background, jeho doterajšiu CMB kotvu ani A2-K4 výpočty.

## Rozsudok a hranice

K2 nie je mŕtva. Je to **iná backgroundová vetva A1**, nie podkoľaj A1-K1.
Jej životaschopnosť je úplne otvorená a bude vyžadovať vlastný odvodený
kovariantný operátor, BBN/`N_eff`, CMB a perturbácie. Súčasný audit nepočítal
ani jednu z týchto brán a neprideľuje jej hĺbku ani pravdepodobnosť úspechu.

## Vzťah ku K3 a sekvenčným koľajam

K3 s `0<b<1` má rovnaký problém v menšej miere: odchýli sa od A1-K1 o
`(0,(b-1)Gamma rho_F,(1-b)Gamma rho_F)`. K4–K7 majú k tomu ešte sekundárny
konverzný/oneskorovací kernel. Preto sa žiadna z nich nesmie tváriť ako
neškodná zmena existujúcej A1-K1 vetvy.
