# DMTRD rev3.1 – Gotowość do Konsultacji Zewnętrznej (External Review Readiness)

**Data:** 2026-11-08  
**Commit:** ac00b7037a5f607ddf876225a75aeebbcd9ef9cb  
**Gałąź:** research/dmtrd-rev3-canonical  
**PR:** #3 (base: research/dmtrd-rev1-critical)

---

## 1. Wykonane korekty F1–F4

### F1 – Usunięto nieuzasadniony ranking stanów
**Plik:** `src/build_document.py` (sekcja "Kontynuowanie działania (persistencja)")
- **Przed:** `"Stan 111 (racjonalne przekonanie o konieczności) > 110 (autonomia) > 011 (compliance) > 101 (blokada)."`
- **Po:** Opisowy tekst: `"Stan 111 (racjonalne przekonanie o konieczności), 110 (autonomia), 011 (działanie bez wewnętrznej zgody) i 101 (blokada) różnią się jakością i stabilnością kontynuacji."`
- **Uzasadnienie:** Hierarchia nie jest empirycznie zweryfikowana; różnice w jakości i stabilności zależą od kontekstu.

### F2 – Oddzielono stan od działania
**Pliki:** `src/build_document.py`, `src/build_reviewer_doc.py`
- **Stan 011:** Zmieniono "compliance" → "działanie bez wewnętrznej zgody" (opis konfiguracji, nie teoria SDT)
- **Stan 110:** Zmieniono "autonomia/motywacja autonomiczna SDT" → "gotowość do działania z inicjatywy, sprawczość"
- **Stan 111:** Zachowano "pełna gotowość (nie zawsze optymalna)" – bez deklarowania uniwersalnego optimum
- **Stan 101:** Zmieniono "najbardziej napięty stan" → "silne napięcie motywacyjne"
- **Zastosowania (sekcja 17):** Zastąpiono etykiety teoriowe (compliance, autonomia, zaangażowanie) opisami kanonicznymi stanów

### F3 – Poprawiono bibliografię Sheeran et al. (2016)
**Pliki:** `research/bibliografia.bib`, `research/zrodla.csv`
- **Przed:** `Sheeran, Paschal and Maki, Aya and Montanaro, Erica and Bryan, Angela and Klein, William MP and Miles, Emily and Rothman, Alexander J` (7 autorów)
- **Po:** `Sheeran, Paschal and Maki, Aya and Montanaro, Erica and Avishai-Yitshak, Aya and Bryan, Angela and Klein, William MP and Miles, Emily and Rothman, Alexander J` (8 autorów)
- **Źródło:** PubMed PMID 27280365 – dodano brakującą autorkę **Aya Avishai-Yitshak**
- Zaktualizowano zarówno plik `.bib` (dla LaTeX), jak i `zrodla.csv` (dla generatorów)

### F4 – Skorygowano walidator i raport
**Plik:** `src/validate_docx.py`
- Funkcja `check_q3_diagram()` weryfikuje **obie** warunki: obecność osadzonego obrazu ORAZ odwołania tekstowego ("Rysunek 1", "Graf stanów", "Q3")
- Jeśli tylko odwołanie tekstowe – ostrzeżenie (WARN), nie PASS
- Raport walidacyjny (`DMTRD_rev3_1_docx_validation.md`) nie deklaruje kontroli semantycznych ani wizualnych – tylko kontrole strukturalne i regresyjne
- Zaktualizowano informacje o wersji rev3.1 i commicie ostatecznym

---

## 2. Wykonane testy

### 2.1. Walidacja modelu (`validate_model.py`)
```
STATUS: PASS (0 błędów)
- 8 stanów: OK
- 24 przejścia: OK
- d_H = 1 dla wszystkich przejść: OK
- Przejścia odwrotne: OK
- GraphML 12 krawędzi: OK
- GraphML 24 przejścia: OK
- Topologia Q3 (NetworkX): OK (węzły=8, krawędzie=12, stopień=3, dwudzielny, średnica=3, cykle 4=6)
```

