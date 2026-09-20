# Instrukcja Kontynuacji Prac (Continuation Guide)
## Husqvarna Viking Automatic - Klasa 21 / 21A / 21E Operating Manual (56-Page Booklet)

Niniejszy dokument stanowi kompletne podsumowanie stanu projektu, analiz tekstu oraz procedur, umożliwiając natychmiastowe podjęcie i kontynuowanie prac na dowolnym innym komputerze / w nowej sesji agenta.

---

## 🎯 1. Cel i Wymagania Końcowe
- **Format:** Oryginalny format fabrycznej książeczki Husqvarny: **Landscape Booklet A5** (poziomy format 56 stron, `@page { size: 210mm 148mm; margin: 0; }`).
- **Język:** Angielski (pełny, fabryczny tekst Viking / Husqvarna Automatic Class 21 / 21A / 21E).
- **Jakość dokumentu:** Prawdziwy dokument cyfrowy (czysty skład typograficzny, przeszukiwalny tekst, ostre linie, brak plam, cieni skanu czy odręcznych dopisków).
- **Ilustracje i schematy:** Wszystkie oryginalne ilustracje (akcesoria, stopki, nawlekanie, wzorniki krzywek A/B/C/D, cerowanie, smarowanie) oraz pełne rozkładówki techniczne (**Fig. 1 – Front View** oraz **Fig. 2 – Rear View**) z angielskimi oznaczeniami podzespołów 1–40.

---

## 📂 2. Struktura Projektu w Repozytorium

```text
husqvarna-21-manuals/
├── README.md                                             # Główny opis repozytorium
├── CONTINUATION_GUIDE.md                                 # Ten dokument (instrukcja kontynuacji)
├── Husqvarna_Automatic_Class_21_Operating_Manual_EN.html # Główny plik źródłowy HTML (56 stron)
├── Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf  # Skompilowany dokument PDF (56 stron A5)
├── Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf        # Instrukcja serwisowa PL (klasa 21)
├── Husqvarna_21A_Automatic_Operating_Manual_EN_A4.pdf    # Wersja pomocnicza EN (pionowe A4)
├── images_manual_en/                                     # Katalog wszystkich rycin i ilustracji (ponad 70 plików)
├── scripts/                                              # Skrypty generatorów i kadrowania
│   ├── build_full_manual.py                              # Główny skrypt generujący 56 stron HTML
│   ├── crop_all_manual_images.py                         # Skrypt automatycznego wycinania rycin
│   ├── render_hires_en.py                                # Renderowanie stron skanu EN w wysokiej rozdzielczości
│   ├── scan_en_pages.py                                  # Analiza i podgląd stron angielskich
│   ├── build_en_a4_pdf.py                                # Skrypt pomocniczy dla wersji A4
│   ├── crop_clean.py                                     # Czyszczenie i przycinanie krawędzi
│   └── crop_figures.py                                   # Kadrowanie figur technicznych
└── data/                                                 # Baza analiz tekstu i OCR
    ├── en_full_ocr.json                                  # Pełny OCR wszystkich stron podręcznika EN (JSON)
    ├── en_djvu.txt                                       # Wyodrębniony tekst z oryginalnej warstwy DjVu
    └── Husqvarna_21A_djvu.xml                            # Szczegółowa mapa współrzędnych słów (XML DjVu)
```

---

## 📌 3. Zadania do Wykonania (Zgłoszone przez Użytkownika)

1. **Oczyszczenie rycin z tekstów norweskich:**
   - W części rycin w katalogu `images_manual_en/` (wyciętych pierwotnie z poziomego skanu norweskiego) znalazły się fragmenty opisów w języku norweskim, np.:
     - `fig_26_buttonhole_foot.png` i `fig_26a_buttonhole_steps.png` (zawierają tekst „Så syr De knapphullet slik...”).
     - Ewentualne nagłówki wzorników krzywek (`cam_b_patterns.png`, `cam_cd_patterns.png` itp.).
   - **Rozwiązanie:** Należy wykadrować same ryciny bez otaczającego tekstu lub podmienić je na odpowiedniki wycięte bezpośrednio ze skanu angielskiego (`Husqvarna_21A_Automatic_Manual_EN.pdf`).
2. **Dopasowanie składu tekstu i zdjęć do oryginału:**
   - Zweryfikować układ każdej strony z osobna w zestawieniu z oryginalną książeczką (układ kolumn, położenie rysunków po lewej/prawej stronie).
3. **Korekta językowa i ortograficzna:**
   - Przeprowadzić pełny spellcheck angielskich tekstów zawartych w `scripts/build_full_manual.py`.

---

## 🛠️ 4. Jak Uruchomić i Kompilować Projekt

### Wymagania:
- Python 3 (`pip install Pillow`)
- Chromium lub Google Chrome (do bezgłowej kompilacji HTML -> PDF)
- Opcjonalnie Poppler (`pdftoppm`, `pdfinfo`) do podglądu wyrenderowanych stron

### Komendy:
1. **Generowanie pliku HTML:**
   ```bash
   python3 scripts/build_full_manual.py
   ```
2. **Kompilacja do gotowego PDF (A5 landscape booklet):**
   ```bash
   chromium --headless --no-sandbox --disable-gpu --print-to-pdf="Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf" Husqvarna_Automatic_Class_21_Operating_Manual_EN.html
   ```
3. **Podgląd wybranej strony jako obrazu PNG (np. strona 20):**
   ```bash
   pdftoppm -png -r 150 -f 20 -l 20 Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf preview_p20
   ```

---

## 🌐 5. Informacje o Repozytorium Zdalnym (Git)
- **URL:** `git@github.com:qbarteczek/husqvarna-21-manuals.git`
- **Gałąź robocza:** `main`
- Wszystkie skrypty, pliki bazy danych OCR oraz zaktualizowane pliki HTML/PDF są synchronizowane za pomocą:
  ```bash
  git add .
  git commit -m "Opis zmian"
  git push origin main
  ```
