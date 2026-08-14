# A3/K3a — manifest, prostredie a stav balíka

**Dátum:** 2026-07-13  
**K5/K1:** `MŔTVA — ARCHIVOVANÁ M-012`  
**K5/K3a:** `PREŽÍVA K3a.0 — 40/100; G_eff A RAST EŠTE NEOVERENÉ`

## 1. Prostredie

```text
OS       Windows 10.0.26200
Python   3.11.3
CAMB     1.6.6
NumPy    2.4.6
SciPy    1.17.1
```

CAMB, NumPy a SciPy boli izolovane nainštalované do `.deps/python`.
Adresár je lokálna závislosť a podľa plánu sa nesmie commitnúť. Prvý pokus o
CAMB 1.6.7 zlyhal, pretože dostupný balíkový index končil verziou 1.6.6.
Výpočet bol následne fixovaný na skutočne dostupnú verziu 1.6.6; neúspech sa
nezamlčuje.

## 2. Rozhodovacie výstupy

### A3-K5/K1

```text
lambda=0 growth null error          0.0
weighted growth ratio               1.0519633794 to 1.0530532566
constant-w CAMB S8                  0.9338450635
constant-w hybrid K5/K1 S8          0.9836423799
CPL CAMB S8                         0.9552570774
CPL hybrid K5/K1 S8                 1.0062658626
predeclared KiDS screen             0.863
required As reduction               23.03% to 26.45%
status                              FAIL_A3_CONSERVATIVE_GROWTH_GATE
verdict                             DEAD M-012
```

Rozsudok je konzervatívna CMB-normalizovaná rastová brána, nie tvrdenie
plnej vlastnej K5/K1 TT/TE/EE/lensing alebo KiDS likelihood.

### K5/K3a.0

```text
action          f=-f1(phi)rho_c+eta Z^2
eta grid        0, 0.1, 0.5, 1, 2, 5
rho residual    2.22045e-16
pressure resid. 2.22045e-16
Q residual      2.77556e-17
q_s             positive on all tested points
q_c             positive on all tested points
hat(c_s)^2      positive on all tested points
c_CDM^2         exactly zero by f_,ncnc=0
step convergence max 1.519e-8
status          PASS_K3a_ACTION_BACKGROUND_HIGH_K_STABILITY_GATE
```

K3a.0 ešte nedokázala `G_eff,c<=G` pri súčasnom `f1!=0`; to je povinná
K3a.1 brána.

## 3. SHA-256 dôkazov

| Súbor | SHA-256 |
|---|---|
| `scripts/45_script_A3_K5_K1_CAMB_anchor_and_growth_bound.py` | `F0DE5BD1C801F86441F03861F1539980FB1CA36552D82E2D16BF9F2FF873689A` |
| `scripts/46_script_A3_K5_K1_required_primordial_amplitude.py` | `9F86BF5B35D66C96E9BD46A6242F6D4104977AE9FFADA1166991B2AC0B03DD15` |
| `scripts/47_script_A2_K5_K3a_action_background_stability_gate.py` | `4DF23622A64836A818BBD0BBF4DFBB0557A07FA136027B98F92B09A1815DCAF3` |
| `scripts/33_script_A2_K5_K1_quasistatic_growth_gate.py` | `D05F7A548D9E4050102A8EAB298F83059AD164C55F284CD0FCB4C0D3721337C3` |
| `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py` | `7FB9E3BF82ABE1A1985E426AA37F00B40329EEA9781B4334B20359A99898BA6E` |
| `Audit/A3_K5_K1_MRTVA_CMB_normalizovana_rastova_brana_M012.md` | `5711BFCA8905ABCC2219517893DEE2A3BBB10F46F34FC86A74004DAE8391C633` |
| `Audit/A2_K5_K3a_0_akcna_backgroundova_stabilitna_brana.md` | `0B479A6711F19F0804F467B970940193101FA4A1BDF0D00D41EF37AADB1CE511` |
| `Audit/REGISTER_MRTVYCH_KOLAJI_A_DOKAZOV_v3.18_ADDENDUM_A3.md` | `66772422184312677FD8A460178FC7B28441E80B90E99F88585C355F0B6A2602` |
| `Questions/A3_STAV_A_AKCNY_PLAN_PO_M012_A_K3a_0.md` | `5EED4AB80D7C0141CE9D87DBBE9524FFD81E4534CD93504863C90DB112895E63` |
| `Questions/PLAN_upratania_dokumentacie_GitHub_Zenodo.md` | `76FB1C064B708FC729B329392FA27568D75FBCF11535AECA77C75361FEC1F5AA` |
| `theory/SK/05j_Methodology_Rules_and_Question_Register_A3_K3a_SK.md` | `7336440C0EC1ABA772A39B7E79BE19A3586166E9D354F85259C8B62C9C97B18B` |
| `theory/EN/05j_Methodology_Rules_and_Question_Register_A3_K3a_EN.md` | `5A60396C4EA335249E0F6A60FEAD7AD8C4B8431738A7B79894BE53946EB19F45` |

## 4. GitHub a dokumentácia

Vzdialený repozitár
`https://github.com/jambormartinsvk-netizen/cellular-universe.git` bol
čítaním overený: vetva `main` ukazovala na
`77828f767ce2ecdbf7e4535e91926f7cbc1b5a50`. Lokálny `.git` je neplatný;
nebol inicializovaný, prepísaný ani pripojený. Bezpečný staging a migrácia sú
zapísané v `Questions/PLAN_upratania_dokumentacie_GitHub_Zenodo.md`.

## 5. Povinný nasledujúci fyzikálny krok

K3a.1: úplné súčasné `f1+eta Z^2` perturbácie, dva nulové limity a presné
`G_cc`, `G_cb`, `G_bc`, `G_bb` na A1 backgrounde. Až výsledok tejto brány
smie rozhodnúť, či K3a naozaj odstraňuje rastový problém M-012.
