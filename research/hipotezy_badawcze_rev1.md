# Hipotezy Badawcze DMTRD – Wersja rev1 (po rewizji ASTRA)

**Wersja:** 1.0  
**Data:** 07.11.2026  
**Status:** Przeopisane po rewizji krytycznej ASTRA  
**Kluczowa zmiana:** Redukcja z 24 hipotez szczegółowych do **3 hipotez głównych (główne testy potwierdzające)** + hipotezy eksploracyjne.

---

## 1. Hipotezy Główne (DMTRD-core) – Testy Potwierdzające

Te 3 hipotezy stanowią **zamknięty zestaw testów potwierdzających (confirmatory)**. Ich wynik decyduje o trafności wersji core DMTRD. Pozostałe hipotezy są eksploracyjne.

**Ważne rozróżnienia metodologiczne:**

- **HPE-model vs HPE-empiryczna**: HPE-model to ograniczenie na generatorze Q (qᵢⱼ = 0 dla d_H ≥ 2). HPE-empiryczna to hipoteza o danych obserwowanych (odsetek d_H ≥ 2 mniejszy niż w modelach alternatywnych). Nawet prawdziwy HPE-model generuje d_H ≥ 2 w P(Δt) = exp(QΔt).
- **M_indep jako szczególny przypadek HPE-model**: Model niezależnych bitów (6 intensywności) to HPE-model z dodatkowym ograniczeniem qᵢⱼ zależnych tylko od bitu, nie konfiguracji. Test HPE-model vs M_indep weryfikuje, czy intensywności zależą od kontekstu (W,C,N).
- **Liczba parametrów**: M_HPE = 24 qᵢⱼ; M_full = 56 qᵢⱼ; M_indep = 6 intensywności; M_cont = parametry procesu ciągłego.
- **Warunki porównania modeli**: Ten sam wynik (zachowanie/stan), te same dane, ten sam horyzont predykcji. Porównanie AIC/BIC między modelami o różnych zmiennych wynikowych jest nieuczciwe.
- **Nieistotność ≠ dowód równoważności**: LRT n.s. (p > 0.05) to brak dowodu PRZECIW HPE-model, nie dowód JEGO POPRAWNOŚCI. Równoważność wymaga testów ekwiwalencji (TOST) lub Bayes factor.
- **Test Diebold-Mariano**: Wymaga sprawdzenia założeń (stacjonarność, niezależność reszt) – dla zależnych czasowo danych EMA może być nieadekwatny. Alternatywa: walidacja krzyżowa blokowa / rolling window z log-loss.

| Id | Nazwa | Formalna treść | Alternatywa | Zmienne | Metoda | Kryterium sukcesu | Kryterium odrzucenia |
|----|-------|----------------|-------------|---------|--------|-------------------|----------------------|
| **HPE** | **Test HPE-model** | Generator CTMC spełnia HPE-model: $q_{ij} = 0$ dla $d_H \geq 2$. | M_full (56 wolnych $q_{ij}$), M_indep (6 intensywności), M_cont (procesy ciągłe) | $Q$ (generator CTMC) oszacowany z danych EMA | Estymacja CTMC (MLE/Bayesian); LRT: M_HPE vs M_full (bootstrap parametryczny); AIC/BIC; walidacja krzyżowa log-loss | LRT n.s. ($p > 0.05$) – brak istotnej poprawy dopasowania przez M_full; ΔAIC > 10 na korzyść M_HPE; log-loss out-of-sample niższy lub równy dla M_HPE | LRT istotne ($p < 0.05$) – M_full dopasowuje istotnie lepiej; ΔAIC < 2 na korzyść M_full |
| **HPD** | **Path Dependence (zależność od historii)** | Stabilność/przyszłość stanu zależy od drogi dojścia (path dependence). Formalnie: model rzędu 2 / z zmiennymi latentnymi historii lepiej dopasowuje dane niż model Markowski rzędu 1. | Model Markowski rzędu 1 (bezpamięciowy) | Trajektorie stanów; zmienne latentne historii (np. liczba cykli, czas od ostatniej zmiany W/C/N) | Porównanie: CTMC rzędu 1 vs CTMC rzędu 2 / HMM z historią / CTMC z kowariancjami zależnymi od czasu; LRT, AIC, BIC | LRT: $p < 0.05$ na korzyść modelu z historią; ΔAIC > 6 na korzyść modelu z historią | LRT n.s. ($p > 0.10$) LUB ΔAIC < 2 na korzyść modelu Markowskiego |
| **HPP** | **Wartość predykcyjna topologii Q3 (HPE-model)** | Model CTMC z HPE-model (24 parametry $q_{ij}$ zależnych od konfiguracji) lepiej przewiduje przyszłe zachowanie i stany niż: (a) model ciągły W,C,N z interakcjami, (b) model 8 konfiguracji bez HPE (24 wolne $q_{ij}$ bez kowariancji), (c) prosty model autoregresyjny zachowania. | (a) Regresja ciągła W,C,N z interakcjami; (b) Model 8 stanów bez HPE (24 $q_{ij}$ bez kowariancji); (c) AR(1) zachowania | Przewidywanie $Behavior_{t+\Delta t}$ i $State_{t+\Delta t}$ | Walidacja out-of-sample (leave-one-person-out / rolling window); log-loss, Brier score, kalibracja | Log-loss out-of-sample istotnie niższy dla DMTRD-core vs wszystkie modele referencyjne (test DM / walidacja krzyżowa $p < 0.05$); kalibracja (Brier score) lepsza | Brak przewagi predykcyjnej vs model ciągły / bez HPE / AR(1) (Δlog-loss n.s., test DM n.s.) |

