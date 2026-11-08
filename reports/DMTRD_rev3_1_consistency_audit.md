# DMTRD rev3.1 – Raport Audytu Spójności

**Data:** 2026-11-08  
**Wersja:** 3.1  
**Commit bazowy:** 7fde239 (rev3: restore canonical WCN definitions)  
**Gałąź:** research/dmtrd-rev3-canonical  

---

## 1. Wykonane poprawki

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

### 1.3. src/build_document.py (Generator dokumentu głównego)
- **Streszczenie naukowe (abstract):** Zastąpiono stare definicje kanonicznymi.
- **Wstęp (sekcja 1):** Zaktualizowano opis trzech wymiarów.
- **Sekcja 3 (Uzasadnienie trzech wymiarów):** Pełna przebudowa opisów W, C, N z kanonicznymi definicjami i wyliczeniem "co to NIE jest".
- **Sekcja 4 (Definicje konstruktów):** Przeredagowano wszystkie trzy definicje operacyjne.
- **Sekcja 8 (Charakterystyka ośmiu stanów):** Pełna przebudowa opisów wszystkich 8 stanów (000–111) zgodnie z kaninem.
- **Sekcja 9.2 (Asymetria przejść odwrotnych):** Zaktualizowano opisy procesów (np. "internalizacja" → "pojawienie się chęci", "dezautonomizacja" → "utrata chęci").
- **Sekcja 10 (Mechanizmy dynamiki):** Zaktualizowano terminologię (motywacja → chęć, możliwość → przekonanie o możliwości, obowiązek → przekonanie o konieczności).
- **Sekcja 11 (Związek stanów z działaniem):** Zaktualizowano opisy stanów.
- **Sekcja 12 (Zależność od ścieżki):** Zaktualizowano terminologię (internalizacja normy → internalizacja przekonania o konieczności).
- **Sekcja 14 (Skale pomiarowe):** Zaktualizowano uwagę o IMI.

### 1.4. src/build_reviewer_doc.py (Generator streszczenia dla recenzenta)
- **Sekcja 1 (Istota modelu):** Kanoniczne definicje W, C, N.
- **Sekcja 2 (Wyjaśnienie trzech wymiarów):** Kanoniczne pytania.
- **Sekcja 3 (Struktura ośmiu stanów):** Zaktualizowano nazwy i opisy stanów (np. "Stan neutralny" → "Spoczynek / Brak przesłanek", "Obowiązek niewykonalny" → "Tylko powinność", "Pragnienie bez możliwości" → "Tylko chęć", "Motywacja i obowiązek bez możliwości" → "Chęć + powinność (bez możliwości)", "Motywacja autonomiczna" → "Gotowość autonomiczna").
- **Sekcja 5 (Powiązania z teoriami):** Zaktualizowano terminologię ("brak motywacji" → "brak chęci").
- **Sekcja 7 (Wątpliwości):** Zaktualizowano terminologię.

### 1.5. src/validate_docx.py (Walidator DOCX)
- **check_24_transitions():** Zmieniono warunek z `found_transitions > 20` na wymóg **dokładnie 24/24**.
- **Dodano check_canonical_definitions():** Nowa walidacja wykrywająca twierdzenia pozytywne ze starymi definicjami (W = osobista akceptacja..., N = poczucie zobowiązania..., N = presja społeczna, N = emocjonalna wina) z wykluczeniem negacji ("N nie jest...").

### 1.6. research/DMTRD_charakterystyka_stanow_rev3.md
- **Stan 110:** Usunięto utożsamienie z "motywacją autonomiczną SDT" – zmieniono na "stan gotowości do działania z inicjatywy, sprawczości, potencjalnego flow".
- **Stan 110 (sytuacje adaptacyjne):** "Najwyższa jakość zaangażowania (SDT: motywacja autonomiczna)" → "Wysoka jakość zaangażowania (bliska motywacji autonomicznej SDT)".

### 1.7. Diagramy (GraphML)
- Prze-generowano pliki `DMTRD_12_krawedzi.graphml` i `DMTRD_24_przejscia.graphml` z aktualnymi danymi z CSV.

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
3. Diagram Q3: OK
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

## 5. Ocena gotowości do konsultacji psychologicznej

### Mocne strony (gotowe do prezentacji):
1. **Pełna spójność definicyjna** – jeden kanonyczny źródło (DMTRD_KANON_KONCEPCYJNY.md), wszystkie generatory zsynchronizowane.
2. **Kompletna dokumentacja** – 8 stanów, 24 przejścia, mechanizmy, zastosowania, ograniczenia.
3. **Walidacja automatyczna** – model i DOCX przechodzą wszystkie testy (0 błędów).
4. **Rzetelność naukowa** – hipotezy odrębne od ustaleń, status epistemiczny jasny, brak fikcyjnych cytowań.
5. **Praktyczna użyteczność** – schematy A-L dla stanów, 1-12 dla przejść, przykłady życiowe i zawodowe.

### Obszary wymagające uwagi recenzenta:
1. **Diagramy SVG/PNG** – wymagają ręcznej regeneracji w yEd (plik .graphml jest aktualny).
2. **Operacjonalizacja pomiarowa** – wersja ciągła (Likert) vs binarna – dokument opisuje obie, ale model bazowy do estymacji to CTMC ze stanami ciągłymi.
3. **Luka System 1 (nawyki)** – jasno oznaczona jako ograniczenie, parametr H proponowany jako rozszerzenie.
4. **Identyfikowalność statystyczna** – problem 0 df dla wersji binarnej w LTA – rozwiązane przez wersję ciągłą.

### Rekomendacja:
**Model gotowy do konsultacji psychologicznej merytorycznej.** Wszystkie elementy rdzenia (definicje, topologia, charakterystyki stanów i przejść) są spójne, kompletne i zgodne z kaninem. Dokument główny (DMTRD_koncepcja_rev3_1.docx) i streszczenie (DMTRD_streszczenie_dla_recenzenta_rev3_1.docx) stanowią samodzielne, pełne reprezentacje modelu rev3.1.

---

## 6. Pliki wyjściowe rev3.1

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

## 7. Następne kroki (opcjonalne)

1. **Regeneracja SVG/PNG** – otworzyć .graphml w yEd, ułożyć węzły, wyeksportować jako SVG/PNG.
2. **Aktualizacja README.md** – dodać informację o wersji rev3.1 i linkach do plików.
3. **Push do GitHub** – commit i push na gałąź `research/dmtrd-rev3-canonical`, aktualizacja PR #3.

---

*Raport wygenerowany automatycznie w ramach procesu weryfikacji DMTRD rev3.1.*