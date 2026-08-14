# A2-K8.1 — G2 audit produkcie počtu konštantne hmotného popola

## Rozsudok

**Rodič A2-K8 zostáva otvorený na G1, 10,0/100. G2 neprešla, ale koľaj nie je mŕtva.**

Backgroundová energia sa dá reprodukovať presne. Samotný skalárny zdroj počtu `S_n` však neurčuje priestorový moment produkcie, teda úplný štvorvektor `Q_c^mu`. Chýba fyzikálny pôrodný frame alebo úplný kinetický collision kernel.

## Presná kovariantná bilancia

Pre

```text
N_c^mu=n_c u_c^mu,
nabla_mu N_c^mu=S_n,
rho_c=m_c n_c,
T_c^{mu nu}=rho_c u_c^mu u_c^nu,
m_c=constant
```

produktové pravidlo dáva

```text
nabla_mu T_c^{mu nu}=m_c S_n u_c^nu+rho_c a_c^nu,
a_c^nu=u_c^mu nabla_mu u_c^nu.
```

Projekcie pri signatúre `(-,+,+,+)` sú

```text
-u^c_nu Q_c^nu=m_c S_n,
h^alpha_nu Q_c^nu=rho_c a_c^alpha.
```

Záver: `S_n` určuje energetický moment v rámci popola, ale nie kolmú hybnosť ani akceleráciu. To zodpovedá všeobecnej kinetickej štruktúre, v ktorej prúd častíc a tenzor energie-hybnosti vznikajú ako odlišné momenty distribučnej funkcie; jeden moment preto nemožno zameniť za celý collision integral. Pozri [Sarbach a Zannias, Relativistic Kinetic Theory](https://arxiv.org/abs/1303.2899).

## Background A1-K1

Vo FLRW sa všetky izotropné rámce zhodujú. Voľba

```text
m_c S_n=q=Gamma rho_f
```

dáva

```text
dot rho_c+3H rho_c=+q,
dot rho_f+3H(1+w_f)rho_f=-q.
```

Súčet sa ruší presne. Skript 150 overil na 1000 deterministických vzorkách maximálne backgroundové rezíduum `7.105427357601002e-15`.

To je **backgroundový PASS vnútri G2**, nie úplný G2 PASS: homogénny background nedokáže určiť priestorový smer `Q_c^mu`.

## Frame mapa a živé/mŕtve možnosti

| Podkoľaj | Úplný prvý moment | Výsledok |
|---|---|---|
| K8.1-Fc | studený geodetický zrod, `Q_c^mu=q u_c^mu` | deterministický fluidný limit je A2-K1; dedí M-009, nie je nová živá koľaj |
| K8.1-Ff | zrod v rámci paliva, `Q_c^mu=q u_f^mu` | fluidný limit je A2-K3; dedí M-010 |
| K8.1-Fd | zrod v entalpickom energy-frame, `Q_c^mu=q u_d^mu` | fluidný limit sa zlieva s A2-K4; nejde o nezávislý počet živých koľají |
| K8.1-Fkin | explicitná distribúcia zrodu `C_c[f]` s nultým, prvým a tlakovým/šumovým momentom | **živá hypotéza**, ešte iba G1; musí uzavrieť G2–G3 |

Mapovanie na K1/K3 je deterministická inferencia z rovnakého `Q^mu` a rovnakého studeného `T_c^{mu nu}`. Literatúra nezávisle potvrdzuje, že jednoduché interagujúce dark-energy fluidy môžu mať fatálny skorý superhorizontový mód a že konzistentná perturbatívna formulácia je rozhodujúca; pozri [Valiviita, Majerotto a Maartens](https://arxiv.org/abs/0804.0232). Konkrétne identifikátory M-009/M-010 však pochádzajú z našich zachovaných auditov, nie z citovaného článku.

## Creation pressure — obmedzenie staršej formulácie

Efektívny tlak tvorby

```text
p_cr=-q/(3H)
```

presne prepíše zdrojovú rovnicu popola

```text
dot rho_c+3H rho_c=q
```

na konzervovaný tvar

```text
dot rho_c+3H(rho_c+p_cr)=0.
```

Je to alternatívne účtovanie. Ak sa rovnaké `p_cr` vloží na ľavú stranu a súčasne sa ponechá rovnaký explicitný zdroj `q` na pravej strane, energia sa započíta dvakrát. Skript 150 overil obe identity s maximálnym rezíduom `1.4210854715202004e-14`. Termodynamika kozmologickej tvorby častíc skutočne spája rýchlosť tvorby, tlak a entropiu, ale konkrétny rozklad závisí od zvoleného otvoreného-systémového popisu; pozri [Ivanov a Prodanov](https://arxiv.org/abs/1911.04380).

Staršie tvrdenie „K8 musí pridať creation pressure“ sa preto obmedzuje: K8 ho musí **odvodiť a účtovne zaradiť**, nie automaticky pridať navyše k explicitnému `Q^mu`. Entropický a šumový ledger naďalej chýba.

## Numerický a nezávislý audit

### Skript 150

- 9/9 kontrol PASS,
- 1000 vzoriek,
- runtime približne `0.015 s`, limit 5 s,
- maximálne projekčné rezíduum `2.842170943040401e-14`,
- geodetický nulový limit: presne `0.0`.

### Skript 151

- 5/5 kontrol PASS,
- `Q parallel u_c`: priestorová projekcia v c-frame presne nulová,
- `Q parallel u_f`: nenulová projekcia `(-0.0033576,-0.0335760,0,0)`,
- runtime približne `0.094 s`, limit 5 s.

## Dôvod, prečo K8 neumiera

No-go sa týka iba konkrétnych studených frame uzáverov Fc a Ff. Všeobecný collision kernel môže niesť tlak, rozptyl a šum, a preto nie je matematicky totožný s K1/K3. K8-Fkin má teda otvorený fyzikálny priestor, hoci zatiaľ neprešla G2.

## Ďalší krok

Pred drahou konštrukciou K8-Fkin vykonať rovnaký lacný G1–G2 audit A2-K9. K9 už zo svojej definície vyžaduje jeden spoločný produkčno-rozptylový operátor; audit rozhodne, či ide o skutočne uzavretejší mechanizmus alebo iba o pomenovanie chýbajúceho collision kernelu K8-Fkin.