### Kryteria odrzucenia wersji DMTRD-core
Wersję core odrzucamy, jeśli **którakolwiek** z 3 hipotez głównych zostanie odrzucona. Nie dopuszczamy "ratowania" wersji core poprzez dodawanie wymiarów, progów, moderatorów, pamięci po zobaczeniu danych.

---

## 1.1. Status hipotez do prerejestracji

| Hipoteza | Status | Uzasadnienie |
|----------|--------|--------------|
| **HPE** | Gotowa do prerejestracji | Pełna specyfikacja: model, parametry, alternatywy, metoda estymacji (CTMC z bootstrap), kryteria sukcesu/odrzucenia |
| **HPD** | Gotowa do prerejestracji | Pełna specyfikacja: model rzędu 1 vs rzędu 2/HMM, zmienne latentne historii, LRT/AIC |
| **HPP** | Gotowa do prerejestracji (z zastrzeżeniem DM) | Pełna specyfikacja, ale test Diebold-Mariano wymaga weryfikacji założeń na danych EMA; zalecana walidacja krzyżowa blokowa jako metoda podstawowa |
| **H_MD** | Koncepcyjna | Wymaga operacjonalizacji kontekstu moralnego i skali MDS |
| **H_Nsource** | Koncepcyjna | Wymaga finalizacji kategoryzacji N_source |
| **H_Habit, H_Affect_Valence, H_Cost, H_Scope** | Koncepcyjne | Wymagają definicji operacyjnych nowych konstruktów (H, koszt) |
| **E1–E24** | Eksploracyjne | Nie są testami potwierdzającymi; generują hipotezy do przyszłych badań |

---

## 2. Hipotezy Eksploracyjne (dawniej H1–H24, poprawione i zgrupowane)

Te hipotezy są **eksploracyjne** – generują hipotezy do przyszłych badań, nie są testami potwierdzającymi wersji core. Oznaczone jako **E1–E24** (odpowiedniki dawnych H1–H24, poprawione).

### 2.1. Przejścia zmieniające W (CHCĘ)

