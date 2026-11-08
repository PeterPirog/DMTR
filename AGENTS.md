# AGENTS.md – Instrukcje dla agentów OpenCode (DMTRD)

## Katalog roboczy
`D:\Opencode_Projects\projects\DMTRD`

## Źródła prawdy dla danych modelu
- `model/stany.csv` – definicje 8 stanów (kod, W, C, N, opisy, przejścia)
- `model/przejscia_24.csv` – 24 przejścia kierunkowe z pełną charakterystyką
- `model/definicje.md` – formalizacja matematyczna (Q3, HPE, DTMC, CTMC, LTA)
- `model/DMTRD_KANON_KONCEPCYJNY.md` – **KANON KONCEPCYJNY** – jedno źródło prawdy dla definicji W, C, N

## Zasady spójności modelu
1. **Osiem stanów**: kody 000–111, każdy ma unikalny kod 3-bitowy zgodny z W,C,N
2. **12 par sąsiedztwa**: każda para stanów o odległości Hamminga d_H = 1
3. **24 przejścia kierunkowe**: każda krawędź nieskierowana = 2 przejścia odwrotne
4. **HPE (Hipoteza Przejść Elementarnych)**: każde dozwolone przejście ma d_H = 1
5. **Asymetria**: przejścia odwrotne (np. 011→111 vs 111→011) to odrębne procesy psychologiczne

## Zasady ochrony przed dryftem koncepcyjnym (rev3)
1. **Nie redefiniować W, C, N** bez wyraźnej decyzji autora.
   - W = CHCĘ = chęć wykonania konkretnego działania
   - C = MOGĘ = subiektywnie oceniana wykonalność działania
   - N = POWINIENEM = racjonalne przekonanie o konieczności działania ze względu na swoje cele
2. **Nie dodawać nowych podstawowych wymiarów** do rdzenia bez uzasadnienia.
3. **Nie zastępować modelu binarnego modelem ciągłym** jako wersji bazowej.
4. **Nie przedstawiać modelu probabilistycznego jako obowiązkowego elementu DMTRD.**
   - CTMC, LTA, HMM to rozszerzenia, nie rdzeń.
5. **Nie traktować HPE jako udowodnionego prawa psychologicznego.**
   - HPE-model = topologia Q (qᵢⱼ=0 dla d_H≥2)
   - HPE-empiryczna = hipoteza testowalna
6. **Nie utożsamiać stanu z faktycznym zachowaniem.**
   - Stan = konfiguracja trzech ocen (W,C,N)
   - Zachowanie = osobna zmienna wynikowa
7. **Nie utożsamiać N z emocjonalną winą lub presją.**
   - N = racjonalne przekonanie o konieczności działania ze względu na swoje cele
8. **Priorytetem są praktyczne charakterystyki stanów i przejść.**
   - Każdy stan: schemat A–L (kod, nazwa, znaczenie, psychologia, przykłady, granice)
   - Każde przejście: schemat 1–12 (etykieta neutralna, hipotezy mechanistyczne, granice)
9. **Zachowywać zgodność dokumentów, danych i diagramów.**
   - Jeden kanonyczny źródło: `model/DMTRD_KANON_KONCEPCYJNY.md`
   - Generatory czytają z CSV, nie hartują definicji
10. **Nie ogłaszać walidacji empirycznej bez odpowiednich badań.**
    - Rev3 to wersja koncepcyjna, nie zwalidowana empirycznie
    - Hipotezy HPE, HPD, HPP, E1–E24 to propozycje do testowania

## Aktualizacja diagramów GraphML
- Uruchom: `.venv\Scripts\python.exe src\build_graph.py`
- Pliki wyjściowe: `diagrams/DMTRD_12_krawedzi.graphml`, `diagrams/DMTRD_24_przejscia.graphml`
- SVG/PNG: `.venv\Scripts\python.exe src\generate_diagrams.py`
- Otwórz .graphml w yEd do edycji wizualnej

## Testy i walidacja
- Uruchom: `.venv\Scripts\python.exe src\validate_model.py`
- Wszystkie testy muszą przechodzić (0 błędów)
- Sprawdzane: 8 stanów, 24 przejścia, d_H=1, odwrotności, GraphML, topologia Q3
- Walidacja DOCX: `.venv\Scripts\python.exe src\validate_docx.py` (10 kryteriów)
- Test symulacji CTMC: `.venv\Scripts\python.exe src\hpe_simulation.py` (test CR-01)

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
- Główny dokument: `.venv\Scripts\python.exe src\build_document.py` → `DMTRD_koncepcja_rev3.docx`
- Streszczenie recenzenta: `.venv\Scripts\python.exe src\build_reviewer_doc.py` → `DMTRD_streszczenie_dla_recenzenta_rev3.docx`
- GraphML: `.venv\Scripts\python.exe src\build_graph.py` → `diagrams/DMTRD_12_krawedzi.graphml`, `diagrams/DMTRD_24_przejscia.graphml`

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

## Wersje dokumentów
- **rev1** – wersja początkowa (dryft koncepcyjny)
- **rev2** – audyt spójności (naprawy techniczne, ale dryft w definicjach)
- **rev3 (kanoniczna)** – przywrócenie definicji autora, binarny rdzeń, praktyczna użyteczność