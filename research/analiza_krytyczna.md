# Analiza Krytyczna Modelu DMTRD

## Status: Wersja robocza do recenzji

---

## 1. Wstęp

Niniejszy dokument zawiera systematyczną analizę krytyczną modelu DMTRD, zgodnie z wymaganiami etapu 1 projektu. Analiza opiera się na 20 pytaniach krytycznych zdefiniowanych w zadaniu, zidentyfikowaniem 5 najpoważniejszych argumentów przeciwko modelowi oraz propozycjami poprawek.

---

## 2. 20 pytań krytycznych – analiza

### P1: Czy trzy wymiary są rzeczywiście niezależnymi konstruktami?
**Analiza:** W, C, N korelują w badaniach empirycznych (np. self-efficacy koreluje z motywacją; normy z intencją). CFA na danych przekrojowych konieczne.
**Ryzyko:** Wysokie. Jeśli korelacje > 0.7, dyskryminacyjna trafność konstruktu zagrożona.
**Akcja:** Test CFA (3 czynniki) na próbie N≥300; AVE > kwadrat korelacji.

### P2: Czy zmienne binarne nadmiernie upraszczają motywację?
**Analiza:** Tak. SDT rozróżnia 6 typów regulacji; TPB/SCT/Goal-Setting używają skal ciągłych. Binarne W traci: intryntyczną vs zidentyfikowaną vs introjektowaną motywację. Binarne C traci gradację self-efficacy (kluczową w SCT). Binarne N miesza: normy opisowe, inskryptywne, moralne, rolowe, zinternalizowane.
**Ryzyko:** Krytyczne. Utrata wariancji wyjaśnionej, niemożność przewidywania natężenia/trwałości.
**Poprawka:** Wersja ciągła W,C,N ∈ [0,1] lub Likert 1–7; stany = oktaanty w sześcianie.

### P3: Czy jeden bit może odpowiadać elementarnemu procesowi psychologicznemu?
**Analiza:** HPE to hipoteza, nie fakt. Psychologicznie: internalizacja normy (N: 0→1) często towarzyszy wzrostowi motywacji (W: 0→1) – np. 001→111 (d_H=2). Ambiwalencja może generować równoczesne zmiany. Ograniczona częstotliwość EMA (np. 2-3h) maskuje sekwencje.
**Ryzyko:** Wysokie. Wymaga weryfikacji w gęstym EMA (np. co 30 min) lub CTMC.
**Test:** Analiza sekwencji w EMA – odsetek zmian d_H=1 vs d_H≥2.

### P4: Czy możliwe są równoczesne zmiany wielu wymiarów?
**Analiza:** Tak. Ambiwalencja (Lewin), bifurkacje (Vallacher & Nowak), internalizacja zrównoleglą (001→111), moral distress resolution (101→111 może wiązać się ze zmianą C i W). HPE zakłada sekwencyjność.
**Ryzyko:** Średnie. Rozwiązanie: CTMC z qᵢⱼ=0 dla d_H≥2 na poziomie generatora, ale P(Δt) pozwala na d_H≥2 przy Δt>0.

### P5: Czy model ma wartość wyjaśniającą większą niż klasyczne modele?
**Analiza:** Nieznane. Wymaga porównania out-of-sample: DMTRD (LTA/CTMC) vs TPB (regresja) vs SDT (SEM) vs COM-B (regresja logistyczna). Kryteria: AIC, BIC, R², moc predykcyjna.
**Ryzyko:** Nieznane. Hipoteza HG1: DMTRD lepiej dopasowuje dane EMA dzięki topologii stanów.

