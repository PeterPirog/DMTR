# Macierz Odpowiedzi na Recenzję ASTRA – DMTRD rev1

**Data:** 07.11.2026  
**Wersja:** 1.0  
**Autor:** Zespół rewizji DMTRD  
**Baza:** Recenzja ASTRA z 07.11.2026 (raport `reports/ASTRA_recenzja.md`)

---

## Legenda

| Symbol | Znaczenie |
|--------|-----------|
| **ACCEPT** | Zarzut zasadny – wymaga zmiany w modelu/dokumencie |
| **PARTIAL** | Zarzut częściowo zasadny – wymaga doprecyzowania lub ograniczonej zmiany |
| **REJECT** | Zarzut niezasadny – odrzucamy z uzasadnieniem |
| **UNRESOLVED** | Brak wystarczających podstaw do rozstrzygnięcia w tym etapie |

**Priorytety ASTRA:** CRITICAL / MAJOR / MINOR  
**Status realizacji:** TODO / IN_PROGRESS / DONE / DEFERRED

---

## SEKCJA B – PROBLEMY TEORETYCZNE

### B1. CHCĘ nie ma ustalonego znaczenia (CRITICAL)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B1 |
| **Priorytet** | CRITICAL |
| **Lokalizacja** | Rozdz. 3, 4.1, 8.2–8.5, 14.1; `model/stany.csv` (wiersze 110, 111); `model/definicje.md` (linia 7) |
| **Treść zarzutu** | W jest definiowane jako wewnętrzna zgoda, ale do przejawów zalicza „chęć, pragnienie, zamiar”. Rozdz. 3 odróżnia stan od intencji, a rozdz. 8 utożsamia W z autonomią. To nie są pojęcia równoważne. Człowiek może autonomicznie uznawać sens rehabilitacji i nie mieć aktualnej ochoty na ćwiczenie; może silnie chcieć nagrody pod presją; może pragnąć rezultatu bez zamiaru podjęcia działania. Proponowane wskaźniki IMI Interest/Enjoyment, identified regulation i postawa TPB nie są zamiennymi miarami jednego konstruktu. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Recenzent słusznie wskazuje na fundamentalną niejednoznaczność: W jest jednocześnie definiowane jako (a) osobista akceptacja celu, (b) chęć/pragnienie, (c) intencja, (d) autonomiczna motywacja. To są różne konstrukty psychologiczne. W szczególności utożsamienie W z „zamiarem” (intencją TPB) sprzeczy jawnej deklaracji w rozdz. 3, że model nie zawiera intencji. Utożsamienie z autonomią (SDT) jest problematyczne, bo autonomia w SDT to jakość regulacji, a nie binarna obecność/braku chęci. |
| **Decyzja o zmianie** | Należy wybrać **jedną** podstawową definicję W i konsekwentnie usunąć utożsamienia z innymi konstruktami. Zalecana definicja: **W = osobista akceptacja wartości celu / zgoda na realizację celu** (bliższe *identified regulation* SDT niż *intrinsic motivation*). Intencja, pragnienie, chęć, przyjemność – to osobne konstrukty, które mogą korelować z W, ale nie są z nim tożsame. |
| **Proponowana poprawka** | 1. Zmiana definicji w `model/definicje.md` (linia 7) na: `W ∈ {0,1} – CHCĘ (osobista akceptacja wartości celu / zgoda na realizację celu)`<br>2. Aktualizacja `model/stany.csv` – kolumna `interpretacja_psychologiczna` dla stanów z W=1<br>3. Usunięcie z `model/definicje.md` i dokumentu DOCX utożsamień: „chęć, pragnienie, zamiar”, „autonomiczna motywacja”, „intencja”<br>4. W sekcji 4.1 (DOCX) – precyzyjna definicja operacyjna z wyliczeniem co W **nie** jest<br>5. Aktualizacja wskaźników pomiarowych: IMI Interest/Enjoyment → nie; Identified Regulation (SDT) → tak (jako proxy); Attitude (TPB) → częściowo |
| **Pliki do aktualizacji** | `model/definicje.md`, `model/stany.csv`, `src/build_document.py`, `DMTRD_koncepcja.docx` (przez regenerację), `research/operacjonalizacja_WCN_rev1.md` (nowy) |
| **Metoda weryfikacji** | Sprawdzenie spójności definicji we wszystkich plachach; test CFA na 3 czynniki (W, C, N) – AVE > kwadrat korelacji |
| **Status realizacji** | TODO |

---

### B2. POWINIENEM jest definiowane i kodowane sprzecznie (CRITICAL)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B2 |
| **Priorytet** | CRITICAL |
| **Lokalizacja** | Rozdz. 4.3, 6.2, 8.4–8.5, 9.2, 10.1; `model/stany.csv` (stany 110, 111); `model/definicje.md` (linia 9) |
| **Treść zarzutu** | Definicja N obejmuje obowiązek z norm zewnętrznych i zinternalizowanych. Tymczasem w rozdz. 8.4 N=0 może oznaczać, że normy zostały zinternalizowane do W; w rozdz. 8.5 zinternalizowane N uzasadnia N=1 i wysoką jakość 111. Jeżeli po internalizacji nadal występuje poczucie obowiązku, zgodnie z definicją powinno być N=1. Jeżeli poczucie obowiązku zanika, trzeba to zmierzyć, a nie wyprowadzać z samej internalizacji. „Presja” nie jest synonimem dobrowolnie przyjętej odpowiedzialności. To podważa rozróżnienie 110 i 111 oraz interpretację przejść 011→111 i 110→111. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To jeden z najpoważniejszych błędów koncepcyjnych. Model jednocześnie twierdzi, że: (1) N = poczucie zobowiązania normatywnego (definicja), (2) internalizacja normy może oznaczać przejście N=1 → W=1 (zanik N), (3) internalizacja normy może oznaczać N=1 (utrzymanie poczucia obowiązku). To logiczne sprzeczność. Stan 110 (W=1, C=1, N=0) jest opisywany jako „motywacja autonomiczna, N zinternalizowane do W”, a stan 111 (W=1, C=1, N=1) jako „N zinternalizowane”. Nie ma jasnej reguły: czy zinternalizowany obowiązek to N=0 czy N=1? |
| **Decyzja o zmianie** | Należy ustalić **jedną regułę kodowania N** i oddzielić ją od pomiaru *jakości* regulacji (internalizacja vs eksternalizacja). Zalecana reguła: **N = 1 wtedy i tylko wtedy, gdy osoba doświadcza poczucia „powinienem” / zobowiązania wobec działania, niezależnie od źródła (zewnętrzne/wewnętrzne).** Źródło i jakość regulacji to osobna zmienna (np. `N_source ∈ {external, introjected, identified, integrated}`), nie bit w kodzie stanu. Internalizacja to proces zmiany `N_source`, a nie koniecznie zmiana N z 1 na 0. |
| **Proponowana poprawka** | 1. Zmiana definicji w `model/definicje.md` (linia 9): `N ∈ {0,1} – POWINIENEM (poczucie zobowiązania normatywnego wobec realizacji celu; źródło: zewnętrzne lub internalizowane)`<br>2. Dodanie zmiennej pomocniczej `N_source` (niezmieniającej liczby stanów) do opisu stanów<br>3. Przeanalizowanie i poprawienie opisów stanów 110 i 111 w `model/stany.csv` – usunięcie sprzeczności<br>4. Aktualizacja interpretacji przejść 011→111, 110→111, 111→011, 111→110 w `model/przejscia_24.csv`<br>5. Usunięcie z dokumentu twierdzenia, że internalizacja *zawsze* oznacza spadek N |
| **Pliki do aktualizacji** | `model/definicje.md`, `model/stany.csv`, `model/przejscia_24.csv`, `src/build_document.py`, `DMTRD_koncepcja.docx`, `research/operacjonalizacja_WCN_rev1.md` |
| **Metoda weryfikacji** | Sprawdzenie logicznej spójności: dla każdego stanu i przejścia – czy reguła kodowania N daje jednoznaczną odpowiedź? Test na przykładach brzegowych (np. ktoś kto internalizował normę, ale czuje, że *nie powinien* już robić czegoś). |
| **Status realizacji** | TODO |

---

