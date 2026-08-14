# KMPC-101/102 — natívny HP-M1 CPQR: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov a interný audítor:** Codex (OpenAI)  
**Stav:** `INTERNALLY_AUDITED / VALID_DIAGNOSTIC_REVIEW`  
**Autoritatívny výsledok:** `REVIEW_C2_BI_K0p15_NATIVE_HP_M1_SOLVER_BOUNDARY_CLOSED`

## Dôkazová identita

- immutable KMPC-102 raw:
  `49187BB85B8C59559A23EF6741DFB64F0015C2F0CC458D5C9D284FF2CECDE0CB`;
- V9 calculation modul:
  `8EBDA7232BEADF0640A2C8361B444A9A896EB215E159E552AC494EAE2C0CCD0A`;
- V10 routing wrapper:
  `0E70793D89F32D70A0B1CDB021DE4D8C5785D06DB7245BE83ED2F2F720920801`;
- runner 346:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- official runtime: `17.719 s` vnútri zmrazeného limitu `45.0 s`;
- source ledger `39/39`, prerequisite ledger `15/15`, payload contract aj
  všetkých sedem checks sú true.

## Technický incident PF-104

Runner 345 compile/help/smoke prešiel, ale prvé official CLI volanie použilo
iba basename v `--output`. Stabilný harness skončil v `guarded_import` pred
M1 assembly a CPQR. Failure raw má SHA
`378A4FC7180E01FD89AF58CA803D3FBDD058DED6AA57AF38E1D1EB0B53A119CA`.

KMPC-102 bol predregistrovaný routing-only successor. V9 calculation modul,
metóda aj prahy ostali byteovo nezmenené. Úspešný vecný výsledok resetuje
aktívny technický counter z `1/10` na `0/10`; PF-104 zostáva v histórii.

## Výsledok natívneho rank-revealing solve

| Veličina | Výsledok | Zmrazená brána |
|---|---:|---:|
| shape | `121×98` | presne `121×98` |
| natívny 80-dps rank | `98/98` | `98` |
| rank absolute threshold | `3.3618661e-58` | `1e-60 × max initial column norm` |
| najväčšia CPQR diagonála | `336.1866148436` | report |
| najmenšia resolved diagonála | `0.7279919762` | nad rank prahom |
| min/max diagonála | `2.1654401e-3` | report, nie condition number |
| `max|Q^TQ-I|` | `3.2077340e-81` | `<=1e-60` |
| relatívna chyba `AP-QR` | `1.0034615e-82` | `<=1e-60` |
| relatívny normálový reziduál | `7.8497783e-85` | `<=1e-55` |
| unweighted residual L2 | `6.1837151e-83` | report |

Stĺpcová permutácia má SHA
`0D4653D149FA907C83732D5F731455745B8DB35B0A55F0563376B2525AF62686`.
Použil sa presne jeden natívny HP-M1 solve, bez row scalingu a bez zmeny
neváženého least-squares cieľa.

## M1 lokálne rezíduá

- driver + initial maximum relative residual:
  `1.6724456e-80`, worst `cdm_continuity[7]`;
- driver absolute-fallback maximum:
  `3.9520395e-83`, worst `initial:Ufs[-1]`;
- M1 non-fit holdout maximum relative residual:
  `1.3941708e-17`, worst `Einstein_00[2]`;
- holdout absolute-fallback maximum:
  `3.0067091e-84`, worst `Einstein_0i[-1]`;
- raw M1 driver-and-holdout boundary je true;
- najväčší rozdiel oproti frozen binary64 M1 koeficientu je
  `3.6342457e-16` pri `delta_fs[1]`.

Tieto holdouty patria k samotnej M1 order-7 sústave. Nie sú totožné s
finálnym C2 holdoutom po F0, fractional-background a M3 handoffe. Preto ich
PASS ešte neuzatvára historické `Einstein_0i[7] = 3.0197566e-9`.

## Interný audit

1. Predregistrácia zmrazila metódu, rank prah aj tri numerické brány pred
   prvým production CPQR solve. Smoke nezávisle rozlíšil rank 3 aj presne
   deficientný rank 2 a vynútil pivot.
2. Natívny rank `98/98` priamo potvrdzuje projected-rank záver KMPC-099.
   Najmenšia resolved CPQR diagonála je približne `2.17e55`-krát nad
   absolútnym rank prahom; rank záver nie je hraničný.
3. Ortogonalita, faktorizácia a normálový reziduál prešli o 21 až 30 rádov
   pod zmrazenými bránami. Staré `mpmath.qr_solve: numerically singular` je
   tým uzavreté ako algoritmická chyba nepivotovaného solvera, nie fyzikálna
   singularita M1 sústavy.
4. Natívne HP M1 riešenie uzatvára vlastné driver aj non-fit holdout riadky,
   ale skript správne potlačil `M1/core/common/tail/background` physics PASS
   polia a `pass_c2_atom_candidate=false`.
5. Ďalší krok už nesmie meniť solver ani M1 maticu. Musí iba vložiť toto
   HP-M1 riešenie do zachovaného 13-stavového registra, prepočítať zmrazený
   F0/M3/non-fit holdout pipeline a zmerať finálny `Einstein_0i[7]`.

## Autoritatívny dopad

- HP-M1 solver boundary: **uzavretá diagnosticky**;
- C2 zostáva `5/10 PASS`;
- P5 zostáva `3.5/6`;
- A2-K4 zostáva `LIVE / 60/100`, bez fyzikálneho STOP;
- prediction table, release a Zenodo trigger zostávajú `NONE`;
- aktívny technický counter: `0/10`.

## Ďalší predregistrovaný krok

KMPC-103 smie byť jediný downstream-insertion successor. Musí byteovo
zachovať V9 solver a prahy, zlúčiť 11 HP-M1 stavov do pôvodného 13-stavového
registra so SHA dôkazom nezmenených `delta_f,U_f`, spustiť existujúci exact
F0/M3/non-fit holdout rez a reportovať finálny `Einstein_0i[7]` aj všetky
ostatné zmrazené C2 brány. Stará KMPC-087 attribution-reconstruction brána,
ktorá po legitímnej zmene M1 už nie je invariantom, sa nesmie používať ako
success gate; prípadná nová atribúcia musí byť iba novým ledgerom voči
aktuálnemu výsledku. Fyzikálny PASS môže prideliť až interný audit raw.