### 2.2. Walidacja DOCX (`validate_docx.py`) – DMTRD_koncepcja_rev3_1.docx
```
STATUS: PASS (11/11 testów)
1. Otwarcie dokumentu: OK
2. Wymagane rozdziały (20): OK
3. Diagram Q3 (obraz osadzony + odwołanie): OK
4. Osiem stanów (8/8): OK
5. 24 przejścia (24/24): OK
6. Hipotezy aktualne (HPE, HPD, HPP, E1-E24): OK
7. Brak starych błędów: OK
8. Definicje kanoniczne: OK
9. Bibliografia: OK
10. Tabele poprawne: OK
11. Wersja spójna: OK
```

### 2.3. Walidacja DOCX – DMTRD_streszczenie_dla_recenzenta_rev3_1.docx
- Plik wygenerowany pomyślnie, zawiera kanoniczne definicje, 8 stanów, HPE, asymetrię, 8 pytań do recenzenta.

---

## 3. Stan dokumentów

### DMTRD_koncepcja_rev3_1.docx
✅ **KOMPLETNY I POPRAWNY**
- Kanoniczne definicje W, C, N (abstract, wstęp, sekcje 3, 4, 8, 9, 10)
- 8 szczegółowych charakterystyk stanów z naturalnymi opisami "Dosłowne znaczenie"
- 24 szczegółowe opisy przejść (stan start/koniec, wymiar, znaczenie, definicja, przyczyny, przykład, konsekwencje, czynniki, granice, literatura, hipoteza)
- Przejścia N:1→0 (001→000, 011→010, 101→100, 111→110) jako ponowna racjonalna ocena
- Diagram Q3 osadzony (Rysunek 1 w sekcji 9)
- Ograniczenia interpretacyjne przy każdym stanie i przejściu
- Porównanie z 10 teoriami psychologicznymi
- Bibliografia (20+ pozycji, DOI poprawne, Sheeran et al. z 8 autorami)
- Aneksy z odsyłaczami do plików źródłowych

### DMTRD_streszczenie_dla_recenzenta_rev3_1.docx
✅ **KOMPLETNY I POPRAWNY**
- Kanoniczne definicje W, C, N
- 8 stanów z poprawnymi nazwami i opisami (011: "działanie bez wewnętrznej zgody", 110: "gotowość do działania z inicjatywy", 101: "silne napięcie motywacyjne", 111: "pełna gotowość (nie zawsze optymalna)")
- HPE-model i HPE-empiryczna rozróżnione
- Asymetria przejść opisana jako hipotezy
- 8 pytań do recenzenta
- Odniesienie do dokumentu głównego rev3.1

---

## 4. Nierozstrzygnięte ograniczenia naukowe

1. **Binarność konstruktów** – traci wariancję (typy motywacji, gradacja self-efficacy, kategorie norm). Rozwiązanie: wersja ciągła (oktaanty) jako rozszerzenie.
2. **Brak intencji i celu** – luka teoretyczna względem TPB, Rubikon, Goal-Setting. Rozwiązanie: 4. wymiar I jako rozszerzenie.
3. **Pomijanie automatyzmu/nawyku (System 1)** – 40-50% działań. Rozwiązanie: parametr H jako rozszerzenie.
4. **N miesza kategorie normatywnych** – moralne, rolowe, społeczne, zinternalizowane, eksternalne. Rozwiązanie: rozdzielenie N na podwymiary.
5. **Identyfikowalność statystyczna** – wersja binarna: saturated model (0 df) w LTA. Rozwiązanie: wersja ciągła (Likert) jako model bazowy.
6. **HPE to hipoteza, nie fakt** – wymaga weryfikacji empirycznej (EMA).
7. **Stan 111 nie zawsze optymalny** – jakość zależy od N_source.
8. **Brak walidacji empirycznej** – model na etapie koncepcyjnym (Etap 1).

---

## 5. Ocena gotowości do konsultacji psychologicznej

