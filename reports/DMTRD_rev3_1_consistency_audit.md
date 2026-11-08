# DMTRD rev3.1 – Raport Audytu Spójności i Brama Wydania (Release Gate)

**Data:** 2026-11-08  
**Wersja:** 3.1  
**Commit bazowy:** b08449a (rev3.1: canonical consistency fixes and practical utility gate)  
**Gałąź:** research/dmtrd-rev3-canonical  
**Pull Request:** #3 (base: research/dmtrd-rev1-critical)

---

## 1. Wykonane poprawki (Release Gate rev3.1)

### 1.1. AGENTS.md
- **Zmieniono definicję W** w sekcji "Zasady ochrony przed dryftem koncepcyjnym" z:
  - `W = CHCĘ = osobista akceptacja wartości celu / zgoda na realizację celu`
  - na: `W = CHCĘ = chęć wykonania konkretnego działania`
- Definicje C i N były już poprawne.

### 1.2. model/definicje.md
- **Sekcja 1.1 (Wymiarowe przestrzenie):** Zaktualizowano definicje kanoniczne:
  - `W ∈ {0,1} – CHCĘ (chęć wykonania konkretnego działania)`
  - `C ∈ {0,1} – MOGĘ (subiektywne przekonanie o możliwości wykonania działania)`
  - `N ∈ {0,1} – POWINIENEM (racjonalne przekonanie o konieczności wykonania działania ze względu na swoje cele)`
- **Sekcja 1.3 (Wartościowanie bitów):** Zaktualizowano tabelę interpretacji:
  - W: "Brak chęci wykonania działania" / "Chęć wykonania działania"
  - C: "Przekonanie o braku możliwości" / "Przekonanie o możliwości"
  - N: "Brak przekonania o konieczności" / "Racjonalne przekonanie o konieczności"
- **Sekcja 8.3 (Specyfikacja modelu pomiarowego):** Zaktualizowano pytania Likert:
  - W: "W jakim stopniu chcesz wykonać to działanie?"
  - N: "W jakim stopniu uważasz, że powinieneś to zrobić ze względu na swoje cele?"

### 1.3. src/build_document.py (Generator dokumentu głównego) – GŁÓWNA ZMIANA REV3.1
- **Pełna treść w dokumencie głównym:** Usunięto odsyłacze do zewnętrznych plików Markdown/CSV. Dokument główny zawiera teraz:
  - **Szczegółowe opisy wszystkich 8 stanów** (sekcja 8): kod, nazwa, dosłowne znaczenie W/C/N, charakterystyka psychologiczna, typowe możliwe zachowania, typowe sytuacje życiowe, przykłady, możliwe źródła napięcia, sytuacje adaptacyjne i niekorzystne, granice interpretacji, przejścia wychodzące/przychodzące.
  - **Szczegółowe opisy wszystkich 24 przejść** (sekcja 9): stan początkowy/końcowy, zmieniony wymiar, dosłowne znaczenie, definicja, możliwe przyczyny i mechanizmy, praktyczny przykład, możliwe konsekwencje (emocjonalne i behawioralne), czynniki modyfikujące, granice interpretacji (z szczególnym uwzględnieniem 4 przejść N:1→0), literatura i hipoteza testowalna.
- **Specyficzne przejścia N:1→0 (001→000, 011→010, 101→100, 111→110):** Wyjaśnione jako możliwe skutki **ponownej oceny racjonalnej zasadności działania względem własnych celów**. NIE utożsamiano automatycznie z redukcją stresu ani uwolnieniem emocjonalnym.
- **Streszczenie naukowe (abstract), Wstęp, Sekcje 3, 4, 10, 11, 12, 14:** Zaktualizowano terminologię na kanoniczną (motywacja → chęć, możliwość → przekonanie o możliwości, obowiązek → przekonanie o konieczności).
- **Sekcja 9.2 (Asymetria przejść):** Zaktualizowano opisy procesów na neutralne/kanoniczne.

### 1.4. src/build_reviewer_doc.py (Generator streszczenia dla recenzenta)
- Zaktualizowano odniesienie do dokumentu głównego na `DMTRD_koncepcja_rev3_1.docx`.
- Treść zgodna z kanonicznymi definicjami i nazwami stanów z rev3.1.

### 1.5. src/validate_docx.py (Walidator DOCX)
- **check_24_transitions():** Wymóg **dokładnie 24/24** (zamiast >20).
- **check_canonical_definitions():** Wykrywa twierdzenia pozytywne ze starymi definicjami z wykluczeniem negacji ("N nie jest...").
- **check_q3_diagram():** Weryfikuje obecność osadzonego obrazu, a nie tylko odwołania tekstowego.

### 1.6. research/DMTRD_charakterystyka_stanow_rev3.md
- **Stan 110:** Usunięto utożsamienie z "motywacją autonomiczną SDT" – "stan gotowości do działania z inicjatywy, sprawczości, potencjalnego flow".
- **Stan 110 (sytuacje adaptacyjne):** "Najwyższa jakość zaangażowania (SDT: motywacja autonomiczna)" → "Wysoka jakość zaangażowania (bliska motywacji autonomicznej SDT)".

