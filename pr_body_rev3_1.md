## DMTRD rev3.1 – Canonical Consistency and Practical Utility Gate

### Cel
Przywrócenie pełnej zgodności z kaninem koncepcyjnym autora (`model/DMTRD_KANON_KONCEPCYJNY.md`) i doprowadzenie dokumentu głównego do stanu samodzielnego (bez odsyłaczy do plików zewnętrznych).

### Główne zmiany względem rev3 (base: research/dmtrd-rev1-critical)

#### 1. Definicje kanoniczne W, C, N – przywrócone we wszystkich plikach
- **W = CHCĘ = chęć wykonania konkretnego działania** (nie: akceptacja wartości celu, nie: intencja, nie: autonomia SDT)
- **C = MOGĘ = subiektywne przekonanie o możliwości wykonania działania** (nie: obiektywna zdolność)
- **N = POWINIENEM = racjonalne przekonanie o konieczności wykonania działania ze względu na swoje cele** (nie: emocjonalna wina, nie: presja społeczna, nie: samo istnienie normy)

#### 2. Dokument główny (DMTRD_koncepcja_rev3_1.docx) – PEŁNA TREŚĆ
- **Sekcja 8:** Szczegółowe opisy wszystkich 8 stanów (kod, nazwa, dosłowne znaczenie W/C/N, charakterystyka psychologiczna, typowe zachowania, sytuacje życiowe, przykłady, źródła napięcia, sytuacje adaptacyjne/niekorzystne, granice interpretacji, przejścia).
- **Sekcja 9:** Szczegółowe opisy wszystkich 24 przejść (stan start/koniec, zmieniony wymiar, dosłowne znaczenie, definicja, przyczyny/mechanizmy, praktyczny przykład, konsekwencje, czynniki modyfikujące, granice interpretacji, literatura, hipoteza testowalna).
- **Przejścia N:1→0 (001→000, 011→010, 101→100, 111→110):** Wyjaśnione jako **ponowna racjonalna ocena zasadności działania względem własnych celów**. NIE utożsamiano z redukcją stresu, ucieczką ani uwolnieniem emocjonalnym.
- Usunięto odsyłacze do plików zewnętrznych (CSV, Markdown) jako jedynego źródła treści.

#### 3. Poprawki interpretacji psychologicznych
- **Stan 011:** Compliance = działanie bez wewnętrznej zgody. NIE automatycznie "przymus" ani "działanie pod presją" – to konfiguracja W=0, C=1, N=1.
- **Stan 101:** Napięcie krytyczne (chęć + przekonanie o konieczności bez możliwości). NIE koniecznie "najbardziej napięty" ani "wymagający natychmiastowej zmiany" – zależy od kontekstu.
- **Stan 110:** Gotowość autonomiczna, sprawczość. NIE utożsamiano z "motywacją autonomiczną SDT" – to stan binarny, SDT to teoria jakości regulacji.
- **Stan 111:** Pełna zbieżność. NIE zawsze optymalne – jakość zależy od pochodzenia N (N_source).
- **Stan 000:** Spoczynek/brak przesłanek. NIE apatia ani patologia.
- Usunięto automatyczne przypisywanie depresji, wypalenia, winy, lęku do stanów – oznaczone jako *możliwe* i *zależne od kontekstu*.

#### 4. Modele statystyczne – jasne rozróżnienie
- **RDZEŃ DMTRD:** Model binarny, 8 stanów, 24 przejścia, topologia Q3, HPE-model.
- **ROZSZERZENIA:** CTMC, HMM, LTA, wersja ciągła (oktaanty), 4. wymiar (Intencja), 5. wymiar (Działanie/Nawyk) – opcjonalne, nieobowiązkowe.
- Poprawiono stwierdzenie sugerujące, że bazowy model to CTMC ze stanami ciągłymi.
- HPE-model = topologia generatora Q (qᵢⱼ=0 dla d_H≥2). HPE-empiryczna = hipoteza testowalna w EMA.

#### 5. Walidacja i narzędzia
- `validate_docx.py`: wymóg **dokładnie 24/24** przejść, nowy test `check_canonical_definitions()` (wykrywa twierdzenia ze starymi definicjami, wyklucza negacje), weryfikacja osadzonego obrazu diagramu.
- `validate_model.py`: 0 błędów (8 stanów, 24 przejścia, d_H=1, odwrotności, GraphML, topologia Q3).
- `build_graph.py`: prze-generowane GraphML z aktualnymi danymi CSV.

### Pliki zmienione
- `AGENTS.md` – definicja W w ochronie przed dryftem
- `model/definicje.md` – definicje kanoniczne, pytania Likert
- `src/build_document.py` – pełna treść stanów i przejść w dokumencie głównym
- `src/build_reviewer_doc.py` – odniesienie do rev3.1
- `src/validate_docx.py` – 11 kryteriów (24/24 przejść, definicje kanoniczne, osadzony diagram)
- `README.md` – wersja rev3.1, zaktualizowane kryteria ukończenia
- `reports/DMTRD_rev3_1_consistency_audit.md` – raport bramy wydania (Release Gate)

### Pliki nowe (rev3.1)
- `DMTRD_koncepcja_rev3_1.docx`
- `DMTRD_streszczenie_dla_recenzenta_rev3_1.docx`
- `reports/DMTRD_rev3_1_consistency_audit.md`
- `reports/DMTRD_rev3_1_docx_validation.md`

### Status walidacji
- **Model (validate_model.py):** PASS – 0 błędów
- **DOCX główny (validate_docx.py):** PASS – 11/11 testów
- **DOCX streszczenie:** wygenerowany pomyślnie

### Nierozwiązane
- SVG/PNG diagramów – wymagają ręcznego eksportu z yEd (GraphML jest aktualny)
- Pliki historyczne (rev1, rev2, raporty recenzji) – zostawione bez zmian

---

**Gotowy do konsultacji psychologicznej merytorycznej.** Wszystkie elementy rdzenia spójne, kompletne, zgodne z kaninem. Dokumenty rev3.1 to samodzielne, pełne reprezentacje modelu.

*Uwaga: Gotowość koncepcyjna ≠ walidacja empiryczna. Teoria wymaga Etapów 2-6 (EMA, eksperymenty, rozszerzenia).*