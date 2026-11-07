# DMTRD — niezależna recenzja naukowa ASTRA

**Data:** 7 listopada 2026 r.

**Dokument:** `DMTRD_koncepcja.docx`, wersja robocza z 07.11.2026.

**Przeznaczenie:** materiał do późniejszej rewizji przez Nemotron.

**Rekomendacja:** zasadnicza rewizja teoretyczna i metodologiczna przed badaniem potwierdzającym.

## Zakres i sposób oceny

Przeanalizowano tekst i tabele dokumentu DOCX, włącznie z bibliografią i odsyłaczami do aneksów. Ponieważ część aneksów jest jedynie wskazana jako pliki zewnętrzne, pomocniczo sprawdzono `model/stany.csv`, `model/przejscia_24.csv`, `model/definicje.md` i `research/hipotezy_badawcze.md`. Uwagi dotyczące aneksów są oznaczone. Nie oparto oceny na wcześniejszych raportach recenzenckich projektu. Nie przeprowadzono nowego pełnego przeglądu literatury ani analizy danych empirycznych DMTRD. Wybrane źródła zweryfikowano w publicznych rejestrach, abstraktach i opracowaniu instytucjonalnym SDT; dokładny zakres weryfikacji podano w sekcji J.

Odniesienia dotyczą **numerów rozdziałów dokumentu**, nie stron, których numeracja zależy od renderowania DOCX. Cytaty krótkie służą lokalizacji problemów. Wnioski matematyczne recenzenta odróżniono od wyników badań. Model pozostaje propozycją hipotetyczną.

**Priorytety:**
- **CRITICAL** — problem podważający podstawy obecnej wersji modelu albo możliwość jej rozstrzygającego testu.
- **MAJOR** — problem istotnie ograniczający trafność, interpretację lub wartość naukową.
- **MINOR** — problem redakcyjny lub drugorzędny.

Priorytet oznacza wagę uwagi dla rewizji. W sekcji mocnych stron oznacza wagę zachowania danego rozwiązania, nie występowanie błędu. CRITICAL nie oznacza, że koncepcji nie można naprawić.

## Rozstrzygnięcie ogólne

**DMTRD jest obecnie przede wszystkim formalnie uporządkowaną klasyfikacją deklarowanych konfiguracji motywacyjnych, z niedomkniętym szkicem modelu dynamiki. Nie stanowi jeszcze spójnej, empirycznie określonej teorii regulacji działania. Ma warunkowy potencjał badawczy, jeżeli autor ograniczy roszczenia, ustabilizuje znaczenie konstruktów i zdefiniuje test odróżniający model od prostszych alternatyw.**

| Pytanie | Ocena | Uzasadnienie i odniesienia |
|---|---|---|
| Czy jest użyteczną klasyfikacją? | **Potencjalnie tak; użyteczność nie została wykazana.** | Osiem kombinacji porządkuje odpowiedzi na trzy pytania. Może pomagać opisywać różnicę między brakiem chęci, poczuciem niewykonalności i obowiązkiem. Nie dowodzi to istnienia ośmiu jakościowo odrębnych stanów psychicznych ani trafności ich nazw. Rozdz. 3–4, 7.1, 8. |
| Czy stanowi spójny model teoretyczny? | **Nie w obecnym brzmieniu.** | Poprawna kombinatoryka współistnieje ze zmiennym znaczeniem W i N, zamianą subiektywnego C na obiektywną możliwość, sprzecznymi testami HPE i nieuzgodnionymi założeniami o pamięci procesu. Rozdz. 4, 7.2–7.3, 8.4–8.5, 11–14. |
| Czy ma potencjał jako empirycznie testowalna teoria? | **Tak, ale warunkowy i węższy od obecnych deklaracji.** | Można testować narzucone ograniczenia generatora przejść, zależność intensywności od kontekstu i przyrost predykcji przyszłego zachowania. Nie wystarczy dopasować osiem klas, zaobserwować korelacje lub potwierdzić znane przewidywania SDT. Rozdz. 13–14, 18–19. |

**Pięć problemów o największym znaczeniu:**
1. **CRITICAL:** definicje nie wyznaczają jednoznacznie W, C i N; ta sama sytuacja może otrzymać różne kody.
2. **CRITICAL:** test HPE w planie EMA jest niezgodny z jej poprawniejszą formalizacją CTMC; ponadto pojedyncze przekroczenie progu nie identyfikuje elementarnego procesu psychologicznego.
3. **CRITICAL:** nie wybrano identyfikowalnego modelu pomiarowego; opis problemu „ośmiu wzorców = osiem klas = 0 df” jest statystycznie błędny jako ogólne twierdzenie o LTA/HMM.
4. **MAJOR:** etykiety ośmiu stanów i 24 przejść wykraczają poza informację zawartą w bitach; szczególnie nieuzasadnione są równoważności z autonomią, internalizacją, moral distress i wypaleniem.
5. **MAJOR:** nie pokazano swoistej wartości predykcyjnej ani uzasadnionej oryginalności; Q3 jest konstrukcją kombinatoryczną, a asynchroniczne procesy wielozmiennowe i asymetryczne intensywności były wcześniej formalizowane.

## A. Najważniejsze mocne strony

### A1. Jawne ograniczenie topologii umożliwia sformułowanie rzeczywistego testu — MAJOR
**Miejsce:** rozdz. 5, 7.1–7.3, 9.

Lista ośmiu kodów i 24 kierunkowych krawędzi jest matematycznie określona. Ograniczenie `q_ij = 0` dla odległości Hamminga co najmniej 2 może być porównane z modelem dopuszczającym takie skoki. To konkretny element, który da się zachować po rewizji. Wartość polega na możliwości ograniczenia przestrzeni modeli, a nie na psychologicznej prawdziwości samego sześcianu. Topologia nie wyznacza wartości intensywności ani nazw mechanizmów.

### A2. Rozdzielenie subiektywnej możliwości, obowiązku i osobistego stosunku do działania jest użytecznym pytaniem badawczym — MAJOR
**Miejsce:** rozdz. 3–4, 8.1–8.5.

Koncepcja pozwala zadać konkretne pytanie: czy przy podobnej deklarowanej wykonalności i podobnym obowiązku różnica w osobistym poparciu działania przewiduje dalszy przebieg zaangażowania? Analogicznie można porównywać sytuacje podobnego W i C przy różnym N. To sensowne kontrasty, pod warunkiem trafnego pomiaru. Ich sensowność nie dowodzi niezależności konstruktów ani oryginalności względem TPB i SDT.

### A3. Rozdział 7.3 zawiera poprawną zasadę obserwacji CTMC — MAJOR
**Miejsce:** rozdz. 7.3, akapit CTMC.

Wzór `P(Δt) = exp(QΔt)` trafnie oddziela przejście elementarne od zmiany zarejestrowanej między dwiema obserwacjami. Ta zasada umożliwia modelowanie nieregularnych odstępów pomiarowych i nieobserwowanych stanów pośrednich. Należy ją konsekwentnie przenieść do rozdz. 13–14; sama nie usuwa problemu identyfikacji z rzadkich pomiarów.

### A4. Część kontrastów ma potencjał wykraczający poza prosty ranking „więcej jedynek = lepiej” — MAJOR
**Miejsce:** rozdz. 3, 8.5, 9.2, 13: H8, H10, H24.

Zestawienie utraty osobistego poparcia `111→011` z utratą obowiązku `111→110` może prowadzić do mierzalnych różnic w afekcie lub późniejszym zaangażowaniu. Autor słusznie dopuszcza, że 111 nie zawsze jest korzystne. Warto zachować takie kontrasty, ale powiązać je z mierzalnymi moderatorami i identycznym horyzontem wyniku. Zaplanowana sukcesja i wymuszona utrata roli nie mogą być traktowane jako równoważne konteksty.

## B. Poważne problemy teoretyczne

### B1. CHCĘ nie ma ustalonego znaczenia: poparcie celu, chęć, napęd, zamiar i autonomia są zamieniane — CRITICAL
**Miejsce:** rozdz. 3, 4.1, 8.2–8.5, 14.1.

Rozdział 4.1 definiuje W jako wewnętrzną zgodę, ale do jej przejawów zalicza „chęć, pragnienie, zamiar”. Rozdział 3 odróżnia stan od intencji, a rozdział 8 utożsamia W z autonomią. To nie są pojęcia równoważne. Człowiek może autonomicznie uznawać sens rehabilitacji i nie mieć aktualnej ochoty na ćwiczenie; może silnie chcieć nagrody pod presją; może pragnąć rezultatu bez zamiaru podjęcia działania.

Proponowane wskaźniki IMI Interest/Enjoyment, identified regulation i postawa TPB nie są zamiennymi miarami jednego konstruktu. Pierwszy dotyczy zainteresowania/przyjemności, drugi uznawania wartości działania, trzeci jego oceny. Jeśli W ma oznaczać autonomiczne poparcie działania, należy konsekwentnie usunąć utożsamienia z samą siłą pragnienia i intencją. Jeśli ma oznaczać ogólną chęć, nie można wyprowadzać z W=1 autonomii. **Bez tej decyzji nie wiadomo, co zmienia się w przejściach W.**

### B2. POWINIENEM jest definiowane i kodowane sprzecznie — CRITICAL
**Miejsce:** rozdz. 4.3, 6.2, 8.4–8.5, 9.2, 10.1; aneks B, opis 110.