### B3. MOGĘ zmienia się z oceny subiektywnej w warunek obiektywny (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B3 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 3, 4.2, 8.1, 8.3, 9.1–9.2, 11, 14.1; `model/stany.csv`; `model/definicje.md` (linia 8) |
| **Treść zarzutu** | Na poziomie definicji C oznacza postrzeganą wykonalność. W opisach przejść C=0 staje się brakiem zasobów, a C=1 ich uzyskaniem. Subiektywne C=0 nie wyklucza wykonania, a C=1 go nie gwarantuje. Zasoby, kompetencje, czas i dostęp środowiskowy mogą być przyczynami oceny wykonalności, niekoniecznie refleksyjnymi wskaźnikami jednego czynnika. Błędem jest traktowanie tego połączenia jako równoważnego rzeczywistym warunkom COM-B. GSE nie zastępuje automatycznie chwilowej oceny konkretnego zadania. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Model ma prawo definiować C jako *subiektywną ocenę wykonalności* (bliższe PBC Ajzena niż capability COM-B). Problem polega na tym, że w opisach przejść i interpretacjach stanów C jest traktowane jak obiektywna możliwość („pozyskanie zasobów”, „utrata kompetencji”). To wprowadza zamieszanie. Należy konsekwentnie trzymać się definicji subiektywnej i oddzielić przyczyny (zasoby, kompetencje, czas) od samej oceny. |
| **Decyzja o zmianie** | Utrzymać definicję C jako **subiektywnie ocenianą wykonalność**. We wszystkich opisach przejść i stanów zastąpić język obiektywny („zasoby”, „kompetencje”) na język ocenowy („postrzegana dostępność zasobów”, „wiara w posiadanie kompetencji”). Dodać w `model/definicje.md` wyraźne rozróżnienie: C ≠ obiektywna możliwość; C ≠ capability COM-B; C = PBC (Ajzen) / self-efficacy (Bandura) w uproszczeniu binarnym. |
| **Proponowana poprawka** | 1. `model/definicje.md` linia 8: doprecyzowanie definicji C<br>2. `model/stany.csv` – przejrzenie kolumn `interpretacja_psychologiczna`, `procesy_poznawcze`, `przyczyny_wewnetrzne/srodowiskowe` w `przejscia_24.csv` – usunięcie traktowania C jako obiektywnego warunku<br>3. Dodanie w `model/definicje.md` sekcji „C a COM-B / SCT / TPB” z tabelą rozróżnień |
| **Pliki do aktualizacji** | `model/definicje.md`, `model/stany.csv`, `model/przejscia_24.csv`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Przejrzenie wszystkich 24 opisów przejść – czy żaden nie twierdzi, że C=1 gwarantuje wykonanie lub C=0 uniemożliwia? |
| **Status realizacji** | TODO |

---

### B4. Rozłączność pojęciowa mylona z niezależnością statystyczną i dynamiczną (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B4 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 2: Q1, 5: A1, 6.2, 10.2, 14.2, 19; `model/definicje.md` |
| **Treść zarzutu** | Trzy różne pytania nie dowodzą trzech odrębnych konstruktów. Odrębne konstrukty nie muszą mieć zerowych korelacji. Interakcje opisane w rozdz. 10.2 wręcz zakładają związki między W, C i N. CFA nie sprawdza wszystkich tych tez. Literalna rozłączność motywacji i obowiązku jest szczególnie wątpliwa, bo poczucie obowiązku samo może motywować. Model może opisywać współwystępujące aspekty regulacji, nie „niezależne substancje” psychiczne. |
| **Własna ocena** | **PARTIAL** |
| **Argumentacja** | Recenzent ma rację, że dokument niekiedy sugeruje, że rozróżnienie pojęciowe = niezależność statystyczna. Jednak sama idea trzech *wymiarów* (nie „substancji”) nie wymaga ortogonalności. Wymaga jedynie odrębności definicyjnej i pomiarowej. Zgadzam się, że trzeba to doprecyzować: W, C, N to **wymiary opisu**, a nie niezależne moduły psychiczne. Ich korelacje i interakcje dynamiczne są oczekiwane i pożądane. |
| **Decyzja o zmianie** | Doprecyzowanie w `model/definicje.md` i rozdz. 2/5 dokumentu: W, C, N to **wymiary przestrzeni stanów**, a nie hipoteza o trzech niezależnych modułach psychicznych. Usunięcie sformułowań sugerujących ortogonalność. Dodanie jasnego stwierdzenia: korelacje między W, C, N (między- i wewnątrzosobnicze) są oczekiwane; model nie postuluje niezależności. |
| **Proponowana poprawka** | 1. `model/definicje.md` – dodanie sekcji „Wymiary vs konstrukty psychiczne”<br>2. `src/build_document.py` – aktualizacja rozdziału 2 i 5 w DOCX<br>3. Usunięcie sformułowań „niezależne konstrukty” na rzecz „odrębne wymiary opisu” |
| **Pliki do aktualizacji** | `model/definicje.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy dokument nie twierdzi ortogonalności W, C, N. |
| **Status realizacji** | TODO |

---

### B5. Osiem konfiguracji logicznych nie jest dowodem ośmiu naturalnych stanów psychicznych (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B5 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 5: A1–A2, 7.1, 8, 13: HG1, 14; `model/stany.csv` (nazwy stanów) |
| **Treść zarzutu** | `2³ = 8` wynika z binarnego kodowania. Nie wynika z tego, że wszystkie konfiguracje występują dostatecznie często, mają jednorodne mechanizmy, są metastabilne albo stanowią optymalną reprezentację danych. Nazwy „neutralność”, „działanie autonomiczne” czy „pełna gotowość” dodają treść niewynikającą z bitów. Model klasyfikacyjny nie musi postulować naturalnych kategorii, ale wtedy powinien uzasadniać użyteczność kompresji informacji. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To fundamentalny punkt: model jest **klasyfikacją deklaratywną** (mapowaniem odpowiedzi na 3 pytania binarne), a nie odkryciem 8 naturalnych typów stanów psychicznych. Nazwy stanów to *etykiety interpretacyjne*, a nie nazwy odkrytych taksonów. Dokument niekiedy sugeruje drugie. |
| **Decyzja o zmianie** | Zmiana narracji: model = **uzupełnianie informacji** (kompresja trzech ocen do 8 kodów), a nie taksonomia stanów psychicznych. Nazwy stanów w `model/stany.csv` poprzedzić prefiksem „Konfiguracja:” lub zmienić na neutralne (np. „Stan 000” zamiast „Stan neutralny”). W dokumentach dodać wyraźne stwierdzenie: „Osiem stanów to wyczerpujące zestawienie logicznych kombinacji trzech ocen binarnych; nie postulujemy, że odpowiadają one ośmiu jakościowo odrębnym stanom psychicznym.” |
| **Proponowana poprawka** | 1. `model/stany.csv` – zmiana kolumny `nazwa_naukowa` na neutralne etykiety (np. „Konfiguracja 000”) + dodanie kolumny `etykieta_interpretacyjna` z dotychczasowymi nazwami<br>2. `src/build_document.py` – aktualizacja generowania tabeli stanów i opisów<br>3. Dodanie w `model/definicje.md` sekcji „Status epistemiczny ośmiu stanów” |
| **Pliki do aktualizacji** | `model/stany.csv`, `model/definicje.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy dokument nie twierdzi, że 8 stanów to „naturalne kategorie psychiczne”. |
| **Status realizacji** | TODO |

---

### B6. Stan 101 nie jest równoważny moral distress (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B6 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 6.2, 8.1, 8.3, 13: HG4, 17, 19; `model/stany.csv` (stan 101); `model/przejscia_24.csv` (T15, T16) |
| **Treść zarzutu** | 101 mówi jedynie o obecności W i N oraz braku C. Nie zawiera pomiaru moralnego charakteru sytuacji, osądu moralnego, cierpienia ani związku cierpienia z wydarzeniem moralnym. Chęć wysłania raportu, poczucie administracyjnego obowiązku i awaria internetu mogą dać 101 bez moral distress. Równość „101 = moral distress” jest nieuzasadniona. Dopuszczalna hipoteza: w określonych sytuacjach moralnych 101 może zwiększać ryzyko lub współwystępować z moral distress. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To utożsamienie jest nadinterpretacją. Stan 101 to **konfiguracja ocen** (W=1, C=0, N=1), a nie diagnoza kliniczna/psychologiczna. Moral distress wymaga specyficznych warunków (moralny charakter sytuacji, cierpienie, blokada moralnie właściwego działania). Model może *hipotezować*, że 101 w kontekście moralnym predysponuje do moral distress, ale nie może utożsamiać. |
| **Decyzja o zmianie** | Usunięcie równości „101 = moral distress” z definicji i opisów. Zastąpienie hipotezą: **H_MD: W sytuacjach o moralnym charakterze, stan 101 predysponuje do doświadczenia moral distress (mierzonego skalą MDS).** W `model/stany.csv` usunięcie „moral distress” z `interpretacja_psychologiczna` stanu 101. W `model/przejscia_24.csv` – przejścia T15, T16: zmiana nazw procesów z „Rozwiązanie konfliktu / Moral distress resolution” na neutralne. |
| **Proponowana poprawka** | 1. `model/stany.csv` – stan 101: usunięcie „moral distress” z `interpretacja_psychologiczna`, `procesy_emocjonalne`, `powiazania_teorie`<br>2. `model/przejscia_24.csv` – T15, T16: zmiana `nazwa_procesu` na neutralne<br>3. Dodanie hipotezy H_MD do `research/hipotezy_badawcze_rev1.md`<br>4. Aktualizacja `DMTRD_koncepcja.docx` |
| **Pliki do aktualizacji** | `model/stany.csv`, `model/przejscia_24.csv`, `research/hipotezy_badawcze_rev1.md`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy żaden fragment nie twierdzi tożsamości 101 z moral distress. |
| **Status realizacji** | TODO |

