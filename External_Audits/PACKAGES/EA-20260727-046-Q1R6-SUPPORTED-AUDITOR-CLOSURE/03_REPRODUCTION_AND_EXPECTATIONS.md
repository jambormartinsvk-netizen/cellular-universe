# Statický T1 audit EA-046

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath .\EVIDENCE\002__Q1R6_ARXIV_SOURCE.tar.gz
Get-ChildItem -LiteralPath . -Recurse -Force -File
tar -tzf .\EVIDENCE\002__Q1R6_ARXIV_SOURCE.tar.gz
tar -xOf .\EVIDENCE\002__Q1R6_ARXIV_SOURCE.tar.gz main.tex
```
Očakáva sa archive hash `5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416`, 11 entries, 16 package files, 9 evidence, `REPRO=0`, runtime 0; Python/smoke/official/generated JSON `NOT_RUN`.
