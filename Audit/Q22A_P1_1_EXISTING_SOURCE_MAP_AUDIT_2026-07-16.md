# Q22a/Q18 P1.1 — mapa existujúcich zdrojov, stavov a rezervoárov

**Otázka P1.1:** obsahujú dnešné postuláty už objekt, ktorý môže bez novej
mikrofyziky vytvoriť lokálny skorý zdroj pary `S_s^mu`?  
**Rozsah:** iba existujúce Q4, Q8, Q18/Q23 a A2.0; žiadny nový parameter,
funkcia, skript ani fit.  
**Verdikt:** `P1.1 COMPLETE; P1 STOP PRE FUNDAMENTÁLNU A4 FUNKCIU V SÚČASNEJ v3.18.`

Tento STOP nehovorí, že skorá para je fyzikálne nemožná. Hovorí presne, že
existujúca dokumentácia zatiaľ neobsahuje kompletný lokálny vstup potrebný na
jej odvodenie.

## Povinné polia P1

Kandidát môže postúpiť do P2 iba ak už má všetkých päť položiek:

1. lokálny skalárny stav/clock `chi`; 2. energeticky identifikovaný rezervoár;
3. evolučnú rovnicu alebo lokálny generátor; 4. párový štvorvektorový ledger
pre paru; 5. mechanizmus skorého vypnutia, ktorý nie je voľným kozmickým časom.

## Inventár

| Kandidát | Lokálny stav | Energia/rezervoár | Evolúcia | Ledger do pary | Skoré vypnutie | P1 verdict |
|---|---|---|---|---|---|---|
| `rho_f`, konštantné `Gamma` | **ÁNO:** `rho_f=T_f^(mu nu)u_{f,mu}u_{f,nu}` | **ÁNO:** palivo | **ÁNO:** A1/A2 continuity | **NIE:** existujúci `Q^mu=Gamma rho_f u_c^mu` je iba `F->C`; A2 pre paru vedie `Q_s=0` po vzniku | **NIE:** konštantné `Gamma` samo nedá skorý ukončený impulz | `PARTIAL; NIE P2-READY` |
| `n_I,xi` jazvy | iba navrhnuté argumenty hazardu | **NIE:** energia jednej jazvy nie je definovaná | **NIE:** Q4 nemá rovnice `n_I,xi` | **NIE** | **NIE** | `NIE P2-READY` |
| Doména I | slovne absorpčný stav/pamäť | **NIE:** chýba hustota, tlak, štvorrýchlosť, `T_I^(mu nu)` | **NIE:** chýba lokálny generátor/Lindbladián alebo unitárne rozšírenie | **NIE:** chýba `Q_I^mu` aj `S_s^mu` | **NIE** | `NIE P2-READY; zakázaný skrytý rezervoár` |
| exit/reheating Q18/Q23 | **NIE:** otázka určuje potrebný jav, nie stav | **NIE** | **NIE** | **NIE** | **NIE** | `NIE P2-READY` |
| samotná už zadaná para | relativistická zložka je v A2 evidovaná | po svojom vzniku sa zachováva | `rho_s∝a^-4` po vzniku | **NIE:** nemá rodičovský zdroj | nie je mechanizmus vzniku | `NIE JE REZERVOÁR` |

## Dôkazy

1. `Audit/A2_00_kovariantny_ledger_zloziek_a_interakcii.md`, riadky 42–44,
48–68, 130–139: A2 uvádza paru až po zadanom vzniku a explicitne neobsahuje
kanál do pary; jediný lokálne uzavretý bunkový transfer je `F->C` s
konštantným `Gamma`.
2. Ten istý dokument, riadky 38–40: Doména I bez `T_I^(mu nu)` a `Q_I^mu`
nesmie fungovať ako skrytý rezervoár.
3. `Questions/Q4_problem_epsilon_jazvy_kolaje_K1-K4.md`, riadky 11–20 a
103–120: `xi`, energia jazvy a dynamika `n_I` nie sú definované; hazard je
iba modelová trieda bez rovníc.
4. `Questions/Q8_problem_domena_I_kolaje_K1-K4.md`, riadky 15–27 a 101–113:
energetická bilancia a lokálny generátor Domény I sú povinné, ale chýbajú.
5. `theory/SK/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_SK.md`,
Q18/Q23: source history, exit, reheating, entropia a BBN počiatočné podmienky
sú explicitne kriticky otvorené.

## Rozsudok a hranica

- **Žiadny kandidát nemá všetkých päť P1 polí.** Preto sa neotvára P2 s
  novou rovnicou `S_s^mu`; tá by bola nová hypotéza, nie odvodenie.
- `rho_f` je dôležitý čiastočný kandidát, ale nesmie sa potichu premenovať na
  skorú paru: zmenilo by to existujúci A1 transfer a bez derived switchu by
  obnovilo problém M-015.
- Efektívna FLRW rodina skorých ukončených zdrojov naďalej prežíva ako
  matematická a bilančne možná trieda. Nie je však predikciou siete.

## Následný postup

P1 sa uzatvára `STOP` pre **súčasnú fundamentálnu A4 vetvu**. Nie je poctivé
otvárať P2, P3, numerický sken ani pozorovací fit. Nasledujúce možnosti sú
iba dve a obe vyžadujú nový, explicitne označený fyzikálny vstup:

1. Q4/Q8 doplní lokálny stav jazvy, jeho energiu, dynamiku a `T_I^(mu nu)`;
2. Q23 doplní skutočný exit/reheating rezervoár s lokálnym transferom.

Po jeho dodaní sa znovu vykoná P1 od začiatku; tento audit zostáva historickou
stopou, že v3.18 taký vstup ešte neexistoval.