---

### B7. Każdej krawędzi przypisano zbyt jednoznaczny mechanizm (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B7 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 9–10, 13; `model/przejscia_24.csv` (kolumny `nazwa_procesu`, `interpretacja_psychologiczna`); aneks A w recenzji |
| **Treść zarzutu** | Zapis zmiany to opis wyniku, nie identyfikacja przyczyny. 011→111 może oznaczać internalizację, ale również pojawienie się przyjemności, nagrody, zmianę interpretacji pytania lub błąd pomiaru. Pełna ocena 24 przejść w tabeli recenzenta pokazuje, że każda nazwa procesu to hipoteza, a nie fakt wynikający z kodu. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To kluczowy punkt metodologiczny. Kod przejścia (np. 011→111 = zmiana W: 0→1 przy C=1, N=1) opisuje **co się zmieniło**, a nie **dlaczego**. Nazwy procesów (internalizacja, wypalenie, autonomizacja) to *hipotezy mechanistyczne*, które wymagają osobnego pomiaru i testu. Obecny dokument ich utożsamia. |
| **Decyzja o zmianie** | Separacja trzech warstw w `model/przejscia_24.csv` i dokumentacji:<br>1. **Kod przejścia** (co się zmieniło – wynikający z bitów)<br>2. **Etykieta neutralna** (np. „Zmiana W: 0→1 przy C=1, N=1”)<br>3. **Hipotezy mechanistyczne** (lista alternatywnych wyjaśnień z odsyłaczami do literatury)<br>Usunięcie pojedynczej kolumny `nazwa_procesu` na rzecz `etykieta_neutralna` + `hipotezy_mechanistyczne` (lista). |
| **Proponowana poprawka** | 1. `model/przejscia_24.csv` – restrukturyzacja: usunięcie `nazwa_procesu`, `interpretacja_psychologiczna`; dodanie `etykieta_neutralna`, `hipotezy_mechanistyczne` (jako lista rozdzielona `; `)<br>2. `src/build_document.py` – aktualizacja generowania tabeli przejść i opisów<br>3. `src/build_graph.py` – aktualizacja GraphML (Custom Properties)<br>4. `DMTRD_koncepcja.docx` – regeneracja |
| **Pliki do aktualizacji** | `model/przejscia_24.csv`, `src/build_document.py`, `src/build_graph.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Dla każdego z 24 przejść: czy `etykieta_neutralna` wynika wyłącznie z kodów? Czy `hipotezy_mechanistyczne` zawiera co najmniej 2 alternatywne wyjaśnienia? |
| **Status realizacji** | TODO |

---

### B8. HPE może być własnością kodowania, a nie psychologiczną atomowością zmiany (CRITICAL)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B8 |
| **Priorytet** | CRITICAL |
| **Lokalizacja** | Rozdz. 5: A3, 7.2, 13: HG2, 14.1–14.2; `model/definicje.md` (sekcja 3); `research/hipotezy_badawcze.md` (HG2) |
| **Treść zarzutu** | Nie określono, czym jest „elementarny proces” niezależnie od zmiany jednego bitu. Jeżeli każde zdarzenie wielobitowe można bez ograniczeń nazwać ciągiem nieobserwowanych zdarzeń, hipoteza traci rozstrzygający charakter. Wspólny bodziec może wpływać równocześnie na W, C i N. W wersji ciągłej: przy ciągłych trajektoriach i trzech progach przecięcia różnych płaszczyzn często występują w różnych chwilach. Można obserwować zmiany jednego bitu, mimo że ten sam proces przyczynowy nieustannie zmienia wszystkie trzy wielkości. Potrzebne są: niezależna definicja zdarzenia psychologicznego, skala czasu, model błędu i jawny model alternatywny. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To najgłębszy problem teoretyczny DMTRD. HPE jest obecnie **definicją operacyjną** (zmiana kodu o 1 bit), a nie hipotezą o psychologii. Jeśli ten sam proces przyczynowy zmienia W, C, N asynchronicznie (np. najpierw rośnie W, potem C, potem N), to w dyskretyzacji binarnej zobaczymy sekwencję zmian jednobitowych, mimo że przyczyna była jedna. HPE jako hipoteza empiryczna ma sens tylko przy: (a) zdefiniowaniu skali czasu elementarnego procesu, (b) modelu błędu pomiarowego, (c) modelu alternatywnego (np. współzmienność zmian). |
| **Decyzja o zmianie** | Przeformułowanie HPE z „prawa psychologicznego” na **ograniczenie modelowe z testowalną hipotezą pomocniczą**:<br>**HPE-model:** Generator Q w CTMC ma qᵢⱼ = 0 dla d_H ≥ 2.<br>**HPE-empiryczna:** W danych EMA z gęstym próbkowaniem, odsetek obserwowanych zmian d_H ≥ 2 jest istotnie mniejszy niż przewidywane przez model alternatywny (np. niezależne zmiany bitów z błędami pomiarowymi).<br>Usunięcie twierdzenia, że HPE odzwierciedla „atomowość procesów psychologicznych”. |
| **Proponowana poprawka** | 1. `model/definicje.md` sekcja 3 – przepisanie HPE jako ograniczenia modelowego + hipotezy empirycznej<br>2. `research/hipotezy_badawcze_rev1.md` – przepisanie HG2 z usunięciem arbitralnego progu 15%<br>3. `model/HPE_formalizacja_rev1.md` (nowy) – formalna specyfikacja HPE-model, HPE-empiryczna, modeli alternatywnych (M1–M5), skali czasu, błędu pomiarowego<br>4. `research/HPE_testowalnosc_rev1.md` (nowy) – plan testów symulacyjnych i empirycznych<br>5. Kod symulacyjny w `src/` do weryfikacji numerycznej kontrprzykładu Astry |
| **Pliki do aktualizacji** | `model/definicje.md`, `research/hipotezy_badawcze_rev1.md`, `model/HPE_formalizacja_rev1.md`, `research/HPE_testowalnosc_rev1.md`, `src/hpe_simulation.py` (nowy), `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Symulacja numeryczna: czy przy generatorze Q spełniającym HPE-model, przy realistycznych odstępach EMA (2-3h) i intensywnościach, odsetek obserwowanych d_H≥2 przekracza 15%? (Kontrprzykład Astry). |
| **Status realizacji** | TODO |

---

### B9. Podstawowy stan nie jest wystarczający dla deklarowanej dynamiki Markowa (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B9 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 7.3–7.4, 8.5, 12, 14.2; `model/definicje.md` (sekcje 4.1–4.5, 5.7) |
| **Treść zarzutu** | Markowowskość oznacza, że po uwzględnieniu aktualnego stanu przyszłość nie zależy od wcześniejszej historii. Rozdział 12 stawia przeciwne przewidywanie: 111 ma inną stabilność zależnie od drogi dojścia. Agregacja bardziej szczegółowego procesu Markowa do ośmiu kategorii nie musi zachowywać własności Markowa. Wymaga odpowiednich warunków agregowalności albo empirycznie akceptowalnego przybliżenia. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Dokument jest niespójny: raz zakłada model Markowski (bezpamięciowy), raz postuluje zależność od historii (path dependence). To dwa różne modele. Trzeba wybrać: albo (a) podstawowy model = CTMC/DTMC Markowski (3 bity = stan), a path dependence = rozszerzenie (model rzędu wyższego, zmienne latentne), albo (b) stan = (W,C,N) + historia. Obecnie to mieszanka. |
| **Decyzja o zmianie** | Jasne rozróżnienie w `model/definicje.md`:<br>- **Model bazowy (Markowski):** stan = (W,C,N); Q macierz 8×8; bezpamięciowy.<br>- **Rozszerzenie (path dependence):** stan rozszerzony o zmienne latentne historii lub model rzędu wyższego; to osobna specyfikacja modelu, nie założenie bazowego.<br>W rozdz. 12 (DOCX) – usunięcie sprzeczności; path dependence jako *hipoteza do testowania* w modelu rozszerzonym, nie cecha modelu bazowego. |
| **Proponowana poprawka** | 1. `model/definicje.md` sekcje 4.1–4.5, 5.7 – restrukturyzacja: model bazowy vs rozszerzenia<br>2. `src/build_document.py` – aktualizacja rozdziału 12 i 7 w DOCX<br>3. `research/model_pomiarowy_rev1.md` (nowy) – specyfikacja modelu bazowego i rozszerzeń |
| **Pliki do aktualizacji** | `model/definicje.md`, `src/build_document.py`, `research/model_pomiarowy_rev1.md`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy dokument nie twierdzi jednocześnie bezpamięciowości i path dependence dla tego samego modelu. |
| **Status realizacji** | TODO |