### P6: Czy nazwa „POWINIENEM” nie łączy nadmiernie różnych kategorii normatywnych?
**Analiza:** Tak – to najpoważniejszy problem konstruktowy. N łączy: normy opisowe (Cialdini – inni robią), inskryptywne (inni oczekują), moralne (Schwartz – internalizowane), rolowe (Kahn – obowiązki stanowiska), zinternalizowane (Kelman – identyfikacja), eksternalne (TPB – presja społeczna). To różne mechanizmy psychologiczne z różnymi konsekwencjami (compliance vs internalizacja vs identyfikacja).
**Ryzyko:** Krytyczne. Stan 011 może być compliance (eksternalne N) LUB introjektowana regulacja (wewnętrzne N) – DMTRD nie rozróżnia.
**Poprawka:** Rozdzielić N na: N_soc (normy społeczne opisowe/inskryptywne), N_mor (normy moralne personalne), N_rol (obowiązki rolowe). 3 bity zamiast 1 → 5 wymiarów (32 stany) lub model hierarchiczny N.

### P7: Czy „MOGĘ” nie miesza samooceny kompetencji z obiektywnymi możliwościami?
**Analiza:** Tak. C = subiektywna wykonalność (bliższe PBC Ajzena). Self-efficacy (Bandura) = wiara w zdolność do organizacji/wykonania; PBC = postrzegana łatwość/trudność (mieszanka self-efficacy i kontroli środowiskowej). COM-B rozdziela: Capability (psychologiczna/fizyczna – wewnętrzne) i Opportunity (społeczna/fizyczna – zewnętrzne). DMTRD scala to w jednym bicie.
**Ryzyko:** Wysokie. Utrata możliwości rozróżnienia: "umiem, ale nie mam czasu" (Opportunity=0, Capability=1) vs "mam czas, ale nie umiem" (Capability=0, Opportunity=1).
**Poprawka:** Rozdzielić C na Capability (wewnętrzne) i Opportunity (zewnętrzne) – jak COM-B.

### P8: Czy „CHCĘ” oznacza przyjemność, preferencję, intencję czy autonomiczną motywację?
**Analiza:** W DMTRD: W = osobista akceptacja i motywacja (autonomiczna w sensie SDT). Nie jest to: przyjemność (hedonizm), preferencja (wybór), intencja (TPB – plan), ani motywacja intryntyczna (tylko jeden typ w SDT). W=1 obejmuje intryntyczną, zidentyfikowaną, zintegrowaną regulację.
**Ryzyko:** Wysokie. Nieprecyzyjna definicja utrudnia operacjonalizację i walidację.
**Poprawka:** Precyzyjna definicja operacyjna + CFA z IMI (Interest/Enjoyment) i SDT (Autonomous Motivation).

### P9: Czy model uwzględnia ambiwalencję?
**Analiza:** Nie. Binarne W (0/1) nie pozwala na współistnienie chęci i niechęci. Ambiwalencja (Lewin, Miller; Greenwald & Nosek – implicit-explicit discrepancy) to kluczowy predyktor zachowań zdrowotnych, uzależnień, decyzji moralnych. DMTRD: 101 (chcę + powinienem, nie mogę) ≠ ambiwalencja (to napięcie, nie współistnienie tendencji do/przeciw).
**Ryzyko:** Średnie. Dla wielu zachowań (nawykowe, uzależnienia, decyzje moralne) ambiwalencja jest centralna.
**Poprawka:** Wersja ciągła W ∈ [-1,1] (ambivalencja = blisko 0) lub dodanie 4. wymiaru A (ambiwalencja).

### P10: Czy może wyjaśnić działanie pomimo braku świadomej motywacji?
**Analiza:** Nie w obecnej formie. Działania nawykowe (System 1; Wood & Neal) zachodzą przy W=0, C=1 (stan 010/011). DMTRD interpretuje to jako "brak motywacji" lub "compliance", a to normalne działanie automatyczne. Przejścia 010↔110 nie oddają dynamiki nawyków (formowanie przez powtarzanie, łamanie przez kontrolę wykonywczą).
**Ryzyko:** Wysokie. Model nie dotyczy większości zachowań codziennych.
**Poprawka:** Dodać parametr H (siła nawyku) modyfikujący przejścia; rozdzielić System 1/2.