| Id | Przejście | Hipoteza eksploracyjna (poprawiona) | Uwagi / Poprawki vs dawny H |
|----|-----------|-------------------------------------|------------------------------|
| **E1** | 000→100 | Wzrost *outcome expectancies* (SCT) i *self-efficacy* (SCT/TPB) przewiduje wzrost W (0→1) przy C=N=0. | Dawny H1: OK, ale "self-efficacy" to predyktor C, nie W. Doprecyzowanie: *outcome expectancies* (wartość wyniku) → W. |
| **E2** | 100→000 | Niska *self-efficacy* i negatywne *outcome expectancies* przewidują spadek W (1→0) przy C=N=0. | Dawny H2: OK. Dodatkowo: *goal disengagement* (Wrosch) jako moderator. |
| **E3** | 001→101 | *Perceived Autonomy Support* (mPAS) mediuje przejście 001→101 (internalizacja N→W) poprzez wzrost *Identified Regulation* (SDT). | Dawny H3: "Internalizacja" to zmiana $N_{source}$ (external→identified), nie koniecznie zmiana W. Doprecyzowanie: mediator = *Identified Regulation* (SDT), outcome = W. |
| **E4** | 101→001 / 101→011 | Brak *perceived control* → 101→001 (rezygnacja z W); silne *subjective norms* (TPB) → 101→011 (compliance bez W). | Dawny H4: **BŁĄD** – 101→011 zmienia DWA bity (W i C). Poprawa: to nie jest pojedyncza krawędź HPE. Hipoteza dotyczy *następnego* przejścia po 101 (multinomial logit na kategorię następnego stanu). |
| **E5** | 010→110 | *Intrinsic Motivation* (IMI Interest/Enjoyment) i *Autonomy Support* przewidują 010→110. | Dawny H5: "Intrinsic motivation" pokrywa się treściowo z W. Doprecyzowanie: predyktor = *Interest/Enjoyment* (IMI) – skala zewnętrzna do W. |
| **E6** | 110→010 | Niskie *Autonomy Support* przewiduje 110→010 (utrata W). Moderator: *Job Demands* (JD-R). | Dawny H6: OK. "Wypalenie" to outcome, nie predyktor. Predyktor = niskie AS + wysokie JD. |
| **E7** | 011→111 | *Perceived Autonomy Support* i *Identified Regulation* (SDT) mediują 011→111 (internalizacja). | Dawny H7: "Internalizacja" = zmiana $N_{source}$ (introjected→identified) + wzrost W. Mediator = *Identified Regulation*. |
| **E8** | 111→011 | Przejście 111→011 (utrata W przy N=1) silniej predykuje *wypalenie* (MBI) niż 111→110 (utrata N przy W=1). | Dawny H8: OK. Wymaga definicji wypalenia jako zdarzenia (Cox) lub ciągłej skali (regresja). Kontrast: 111→011 vs 111→110. |

### 2.2. Przejścia zmieniające C (MOGĘ)

| Id | Przejście | Hipoteza eksploracyjna (poprawiona) | Uwagi / Poprawki vs dawny H |
|----|-----------|-------------------------------------|------------------------------|
| **E9** | 000→010 | *Mastery Experience* (Bandura) przewiduje 000→010 (wzrost C). | Dawny H9: OK. "C rośnie stopniowo" – HPE zakłada skok, ale w danych ciągłych C rośnie stopniowo; progowanie generuje skok. |
| **E10** | 010→000 | Utrata C bez W/N (010→000) mniej stresogenna (niższy PANAS negatywny, niższy PSS) niż utrata C przy W=1 (110→100, 111→101). | Dawny H10: OK. Kontrast: 010→000 vs 110→100 vs 111→101. |
| **E11** | 001→011 | *Perceived Organizational Support* (POS) przewiduje 001→011 (empowerment w roli). | Dawny H11: OK. "Empowerment" szersze niż C; tu: wzrost C przy N=1. |
| **E12** | 011→001 | 011→001 (utrata C przy N=1) silniej predykuje *intencję odejścia* (Turnover Intention) niż 011→010. | Dawny H12: OK. "Moral distress" to outcome, nie mechanizm. Outcome = Turnover Intention. |
| **E13** | 100→110 | *Implementation Intentions* (Gollwitzer) mediują 100→110 (planowanie → wzrost C). | Dawny H13: "Przełamanie barier" to outcome. Mediator = *Implementation Intentions* (II). Outcome = C. |
| **E14** | 110→100 | 110→100 (utrata C przy W=1) częściej prowadzi do *persistencji* (powrót 100→110) niż do *rezygnacji* (100→000). | Dawny H14: OK. Analiza trajektorii (sekwencje stanów). |
| **E15** | 101→111 | *Problem-focused Coping* (Brief COPE) i *Social Support* (MSPSS) przewidują 101→111 (rozwiązanie konfliktu). | Dawny H15: OK. "Rozwiązanie konfliktu" = wzrost C przy W=1, N=1. |
| **E16** | 111→101 | 111→101 (utrata C przy W=1, N=1) silniej predykuje *ostre stresowe reakcje* (ASDS) i *PTSD* (PCL-5) niż inne utraty C (110→100, 011→001, 010→000). | Dawny H16: **BŁĄD** – dawny kontrast "inne utraty C" zawierał 111→110 i 111→011, które ZACHOWUJĄ C=1. Poprawa: kontrast z 110→100, 011→001, 010→000 (utrata C). "PTSD" wymaga właściwej ekspozycji i horyzontu czasu (Cox/regresja). |

