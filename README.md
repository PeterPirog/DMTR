# DMTRD – Dynamiczny Model Trójwymiarowej Regulacji Działania

**Wersja kanoniczna: rev3** (08.11.2026)

## Etap 1 – Analiza naukowa, formalizacja matematyczna i przygotowanie dokumentacji do recenzji

---

## Struktura projektu

```
DMTRD/
├── DMTRD_koncepcja_rev3.docx                    # Główny dokument naukowy (wersja kanoniczna)
├── DMTRD_streszczenie_dla_recenzenta_rev3.docx  # Streszczenie dla recenzenta (~2-4 strony)
├── README.md                                    # Ten plik
├── requirements.txt                             # Zależności Python
│
├── research/                                    # Materiały badawcze
│   ├── DMTRD_charakterystyka_stanow_rev3.md    # Szczegółowe opisy 8 stanów (schemat A-L)
│   ├── DMTRD_charakterystyka_przejsc_24_rev3.md # Szczegółowe opisy 24 przejść (schemat 1-12)
│   ├── DMTRD_zastosowania_praktyczne_rev3.md   # 8 przypadków analitycznych, tabela decyzyjna
│   ├── przeglad_literatury.md                  # Przegląd 10 teorii motywacji
│   ├── analiza_teorii_pokrewnych.md            # Tabela porównawcza, ocena oryginalności
│   ├── analiza_krytyczna.md                    # 20 pytań krytycznych, 5 argumentów przeciw
│   ├── hipotezy_badawcze_rev1.md               # 3 hipotezy główne (HPE, HPD, HPP) + 24 E1-E24
│   ├── bibliografia.bib                        # Bibliografia BibTeX
│   └── zrodla.csv                              # Źródła w formacie CSV
│
├── model/                                       # Definicje formalne modelu
│   ├── DMTRD_KANON_KONCEPCYJNY.md              # KANON KONCEPCYJNY – jedno źródło prawdy
│   ├── definicje.md                            # Formalizacja matematyczna (Q3, Markow, CTMC)
│   ├── stany.csv                               # 8 stanów (24 kolumny, dane do importu)
│   ├── przejscia_24.csv                        # 24 przejścia (19 kolumn, dane do importu)
│   └── model_matematyczny.md                   # Szczegóły formalne
│
├── diagrams/                                    # Diagramy grafowe
│   ├── DMTRD_12_krawedzi.graphml               # Graf Q3 – 12 krawędzi nieskierowanych (yEd)
│   ├── DMTRD_24_przejscia.graphml              # Graf Q3 – 24 przejścia skierowane (yEd)
│   ├── DMTRD_diagram.svg                       # Diagram główny (SVG)
│   ├── DMTRD_diagram.png                       # Diagram główny (PNG)
│   ├── DMTRD_diagram_12_edges.svg              # Wersja 12 krawędzi
│   ├── DMTRD_diagram_12_edges.png
│   ├── DMTRD_diagram_24_transitions.svg        # Wersja 24 przejścia
│   ├── DMTRD_diagram_24_transitions.png
│   ├── DMTRD_states_table.svg                  # Tabela stanów
│   └── DMTRD_states_table.png
│
├── src/                                         # Skrypty Python
│   ├── build_graph.py                          # Generowanie GraphML (yEd)
│   ├── generate_diagrams.py                    # Generowanie SVG/PNG (matplotlib/networkx)
│   ├── build_document.py                       # Generowanie DMTRD_koncepcja_rev3.docx
│   ├── build_reviewer_doc.py                   # Generowanie DMTRD_streszczenie_dla_recenzenta_rev3.docx
│   ├── hpe_simulation.py                       # Symulacja CTMC (naprawiony CR-01)
│   ├── validate_model.py                       # Walidacja modelu (CSV, GraphML, Q3)
│   └── validate_docx.py                        # Walidacja DOCX (10 kryteriów)
│
├── tests/                                       # Testy automatyczne
│   └── (zintegrowane z validate_model.py)
│
└── reports/                                     # Raporty
    ├── DMTRD_rev3_conceptual_restoration.md    # Raport audytu i przywracania koncepcji (ten plik)
    ├── DMTRD_rev2_docx_validation.md           # Walidacja DOCX rev2
    ├── DMTRD_rev1_final_validation.md          # Walidacja końcowa rev1
    ├── DMTRD_rev1_change_report.md             # Raport zmian rev1
    ├── github_publication_report.md            # Raport publikacji GitHub
    └── github_initialization_report.md         # Raport inicjalizacji GitHub
```

---

## Wymagania

- Python 3.12+ (testowane na 3.14)
- Zależności w `requirements.txt`

## Instalacja

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uruchamianie

```bash
# Walidacja modelu (testy CSV, GraphML, Q3 topologia)
.venv\Scripts\python.exe src\validate_model.py

# Walidacja dokumentu DOCX (10 kryteriów)
.venv\Scripts\python.exe src\validate_docx.py

# Generowanie diagramów GraphML (dla yEd)
.venv\Scripts\python.exe src\build_graph.py

# Generowanie diagramów SVG/PNG (matplotlib)
.venv\Scripts\python.exe src\generate_diagrams.py

# Generowanie dokumentu głównego (wersja kanoniczna rev3)
.venv\Scripts\python.exe src\build_document.py

# Generowanie streszczenia dla recenzenta (wersja rev3)
.venv\Scripts\python.exe src\build_reviewer_doc.py

# Test symulacji CTMC (w tym test CR-01)
.venv\Scripts\python.exe src\hpe_simulation.py
```

## Pliki wyjściowe (kluczowe – wersja rev3)