### P11: Czy uwzględnia nawyki?
**Analiza:** Nie – patrz P10. To fundamentalna luka. COM-B ma Automatic Motivation; dual-process theories rozdzielają System 1/2. DMTRD to model wyłącznie refleksywny.
**Ryzyko:** Wysokie. Niska walidacja ekologiczna.

### P12: Czy jest wrażliwy na kontekst społeczny i kulturowy?
**Analiza:** Niejawnie. N obejmuje normy społeczne/rolowe (kontekst), ale model nie ma zmiennych kontekstowych (Xₜ) wpływających na Q/P. Kultura wpływa na: siłę norm (kultury kolektywistyczne → silniejsze N), autonomię (kultury indywidualistyczne → silniejsze W), definicję ról.
**Ryzyko:** Średnie. Wymaga testów cross-cultural i modeli multiniveau.

### P13: Czy historia przejść zmienia późniejszą dynamikę?
**Analiza:** Model Markowski (bezpamięciowy) zakłada, że nie. Psychologicznie: tak. Ścieżka do 111: 000→100→110→111 (budowanie autonomii) vs 000→001→011→111 (internalizacja normy) – różna jakość 111. Wielokrotne cykle 110→010→110 mogą budować odporność LUB wrażliwość (sensytyzacja).
**Ryzyko:** Wysokie. Wymaga modeli z path dependence (łańcuch rzędu wyższego, semi-Markowski ze zmiennymi latentnymi, CTMC z kowariancjami zależnymi od historii).

### P14: Czy założenia są falsyfikowalne?
**Analiza:** Tak. H1–H24 (przejścia), HG1–HG5 (ogólne) są specyficzne, mają zmienne, pomiar, analizę, czynniki zakłócające. HPE (d_H=1) falsyfikowalne przez obserwację d_H≥2 w gęstym EMA. Asymetria (qᵢⱼ ≠ qⱼᵢ) testowalna w CTMC.
**Status:** Spełnione.

### P15: Czy model jest identyfikowalny statystycznie?
**Analiza:** Nie w wersji binarnej. 3 wskaźniki binarne → 8 wzorców odpowiedzi = 8 klas latentnych = model nasycony (0 df). LTA/HMM nie testowalne bez: wskaźników ciągłych (Likert), dodatkowych zmiennych (zachowanie, afekt, kontekst), silnych ograniczeń (np. równość qᵢⱼ).
**Ryzyko:** Krytyczne. Wymaga wersji ciągłej lub rozszerzonego modelu pomiarowego.

### P16: Czy może być używany do prognozowania zachowania?
**Analiza:** Nieznane. Model opisuje stan motywacyjny, nie deterministycznie zachowanie. Prognoza wymaga: P(zachowanie | stan) + model przejść. Wymaga walidacji predykcyjnej out-of-sample vs TPB/SDT/COM-B.
**Ryzyko:** Nieznane. Wymaga badania EMA z pomiarem zachowania.

### P17: Czy istnieje ryzyko tautologicznego wyjaśniania działania?
**Analiza:** Średnie. Jeśli stan 111 definiowany jest jako "stan przed działaniem" i działanie następuje, to tautologia. Rozwiązanie: rozdzielenie stanu motywacyjnego od zachowania (wymiar A ∈ {0,1}), pomiar zachowania niezależny od self-reportu stanu.
**Ryzyko:** Średnie. Wymaga wymiaru A (Działanie).

### P18: Czy model wymaga dodatkowego wymiaru reprezentującego faktyczne działanie?
**Analiza:** Tak. Stan (W,C,N) ≠ działanie. Wymiar A ∈ {0,1} (Działanie: tak/nie) → 16 stanów (Q₄). Pozwala modelować: 111→111 (stan utrzymany, działanie wykonane), 111→110 (stan zmieniony, działanie nie wykonane), volicję (Kuhl) jako przejście 111(A=0)→111(A=1).
**Ryzyko:** Wysokie. Fundamentalna luka teoretyczna.

