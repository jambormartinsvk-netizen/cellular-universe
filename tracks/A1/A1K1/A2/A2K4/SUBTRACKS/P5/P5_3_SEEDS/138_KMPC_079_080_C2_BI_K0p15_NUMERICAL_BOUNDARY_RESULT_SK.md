# KMPC-079/080 — C2 BI/k=.15 numerical boundary: výsledok

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Stav:** `REVIEW_INDEPENDENT_HOLDOUT_NUMERICAL_BOUNDARY`

KMPC-079 raw SHA je
`014B3F7E76929ED7C3DC894C8B84550AB68435BF7BC2A650788801D786D4A5E5`.
KMPC-080 same-matrix raw SHA je
`028BE28F8111FE6F775ACFC68A46FF51156DE0F1BD753D5A9C9CEA1CDF83DD1F`.

Tri corrections na presne tej istej 104×104 matici boli vybrané korektne:
main-driver maximum kleslo z `1.5550018952758203e-10` na
`1.3521906982651137e-16`, `M3_driver=true`. Core však ostal REVIEW, pretože
nezávislý holdout `Einstein_0i[7]` má relatívne rezíduum
`3.019756779905407e-9 > 1e-9` pri absolútnom rezíduu iba
`8.728840268468619e-17`.

M1, rank, forbidden-layer/stress, S-C0, common, tail a background brány
prešli. Nejde o fyzikálny STOP ani support fail. C2 ostáva `5/10 PASS`;
BI/k=.15 sa nepripočítava. Ďalší krok musí predregistrovať numerický boundary
audit toho istého 104×104 systému s vyššou presnosťou a bez pridania holdout
riadkov do fitovanej matice.