Definicja obejmuje obowiązek wynikający zarówno z norm zewnętrznych, jak i zinternalizowanych. Tymczasem w rozdz. 8.4 N=0 może oznaczać, że normy zostały zinternalizowane do W; w rozdz. 8.5 zinternalizowane N uzasadnia N=1 i wysoką jakość 111. Jeżeli po internalizacji nadal występuje poczucie obowiązku, zgodnie z definicją powinno być N=1. Jeżeli poczucie obowiązku zanika, trzeba to zmierzyć, a nie wyprowadzać z samej internalizacji.

Ponadto „presja” nie jest synonimem dobrowolnie przyjętej odpowiedzialności. N może agregować odmienne źródła tego samego odczucia, lecz wtedy nie wolno z samego N wnioskować o rodzaju regulacji. **Ta niejednoznaczność podważa rozróżnienie 110 i 111 oraz interpretację przejść 011→111 i 110→111.** Potrzebna jest jedna reguła kodowania i osobny pomiar źródła oraz jakości obowiązku.

### B3. MOGĘ zmienia się z oceny subiektywnej w warunek obiektywny — MAJOR
**Miejsce:** rozdz. 3, 4.2, 8.1, 8.3, 9.1–9.2, 11, 14.1.

Na poziomie definicji C oznacza postrzeganą wykonalność. W opisach przejść C=0 staje się brakiem zasobów, a C=1 ich uzyskaniem. Rozdział 11 stwierdza, że kontynuacja w 101 jest „niemożliwa bez C”, mimo wcześniejszego zastrzeżenia, że C może być błędnym przekonaniem. Subiektywne C=0 nie wyklucza wykonania, a C=1 go nie gwarantuje.

Zasoby, kompetencje, czas i dostęp środowiskowy mogą być **przyczynami oceny wykonalności**, niekoniecznie refleksyjnymi wskaźnikami jednego czynnika. Samo połączenie ich w ocenę globalną nie jest błędem; błędem jest traktowanie tego połączenia jako równoważnego rzeczywistym warunkom COM-B. Należy ustalić, czy badany jest sąd „mogę wykonać X do czasu Y”, czy indeks warunków wykonania. GSE, skala ogólnej własnej skuteczności, nie zastępuje automatycznie chwilowej oceny konkretnego zadania.

### B4. Rozłączność pojęciowa jest mylona z niezależnością statystyczną i dynamiczną — MAJOR
**Miejsce:** rozdz. 2: Q1, 5: A1, 6.2, 10.2, 14.2, 19.

Trzy różne pytania nie dowodzą trzech odrębnych konstruktów. Z drugiej strony odrębne konstrukty nie muszą mieć zerowych korelacji. Interakcje opisane w rozdz. 10.2 wręcz zakładają związki między W, C i N. Możliwość zapisania ośmiu kombinacji nie wymaga statystycznej niezależności bitów; nierówna częstość konfiguracji nie obala samej przestrzeni kombinatorycznej.

Należy rozdzielić: (a) odrębność treści i pomiaru, (b) korelacje między osobami, (c) współzmienność w obrębie osoby, (d) wpływ jednego wymiaru na tempo zmiany drugiego. CFA nie sprawdza wszystkich tych tez. Literalna rozłączność motywacji i obowiązku jest szczególnie wątpliwa, bo poczucie obowiązku samo może motywować. Model może opisywać współwystępujące aspekty regulacji, nie „niezależne substancje” psychiczne.

### B5. Osiem konfiguracji logicznych nie jest dowodem ośmiu naturalnych stanów psychicznych — MAJOR
**Miejsce:** rozdz. 5: A1–A2, 7.1, 8, 13: HG1, 14.

`2³ = 8` wynika z binarnego kodowania. Nie wynika z tego, że wszystkie konfiguracje występują dostatecznie często, mają jednorodne mechanizmy, są metastabilne albo stanowią optymalną reprezentację danych. Nazwy „neutralność”, „działanie autonomiczne” czy „pełna gotowość” dodają treść niewynikającą z bitów. Przykładowo 000 względem konkretnego zadania jest zgodne z intensywnym zaangażowaniem w inne zadanie; nie oznacza globalnej apatii.

Model klasyfikacyjny nie musi postulować naturalnych kategorii, ale wtedy powinien uzasadniać użyteczność kompresji informacji, nie odkrycie ośmiu odrębnych typów psychologicznych. Osiem narzuconych klas LTA nie jest niezależnym potwierdzeniem ośmiu stanów.

### B6. Stan 101 nie jest równoważny moral distress — MAJOR
**Miejsce:** rozdz. 6.2, 8.1, 8.3, 13: HG4, 17, 19.

101 mówi jedynie o obecności W i szeroko rozumianego N oraz braku postrzeganej wykonalności. Nie zawiera pomiaru moralnego charakteru sytuacji, osądu moralnego, cierpienia ani związku cierpienia z wydarzeniem moralnym. Chęć terminowego wysłania nieskomplikowanego raportu, poczucie administracyjnego obowiązku i chwilowa awaria internetu mogą dać 101 bez moral distress. Można też doświadczać cierpienia moralnego przy zachowanej zdolności wykonania określonej czynności, np. wobec konfliktu wartości.

W literaturze istnieją konkurencyjne definicje moral distress; synteza Morley i współautorów [S4] pokazuje ten problem wprost. W wąskim ujęciu blokada moralnie właściwego działania jest ważna, lecz szerokie N i subiektywne C nie gwarantują spełnienia tego warunku. Rozdział 8.1 dodatkowo przypisuje moral distress stanowi 001, co osłabia deklarowaną swoistość 101. **Dopuszczalna hipoteza brzmi: w określonych sytuacjach moralnych 101 może zwiększać ryzyko lub współwystępować z moral distress. Równość „101 = moral distress” jest nieuzasadniona.**

### B7. Każdej krawędzi przypisano zbyt jednoznaczny mechanizm — MAJOR
**Miejsce:** rozdz. 9–10, 13; aneks A.

Zapis zmiany jest opisem wyniku, nie identyfikacją przyczyny. 011→111 może oznaczać internalizację, ale również pojawienie się przyjemności, nagrody, zmianę interpretacji pytania lub błąd pomiaru. 111→011 może wynikać z adaptacyjnej zmiany priorytetów, a nie dezautonomizacji. 101→111 może odzwierciedlać korektę przekonania o wykonalności bez usunięcia obiektywnej bariery.

**Pełna ocena 24 przejść — grupowanie wyłącznie dla czytelności; oba kierunki oceniono osobno:**

| Przejścia z rozdz. 9.1 | Co wynika z kodu | Co wymaga dodatkowego dowodu | Priorytet |
|---|---|---|---|
| T01 000→100; T02 100→000 | Pojawienie się / zanik W przy C=N=0. | T01 nie dowodzi ustanowienia celu; T02 nie dowodzi jego porzucenia. Aktualna chęć może się zmienić przy utrzymanym zobowiązaniu do celu. | MAJOR |
| T03 001→101; T04 101→001 | Zmiana W przy poczuciu obowiązku i C=0. | T03 nie identyfikuje internalizacji; T04 nie identyfikuje wypalenia ani moral residue. Potrzebne osobne miary rodzaju regulacji i skutków. | MAJOR |
| T05 010→110; T06 110→010 | Zmiana W przy C=1, N=0. | T05 nie dowodzi inicjacji działania. T06 nazwano wypaleniem w rozdz. 9, a automatyzacją w 11.1: te wyjaśnienia dają odmienne przewidywania. | MAJOR |
| T07 011→111; T08 111→011 | Zmiana W przy C=N=1. | Internalizacja i utrata autonomii są hipotezami o mechanizmie. Wzrost lub spadek przyjemności nie musi oznaczać zmiany autonomii. | MAJOR |
| T09 000→010; T10 010→000 | Zmiana postrzeganej wykonalności bez W i N. | T09 nie musi oznaczać zdobycia zasobu; T10 jego utraty. Przewidywany mniejszy stres zależy m.in. od znaczenia zadania, którego W=0 nie wyczerpuje. | MAJOR |
| T11 001→011; T12 011→001 | Zmiana C przy W=0, N=1. | Empowerment jest szerszy niż C. Spadek C nie dowodzi odebrania władzy ani pojawienia się moral distress. | MAJOR |
| T13 100→110; T14 110→100 | Zmiana C przy W=1, N=0. | T13 nie jest z definicji przekroczeniem Rubikonu ani planem implementacyjnym. T14 nie przesądza o faktycznym zatrzymaniu wykonania. | MAJOR |
| T15 101→111; T16 111→101 | Zmiana C przy W=N=1. | T15 nie gwarantuje rozwiązania konfliktu moralnego; T16 nie identyfikuje traumy. Prognozy PTSD wymagają właściwej ekspozycji i horyzontu czasowego. | MAJOR |
| T17 000→001; T18 001→000 | Pojawienie się / zanik N przy W=C=0. | T17 nie musi być przyjęciem roli, T18 jej odrzuceniem. Obowiązek może wygasnąć po zmianie terminu lub sytuacji. | MAJOR |
| T19 010→011; T20 011→010 | Zmiana N przy W=0, C=1. | T19 nie dowodzi podporządkowania w zachowaniu ani narzucenia obowiązku; T20 nie dowodzi deregulacji otoczenia lub wzrostu autonomii. | MAJOR |
| T21 100→101; T22 101→100 | Zmiana N przy W=1, C=0. | Moralizacja i „sekularyzacja” są zbyt wąskie wobec definicji obejmującej obowiązki administracyjne, prawne i rolowe. | MAJOR |
| T23 110→111; T24 111→110 | Zmiana N przy W=C=1. | T23 nie dowodzi OCB ani prospołeczności. T24 nie dowodzi delegacji; przykład lidera zmieniającego pracę operacyjną na mentoring może zmieniać samo działanie odniesienia. | MAJOR |

