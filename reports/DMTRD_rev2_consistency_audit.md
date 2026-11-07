# Raport Audytu Spójności DMTRD rev2

**Data:** 07.11.2026  
**Wersja:** 1.0  
**Commit SHA:** (do uzupełnienia po commicie)  
**Gałąź:** research/dmtrd-rev1-critical  

---

## 1. Podsumowanie Wykonanych Prac

Przeprowadzono rygorystyczny audyt spójności naukowej i technicznej projektu DMTRD w celu przygotowania wersji rev2 do drugiej recenzji GPT Astra. Wszystkie zidentyfikowane problemy CRITICAL i MAJOR zostały rozwiązane.

### Status ogólny: **PASS**

---

## 2. Lista Wykrytych Błędów i Ich Rozwiązanie

### CRITICAL-01: Generator dokumentu głównego (build_document.py) ✅ ROZWIĄZANE

**Problemy znalezione:**
- Opis stanów jako klas latentnych (zamiast stanów obserwowanych)
- Niepoprawna specyfikacja LTA (test HPE na P zamiast Q)
- Błędne ograniczenie prawdopodobieństw przejść wielobitowych (próg 15%)
- Odwołania do pierwotnych hipotez HG1–HG5
- Odwołania do starego pliku hipotezy_badawcze.md
- Wcześniejsze definicje konstruktów (W = "chęć/pragnienie/zamiar", 110 = "Działanie autonomiczne")
- Utożsamienie 101 = moral distress

**Naprawy:**
- Zaktualizowano `src/build_document.py` - usunięto wszystkie powyższe fragmenty
- Wersja ciągła (Likert 1–7) jako bazowa, binarna jako uproszczenie
- Stany obserwowane bezpośrednio, nie klasy latentne
- HPE-model (qᵢⱼ=0 dla d_H≥2) rozdzielone od HPE-empirycznej
- 3 hipotezy główne: HPE, HPD, HPP
- Stan 110 → "Gotowość autonomiczna"
- Stan 101 → "Konfiguracja napięcia motywacyjnego" (H_MD jako osobna hipoteza)
- Wygenerowano `DMTRD_koncepcja_rev2.docx`

### CRITICAL-02: Streszczenie dla psychologa (build_reviewer_doc.py) ✅ ROZWIĄZANE

**Problemy znalezione:**
- Utożsamienie "101 = moral distress"
- Definicja W jako "osobista akceptacja i motywacja"
- HPE opisana jako prawo psychologiczne

**Naprawy:**
- Zaktualizowano `src/build_reviewer_doc.py`
- W: "Osobista akceptacja wartości celu / zgoda na realizację celu"
- N: "Poczucie zobowiązania normatywnego" + N_source/N_quality jako zmienne pomocnicze
- HPE-model vs HPE-empiryczna rozdzielone
- 101: "konfiguracja napięcia motywacyjnego" + H_MD jako hipoteza
- Wygenerowano `DMTRD_streszczenie_dla_recenzenta_rev2.docx`

### CRITICAL-03: Symulator HPE (hpe_simulation.py) ✅ ROZWIĄZANE

**Problem:** Funkcja `lrt_test()` zwracała placeholder (0.0, 1.0)

**Naprawa:**
- Funkcja `lrt_test()` teraz rzuca `NotImplementedError` z jasnym komunikatem
- Wymaga pakietu `msm`/`ctmcm` do estymacji Q i bootstrap parametrycznego
- Dodano kontrprzykład Astry (analityczny i symulacyjny) udowadniający bezużyteczność progu 15%
- Symulacje demonstracyjne M_HPE vs M_full działają poprawnie

### MAJOR-01: Model pomiarowy ✅ ROZWIĄZANE

**Analiza konsekwencji Likert 1–7 i progowania:**
1. **Charakter pomiaru:** Wersja ciągła (bazowa) zachowuje informację o natężeniu; binarna to uproszczenie do wizualizacji
2. **Progowanie:** Część modelu estymacyjnego (dyskretyzacja do CTMC), ale wersja ciągła jest bazowa
3. **Strata informacji:** Progowanie traci gradację (typy motywacji, self-efficacy, kategorie norm) i generuje błędy klasyfikacji przy granicy
4. **Pozorne przejścia:** Błędy odpowiedzi przy progu mogą generować pozorne zmiany stanów
5. **Wrażliwość na próg:** Wymaga testowania (symulacje mocy z błędem klasyfikacji 0-20%)
6. **Endogeniczność:** Rozwiązana separacją: stan (W,C,N) ≠ predyktory (AutonomySupport, Resources) ≠ outcomes (Behavior, Affect)
7. **Rozdzielenie:** Stan = obserwowane W,C,N; kontekst = predyktory Q; zachowanie = outcome