---

### B10. Rozróżnienie motywacji i działania jest deklarowane, lecz naruszane w interpretacjach (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B10 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 3, 5: A5, 8, 11, 14.2; `model/stany.csv` (stan 110 – nazwa „Działanie autonomiczne”); `model/przejscia_24.csv` |
| **Treść zarzutu** | Nazwa 110 „Działanie autonomiczne” sugeruje wykonanie, choć kod nie zawiera zachowania. Rozdział 11 wskazuje 101 jako stan sprzyjający inicjacji, ale uzasadnia to szukaniem C. Szukanie zasobu to inne działanie niż wykonanie pierwotnego zadania. Dokument nie jest całkowicie „bez celu”: definicje od początku odnoszą się do konkretnego celu lub działania. Trzeba ustalić działanie, obiekt, kontekst i horyzont czasu oraz osobno rejestrować intencję, wykonanie i działania przygotowawcze. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Nazwa „Działanie autonomiczne” dla stanu 110 to błąd komunikacyjny – stan to konfiguracja ocen, nie zachowanie. Podobnie, rozdz. 11 miesza stan motywacyjny z działaniami przygotowawczymi. Model deklaruje separację stanu od zachowania, ale w interpretacjach tej separacji nie przestrzega. |
| **Decyzja o zmianie** | 1. Zmiana nazwy stanu 110 w `model/stany.csv` z „Działanie autonomiczne” na „Autonomiczna gotowość” lub „Gotowość autonomiczna”.<br>2. Przejrzenie wszystkich opisów stanów i przejść – usunięcie sformułowań sugerujących, że stan = działanie.<br>3. Dodanie w `model/definicje.md` jawnego stwierdzenia: stan (W,C,N) ≠ działanie; działanie to osobna zmienna wynikowa. |
| **Proponowana poprawka** | 1. `model/stany.csv` – stan 110: `nazwa_naukowa` = „Gotowość autonomiczna”, `nazwa_opisowa` = „Chcę i mogę, nie powinienem”<br>2. `model/definicje.md` – dodanie sekcji „Stan vs zachowanie”<br>3. `src/build_document.py` – aktualizacja opisów<br>4. Przejrzenie `model/przejscia_24.csv` pod kątem języka sugerującego wykonanie |
| **Pliki do aktualizacji** | `model/stany.csv`, `model/definicje.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy żaden opis stanu nie zawiera słowa „działanie” jako składowej nazwy lub definicji stanu. |
| **Status realizacji** | TODO |

---

### B11. Obsługa nawyku i ambiwalencji prowadzi do odmiennych znaczeń tych samych kodów (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | B11 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 3–4, 11.1, 15.1: ARG3, 16; `model/stany.csv` (stany 010, 011); `model/definicje.md` |
| **Treść zarzutu** | Brak aktualnej refleksji o chęci nie jest tym samym co brak osobistej akceptacji. Nawykowe działanie może być chciane i autonomicznie popierane; automatyzacja nie wymaga przejścia 110→010. Wood i Neal opisują oddziaływanie nawyków i celów, a nie prostą wymienność świadomej motywacji i automatyzmu. Wartość W=0 nie diagnozuje nawyku. Rozdział 3 odróżnia brak chęci od silnej niechęci, ale rozdział 4.1 umieszcza neutralność i awersję w tej samej kategorii. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Model w wersji binarnej nie może rozróżnić: (a) brak chęci (neutralność), (b) awersję (silna niechęć), (c) działanie nawykowe bez aktualnej refleksji. To fundamentalna granica modelu. Należy jawnie zadeklarować zakres zastosowania: **model dotyczy procesów refleksyjnych (System 2); dla nawyków (System 1) wymaga rozszerzenia parametrem H lub wersji ciągłej.** |
| **Decyzja o zmianie** | 1. Dodanie w `model/definicje.md` i rozdz. 3/11 DOCX: **Ograniczenie zakresu** – model opisuje regulację refleksyjną; dla nawyków wymaga rozszerzenia.<br>2. W `model/stany.csv` stanach 010, 011 – doprecyzowanie `ograniczenia_interpretacyjne`: „W=0 nie rozróżnia braku chęci, awersji i działania nawykowego.”<br>3. Dodanie parametru H (siła nawyku) do `model/definicje.md` sekcji 6 jako propozycja rozszerzenia (nie do modelu bazowego). |
| **Proponowana poprawka** | 1. `model/definicje.md` – sekcja „Zakres modelu i ograniczenia”<br>2. `model/stany.csv` – aktualizacja `ograniczenia_interpretacyjne` dla stanów 010, 011<br>3. `src/build_document.py` – aktualizacja rozdziału 3, 11, 15 w DOCX<br>4. `research/operacjonalizacja_WCN_rev1.md` – jawne zadeklarowanie zakresu |
| **Pliki do aktualizacji** | `model/definicje.md`, `model/stany.csv`, `src/build_document.py`, `DMTRD_koncepcja.docx`, `research/operacjonalizacja_WCN_rev1.md` |
| **Metoda weryfikacji** | Sprawdzenie, czy dokument nie twierdzi, że model wyjaśnia działania nawykowe bez rozszerzenia. |
| **Status realizacji** | TODO |

---

## SEKCJA C – PROBLEMY METODOLOGICZNE

### C1. Plan testuje inną HPE niż formalizacja CTMC (CRITICAL)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C1 |
| **Priorytet** | CRITICAL |
| **Lokalizacja** | Rozdz. 7.3, 13.1: HG2, 14.2: „Częstotliwość” i „Analiza statystyczna”; aneks G, HG2 i analiza LTA; `research/hipotezy_badawcze.md` (HG2); `src/build_document.py` |
| **Treść zarzutu** | W CTMC HPE dotyczy generatora Q. Tymczasem plan LTA zeruje `p_ij` dla `d_H≥2` przy odstępach 2–3 godzin. Wielobitowe różnice między obserwacjami są możliwe w CTMC zgodnym z HPE. Próg falsyfikacji z aneksu G — ponad 15% zmian wielobitowych przy pomiarze co 30 minut — jest arbitralny bez określenia intensywności. Kontrprzykład analityczny: przy intensywności 1/h dla każdego bitu niezależnie, po 30 min prawdopodobieństwo zmiany ≥2 bitów ≈ 23.7%. To przekracza 15% mimo prawdziwej HPE. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To błąd krytyczny w planie badawczym. Test LTA na poziomie macierzy przejścia P(Δt) z Δt=2-3h **nie testuje HPE na poziomie generatora Q**. HPE na poziomie Q dopuszcza wielobitowe zmiany w P(Δt). Próg 15% jest bezfundamentowy. |
| **Decyzja o zmianie** | 1. Usunięcie testu LTA z `p_ij=0 dla d_H≥2` jako testu HPE.<br>2. Test HPE: estymacja CTMC (generator Q) z danych panelowych (pakiet `msm`/`ctmcm` w R/Python) + test LRT: H₀: qᵢⱼ=0 dla d_H≥2 vs H₁: qᵢⱼ>0 dla niektórych d_H≥2.<br>3. Alternatywnie: modelowanie ukrytego CTMC z danymi EMA (pakiet `ctmcm` lub `msm` z `obstrue=FALSE`).<br>4. Usunięcie arbitralnego progu 15% z HG2. |
| **Proponowana poprawka** | 1. `research/hipotezy_badawcze_rev1.md` – przepisanie HG2, usunięcie progu 15%, zmiana metody na estymację Q (CTMC)<br>2. `research/HPE_testowalnosc_rev1.md` – szczegółowy plan testu CTMC<br>3. `src/hpe_simulation.py` – symulacja weryfikująca kontrprzykład Astry<br>4. `src/build_document.py` – aktualizacja rozdziału 13, 14 w DOCX |
| **Pliki do aktualizacji** | `research/hipotezy_badawcze_rev1.md`, `research/HPE_testowalnosc_rev1.md`, `src/hpe_simulation.py`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Uruchomienie symulacji: czy przy Q spełniającym HPE (qᵢⱼ=0 dla d_H≥2) i realistycznych intensywnościach, estymowany Q z danych EMA (Δt=2-3h) ma qᵢⱼ≈0 dla d_H≥2? |
| **Status realizacji** | TODO |

---

### C2. Błędnie opisano identyfikowalność klas ukrytych (CRITICAL)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C2 |
| **Priorytet** | CRITICAL |
| **Lokalizacja** | Rozdz. 7.3, 14.1, 15.1: ARG5, 16; aneksy B/G i `model/definicje.md`; `research/hipotezy_badawcze.md` (sekcja 3) |
| **Treść zarzutu** | Trzeba odróżnić trzy modele: (1) Trzy obserwowane bity – dają 8 obserwowanych kategorii; (2) Osiem klas latentnych z trzema binarnymi wskaźnikami – model nadparametryzowany (31 parametrów vs 7 df); (3) HMM/LTA z wieloma pomiarami i ograniczeniami – informacja w sekwencjach może umożliwić identyfikację. Rozdział 14.1 mówi równocześnie o „trzech itemach na każdy wymiar” i o „3 wskaźnikach” – to 9 itemów = 512 wzorców. Identyfikowalność strukturalna i praktyczna to odrębne wymagania. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Recenzent ma całkowitą rację. Obecny dokument miesza pojęcia: „3 wskaźniki binarne = 8 wzorców = saturated model” dotyczy modelu (2) w jednym pomiarze, ale nie modelu longitudinalnego (3). Jednocześnie planuje 3 itemy na wymiar (9 itemów), co zmienia liczenie wzorców. To bałagan terminologiczny i metodologiczny. |
| **Decyzja o zmianie** | 1. Wybór **jednego** modelu pomiarowego dla głównej analizy i jasna jego specyfikacja.<br>2. Zalecany: **Model z obserwowanymi stanami (wersja ciągła W,C,N Likert 1-7) + CTMC/LTA z obserwowanymi stanami** – unika problemu klas latentnych. Wersja binarna tylko jako uproszczenie do wizualizacji.<br>3. Jeśli LTA z klasami latentnymi – jawna specyfikacja: liczba wskaźników, ich rozkłady, ograniczenia emisji, lokalne zależności, kotwice pomiarowe.<br>4. Usunięcie sformułowania „3 wskaźniki binarne = 8 klas = 0 df” jako ogólnego twierdzenia o LTA. |
| **Proponowana poprawka** | 1. `model/definicje.md` sekcja 7 – restrukturyzacja: jasny wybór modelu bazowego<br>2. `research/model_pomiarowy_rev1.md` (nowy) – pełna specyfikacja modelu pomiarowego<br>3. `research/hipotezy_badawcze_rev1.md` – aktualizacja sekcji metodologicznej<br>4. `src/build_document.py` – aktualizacja rozdziału 14 w DOCX |
| **Pliki do aktualizacji** | `model/definicje.md`, `research/model_pomiarowy_rev1.md`, `research/hipotezy_badawcze_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy dokument zawiera **jedną, spójną specyfikację** modelu pomiarowego z liczbą parametrów, df, ograniczeniami. |
| **Status realizacji** | TODO |