1. **DMTRD_koncepcja_rev3.docx** – Główny dokument naukowy do recenzji (wersja kanoniczna)
2. **DMTRD_streszczenie_dla_recenzenta_rev3.docx** – Streszczenie dla recenzenta z 8 pytaniami
3. **DMTRD_12_krawedzi.graphml** – Graf Q3 do yEd (12 krawędzi nieskierowanych)
4. **DMTRD_24_przejscia.graphml** – Graf Q3 do yEd (24 przejścia skierowane)
4. **DMTRD_diagram.svg/png** – Diagramy do włączenia do dokumentu

## Walidacja

Wszystkie testy przechodzą (0 błędów):
- 8 stanów, unikalne kody, spójność W/C/N
- 24 przejścia, d_H=1, istnienie odwrotności, brak wielobitowych
- Spójność CSV (stany ↔ przejścia)
- GraphML: 8 węzłów, 12/24 krawędzie, poprawny edgedefault
- Topologia Q3 (NetworkX): stopnie=3, spójny, dwudzielny, średnica=3
- DOCX rev3: 10/10 kryteriów (otwarcie, rozdziały, diagram, 8 stanów, 24 przejścia, hipotezy, brak starych błędów, bibliografia, tabele, wersja)
- Symulacja CTMC: test CR-01 przechodzi (Monte Carlo vs exp(Q*dt): różnica < 0.02)

## Status projektu

**ETAP 1 – ZAKOŃCZONY (wersja kanoniczna rev3)** ✓

Wszystkie kryteria ukończenia spełnione:
1. ✓ DMTRD_koncepcja_rev3.docx istnieje (wersja kanoniczna)
2. ✓ DMTRD_streszczenie_dla_recenzenta_rev3.docx istnieje
3. ✓ Opisano wszystkie 8 stanów (szczegółowo, schemat A-L)
4. ✓ Opisano wszystkie 24 przejścia (szczegółowo, schemat 1-12)
5. ✓ Przeprowadzono analizę porównawną z 10 teoriami
6. ✓ Zidentyfikowano istotne ograniczenia (5 argumentów krytycznych)
7. ✓ Przedstawiono formalizację matematyczną (Q3, DTMC, CTMC, LTA)
8. ✓ Sformułowano 3 hipotezy główne (HPE, HPD, HPP) + 24 eksploracyjne (E1-E24)
9. ✓ Zaproponowano program walidacji (EMA, LTA, CTMC, SEM)
10. ✓ Utworzono diagramy GraphML dla yEd
11. ✓ Zweryfikowano strukturę grafów (testy przechodzą)
12. ✓ Utworzono bibliografię (20+ pozycji, z DOI)
13. ✓ Sprawdzono spójność cytowań
14. ✓ Przeprowadzono audyt końcowy i przywrócenie koncepcji (rev3)
15. ✓ Wszystkie pliki w katalogu projektu
16. ✓ Naprawiono błąd CR-01 w symulacji CTMC (test deterministyczny przechodzi)
17. ✓ Przywrócono kanoniczne definicje W, C, N (bez utożsamień z TPB/SDT/COM-B)
18. ✓ Przywrócono binarny rdzeń modelu (8 stanów, 24 przejścia, Q3)
19. ✓ Oddzielono warstwę logiczną (kody) od psychologicznej (hipotezy mechanistyczne)
20. ✓ Usunięto utożsamienia: 101≠moral distress, 110≠działanie, 111≠optimum

## Następne kroki (Etap 2+)

1. **Niezależna recenzja** – przekazanie `DMTRD_koncepcja_rev3.docx` i `DMTRD_streszczenie_dla_recenzenta_rev3.docx` psychologowi-metodologowi (z tą recenzją i jawym wykazem ograniczeń)
2. **Etap 2 – Walidacja psychometryczna** (N=300–500): CFA, walidacja konstruktu, wersja ciągła W,C,N, rozdzielenie N na podwymiary, wywiady poznawcze
3. **Etap 3 – Badanie EMA pilotażowe** (N=100, T=14 dni): test HPE, asymetrii, hipotez E1-E24, gęstość próbkowania z symulacji
4. **Etap 4 – Badanie EMA główne** (N=300–500, T=21 dni): pełna walidacja predykcyjna, analiza path dependence
5. **Etap 5 – Eksperymenty laboratoryjne**: manipulacja W, C, N; test przyczynowy
6. **Etap 6 – Rozszerzenia**: wersja ciągła (oktaanty), wymiar A (Działanie), H (Nawyk), I (Intencja)

---

## Zasady ochrony przed dryftem koncepcyjnym (z AGENTS.md)

1. **Nie redefiniować W, C, N** bez wyraźnej decyzji autora.
2. **Nie dodawać nowych podstawowych wymiarów** do rdzenia bez uzasadnienia.
3. **Nie zastępować modelu binarnego modelem ciągłym** jako wersji bazowej.
4. **Nie przedstawiać modelu probabilistycznego jako obowiązkowego elementu DMTRD.**
5. **Nie traktować HPE jako udowodnionego prawa psychologicznego.**
6. **Nie utożsamiać stanu z faktycznym zachowaniem.**
7. **Nie utożsamiać N z emocjonalną winą lub presją.**
8. **Priorytetem są praktyczne charakterystyki stanów i przejść.**
9. **Zachowywać zgodność dokumentów, danych i diagramów.**
10. **Nie ogłaszać walidacji empirycznej bez odpowiednich badań.**

---

## Kontakt

Projekt realizowany w ramach prac badawczych nad modelem DMTRD.
Wszelkie pytania kierować do autora projektu.

*Ostatnia aktualizacja: 08.11.2026 (wersja rev3 – kanoniczna)*