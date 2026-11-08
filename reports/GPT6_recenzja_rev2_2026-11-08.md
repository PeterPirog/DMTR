# DMTRD — niezależna recenzja naukowa rev2 (GPT-6)

**Data:** 2026-11-08  
**Przedmiot:** Dynamiczny Model Trójwymiarowej Regulacji Działania (DMTRD)  
**Repozytorium:** PeterPirog/DMTR  
**Recenzowany commit:** df0d4041c55a6a170b8173fba018b3fa0d224d88  
**Gałąź autora:** research/dmtrd-rev1-critical  
**Powiązany PR:** #1, rev2: Scientific consistency audit  
**Rodzaj oceny:** niezależna recenzja koncepcyjna, metodologiczna i audyt wybranych implementacji  
**Werdykt:** **MAJOR REVISION REQUIRED**  
**Recenzja opublikowana niezależnie od gałęzi autora; nie jest aprobatą PR #1 ani walidacją empiryczną.**

## 1. Zakres, metoda i ograniczenia recenzji

Oceniono źródła tekstowe w gałęzi: definicje i formalizację HPE, model pomiarowy, operacjonalizację WCN, hipotezy badawcze, raporty autora, macierz odpowiedzi na wcześniejszą recenzję, generatory DOCX, walidator DOCX oraz symulator CTMC. Skonfrontowano wybrane twierdzenia z publikacjami o CTBN, modelach wielostanowych z obserwacjami panelowymi i teorią autodeterminacji.

**Ograniczenie dostępu:** nie wykonano niezależnego odczytu kompletnego binarnego pliku DMTRD_koncepcja_rev2.docx ani renderingu wszystkich stron. Ocena treści dokumentu wynikowego opiera się na jego publicznym generatorze, tekstowych źródłach i raporcie walidacji autora. W konsekwencji nie potwierdzam wizualnej jakości Worda ani tego, że wszystkie fragmenty gotowego DOCX są identyczne z analizowanymi źródłami. Nie wykonywano również pełnej replikacji kodu w środowisku autora. Uwagi do kodu oparte na wskazanych fragmentach zostały zweryfikowane przez analizę algorytmiczną.

Status PASS w raportach autora dotyczy deklarowanych kontroli technicznych; nie dowodzi trafności konstruktu, identyfikowalności statystycznej ani wartości predykcyjnej teorii.

## 2. Streszczenie oceny

Podstawowa idea rozdzielenia osobistej aprobaty celu (W), postrzeganej wykonalności (C) i poczucia zobowiązania (N) jest koncepcyjnie komunikatywna i może posłużyć do badań eksploracyjnych. Reprezentacja ośmiu stanów i 24 kierunkowych zmian jednego bitu jest matematycznie spójna jako graf Q3. Rozdzielenie stanów od faktycznego zachowania, oznaczanie mechanizmów jako hipotez oraz odróżnienie generatora Q od P(delta t) są ważnymi ulepszeniami.

Nie wykazano jednak, że HPE jest swoistym prawem psychologicznym, że istnieje jednoznaczny model obserwacji WCN ani że dostępne dane EMA pozwolą odróżnić skoki wielobitowe od wielokrotnych skoków niewidocznych między pomiarami i błędów klasyfikacji. Implementacja symulacji zawiera jednoznaczny błąd indeksowania, a deklaracje gotowości do prerejestracji są przedwczesne.

**Rekomendacja:** rozwinąć DMTRD jako ostrożnie sformułowany model integracyjny i program hipotez, nie nazywać go empirycznie potwierdzoną teorią. Można skierować wersję koncepcyjną do psychologa w celu konsultacji, z tą recenzją i jawnym wykazem ograniczeń. Nie należy jeszcze prerejestrować wszystkich trzech hipotez jako gotowego planu badawczego.

## 3. Uwagi CRITICAL (blokują zatwierdzenie rev2 jako spójnej specyfikacji)

### CR-01. Błąd przesunięcia stanów w symulatorze CTMC — błąd wyników

**Lokalizacja:** src/hpe_simulation.py, funkcja simulate_ctmc, około wierszy 125–136.