Zalecenie: nazwa neutralna wynikająca z kodu + lista alternatywnych mechanizmów + osobny pomiar umożliwiający ich rozróżnienie. Nie trzeba usuwać przykładów, lecz nie mogą pełnić funkcji definicji.

### B8. HPE może być własnością kodowania, a nie psychologiczną atomowością zmiany — CRITICAL
**Miejsce:** rozdz. 5: A3, 7.2, 13: HG2, 14.1–14.2.

Nie określono, czym jest „elementarny proces” niezależnie od zmiany jednego bitu. Jeżeli każde zdarzenie wielobitowe można bez ograniczeń nazwać ciągiem nieobserwowanych zdarzeń, hipoteza traci rozstrzygający charakter. Wspólny bodziec może wpływać równocześnie na wartość działania, wykonalność i obowiązek; HPE nie wynika ani z ich rozróżnialności, ani z grafu.

Istotniejszy problem pojawia się w proponowanej wersji ciągłej: przy ciągłych trajektoriach i trzech progach przecięcia różnych płaszczyzn często występują w różnych chwilach. W wielu niesingularnych modelach dokładna jednoczesność przekroczeń będzie zdarzeniem o zerowym prawdopodobieństwie. Można więc obserwować zmiany jednego bitu, mimo że **ten sam proces przyczynowy nieustannie zmienia wszystkie trzy wielkości**. Nie jest to twierdzenie o każdej możliwej trajektorii, lecz kontrprzykład wobec wniosku „jeden bit = jeden mechanizm”.

Potrzebne są: niezależna definicja zdarzenia psychologicznego, skala czasu, model błędu i jawny model alternatywny. Test struktury generatora może być sensowny, ale sprawdza asynchroniczny model skokowy w danej reprezentacji, nie uniwersalne prawo elementarności motywacji.

### B9. Podstawowy stan nie jest wystarczający dla deklarowanej dynamiki Markowa — MAJOR
**Miejsce:** rozdz. 7.3–7.4, 8.5, 12, 14.2.

Markowowskość oznacza, że po uwzględnieniu aktualnego stanu przyszłość nie zależy od wcześniejszej historii. Rozdział 12 stawia przeciwne przewidywanie: 111 ma inną stabilność zależnie od drogi dojścia. Nie należy ogłaszać założenia Markowa psychologicznie niemożliwym, jak sugeruje dokument; może być użytecznym przybliżeniem. Nie można jednak równocześnie traktować trzech bitów jako wystarczającego stanu i przypisywać historii niewyjaśnionej roli predykcyjnej.

Szczególnie ważny jest problem agregacji: dwie osoby w 111, z odmienną intensywnością W i odmiennym rodzajem N, mogą mieć różne intensywności wyjścia. Agregacja bardziej szczegółowego procesu Markowa do ośmiu kategorii **nie musi zachowywać własności Markowa**. Wymaga odpowiednich warunków agregowalności albo empirycznie akceptowalnego przybliżenia. Samo progowanie zmiennych tego nie zapewnia.

Jednorodny CTMC dopuszcza różne średnie czasy trwania stanów: „111 trwa dłużej” nie wymaga jeszcze modelu semi-Markowa. Dopiero zależność ryzyka wyjścia od czasu już spędzonego w stanie podważa wykładniczy czas trwania w tej wersji CTMC. Zwykły model semi-Markowa nie koduje automatycznie całej drogi dojścia; należy wskazać, które cechy historii mają znaczenie.

### B10. Rozróżnienie motywacji i działania jest deklarowane, lecz naruszane w interpretacjach — MAJOR
**Miejsce:** rozdz. 3, 5: A5, 8, 11, 14.2.

Nazwa 110 „Działanie autonomiczne” sugeruje wykonanie, choć kod nie zawiera zachowania. Rozdział 11 wskazuje 101 jako jeden ze stanów najbardziej sprzyjających inicjacji, ale następnie uzasadnia to szukaniem C. **Szukanie zasobu to inne działanie niż wykonanie pierwotnego zadania.** Podobna zmiana jednostki analizy występuje przy planowaniu, delegacji i reengagement.

Dokument nie jest całkowicie „bez celu”: definicje od początku odnoszą się do konkretnego celu lub działania. Trafna krytyka dotyczy braku utrzymanego, operacyjnego odniesienia i mechanizmu wyboru między konkurującymi celami, nie zupełnego braku celu w tekście. Trzeba ustalić działanie, obiekt, kontekst i horyzont czasu oraz osobno rejestrować intencję, wykonanie i działania przygotowawcze. Nie jest konieczne dodawanie bitu działania do sześcianu; zachowanie może pozostać zewnętrznym wynikiem.

### B11. Obsługa nawyku i ambiwalencji prowadzi do odmiennych znaczeń tych samych kodów — MAJOR
**Miejsce:** rozdz. 3–4, 11.1, 15.1: ARG3, 16.

Brak aktualnej refleksji o chęci nie jest tym samym co brak osobistej akceptacji. Nawykowe działanie może być chciane i autonomicznie popierane; automatyzacja nie wymaga przejścia 110→010. Wood i Neal [S8] opisują oddziaływanie nawyków i celów, a nie prostą wymienność świadomej motywacji i automatyzmu. Wartość W=0 nie diagnozuje nawyku.

Rozdział 3 odróżnia brak chęci od silnej niechęci, ale rozdział 4.1 umieszcza neutralność i awersję w tej samej kategorii. To dopuszczalne uproszczenie klasyfikacyjne, ale destrukcyjne dla jednoznacznych przewidywań o napięciu i działaniu. Jedna skala od niskiej do wysokiej chęci nie odróżni też niskiego zaangażowania od jednocześnie silnego przyciągania i odpychania. Zakres modelu powinien być jawnie ograniczony lub uzupełniony o mierzalne moderatory.

## C. Poważne problemy metodologiczne

### C1. Plan testuje inną HPE niż formalizacja CTMC — CRITICAL
**Miejsce:** rozdz. 7.3, 13.1: HG2, 14.2: „Częstotliwość” i „Analiza statystyczna”; aneks G, HG2 i analiza LTA.

W CTMC HPE dotyczy generatora Q. Tymczasem plan LTA zeruje `p_ij` dla `d_H≥2` przy odstępach 2–3 godzin. Wielobitowe różnice między obserwacjami są możliwe w CTMC zgodnym z HPE. Taki LTA narzuca dodatkowy warunek: stan końcowy może różnić się od początkowego najwyżej jednym bitem. Nie określa to liczby rzeczywistych zmian w interwale, ponieważ możliwe są powroty. To nie jest ten sam model co panelowo obserwowany CTMC z HPE.

Próg falsyfikacji z aneksu G — ponad 15% zmian wielobitowych przy pomiarze co 30 minut — jest arbitralny bez określenia intensywności. **Kontrprzykład analityczny:** niech każdy z trzech bitów niezależnie odwraca się z intensywnością 1 na godzinę. Proces idealnie spełnia HPE. Po pół godzinie prawdopodobieństwo zmiany wartości pojedynczego bitu wynosi `p=(1−exp(−1))/2≈0,316`. Prawdopodobieństwo różnicy w co najmniej dwóch bitach to `3p²(1−p)+p³≈0,237`. Przekracza 15% mimo prawdziwej HPE; wśród obserwacji ze zmianą odsetek jest jeszcze większy. To ilustracja matematyczna, nie wynik badania ludzi.

Odwrotnie, duża liczba zmian jednobitowych może wynikać z wolnych zmian, błędu pojedynczego wskaźnika lub progowania i nie potwierdza HPE. Należy modelować dokładne odstępy oraz porównywać generatory z tym samym modelem pomiaru. Dla skończonych intensywności, przy małym `Δt`, przejście wymagające dwóch skoków ma wkład rzędu `Δt²`, a bezpośredni skok wielobitowy — rzędu `Δt`. Zróżnicowanie odstępów może pomóc, jeżeli pomiar i liczba obserwacji pozwolą rozróżnić te zachowania.

Test zerowych intensywności dotyczy parametrów na brzegu przestrzeni. Standardowy rozkład chi-kwadrat dla LRT nie jest automatycznie poprawny; kalibrację trzeba uzasadnić, np. symulacją lub bootstrapem parametrycznym. Odrzucenie Q3 odrzuca określoną specyfikację pomiarowo-dynamiczną; dopiero diagnostyka błędu, heterogeniczności i niejednorodności pozwala wiązać wynik z samą HPE.

### C2. Błędnie opisano identyfikowalność klas ukrytych — CRITICAL
**Miejsce:** rozdz. 7.3, 14.1, 15.1: ARG5, 16; aneksy B/G i `model/definicje.md`.

Trzeba odróżnić trzy różne modele:

1. **Trzy obserwowane, bezbłędne bity.** Dają osiem obserwowanych kategorii. Rozkład w jednym pomiarze ma siedem niezależnych prawdopodobieństw i może być nasycony. Nie wyklucza to testowania ograniczeń przejść w danych podłużnych.
2. **Osiem klas latentnych z trzema binarnymi wskaźnikami i swobodnymi emisjami, w jednym pomiarze.** Przy lokalnej niezależności jest `7 + 8×3 = 31` parametrów wobec siedmiu niezależnych częstości. To model nadparametryzowany i nieidentyfikowalny w tej postaci, a nie po prostu „0 df”.
3. **HMM/LTA z wieloma pomiarami i ograniczeniami.** Informacja zawarta w sekwencjach może umożliwiać identyfikację pod odpowiednimi warunkami. Nie można przenosić rachunku z pojedynczego pomiaru na dowolny model longitudinalny. Z kolei dołożenie skali Likert nie stanowi dowodu identyfikowalności.

