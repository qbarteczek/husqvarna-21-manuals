# Husqvarna Viking Automatic — Klasa 21 / 21A / 21E — instrukcje i dokumentacja

Repozytorium zawiera instrukcje do szwedzkiej maszyny do szycia
**Husqvarna Viking Automatic klasa 21 / 21A / 21E** (Husqvarna Vapenfabriks AB, Huskvarna).

---

## 1. Instrukcja obsługi EN — wydanie A4 do druku 🌟

**[`Husqvarna_Automatic_21A_Operating_Manual_EN_A4.pdf`](Husqvarna_Automatic_21A_Operating_Manual_EN_A4.pdf)** — 36 stron A4.

Pełna instrukcja obsługi przepisana **ze skanu oryginału**
(`original_scans/Husqvarna_21A_Automatic_Manual_EN.pdf`) i złożona od nowa.
Wszystkie ryciny wycięto z tego samego skanu w rozdzielczości 400 dpi.

- Format **A4 pionowy, dwie kolumny**, EB Garamond 9,6 pt + Jost w nagłówkach.
- **Marginesy lustrzane** pod oprawę: wewnętrzny 24 mm, zewnętrzny 15 mm.
  Strony nieparzyste są prawe (recto), parzyste lewe (verso) — drukować dwustronnie,
  „odwracaj wzdłuż dłuższej krawędzi". 36 stron to wielokrotność 4, więc pasuje też
  do składu zeszytowego.
- Skład **wzorowany** na oryginale (zielone belki, pas rycin u dołu strony), ale nie
  odtwarza go strona w stronę.
- **Odsyłacze w tekście i spis treści przeliczone na nową paginację** — numery stron
  nie odpowiadają już wydaniu z lat 50.

### Uwaga o brakujących stronach 22–23 oryginału

W angielskim skanie brakuje barwnej rozkładówki z przykładami ściegów ozdobnych
(skan przeskakuje ze strony 21 na 24). Odtworzono ją z odpowiadających stron wydania
norweskiego (`original_scans/Husqvarna-21E_User-Manual_NO.pdf` — ta sama książka),
a norweskie podpisy zastąpiono angielskimi. W wydaniu A4 to **strona 21**.
Wszystkie pozostałe strony pochodzą wyłącznie ze skanu angielskiego.

### Jak przebudować

```bash
python scripts/detect_figures.py     # wykrywa bloki zdjęć na stronach skanu
python scripts/detect_lineart.py     # wykrywa rysunki kreskowe
python scripts/extract_figures.py    # wycina ryciny wg data/figure_map.json -> figures/
python scripts/prepare_assets.py     # skaluje je do rozdzielczości druku    -> build/img/
python scripts/build_manual_a4.py    # skleja build/parts_a4/*.html i drukuje do PDF
```

Ostatni krok drukuje przez Chrome w trybie headless. Skład edytuje się w
`build/parts_a4/` (jeden plik na partię stron), kadry rycin w `data/figure_map.json`.
Katalog `figures/` nie jest wersjonowany — odtwarza go `extract_figures.py`.

> **Po każdej zmianie sprawdź liczbę stron w PDF.** Kolumny mają stałą wysokość, nadmiar
> jest po cichu ucinany, a strona, która się przelewa, tworzy w PDF-ie dodatkową kartkę.
> Liczba stron musi równać się liczbie `<div class="page">` w `build/manual_a4.html`.

---

## 2. Instrukcja obsługi EN — wydanie A5 poziome (wierne 1:1)

[`archive/Husqvarna_Automatic_21A_Operating_Manual_EN.pdf`](archive/) — 52 strony
w **oryginalnym formacie A5 poziomym (210 × 148 mm)**, odtworzone strona w stronę,
z zachowaną paginacją oryginału. Obok wersja 2-up na A4 do druku domowego.

To ta sama, przepisana ze skanu treść co wydanie A4 — różni się tylko formatem i tym,
że trzyma się układu oryginału. Budowane przez `scripts/build_manual.py`
i `scripts/impose_a4.py`.

---

## 3. Instrukcja serwisowa PL

[`Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf`](Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf)
— polskie tłumaczenie fabrycznej instrukcji regulacyjnej
(*Service Manual for Viking Automatic home sewing machine class 21*).
Źródło HTML: [`index.html`](index.html), ilustracje w [`obrazy/`](obrazy/).

Spis treści: regulacja ściegu prostego · synchronizacja zygzaka · wysokość drążka stopki ·
centrowanie igły · pozycja środkowa zygzaka · punkt chwytania pętli · wysokość igielnicy ·
luz chwytacz–igła · wysokość ząbków transportera · synchronizacja transportu · poprzeczne
ustawienie ząbków · regulator podawania nici · naciąg sprężynki szarpacza · wymiana paska
wałka krzywkowego.

---

## 4. Materiały wcześniejsze (2026-09, archiwalne)

Pliki [`Husqvarna_Automatic_Class_21_Operating_Manual_EN.html`](Husqvarna_Automatic_Class_21_Operating_Manual_EN.html),
`Husqvarna_Automatic_Class_21_Operating_Manual_EN.pdf`,
`Husqvarna_21A_Automatic_Operating_Manual_EN_A4.pdf` oraz katalog
[`images_manual_en/`](images_manual_en/) pochodzą z wcześniejszego podejścia do tematu.

> ⚠️ **Tekst w tych plikach został zredagowany i sparafrazowany, a nie przepisany ze skanu**
> — nie jest wierną transkrypcją oryginalnej instrukcji. Część rycin wycięto ze skanu
> norweskiego i zostały w nich norweskie podpisy. Jako źródło treści służą wyłącznie
> wydania opisane w punktach 1 i 2 oraz same skany.

Zostawione dla porządku i historii prac. Dokumentacja tamtego etapu:
[`CONTINUATION_GUIDE.md`](CONTINUATION_GUIDE.md), [`RESUME_PROMPT.md`](RESUME_PROMPT.md),
[`docs/`](docs/), dane OCR w [`data/`](data/).

---

## Skany źródłowe

[`original_scans/`](original_scans/)

| Plik | Zawartość |
|---|---|
| `Husqvarna_21A_Automatic_Manual_EN.pdf` | instrukcja obsługi EN, 48 stron skanu (44 numerowane strony książki, A5 poziomo) |
| `Husqvarna-21E_User-Manual_NO.pdf` | to samo wydanie po norwesku, 56 stron |
| `Husqvarna-Class-21_Service-Manual_EN.pdf` | fabryczna instrukcja serwisowa EN |

*Opracowano na podstawie oryginalnych materiałów Husqvarna Vapenfabriks AB • Sweden.*