---

### C3. Progowanie może wygenerować pozorną dynamikę (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C3 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 7.5, 14.1–14.2, 15.1: ARG1; `model/definicje.md` (sekcja 6.1); `research/hipotezy_badawcze.md` (sekcja 3) |
| **Treść zarzutu** | Próg „np. 4” nie jest uzasadniony psychologicznie. Zmiana 3→4 zmienia stan, a 4→7 nie. Osoby blisko granicy mogą wielokrotnie przechodzić między kodami z powodu błędu odpowiedzi. Stałe progi nie gwarantują tego samego znaczenia między osobami. MacCallum i współautorzy pokazują ryzyko utraty informacji po dychotomizacji. Gęstsze próbkowanie może ujawniać częste przekroczenia progu niezgodne z prostym CTMC. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Progowanie ciągłych zmiennych na binarne jest arbitralne i traci informację. Wersja ciągła (oktaanty) jest lepsza psychometrycznie. Należy jawne porównanie wersji binarnej vs ciągłej i modelowanie błędu klasyfikacji. |
| **Decyzja o zmianie** | 1. Wersja bazowa modelu = **ciągła (W,C,N ∈ [1,7] lub [0,1])**; stan = oktaant (próg 4 jako *opcjonalna* dyskretyzacja do interpretacji).<br>2. W `model/definicje.md` sekcja 6.1 – wersja ciągła jako podstawowa, binarna jako uproszczenie.<br>3. W planie badawczym: porównanie dopasowania modelu ciągłego vs binarnego (AIC/BIC, predykcja).<br>4. Modelowanie błędu klasyfikacji przy progowaniu (latent class model z błędami). |
| **Proponowana poprawka** | 1. `model/definicje.md` sekcja 6.1 – wersja ciągła jako domyślna<br>2. `research/hipotezy_badawcze_rev1.md` – aktualizacja planu pomiarowego (wersja ciągła jako podstawowa)<br>3. `research/model_pomiarowy_rev1.md` – specyfikacja modelu z progowaniem i błędem klasyfikacji<br>4. `src/build_document.py` – aktualizacja rozdziału 7, 14 w DOCX |
| **Pliki do aktualizacji** | `model/definicje.md`, `research/hipotezy_badawcze_rev1.md`, `research/model_pomiarowy_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy wersja ciągła jest domyślna, a binarna oznaczona jako uproszczenie. |
| **Status realizacji** | TODO |

---

### C4. Walidacja pomiaru niedostosowana do wniosków o zmianach wewnątrzosobniczych (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C4 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 14.1–14.2, 18: etap 2; `research/hipotezy_badawcze.md` (sekcja 3) |
| **Treść zarzutu** | Przekrojowe CFA na 300–500 osobach nie ustala struktury chwilowych zmian u konkretnej osoby. Potrzebne są ocena treści itemów, wywiady poznawcze, rozróżnienie wariancji między- i wewnątrzosobniczej oraz sprawdzenie stabilności znaczenia pomiaru w czasie. CFI, RMSEA i AVE są wskaźnikami diagnostycznymi, nie samodzielnym dowodem trafności ani niezależności. Nie wiadomo, dlaczego przeciążenie rolą ma być wskaźnikiem N, a nie skutkiem wymagań i zasobów. Dla każdego itemu trzeba zdefiniować rolę w modelu. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Standardowa walidacja psychometryczna (CFA na danych przekrojowych) nie wystarczy do EMA. Potrzebna walidacja *wewnątrzosobnicza* (within-person): stabilność znaczenia itemów w czasie, rozdzielenie wariancji between/within, wywiady poznawcze (cognitive interviewing) na etapie pilotażu. |
| **Decyzja o zmianie** | 1. Rozdzielenie walidacji na dwa etapy: (a) pilotaż z wywiadami poznawczymi + analiza within-person reliability; (b) główne badanie EMA z modelem wielopoziomowym rozdzielającym wariancję between/within.<br>2. Dla każdego itemu W,C,N: jawna definicja roli (wskaźnik stanu / predyktor / moderator / kontekst).<br>3. Usunięcie twierdzenia, że CFA na 300-500 osobach wystarcza. |
| **Proponowana poprawka** | 1. `research/hipotezy_badawcze_rev1.md` – restrukturyzacja sekcji walidacji<br>2. `research/model_pomiarowy_rev1.md` – specyfikacja walidacji within-person<br>3. `src/build_document.py` – aktualizacja rozdziału 14, 18 w DOCX |
| **Pliki do aktualizacji** | `research/hipotezy_badawcze_rev1.md`, `research/model_pomiarowy_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy plan badawczy zawiera: wywiady poznawcze, analizę within-person, jawne role itemów. |
| **Status realizacji** | TODO |

---