Rozdział 14.1 mówi równocześnie o **trzech itemach na każdy wymiar** i o „3 wskaźnikach”. To dziewięć itemów, chyba że wcześniej tworzy się trzy kompozyty. Przy dziewięciu binarnych itemach jest 512 możliwych wzorców, ale samo policzenie wzorców nadal nie dowodzi identyfikowalności konkretnego modelu z ograniczeniami i błędem.

Potrzebna jest jedna specyfikacja: liczba i rodzaj wskaźników, ich rozkłady warunkowe, parametry wspólne w czasie, lokalne zależności, model przejść, rozkład początkowy, efekty osób i reguły nadawania etykiet klasom. Bez kotwic pomiarowych klasa numer 5 w modelu mieszaninowym nie staje się automatycznie stanem 101. Identyfikowalność strukturalna i praktyczna precyzja estymacji to odrębne wymagania.

### C3. Progowanie może wygenerować pozorną dynamikę — MAJOR
**Miejsce:** rozdz. 7.5, 14.1–14.2, 15.1: ARG1.

Próg „np. 4” nie jest uzasadniony psychologicznie. Zmiana odpowiedzi 3→4 może zmienić stan, a znacznie większa 4→7 nie zmieni go wcale. Osoby blisko granicy mogą wielokrotnie przechodzić między kodami z powodu błędu odpowiedzi. Stałe progi nie gwarantują też tego samego znaczenia między osobami, działaniami i językami.

MacCallum i współautorzy [S6] pokazują ogólne ryzyko utraty informacji i zniekształceń po dychotomizacji. Nie wynika z tego zakaz wszystkich modeli dyskretnych. W DMTRD należy porównać model ciągły z modelem stanowym, sprawdzić wrażliwość na próg i modelować błąd klasyfikacji. Pomiar na skali Likert, po którym natychmiast odrzuca się informację przez progowanie, nie rozwiązuje problemu. Gęstsze próbkowanie może wręcz ujawniać częste przekroczenia progu niezgodne z prostym CTMC o skończonych intensywnościach.

### C4. Walidacja pomiaru jest niedostosowana do wniosków o zmianach wewnątrzosobniczych — MAJOR
**Miejsce:** rozdz. 14.1–14.2, 18: etap 2.

Przekrojowe CFA na 300–500 osobach nie ustala struktury chwilowych zmian u konkretnej osoby. Potrzebne są ocena treści itemów, wywiady poznawcze, rozróżnienie wariancji między- i wewnątrzosobniczej oraz sprawdzenie stabilności znaczenia pomiaru w czasie. CFI, RMSEA i AVE są wskaźnikami diagnostycznymi, nie samodzielnym dowodem trafności ani niezależności.

Nie wiadomo, dlaczego przeciążenie rolą ma być wskaźnikiem N, a nie skutkiem wymagań i zasobów; dlaczego zadowolenie z zadania ma mierzyć zgodę na jego wartość; czy zasoby i czas są wskaźnikami, czy przyczynami C. Dla każdego itemu trzeba zdefiniować rolę w modelu. Zapożyczenie nazwy skali nie waliduje jej adaptacji do chwilowego EMA.

### C5. Dodawanie zachowania do definicji klas grozi zanieczyszczeniem kryterium — MAJOR
**Miejsce:** rozdz. 7.3, 14.2, 15.1: ARG5.

Dokument proponuje ratowanie identyfikowalności dodatkowymi wskaźnikami „zachowanie, afekt, kontekst”, a potem przewidywanie zachowania i afektu ze stanu. Jeżeli wynik współtworzy stan, korelacja stanu z wynikiem nie jest niezależną walidacją. Można skonstruować poprawny wspólny model pomiaru i wyniku, ale trzeba jawnie zdefiniować rolę każdej zmiennej i sposób oceny na nowych danych.

W predykcji przyszłości stan w chwili t powinien być wyznaczany z informacji dostępnej do t. Użycie wygładzonych stanów HMM, oszacowanych także z późniejszych obserwacji, może prowadzić do przecieku informacji. Potrzebne jest filtrowanie prospektywne lub właściwa procedura prognozowania całego modelu.

### C6. HG1 i HG5 nie mają uczciwie zdefiniowanego porównania konkurencyjnego — MAJOR
**Miejsce:** rozdz. 13.1, 14.2, 19; aneks G.

TPB, SDT i COM-B to teorie lub ramy, a nie pojedyncze modele statystyczne o ustalonej funkcji wiarygodności. AIC/BIC modelu klas dla wskaźników WCN nie można bezpośrednio porównywać z AIC/BIC regresji innego wyniku na innych zmiennych. Zagnieżdżenie również nie wynika z nazw teorii. Trzeba porównywać tę samą zmienną wynikową, te same obserwacje, horyzont i zakres informacji oraz odpowiednie funkcje wiarygodności.

Minimalne alternatywy to: ostatnie zachowanie i prosty model autoregresyjny; ciągłe W,C,N z nieliniowościami i interakcjami; pełny model ośmiu konfiguracji bez HPE; prostszy model zmian bitów; odpowiednio operacjonalizowane TPB/SDT/COM-B. Szczególnie ważne: dowolne osiem średnich wyniku dla kombinacji trzech bitów można odtworzyć regresją zawierającą wyraz wolny, trzy efekty główne, trzy interakcje dwuczynnikowe i interakcję trójczynnikową. **Sam profil ośmiu stanów nie daje więc przewidywań „niedostępnych modelom płaskim”.** Wkład Q3 musi dotyczyć ograniczeń dynamiki lub efektywności estymacji.

Walidacja musi uwzględniać zależność czasową: osobno prognozowanie późniejszego okresu u znanych osób i generalizację na nowe osoby. Losowy podział pojedynczych rekordów EMA jest niewystarczający. Raportować należy np. log-loss, Brier score i kalibrację dla zachowania binarnego oraz niepewność różnic między modelami, nie tylko R².

### C7. Asymetria intensywności nie identyfikuje asymetrii mechanizmów ani kosztów — MAJOR
**Miejsce:** rozdz. 5: A4, 7.4, 9.2, 13.1: HG3.

Nierówność `q_ij ≠ q_ji` mówi o różnych tempach zmian warunkowych względem stanu startowego. Nie dowodzi różnych procesów psychologicznych, wysiłku ani kosztu emocjonalnego. Procesy o różnych przyczynach mogą mieć równe tempa, a różne tempa mogą wynikać z jednego mechanizmu działającego przy różnej dostępności okazji.

To także nie jest równoznaczne z nieodwracalnością procesu. W stanie stacjonarnym równowaga szczegółowa ma postać `π_i q_ij = π_j q_ji`; intensywności mogą być nierówne przy procesie odwracalnym. Liczby przejść należy odnosić do czasu ekspozycji na stan startowy.

Próg „co najmniej 50% par” nie ma wyprowadzenia. Aneks G traktuje `p>0,05` dla wielu par jako falsyfikację, choć brak istotności może wynikać z małej precyzji. Potrzebne są minimalne istotne naukowo różnice/ilorazy intensywności, przedziały niepewności i odpowiednia moc. Koszty i mechanizmy powinny być mierzone oddzielnie.

### C8. H1–H24 nie tworzą 24 poprawnie określonych testów mechanizmów — MAJOR
**Miejsce:** rozdz. 13, tabela 4; aneks G.

| Hipotezy | Problem wymagający korekty |
|---|---|
| H1–H2 | Self-efficacy jest bliskie definicji C. Należy oddzielić predyktor od wskaźnika stanu i wyjaśnić, jak jego wzrost przewiduje zmianę W przy pozostaniu C=0; jest to możliwe przy progu, ale nie wynika z opisu. |
| H3, H7, H13, H15 | Słowo „mediuje” bywa używane bez jednoznacznej ekspozycji X, mediatora M i wyniku Y. Wsparcie autonomii pojawia się raz jako mediator, raz jako predyktor. Sam zapis SEM nie dostarcza identyfikacji przyczynowej. |
| H4 | 101→011 zmienia dwa bity. Jest dopuszczalne jako wynik między pomiarami CTMC, ale nie jako pojedyncza krawędź HPE. Hipoteza musi określić poziom obserwacji i mechanizm zmiany C. |
| H5, H7 | Intrinsic motivation lub identified regulation mogą pokrywać się treściowo z W. „Predykcja W przez W pod inną nazwą” nie testuje nowej teorii. |
| H8, H12, H16, H24 | Wypalenie, intencja odejścia i objawy stresowe mają różne skale czasu i formaty. Cox wymaga zdefiniowanego zdarzenia i czasu ryzyka; powtarzana skala wypalenia nie staje się takim zdarzeniem automatycznie. |
| H16 | W aneksie zapowiedziano porównanie z „innymi utratami C”, lecz podano 111→110 i 111→011, które zachowują C=1. Właściwe kontrasty utraty C to m.in. 110→100, 011→001 i 010→000. |
| H17, H19–H21 | Część hipotez dotyczy kolejnego przejścia po krawędzi wymienionej w nagłówku, a H20 obejmuje również utratę C. Nie jest to jednoznaczne przyporządkowanie jednej hipotezy do jednej krawędzi. |
| H22 | Po wybraniu 101→100 binarne W=1 i określona zmiana N są stałe. Interakcja tych zmiennych w takiej podpróbie nie jest identyfikowalna; potrzebna inna próba lub jawna ciągła miara identyfikacji. |
| H23 | OCB jest zachowaniem, nie zmianą N. Trzeba rozdzielić test przejścia 110→111 od testu przyszłego działania prospołecznego. |

