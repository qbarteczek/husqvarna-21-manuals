# 🚀 Prompt do Wznowienia Prac na Nowej Maszynie

Skopiuj i wklej poniższy tekst do okna czatu asystenta AI (Antigravity / Gemini) na nowym komputerze po sklonowaniu repozytorium:

---

```text
Kontynuujemy projekt cyfrowej rekonstrukcji podręcznika użytkownika maszyny do szycia Husqvarna Viking Automatic Klasa 21 / 21A / 21E.

Wszystkie dotychczasowe analizy, skrypty, oryginalne skany i baza danych OCR znajdują się w tym repozytorium.
Zapoznaj się z plikami:
1. CONTINUATION_GUIDE.md
2. docs/implementation_plan.md
3. docs/walkthrough.md

Aktualny stan projektu:
- Wygenerowano 56-stronicowy szablon HTML i plik PDF w oryginalnym formacie poziomej broszury A5 (size: 210mm 148mm;): `Husqvarna_Automatic_Class_21_Operating_Manual_EN.html` oraz `.pdf`.
- W katalogu `original_scans/` umieszczono kompletne skany źródłowe:
  * `Husqvarna_21A_Automatic_Manual_EN.pdf` (czysty tekst angielski i angielskie ryciny techniczne)
  * `Husqvarna-21E_User-Manual_NO.pdf` (oryginalna pozioma geometria broszury 56 stron)
  * `Husqvarna-Class-21_Service-Manual_EN.pdf` (instrukcja serwisowa)
- W katalogu `data/` znajduje się pełny OCR tekstu angielskiego (`en_full_ocr.json`, `Husqvarna_21A_djvu.xml`).
- W katalogu `scripts/` znajduje się generator `build_full_manual.py` i narzędzia kadrujące.

Zadania do zrealizowania zgodnie z uwagami użytkownika:
1. W rycinach znajdujących się w `images_manual_en/` (wyciętych z norweskiego skanu) znajdują się fragmenty tekstów w języku norweskim (np. Fig. 26/26a dotyczące dziurek, opisy przy wzornikach ściegów krzywek itp.). Należy te teksty wyczyścić z obrazów lub zastąpić odpowiednikami wykadrowanymi bezpośrednio z angielskiego skanu `original_scans/Husqvarna_21A_Automatic_Manual_EN.pdf`. Obrazy mają zawierać wyłącznie elementy graficzne/oznaczenia, bez obcego tekstu.
2. Skład tekstu i rozmieszczenie zdjęć ma w 100% odpowiadać oryginalnej fabrycznej książeczce (układ kolumn, proporcje, podpisy rycin).
3. Przeprowadź gruntowne sprawdzenie pisowni (spellcheck) i terminologii w całym tekście podręcznika.
4. Zrekompiluj plik PDF (poleceniem chromium --headless --no-sandbox --disable-gpu --print-to-pdf="Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf" Husqvarna_Automatic_Class_21_Operating_Manual_EN.html), zweryfikuj podgląd stron i zsynchronizuj repozytorium git.
```

---

## 🛠️ Kroki przygotowawcze na nowej maszynie:
1. **Sklonowanie repozytorium:**
   ```bash
   git clone git@github.com:qbarteczek/husqvarna-21-manuals.git
   cd husqvarna-21-manuals
   ```
2. **Instalacja zależności (jeśli potrzebne):**
   ```bash
   pip install Pillow
   sudo apt install -y poppler-utils chromium-browser  # lub google-chrome
   ```
3. Wklejenie powyższego promptu do asystenta.
