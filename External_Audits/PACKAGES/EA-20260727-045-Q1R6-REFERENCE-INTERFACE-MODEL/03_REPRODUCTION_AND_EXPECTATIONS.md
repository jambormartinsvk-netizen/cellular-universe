# Statický T1 audit a očakávania EA-045

EA-045 je statický T1 primary-source capsule. Nemá runtime closure, `REPRO`
adresár, executable runner, smoke ani official calculation.

Externý auditor môže iba v package pracovnom adresári vykonať tieto bounded
package-local read-only príkazy (žiadny príkaz nesmie otvoriť live cesty):

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath .\EVIDENCE\002__Q1R6_ARXIV_2204_13120_SOURCE.tar.gz
Get-ChildItem -LiteralPath . -Recurse -Force -File
tar -tzf .\EVIDENCE\002__Q1R6_ARXIV_2204_13120_SOURCE.tar.gz
tar -xOf .\EVIDENCE\002__Q1R6_ARXIV_2204_13120_SOURCE.tar.gz main.tex
```

Očakávanie: archive hash je
`5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416`; archive
má 11 deklarovaných položiek; package obsahuje 20 files, 13 manifestovaných
evidence kópií, `REPRO=0` a runtime rows `0`. Žiadny generated JSON,
Python, smoke ani official audit sa neočakáva.

Správny audit môže potvrdiť alebo zúžiť reference-interface scope a nájsť
presnú passport/gate medzeru. Nemôže z tohto balíka vydať complete W10,
fyzikálny no-go, computed verdict, A3 výsledok ani zmenu projektu.