Algorytm przechowuje jump_states = [stan_początkowy, stan_po_1_skoku, stan_po_2_skoku, ...] oraz jump_times = [t_1, t_2, ...]. Dla obserwacji t > t_1 i t < t_2 używa indeksu searchsorted(jump_times,t,side='right') - 1, przez co wybiera jump_states[0], czyli STAN SPRZED pierwszego skoku. Analogicznie każda późniejsza obserwacja jest opóźniona o jeden skok. Przy dokładnym czasie skoku otrzymujemy ten sam problem.

**Poprawny indeks przy obecnej konwencji:** k = searchsorted(jump_times,t,side='right'); stan = jump_states[k]. Warunkiem jest spójna konwencja wartości lewostronnych/prawostronnych w chwili skoku.

**Przykład deterministyczny:** jump_times=[0.2,0.4], jump_states=[0,1,2]. Dla t=0.3 poprawny stan wynosi 1, a obecny kod zwraca 0. Dla t=0.5 poprawny stan wynosi 2, kod zwraca 1.

**Konsekwencja:** statystyki bazujące na symulowanych trajektoriach, w tym demonstracja d_H>=2, nie mogą być przyjmowane jako niezależnie zwalidowane, zanim błąd zostanie usunięty. Sam analityczny wzór dla symetrycznych niezależnych bitów jest odrębną kwestią i może być poprawny.

**Wymagany dowód naprawy:** test jednostkowy znanego harmonogramu skoków oraz empiryczna zgodność P_hat(delta t) z exp(Q delta t) w granicach błędu Monte Carlo dla kilku macierzy Q i interwałów.

### CR-02. Brak jednoznacznie wyprowadzonego procesu obserwacyjnego i ryzyko niewłaściwej własności Markowa

**Lokalizacja:** research/model_pomiarowy_rev1.md, sekcje 1.1, 1.3, 2.1 i 3.1–3.3; research/operacjonalizacja_WCN_rev1.md.

Dokument równocześnie nazywa siedmiopunktową skalę Likerta modelem „ciągłym bazowym”, dychotomizację tylko wizualizacją oraz dyskretyzację częścią estymacji ośmiostanowego CTMC. To trzy nieekwiwalentne stwierdzenia. Skala Likerta ma pojedyncze kategorie uporządkowane; jej aproksymacja ciągła jest wyborem analitycznym wymagającym uzasadnienia.

Co więcej, q_ij(X_t) dopuszcza w X_t bieżące wartości ciągłe W,C,N, które jednocześnie WYZNACZAJĄ skategoryzowany stan S_t. Wtedy same osiem kodów WCN nie musi stanowić pełnego stanu Markowa: intensywności w obrębie tego samego kodu mogą zależeć od położenia względem progów i historii nieobserwowanych wartości. Nie wolno nazywać tej sytuacji prostym jednorodnym CTMC na 8 stanach bez określenia procesu kowariancji / powiększonego stanu.

**Wymagana korekta:** rozdzielić (i) model konstruktu i pomiaru, (ii) model dynamiki stanów, (iii) zmienne zewnętrzne i zależne czasowo, (iv) model zachowania. Wybrać jeden prosty model PRIMARY do pilotażu, a resztę oznaczyć jako modele konkurencyjne / czułości. Rozważyć wariant bazowy 8-stanowy z kategoryzacją zgodną z prerejestrowaną regułą oraz oddzielny model porządkowy/ciągły bez utożsamiania ich parametrów.

**Wymagany dowód naprawy:** kompletny schemat probabilistyczny i opis obserwowanych/latentnych zmiennych oraz identyfikowalności, w tym model błędu klasyfikacji.

### CR-03. HPE nie zostało wyizolowane jako właściwość psychologiczna od artefaktu konstrukcji matematycznej

**Lokalizacja:** model/HPE_formalizacja_rev1.md, sekcje 1–3; research/HPE_testowalnosc_rev1.md; research/hipotezy_badawcze_rev1.md.