### 2.3. Przejścia zmieniające N (POWINIENEM)

| Id | Przejście | Hipoteza eksploracyjna (poprawiona) | Uwagi / Poprawki vs dawny H |
|----|-----------|-------------------------------------|------------------------------|
| **E17** | 000→001 | *Autonomy Support* rozróżnia internalizację (→101: wzrost W) od compliance (→011: brak wzrostu W). | Dawny H17: OK. Interakcja AS × Internalization (Kelman). |
| **E18** | 001→000 | *Role Ambiguity* i niskie *Role Commitment* przewidują 001→000 (odrzucenie roli). | Dawny H18: OK. Cox model (czas do 001→000). |
| **E19** | 010→011 | 010→011 przy niskim *Autonomy Support* przewiduje kolejne 011→001 (rezygnacja z C), nie 011→111. | Dawny H19: OK. Analiza trajektorii z moderacją AS. |
| **E20** | 011→010 / 011→001 | Wysoka *Autonomy* → 011→010 (wolność); niska *Autonomy* → 011→001 (bezsilność). | Dawny H20: OK. Moderacja *Autonomy* (multinomial logit). |
| **E21** | 100→101 | *Personal Norm* (Schwartz) → 100→101→111 (internalizacja moralna); *Subjective Norms* (TPB) → 100→101→001 (compliance). | Dawny H21: OK. Moderacja *Personal Norm* vs *Subjective Norms*. |
| **E22** | 101→100 | Wysoka *Goal Identification* (W) przy 101→100 zapobiega 100→000 (rezygnacji z celu). | Dawny H22: **BŁĄD** – po 101→100, W=1 i N=0 są stałe. Interakcja W × N_change nieidentyfikowalna w podpróbie. Poprawa: test na pełnej próbie z ciągłymi W, N; lub inna próba. |
| **E23** | 110→111 | *Organizational Identification* i *Prosocial Motivation* przewidują 110→111 (wzrost N). Outcome = N (wzrost), nie OCB (zachowanie). | Dawny H23: **BŁĄD** – OCB to zachowanie, nie zmiana N. Outcome = N (wzrost). Mediatory: *Org Identification*, *Prosocial Motivation*. |
| **E24** | 111→110 | Planowana *Succession Planning* przy 111→110 nie predykuje wypalenia; 111→011 (utrata W) tak. | Dawny H24: OK. Kontrast: 111→110 (z SP) vs 111→011 (bez SP). Cox/SEM na trajektorie wypalenia. |

---

## 3. Hipotezy Dodatkowe (Nowe, wynikające z rewizji)

| Id | Nazwa | Treść | Status |
|------|-------|-------|--------|
| **H_MD** | **Moral Distress a stan 101** | W sytuacjach o moralnym charakterze (mierzone kontekstem), stan 101 (W=1, C=0, N=1) predysponuje do *moral distress* (MDS, Corley) i predykuje wypalenie/odjście. | Eksploracyjna |
| **H_Nsource** | **Źródło obowiązku ($N_{source}$) moderuje dynamikę N** | $N_{source}$ (external vs identified/integrated) moderuje: (a) prawdopodobieństwo 011→111 (internalizacja), (b) stabilność 111, (c) reakcję na 111→011 vs 111→110. | Eksploracyjna |
| **H_Habit** | **Siła nawyku (H) moderuje przejścia W↔0 przy C=1** | Wysoka *HabitStrength* (SRHI) hamuje 010→110 (trudność przejęcia kontroli) i ułatwia 110→010 (automatyzacja). | Eksploracyjna (wymaga parametru H) |
| **H_Affect_Valence** | **Walenność afektu przy zmianach W i C** | Wzrost W/C (0→1) związany z pozytywnym afektem (PANAS+); spadek W/C (1→0) związany z negatywnym afektem (PANAS-), **ALE** spadek W przy C=0, N=1 (101→001) może dawać *ulgę* (pozytywny afekt) – test dwukierunkowy. | Eksploracyjna |
| **H_Cost** | **Operacjonalizacja "kosztu" przejścia** | "Koszt" = funkcja: (a) wysiłek (self-report), (b) negatywny afekt (PANAS-), (c) utracone alternatywy (decisional regret), (d) czas. Test: czy koszt 011→111 < 001→101? Czy koszt 111→011 > 111→110? | Eksploracyjna (wymaga definicji operacyjnej kosztu) |
| **H_Scope** | **Zakres modelu: System 2 vs System 1** | Model DMTRD-core (W,C,N) przewiduje zachowania nienawykowe (System 2). Dla zachowań nawykowych (SRHI > próg) siła predykcyjna spada; parametr H (siła nawyku) poprawia predykcję. | Eksploracyjna (wymaga parametru H) |

