# KMPC-030 — procesový ledger pokusu 9

**Dátum:** 2026-07-16  
**Stav pred procesom 1:** `PREREGISTERED / HASH_FROZEN / NOT_RUN`  
**Fyzikálny stav:** `NONE_NOT_YET_AWARDED`  
**K4:** `LIVE / 60/100`  
**Technické počítadlo pred behom:** `8/10`  
**Autoritatívne po audite:** `9/10`

## Čo sa počíta ľudskou rečou

Najprv iba kontrolujeme, či dva zmrazené Python súbory majú platnú syntax a či
runner pozná správne argumenty. Až štvrtý proces znovu zostaví ten istý J8 systém
117 rovníc, zopakuje známu chybu na `fuel_Euler[8]`, urobí presne jednu
numerickú korekciu a skontroluje ju priamo aj cez maticu. Potom bez ďalšieho
solve porovná J4, J6 a opravený J8.

## Zmrazené hashe

| artefakt | SHA-256 |
|---|---|
| wrapper | `A8E2EA26B6960F23298259EFBECFFC9806ECF10F0207AE4D2B2AD0C2713DA0AB` |
| runner | `81D777534C552DC14E12807814FA63446807C1243B228EAFEE997F9D76B816FD` |

## Proces 1 — compile wrappera

**Stav:** `PASS / exit 0 / 0.7 s`  
**Očakávanie:** exit `0` do `10 s`, bez výstupu.  
**PASS:** syntax wrappera je platná; pred procesom 2 sa zapíše výsledok sem.  
**STOP:** syntax/import-free compile chyba je technická; pokus 9 sa označí
`TECHNICAL_FAILURE`, nie fyzikálnou smrťou, a opraví sa v ďalšej technickej
línii do limitu 10.

## Proces 2 — compile runnera

**Stav:** `PASS / exit 0 / 0.8 s`  
**Očakávanie:** exit `0` do `10 s`, bez výstupu.

## Proces 3 — help runnera

**Stav:** `PASS / exit 0 / 0.7 s / canonical CLI confirmed`  
**Očakávanie:** exit `0` do `10 s`; iba `--max-runtime-seconds` a `--audit`, bez
alternatívneho `--output`.

## Proces 4 — autoritatívny audit

**Stav:** `TECHNICAL_COMPLETE / exit 0 / payload 3.328 s / process 5.4 s`  
**Interný limit:** `4.8 s`; **vonkajší limit:** `10 s`.

Očakávaný priaznivý rozsah:

- pôvodný incident sa presne zopakuje na `fuel_Euler[8]` približne
  `1.5577e-10` a zostane pôvodne FAIL;
- po jednej korekcii driver `<=1e-10`, holdout `<=1e-9`;
- direct a affine cesty prejdú, ich absolútny rozdiel `<=1e-12`;
- forbidden layers `<=1e-10`, `U_c` regularita `<=1e-12`;
- coefficient drift `<=1e-8` relatívne alebo `<=1e-12` absolútne;
- rank `117/117`, všetko finite, všetky tri hooks a shape guards obnovené;
- J4/J6 a J6/J8 F0 aj M3 mosty PASS a tail sa nezhoršuje.

Ak všetko prejde, výstup je iba kandidát, že J4 je pre tento sentinel dostatočný;
hlavný orchestrátor ešte musí auditovať JSON. Ak niektorá numerická brána
neprejde, zostáva `REVIEW` bez druhej korekcie. Exception, timeout alebo zápisová
chyba sú technické, nie fyzikálny STOP.

## Release

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```

## Výsledok procesu 4 pred autoritatívnym auditom

Výstup:
`RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT.json`  
SHA-256:
`8CB706223C43EB4E72F2B56BE266C73E07349F2E0D6B32212E280AB64F803C6F`

- všetky `numerical_checks` sú `true`;
- pôvodný `fuel_Euler[8] = 1.5577307299e-10` sa reprodukoval;
- opravený driver `1.7100e-16`, direct driver `1.8114e-16`;
- holdout `3.3694e-11`, teda PASS voči `1e-9`;
- forbidden maximum `5.9167e-16`, `U_c` regularita `1.1097e-16`;
- coefficient drift `7.3733e-10`, teda PASS voči `1e-8`;
- všetky štrukturálne ladder checks sú `true` a tail je monotónne lepší;
- oba tails však na hlbokej ploche `z=1e-4` ostali nad relatívnym prahom:
  J4/J6 `1.2308e-5`, J6/J8 `3.3632e-6` voči `1e-6`.

Preto automatický text je `REVIEW_LADDER_STILL_UNCLOSED`. Nejde o technickú
chybu ani fyzikálnu smrť. Pred ďalším behom treba auditovať, či hlboký relatívny
tail `U_b` meria reálnu truncation chybu alebo pomer dvoch hodnôt blízko nuly.

## Autoritatívny audit hlavného orchestrátora

```text
ATTEMPT_9_CLOSED
TECHNICAL_COMPLETE
REVIEW_TAIL_METRIC_SEMANTICS
K4 = LIVE / 60/100
SCORE_EFFECT = NONE
```

Tri read-only audity potvrdili integritu hashu, presne jednu korekciu a všetkých
22 numerických PASS. Raw tail FAIL sa spätne neprepisuje. Jeho numerátor však
takmer celý tvorí drift formálne nulového `U_b[0]`: J4/J6 raw rozdiel
`5.9588e-16` oproti novým powers 5–6 iba `4.5800e-25`; J6/J8 raw rozdiel
`1.6282e-16` oproti powers 7–8 iba `7.8525e-35`. Preto raw metrika nie je dôkaz
nekonvergencie supportu. Posledný balík 10/10 smie bez solve a bez zmeny prahov
oddeliť common drift od explicitného added-power tailu.