W CTBN asynchroniczna zmiana pojedynczej zmiennej przy skoku elementarnym stanowi znaną reprezentację matematyczną (Nodelman, Shelton, Koller, 2002). Również gdy trzy procesy bazowe mają trajektorie ciągłe i odpowiednio regularne, przejścia pomiędzy ośmioma obszarami wyznaczonymi progami na ogół przecinają jedną granicę naraz; zmiana jednego bitu może być więc konsekwencją progowania, a nie niezależną teorią motywacji. Przy przebiegach nieregularnych, skokach wspólnych i błędach pomiaru sytuacja jest odmienna.

Samo wykazanie P(d_H>=2)>0 po czasie delta t przy generatorze Q z krawędziami Q3 jest poprawną własnością CTMC, ale nie rozstrzyga, czy psychika zmienia jeden wymiar na raz. Opis HPE-empirycznej jako obserwowanego odsetka zmian wielobitowych „mniejszego od alternatywy” jest nieuniwersalny — częstości zależą od intensywności, delta t i jakości pomiaru; M_indep jest podmodelem M_HPE, nie alternatywą naruszającą HPE.

**Wymagana korekta:** oddzielić HPE-topologię (definicja modelu), HPE-statystyczną (ograniczenie generatora Q w przyjętej rodzinie modeli) oraz HPE-mechanistyczną (odrębny twierdzenie psychologiczne, dziś nieudowodnione). Zaprojektować falsyfikator i model alternatywny obejmujący skoki wielobitowe, wspólne przyczyny i błąd pomiaru; określić, czego nie da się z danych panelowych zidentyfikować.

## 4. Uwagi MAJOR (istotne przed prerejestracją i kolejną formalną oceną)

### MJ-01. Hipoteza HPE nadal ma niewłaściwe kryterium pozytywnej weryfikacji

**Lokalizacja:** research/hipotezy_badawcze_rev1.md, tabela 3 hipotez; src/build_document.py, tabela hipotez.

Tekst wyjaśniający słusznie zauważa, że nieistotny LRT nie dowodzi HPE, ale w tabeli przy HPE wymieniono „LRT n.s. (p>0.05)” jako warunek sukcesu. To nadal wprowadza logiczną sprzeczność. AIC i różnice log-loss są innymi rodzajami dowodu; wartości graniczne wymagają uzasadnienia, a parametry zerowe są na brzegu przestrzeni parametrów, więc klasyczny asymptotyczny rozkład LRT nie musi obowiązywać.

**Naprawa:** jawne rozdzielenie odrzucenia ograniczenia, nieodrzucenia i predykcyjnej adekwatności; ewentualnie prerejestrowany margines dopuszczalnej straty predykcyjnej, bootstrap parametryczny / inna poprawna kalibracja.

### MJ-02. HPP porównuje niejednoznaczne modele i wyniki

**Lokalizacja:** research/hipotezy_badawcze_rev1.md, wiersz HPP; src/build_document.py (tabela hipotez).

„8 stanów bez HPE z 24 intensywnościami” nie odpowiada swobodnemu, jednorodnemu generatorowi 8-stanowemu, który ma 8×7=56 potencjalnych intensywności poza przekątną. Model z 24 intensywnościami może być szczególną konstrukcją, ale wówczas musi mieć jawnie podane ograniczenia. Ujednolicić porównania na ten sam horyzont, wynik, reprezentację cech i zbiór danych; oddzielić przewidywanie przyszłych stanów od przewidywania działania.

### MJ-03. HPD nie może być bez zastrzeżeń warunkiem poprawności bazowego modelu Markowa

**Lokalizacja:** research/hipotezy_badawcze_rev1.md, HPD i „kryteria odrzucenia DMTRD-core”.

Zależność od historii wykracza poza jednorodny 8-stanowy CTMC. Pozorna pamięć może wynikać z heterogeniczności między osobami, nieobserwowanej kowariancji, błędu pomiaru, czasu przebywania w stanie i wyboru progu, a nie z psychologicznej path dependence. Różne modele mogą nie być zagnieżdżone; zatem proste LRT i arbitralne progi nie wystarczą.