---

## 4. Specyfikacja Metodologiczna Wspólna (dla wszystkich hipotez)

### 4.1. Pomiar W, C, N (EMA)
- **Wersja bazowa:** Skale Likert 1–7 dla każdego wymiaru (3 itemy główne).
- **Wersja binarna (do wizualizacji/Q3):** Próg >4 na skali 1–7 (wartość 4 = neutralność → 0 lub wykluczona).
- **Czas wypełnienia:** < 30 sekund (3 itemy główne).
- **Losowa kolejność itemów.**

### 4.2. Pomiar zachowania
- Samoraport: "Czy wykonałeś działanie od ostatniego pomiaru?" (tak/nie) + czas trwania/intensywność.
- Opcjonalnie obiektywne: akcelerometr, logi aplikacji, systemy CRM.

### 4.3. Częstotliwość EMA
- **Losowe:** 5×/dzień (9:00–21:00), odstępy ~2–3h (dopasowane w symulacjach).
- **Event-based:** do 1h po działaniu (max 3/dzień) – oznaczane jako *potencjalny skutek* wykonania.
- **Całkowity czas:** 14–21 dni.
- **Łącznie:** ~100–150 pomiarów/osoba.

### 4.4. Analiza statystyczna
1. **CTMC (msm/ctmcm):** Estymacja $Q$ z danych panelowych. Test HPE: LRT (M_HPE vs M_full). Test asymetrii: LRT ($q_{ij} = q_{ji}$).
2. **Regresje logistyczne wielopoziomowe (lme4/brms):** Przewidywanie przejść (E1–E24).
3. **SEM (lavaan/Mplus):** Mediacje (E3, E7, E13, E15, E23).
4. **Analiza przeżycia (survival):** Cox regression (E2, E6, E8, E12, E18, E24).
5. **Analiza sekwencji / trajektorii:** TraMineR / seqHMM (E4, E14, E19, E24).
6. **Modele rzędu wyższego / HMM z historią:** Test HPD (path dependence).

### 4.6. Walidacja trafności konstruktu
- CFA: 3 czynniki (W,C,N) – CFI>0.95, RMSEA<0.06, SRMR<0.08.
- Dyskryminacyjna: AVE > kwadrat korelacji między czynnikami (Fornell-Larcker).
- Kryterialna: Korelacje ze skalami referencyjnymi (IMI, GSE, MDS, POS, MBI).

### 4.7. Walidacja trafności predykcyjnej
- Przewidywanie zachowania (następny pomiar) ze stanu (bieżący pomiar).
- Porównanie z TPB, SDT, COM-B (regresje zagnieżdżone).
- Kryteria: AIC, BIC, R², moc predykcyjna out-of-sample (walidacja krzyżowa).

### 4.8. Analiza mocy
- Symulacja Monte Carlo (N=100–500, T=50–150, efekty małe/średnie/duże).
- Cel: moc > 0.80 dla testów HPE (d_H≥2), asymetrii (qᵢⱼ≠qⱼᵢ), mediacji (E3, E7).
- Plan: 1000 replikacji, raportowanie mocy dla różnych N, T, wielkości efektu.

---

## 5. Czynniki Zakłócające (Ogólne)

