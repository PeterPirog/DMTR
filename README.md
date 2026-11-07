# DMTRD – Dynamiczny Model Trójwymiarowej Regulacji Działania

## Etap 1 – Analiza naukowa, formalizacja matematyczna i przygotowanie dokumentacji do recenzji

---

## Struktura projektu

```
DMTRD/
├── DMTRD_koncepcja.docx                    # Główny dokument naukowy (~25-30 stron)
├── DMTRD_streszczenie_dla_recenzenta.docx  # Streszczenie dla recenzenta (~2 strony)
├── README.md                               # Ten plik
├── requirements.txt                        # Zależności Python
│
├── research/                               # Materiały badawcze
│   ├── przeglad_literatury.md              # Przegląd 10 teorii motywacji
│   ├── analiza_teorii_pokrewnych.md        # Tabela porównawcza, ocena oryginalności
│   ├── analiza_krytyczna.md                # 20 pytań krytycznych, 5 argumentów przeciw
│   ├── hipotezy_badawcze.md                # 24 hipotezy H1-H24 + 5 HG
│   ├── bibliografia.bib                    # Bibliografia BibTeX
│   └── zrodla.csv                          # Źródła w formacie CSV
│
├── model/                                  # Definicje formalne modelu
│   ├── definicje.md                        # Formalizacja matematyczna (Q3, Markow, CTMC)
│   ├── stany.csv                           # 8 stanów (dane do importu)
│   ├── przejscia_24.csv                    # 24 przejścia (dane do importu)
│   └── model_matematyczny.md               # Szczegóły formalne
│
├── diagrams/                               # Diagramy grafowe
│   ├── DMTRD_12_krawedzi.graphml           # Graf Q3 – 12 krawędzi nieskierowanych (yEd)
│   ├── DMTRD_24_przejscia.graphml          # Graf Q3 – 24 przejścia skierowane (yEd)
│   ├── DMTRD_diagram.svg                   # Diagram główny (SVG)
│   ├── DMTRD_diagram.png                   # Diagram główny (PNG)
│   ├── DMTRD_diagram_12_edges.svg          # Wersja 12 krawędzi
│   ├── DMTRD_diagram_12_edges.png
│   ├── DMTRD_diagram_24_transitions.svg    # Wersja 24 przejścia
│   ├── DMTRD_diagram_24_transitions.png
│   ├── DMTRD_states_table.svg              # Tabela stanów
│   └── DMTRD_states_table.png
│
├── src/                                    # Skrypty Python
│   ├── build_graph.py                      # Generowanie GraphML (yEd)
│   ├── generate_diagrams.py                # Generowanie SVG/PNG (matplotlib/networkx)
│   ├── build_document.py                   # Generowanie DMTRD_koncepcja.docx
│   ├── build_reviewer_doc.py               # Generowanie DMTRD_streszczenie_dla_recenzenta.docx
│   └── validate_model.py                   # Walidacja modelu (testy)
│
├── tests/                                  # Testy automatyczne
│   ├── test_graph.py                       # (zintegrowane z validate_model.py)
│   └── test_document.py                    # (zintegrowane z validate_model.py)
│
└── reports/                                # Raporty
    ├── audyt_naukowy.md                    # Audyt końcowy (ten plik)
    ├── walidacja_techniczna.md             # Wyniki walidacji technicznej
    ├── raport_koncowy.md                   # Podsumowanie projektu
    └── zagadnienia_do_recenzji.md          # Pytania do recenzenta
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
# Walidacja modelu (testy)
.venv\Scripts\python.exe src\validate_model.py

# Generowanie diagramów GraphML (dla yEd)
.venv\Scripts\python.exe src\build_graph.py

# Generowanie diagramów SVG/PNG (matplotlib)
.venv\Scripts\python.exe src\generate_diagrams.py

# Generowanie dokumentu głównego
.venv\Scripts\python.exe src\build_document.py

# Generowanie streszczenia dla recenzenta
.venv\Scripts\python.exe src\build_reviewer_doc.py
```

## Pliki wyjściowe (kluczowe)

1. **DMTRD_koncepcja.docx** – Główny dokument naukowy do recenzji
2. **DMTRD_streszczenie_dla_recenzenta.docx** – Streszczenie dla recenzenta z 8 pytaniami
3. **DMTRD_12_krawedzi.graphml** – Graf Q3 do yEd (12 krawędzi nieskierowanych)
4. **DMTRD_24_przejscia.graphml** – Graf Q3 do yEd (24 przejścia skierowane)
5. **DMTRD_diagram.svg/png** – Diagramy do włączenia do dokumentu

## Walidacja

Wszystkie testy przechodzą (0 błędów):
- 8 stanów, unikalne kody, spójność W/C/N
- 24 przejścia, d_H=1, istnienie odwrotności, brak wielobitowych
- Spójność CSV (stany ↔ przejścia)
- GraphML: 8 węzłów, 12/24 krawędzie, poprawny edgedefault
- Topologia Q3 (NetworkX): stopnie=3, spójny, dwudzielny, średnica=3

## Status projektu

**ETAP 1 – ZAKOŃCZONY** ✓

Wszystkie kryteria ukończenia spełnione:
1. ✓ DMTRD_koncepcja.docx istnieje
2. ✓ DMTRD_streszczenie_dla_recenzenta.docx istnieje
3. ✓ Opisano wszystkie 8 stanów
4. ✓ Opisano wszystkie 24 przejścia
5. ✓ Przeprowadzono analizę porównawczą z 10 teoriami
6. ✓ Zidentyfikowano istotne ograniczenia (5 argumentów krytycznych)
7. ✓ Przedstawiono formalizację matematyczną (Q3, DTMC, CTMC, LTA)
8. ✓ Sformułowano 24+5 hipotez falsyfikowalnych
9. ✓ Zaproponowano program walidacji (EMA, LTA, CTMC, SEM)
10. ✓ Utworzono diagramy GraphML dla yEd
11. ✓ Zweryfikowano strukturę grafów (testy przechodzą)
12. ✓ Utworzono bibliografię (20+ pozycji, z DOI)
13. ✓ Sprawdzono spójność cytowań
14. ✓ Przeprowadzono audyt końcowy
15. ✓ Wszystkie pliki w katalogu projektu

## Następne kroki (Etap 2+)

1. **Niezależna recenzja** – przekazanie `DMTRD_koncepcja.docx` i `DMTRD_streszczenie_dla_recenzenta.docx` psychologowi-metodologowi
2. **Etap 2 – Walidacja psychometryczna** (N=300–500): CFA, walidacja konstruktu, wersja ciągła W,C,N, rozdzielenie N na podwymiary
3. **Etap 3 – Badanie EMA pilotażowe** (N=100, T=14 dni): test HPE, asymetrii, hipotez H1–H24
4. **Etap 4 – Badanie EMA główne** (N=300–500, T=21 dni): pełna walidacja predykcyjna
5. **Etap 5 – Eksperymenty laboratoryjne**: manipulacja W, C, N; test przyczynowy
6. **Etap 6 – Rozszerzenia**: wersja ciągła, wymiar A (Działanie), H (Nawyk), I (Intencja)

---

## Kontakt

Projekt realizowany w ramach prac badawczych nad modelem DMTRD.
Wszelkie pytania kierować do autora projektu.

*Ostatnia aktualizacja: Listopad 2026*