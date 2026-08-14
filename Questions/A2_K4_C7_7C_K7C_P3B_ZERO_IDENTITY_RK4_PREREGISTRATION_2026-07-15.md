# K7c P3a-B — predregistrácia RK4 po presnej nulovej identite

Dátum: 2026-07-15  
Stabilné ID: `SCI-A2K4-C7G5-K7C-P3B-ZERO-IDENTITY-RK4`  
Typ: izolovaná evolučná fyzikálna brána  
Score effect pred výsledkom: `NONE`

## Otázka

Odstráni auditovaná presná nula dvoch koeficientov príčinu neasymptotického
RK4 správania K7c, alebo po oprave zostáva ďalšia dynamická/numerická stena?

## Zmrazené vstupy

| Artefakt | SHA-256 |
|---|---|
| čistý P1 skript 197 | `088B4CD58F57A30BD061D30042BA3E2CB5021DF9BF320003ED8291D86FB6C022` |
| P1 raw JSON | `A5A94550BB7542090D6244237326404A5A5CD2298D4D70A53C061B2A6B791BA5` |
| seed source 178 | `875ABF60DAE70D322CBFB5A9BC16361E2EF4861A0267E4555BCF6BD353DD6F55` |
| P3a-A skript 201 | `03AA42272D05B8031EC54A39209275EE6B15D448FFE7204AA20EE25967FCAF38` |
| P3a-A raw JSON | `4C9747DEF1AB9662735E974B1A992C6FC12784F20F69EB4A73862A9E234C7E65` |

## Jediná povolená fyzikálna zmena

V ôsmom RHS komponente `M'` sa odstránia presne tieto dva identicky nulové
členy:

[
left({3over2}Omega_b-W_gamma{Rover1+R}ight)U_gamma,
qquad
left({W_gammaover4(1+R)}-{Omega_gammaover2}ight)delta_gamma.
]

Žiadna iná fyzikálna alebo numerická zmena nie je povolená. Background,
seed, 13-zložková báza, projekcia, ostatných sedem členov `M'`, ostatných
12 RHS komponentov, closure, normalizácia, safety cap, RK4 integrátor,
kroky `0.0025/0.00125/0.000625`, interval, checkpointy a normy zostávajú
zhodné so skriptom 197. Rozdiely v názve testu, provenance kontrolách,
verdict logike a fail-closed výstupe sú auditná vrstva, nie fyzika.

Samostatný source-delta audit musí toto obmedzenie potvrdiť pred evolúciou.

## Predbehové očakávanie

Centrálne očakávanie pri správnej diagnóze:

- `difference_200_400 < 1e-6`;
- `8 <= difference_100_200/difference_200_400 <= 32`;
- tri checkpointy na každej mriežke, konečné stavy/RHS;
- density a momentum cancellation monitory pod pôvodným `5e-12`;
- rovnaké seed/background/integrátorové fingerprinty.

Prah sa po výsledku nemení. Menší rozdiel alebo lepší pomer mimo brány je
iba diagnostický pokrok, nie PASS.

## Rozhodovanie

- source-delta, provenance alebo formálna brána FAIL: `REVIEW`, evolúcia
  sa nepovolí alebo sa jej čísla fyzikálne neinterpretujú;
- všetky technické brány a obe fyzikálne brány PASS:
  `PASS_P3B_ZERO_IDENTITY_RK4_CONVERGENCE`; otvorí sa širší G4/G6 audit;
- platná evolúcia, ale aspoň jedna fyzikálna brána FAIL:
  `STOP_P3B_ZERO_IDENTITY_NOT_SUFFICIENT`; dôkazy a skripty sa zachovajú
  a pokračuje samostatný audit lokálnej tuhosti/eigenmódov;
- timeout: `TIMEOUT_UNCLOSED`, nie fyzikálny rozsudok.

Interný limit evolučného behu je 25 s, seed source 15 s, jeho child 6 s a
externý limit 30 s. Výstup a tri grid checkpointy musia byť nové a nesmú sa
prepísať.