### P19: Czy model ośmiu stanów jest najlepszą reprezentacją, czy tylko użyteczną abstrakcją?
**Analiza:** Użyteczna abstrakcja. Wersja ciągła (oktaanty w [0,1]³) zachowuje topologię Q3, ale dodaje gradację. 8 stanów = dyskretyzacja dla uproszczenia modelowania Markowskiego i interpretacji. Wersja ciągła lepsza psychometrycznie, dyskretna – do modelowania Markowskiego/LTA.
**Ryzyko:** Średnie. Obie wersje warto testować.

### P20: W jakich zastosowaniach model może wprowadzać w błąd?
**Analiza:** 
- Działania nawykowe (System 1) – stan 010/011 to normalne działanie, nie "brak motywacji".
- Ambiwalencja – binarne W nie uchwyci współistnienia tendencji.
- Patologie kliniczne – depresja (W=0, C=0, N=1?) vs apatia vs anhedonia – model nie rozróżnia.
- Różnice kulturowe – siła N, W, definicja ról zależna od kultury.
- Działania z silnym komponentem hedonistycznym – W nie rozróżnia przyjemności od sensu.
- Interwencje behawioralne – brak narzędzia jak BCW (COM-B).

---

## 3. Pięć najpoważniejszych argumentów przeciwko DMTRD

### ARG1: Binarność traci istotną wariancję
- **Problem:** Wszystkie teorie referencyjne (TPB, SDT, SCT, Goal-Setting, COM-B) używają skal ciągłych. Binarne W traci typy motywacji (intryntyczna vs zidentyfikowana vs introjektowana); binarne C traci gradację self-efficacy; binarne N traci kategorie norm (moralne, rolowe, społeczne).
- **Znaczenie:** Redukcja siły wyjaśniającej, niemożność przewidywania natężenia zachowania/trwałości.
- **Konsekwencje:** Model może nie wyjaśniać wariancji, którą wyjaśniają modele ciągłe.
- **Poprawka:** Zmienne ciągłe W,C,N ∈ [0,1] lub Likert 1–7; stany = oktaanty.
- **Wpływ na prostotę/oryginalność:** Utrata prostej topologii Q3, trudniejsza interpretacja, ale większa wierność psychologiczna.

### ARG2: Brak intencji i celu – luka teoretyczna
- **Problem:** TPB, Rubikon, HAPA, Goal-Setting, Carver & Scheier – intencja/cel centralne. DMTRD: stan (W,C,N) bez intencji ani celu. Stan 111 może oznaczać gotowość (preactional) lub działanie (actional).
- **Znaczenie:** Brak mechanizmu łączącego stan z działaniem; niejasność: czy 111 = intencja czy volicja?
- **Konsekwencje:** Trudność w przewidywaniu zachowania; niejasne rozróżnienie motywacji vs volicji.
- **Poprawka:** Dodać 4. wymiar I (Intencja) → Q₄ (16 stanów) lub modelować I jako funkcję (W,C,N).
- **Wpływ na prostotę/oryginalność:** Podwojenie stanów, większa złożoność, ale zamknięcie luki teoretycznej.

### ARG3: Pomijanie automatyzmu/nawyku – większość działań
- **Problem:** Wood & Neal (2007) – 40–50% codziennych działań nawykowych (System 1). DMTRD: stan 010/011 interpretowany jako "brak motywacji", a to normalny stan działania nawykowego. Przejścia 010↔110 nie oddają dynamiki nawyków (formowanie/łamanie).
- **Znaczenie:** Model nie dotyczy większości zachowań codziennych; ryzyko fałszywych wniosków.
- **Konsekwencje:** Niska walidacja ekologiczna; trudność w zastosowaniu do interwencji nawykowych.
- **Poprawka:** Dodać parametr H (siła nawyku) modyfikujący przejścia; rozdzielić System 1/2.
- **Wpływ na prostotę/oryginalność:** Significante ułożenie modelu, nowy wymiar złożoności.