**Naprawa:** traktować HPD jako test osobnej hipotezy rozszerzającej, stosować modele z random effects/latent heterogeneity, semi-Markov i modele czułości, nie odrzucać automatycznie całego DMTRD po niepowodzeniu HPD.

### MJ-04. Trafność różnicowa W i N jest zagrożona na poziomie pozycji kwestionariuszowych

**Lokalizacja:** research/operacjonalizacja_WCN_rev1.md, sekcja 2.2, dodatkowy item W nr 3.

Zdanie „Zgadzam się z tym, że ten cel powinien zostać zrealizowany” mierzy powinność, aprobatę normy lub ocenę normatywną, a nie jednoznacznie osobistą akceptację wartości. Sztuczna korelacja W–N może wynikać ze wspólnego brzmienia itemów. C również łączy zdolność i zasoby zewnętrzne. Nie ustalono trafności różnicowej ani niezmienniczości pomiaru w czasie.

**Naprawa:** stworzyć macierz treściową itemów, przeprowadzić wywiady poznawcze, wstępne analizy czynnikowe z odpowiednim traktowaniem danych porządkowych, ocenić dyskryminacyjność W/N i oddzielić C od jego przyczyn w analizach pomocniczych.

### MJ-05. Binarna klasyfikacja neutralności i progu jest decyzją badawczą, nie prawem motywacji

**Lokalizacja:** research/operacjonalizacja_WCN_rev1.md, reguła >4 i „4 jako 0 lub wykluczona”; research/model_pomiarowy_rev1.md nadal deklaruje >=4.

W różnych plikach pozostają NIEZGODNE reguły progowania. Przytrzymanie wartości 4 w kategorii 0 nie jest równoważne pominięciu jej w modelu; może wprowadzić systematyczny błąd oraz utratę obserwacji. Przy przełączaniu wokół progu powstaną pozorne przejścia, a modele stanów progowych wyznaczone z procesu ciągłego nie muszą mieć wykładniczego czasu pobytu.

**Naprawa:** pojedyncza specyfikacja progowania i protokół czułości (>=4, >4, strefa niepewności, model porządkowy), bez mieszania definicji w DOCX/MD/CSV.

### MJ-06. Kod symulacyjno-estymacyjny nie uzasadnia deklaracji „gotowe do badań” 

**Lokalizacja:** src/hpe_simulation.py, build_Q_full, estimate_Q_from_P, lrt_test, run_power_simulation i run_simulation_demo; reports/DMTRD_rev2_consistency_audit.md.

- build_Q_full przyjmuje parametr rates, ale generuje z góry ustalone intensywności; może mylić użytkownika API.
- estimate_Q_from_P wykorzystuje logm(P), po czym obcina wartości ujemne i wymusza przekątną; taki zabieg nie jest generalnie poprawnym estymatorem generatora CTMC i może ukrywać problem osadzalności (embeddability).
- lrt_test poprawnie zgłasza NotImplementedError, lecz NIE realizuje testu inferencyjnego.
- run_power_simulation jest jawnie placeholderem i nie wyznacza mocy.
- run_simulation_demo ma argumenty dt i T, ale w wywołaniu symulatora używa stałych 0.5 i 24.
- nie przedstawiono testów regresyjnych wychwytujących CR-01.

**Naprawa:** wprowadzić jeden naprawdę działający, przetestowany pipeline symulacji i estymacji albo jawnie ograniczyć zakres do demonstracji; nie wyliczać pozornej mocy i nie raportować prób pozorujących wyniki LRT.

### MJ-07. Walidator DOCX nie stanowi rygorystycznego bramkowania naukowego

**Lokalizacja:** src/validate_docx.py, check_24_transitions i check_q3_diagram.

check_24_transitions() zwraca True, gdy znaleziono >20, a nie wszystkie 24 przejścia. check_q3_diagram() może zwrócić True na podstawie samego odwołania tekstowego bez osadzonej grafiki. Sama obecność kodów, nazw hipotez i bibliografii nie dowodzi poprawności semantycznej.