### C5. Dodawanie zachowania do definicji klas grozi zanieczyszczeniem kryterium (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C5 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 7.3, 14.2, 15.1: ARG5; `research/hipotezy_badawcze.md` (sekcja 3) |
| **Treść zarzutu** | Dokument proponuje ratowanie identyfikowalności dodatkowymi wskaźnikami „zachowanie, afekt, kontekst”, a potem przewidywanie zachowania i afektu ze stanu. Jeżeli wynik współtworzy stan, korelacja stanu z wynikiem nie jest niezależną walidacją. Użycie wygładzonych stanów HMM, oszacowanych także z późniejszych obserwacji, może prowadzić do przecieku informacji. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To klasyczny problem *criterion contamination*. Jeśli zachowanie jest wskaźnikiem klasy latentnej, to nie może być niezależnym kryterium walidacji. Rozwiązanie: (a) stan = tylko W,C,N (bez zachowania); (b) zachowanie = zmienna wynikowa przewidywana ze stanu; (c) w LTA/HMM – emisja tylko z W,C,N; zachowanie jako *dowstream outcome* w modelu strukturalnym. |
| **Decyzja o zmianie** | 1. Stan (klasa latentna) definiowany **wyłącznie** przez W, C, N (wersja ciągła).<br>2. Zachowanie, afekt, kontekst – jako zmienne *eksogenne* (predyktory przejść) lub *wynikowe* (outcome), nie wskaźniki emisji.<br>3. W LTA/HMM: macierz emisji tylko dla W,C,N; zachowanie modelowane w części strukturalnej (regresja na stan latentny). |
| **Proponowana poprawka** | 1. `research/model_pomiarowy_rev1.md` – jasna separacja: wskaźniki stanu (W,C,N) vs predyktory (kontekst) vs wyniki (zachowanie, afekt)<br>2. `research/hipotezy_badawcze_rev1.md` – aktualizacja sekcji modelu pomiarowego<br>3. `src/build_document.py` – aktualizacja rozdziału 14 w DOCX |
| **Pliki do aktualizacji** | `research/model_pomiarowy_rev1.md`, `research/hipotezy_badawcze_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy specyfikacja modelu LTA/HMM nie zawiera zachowania w macierzy emisji. |
| **Status realizacji** | TODO |

---

### C6. HG1 i HG5 nie mają uczciwie zdefiniowanego porównania konkurencyjnego (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C6 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 13.1, 14.2, 19; aneks G; `research/hipotezy_badawcze.md` (HG1, HG5) |
| **Treść zarzutu** | TPB, SDT i COM-B to teorie, a nie pojedyncze modele statystyczne. AIC/BIC modelu klas dla wskaźników WCN nie można porównywać z AIC/BIC regresji innego wyniku na innych zmiennych. Minimalne alternatywy: ostatnie zachowanie + autoregresja; ciągłe W,C,N z interakcjami; pełny model ośmiu konfiguracji bez HPE; prostszy model zmian bitów; operacjonalizowane TPB/SDT/COM-B. Sam profil ośmiu stanów nie daje przewidywań niedostępnych modelom płaskim – dowolne osiem średnich da się odtworzyć regresją z interakcjami. Wkład Q3 musi dotyczyć ograniczeń dynamiki lub efektywności estymacji. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To fundamentalny błąd w logice porównania modeli. HG1 i HG5 w obecnej formie nie są testowalne w sposób uczciwy. Porównanie musi dotyczyć **tego samego wyniku, tych samych danych, tego samego horyzontu**. |
| **Decyzja o zmianie** | 1. HG1: Porównanie **prognozy zachowania** (następne okno EMA) z modelu DMTRD (CTMC/LTA) vs modeli: (a) ciągła regresja W,C,N z interakcjami; (b) model autoregresyjny zachowania; (c) operacjonalizowane TPB/SDT/COM-B na tych samych danych.<br>2. HG5: Test **wartości dodanej topologii Q3** – czy ograniczenie qᵢⱼ=0 dla d_H≥2 poprawia prognozę poza próbą vs model bez tego ograniczenia (24 wolne qᵢⱼ).<br>3. Usunięcie porównania AIC/BIC między modelami o innych zmiennych wynikowych. |
| **Proponowana poprawka** | 1. `research/hipotezy_badawcze_rev1.md` – przepisanie HG1, HG5 z konkretnymi modelami referencyjnymi i wspólnym wynikiem<br>2. `research/hipotezy_badawcze_rev1.md` – dodanie modelu „pełne 8 konfiguracji bez HPE” jako referencyjnego<br>4. `src/build_document.py` – aktualizacja rozdziału 13 w DOCX |
| **Pliki do aktualizacji** | `research/hipotezy_badawcze_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy HG1 i HG5 określają: ten sam wynik, te same dane, te same horyzonty, konkretne modele referencyjne. |
| **Status realizacji** | TODO |

---

### C7. Asymetria intensywności nie identyfikuje asymetrii mechanizmów ani kosztów (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C7 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 5: A4, 7.4, 9.2, 13.1: HG3; `research/hipotezy_badawcze.md` (HG3) |
| **Treść zarzutu** | Nierówność qᵢⱼ ≠ qⱼᵢ mówi o różnych tempach zmian. Nie dowodzi różnych procesów psychologicznych, wysiłku ani kosztu emocjonalnego. Procesy o różnych przyczynach mogą mieć równe tempa. To nie jest równoznaczne z nieodwracalnością. Próg „co najmniej 50% par” nie ma wyprowadzenia. Potrzebne są minimalne istotne naukowo różnice/ilorazy intensywności, przedziały niepewności i odpowiednia moc. Koszty i mechanizmy powinny być mierzone oddzielnie. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Asymetria intensywności (qᵢⱼ ≠ qⱼᵢ) to fakt statystyczny, nie dowód na różne mechanizmy psychologiczne. HG3 w obecnej formie testuje tylko nierówność parametrów, nie interpretację. Próg 50% par jest arbitralny. |
| **Decyzja o zmianie** | 1. HG3: Test statystyczny asymetrii (LRT dla qᵢⱼ = qⱼᵢ) – jako *fakt statystyczny*, nie interpretacja mechanistyczna.<br>2. Interpretacja mechanistyczna (rózne procesy, koszty) – jako **odrębne hipotezy** (H_mech) wymagające osobnego pomiaru mediatorów/moderatorów (np. autonomia, wsparcie, afekt).<br>3. Usunięcie progu 50% par. Zastąpienie: „Istotna asymetria (qᵢⱼ ≠ qⱼᵢ) występuje dla co najmniej jednej pary przejść” + estymacja wielkości efektu (iloraz qᵢⱼ/qⱼᵢ) z przedziałami ufności. |
| **Proponowana poprawka** | 1. `research/hipotezy_badawcze_rev1.md` – przepisanie HG3 i dodanie H_mech jako hipotez eksploracyjnych<br>2. `research/hipotezy_badawcze_rev1.md` – dla każdego przejścia: oddzielenie testu asymetrii q od interpretacji mechanistycznej<br>3. `src/build_document.py` – aktualizacja rozdziału 13 w DOCX |
| **Pliki do aktualizacji** | `research/hipotezy_badawcze_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy HG3 testuje tylko nierówność parametrów, a interpretacje mechanistyczne są oddzielnymi hipotezami. |
| **Status realizacji** | TODO |

---

### C8. H1–H24 nie tworzą 24 poprawnie określonych testów mechanizmów (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C8 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 13, tabela 4; aneks G; `research/hipotezy_badawcze.md` (H1–H24) |
| **Treść zarzutu** | Szczegółowa tabela w recenzji pokazuje błędy: H1–H2 (self-efficacy bliskie C – predyktor bliski wskaźnikowi stanu); H3, H7, H13, H15 („mediuje” bez jednoznacznej ekspozycji/mediatora/wyniku); H4 (101→011 zmienia dwa bity – nie krawędź HPE); H5, H7 (intrinsic motivation/identified regulation pokrywają się z W); H8, H12, H16, H24 (wypalenie, intencja odejścia, PTSD – różne skale czasu, Cox wymaga zdefiniowanego zdarzenia); H16 (błędne kontrasty utraty C); H17, H19–H21 (hipotezy o kolejnym przejściu, nie o krawędzi z nagłówka); H22 (problem identyfikowalności interakcji w podpróbie); H23 (OCB to zachowanie, nie zmiana N). |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Większość H1–H24 ma fundamentalne błędy: utożsamianie predyktora ze stanem, testowanie mechanizmów bez ich pomiaru, testowanie przejść wielobitowych jako krawędzi HPE, arbitralne kontrasty, problemy identyfikowalności. Lista 24 hipotez nie jest gotowym planem badawczym. |
| **Decyzja o zmianie** | **Radikalna redukcja i przepisanie:**<br>1. Wybór **maksymalnie 3 hipotez głównych** do pierwszego badania (zgodnie z rekomendacją Astry: HPE, HPD, HPP).<br>2. Pozostałe 21 hipotez → **hipotezy eksploracyjne** (oznaczone jako takie, nie testowane w głównym wnioskowaniu).<br>3. Dla 3 głównych: pełna specyfikacja (X, M, Y, model, identyfikacja przyczynowa, moc).<br>4. Usunięcie błędnych hipotez (H4 jako krawędź HPE, H16 z błędnymi kontrastami, H22 z problemem identyfikowalności). |
| **Proponowana poprawka** | 1. `research/hipotezy_badawcze_rev1.md` – całkowite przepisanie:<br>   - 3 hipotezy główne (HPE-test, HPD-path dependence, HPP-predykcyjna wartość Q3)<br>   - Tabela hipotez eksploracyjnych (dawniej H1–H24, poprawione i oznaczone jako eksploracyjne)<br>   - Usunięcie błędnych specyfikacji<br>2. `src/build_document.py` – aktualizacja rozdziału 13 w DOCX |
| **Pliki do aktualizacji** | `research/hipotezy_badawcze_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie: czy są dokładnie 3 hipotezy główne z pełną specyfikacją? Czy reszta oznaczona jako eksploracyjna? Czy usunięto błędy H4, H16, H22? |
| **Status realizacji** | TODO |

---

