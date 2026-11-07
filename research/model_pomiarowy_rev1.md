# Model Pomiarowy DMTRD – Specyfikacja G3 (rev1)

**Wersja:** 1.0  
**Data:** 07.11.2026  
**Status:** Specyfikacja zgodna z rekomendacjami ASTRA (G3)  
**Cel:** Jednoznaczna specyfikacja modelu pomiarowego do badania pilotażowego i głównego.

---

## 1. Przegląd modelu

### 1.1. Filozofia pomiarowa
- **Stan (W,C,N) ≠ zachowanie.** Stan to konfiguracja ocen motywacyjnych; zachowanie to zmienna wynikowa.
- **Wersja ciągła (bazowa):** $W,C,N \in [1,7]$ Likert. Zachowuje informację o natężeniu, gradacji, unika błędów progu.
- **Wersja binarna (uproszczenie):** $W,C,N \in \{0,1\}$ (próg 4). Tylko do wizualizacji Q3, interpretacji, nie do estymacji.
- **Stan ≠ klasa latentna.** W modelu bazowym stany są **obserwowane bezpośrednio** (observed states) – unika problemu identyfikowalności LTA/HMM z 3 wskaźnikami binarnymi.

### 1.2. Trzy role zmiennych (kluczowe rozróżnienie)

| Rola | Zmienne | Przykłady | Uwagi |
|------|---------|-----------|-------|
| **Stan (State)** | $W_{it}, C_{it}, N_{it}$ | Itemy Likert 1–7 dla W, C, N | Definiują stan w CTMC; **nie zawierają zachowania** |
| **Predyktory / Moderatory (Exogenous)** | $X_{it}$ | AutonomySupport, Resources, RoleAmbiguity, HabitStrength, $N_{source}$ | Wpływają na generator $Q$ (intensywności $q_{ij}$) |
| **Wyniki (Outcomes)** | $Y_{it}$ | Behavior, Affect (PANAS), Burnout (MBI), MoralDistress (MDS) | Przewidywane ze stanu; **nie** wskaźniki emisji |

**Zasada krytyczna:** Zachowanie, afekt, wypalenie, moral distress to **zmienne wynikowe (outcomes)** przewidywane ze stanu $(W,C,N)$, a **nie** wskaźniki emisji definiujące stan. To unika *criterion contamination* (zanieczyszczenia kryterium).

---

## 2. Specyfikacja zmiennych

### 2.1. Zmienne stanu (State variables) – obserwowane bezpośrednio

| Zmienna | Skala | Item główny (EMA) | Zakres | Rola w modelu |
|---------|-------|-------------------|--------|---------------|
| $W_{it}$ | Likert 1–7 | "W jakim stopniu osobiście akceptujesz wartość tego celu / zgadzasz się z jego realizacją?" | 1–7 | Stan W |
| $C_{it}$ | Likert 1–7 | "W jakim stopniu uważasz, że jesteś w stanie to zrealizować / widzisz sposób na to, by to zrobić?" | 1–7 | Stan C |
| $N_{it}$ | Likert 1–7 | "W jakim stopniu czujesz, że powinieneś to zrobić / to jest Twoje zobowiązanie?" | 1–7 | Stan N |

**Wersja binarna (do wizualizacji/Q3):** Próg 4 na skali 1–7.
- $W_{bin} = 1$ jeśli $W \geq 4$, wpp. 0
- $C_{bin} = 1$ jeśli $C \geq 4$, wpp. 0
- $N_{bin} = 1$ jeśli $N \geq 4$, wpp. 0

### 2.2. Zmienne eksogenne (Predyktory / Moderatory) – wpływ na $Q$

| Zmienna | Skala / Typ | Rola w modelu | Uwagi |
|---------|-------------|---------------|-------|
| $AutonomySupport_{it}$ | Likert 1–7 (mPAS) | Moderator $q_{ij}$ dla przejść W (0→1) | mPAS – skala wsparcia autonomii |
| $Resources_{it}$ | Likert 1–7 / count | Predyktor $q_{ij}$ dla przejść C (0→1) | Dostępne zasoby, czas, wsparcie |
| $RoleAmbiguity_{it}$ | Likert 1–7 (RCS) | Predyktor $q_{ij}$ dla przejść N (1→0) | Ambiguitet roli |
| $RoleConflict_{it}$ | Likert 1–7 (RCS) | Predyktor $q_{ij}$ dla przejść N (0→1) | Konflikt ról |
| $HabitStrength_{it}$ | Likert 1–7 (SRHI) | Moderator $q_{ij}$ dla przejść W (0↔1) | Siła nawyku (opcjonalnie) |
| $N_{source,it}$ | Kategoryczna (7 kat.) | Moderator $q_{ij}$ dla przejść N, W | Źródło obowiązku (external, introjected, identified, integrated, moral, role, legal) |
| $RoleOverload_{it}$ | Likert 1–7 | Predyktor $q_{ij}$ dla przejść N (1→0) | Przeładowanie roli |