**Naprawa:** oddzielić testy strukturalne od semantycznych, wymagać dokładnie 24/24, obecności diagramu oraz kontrprzykładów treściowych, wykorzystać testy regresyjne dla znanych błędów.

### MJ-08. Raport PASS ma zakres szerszy niż udokumentowana walidacja

**Lokalizacja:** reports/DMTRD_rev2_consistency_audit.md, sekcje 5–10.

Raport stwierdza PASS dla „validation of scientific claims” i gotowość HPE, HPD, HPP do prerejestracji, choć analiza kodu i hipotez ujawnia nierozwiązane zagadnienia. Poprawność geometrii Q3 nie implikuje poprawności psychologii, a brak niezależnej walidacji bibliografii pozostaje jawnym ograniczeniem.

**Naprawa:** zmienić status ocen naukowych i inferencyjnych na PARTIAL/UNVERIFIED do uzyskania dowodów; rozdzielić concept-review ready od preregistration ready.

### MJ-09. Problemy w interpretacji stanów i etykietach 

**Lokalizacja:** src/build_reviewer_doc.py, interpretacje 100, 101, 110 oraz przykłady.

W=1 zostało w rev2 określone jako akceptacja wartości, nie chwilowe pragnienie ani koniecznie autonomiczna motywacja. Etykiety „Pragnienie”, „napięcie krytyczne”, „wypalenie” i powiązania ze zjawiskami klinicznymi mogą sugerować więcej niż wynika z konfiguracji bitów. Moral distress wymaga kontekstu moralnego, nie wynika z samego 101. Proponuję neutralne nazwy podstawowe i interpretacje jedynie jako możliwe, wyraźnie warunkowe.

## 5. Uwagi MINOR

**MN-01.** Nazwy i wersje źródeł pozostają mylące: dokumenty rev2 odwołują się do plików *_rev1.md. W README dodać mapę stanu wersji i kanonicznych źródeł.  
**MN-02.** Nazwa „teoria” jest przedwczesna. Preferować „model koncepcyjny / program badawczy” do czasu walidacji.  
**MN-03.** W dokumentacji zastąpić deklaracje „przewidywane korelacje r>0.6” jako warunki faktograficzne przez jawne hipotezy z uzasadnieniem; unikać nieuzasadnionej precyzji.  
**MN-04.** Nie używać terminu „System 2” jako literalnego zakresu modelu bez uzasadnionego mapowania na uznaną teorię procesów poznawczych.

## 6. Ocena oryginalności

Oryginalność grafu Q3, 24 krawędzi kierunkowych ani samej asynchroniczności skoków nie została wykazana; matematyczna rodzina CTBN jest wcześniejsza. Częściowo pokrewne konstrukty są obecne w TPB, SDT i COM-B. Potencjalny wkład DMTRD może leżeć w (a) przejrzystej operacjonalizacji odrębnych ocen W/C/N, (b) testowalnych interakcjach dotyczących kierunkowych zmian, (c) konsekwencjach ścieżek dojścia do tego samego stanu, (d) dopasowaniu interwencji do konfiguracji. Jest to HIPOTEZA o wartości dodatkowej, nie wynik badań.

Kluczowy falsyfikator: czy po porównaniu z dobrze skonstruowanym modelem ciągłym/porządkowym i dynamicznymi modelami alternatywnymi topologia Q3 poprawia predykcję zachowania albo trajektorii stanów w nowych danych, przy właściwej walidacji panelowej?

## 7. Ocena gotowości

| Obszar | Ocena |
| --- | --- |
| Przydatność jako narzędzie konceptualizacji | POTENCJALNIE TAK |
| Spójność topologii Q3 | TAK (matematyczna) |
| Trafność konstruktu W/C/N | NIEZWERYFIKOWANA |
| Empiryczne potwierdzenie HPE | BRAK |
| Poprawność całego kodu symulacyjnego | NIE, wykryto CR-01 |
| Gotowość statystycznej procedury inferencyjnej | NIE |
| Gotowość do prerejestracji testów HPE/HPD/HPP | NIE |
| Gotowość do rozmowy z psychologiem | WARUNKOWO TAK, z recenzją i zastrzeżeniami |
| Zgoda na merge PR #1 w obecnym stanie | NIE REKOMENDUJĘ |