### 1.7. Diagramy (GraphML)
- Prze-generowano pliki `DMTRD_12_krawedzi.graphml` i `DMTRD_24_przejscia.graphml` z aktualnymi danymi z CSV.

### 1.8. README.md
- Zaktualizowano na wersję rev3.1, zaktualizowano listę plików wyjściowych, status projektu, kryteria ukończenia.

### 1.9. Pull Request #3
- Zmieniono base branch na `research/dmtrd-rev1-critical` (prezentuje zmiany względem rev2).
- Zaktualizowano opis PR.

---

## 2. Problemy nierozwiązane

| Problem | Status | Uwagi |
|---------|--------|-------|
| SVG/PNG diagramów | **Nie zaktualizowano** | Wymaga ręcznego otwarcia .graphml w yEd i eksportu. Pliki SVG/PNG w `diagrams/` mają datę 07.11.2026 (przed zmianami). |
| Pliki historyczne (rev1, rev2) | **Zostawione bez zmian** | Zgodnie z zasadą: "Starsze dokumenty historyczne pozostaw bez zmian." |
| Raporty recenzji (ASTRA_response_matrix.md, DMTRD_rev1_change_report.md, itp.) | **Zostawione bez zmian** | To dokumenty historyczne udowadniające ewolucję modelu. |
| pr_body_rev3.md | **Zostawiony bez zmian** | Zawiera starą definicję W w opisie PR – to dokument historyczny. |

---

## 3. Wyniki testów

### 3.1. Walidacja modelu (validate_model.py)
```
STATUS: PASS
- 8 stanów: OK
- 24 przejścia: OK
- d_H = 1 dla wszystkich przejść: OK
- Przejścia odwrotne: OK
- GraphML 12 krawędzi: OK
- GraphML 24 przejścia: OK
- Topologia Q3 (NetworkX): OK (węzły=8, krawędzie=12, stopień=3, dwudzielny, średnica=3, cykle 4=6)
```

### 3.2. Walidacja DOCX (validate_docx.py) – DMTRD_koncepcja_rev3_1.docx
```
STATUS: PASS (11/11 testów)
1. Otwarcie dokumentu: OK
2. Wymagane rozdziały (20): OK
3. Diagram Q3: OK (obraz osadzony)
4. Osiem stanów: OK (8/8)
5. 24 przejścia: OK (24/24)
6. Hipotezy aktualne (HPE, HPD, HPP, E1-E24): OK
7. Brak starych błędów: OK
8. Definicje kanoniczne: OK (brak twierdzeń ze starymi definicjami)
9. Bibliografia: OK
10. Tabele poprawne: OK
11. Wersja spójna: OK
```

### 3.3. Walidacja DOCX – DMTRD_streszczenie_dla_recenzenta_rev3_1.docx
- Plik wygenerowany pomyślnie. Walidator sprawdza tylko dokument główny.

---

## 4. Zgodność z kanonem (model/DMTRD_KANON_KONCEPCYJNY.md)

| Element kanonu | Status | Uwagi |
|----------------|--------|-------|
| **Definicja W (CHCĘ = chęć wykonania działania)** | ✅ ZGODNE | Wszystkie generatory i dokumenty zaktualizowane |
| **Definicja C (MOGĘ = przekonanie o możliwości)** | ✅ ZGODNE | Wszystkie generatory i dokumenty zaktualizowane |
| **Definicja N (POWINIENEM = racjonalne przekonanie o konieczności)** | ✅ ZGODNE | Wszystkie generatory i dokumenty zaktualizowane |
| **8 stanów (kody 000–111)** | ✅ ZGODNE | CSV, generatory, charakterystyki |
| **24 przejścia (d_H = 1)** | ✅ ZGODNE | CSV, generatory, charakterystyki, GraphML |
| **Asymetria przejść odwrotnych** | ✅ ZGODNE | Opisane w dokumentach i charakterystykach |
| **HPE-model vs HPE-empiryczna** | ✅ ZGODNE | Rozróżnienie zachowane |
| **Stan ≠ zachowanie** | ✅ ZGODNE | Podkreślone w dokumentach |
| **N ≠ emocjonalna winę/presja** | ✅ ZGODNE | Wyliczone w definicjach "co to NIE jest" |
| **111 nie zawsze optymalne** | ✅ ZGODNE | Wskazane w charakterystykach stanów |
| **000 nie jest apatią** | ✅ ZGODNE | Granice interpretacji w stanie 000 |
| **101 ≠ moral distress** | ✅ ZGODNE | Hipoteza H_MD oddzielona |
| **Binarny rdzeń modelu** | ✅ ZGODNE | Rozszerzenia (ciągłe, 4. wymiar) oznaczone jako opcjonalne |
| **CTMC/LTA jako rozszerzenia** | ✅ ZGODNE | Nieobowiązkowe elementy rdzenia |

---

## 5. Kontrola dokumentu głównego (DMTRD_koncepcja_rev3_1.docx)