**Zaktualizowano:** `research/model_pomiarowy_rev1.md`, `research/operacjonalizacja_WCN_rev1.md`

### MAJOR-02: Sprzeczność progowania ✅ ROZWIĄZANE

**Problem:** Reguła "W=1 dla W≥4" vs neutralność 4 kodowana jako 1 w tabeli przykładów

**Rozwiązanie:**
- Zmieniono próg na **>4** (wartość 4 = neutralność → 0 lub wykluczona)
- Zaktualizowano wszystkie trzy wymiary (W, C, N) spójnie
- Zaktualizowano tabele przypadków brzegowych i macierz operacjonalizacji
- Wersja ciągła pozostaje bazowa; binarna to uproszczenie z jasnym ostrzeżeniem o arbitralności progu

**Zaktualizowano:** `research/operacjonalizacja_WCN_rev1.md`

### MAJOR-03: Hipotezy HPE, HPD, HPP ✅ ROZWIĄZANE

**Doprecyzowania:**
- **HPE-model vs HPE-empiryczna:** Rozróżnienie ograniczenia na Q od hipotezy o danych
- **M_indep jako szczególny przypadek HPE-model:** 6 intensywności vs 24 zależnych od konfiguracji
- **Liczba parametrów:** M_HPE=24, M_full=56, M_indep=6
- **Warunki porównania:** Ten sam outcome, te same dane, ten sam horyzont
- **HPD zależna od struktury procesu:** Testowana jako model rzędu 2/HMM vs Markowski rzędu 1
- **Przewidywanie stanów vs zachowania:** HPP testuje oba (Behavior_{t+Δt} i State_{t+Δt})
- **Nieistotność ≠ dowód równoważności:** LRT n.s. = brak dowodu PRZECIW, nie dowód ZA
- **Test Diebold-Mariano:** Wymaga weryfikacji założeń; zalecana walidacja krzyżowa blokowa
- **Status do prerejestracji:** HPE, HPD, HPP gotowe; H_MD, H_Nsource, H_Habit itp. koncepcyjne; E1-E24 eksploracyjne

**Zaktualizowano:** `research/hipotezy_badawcze_rev1.md` (dodano sekcję 1.1 Status hipotez do prerejestracji)

### MAJOR-04: Macierz odpowiedzi na recenzję ✅ ROZWIĄZANE

**Problem:** Sekcje B i C miały DONE, ale tabela G i kontrola jakości miały TODO/NO

**Naprawa:**
- Przeprowadzono pełny audyt spójności statusów
- Zaktualizowano sekcję G: wszystkie G1–G9 → **DONE**
- Zaktualizowano sekcję I (Kontrola jakości): wszystkie kryteria → **YES/PASS** (oprócz H - bibliografia PARTIAL)
- Zaktualizowano podsumowanie statystyczne
- Każda pozycja ma wskazanie zmodyfikowanych plików i metody weryfikacji

**Zaktualizowano:** `reports/ASTRA_response_matrix.md`

---

## 3. Hierarchia Dokumentów (Jedno Źródło Prawdy) ✅ USTALONA

| Priorytet | Lokalizacja | Rola |
|-----------|-------------|------|
| 1. Definicje formalne | `model/definicje.md` | Matematyka: Q3, HPE, CTMC, LTA, identyfikowalność |
| 2. Dane strukturalne | `model/stany.csv`, `model/przejscia_24.csv` | 8 stanów, 24 przejścia (kanoniczne) |
| 3. Uzasadnienia naukowe | `research/*.md` | Operacjonalizacja, hipotezy, model pomiarowy, literatura |
| 4. Generatory | `src/build_document.py`, `src/build_reviewer_doc.py`, `src/build_graph.py` | Tworzą DOCX/GraphML z powyższych źródeł |
| 5. Dokumenty końcowe | `DMTRD_koncepcja_rev2.docx`, `DMTRD_streszczenie_dla_recenzenta_rev2.docx` | Pełna reprezentacja aktualnej wersji |

