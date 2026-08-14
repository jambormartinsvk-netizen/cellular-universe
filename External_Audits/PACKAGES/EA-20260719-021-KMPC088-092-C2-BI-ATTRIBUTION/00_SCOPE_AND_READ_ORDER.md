# Scope — KMPC-088 až KMPC-092 BI coefficient attribution

- Package ID: `EA-20260719-021-KMPC088-092-C2-BI-ATTRIBUTION`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Reprodukuje KMPC-092 úplný read-only 73-term ledger frozen rovnice
`Einstein_0i[7]` z KMPC-087? Je rezíduum
`-5.497017142831483e-17` dôsledkom zrušenia exact-driver subtotalu
`+7.066191085120618e-9` s upstream subtotalom `-7.066191140090789e-9`,
pričom dominantný upstream owner je fractional background × M1 a F0 je
iba malý príspevok? Opravili KMPC-089 až 092 iba serializáciu, fixture,
binary64-product ledger a owner lifecycle bez zmeny fyziky?

## Poradie čítania

1. Evidence 001–004: protokol, C2 kontrakt a frozen KMPC-087 východisko.
2. Evidence 005–012: predregistrácie a technické/error registre.
3. Evidence 013–017: aktuálny plán, interný audit, failure raws a úspešný raw.
4. Evidence 018–027: päť runnerov a päť versioned attribution modulov.
5. Dokument 03 a fresh-copy reprodukcia iba runnera 336.

## Nonclaims

- Nie je to BI/k=.15 PASS, fyzikálny STOP ani dôkaz chybnej rovnice.
- Atribúcia sama nerozlišuje, či binary64 obmedzenie vzniká v M1 stave alebo
  vo fractional-background generátore, pretože dominantný blok je bilineárny.
- Holdout sa nepridáva do solve; support, rovnice a prahy sa nemenia.
- K4 ostáva `60/100`, P5 `3.5/6` a C2 `5/10`.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje 73 členov, rovnaké term/driver/holdout
fingerprinty, nulový počet holdout riadkov vo fite, presne dva HP solve,
úspešnú serializačne viazanú rekonštrukciu a zhodné owner/species subtotaly.
Odchýlka je `REVIEW_REPRODUCTION_MISMATCH`, nie automatický fyzikálny verdikt.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