Zmiany wielokrotne i konkurujące wyjścia ze stanu wymagają uwzględnienia zbioru osób/okazji pozostających w ryzyku, zdarzeń powtarzalnych i zagnieżdżenia. Lista nazw analiz nie zastępuje modelu danych. Obserwacyjny CLPM lub SEM nie dowodzi mechanizmu przyczynowego; Hamaker i współautorzy [S7] dodatkowo pokazują, dlaczego standardowy CLPM może mieszać różnice między osobami ze zmianami wewnątrzosobniczymi.

### C9. Plan EMA jest zbyt szeroki i nie dopasowuje rozdzielczości do zjawisk — MAJOR
**Miejsce:** rozdz. 14.2, 18; aneks G.

Jedno badanie na 100–150 pracownikach lub 200 studentach ma równocześnie testować HPE, 24 hipotezy, asymetrię, mediacje, wypalenie, moral distress i porównanie wielu teorii. Liczba pomiarów ogółem nie gwarantuje informacji o rzadkich stanach i rzadkich przejściach. Mieszanie ćwiczeń, nauki języka i projektów zawodowych może tworzyć pozorną heterogeniczność stanów i tempa zmian. Heterogeniczność uczestników może też imitować zależność od historii.

Odstępy 2–3 godzin nie są z definicji „kluczową” rozdzielczością dla HPE. Pilotaż powinien ustalić skalę zmian i tolerancję obciążenia. Pomiar event-based po działaniu jest selektywny i może rejestrować **skutki** wykonania: wzrost C po sukcesie lub spadek N po spełnieniu obowiązku. Trzeba odróżniać te skutki od poprzedzających predyktorów.

Plan powinien uwzględnić dokładne znaczniki czasu, zmienną długość okna zachowania, przerwy nocne, brak okazji do działania, informacyjny brak odpowiedzi i rezygnację z badania. Deklaracja „12 itemów <30 sekund” wymaga pomiaru wykonalności; nie obejmuje wszystkich dodatkowych skal wymienionych w hipotezach.

### C10. Obecne kryteria falsyfikacji nie rozdzielają teorii, pomiaru i implementacji — MAJOR
**Miejsce:** rozdz. 5: A7, 13.1, 15.2; aneks G.

Wybór innej liczby klas podważa konkretną reprezentację danych, niekoniecznie użyteczność trzech pytań. Brak przewagi predykcyjnej może podważyć HG1/HG5, ale nie samą logiczną możliwość ośmiu kodów. Korelacja z MDS nie dowodzi równoważności z moral distress; jej brak może dotyczyć też nietrafnej populacji lub skali czasu. Należy wskazać, **co dokładnie zostaje odrzucone** przy każdym wyniku i jakie modyfikacje nie będą dopuszczane po obejrzeniu danych.

Rozbudowywanie liczby wymiarów, progów, moderatorów i pamięci procesu po każdym niepowodzeniu może uczynić DMTRD niewrażliwym na obalenie. Wersja potwierdzająca powinna mieć zamknięty zestaw głównych przewidywań, model pomiaru oraz kryteria wyniku nierozstrzygającego.

## D. Założenia niepoparte przedstawionymi dowodami

Poniższe twierdzenia mogą być hipotezami; dokument nie dostarcza wyników empirycznych ani wystarczającego wyprowadzenia, aby traktować je jako ustalenia.

| Założenie | Miejsce | Dlaczego jest istotne | Priorytet |
|---|---|---|---|
| W,C,N wystarczają do opisania istotnej dynamiki. | 5: A1/A6; 7; 12 | Różnice rodzaju N, nasilenia W, nawyku i historii mogą pozostawiać różną przyszłość w obrębie tego samego kodu. | MAJOR |
| Elementarna zmiana psychologiczna obejmuje dokładnie jeden wymiar. | 5: A3; 7.2 | To centralne ograniczenie; nie wynika z literatury o trzech determinantach działania. | CRITICAL |
| 101 jest „najbardziej napięty” i „czasową bombą”. | 8.3; aneks B | Silny przymus w 001 lub 011 może być bardziej obciążający; kod nie zawiera natężenia, ważności ani czasu trwania. | MAJOR |
| 111 z internalizowanym N daje najwyższą jakość i większą trwałość niż 110. | 8.5; 11; 12 | Rodzaj N nie jest częścią kodu, a większy obowiązek nie gwarantuje jakości. Nie podano warunków i wielkości przewagi. | MAJOR |
| Wzrost W/C ma zasadniczo dodatni, a spadek ujemny bilans afektywny. | 9.2; 10.3 | Utrata chęci do nieosiągalnego celu może dawać ulgę; zdobycie możliwości może zwiększać odpowiedzialność i lęk. | MAJOR |
| Wzrost C oznacza mały koszt, a jego utrata bardzo wysoki koszt/PTSD. | 9.2; 13: H16 | Pozytywny wynik nie oznacza niskiego wysiłku. Nie ma miary „kosztu”; PTSD nie jest ogólną konsekwencją frustracji. | MAJOR |
| N=1 ułatwia wzrost W. | 10.2 | Presja może sprzyjać internalizacji lub ją osłabiać; konieczne są warunki dotyczące jakości relacji i wsparcia autonomii. | MAJOR |
| Nierówność intensywności obejmuje co najmniej połowę par. | 13.1: HG3 | Brak wyprowadzenia progu oraz minimalnej istotnej wielkości różnicy. | MAJOR |
| Wskaźniki ciągłe wystarczą do uzyskania identyfikowalnego HMM/LTA. | 7.3; 15.1: ARG5 | Identyfikowalność jest własnością konkretnej parametryzacji i projektu, nie etykiety „ciągłe”. | CRITICAL |
| Większość codziennych działań można wyłączyć jako nawykowe na podstawie 40–50%. | 6.1; 15.1: ARG3 | 40–50% samo nie uzasadnia „większości”; częstość zachowań nawykowych zależy od sposobu operacjonalizacji i nie dowodzi braku W. | MAJOR |

## E. Elementy opisane wcześniej i zgodność z literaturą

### E1. Trzy grupy determinant nie stanowią same w sobie nowej teorii — MAJOR
**Miejsce:** rozdz. 3, 6–6.2, 19.

- **TPB:** postawa, norma subiektywna i postrzegana kontrola są bliskimi, choć nie identycznymi odniesieniami dla W,N,C; intencja i kontrola uczestniczą w przewidywaniu zachowania. Wyodrębnienie normy obok osobistej oceny i kontroli nie jest nowe. Dodanie moralnego obowiązku do normy społecznej poszerza treść N, ale nie dowodzi nowego mechanizmu [S1, S5].
- **SDT:** rozróżnienia motywacji autonomicznej i kontrolowanej, internalizacji, regulacji zidentyfikowanej i zintegrowanej poprzedzają DMTRD. SDT nie redukuje się do ilości chęci. Kompetencja jako potrzeba psychologiczna nie jest tożsama z posiadaniem zasobów. Aktualne opracowanie SDT oraz metaanaliza struktury motywacji nie uzasadniają odwzorowania „011=kontrolowana, 110=autonomiczna, 111=zintegrowana” na podstawie samych bitów [S2, S10–S11].
- **COM-B:** obejmuje capability, opportunity, motivation i zachowanie B; rozdziela motywację refleksyjną i automatyczną. W rozdz. 14.2 skrót „COM-B (M,O,A)” miesza go z MOA. Samo włączenie wykonalności do opisu działania nie jest oryginalne [S3].
- **SCT, modele oczekiwania i wartości, Rubikon oraz samoregulacja:** przekonania o skuteczności, wartościowanie celu, planowanie, przejście od wyboru do realizacji i zmiana zaangażowania są wcześniejszymi ideami. Przyrost C nie jest definicją przekroczenia Rubikonu; decyzja/intencja nie jest po prostu oceną możliwości.
- **Moral distress i konflikt ról:** zablokowane moralnie ważne działanie i sprzeczności między wymaganiami a możliwościami były badane przed DMTRD [S4, S9]. Nowy kod nie stanowi odkrycia tych zjawisk.
- **Modele wielostanowe:** CTMC, HMM i modelowanie błędu klasyfikacji w danych panelowych są gotowymi metodami, a nie nowymi składnikami teorii psychologicznej [S12].

Nie wszystkie teorie odniesienia zakładają trzy identyczne „fundamentalne filary”, jak sugeruje rozdz. 6.1. Takie mapowanie jest interpretacją autora. Nie należy też przeciwstawiać DMTRD wszystkim innym teoriom jako modelu dynamicznego wobec modeli statycznych: SDT opisuje internalizację, COM-B sprzężenia, a samoregulacja z definicji obejmuje dynamikę.

### E2. Formalizm pojedynczych zmian lokalnych ma wyraźne precedensy — MAJOR
**Miejsce:** rozdz. 6.2, 7.2–7.3, 19.

Nodelman, Shelton i Koller przedstawili **Continuous Time Bayesian Networks** w UAI 2002 [S13]. Jest to opis systemu przez lokalne zmienne, których intensywności zmian zależą od wartości innych zmiennych. Dla trzech zmiennych binarnych ze zmianami jednej współrzędnej oraz pełną zależnością tempa od pozostałych dwóch otrzymuje się tę samą rodzinę generatorów o maksymalnie 24 kierunkowych intensywnościach, co w podstawowej wersji CTMC DMTRD. To porównanie konstrukcji matematycznych, nie twierdzenie, że CTBN opisuje psychologiczne W,C,N.