| Kryterium | Wynik | Szczegóły |
|-----------|-------|-----------|
| **Obecność 8 stanów** | ✅ PASS | Sekcja 8 – pełne opisy wszystkich stanów |
| **Obecność 24 przejść** | ✅ PASS | Sekcja 9 – pełne opisy wszystkich przejść |
| **Każde przejście ma: stan start/koniec, wymiar, znaczenie, przykład, mechanizm, konsekwencje, granice** | ✅ PASS | Szczegółowe opisy dla każdego z 24 przejść |
| **Przejścia 001→000, 011→010, 101→100, 111→110 jako reocena racjonalna** | ✅ PASS | Granice interpretacji jawnie to zaznaczają |
| **Brak utożsamienia N:1→0 ze stresem/uwolnieniem** | ✅ PASS | Granice: "NIE jest to automatycznie ucieczka, redukcja stresu ani uwolnienie emocjonalne" |
| **Diagram Q3 osadzony** | ✅ PASS | Rysunek 1 w sekcji 9 |
| **Definicje kanoniczne W, C, N** | ✅ PASS | Abstract, Wstęp, Sekcje 3, 4, 8, 9, 10, 11 |
| **Brak starych definicji** | ✅ PASS | Walidator: 0 znalezionych |
| **Bibliografia spójna** | ✅ PASS | 20+ pozycji z DOI |
| **Tabele poprawne** | ✅ PASS | Tabela stanów, tabela przejść, tabela hipotez głównych |

---

## 6. Kontrola streszczenia (DMTRD_streszczenie_dla_recenzenta_rev3_1.docx)

| Kryterium | Wynik |
|-----------|-------|
| Kanoniczne definicje W, C, N | ✅ PASS |
| 8 stanów z poprawnymi nazwami | ✅ PASS |
| HPE-model i HPE-empiryczna rozróżnione | ✅ PASS |
| Asymetria przejść opisana | ✅ PASS |
| 8 pytań do recenzenta | ✅ PASS |
| Odniesienie do dokumentu głównego rev3.1 | ✅ PASS |

---

## 7. Ograniczenia naukowe (nie rozwiązane w rev3.1)

1. **Binarność konstruktów** – traci wariancję (typy motywacji, gradacja self-efficacy, kategorie norm). Rozwiązanie: wersja ciągła (oktaanty) jako rozszerzenie.
2. **Brak intencji i celu** – luka teoretyczna względem TPB, Rubikon, Goal-Setting. Rozwiązanie: 4. wymiar I jako rozszerzenie.
3. **Pomijanie automatyzmu/nawyku (System 1)** – 40-50% działań. Rozwiązanie: parametr H jako rozszerzenie.
4. **N miesza kategorie normatywnych** – moralne, rolowe, społeczne, zinternalizowane, eksternalne. Rozwiązanie: rozdzielenie N na podwymiary jako rozszerzenie.
5. **Identyfikowalność statystyczna** – wersja binarna: 3 wskaźniki → 8 wzorców = saturated model (0 df) w LTA. Rozwiązanie: wersja ciągła (Likert) jako model bazowy do estymacji.
6. **HPE to hipoteza, nie fakt** – wymaga weryfikacji empirycznej (EMA).
7. **Stan 111 nie zawsze optymalny** – jakość zależy od N_source.
8. **Brak walidacji empirycznej** – model na etapie koncepcyjnym (Etap 1).

---

## 8. Gotowość do konsultacji psychologicznej

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

## 9. Pliki wyjściowe rev3.1

| Plik | Opis |
|------|------|
| `DMTRD_koncepcja_rev3_1.docx` | Główny dokument naukowy (pełna treść, nie tylko odsyłacze) |
| `DMTRD_streszczenie_dla_recenzenta_rev3_1.docx` | Streszczenie dla recenzenta |
| `model/stany.csv` | Dane 8 stanów (niezmienione, zgodne z kanonem) |
| `model/przejscia_24.csv` | Dane 24 przejść (niezmienione, zgodne z kanonem) |
| `model/definicje.md` | Formalizacja matematyczna (zaktualizowane definicje) |
| `model/DMTRD_KANON_KONCEPCYJNY.md` | Kanon koncepcyjny (źródło prawdy) |
| `diagrams/DMTRD_12_krawedzi.graphml` | Graf 12 krawędzi nieskierowanych (zaktualizowane) |
| `diagrams/DMTRD_24_przejscia.graphml` | Graf 24 przejść kierunkowych (zaktualizowane) |
| `reports/DMTRD_rev3_1_consistency_audit.md` | Niniejszy raport |
| `reports/DMTRD_rev3_1_docx_validation.md` | Raport walidacji DOCX |

---

## 10. Następne kroki

1. **Regeneracja SVG/PNG** – otworzyć .graphml w yEd, ułożyć węzły, wyeksportować jako SVG/PNG.
2. **Push do GitHub** – commit i push na gałąź `research/dmtrd-rev3-canonical`, PR #3 zaktualizowany.

---

*Raport zamknięcia (Release Gate) dla DMTRD rev3.1.*