| Czynnik | Opis | Kontrola |
|---------|------|----------|
| Reaktywność pomiaru | EMA zmienia stan motywacyjny | Grupa kontrolna bez EMA / tylko event-based; analiza trendów w czasie |
| Selekcja próby | Uczestnicy zmotywowani do udziału | Rekrutowanie różnorodne; analiza nierespondentów |
| Pamięć/retrospekcja | Błędy w samoraporcie zachowania | Event-based EMA (do 1h po działaniu); dane obiektywne gdzie możliwe |
| Kontekst sytuacyjny | Stres, afekt, zdarzenia życiowe | Pomiar PANAS, PSS, zdarzeń życiowych w EMA; kontrola statystyczna |
| Nawyk/automatyzm | System 1 nie modelowany w DMTRD-core | Krótkie itemy nawyku (SRHI) w EMA; analiza podgrup (nawykowe vs nienawykowe) |
| Różnice indywidualne | Cechy osobowości, demografia | Kontrola: Big Five, wiek, płeć, wykształcenie, staż |
| Sezonowość/tydzień | Wzorce cykliczne motywacji | Efekty losowe dla dnia tygodnia, tygodnia badania |

---

## 6. Plan Symulacji Mocy (do wykonania przed Etapem 3)

1. **Generowanie danych:** CTMC z Q (z literatury / eksperci) dla N=100, 200, 300, 500; T=50, 100, 150.
2. **Efekty:** Małe (OR=1.5), średnie (OR=2.5), duże (OR=4.0) dla przejść kluczowych (E1, E3, E7, E8, E15).
3. **Modele do testowania:** LTA (8 klas), CTMC (Q), Regresje logistyczne wielopoziomowe.
4. **Testy:** HPE (d_H≥2), Asymetria (qᵢⱼ≠qⱼᵢ), Mediacja (E3, E7), Predykcja zachowania.
5. **Replikacje:** 1000 per warunek.
6. **Output:** Tabele mocy dla każdego testu × N × T × wielkość efektu.
7. **Decyzja:** Minimalne N i T dla mocy >0.80 przy efekcie średnim.

---

## 6. Podsumowanie Zmian vs Wersja Pierwotna

| Kategoria | Wersja pierwotna | Wersja rev1 |
|-----------|------------------|-------------|
| Liczba hipotez głównych | 5 (HG1–HG5) | **3 (HPE, HPD, HPP)** |
| Liczba hipotez szczegółowych | 24 (H1–H24) | **24 eksploracyjne (E1–E24) + 6 nowych** |
| HG1 (dopasowanie modelu) | Porównanie AIC/BIC z TPB/SDT/COM-B (różne modele/zmienne) | **Usunięta** – nieuczciwe porównanie (C6) |
| HG2 (HPE) | Prog 15% zmian d_H≥2 przy EMA co 30 min | **Usunięta** – arbitralna, niezgodna z CTMC (C1) |
| HG3 (asymetria) | Próg 50% par z qᵢⱼ≠qⱼᵢ | **Usunięta** – arbitralny próg (C7) |
| HG4 (101 = moral distress) | Równość 101 = moral distress | **Usunięta** – nieuzasadniona równość (B6) → H_MD jako eksploracyjna |
| HG5 (wartość Q3) | Porównanie R² out-of-sample vs modele płaskie | **Zastąpiona HPP** – uczciwe porównanie z modelami referencyjnymi na tym samym wyniku |
| H4, H16, H22 | Błędy: wielobitowe przejścia, błędne kontrasty, identyfikowalność | **Poprawione** jako E4, E16, E22 z uwagami |
| H3, H7, H13, H15 | "Mediuje" bez jednoznacznej specyfikacji X, M, Y | **Poprawione** jako E3, E7, E13, E15 z jawnego X, M, Y |
| H23 | OCB jako outcome zmiany N | **Poprawione** jako E23: outcome = N (wzrost), nie OCB |

---

*Dokument wersja 1.0. Gotowy do zastosowania w Etapie 2 (walidacja psychometryczna) i Etapie 3 (EMA pilotażowe). Wszystkie hipotezy główne (HPE, HPD, HPP) są testy potwierdzające; pozostałe to hipotezy eksploracyjne do przyszłych badań.*