Zatem **nowość Q3, 24 intensywności, lokalnych zmian i potencjalnej asymetrii jako narzędzi formalnych nie jest uzasadniona**. Potencjalna nowość może leżeć w trafnym psychologicznym doborze zmiennych, ograniczeniach między parametrami i przewidywaniach interwencyjnych. Stwierdzenie „nie znaleziono modelu z tą strukturą” bez określonego zakresu wyszukiwania nie ustala pierwszeństwa.

### E3. Deklaracja aktualności literatury jest szersza od wykazanego pokrycia — MAJOR
**Miejsce:** „Status epistemiczny opracowania”, rozdz. 6, bibliografia.

Dokument deklaruje odniesienie do literatury do listopada 2026 r., natomiast najnowsza pozycja jego bibliografii pochodzi z 2016 r. Nie dowodzi to automatycznie błędności każdego twierdzenia, lecz nie uzasadnia deklarowanej aktualności. Selektywna kontrola wykazała istotne późniejsze punkty odniesienia: metaanalizę SDT z 2017 r., syntezę moral distress z 2019 r. i opracowanie SDT z 2020 r. [S4, S10–S11].

Metaanaliza Sheerana i współautorów [S5] dostarcza eksperymentalnego wsparcia roli postaw, norm i własnej skuteczności w intencjach i zachowaniu. **Nie potwierdza** ich binarności, ośmiu stanów, HPE ani równoważności W,C,N z jej zmiennymi. Literatura wspiera część ogólnego tła DMTRD, nie jego swoiste postulaty. Niniejsza recenzja nie poświadcza kompletności literatury do 2026 r.

## F. Elementy potencjalnie oryginalne

### F1. Oszczędny model trajektorii konkretnych konfiguracji WCN — MAJOR
**Miejsce:** rozdz. 7–9, 13.

Możliwym wkładem byłoby wykazanie, że dobrze zdefiniowane WCN tworzą użyteczną kompresję procesu: model z ograniczonym generatorem przewiduje przyszłe obserwacje niemal tak dobrze jak znacznie bardziej złożony model lub lepiej generalizuje przy mniejszej ilości danych. Jest to sprawdzalna propozycja dotycząca efektywności reprezentacji. Obecny dokument nie przedstawia takiego wyniku ani przeglądu pozwalającego stwierdzić pierwszeństwo.

### F2. Kontekstowe przewidywania o różnicach między drogami zmiany — MAJOR
**Miejsce:** rozdz. 9.2, 12, 13: H8/H10/H24.

Potencjalnie wartościowe są prerejestrowane przewidywania, że np. utrata osobistego poparcia przy utrzymanym obowiązku ma inne następstwa niż zdjęcie obowiązku przy utrzymanym poparciu. Aby były swoiste dla DMTRD, trzeba wykazać, co dodaje topologia lub historia ponad znane zmienne SDT, obciążenie i zasoby. Sama różnica następstw utraty motywacji i utraty presji nie jest nowym odkryciem.

### F3. Falsyfikowalne ograniczenia zmian po określonych interwencjach — MAJOR
**Miejsce:** rozdz. 10.2, 18: etap 5.

Oryginalny wkład mógłby polegać na trafnym przewidywaniu, które drogi zmian są ograniczone w danych warunkach i kiedy pojawiają się bezpośrednie zmiany wielowymiarowe. Wymaga to predykcji wyprowadzonych przed badaniem i pomiaru wszystkich trzech wymiarów. Nie można zakładać, że manipulacja zasobami wpływa wyłącznie na C, a wsparcie autonomii wyłącznie na W.

**Bilans:** nie ma wystarczających podstaw do nazwania DMTRD nowatorską teorią. Są kandydaci na wkład empiryczny, nie dowiedzione innowacje.

## G. Zmiany niezbędne przed rozpoczęciem badań empirycznych

„Przed badaniami” należy rozumieć proporcjonalnie: wywiady poznawcze i mały pilotaż pomiaru mogą służyć dopracowaniu definicji; nie należy przedstawiać ich jako potwierdzającej walidacji HPE. Przed kosztownym badaniem głównym konieczne są wszystkie kroki poniżej.

| ID / priorytet | Zmiana i odniesienie do dokumentu | Kryterium zakończenia |
|---|---|---|
| G1 — CRITICAL | Ustalić jedno znaczenie W, C i N; rozdz. 3–4, 8. | Jedna sytuacja ma jednoznaczną regułę kodowania; zgodne opisy internalizacji w 110/111; jasno odrębna intencja. |
| G2 — MAJOR | Zdefiniować jednostkę analizy i zakres; rozdz. 2, 11, 14.2. | To samo działanie, kontekst i horyzont we wszystkich pomiarach; działania przygotowawcze i konkurencyjne oznaczone osobno. |
| G3 — CRITICAL | Wybrać podstawowy model pomiaru i stanów; rozdz. 7.3, 14.1. | Jawna specyfikacja emisji/progów, błędu, ograniczeń i oznaczania klas; ocena identyfikowalności oraz odzyskiwania parametrów. |
| G4 — CRITICAL | Uzgodnić HPE z planem testu; rozdz. 7.2–7.3, 13.1, 14.2. | Ograniczenia na Q dla panelowego CTMC, alternatywa z wielobitowymi skokami i ta sama warstwa pomiaru; brak arbitralnego progu 15%. |
| G5 — MAJOR | Oddzielić kody, mechanizmy i skutki; rozdz. 8–11, 17. | Neutralne etykiety, dodatkowe miary autonomii/internalizacji/moral distress i zachowania; bez wniosków diagnostycznych z kodu. |
| G6 — MAJOR | Ograniczyć badanie do kilku rozstrzygających hipotez; rozdz. 13–14. | Jedno główne pytanie dynamiczne i jedno predykcyjne, określone efekty minimalne, okna czasu, kontrasty i reguły wyniku nierozstrzygającego. |
| G7 — MAJOR | Ustalić porównania konkurencyjne i walidację; rozdz. 13: HG1/HG5, 14.2. | Wspólny wynik i horyzont, model ciągły oraz model bez HPE, podział czasowy i po osobach, brak przecieku przyszłych danych. |
| G8 — MAJOR | Dopasować EMA i analizę mocy do informacji o przejściach; rozdz. 14.2, 18. | Symulacje częstości stanów, czasów trwania, błędu, braków danych i heterogeniczności; odzyskiwanie Q oraz kontrola błędnych decyzji. |
| G9 — MAJOR | Poprawić konkretne hipotezy i źródła; rozdz. 13, bibliografia, aneks G. | Usunięte błędy H4/H16/H22, określone mediacje i zdarzenia, poprawny DOI Corley; źródła wspierają dokładnie przypisane twierdzenia. |

### Minimalny projekt rzetelnego badania po rewizji — MAJOR
**Miejsce wymagające zastąpienia planem operacyjnym:** rozdz. 14 i 18.

1. **Jeden rodzaj powtarzalnego działania w jednej populacji.** Wybrać zadanie o realnej zmienności osobistego poparcia, wykonalności i obowiązku. Nie łączyć od razu moral distress personelu medycznego z nauką języka i hobby. Osiągalność wszystkich ośmiu stanów ocenić empirycznie, nie wymuszać rekrutacją pod oczekiwaną topologię.
2. **Wywiady poznawcze i pilotaż pomiarowy.** Sprawdzić, jak uczestnicy rozumieją „chcę”, „mogę” i „powinienem”, zwłaszcza obowiązek dobrowolny, awersję i brak okazji. Zachować informację ilościową. Osobno mierzyć intencję oraz niezbędne moderatory, zamiast włączać je niejawnie do WCN.
3. **EMA z pomiarem przed oknem zachowania.** Stosować dokładne znaczniki czasu. Odpowiedź o stanie poprzedza prospektywne okno wyniku; raport po działaniu jest oznaczony jako pomiar potencjalnego następstwa. Gęstość i zróżnicowanie odstępów ustalić na podstawie pilotażu i symulacji, a nie arbitralnie co 30 minut lub 2–3 godziny.
4. **Wiarygodny wynik.** Główny wynik to wykonanie konkretnego działania w ustalonym oknie, najlepiej z niezależnym śladem behawioralnym. Odróżnić brak działania mimo okazji od braku okazji. Wypalenie i moral distress badać jako odrębne wyniki z odpowiednią skalą czasu; nie diagnozować ich samym stanem.
5. **Niewielki zestaw modeli.** Porównać model ciągły, model konfiguracji bez HPE oraz CTMC/HMM z HPE. W modelach dyskretnych zachować wspólny pomiar. Osobno sprawdzić prostszy generator niezależnych zmian bitów: sześć intensywności bazowych wobec maksymalnie 24 zależnych od konfiguracji, zanim doda się wiele moderatorów.
6. **Odzyskiwanie parametrów i falsyfikacja.** Symulować zarówno dane zgodne z HPE, jak i alternatywy: skoki wielobitowe, ciągłe procesy progowane, zależność od czasu trwania, błąd pomiaru i heterogeniczność. Wymagać nie tylko mocy, ale też właściwej częstości fałszywych odrzuceń, pokrycia przedziałów i precyzji rzadkich przejść. N i T mają wynikać z tego kroku.
7. **Weryfikacja prospektywna.** Ocenić przyszłe zachowanie i przyszłe wskaźniki w zablokowanej części czasowej oraz u nowych osób. Korzyść prostoty oddzielić od wyższej trafności. Wypisać z góry, jaka strata względem modelu ciągłego przekreśla praktyczną użyteczność binarnej kompresji.
8. **Dopiero następnie test mechanizmu.** Randomizować konkretną interwencję, mierzyć wszystkie W,C,N i alternatywne drogi oddziaływania. Efekt interwencji na przejścia nie jest automatycznie dowodem mediacji; mediacja wymaga określonego porządku czasowego i dodatkowych założeń identyfikacyjnych.