### 2.3. Zmienne wynikowe (Outcomes) – przewidywane ze stanu

| Zmienna | Skala / Typ | Horyzont predykcji | Uwagi |
|---------|-------------|-------------------|-------|
| $Behavior_{it}$ | Binarne {0,1} + intensywność | Następne okno EMA ($\Delta t$) | Główna zmienna wynikowa; opcjonalnie obiektywna (akcelerometr, logi) |
| $Affect_{it}$ | PANAS (10+10 itemy) | Współbieżne / następne okno | Pozytywny/negatywny afekt |
| $Burnout_{it}$ | MBI (9 itemy EE+DP+PA) | Tygodniowy / co 2 tygodnie | Wypalenie (skala czasu: tygodnie) |
| $MoralDistress_{it}$ | MDS (Corley) | Po zdarzeniu kryzysowym / co tydzień | Tylko w kontekście moralnym |
| $TurnoverIntention_{it}$ | 3 itemy | Miesięczny | Intencja odejścia z pracy |

---

## 3. Model dynamiczny: CTMC z kowariancjami

### 3.1. Generator $Q$ zależny od kowariancji

$$q_{ij}(X_t) = q_{ij}^0 \cdot \exp(\beta_{ij}^T X_t) \quad \text{dla} \quad d_H(i,j)=1$$

Gdzie:
- $q_{ij}^0$ – intensywność bazowa (intercept)
- $\beta_{ij}$ – wektor współczynników dla kowariancji $X_t$
- $X_t$ – wektor kowariancji w czasie $t$ (AutonomySupport, Resources, itd.)
- Dla $d_H(i,j) \geq 2$: $q_{ij} = 0$ (HPE-model)

### 3.2. Macierz przejścia w czasie dyskretnym (dla porównania z LTA)

$$P(\Delta t) = \exp(Q \Delta t)$$

Dla danych EMA z odstępami $\Delta t$ (zmiennych, znanych z znaczników czasu).

### 3.3. Model bazowy do estymacji (DMTRD-core)

| Parametr | Wartość / Specyfikacja |
|----------|------------------------|
| **Stan** | Obserwowany $(W_{it}, C_{it}, N_{it})$ ciągły 1–7 (dyskretyzacja na 8 stanów próg 4) |
| **Generator $Q$** | 24 wolne parametry $q_{ij}$ ($d_H=1$) + $\beta_{ij}$ dla kowariancji |
| **HPE-model** | $q_{ij}=0$ dla $d_H \geq 2$ (ograniczenie na $Q$) |
| **Estymacja** | MLE / Bayesian (pakiety `msm`/`ctmcm` w R, `ctmcm` w Python) |
| **Dane** | Panel EMA: $N$ osób × $T$ pomiarów, znane $\Delta t$ (znaczniki czasu) |

---

## 4. Modele alternatywne (do porównania w walidacji)

| Model | Opis | Parametry $q_{ij}$ | Cel porównania |
|-------|------|-------------------|----------------|
| **M_HPE (DMTRD-core)** | CTMC z HPE-model + kowariancje | 24 $q_{ij}^0$ + $\beta$ | Model bazowy |
| **M_full** | Pełny generator (bez HPE) | 56 $q_{ij}$ (wszystkie $i \neq j$) | Test HPE (LRT vs M_HPE) |
| **M_indep** | Niezależne bity | 6 intensywności (po 2 na bit) | Test zależności $q$ od konfiguracji |
| **M_cont** | Procesy ciągłe $W,C,N \in [0,1]$ + progowanie | Parametry procesu ciągłego | Test wersji ciągłej vs dyskretnej |
| **M_meas** | HPE-model + błąd klasyfikacji | 24 $q_{ij}$ + parametry błędu | Test wrażliwości na błędy pomiarowe |
| **M_indep_cov** | Niezależne bity + kowariancje | 6 $q_{ij}^0$ + $\beta$ | Test czy kowariancje wyjaśniają zależność od konfiguracji |

---

## 5. Identyfikowalność i estymacja

### 5.1. Dlaczego stany obserwowane (nie latentne)?

