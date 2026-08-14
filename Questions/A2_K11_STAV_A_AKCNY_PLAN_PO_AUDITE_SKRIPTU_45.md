# A2-K11 — stav a akčný plán po audite skriptu 45

**Dátum:** 2026-07-13  
**Stav:** `PREŽÍVA IBA HYPOTÉZU — 10/100 = G1 (historický checkpoint 15)`  
**Skript 45:** `PASS ZAMIETNUTÝ — NEPLATNÝ DÔKAZ`  
**Aktívny krok:** K11.1 — lokálny operátor, regularita a úplné rovnice

## Čo je uzavreté

- čistý ortogonálny prenos hybnosti môže mať nulový backgroundový účinok;
- pri signatúre `(-,+,+,+)` musí mať sila na CDM pre tlmenie plusový
  projektor;
- oprava `1/(aE) -> 1/E` v skripte 45 bola správna, ale nedostatočná;
- predložená mínusová sila je pri deklarovanej interpretácii anti-drag;
- rovnice skriptu 45 nie sú úplnou kovariantnou perturbačnou sústavou;
- numerický `PASS` zlyhal na amplitúdovom škálovaní, krokovej konvergencii
  a relatívnom Einsteinovom constrainte;
- skript 45 nevypočítava `S8`.

Rozhodujúci audit:
`Audit/A2_K11_audit_opraveneho_scriptu_45_a_momentum_drag.md`.

## K11.1 — lokálny a pravidelný momentum-transfer

### K11.1a — definícia jedného operátora

1. fixovať
   `Q_c^mu=Gamma rho_f u_c^mu+F_c^mu`, `Q_f^mu=-Q_c^mu`;
2. odvodiť `F_c^mu` z lokálnej akcie, Boltzmannovho collision integrálu
   alebo otvoreného effective-action opisu;
3. nepredpisovať vopred konštantné `gamma=0.03`; najprv odvodiť hustotnú,
   teplotnú a časovú závislosť koeficientu;
4. požadovať, aby interakcia fyzikálne zanikla, ak zmizne jeden z
   interagujúcich sektorov, alebo presne vysvetliť iný lokálny limit;
5. ak vznikne disipácia po coarse-grainingu, zachovať šum/pamäť alebo
   odvodiť Markovovský limit.

### K11.1b — úplná kovariantná perturbácia

1. odvodiť `delta Q_A` a priestorové projekcie z tej istej definície;
2. zapísať úplné kontinuity a Eulerove rovnice pre fuel, CDM, baryóny a
   radiáciu v jednej konvencii;
3. odvodiť Hamiltonov a momentový Einsteinov constraint;
4. skontrolovať analyticky Bianchiho identitu a celkové
   `nabla_mu T_total^{mu nu}=0`;
5. vytvoriť gauge-invariantnú relatívnu rýchlosť a entropický mód;
6. preveriť limity `gamma->0`, `lambda->0`, `rho_f->0`, `delta->0`.

### K11.1c — predregistrované kill kritériá

K11 zomrie ako `M-015`, ak:

- tlmiaci operátor nemá lokálny pôvod alebo regularitu v hustotných
  limitoch;
- spätná reakcia znovu vytvorí neodstrániteľný pól/silnú väzbu;
- úplné rovnice nepropagujú Einsteinove constrainty;
- superhorizontová alebo high-k matica má fyzikálny rastúci mód;
- potrebný parameter existuje iba ako post-data fit k `S8`.

## K11.2 — až po prejdení K11.1

1. analytická superhorizontová eigenanalýza;
2. high-k kinetická a gradientová matica;
3. numerika so škálovaním amplitúdy, aspoň dvoma toleranciami a dvoma
   krokmi bez `or is_damped` bypassu;
4. relatívny constraint iba tam, kde je jeho menovateľ numericky aktívny;
5. samostatný nulový beh pre každú interakciu.

## K11.3 — observačná brána

Iba po K11.1–K11.2:

- implementovať presný systém v Boltzmannovom kóde;
- normalizovať na rovnaký CMB likelihood;
- vypočítať celé `P(k)`, `sigma_8`, `S8`, CMB lensing a ISW;
- preveriť nelineárny rast, pretože momentum exchange môže mať odlišné
  lineárne a nelineárne dôsledky;
- porovnať model s rovnakým počtom voľných parametrov, nie iba surové
  minimum `chi^2`.

## Poradie práce

1. **aktívne:** K11.1a — odvodenie regularizovaného lokálneho operátora;
2. potom K11.1b a K11.1c;
3. K7.1 zostáva zachovaná ako druhá živá koľaj a po rozhodnutí K11.1 sa na
   ňu vraciame bez prepisovania jej stavu;
4. K8–K10 zostávajú v poradovníku.

Všetky ďalšie skripty, aj keď koľaj zomrie, musia zostať v `scripts/` a
ich výstupy v MD spolu s dôvodom rozsudku.


