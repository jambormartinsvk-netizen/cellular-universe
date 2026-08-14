# KMPC-093 až KMPC-100 — HP-M1 matrix provenance: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov a interný audítor:** Codex (OpenAI)  
**Stav:** `INTERNALLY_AUDITED / VALID_DIAGNOSTIC_REVIEW`  
**Autoritatívny výsledok:** `REVIEW_C2_BI_K0p15_HP_M1_QR_BOUNDARY_LOCALIZED`

## Dôkazová identita

- immutable standalone raw KMPC-099:
  `93780C85488F17831562238D61FF2ADA70182163B488687BAB49BA9A6E96ECD9`;
- read-only publication receipt KMPC-100:
  `2581BC157F0CBA08D91654A9BCE9976D93429D9DB6AA0FA2AE4765F05AD9CC1A`;
- runner 343 / V7:
  `B391FB0FB497922BB63C0F528CA3A5699B47E645B610A4D13084BE1357E1A5BD` /
  `B2CF9C98734303122F82CE85D4BE2D560EA853126EFC447E82C05EAAB77CE9E0`;
- runner 344 / V8:
  `C164D6909B2CF090CF807103BB80E8822FBBBA7F41A76349F0506A4DBE5EA1AA` /
  `28B4950759B494228AFF74A2078CD5D2A13C2D66051B02CD5C7845585702DB59`;
- KMPC-100 overil SHA, V7 source ledger, diagnostic status, všetky tri ranky,
  nulový autoritatívny HP-M1 solve a zákaz C2 PASS bez opakovania matice.

## Technická línia

| Beh | Incident alebo výsledok | Stav |
|---|---|---|
| KMPC-093 | PF-096: nested attribution owner nerozpoznal outer M1 overlay | technický, bez fyziky |
| KMPC-094 | PF-097: `mpmath.qr_solve` označil 121×98 systém singulárny | technický, bez raw |
| KMPC-095 | PF-098: neuskutočniteľný scale fixture | technický, official nebežal |
| KMPC-096 | PF-099: column equilibration nezmenila QR výnimku | technický, bez raw |
| KMPC-097 | PF-100 nesprávny smoke argument; PF-101 zahodené `delta_f,U_f` | technický, bez success raw |
| KMPC-098 | PF-102: neaplikovateľná stará attribution-reference brána | technický, bez success raw |
| KMPC-099 | PF-103 až po exclusive publish: legacy terminal summary chcel `atom_id` | diagnostický raw je platný |
| KMPC-100 | read-only receipt, všetky kontroly prešli, exit 0 | `VALID_DIAGNOSTIC_RECEIPT` |

Incidenty PF-096 až PF-103 nie sú fyzikálne verdikty. KMPC-099/100 tvoria
úspešný vecný diagnostický výsledok, preto sa aktívny technický counter po
internom audite resetuje z `8/10` na `0/10`; úplná história zostáva.

## Výsledok matrix provenance

| Veličina | Natívna 80-dps assembly po binary64 projekcii | Frozen binary64 rebuild |
|---|---:|---:|
| shape | `121×98` | `121×98` |
| rank | `98/98` | `98/98` |
| condition | `634.5198855041807` | `634.5198855041809` |
| najväčšia singular value | `340.9961614309948` | `340.99616143099473` |
| najmenšia singular value | `0.5374081557113753` | `0.5374081557113750` |
| nulové stĺpce | `0` | `0` |
| nulové riadky | `5` | `5` |
| matrix+rhs SHA | `CB188D24...362FD5` | `67E7398B...7D8EF` |

Pravé strany sú byteovo rovnaké: zmenených `0` prvkov. Matice nie sú
byteovo totožné, ale líši sa iba `26` prvkov. Maximum je
`1.7763568394002505e-15` v `fs_shear[6] × eta[6]`:
natívna projekcia `-9.6`, frozen rebuild `-9.600000000000001`.
Maximálny rozdiel voči globálnej scale je `5.2868e-18` a relatívny
Frobeniov rozdiel `6.0852e-18`.

Binary64 diagnostický bridge mal rank `98` a unweighted residual L2
`6.3483e-15`. Slúžil iba na dokončenie diagnostiky. Počet autoritatívnych
HP-M1 solve je `0`; `pass_c2_atom_candidate=false`. Driver/holdout PASS polia
z bridge riešenia nie sú fyzikálne brány a zostali false.

## Interný audit a prínos

1. Obe nezávislé zostavenia majú rovnaký plný stĺpcový rank, prakticky
   identické spektrum a condition. Päť nulových riadkov je rovnakých na oboch
   stranách a nespôsobuje stratu stĺpcového ranku.
2. Rozdiel `e-15` je konzistentný s rozdielom natívnych racionálnych
   koeficientov a už vykonaných binary64 produktov; nie je materiálnou zmenou
   M1 systému. Nebol zavedený nový numerický PASS prah, report je opisný.
3. Predošlé `mpmath.qr_solve: matrix is numerically singular` preto nemožno
   pripísať frozen binary64-projected ranku, zlej pravej strane ani column
   scale. Blokér je lokalizovaný na high-precision QR/algoritmickú hranicu.
4. Výsledok ešte nedokazuje natívny 80-dps rank priamo HP rank-revealing
   metódou a nevytvára HP M1 riešenie. Preto neuzatvára `Einstein_0i[7]` ani
   C2 BI/k=.15.
5. KMPC-100 compatibility polia `M1/core/common/tail/background=false` sú
   explicitne `NOT_EVALUATED_RECEIPT_ONLY`; nesmú sa interpretovať ako FAIL.

## Autoritatívny dopad

- C2 zostáva `5/10 PASS`;
- P5 zostáva `3.5/6`;
- A2-K4 zostáva `LIVE / 60/100`, bez fyzikálneho STOP;
- prediction table, release a Zenodo trigger zostávajú `NONE`;
- technický counter sa resetuje na `0/10`.

## Ďalší predregistrovaný krok

KMPC-101 má na presne tej istej natívnej 80-dps redukovanej M1 matici použiť
jednu explicitne rank-revealing high-precision metódu (SVD alebo ekvivalentný
audited pseudoinverse solve). Musí najprv reportovať natívny HP rank/spektrum,
potom unweighted residual a riešenie. Žiadne row weights, zmena rovníc,
supportu, backgroundu alebo prahov nie sú povolené. Ak natívny HP rank nie je
`98`, krok končí REVIEW bez downstream fyziky. Ak je `98` a residual prejde,
až samostatný successor smie vložiť HP M1 do zmrazeného F0/M3/non-fit
holdout pipeline.
