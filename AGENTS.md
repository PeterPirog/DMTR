# AGENTS.md – Instrukcje dla agentów OpenCode (DMTRD)

## Katalog roboczy
`D:\Opencode_Projects\projects\DMTRD`

## Źródła prawdy dla danych modelu
- `model/stany.csv` – definicje 8 stanów (kod, W, C, N, opisy, przejścia)
- `model/przejscia_24.csv` – 24 przejścia kierunkowe z pełną charakterystyką
- `model/definicje.md` – formalizacja matematyczna (Q3, HPE, DTMC, CTMC, LTA)

## Zasady spójności modelu
1. **Osiem stanów**: kody 000–111, każdy ma unikalny kod 3-bitowy zgodny z W,C,N
2. **12 par sąsiedztwa**: każda para stanów o odległości Hamminga d_H = 1
3. **24 przejścia kierunkowe**: każda krawędź nieskierowana = 2 przejścia odwrotne
4. **HPE (Hipoteza Przejść Elementarnych)**: każde dozwolone przejście ma d_H = 1
5. **Asymetria**: przejścia odwrotne (np. 011→111 vs 111→011) to odrębne procesy psychologiczne

## Aktualizacja diagramów GraphML
- Uruchom: `.venv\Scripts\python.exe src\build_graph.py`
- Pliki wyjściowe: `diagrams/DMTRD_12_krawedzi.graphml`, `diagrams/DMTRD_24_przejscia.graphml`
- SVG/PNG: `.venv\Scripts\python.exe src\generate_diagrams.py`
- Otwórz .graphml w yEd do edycji wizualnej

## Testy i walidacja
- Uruchom: `.venv\Scripts\python.exe src\validate_model.py`
- Wszystkie testy muszą przechodzić (0 błędów)
- Sprawdzane: 8 stanów, 24 przejścia, d_H=1, odwrotności, GraphML, topologia Q3

## Zasady rzetelności naukowej
- **Rozróżniaj hipotezy od ustaleń**: wszystko w DMTRD to propozycje teoretyczne (oznaczaj "hipoteza DMTRD", "postulat DMTRD")
- **Nie twórz fikcyjnych publikacji**: cytuj tylko zweryfikowalne źródła (DOI, autorzy, rok)
- **Nie przedstawiaj DMTRD jako teorii potwierdzonej**: model na etapie opracowywania, niezwalidowany empirycznie
- **Status epistemiczny**: koncepcyjny/hipotetyczny, wymaga niezależnej recenzji i badań EMA/LTA/CTMC

## Bezpieczeństwo
- **Zakaz publikowania sekretów**: klucze API, tokeny, hasła, pliki .env
- Przed `git add` sprawdzaj: `git diff --check`, `git status`
- Nie umieszczaj sekretów nawet przejściowo w historii Git

## Historia rewizji
- Zachowaj historię commitów
- Nie używaj `git push --force`
- Nie przepisuj historii zdalnego repozytorium
- Komunikaty commitów: konwencjonalne (np. `docs:`, `feat:`, `fix:`, `refactor:`)

## Synchronizacja z GitHub
- Remote: `origin` → `https://github.com/PeterPirog/DMTR`
- Gałąź: `main`
- Pull przed push: `git pull origin main`
- Push tylko po walidacji: `git push origin main`
- Dla dużych zmian: twórz gałąź (`git checkout -b feature/xyz`)

## Generowanie dokumentów
- Główny dokument: `.venv\Scripts\python.exe src\build_document.py` → `DMTRD_koncepcja.docx`
- Streszczenie recenzenta: `.venv\Scripts\python.exe src\build_reviewer_doc.py` → `DMTRD_streszczenie_dla_recenzenta.docx`

## Struktura katalogów (nie przemieszczaj plików)
```
DMTRD/
├── *.docx, *.md, *.txt, requirements.txt
├── research/     # materiały badawcze (md, bib, csv)
├── model/        # definicje formalne (md, csv)
├── diagrams/     # GraphML, SVG, PNG
├── src/          # skrypty Python
├── tests/        # testy (zintegrowane z validate_model.py)
└── reports/      # raporty
```