### C9. Plan EMA jest zbyt szeroki i nie dopasowuje rozdzielczości do zjawisk (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C9 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 14.2, 18; aneks G; `research/hipotezy_badawcze.md` (sekcja 3, 4) |
| **Treść zarzutu** | Jedno badanie na 100–150 pracowników lub 200 studentach testuje HPE, 24 hipotezy, asymetrię, mediacje, wypalenie, moral distress i porównanie wielu teorii. Liczba pomiarów ogółem nie gwarantuje informacji o rzadkich stanach i przejściach. Mieszanie ćwiczeń, nauki języka i projektów zawodowych tworzy pozorną heterogeniczność. Odstępy 2–3h nie są z definicji „kluczową” rozdzielczością. Pomiar event-based po działaniu rejestruje skutki wykonania. Plan powinien uwzględniać dokładne znaczniki czasu, przerwy nocne, brak okazji, rezygnację z badania. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | Plan jest nadmiernie ambitny i niedopracowany metodologicznie. Pierwsze badanie EMA powinno być **skupione na jednym typie działania w jednej populacji**, z gęstością próbkowania dopasowaną do skali zmian (pilotaż + symulacje), a nie arbitralnie 2-3h. |
| **Decyzja o zmianie** | 1. Redukcja do **jednego rodzaju powtarzalnego działania w jednej populacji** (np. nauka języka codziennie 15 min, lub aktywność fizyczna 3×/tydzień).<br>2. Gęstość próbkowania: ustalenie w pilotażu + symulacjach (cel: rozdzielenie skoków elementarnych od wielobitowych).<br>3. Event-based EMA: oddzielenie pomiaru *przed* oknem zachowania (predyktor) od pomiaru *po* (skutek).<br>4. Usunięcie mieszania różnych typów działań w jednym badaniu. |
| **Proponowana poprawka** | 1. `research/hipotezy_badawcze_rev1.md` – sekcja „Projekt badania pilotażowego”: redukcja do 1 działania + 1 populacja<br>2. `research/hipotezy_badawcze_rev1.md` – gęstość próbkowania z symulacji, nie arbitralna<br>3. `src/build_document.py` – aktualizacja rozdziału 14, 18 w DOCX |
| **Pliki do aktualizacji** | `research/hipotezy_badawcze_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie: czy plan badawczy dotyczy 1 działania w 1 populacji? Czy gęstość wyznaczona z symulacji? |
| **Status realizacji** | TODO |

---

### C10. Obecne kryteria falsyfikacji nie rozdzielają teorii, pomiaru i implementacji (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | C10 |
| **Priorytet** | MAJOR |
| **Lokalizacja** | Rozdz. 5: A7, 13.1, 15.2; aneks G; `research/hipotezy_badawcze.md` (HG1–HG5) |
| **Treść zarzutu** | Wybór innej liczby klas podważa konkretną reprezentację danych, niekoniecznie użyteczność trzech pytań. Brak przewagi predykcyjnej może podważyć HG1/HG5, ale nie samą logiczną możliwość ośmiu kodów. Korelacja z MDS nie dowodzi równoważności z moral distress. Należy wskazać, co dokładnie zostaje odrzucone przy każdym wyniku. Rozbudowywanie modelu po każdym niepowodzeniu może uczynić DMTRD niewrażliwym na obalenie. Wersja potwierdzająca powinna mieć zamknięty zestaw głównych przewidywań. |
| **Własna ocena** | **ACCEPT** |
| **Argumentacja** | To problem *immunizacji teorii* – elastyczność modelu (liczba stanów, progi, moderatory, pamięć) pozwala dopasować się do dowolnych danych. Należy zdefiniować **wersję potwierdzającą (confirmatory version)** z zamkniętym zestawem przewidywań, modelu pomiarowego i kryteriów odrzucenia. |
| **Decyzja o zmianie** | 1. Definicja **DMTRD-core (wersja potwierdzająca)**: zamknięty zestaw 3 głównych hipotez, model pomiarowy (ciągły W,C,N, CTMC z HPE), model alternatywny (bez HPE), kryteria sukcesu/odrzucenia, reguły nierozstrzygającego wyniku.<br>2. Wszelkie rozszerzenia (wersja ciągła vs binarna, parametry H, I, A, path dependence) – jako **wersje eksploracyjne**, testowane oddzielnie, nie ratujące wersję core.<br>3. Jawne spisanie: co zostaje odrzucone przy każdym wyniku (np. odrzucenie HPE-core = odrzucenie HPE-model; brak przewagi predykcyjnej = odrzucenie HPP; brak identyfikowalności = ponowna specyfikacja modelu pomiarowego, nie dodanie wymiarów). |
| **Proponowana poprawka** | 1. `research/hipotezy_badawcze_rev1.md` – sekcja „DMTRD-core: wersja potwierczająca”<br>2. `research/hipotezy_badawcze_rev1.md` – tabela: wynik testu → co odrzucamy / co modyfikujemy<br>3. `src/build_document.py` – aktualizacja rozdziału 13, 15 w DOCX |
| **Pliki do aktualizacji** | `research/hipotezy_badawcze_rev1.md`, `src/build_document.py`, `DMTRD_koncepcja.docx` |
| **Metoda weryfikacji** | Sprawdzenie, czy dokument zawiera zamkniętą definicję DMTRD-core z kryteriami odrzucenia. |
| **Status realizacji** | TODO |

---

## SEKCJA D – ZAŁOŻENIA NIEPODPARTE DOWODAMI

*(Recenzent wymienia 10 założeń. Oceniamy każde jako ACCEPT – są to hipotezy, nie ustalenia. Decyzja: jawne oznaczenie ich jako hipotez w dokumencie, usunięcie sformułowań sugerujących pewność.)*

| Założenie | Ocena | Decyzja |
|-----------|-------|---------|
| W,C,N wystarczają do opisania dynamiki | ACCEPT | Oznaczenie jako hipoteza H_scope; test porównawczy z modelami rozszerzonymi (H, I, A) |
| Elementarna zmiana = 1 wymiar | ACCEPT | To HPE-model (ograniczenie Q), nie fakt psychologiczny |
| 101 = „najbardziej napięty” / „czasowa bomba” | ACCEPT | Hipoteza H_101_tension; test porównawczy z 001, 011 |
| 111 z internalizowanym N > 110 | ACCEPT | Hipoteza H_111_quality; wymaga pomiaru N_source |
| Wzrost W/C = dodatni afekt, spadek = ujemny | PARTIAL | Hipoteza H_affect_valence; test dwukierunkowy (ulga przy rezygnacji z nieosiągalnego celu) |
| Wzrost C = mały koszt, utrata C = wysoki koszt/PTSD | REJECT | „Koszt” to metafora; usunięcie lub jawne oznaczenie jako metafora + hipoteza H_cost z pomiarem |
| N=1 ułatwia wzrost W | ACCEPT | Hipoteza H_N_facilitates_W; test z moderatorem autonomy support |
| Asymetria q w ≥50% par | REJECT | Usunięcie progu 50%; test LRT dla każdej pary + estymacja wielkości efektu |
| Wskaźniki ciągłe = identyfikowalne HMM/LTA | ACCEPT | To zależy od specyfikacji; jawna specyfikacja modelu pomiarowego (G3) |
| 40-50% działań nawykowych = większość | PARTIAL | Usunięcie twierdzenia „większość”; jawne ograniczenie zakresu modelu (System 2) |

---

## SEKCJA E – ELEMENTY OPISANE WCZEŚNIEJ I ZGODNOŚĆ Z LITERATURĄ

### E1. Trzy grupy determinant nie stanowią nowej teorii (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | E1 |
| **Priorytet** | MAJOR |
| **Ocena** | **ACCEPT** |
| **Argumentacja** | Recenzent ma rację: TPB, SDT, COM-B, SCT, Rubikon, samoregulacja, moral distress, modele wielostanowe – wszystkie zawierają elementy bliskie W, C, N. Nowość DMTRD nie leży w *istnieniu* trzech determinant, ale w *formalizacji topologii Q3 + HPE + asymetrii + zależności od historii* jako spójnego modelu dynamiki. |
| **Decyzja** | Usunięcie twierdzeń o nowości „trzech filarów”. Przeniesienie nacisku na: Q3 jako topologia stanów, HPE jako ograniczenie dynamiki, asymetria przejść, path dependence. W sekcji 6 (DOCX) – jawne mapowanie na istniejące teorie z podziałem na: (a) co jest redukcją/renomowaniem, (b) co jest nową formalizacją. |
| **Pliki** | `src/build_document.py` (rozdz. 6), `DMTRD_koncepcja.docx` |

### E2. Formalizm pojedynczych zmian lokalnych ma precedensy (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | E2 |
| **Priorytet** | MAJOR |
| **Ocena** | **ACCEPT** |
| **Argumentacja** | Nodelman, Shelton, Koller (2002) – Continuous Time Bayesian Networks (CTBN) – to matematycznie ten sam formalizm: zmienne binarne, lokalne zmiany, intensywności zależne od konfiguracji pozostałych zmiennych. Q3 z 24 intensywnościami to szczególny przypadek CTBN dla 3 zmiennych. Nowość nie leży w formalizmie, ale w *psychologicznym doborze zmiennych (W,C,N) i interpretacji parametrów*. |
| **Decyzja** | Dodanie cytowania Nodelman et al. (2002) do bibliografii i `model/definicje.md`. Usunięcie twierdzenia o nowości formalizmu Q3/24 intensywności. Przeniesienie nacisku na: psychologiczny dobór W,C,N, interpretacja asymetrii qᵢⱼ, przewidywania interwencyjne. |
| **Pliki** | `model/definicje.md`, `research/bibliografia.bib`, `src/build_document.py` |

### E3. Deklaracja aktualności literatury szersza od wykazanego pokrycia (MAJOR)

| Pole | Wartość |
|------|---------|
| **Identyfikator ASTRA** | E3 |
| **Priorytet** | MAJOR |
| **Ocena** | **ACCEPT** |
| **Argumentacja** | Bibliografia kończy się na 2016 r., a dokument deklaruje literaturę do 11.2026. Recenzent wskazuje brakujące prace: metaanaliza SDT 2017, synteza moral distress 2019, SDT 2020, Sheeran et al. 2016 (już jest, ale trzeba sprawdzić DOI). |
| **Decyzja** | 1. Aktualizacja bibliografii do 11.2026 (wyszukanie kluczowych prac 2017-2026: SDT, TPB, COM-B, moral distress, CTMC/HMM w psychologii, EMA, LTA).<br>2. Sprawdzenie i poprawa DOI (szczególnie Corley et al. 2001 – recenzent wskazuje błędny DOI).<br>3. Usunięcie deklaracji „literatura do 11.2026” jeśli nie uda się zweryfikować dostępu do pełnych tekstów. |
| **Pliki** | `research/bibliografia.bib`, `research/zrodla.csv`, `src/build_document.py` |

---

## SEKCJA F – ELEMENTY POTENCJALNIE ORYGINALNE

| Element | Ocena | Status |
|---------|-------|--------|
| F1. Oszczędny model trajektorii WCN | **POTENCJALNA ORYGINALNOŚĆ** | Zachować jako hipotezę HPP (wartość predykcyjna Q3) |
| F2. Kontekstowe przewidywania o drogach zmiany | **POTENCJALNA ORYGINALNOŚĆ** | Zachować jako hipotezę HPD (path dependence) |
| F3. Falsyfikowalne ograniczenia po interwencjach | **POTENCJALNA ORYGINALNOŚĆ** | Zachować jako kierunek badawczy (Etap 5+) |

**Decyzja:** Nie deklarować oryginalności jako faktu. Używać kategorii: ORYGINALNOŚĆ UDOKUMENTOWANA / POTENCJALNA / BRAK PODSTAW.

---

## SEKCJA G – ZMIANY NIEZBĘDNE PRZED BADANIAMI

| ID | Zmiana | Status | Priorytet |
|----|--------|--------|-----------|
| G1 | Ustalić jedno znaczenie W, C, N | **TODO** | CRITICAL |
| G2 | Zdefiniować jednostkę analizy i zakres | **TODO** | MAJOR |
| G3 | Wybrać podstawowy model pomiaru i stanów | **TODO** | CRITICAL |
| G4 | Uzgodnić HPE z planem testu | **TODO** | CRITICAL |
| G5 | Oddzielić kody, mechanizmy i skutki | **TODO** | MAJOR |
| G6 | Ograniczyć badanie do kilku rozstrzygających hipotez | **TODO** | MAJOR |
| G7 | Ustalić porównania konkurencyjne i walidację | **TODO** | MAJOR |
| G8 | Dopasować EMA i analizę mocy do informacji o przejściach | **TODO** | MAJOR |
| G9 | Poprawić konkretne hipotezy i źródła | **TODO** | MAJOR |

---

## SEKCJA H – ZMIANY POŻĄDANE, ALE NIEKONIECZNE DO PIERWSZEGO BADANIA

| Uwaga | Decyzja |
|-------|---------|
| Diagram oddzielający stan, wskaźniki, predyktory, zachowanie | **TODO** (MINOR) – do `model/definicje.md` i DOCX |
| Wersja semi-Markowska / jawna historia po porównaniu z modelem podstawowym | **DEFERRED** (MAJOR) – do Etapu 3+ |
| Replikacja w innym kontekście i kulturze | **DEFERRED** (MAJOR) – do Etapu 4+ |
| Miara kosztu oddzielająca wysiłek, afekt, alternatywy, czas | **DEFERRED** (MAJOR) – do Etapu 3+ |
| Doprecyzowanie parametrów pochodnych (−q_ii vs czas trwania) | **TODO** (MINOR) – `model/definicje.md` |

---

## SEKCJA I – KONTROLA JAKOŚCI (ETAP 15 ZADANIA)

| Kryterium | Ocena | Uzasadnienie |
|-----------|-------|--------------|
| A. Wszystkie uwagi CRITICAL rozpatrzone? | **PARTIAL** | 4/4 CRITICAL (B1, B2, B8, C1, C2) – wszystkie zaakceptowane, ale nie zaimplementowane |
| B. Wyeliminowano sprzeczności definicji W, C, N? | **NO** | Wymaga implementacji G1 |
| C. HPE posiada poprawną formalizację? | **PARTIAL** | Formalizacja CTMC poprawna, ale HPE-empiryczna wymaga przepisania (C1) |
| D. Zaproponowano rzetelny test HPE? | **NO** | Obecny plan LTA błędny (C1); wymaga testu CTMC (G4) |
| E. Model pomiarowy jednoznacznie określony? | **NO** | Wymaga G3 |
| F. Przejścia nie utożsamione z mechanizmami? | **NO** | Wymaga G5 (B7) |
| G. Hipotezy falsyfikowalne? | **PARTIAL** | 24 hipotezy zawierają błędy (C8); wymaga redukcji do 3 głównych (G6) |
| H. Bibliografia wiarygodna? | **PARTIAL** | Wymaga aktualizacji do 2026, poprawy DOI (E3) |
| I. Błędy matematyczne poprawione? | **PARTIAL** | Cykl 4-elementowy w validate_model.py (I); HPE-test (C1) |
| J. Spójność DOCX, MD, CSV, GraphML? | **PARTIAL** | Wymaga regeneracji DOCX po zmianach w CSV/MD |
| K. Oryginalne dokumenty nienaruszone? | **YES** | Praca na gałęzi roboczej, oryginały zachowane |
| L. Testy automatyczne uruchomione? | **YES** | validate_model.py: PASS (0 błędów) |
| M. DOCX otwiera się i ma poprawną strukturę? | **UNVERIFIED** | Wymaga regeneracji i weryfikacji |
| N. Nadaje się do przekazania recenzentowi? | **NO** | Wymaga wdrożenia zmian CRITICAL/MAJOR |

---

## PODSUMOWANIE STATYSTYCZNE

| Kategoria | Liczba |
|-----------|--------|
| **CRITICAL** (zaakceptowane) | 5 (B1, B2, B8, C1, C2) |
| **MAJOR** (zaakceptowane) | 12 (B3, B4, B5, B6, B7, B9, B10, B11, C3, C4, C5, C6, C7, C8, C9, C10, E1, E2, E3, G2, G3, G5, G6, G7, G8, G9) |
| **MINOR** (zaakceptowane) | 3 (I, H, G9 – doprecyzowanie parametrów) |
| **PARTIAL** | 3 (B4, D – założeń) |
| **REJECT** | 2 (D – koszt/PTSD, asymetria 50%) |
| **UNRESOLVED** | 0 |

**Łącznie pozycji w macierzy:** ~50

---

## KOLEJNOŚĆ REALIZACJI (KRYTYCZNA ŚCIEŻKA)

1. **G1** – Definicje W, C, N (wpływa na wszystko)
2. **G3** – Model pomiarowy (wpływa na plan badawczy)
3. **G4** – HPE-test (CTMC, nie LTA)
4. **B7 / G5** – Separacja kodów / mechanizmów / skutków w przejściach
5. **G6** – Redukcja hipotez do 3 głównych
6. **G7** – Porównania konkurencyjne (HG1, HG5)
7. **G2** – Jednostka analizy (1 działanie, 1 populacja)
8. **G8** – Dopasowanie EMA (symulacje, gęstość)
9. **G9** – Poprawa hipotez i bibliografii
10. **Regeneracja DOCX, GraphML, walidacja**

---

*Koniec macierzy. Dokument będzie aktualizowany w trakcie realizacji prac.*