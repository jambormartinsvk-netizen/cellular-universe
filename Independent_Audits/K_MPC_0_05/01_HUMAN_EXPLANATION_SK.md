# Čo znamená problém `K_MPC=0.05` — ľudskou rečou

Predstav si vesmír ako oceán.

- **Background** je príliv: hovorí, ako sa rozpína celý oceán. Musí byť
  rovnaký, nech sa pozeráme na malú vlnu alebo na veľkú vlnu.
- **Fourierov mód `k`** je štítok na konkrétnej vlne. Veľké `k` znamená
  kratšiu vlnu; malé `k` dlhšiu. Pri `k=0.05 Mpc^-1` je typická vlnová dĺžka
  približne `2π/k ≈ 126 Mpc`.
- **Referenčný scale `k_*`** môže byť pevná vlastnosť teórie — podobne ako
  pravítko uložené v laboratóriu. Môže sa objaviť vo vzorci, ale nesmie sa
  meniť, keď zmeníme vlnu, ktorú práve meriame.

## Čo hovorí pôvodné odvodenie (nie neskoršia interpretácia)

Pôvodný skript K7 (`213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py`)
nemá samostatnú premennú pre aktuálne evolvovaný perturbatívny mód. Doslova
nastavuje jednu pevnú konštantu `K_MPC = 0.05` a používa ju v

```text
z = K_MPC · a / (H0 sqrt(Omega_r)).
```

Preto je presná odpoveď: **v implementovanom odvodení `k` nie je označené ani
odovzdané ako perturbatívny mód; vystupuje ako pevne zvolená škála.** Samotný
zdroj však nehovorí, či táto pevná škála mala znamenať konvenčný numerický
pivot, alebo fyzikálnu mierku siete. Jeho význam teda nie je odvodený a ostáva
otvoreným bodom K-N1/K-N2.

Ak by autor zamýšľal `0.05 Mpc^-1` ako **pivot**, je to iba referenčná voľba
výpočtu a nesmie určovať `H(a)`. Ak by ho zamýšľal ako **pevný scale siete
`k_*`**, stále nejde o aktuálny Fourierov mód poruchy, ale musí existovať
nezávislé odvodenie jeho hodnoty a jednotiek. Obe možnosti sú zatiaľ REVIEW;
interpretácia „je to aktuálny perturbatívny mód v backgrounde" je vylúčená
univerzálnosťou backgroundu.

V starom K7 výpočte sa `K_MPC=0.05` použil vo výraze

```text
z = K_MPC · a / (H0 sqrt(Omega_r)).
```

To samo osebe nemusí byť chyba. Problém vzniká, ak `K_MPC` znamená práve
Fourierov mód konkrétnej poruchy a ten istý symbol zároveň určuje hustotu
paliva v globálnom backgrounde. Potom by sa príliv oceánu menil podľa toho,
ktorú vlnu sme si vybrali na meranie.

Audit ukázal, že hmotné časti sa zvoleného `K` zbavia, ale palivový člen
zostane úmerný `K^3.93109`. Preto dnes nevieme, či `0.05` je:

1. len technický pivot zvolený pri výpočte — potom nesmie určovať background;
2. fyzikálny, pevný scale siete `k_*` — potom musíme odvodiť, prečo má práve
   túto hodnotu a prečo nie je ďalším fit parametrom;
3. chýbajúca normalizácia, ktorá mala premeniť `z^p` na čistú funkciu `a`.

Nejde o slovíčkarenie. Rozhoduje to, či teória vôbec predpovedá **jeden
vesmír**, alebo inú expanziu pre každú vlnovú dĺžku. CLASS potrebuje prvú
možnosť.
