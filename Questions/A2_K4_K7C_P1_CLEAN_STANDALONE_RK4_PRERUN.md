# A2-K4 / K7c P1 — predregistrácia čistého samostatného RK4

Dátum: 2026-07-15  
Typ: `REGRESSION`  
Skóre: `NONE`; A2-K4 ostáva `66.5/100`

## Povolený zásah

Skript 197 sa mechanicky odvodí zo zdroja 179, SHA-256 `8f45dc698817992e4fb2b859a7cafa49d225b4f7f5fd54b07f88ca99059bd441`:

- zachová celý prefix po definíciu `scaled_rhs`, RHS, background, seed, škálu, closure a parametre;
- opraví iba porovnanie seed názvov z poradia dict na množinu;
- odstráni import SciPy `solve_ivp` a celý adaptive legacy blok od `solution = solve_ivp(` po koniec `main`;
- vloží jedinú čistú fixed classical RK4 cestu pre kroky `0.0025`, `0.00125`, `0.000625`;
- zachová pôvodný exception/timeout obal;
- finálny zdroj nesmie obsahovať súvislý token `solve_ivp` ani nedosiahnuteľný solver;
- po každej mriežke uloží samostatný nemenný checkpoint s endpointom a hashom pred ďalšou mriežkou.

Žiadna rovnica, seed, škála, `L5=0` closure, krok ani fyzikálny parameter sa nesmie zmeniť.
## Čo sa počíta — ľudskou rečou

P1 vypočíta tú istú lineárnu evolúciu porúch troma čoraz jemnejšími pevnými RK4 mriežkami: 100, 200 a 400 krokov. Je to ako zmerať tú istú dráhu troma pravítkami s čoraz jemnejším delením. Cieľom ešte nie je potvrdiť novú fyziku, ale oddeliť skutočný výsledok RK4 rovníc od starého nedosiahnuteľného `solve_ivp` kódu a wrapperov v skriptoch 184/185.

Očakáva sa reprodukcia už pozorovanej nekonvergencie: rozdiel medzi 100 a 200 krokmi približne `1.44327e-6`, medzi 200 a 400 krokmi približne `3.93124e-6`, ich pomer `0.36–0.375` a dominantná odchýlka v móde `M`. Jemnejšia mriežka teda podľa historického výsledku nezmenšuje chybu klasickým RK4 spôsobom.

Ak výsledok zostane v nižšie zmrazených rozsahoch, audit reprodukcie dostane `PASS`, ale fyzikálny verdikt zostane `REVIEW` a skóre K4 sa nezmení. Nasledujúci krok P2 rozloží rovnicu `M'` na jednotlivé členy a bude hľadať zdroj nekonvergencie.

Ak výsledok rozsahy nesplní, tolerancie sa spätne neupravia. Zachovajú sa checkpointy a výsledok ostane `REVIEW`; pred ďalšou fyzikou sa porovná zdrojový hash, seed, stavové škály a každá z troch RK4 úrovní. Pád alebo timeout je technický výsledok, nie dôvod na smrť koľaje.

## Zmrazené numerické očakávania

- 100/200 max endpoint rozdiel: `1.4432726876921487e-6`, absolútna odchýlka najviac `1e-12`;
- historický 200/400 údaj bol zachovaný iba ako zaokrúhlené `3.93124e-6`; preto sa pred behom stanovuje kvantizačný interval `[3.931235e-6, 3.931245e-6]`, nie dodatočne ladená stredná hodnota;
- pomer `(100/200)/(200/400)` musí byť v `[0.36, 0.375]`;
- dominantná zložka 200/400 musí byť `M`;
- density residual rádovo `1e-22`, povinná brána `<5e-12`;
- momentum residual rádovo `1e-17`, povinná brána `<5e-12`;
- safety maximum približne 1, povinná brána `<1e8`;
- všetky tri checkpointy a RHS musia byť konečné;
- fyzikálne convergence checky `difference <1e-6` a klasický RK4 pomer `8–32` majú zostať false.

Auditná reprodukcia je PASS iba ak všetky regresné/formálne checky prejdú a fyzikálny stav ostane REVIEW. P1 nepridáva body.

## Limity

- skript 197: interný limit 20 s, seed source 12 s, seed child 6 s;
- externý limit 25 s, stavová kontrola po 10 s;
- checkpointy sa ukladajú pred ďalšou mriežkou a nesmú prepisovať existujúce súbory;
- timeout je REVIEW, nie smrť K4;
- checker 198 po pridaní 197/198 očakáva 202 ostatných `.py` súborov a 69 karanténnych položiek; 196 bude `SUPERSEDED`.