| Problem | Rozwiązanie w DMTRD-core |
|---------|--------------------------|
| 3 wskaźniki binarne → 8 wzorców = 8 klas = saturated model (0 df) w LTA pojedynczym pomiarze | **Stany obserwowane bezpośrednio** (wersja ciągła W,C,N) – brak klas latentnych, brak problemu identyfikowalności emisji |
| 9 itemów binarnych (3 na wymiar) → 512 wzorców, ale nadal problem lokalnych zależności i identyfikowalności klas | **Stany obserwowane** – brak problemu emisji; $W,C,N$ to stan, nie wskaźniki |
| Identyfikowalność praktyczna: rzadkie stany (np. 000, 111) → niska precyzja $q_{ij}$ | **Kowariancje $X_t$** zwiększają zmienność w rzadkich stanach; symulacje mocy do planowania N, T |

### 5.2. Estymacja parametrów

| Metoda | Pakiety | Uwagi |
|--------|---------|-------|
| **MLE (CTMC)** | `msm` (R), `ctmcm` (Python) | Standard dla CTMC z danymi panelowymi |
| **Bayesian CTMC** | `rstan`/`brms` (R), `pymc` (Python) | Dla małych N, priorowe informacje o $q_{ij}$ |
| **Bayesian HMM/LTA** | `stan`/`brms` | Jeśli wersja z klasami latentnymi (wersja eksploracyjna) |

### 5.3. Wymagane dane do estymacji

| Parametr | Wartość minimalna (szacunkowa, do potwierdzenia symulacjami) |
|----------|---------------------------------------------------------------|
| $N$ (osoby) | 100–200 (dla estymacji 24 $q_{ij}$ + $\beta$ z mocą > 0.80) |
| $T$ (pomiarów/osobę) | 50–100 (gęstość ~2–3h, 14–21 dni) |
| Odsetek obserwacji ze zmianą stanu | > 10% (dla precyzji rzadkich przejść) |
| Rzadkie przejścia (np. 000→001) | Minimum 5–10 obserwacji na przejście dla precyzji $q_{ij}$ |

---

## 5. Walidacja modelu pomiarowego

### 5.1. Walidacja konstruktu (Etap 2 – pilotaż)

| Aspekt | Metoda | Kryterium sukcesu |
|--------|--------|-------------------|
| **Trafność treści (Content validity)** | Wywiady poznawcze (cognitive interviewing) N=15–20 | > 90% uczestników rozumie itemy zgodnie z definicją |
| **Trafność konstruktu (Construct validity) – CFA** | CFA na danych przekrojowych (N≥300) | CFI > 0.95, RMSEA < 0.06, SRMR < 0.08; 3 czynniki (W,C,N) |
| **Trafność dyskryminacyjna** | Fornell-Larcker: AVE > $r^2$ między czynnikami | AVE(W) > $r^2(W,C)$, AVE(W) > $r^2(W,N)$, itd. |
| **Trafność kryterialna (Convergent)** | Korelacje ze skalami referencyjnymi | W ↔ Identified Regulation (r > 0.6); C ↔ PBC (r > 0.6); N ↔ PN/SN (r > 0.4) |
| **Trafność rozróżniająca (Discriminant)** | HTMT < 0.85 lub Fornell-Larcker | W, C, N odrębne konstrukty |
| **Stabilność w czasie (Within-person reliability)** | ICC(1) / ICC(2) na danych EMA (pilotaż N=30, T=50) | ICC(1) > 0.40 (dla stanów chwilowych); separacja wariancji between/within |

### 5.2. Walidacja predykcyjna (Etap 3 – główne badanie)

| Metoda | Porównanie | Kryterium |
|--------|------------|-----------|
| **Out-of-sample prediction** | DMTRD-core (CTMC) vs M_full vs M_indep vs M_cont vs regresja ciągła W,C,N | Log-loss, Brier score, kalibracja dla $Behavior_{t+1}$ |
| **Walidacja krzyżowa** | Leave-one-person-out / rolling window | ΔLog-loss > 0 na korzyść DMTRD-core |
| **Porównanie z teoriami referencyjnymi** | DMTRD-core vs TPB (intencja→zachowanie) vs SDT (regulacje) vs COM-B (M,O,A) | Taki sam wynik ($Behavior$), te same dane, ten sam horyzont |

---

## 6. Plan badawczy (zgodny z G2, G4, G8)

### 6.1. Etap 2 – Walidacja psychometryczna (N=300–500, przekrój)
- CFA na 3 czynniki (W,C,N) + $N_{source}$ jako kategoryczna
- Walidacja kryterialna ze skalami referencyjnymi
- Wywiady poznawcze (N=20) – weryfikacja zrozumienia itemów
- Test wersji ciągłej vs binarnej (AIC/BIC, predykcja)

