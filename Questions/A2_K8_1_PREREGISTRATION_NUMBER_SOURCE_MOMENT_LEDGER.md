# A2-K8.1 — predregistrácia momentového auditu produkcie počtu

## Cieľ

Rozhodnúť, či registrované tvrdenia

```text
nabla_mu(n_c u_c^mu)=S_n,
m_c=constant,
m_c S_n=Gamma rho_f
```

stačia na úplné prejdenie G2 — background a úplný ledger energie aj hybnosti — bez skrytého frame alebo momentum placeholdera.

## Zmrazené konvencie

- signatúra metriky `(-,+,+,+)`,
- `u_c^mu u^c_mu=-1`,
- `N_c^mu=n_c u_c^mu`,
- studený popol `T_c^{mu nu}=rho_c u_c^mu u_c^nu`,
- `rho_c=m_c n_c`, `m_c=constant`,
- `a_c^nu=u_c^mu nabla_mu u_c^nu`, `u_c.nu a_c^nu=0`,
- A1 backgroundový tok `q=Gamma rho_f>0` smeruje z paliva do popola.

## Vopred odvodená identita na kontrolu

Z produktového pravidla musí vyjsť

```text
nabla_mu T_c^{mu nu}=m_c S_n u_c^nu+rho_c a_c^nu.
```

Projekcie musia dať

```text
-u^c_nu Q_c^nu=m_c S_n,
h^alpha_nu Q_c^nu=rho_c a_c^alpha,
h^alpha_nu=delta^alpha_nu+u_c^alpha u^c_nu.
```

## Brány

1. **Background ledger:** `dot rho_c+3H rho_c=q` a `dot rho_f+3H(1+w_f)rho_f=-q` sa musia presne sčítať na nulu.
2. **Momentová úplnosť:** audit rozhodne, či samotný skalár `S_n` určuje aj kolmú časť `Q_c^mu`.
3. **Geodetický nulový limit:** pri `a_c^mu=0` musí vzniknúť `Q_c^mu=m_cS_n u_c^mu`.
4. **Frame mapa:** studený comoving zrod sa musí porovnať s už auditovanou K1; fuel-frame zrod s K3; energy-frame s K4.
5. **Creation-pressure bookkeeping:** efektívny `p_cr=-q/(3H)` je dovolený iba ako prepis explicitného zdroja, nie súčasne s tým istým `Q^mu`.

## Rozsudky

- G2 PASS iba ak je energia aj hybnosť určená bez ďalšieho frame/kernelu.
- Ak background prejde, ale priestorový moment zostane voľný, rodič K8 ostáva `OTVORENÁ — 10/100`, nie mŕtva.
- Konkrétny frame, ktorý je deterministicky totožný s už mŕtvou koľajou, dedí jej no-go a nevytvorí nový živý mechanizmus.
- Nová kinetická distribúcia zrodu môže zostať živou podkoľajou iba ak explicitne určí aspoň nultý, prvý a tlakový/šumový moment.

## Limity výpočtu

- každý skript: interný limit najviac 5 s,
- externý limit: 10 s,
- žiadne ladenie parametrov a žiadna kozmologická integrácia.

