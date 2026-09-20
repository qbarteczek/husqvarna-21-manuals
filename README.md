# Husqvarna Viking Automatic - Klasa 21 / 21A / 21E - Instrukcje i Dokumentacja

Repozytorium zawiera zrekonstruowane, przetłumaczone i zoptymalizowane instrukcje serwisowe oraz obsługi do legendarnej szwedzkiej maszyny do szycia **Husqvarna Viking Automatic Klasa 21 / 21A / 21E**.

---

## 📄 Dostępne dokumenty

### 1. Operating Manual / Instrukcja Obsługi (Język Angielski, Format Broszury 56 stron A5 Poziomo) 🌟
- **Plik PDF:** [Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf](Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf)
- **Wersja źródłowa HTML:** [Husqvarna_Automatic_Class_21_Operating_Manual_EN.html](Husqvarna_Automatic_Class_21_Operating_Manual_EN.html)
- **Katalog ilustracji:** [images_manual_en/](images_manual_en/)
- **Opis:** Wierne odtworzenie 1:1 oryginalnej fabrycznej książeczki Husqvarna Viking (*Operating Manual for Viking Automatic home sewing machine class 21*) w układzie **poziomej broszury A5 (56 stron)**. 
  - Pełny, edytowalny i przeszukiwalny tekst (ponad 8200 słów) pozbawiony zanieczyszczeń skanu i odręcznych dopisków.
  - Elegancki skład typograficzny oparty na oryginalnych proporcjach i czcionkach szwedzkiego wydania.
  - Ponad 60 starannie wykadrowanych i oczyszczonych rycin instruktażowych (m.in. nawlekanie nici, szpulka, dobór igieł, stopki, wzorniki krzywek automatycznych A, B, C, D, obszywanie dziurek, konserwacja).
  - Pełne, dwustronicowe rozkładówki schematów maszyny (**Fig. 1 – Front View** oraz **Fig. 2 – Rear View**) z czytelnymi angielskimi oznaczeniami podzespołów (klucz numeryczny 1–40).

---

### 2. Instrukcja Serwisowa (Język Polski)
- **Plik PDF:** [Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf](Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf)
- **Wersja źródłowa HTML:** [index.html](index.html)
- **Katalog ilustracji:** [obrazy/](obrazy/)
- **Oryginał:** Opracowano na podstawie fabrycznej instrukcji regulacyjnej *Service Manual for Viking Automatic home sewing machine class 21*.

#### Spis treści instrukcji serwisowej:
1. Regulacja maszyny do ściegu prostego
2. Ustawienie momentu wychylenia igły (synchronizacja zygzaka)
3. Ustawienie wysokości drążka stopki dociskowej
4. Centrowanie igły w otworze płytki ściegowej
5. Ustawienie pozycji środkowej dla ściegu zygzakowego
6. Regulacja styczna chwytacza (punkt chwytania pętli)
7. Ustawienie wysokości igielnicy
8. Ustawienie odstępu (luzu) między chwytaczem a igłą
9. Ustawienie wysokości ząbków transportera
10. Synchronizacja transportu
11. Poprzeczne ustawienie ząbków transportera
12. Ustawienie regulatora podawania nici
13. Ustawienie naciągu sprężynki szarpacza nici
14. Wymiana paska napędowego wałka krzywkowego

---

### 3. Wersja pomocnicza A4 (Język Angielski, Format Pionowy A4)
- **Plik PDF:** [Husqvarna_21A_Automatic_Operating_Manual_EN_A4.pdf](Husqvarna_21A_Automatic_Operating_Manual_EN_A4.pdf)
- **Opis:** 48-stronicowy podręcznik użytkownika zorientowany w standardowym pionowym formacie A4 (do szybkiego podglądu na tradycyjnych drukarkach pionowych).

---

## 🛠️ Generowanie dokumentów

- **Instrukcja Obsługi EN (56 stron, broszura A5 landscape):**
  Wygenerowana ze zoptymalizowanego szablonu HTML o geometrii `@page { size: 210mm 148mm; margin: 0; }`:
  ```bash
  chromium --headless --no-sandbox --disable-gpu --print-to-pdf="Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf" Husqvarna_Automatic_Class_21_Operating_Manual_EN.html
  ```
- **Instrukcja Serwisowa PL (pionowy format A4):**
  ```bash
  chromium --headless --no-sandbox --disable-gpu --print-to-pdf="Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf" index.html
  ```

---

*Opracowano na podstawie oryginalnych materiałów technicznych Husqvarna Vapenfabriks AB • Sweden.*