### ARG4: N miesza kategorie normatywnych – konstrukt niejednolity
- **Problem:** N łączy normy opisowe (Cialdini), inskryptywne (Cialdini), moralne (Schwartz), rolowe (Kahn), zinternalizowane (Kelman), eksternalne (TPB). To różne psychologiczne mechanizmy z różnymi konsekwencjami (compliance vs internalizacja vs identyfikacja).
- **Znaczenie:** Stan 011 może być compliance (eksternalne N) lub introjektowana regulacja (wewnętrzne N) – DMTRD nie rozróżnia. Stan 111 z N eksternalnym ≠ 111 z N zinternalizowanym.
- **Konsekwencje:** Nieprecyzyjne przewidywania; utrata zdolności do rozróżnienia jakości zaangażowania.
- **Poprawka:** Rozdzielić N na: N_soc (normy społeczne), N_mor (normy moralne), N_rol (obowiązki rolowe).
- **Wpływ na prostotę/oryginalność:** 3 bity zamiast 1 → 5 wymiarów (32 stany) lub hierarchiczny model N.

### ARG5: Identyfikowalność modelu – problem statystyczny
- **Problem:** 3 wskaźniki binarne → 8 wzorców odpowiedzi = 8 klas latentnych = model nasycony (0 df). Nie da się testować dopasowania LTA/HMM bez dodatkowych założeń. CTMC wymaga wysokiej częstotliwości pomiarów (EMA), co jest kosztowne i reaktywne.
- **Znaczenie:** Trudność w empirycznej weryfikacji; ryzyko overfittingu; ograniczone wnioskowanie.
- **Konsekwencje:** Model może pozostać nienawiązany empirycznie przez długi czas.
- **Poprawka:** Wymagać wskaźników ciągłych (Likert) + dodatkowych zmiennych (zachowanie, afekt, kontekst) lub silnych ograniczeń (np. równość qᵢⱼ w grupach).
- **Wpływ na prostotę/oryginalność:** Większe wymagania pomiarowe, ale identyfikowalność.

---

## 4. Podsumowanie ocen

| Kryterium | Ocena | Uzasadnienie |
|-----------|-------|--------------|
| Spójność pojęciowa | PARTIAL | N miesza kategorie; W, C nieprecyzyjnie zdefiniowane |
| Spójność matematyczna | PASS | Q3, HPE, modele Markowa – spójne formalnie |
| Trafność literatury | PASS | Analiza 10 teorii, mapowanie konstruktów |
| Rozróżnienie faktów/hipotez | PASS | HPE, asymetria, stan 101 jasno oznaczone jako hipotezy |
| Oryginalność | PARTIAL | Q3, HPE, N niezależny, stan 101 – nowość; 3 filary – redukcja MOA/COM-B/TPB |
| Wartość predykcyjna | NIEZNANA | Wymaga walidacji EMA out-of-sample |
| Falsyfikowalność | PASS | H1–H24, HG1–HG5 specyficzne |
| Operacjonalizacja | PARTIAL | Binarna wersja – saturated model; ciągła – wymaga testów |
| Jakość badań | PARTIAL | Plan EMA solidny, ale brak danych pilotażowych |

---

## 5. Rekomendowane priorytety poprawek (przed Etapem 2)

1. **KRYTYCZNE:** Rozdzielić N na podwymiary (N_soc, N_mor, N_rol) – bez tego interpretacje stanów 011, 101, 111 są dwuznaczne.
2. **KRYTYCZNE:** Przejść na wersję ciągłą W,C,N (Likert 1–7) dla identyfikowalności LTA/HMM i wierności psychologicznej.
3. **WYSOKIE:** Dodać wymiar A (Działanie) – rozdzielenie stanu motywacyjnego od zachowania.
4. **WYSOKIE:** Dodać parametr H (Nawyk/Automatyzm) – modelowanie System 1.
5. **ŚREDNIE:** Rozważyć wymiar I (Intencja) lub modelować I jako funkcję (W,C,N).
6. **ŚREDNIE:** Rozdzielić C na Capability/Opportunity (jak COM-B).

---

*Dokument przygotowany do recenzji. Wszystkie oceny wymagają weryfikacji empirycznej.*