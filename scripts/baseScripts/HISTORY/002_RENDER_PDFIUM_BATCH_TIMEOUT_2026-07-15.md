# PDFium render - zachovaný timeout hromadného behu

**Dátum:** 2026-07-15  
**Skript:** `002_render_pdf_pages_bounded_pdfium.py`  
**Stav skriptu:** `REVIEW_FOR_BATCH_USE`  
**Stav vedeckého dôkazu:** nepoužitý

Hromadný shell príkaz požadoval tri po sebe idúce renderovania, spolu deväť
strán. Vonkajší limit 60 s bol dosiahnutý a proces bol ukončený. Výsledok renderu
nebol použitý vo fyzikálnom verdikte.

Príčina nebola izolovaná na konkrétnu stránku. Skript sa preto nesmie spúšťať ako
viacdokumentový balík. Prípadný budúci audit ho môže použiť iba po jednej strane,
s vonkajším limitom najviac 15 s a s kontrolou úplnosti PNG. Ak taký smoke test
neprejde, skript sa presunie medzi nefunkčné utility a nahradí systémovým
Popplerom.