**Werdykt końcowy: MAJOR REVISION REQUIRED.** Nie jest to odrzucenie idei DMTRD, lecz konieczność usunięcia usterek technicznych i doprecyzowania rozstrzygających założeń, zanim autor będzie deklarował kompletność wersji rev2.

## 8. Plan odpowiedzi autora i kryteria akceptacji rewizji rev3

**Gate K1 (blokujący):** testem deterministycznym zrekonstruować i naprawić przesunięcie stanów w simulate_ctmc; pokazać Monte Carlo vs exp(Q delta t); testy wykonane, nie tylko napisane.

**Gate K2 (blokujący):** wybrać jeden PRIMARY model pomiarowo-dynamiczny, jawnie zdefiniować progi, niepewność oraz kowariancje; dołączyć DAG/schemat zależności oraz model likelihood/estymacji. Alternatywy zachować jako sensitivity/competing models.

**Gate K3 (blokujący):** oddzielić HPE jako topologię, restrykcję statystyczną i interpretację mechanistyczną; zaproponować co najmniej jeden test rzeczywiście różnicujący model, uwzględnić CTBN i klasę procesów progowych.

**Gate K4:** usunąć sprzeczne kryteria LRT i niespójne definicje M_full/M_indep, HPP; zapisać rozłączne i obserwowalne kryteria wyniku dodatniego, ujemnego i nierozstrzygającego.

**Gate K5:** poprawić instrument W/N, zapewnić psychometrycznie poprawną procedurę planowania walidacji i analizę progowania 4.

**Gate K6:** rozdzielić HPD od podstawowego założenia Markowa, a predykcję stanu od predykcji zachowania.

**Gate K7:** naprawić rygor walidatora DOCX (wymagaj 24/24 + rzeczywiście osadzonego obrazu), zredukować błędne deklaracje PASS.

**Gate K8:** przygotować pełny DMTRD_koncepcja_rev3.docx i streszczenie dla recenzenta rev3; odtworzyć je z aktualnych źródeł, sprawdzić z użyciem generatorów oraz jeśli dostępny jest renderer — wizualnie.

**Gate K9:** dla każdego punktu CR/MJ sporządzić matrycę Author Response: ACCEPT/PARTIAL/REJECT, uzasadnienie, dokładna lokalizacja zmiany, dowód testu. Nie poprawiać ani nie nadpisywać tej recenzji.

**Gate K10:** aktualizować tylko gałąź roboczą autora i PR #1, nie scalać bez następnego niezależnego audytu.

## 9. Najistotniejsze źródła do dalszej analizy

1. Nodelman, U., Shelton, C. R., & Koller, D. (2002). Continuous Time Bayesian Networks. UAI. https://ai.stanford.edu/~nodelman/papers/ctbn.html
2. Jackson, C. H. (2011). Multi-State Models for Panel Data: The msm Package for R. Journal of Statistical Software, 38(8). https://doi.org/10.18637/jss.v038.i08
3. Fitting and Interpreting Continuous-Time Latent Markov Models for Panel Data. https://pmc.ncbi.nlm.nih.gov/articles/PMC3795797/
4. Self-Determination Theory and Workplace Outcomes: A Meta-Analysis (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC12887546/
5. Ryan, R. M., & Deci, E. L. (2017). Self-Determination Theory: Basic Psychological Needs in Motivation, Development, and Wellness. Guilford Press.

Źródła 1, 3 i 4 sprawdzono pod kątem podstawowych tez przez publiczne strony publikacji. Niniejsza recenzja nie jest przeglądem systematycznym, a prawidłowość wszystkich pozycji w bibliografii autora nie została oddzielnie potwierdzona.

---

**Nota:** recenzję napisano bez ingerowania w pliki autora i bez automatycznego przypisywania statusów DONE. Wszelkie nowe pliki w gałęzi review są artefaktami recenzenckimi.