### 6.2. Etap 3 – Badanie EMA pilotażowe (N=100, T=14 dni)
- **Jedno działanie, jedna populacja** (np. nauka języka 15 min/dzień, studenci)
- Gęstość próbkowania: pilotaż + symulacje (cel: rozdzielenie skoków elementarnych)
- Event-based EMA: pomiar *przed* oknem zachowania (predyktory) vs *po* (skutki)
- Estymacja CTMC (M_HPE vs M_full vs M_indep) – test HPE (LRT)
- Analiza mocy dla głównego badania (symulacje Monte Carlo)

### 6.3. Etap 4 – Badanie EMA główne (N=300–500, T=21 dni)
- Pełna walidacja predykcyjna out-of-sample
- Analiza path dependence (model rzędu wyższego vs Markowski)
- Test hipotez głównych: HPE-test, HPD (path dependence), HPP (wartość predykcyjna Q3)
- Porównanie z modelami konkurencyjnymi (TPB, SDT, COM-B operacjonalizowane)

### 6.4. Etap 5 – Eksperymenty interwencyjne (Etap 5+)
- Randomizacja interwencji: AutonomySupport (dla W), Resources (dla C), RoleClarity (dla N)
- Pomiar wszystkich W,C,N + alternatywne drogi oddziaływania
- Test mediacji (np. AutonomySupport → W → Behavior)

---

## 7. Symulacje mocy (do wykonania przed Etapem 3)

### 7.1. Parametry symulacji
| Parametr | Wartości |
|----------|----------|
| $N$ | 100, 200, 300, 500 |
| $T$ | 50, 100, 150 pomiarów/osobę |
| Intensywności bazowe $q_{ij}^0$ | Z literatury / eksperci (np. 0.1–1.0 na godzinę) |
| Efekty kowariancji $\beta$ | Małe (OR=1.5), średnie (OR=2.5), duże (OR=4.0) |
| Odstępy pomiarowe $\Delta t$ | 30 min, 1h, 2h, 3h (zmiennie) |
| Błąd klasyfikacji (próg 4) | 0%, 5%, 10%, 20% |

### 7.2. Testy do symulacji
1. **Test HPE:** LRT (M_HPE vs M_full) – moc > 0.80 przy efekcie średnim
2. **Test asymetrii:** LRT ($q_{ij} = q_{ji}$) dla kluczowych par (011↔111, 111↔011, 101↔111, 111↔101)
3. **Test HPE-empiryczna:** Odsetek obserwowanych $d_H \geq 2$ vs model alternatywny
4. **Predykcja zachowania:** Log-loss DMTRD-core vs M_full vs M_indep vs regresja ciągła
5. **Precyzja rzadkich przejść:** RMSE estymacji $q_{ij}$ dla rzadkich stanów (000, 111)

### 7.3. Decyzja: Minimalne N i T
Na podstawie symulacji: ustalenie minimalnych N i T dla mocy > 0.80 przy efekcie średnim dla testów kluczowych (HPE, asymetria, predykcja).

---

## 6. Zmiany względem wersji pierwotnej (rev1)

| Zmiana | Uzasadnienie (ASTRA) |
|--------|----------------------|
| Stan = obserwowane W,C,N (ciągłe), nie klasy latentne | Rozwiązanie problemu identyfikowalności (C2, G3) |
| Wersja ciągła (1–7) jako bazowa; binarna jako uproszczenie | Progowanie traci informację, generuje błędy (C3) |
| Stan ≠ zachowanie; zachowanie = outcome, nie wskaźnik emisji | Unikanie criterion contamination (C5) |
| Model bazowy = CTMC z obserwowanymi stanami + kowariancje | Ujednolicenie HPE-model (Q) z planem testu (C1, G4) |
| Jawna separacja: stan / predyktory / outcomes | Unikanie criterion contamination (C5) |
| Jawne modele alternatywne do porównania (M_full, M_indep, M_cont) | Uczciwe porównanie konkurencyjne (C6, G7) |
| Plan EMA: 1 działanie, 1 populacja, gęstość z symulacji | Unikanie heterogeniczności, dopasowanie rozdzielczości (C9, G8) |
| 3 hipotezy główne (HPE, HPD, HPP) zamiast 24 błędnych | Redukcja do rozstrzygających testów (C8, G6) |

---

*Dokument wersja 1.0. Gotowy do zastosowania w Etapie 2 (walidacja psychometryczna) i Etapie 3 (EMA pilotażowe).*