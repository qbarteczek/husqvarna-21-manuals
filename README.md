# Husqvarna Viking Automatic â€” Klasa 21 / 21A / 21E â€” instrukcje i dokumentacja

Repozytorium zawiera instrukcje do szwedzkiej maszyny do szycia
**Husqvarna Viking Automatic klasa 21 / 21A / 21E** (Husqvarna Vapenfabriks AB, Huskvarna).

---

## 1. Instrukcja obsĹ‚ugi EN â€” wydanie A4 do druku đźŚź

**[`Husqvarna_Automatic_21A_Operating_Manual_EN_A4.pdf`](Husqvarna_Automatic_21A_Operating_Manual_EN_A4.pdf)** â€” 36 stron A4.

PeĹ‚na instrukcja obsĹ‚ugi przepisana **ze skanu oryginaĹ‚u**
(`original_scans/Husqvarna_21A_Automatic_Manual_EN.pdf`) i zĹ‚oĹĽona od nowa.
Wszystkie ryciny wyciÄ™to z tego samego skanu w rozdzielczoĹ›ci 400 dpi.

- Format **A4 pionowy, dwie kolumny**, EB Garamond 9,6 pt + Jost w nagĹ‚Ăłwkach.
- **Marginesy lustrzane** pod oprawÄ™: wewnÄ™trzny 24 mm, zewnÄ™trzny 15 mm.
  Strony nieparzyste sÄ… prawe (recto), parzyste lewe (verso) â€” drukowaÄ‡ dwustronnie,
  â€žodwracaj wzdĹ‚uĹĽ dĹ‚uĹĽszej krawÄ™dzi". 36 stron to wielokrotnoĹ›Ä‡ 4, wiÄ™c pasuje teĹĽ
  do skĹ‚adu zeszytowego.
- SkĹ‚ad **wzorowany** na oryginale (zielone belki, pas rycin u doĹ‚u strony), ale nie
  odtwarza go strona w stronÄ™.
- **OdsyĹ‚acze w tekĹ›cie i spis treĹ›ci przeliczone na nowÄ… paginacjÄ™** â€” numery stron
  nie odpowiadajÄ… juĹĽ wydaniu z lat 50.

### Uwaga o brakujÄ…cych stronach 22â€“23 oryginaĹ‚u

W angielskim skanie brakuje barwnej rozkĹ‚adĂłwki z przykĹ‚adami Ĺ›ciegĂłw ozdobnych
(skan przeskakuje ze strony 21 na 24). Odtworzono jÄ… z odpowiadajÄ…cych stron wydania
norweskiego (`original_scans/Husqvarna-21E_User-Manual_NO.pdf` â€” ta sama ksiÄ…ĹĽka),
a norweskie podpisy zastÄ…piono angielskimi. W wydaniu A4 to **strona 21**.
Wszystkie pozostaĹ‚e strony pochodzÄ… wyĹ‚Ä…cznie ze skanu angielskiego.

### Jak przebudowaÄ‡

```bash
python scripts/detect_figures.py     # wykrywa bloki zdjÄ™Ä‡ na stronach skanu
python scripts/detect_lineart.py     # wykrywa rysunki kreskowe
python scripts/extract_figures.py    # wycina ryciny wg data/figure_map.json -> figures/
python scripts/prepare_assets.py     # skaluje je do rozdzielczoĹ›ci druku    -> build/img/
python scripts/build_manual_a4.py    # skleja build/parts_a4/*.html i drukuje do PDF
```

Ostatni krok drukuje przez Chrome w trybie headless. SkĹ‚ad edytuje siÄ™ w
`build/parts_a4/` (jeden plik na partiÄ™ stron), kadry rycin w `data/figure_map.json`
(wspĂłĹ‚rzÄ™dne w pikselach strony skanu przy 150 dpi, po obrĂłceniu do poziomu).
Katalog `figures/` nie jest wersjonowany â€” odtwarza go `extract_figures.py`.

> **Po kaĹĽdej zmianie sprawdĹş liczbÄ™ stron w PDF.** Kolumny majÄ… staĹ‚Ä… wysokoĹ›Ä‡, nadmiar
> jest po cichu ucinany, a strona, ktĂłra siÄ™ przelewa, tworzy w PDF-ie dodatkowÄ… kartkÄ™.
> Liczba stron musi rĂłwnaÄ‡ siÄ™ liczbie `<div class="page">` w `build/manual_a4.html`.

---

## 2. Instrukcja obsĹ‚ugi EN â€” wydanie A5 poziome (wierne 1:1)

