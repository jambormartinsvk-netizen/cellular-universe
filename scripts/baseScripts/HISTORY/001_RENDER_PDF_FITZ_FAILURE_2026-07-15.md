# Neúspešný PDF render cez `fitz`

**Stav:** `NONFUNCTIONAL_IN_CURRENT_RUNTIME`  
**Skript:** `001_render_pdf_pages_bounded.py`  
**Dátum:** 2026-07-15

Skript prešiel `py_compile`, ale pri spustení skončil ešte pred otvorením PDF:

```text
ModuleNotFoundError: No module named 'fitz'
```

Nešlo o chybu vstupného PDF ani o vedecký výsledok. Prostredie obsahovalo
`pypdfium2`, preto skript superseduje
`002_render_pdf_pages_bounded_pdfium.py`. Skript 001 sa nesmie v tomto runtime
spúšťať ani citovať ako vykonanú vizuálnu kontrolu.

Časové limity neboli zmenené: vnútorný limit 45 s, vonkajší limit 60 s.