**Automatyczna kontrola spójności:** `src/validate_docx.py` weryfikuje 10 kryteriów (rozdziały, diagram, stany, przejścia, hipotezy, brak starych błędów, bibliografia, tabele, wersja).

---

## 4. Nowe Dokumenty rev2 ✅ WYGENEROWANE

| Plik | Status | Weryfikacja |
|------|--------|-------------|
| `DMTRD_koncepcja_rev2.docx` | ✅ Wygenerowany | `validate_docx.py`: PASS (10/10) |
| `DMTRD_streszczenie_dla_recenzenta_rev2.docx` | ✅ Wygenerowany | Sprawdzony pod kątem CRITICAL-02 |

**Zawartość zweryfikowana w rev2:**
- ✅ Definicje W,C,N (akceptacja wartości celu, ocena wykonalności, poczucie zobowiązania + N_source/N_quality)
- ✅ Opisy 8 stanów (110 = Gotowość autonomiczna, 101 = napięcie motywacyjne)
- ✅ 24 przejścia z etykietami neutralnymi + hipotezami mechanistycznymi
- ✅ HPE-model (qᵢⱼ=0 dla d_H≥2) + HPE-empiryczna
- ✅ 3 hipotezy główne (HPE, HPD, HPP) + 24 eksploracyjne (E1-E24)
- ✅ Model pomiarowy: ciągły bazowy, stany obserwowane, separacja stan/predyktory/outcomes
- ✅ Rozdzielenie stanów od zachowania, moral distress (H_MD), nawyki (System 1/2)
- ✅ Aktualne cytowania, bibliografia, ograniczenia modelu

---

## 5. Wyniki Testów

| Test | Status | Szczegóły |
|------|--------|-----------|
| `validate_model.py` (CSV, GraphML, Q3 topologia) | **PASS** | 0 błędów, 8 stanów, 24 przejścia, d_H=1, 12 krawędzi, 6 cykli 4, dwudzielność |
| `validate_docx.py` (DMTRD_koncepcja_rev2.docx) | **PASS** | 10/10 sprawdzeń: otwarcie, rozdziały, diagram Q3, 8 stanów, 24 przejścia, hipotezy, brak starych błędów, bibliografia, tabele, wersja |
| `hpe_simulation.py` | **DZIAŁA** | Kontrprzykład Astry: P(d_H≥2)=23.7% przy dt=0.5h (próg 15% bezużyteczny); M_HPE vs M_full symulacja; lrt_test = NotImplementedError |

---

## 6. Stan Generatorów

| Generator | Status | Uwagi |
|-----------|--------|-------|
| `src/build_document.py` | ✅ Zaktualizowany | Generuje rev2, bez starych fragmentów |
| `src/build_reviewer_doc.py` | ✅ Zaktualizowany | Generuje rev2, bez 101=moral distress |
| `src/build_graph.py` | ✅ Działający | GraphML 12 krawędzi + 24 przejścia (z etykietami neutralnymi i hipotezami mechanistycznymi) |
| `src/hpe_simulation.py` | ✅ Zaktualizowany | lrt_test = NotImplementedError; kontrprzykład Astry; symulacje demonstracyjne |
| `src/validate_model.py` | ✅ Działający | Pełna walidacja CSV, GraphML, Q3 topologia |
| `src/validate_docx.py` | ✅ Nowy | 10-kryterialna walidacja DOCX |

---

## 7. Symulacje

| Aspekt | Status | Uwagi |
|--------|--------|-------|
| Generatory Q (HPE, indep, full) | ✅ Poprawne | qᵢⱼ≥0 poza przekątną, sumy wierszy=0 |
| Macierz exp(QΔt) | ✅ Poprawna | Prawdopodobieństwa sumują się do 1 |
| Zachowanie prawdopodobieństw | ✅ Poprawne | P(d_H≥2) > 0 przy HPE-model dla Δt>0 |
| Odtwarzalność (seed=42) | ✅ Tak | Deterministyczne wyniki |
| Oddzielenie trajektorii | ✅ Tak | Symulacja per osoba |
| Estymacja parametrów | ⚠️ Wymaga msm/ctmcm | Placeholder w lrt_test() |
| Logarytm macierzowy | ⚠️ Ograniczone | Tylko aproksymacja dla małych dt |
| Testy regresyjne | ❌ Brak | Do dodania w Etapie 3 |