[`archive/Husqvarna_Automatic_21A_Operating_Manual_EN.pdf`](archive/) â€” 52 strony
w **oryginalnym formacie A5 poziomym (210 Ă— 148 mm)**, odtworzone strona w stronÄ™,
z zachowanÄ… paginacjÄ… oryginaĹ‚u. Obok wersja 2-up na A4 do druku domowego
(przeciÄ…Ä‡ wzdĹ‚uĹĽ Ĺ›rodka, zszyÄ‡ przy lewej krawÄ™dzi).

To ta sama, przepisana ze skanu treĹ›Ä‡ co wydanie A4 â€” rĂłĹĽni siÄ™ tylko formatem i tym,
ĹĽe trzyma siÄ™ ukĹ‚adu oryginaĹ‚u. Budowane przez `scripts/build_manual.py`
(ĹşrĂłdĹ‚o w `build/parts/`, ktĂłrego tu nie ma â€” do odtworzenia z historii) oraz
`scripts/impose_a4.py`.

---

## 3. Instrukcja serwisowa PL

[`Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf`](Husqvarna_Class_21_Instrukcja_Serwisowa_PL.pdf)
â€” polskie tĹ‚umaczenie fabrycznej instrukcji regulacyjnej
(*Service Manual for Viking Automatic home sewing machine class 21*).
ĹąrĂłdĹ‚o HTML: [`index.html`](index.html), ilustracje w [`obrazy/`](obrazy/).

Spis treĹ›ci: regulacja Ĺ›ciegu prostego Â· synchronizacja zygzaka Â· wysokoĹ›Ä‡ drÄ…ĹĽka stopki Â·
centrowanie igĹ‚y Â· pozycja Ĺ›rodkowa zygzaka Â· punkt chwytania pÄ™tli Â· wysokoĹ›Ä‡ igielnicy Â·
luz chwytaczâ€“igĹ‚a Â· wysokoĹ›Ä‡ zÄ…bkĂłw transportera Â· synchronizacja transportu Â· poprzeczne
ustawienie zÄ…bkĂłw Â· regulator podawania nici Â· naciÄ…g sprÄ™ĹĽynki szarpacza Â· wymiana paska
waĹ‚ka krzywkowego.

---

## 4. `legacy/` â€” wczeĹ›niejsze podejĹ›cie (wrzesieĹ„ 2026)

[`legacy/`](legacy/) zawiera dokumentacjÄ™ pierwszego podejĹ›cia do tematu: ĹşrĂłdĹ‚owy HTML
56-stronicowej broszury, notatki projektowe i dane OCR pobrane z archive.org.

> âš ď¸Ź **Tekst tamtej wersji zostaĹ‚ zredagowany i sparafrazowany, a nie przepisany ze skanu**
> â€” nie jest wiernÄ… transkrypcjÄ… oryginalnej instrukcji. CzÄ™Ĺ›Ä‡ rycin wyciÄ™to ze skanu
> norweskiego i zostaĹ‚y w nich norweskie podpisy. Jako ĹşrĂłdĹ‚o treĹ›ci sĹ‚uĹĽÄ… wyĹ‚Ä…cznie
> wydania opisane w punktach 1 i 2 oraz same skany.
>
> Warstwa OCR w `legacy/data/` jest praktycznie bezuĹĽyteczna: strony w skanie sÄ… obrĂłcone
> o 90Â°, wiÄ™c rozpoznany tekst to w wiÄ™kszoĹ›ci Ĺ›mieci. TreĹ›Ä‡ wydaĹ„ 1 i 2 przepisano
> ze zrenderowanych stron, nie z OCR.

Wygenerowane wtedy PDF-y i katalog `images_manual_en/` usuniÄ™to przy odchudzaniu
repozytorium â€” sÄ… odtwarzalne ze skanĂłw.

---

## Skany ĹşrĂłdĹ‚owe

[`original_scans/`](original_scans/)

| Plik | ZawartoĹ›Ä‡ |
|---|---|
| `Husqvarna_21A_Automatic_Manual_EN.pdf` | instrukcja obsĹ‚ugi EN, 48 stron skanu (44 numerowane strony ksiÄ…ĹĽki, A5 poziomo) â€” ĹşrĂłdĹ‚o wydaĹ„ 1 i 2 |
| `Husqvarna-21E_User-Manual_NO.pdf` | to samo wydanie po norwesku, 56 stron â€” ĹşrĂłdĹ‚o brakujÄ…cych stron 22â€“23 |
| `Husqvarna-Class-21_Service-Manual_EN.pdf` | fabryczna instrukcja serwisowa EN â€” ĹşrĂłdĹ‚o tĹ‚umaczenia PL |

Wszystkie trzy sÄ… wejĹ›ciem do przebudowy, dlatego zostajÄ… w repozytorium.

*Opracowano na podstawie oryginalnych materiaĹ‚Ăłw Husqvarna Vapenfabriks AB â€˘ Sweden.*