**Odpowiedź na pytanie o wykonalność:** rzetelne badanie jest możliwe. Obecny plan nie jest jeszcze gotowym protokołem. Najbardziej osiągalnym pierwszym celem jest ustalenie, czy trzy dobrze określone oceny mają stabilny pomiar chwilowy i czy ich dyskretyzacja zachowuje użyteczną informację o przyszłym zachowaniu. Rozstrzygnięcie o atomowości procesów psychologicznych jest znacznie trudniejsze.

## H. Zmiany pożądane, ale niekonieczne do pierwszego ograniczonego badania

| Uwagi | Miejsce | Znaczenie | Priorytet |
|---|---|---|---|
| Pokazać diagram oddzielający stan, wskaźniki, predyktory kontekstowe i zachowanie. | 7, 10–11, 14 | Ułatwi kontrolę, czy np. autonomia jest definicją W, przyczyną W czy jego skutkiem. | MINOR |
| Rozwinąć wersję semi-Markowską lub jawną historię dopiero po porównaniu z modelem podstawowym. | 7.3, 12 | Ważne dla dalszej teorii; nie trzeba od razu estymować wszystkich rozszerzeń. | MAJOR |
| Przeprowadzić późniejszą replikację w innym kontekście i kulturze. | 16, 18 | Potrzebna do szerszego uogólnienia, nie warunek wstępnego testu w jasno ograniczonej populacji. | MAJOR |
| Opracować miarę kosztu oddzielającą wysiłek, negatywny afekt, utracone alternatywy i koszt czasu. | 7.4, 9.2 | Bez niej „koszt” pozostaje metaforą; można pominąć ten moduł w pierwszym badaniu. | MAJOR |
| Doprecyzować parametry pochodne. | 7.3–7.4 | `−q_ii` mierzy tempo wyjścia, więc większa wartość oznacza mniejszą stabilność; lepszą intuicję daje czas trwania. W DTMC z trzema sąsiadami są łącznie 24 wolne parametry przejść, nie 24+8 niezależnych. Suma diagonalna generatora powinna biec po `j≠i`; zapis `j=i` w DOCX wymaga korekty. | MINOR |
| Nadać prawdopodobieństwu osiągnięcia horyzont czasu lub konkurencyjny cel. | 7.4 | W skończonym nieprzywiedlnym łańcuchu prawdopodobieństwo dotarcia kiedyś do niepustego zbioru wynosi 1. Bez horyzontu ta wielkość może nie różnicować stanów. | MINOR |
| Poprawić organizację tabel i aneksów. | 7.2, 9, 15.2, aneks A | Rozdz. 7.2 odsyła do tabeli 2 jako listy przejść, choć to tabela stanów; tabela 15.2 zawiera ponownie H1–H24 przed pytaniami krytycznymi; aneks A zapowiada pełną tabelę, a dokument pokazuje skróty. Utrudnia to kontrolę hipotez. | MINOR |
| Przeprowadzić redakcję językową. | cały dokument, szczególnie 4, 9–10, 14–15 | Literówki, obcojęzyczne wtręty i ucięte nazwy procesów obniżają jednoznaczność, lecz ich naprawa nie rozwiąże problemów naukowych. | MINOR |

Automatyczne dodawanie kolejnych bitów I, A, H i podtypów N nie jest rekomendowanym domyślnym rozwiązaniem. Intencja, zachowanie i kontekst mogą być odrębnymi zmiennymi w modelu; liczba stanów nie musi rosnąć do 16, 32 lub więcej.

## I. Najważniejsze pytania do autora

| Nr | Pytanie | Miejsce | Priorytet |
|---|---|---|---|
| I1 | Czy W oznacza chwilową ochotę, autonomiczną akceptację działania, jego ocenę czy zamiar? Jak zakodować „nie mam ochoty, lecz dobrowolnie uznaję to za ważne”? | 3–4.1, 8 | CRITICAL |
| I2 | Dlaczego zinternalizowany obowiązek ma w jednym miejscu N=0, a w innym N=1? Jaka obserwacja rozstrzyga tę różnicę? | 4.3, 8.4–8.5 | CRITICAL |
| I3 | Czy C jest oceną subiektywną czy warunkiem realnym? Jak kodowany jest sukces przy C=0 i niepowodzenie przy C=1? | 4.2, 11 | MAJOR |
| I4 | Co znaczy „niezależność”: odrębna treść, brak korelacji czy autonomiczny mechanizm zmian? | 2, 6.2, 10.2, 14 | MAJOR |
| I5 | Co jest elementarnym procesem niezależnie od liczby zmienionych bitów? Jaki wynik nie będzie tłumaczony nieobserwowanymi krokami? | 5, 7.2, 13: HG2 | CRITICAL |
| I6 | Czy osiem stanów to umowne kategorie czy hipoteza o naturalnych reżimach? Co autor przewiduje, jeśli model ciągły wyraźnie lepiej prognozuje? | 7–8, 13: HG1 | MAJOR |
| I7 | Która dokładna parametryzacja pomiaru i przejść ma być estymowana, ile ma parametrów i jakie dowody identyfikowalności? | 7.3, 14 | CRITICAL |
| I8 | Czy HPE dotyczy Q czy P dla odstępu EMA? Dlaczego rozdział 14 narzuca warunek sprzeczny z rozdziałem 7.3? | 7.3, 14.2 | CRITICAL |
| I9 | Jak odróżnić internalizację od chwilowego wzrostu chęci przy 011→111? | 9, 13: H7 | MAJOR |
| I10 | Dlaczego 101 miałoby identyfikować moral distress bez pomiaru moralnego zdarzenia i cierpienia? | 8.3, 13: HG4 | MAJOR |
| I11 | Czy ten sam kod ma tę samą dynamikę niezależnie od historii i rodzaju N? Jeśli nie, co jest pełnym stanem modelu? | 8.5, 12 | MAJOR |
| I12 | Jakie przewidywanie DMTRD nie jest odtwarzalne przez ciągłe WCN z interakcjami lub istniejące zmienne TPB/SDT? | 6.2, 13: HG5, 14 | MAJOR |
| I13 | Co pozostaje tym samym działaniem w przykładach szukania zasobów, delegacji i mentoringu? | 9, 11, aneks A | MAJOR |
| I14 | Jak zostanie zmierzony koszt przejścia i dlaczego miałby wynikać z nierówności q_ij i q_ji? | 7.4, 9.2, 13: HG3 | MAJOR |
| I15 | Które wyniki zmuszą autora do porzucenia HPE, ośmiu stanów lub tezy o przewadze predykcyjnej, zamiast rozszerzania modelu? | 13, 15–19 | CRITICAL |

## J. Selektywna weryfikacja źródeł i twierdzeń

### Ustalenia wymagające korekty bibliografii

**J1 — MAJOR; bibliografia, rozdz. 8.3, 13: HG4, 14.1.** DOI przypisany Corley i współautorom (2001), `10.1046/j.1365-2648.2001.01659.x`, prowadzi do **Johnson, Long i White, „Arguments for 'British Pluralism' in qualitative health research”, 33(2), 243–249**, a nie do skali moral distress. Rekord Europe PMC potwierdza poprawny DOI artykułu Corley: **`10.1046/j.1365-2648.2001.01658.x`**, PMID **11168709**, strony **250–256**. Artykuł o skali istnieje; błąd dotyczy identyfikatora. To istotne, bo źródło jest centralne dla proponowanej walidacji 101.

**J2 — MINOR; bibliografia.** Rekord artykułu Sheerana i współautorów (2016) zawiera również **Aya Avishai-Yitshak**, pominiętą w bibliografii dokumentu. Tytuł i DOI są zgodne. Korekta autorstwa jest potrzebna, ale nie zmienia zasadniczej oceny modelu.

### Rejestr źródeł wykorzystanych w recenzji

Poniższe oznaczenia pozwalają odtworzyć sprawdzenie. „Metadane” nie oznaczają przeczytania pełnej publikacji; „abstrakt” nie poświadcza szczegółów niewidocznych w abstrakcie.