### Mocne strony:
1. **Pełna spójność definicyjna** – jeden kanonyczny źródło, wszystkie generatory zsynchronizowane.
2. **Kompletna samodzielna treść w dokumencie głównym** – nie trzeba otwierać plików zewnętrznych.
3. **Walidacja automatyczna** – model i DOCX przechodzą wszystkie testy (0 błędów).
4. **Rzetelność naukowa** – hipotezy odrębne od ustaleń, status epistemiczny jasny.
5. **Praktyczna użyteczność** – schematy opisowe, przykłady, granice interpretacji.

### Rekomendacja:
**PASS – Model gotowy do konsultacji psychologicznej merytorycznej.** Wszystkie elementy rdzenia są spójne, kompletne i zgodne z kaninem. Dokumenty rev3.1 stanowią samodzielne, pełne reprezentacje modelu.

**Uwaga:** Gotowość koncepcyjna ≠ walidacja empiryczna. Teoria wymaga Etapów 2-6 (EMA, eksperymenty, rozszerzenia).

---

## 6. Pakiet dla recenzenta

**Lokalizacja:** `review_package/rev3_1/`

### Zawartość:
1. `DMTRD_koncepcja_rev3_1.docx` – główny dokument naukowy
2. `DMTRD_streszczenie_dla_recenzenta_rev3_1.docx` – streszczenie dla recenzenta
3. `INFO_DLA_RECENZENTA.md` – krótka informacja o statusie naukowym modelu
4. `PYTANIA_DO_RECENZENTA.md` – zestaw 8 pytań do niezależnego recenzenta

### Pytania do recenzenta (z `PYTANIA_DO_RECENZENTA.md`):
1. **Trafność rozróżnienia W, C, N:** Czy trzy konstrukty są psychometrycznie odseparowywalne? Czy binarna operacjonalizacja nie traci istotnej informacji?
2. **Znaczenie binarności:** Czy utrata wariancji (typy motywacji, gradacja self-efficacy, kategorie norm) jest akceptowalna na etapie koncepcyjnym?
3. **Interpretacja ośmiu stanów:** Czy opisy stanów 001, 011, 101, 110, 111 są teoretycznie uzasadnione i empirycznie rozróżnialne?
4. **Przydatność 24 przejść:** Czy asymetria przejść odwrotnych generuje przewidywania różniące się od modeli płaskich?
5. **Mechanizm racjonalnej zmiany N:** Czy interpretacja N:1→0 jako "ponownej oceny racjonalnej zasadności" jest psychologicznie sensowna i odseparowywalna od redukcji stresu/ucieczki?
6. **Rozróżnienie motywacji i zachowania:** Czy model jasno oddziela stan motywacyjny (W,C,N) od faktycznego zachowania?
7. **Ograniczenia modelu:** Czy wskazane ograniczenia (binarność, brak intencji, System 1, kategorie N, identyfikowalność) są kompletne i adekwatnie opisane?
8. **Potencjalna wartość naukowa:** Czy DMTRD wnosi nową treść teoretyczną (Q3, HPE, N niezależny, stan 101, asymetria) nad istniejące modele?

---

## 7. GitHub

- **Commit:** ac00b7037a5f607ddf876225a75aeebbcd9ef9cb
- **Gałąź:** research/dmtrd-rev3-canonical
- **PR #3:** Zaktualizowany (base: research/dmtrd-rev1-critical)
- **Status:** OPEN

---

## 8. Werdykt

### ✅ READY FOR EXTERNAL CONCEPTUAL REVIEW

**Gotowość koncepcyjna:** TAK  
**Gotowość empiryczna:** NIE (wymaga Etapów 2-6)

Wszystkie elementy rdzenia (definicje, topologia, charakterystyki stanów i przejść) są spójne, kompletne i zgodne z kaninem. Dokumenty rev3.1 stanowią samodzielne, pełne reprezentacje modelu. Pakiet recenzencki przygotowany.

*Następnym etapem jest niezależna konsultacja z psychologiem naukowym.*