# Q22a/Q18 M0 — audit proveniencie lokálnej hodiny a rezervoára

**Otázka:** má súčasná teória už definovaný lokálny skalárny stav `chi` a
energetický rezervoár `e`, z ktorých môže bez voľného kozmického času plynúť
skorý zdroj pary `S_s^mu`?

**Verdikt:** `M0 NEUZAVRETÝ — EFEKTÍVNY FLRW ZDROJ JE PRÍPUSTNÝ, ALE NEMÁ EŠTE LOKÁLNU MIKROFYZICKÚ REALIZÁCIU.`

Toto nie je rozsudok smrti pre skorý relikt. Je to stop-brána proti tomu, aby
sa za odvodený zákon vydával ľubovoľný profil `S_s(ln a)`.

## Kritérium M0

Fundamentálny kandidát musí vedieť zapísať

```text
nabla_mu T_s^(mu nu) = +S_s^nu,
nabla_mu T_e^(mu nu) = -S_s^nu,
S_s^nu = C_s(chi, I_1, ...) u^nu,
```

kde:

1. `chi` je definovaný lokálny skalár alebo dynamický stav s evolučnou rovnicou;
2. `e` má definované `T_e^(mu nu)` (alebo je jednoznačne jednou zo súčasných
   zložiek s odpočítaným zdrojom);
3. `C_s` nemá voľný argument `x=ln a`, globálne `H0` ani realizovaný Fourierov
   mód `k`;
4. v homogénnom limite z rovnakého zápisu vznikne skorá, skončená injekcia.

## Zistenia z existujúcej dokumentácie

| Kandidát | Čo dokumentácia naozaj dáva | Prečo M0 neuzatvára |
|---|---|---|
| A1/A2 palivo `rho_f` | `rho_f=T_f^(mu nu)u_{f,mu}u_{f,nu}` je lokálny skalár a efektívny prenos `Q^mu=Gamma rho_f u_c^mu` je bilančne kovariantný. | Tento prenos ide výlučne `F -> C`; pre paru je v A2 výslovne `Q_s=0` po jej vzniku. Konštantné `Gamma` nevytvorí samo skorý vypínajúci impulz bez ďalšieho stavu. |
| Doména I / jazvy | Q4 pripúšťa možný lokálny hazard `Gamma_F(x,t)=Gamma_0 f[n_I(x,t),xi(x,t)]`; Q8 pripúšťa absorpčný stav siete. | `n_I`, `xi`, ich rozsah, dynamika a energia nie sú definované. Q8 nemá generátor ani operátor. Nie je možné z nich počítať `C_s`. |
| Doména I ako rezervoár | Slovne by mohla niesť energiu spojenú s delením/jazvou. | A2.0 explicitne uvádza, že Doména I nemá lokálnu hustotu, tlak, štvorrýchlosť, `T_I^(mu nu)` ani `Q_I^mu`; použiť ju teraz by bol skrytý rezervoár. |
| Q18/Q23 exit/reheating | Uznávajú nutnosť odvodiť zdrojovú históriu pary. | Nedefinujú zatiaľ zdroj, clock, šírku ani normalizáciu; sú presne otvorenou časťou úlohy. |

## Dôkazové odkazy

- `Audit/A2_00_kovariantny_ledger_zloziek_a_interakcii.md`, riadky 38–44:
  Doména I nemá `T_I`/`Q_I`; para je v A2 vedená až **po zadanom**
  vzniku/decouplingu a jej zdrojovú históriu majú odvodiť Q18/Q23.
- Ten istý audit, riadky 48–68: `rho_f` a konštantné `Gamma` dávajú iba
  efektívny lokálny kanál `F -> C`; zápis `lambda=Gamma/H0` nesmie byť
  nesprávne chápaný ako nelokálny mikrofyzický clock.
- `Questions/Q4_problem_epsilon_jazvy_kolaje_K1-K4.md`, riadky 103–120:
  hazard s `n_I,xi` je iba modelová trieda bez rovníc.
- `Questions/Q8_problem_domena_I_kolaje_K1-K4.md`, riadky 101–113:
  absorpčný prechod prežíva ako hypotéza, ale nemá lokálny generátor ani
  dynamický operátor.

## Čo už možno tvrdiť a čo nie

| Tvrdenie | Stav |
|---|---|
| Hladká skorá efektívna FLRW história s párovým ledgerom nie je v rozpore so zachovaním energie. | PASS v deklarovanom efektívnom rozsahu |
| Teória už odvodila jej lokálnu kovariantnú funkciu `C_s(chi,I_i)`. | NIE; M0 REVIEW/STOP |
| Doména I môže byť bez ďalších rovníc použitá ako zdroj energie. | NIE; zakázané ako skrytý rezervoár |
| Súčasný neskorý kanál `F -> C` dokazuje skorú paru. | NIE; je to iný kanál |

## Najmenší korektný ďalší krok

Nie je vhodné skúšať tvary bumpov ani fitovať časy. Treba najprv vytvoriť
jednu z dvoch auditovateľných vstupných koľají:

1. **Jazvová koľaj:** presne definovať lokálny stav `chi=(n_I,xi,...)`, jeho
   jednotky, rovnicu vývoja a jeho príspevok `T_I^(mu nu)`; potom odvodiť
   `C_s` z lokálneho delenia.
2. **Exit/reheating koľaj:** určiť existujúcu fyzikálnu zložku `e`, jej
   `T_e^(mu nu)` a lokálny decay/transfer zákon, bez nazvania voľného času
   novou fyzikou.

Obe koľaje sa najprv hodnotia iba cez M0–M2 a nulové limity. Až ich prechod
oprávňuje použiť BBN/CMB na zúženie tvaru; dáta nesmú nahradiť chýbajúci
operátor.