| ID | Źródło i identyfikator | Faktycznie sprawdzony zakres i znaczenie |
|---|---|---|
| S1 | Ajzen, I. (1991). *The theory of planned behavior*. Organizational Behavior and Human Decision Processes, 50(2), 179–211. DOI: [10.1016/0749-5978(91)90020-T](https://doi.org/10.1016/0749-5978(91)90020-T). | Metadane Crossref. Interpretacja relacji postawa–norma–kontrola–intencja oparta także na wiedzy naukowej; strona autorska zwróciła 403, nie potwierdzono nią pełnego tekstu. |
| S2 | Deci, E. L., Ryan, R. M. (2000). *The “what” and “why” of goal pursuits: Human needs and the self-determination of behavior*. Psychological Inquiry, 11(4), 227–268. DOI: [10.1207/S15327965PLI1104_01](https://doi.org/10.1207/S15327965PLI1104_01). | Teorię i odniesienie do publikacji sprawdzono na stronie [Center for Self-Determination Theory](https://selfdeterminationtheory.org/theory/), zwłaszcza opis OIT. Pobranie PDF przez narzędzie nie dało czytelnego tekstu, więc nie deklaruję weryfikacji całego artykułu. |
| S3 | Michie, S., van Stralen, M. M., West, R. (2011). *The behaviour change wheel: A new method for characterising and designing behaviour change interventions*. Implementation Science, 6, 42. DOI: [10.1186/1748-5908-6-42](https://doi.org/10.1186/1748-5908-6-42). | Europe PMC, PMID [21513547](https://europepmc.org/article/MED/21513547): metadane i abstrakt, potwierdzające capability–opportunity–motivation oraz ramę interwencji. Szczegółowy podział motywacji jest elementem znanej konstrukcji COM-B. Strona wydawcy wymagała obsługi JavaScript. |
| S4 | Morley, G., Ives, J., Bradbury-Jones, C., Irvine, F. (2019; online 2017). *What is 'moral distress'? A narrative synthesis of the literature*. Nursing Ethics, 26(3), 646–662. DOI: [10.1177/0969733017724354](https://doi.org/10.1177/0969733017724354). | Europe PMC, PMID [28990446](https://europepmc.org/article/MED/28990446): metadane i abstrakt. Potwierdza spór definicyjny oraz proponowane powiązanie zdarzenia moralnego i cierpienia. Nie jest dowodem, że jedna definicja jest jedyną uznaną. |
| S5 | Sheeran, P., Maki, A., Montanaro, E., Avishai-Yitshak, A., Bryan, A., Klein, W. M. P., Miles, E., Rothman, A. J. (2016). *The impact of changing attitudes, norms, and self-efficacy on health-related intentions and behavior: A meta-analysis*. Health Psychology, 35(11), 1178–1188. DOI: [10.1037/hea0000387](https://doi.org/10.1037/hea0000387). | Europe PMC, PMID [27280365](https://europepmc.org/article/MED/27280365): metadane i abstrakt; 204 testy eksperymentalne. Wspiera rolę znanych determinant, nie HPE i ośmiu stanów. |
| S6 | MacCallum, R. C., Zhang, S., Preacher, K. J., Rucker, D. D. (2002). *On the practice of dichotomization of quantitative variables*. Psychological Methods, 7(1), 19–40. DOI: [10.1037/1082-989X.7.1.19](https://doi.org/10.1037/1082-989X.7.1.19). | Europe PMC, PMID [11928888](https://europepmc.org/article/MED/11928888): metadane i abstrakt o konsekwencjach dychotomizacji. |
| S7 | Hamaker, E. L., Kuiper, R. M., Grasman, R. P. P. P. (2015). *A critique of the cross-lagged panel model*. Psychological Methods, 20(1), 102–116. DOI: [10.1037/a0038889](https://doi.org/10.1037/a0038889). | Europe PMC, PMID [25822208](https://europepmc.org/article/MED/25822208): metadane i abstrakt; problem mieszania stałych różnic międzyosobniczych z dynamiką wewnątrzosobniczą. |
| S8 | Wood, W., Neal, D. T. (2007). *A new look at habits and the habit-goal interface*. Psychological Review, 114(4), 843–863. DOI: [10.1037/0033-295X.114.4.843](https://doi.org/10.1037/0033-295X.114.4.843). | Europe PMC, PMID [17907866](https://europepmc.org/article/MED/17907866): metadane i abstrakt o nawykach, kontekście i celach. Abstrakt nie poświadcza uniwersalnego odsetka 40–50% zachowań. |
| S9 | Corley, M. C., Elswick, R. K., Gorman, M., Clor, T. (2001). *Development and evaluation of a moral distress scale*. Journal of Advanced Nursing, 33(2), 250–256. DOI: [10.1046/j.1365-2648.2001.01658.x](https://doi.org/10.1046/j.1365-2648.2001.01658.x). | Europe PMC, PMID [11168709](https://europepmc.org/article/MED/11168709): metadane i abstrakt; 214 pielęgniarek, 32 pozycje skali. Nie waliduje kodu 101 ani przeniesienia skali bez adaptacji na każdą populację. |
| S10 | Howard, J. L., Gagné, M., Bureau, J. S. (2017). *Testing a continuum structure of self-determined motivation: A meta-analysis*. Psychological Bulletin, 143(12), 1346–1377. DOI: [10.1037/bul0000125](https://doi.org/10.1037/bul0000125). | Europe PMC, PMID [29048175](https://europepmc.org/article/MED/29048175): metadane i abstrakt; 486 prób, ponad 205 tys. osób. Wspiera uporządkowaną wielowymiarową strukturę, ujawnia też problemy odrębności części podskal. Nie dowodzi, że każdy wymiar DMTRD musi być ciągły. |
| S11 | Ryan, R. M., Deci, E. L. (2020). *Intrinsic and extrinsic motivation from a self-determination theory perspective: Definitions, theory, practices, and future directions*. Contemporary Educational Psychology, 61, 101860. DOI: [10.1016/j.cedpsych.2020.101860](https://doi.org/10.1016/j.cedpsych.2020.101860). | Metadane Crossref; wskazanie późniejszego opracowania definicji SDT. Pełnego tekstu nie weryfikowano w tej sesji. |
| S12 | Jackson, C. (2011). *Multi-State Models for Panel Data: The msm Package for R*. Journal of Statistical Software, 38(8), 1–28. DOI: [10.18637/jss.v038.i08](https://doi.org/10.18637/jss.v038.i08). | [Strona czasopisma i abstrakt](https://www.jstatsoft.org/article/view/v038i08): modele panelowe, intensywności zależne od kowariat i HMM z błędną klasyfikacją. |
| S13 | Nodelman, U., Shelton, C. R., Koller, D. (2002). *Continuous Time Bayesian Networks*. Proceedings of UAI 2002, 378–387. Repozytorium: [arXiv:1301.0591](https://arxiv.org/abs/1301.0591), DOI repozytorium: [10.48550/arXiv.1301.0591](https://doi.org/10.48550/arXiv.1301.0591). | Sprawdzono rekord i abstrakt; rekord wskazuje UAI 2002, choć kopię zgłoszono do arXiv w 2012 r. Równoważność rodziny generatorów dla trzech bitów wynika z porównania parametryzacji, nie z empirycznej walidacji WCN w tej publikacji. |

Weryfikację rekordów biomedycznych/psychologicznych wykonano przez publiczny interfejs Europe PMC, ponieważ bezpośredni dostęp do części stron PubMed/wydawców był blokowany przez wymagania przeglądarki. Dwa wyszukiwania DOI nie zwróciły rekordu w Europe PMC; jedno źródło potwierdzono następnie w Crossref, a niepotwierdzonego w tej sesji źródła o identyfikowalności nie użyto jako podstawy cytowania. Nie sprawdzono wszystkich pozycji bibliografii dokumentu ani każdej proponowanej skali. Błędy odczytu technicznego nie były traktowane jako nieistnienie publikacji.

## K. Mapa pokrycia 14 pytań recenzenckich

| Zagadnienie | Główne uwagi |
|---|---|
| 1. Trafność CHCĘ, MOGĘ, POWINIENEM | B1–B3, C4 |
| 2. Rozłączność i niezależność | B4, B9, C4 |
| 3. Osiem stanów | B5–B6, C2–C3 |
| 4. Interpretacja 24 przejść | B7 — kompletna tabela, C8 |
| 5. Pojedyncza zmiana bitu | B8, C1 |
| 6. Procesy Markowa | A3, B9, C1–C2, C7 |
| 7. Binarność | B5, B8, C3, E3 |
| 8. Motywacja a działanie | B1, B10–B11, C5 |
| 9. Identyfikowalność | C2, C4–C5, G3 |
| 10. Falsyfikacja | C1, C7–C10, G4/G6 |
| 11. Zgodność z literaturą | B6, B11, E, J |
| 12. Oryginalność względem TPB, SDT, COM-B i innych | E1–E2, F |
| 13. Wartość predykcyjna | C5–C6, F1–F2, G7 |
| 14. Rzetelne badanie empiryczne | C9, G — projekt i kryteria gotowości |

## Ostateczna rekomendacja dla kolejnej rewizji

**Zachować:** jawne kodowanie konfiguracji, rozdzielenie kierunków przejść, poprawną formalizację CTMC i kilka kontrastów o niezależnie mierzalnych skutkach.

**Przebudować:** definicje WCN, powiązanie konfiguracji z mechanizmami, model pomiaru, test HPE i procedurę porównań predykcyjnych. Ogólna deklaracja „to tylko hipotezy” nie usuwa sprzeczności między rozdziałami.

**Wycofać jako aktualnie nieuzasadnione:** utożsamienie 101 z moral distress, identyfikowanie działania/autonomii/wypalenia z pojedynczym kodem, tezę o nowości samej topologii oraz deklarację gotowej falsyfikowalnej specyfikacji 24 hipotez.

**Rozstrzygnięcie:** klasyfikacja — potencjalnie użyteczna; spójny model teoretyczny — jeszcze nie; empirycznie testowalna teoria — możliwy kierunek rozwoju po zasadniczej rewizji. Najważniejszym sprawdzianem nie będzie odnalezienie ośmiu kodów w danych, lecz wykazanie, że ustalone z góry ograniczenia DMTRD zachowują trafność przy uwzględnieniu błędu pomiaru i przewidują coś istotnego ponad prostsze modele.