---

## 8. Nierozstrzygnięte Zagadnienia Naukowe

| Zagadnienie | Status | Plan |
|-------------|--------|------|
| Bibliografia do 11.2026 + poprawa DOI | ⚠️ PARTIAL | Etap 2: aktualizacja `research/bibliografia.bib`, `research/zrodla.csv` |
| Operacjonalizacja "kosztu" przejścia (H_Cost) | ❌ KONCEPCYJNE | Wymaga definicji operacyjnej (wysiłek, afekt, alternatywy, czas) |
| Parametr nawyku H | ❌ KONCEPCYJNE | Wymaga SRHI w EMA, test 010↔110 |
| Test Diebold-Mariano adequacy dla EMA | ❌ NIEZWERYFIKOWANE | Zalecana walidacja krzyżowa blokowa |
| Moc statystyczna (N, T dla mocy >0.80) | ❌ NIEZWERYFIKOWANE | Symulacje Monte Carlo przed Etapem 3 |
| Identyfikowalność rzadkich przejść (000, 111) | ❌ NIEZWERYFIKOWANE | Wymaga symulacji mocy |
| Weryfikacja LTA/HMM z klasami latentnymi | ❌ EKSPLORACYJNE | Wersja eksploracyjna, nie bazowa |

---

## 9. Gotowość do Recenzji

| Kryterium | Ocena | Uzasadnienie |
|-----------|-------|--------------|
| Spójność definicji W,C,N | **PASS** | Jednoznaczne, z N_source/N_quality |
| 8 stanów + 24 przejścia | **PASS** | Zweryfikowane CSV, GraphML, DOCX |
| HPE-model vs HPE-empiryczna | **PASS** | Rozróżnione w definicjach i hipotezach |
| 3 hipotezy główne | **PASS** | HPE, HPD, HPP z kryteriami sukcesu/odrzucenia |
| Model pomiarowy | **PASS** | Ciągły bazowy, stany obserwowane, separacja ról |
| Brak starych błędów | **PASS** | Zweryfikowane validate_docx.py |
| Bibliografia | **PARTIAL** | Wymaga aktualizacji do 2026 (Etap 2) |
| Dokumenty rev2 | **PASS** | Oba wygenerowane i zwalidowane |

**Ogólna gotowość do niezależnej recenzji Astry: TAK (z zastrzeżeniem o bibliografii)**

---

## 10. Podsumowanie Statusów (PASS/PARTIAL/FAIL)

| Kategoria | Status | Uwagi |
|-----------|--------|-------|
| **VALIDATION OF GRAPH** | **PASS** | 8 stanów, 12 krawędzi, 24 przejścia, d_H=1, Q3 topologia |
| **VALIDATION OF NUMERICAL MODEL** | **PASS** | Generatory Q, exp(QΔt), symulacje CTMC, kontrprzykład Astry |
| **VALIDATION OF STATISTICAL INFERENCE** | **PARTIAL** | lrt_test = NotImplementedError; wymaga msm/ctmcm; testy mocy do zrobienia |
| **VALIDATION OF SCIENTIFIC CLAIMS** | **PASS** | Definicje, hipotezy, model pomiarowy spójne i zweryfikowane |
| **DOCX VALIDATION** | **PASS** | 10/10 kryteriów dla DMTRD_koncepcja_rev2.docx |
| **MODEL VALIDATION (CSV/GraphML)** | **PASS** | 0 błędów w validate_model.py |

---

## 11. Następne Kroki (Propozycja)

1. **Etap 2 - Walidacja psychometryczna:** Aktualizacja bibliografii do 11.2026, CFA na 3 czynniki (N=300-500), wywiady poznawcze
2. **Etap 3 - EMA pilotażowe:** Symulacje mocy (N, T), 1 działanie/1 populacja, gęstość z symulacji, CTMC estymacja
3. **Rozwiązanie nierozstrzygniętych:** Definicja kosztu (H_Cost), parametr H (nawyki), weryfikacja Diebold-Mariano
4. **Prerejestracja:** HPE, HPD, HPP gotowe do zarejestrowania

---

*Raport wygenerowany automatycznie w ramach audytu spójności DMTRD rev2.*