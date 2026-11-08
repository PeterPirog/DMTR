# Definicje Matematyczne i Formalne – DMTRD

## 1. Przestrzeń Stanów

### 1.1. Wymiarowe przestrzenie
Niech:
- $W \in \{0,1\}$ – CHCĘ (chęć wykonania konkretnego działania)
- $C \in \{0,1\}$ – MOGĘ (subiektywne przekonanie o możliwości wykonania działania)
- $N \in \{0,1\}$ – POWINIENEM (racjonalne przekonanie o konieczności wykonania działania ze względu na swoje cele)

Przestrzeń stanów: $\mathcal{S} = \{0,1\}^3$

### 1.2. Reprezentacja stanu
Stan $s \in \mathcal{S}$ reprezentujemy jako trójkę uporządkowaną:
$$s = (W, C, N)$$

Kod binarny: $s_{bin} = WCN$ (np. $101 = (1,0,1)$)

Liczba stanów: $|\mathcal{S}| = 2^3 = 8$

### 1.3. Wartościowanie (interpretacja) bitów
| Bit | Wartość 0 | Wartość 1 |
|-----|-----------|-----------|
| W | Brak chęci wykonania działania | Chęć wykonania działania |
| C | Przekonanie o braku możliwości | Przekonanie o możliwości |
| N | Brak przekonania o konieczności | Racjonalne przekonanie o konieczności |

**Uwaga:** Wartość 0 **nie** oznacza:
- Dla W: silną niechęć, awersję ani brak intencji (to oddzielne konstrukty)
- Dla C: obiektywną niemożność (to subiektywna ocena; C=0 nie wyklucza wykonania, C=1 nie gwarantuje go)
- Dla N: zakaz ani brak internalizacji (to brak przekonania o konieczności; internalizacja normy to osobna zmienna `N_source`, nie bit w kodzie stanu)

---

## 2. Graf Stanów – Hipersześcian Q3

### 2.1. Definicja grafu
Graf stanów $G = (V, E)$ gdzie:
- $V = \mathcal{S}$ (węzły = 8 stanów)
- $E = \{\{s_i, s_j\} \subseteq V : d_H(s_i, s_j) = 1\}$ (krawędzie nieskierowane)

$d_H$ – odległość Hamminga:
$$d_H(s_i, s_j) = \sum_{k \in \{W,C,N\}} |s_i^k - s_j^k|$$

### 2.2. Właściwości Q3
| Właściwość | Wartość |
|------------|---------|
| Liczba węzłów $|V|$ | 8 |
| Liczba krawędzi nieskierowanych $|E|$ | 12 |
| Liczba przejść kierunkowych | 24 |
| Stopień węzła $\deg(v)$ | 3 (dla każdego $v$) |
| Średnica grafu | 3 |
| Liczba najkrótszych ścieżek między węzłami | Zależy od odległości Hamminga |
| Dwudzielność | Tak (graf bipartytny) |
| Spójność | Spójny |
| Cyklowe | Tak (cykle długości 4, 6, 8) |

### 2.3. Macierz sąsiedztwa (nieskierowana)
Indeksowanie stanów (koleksność leksykograficzna):
0: 000, 1: 001, 2: 010, 3: 011, 4: 100, 5: 101, 6: 110, 7: 111

$$A_{ij} = \begin{cases} 1 & \text{jeśli } d_H(s_i, s_j) = 1 \\ 0 & \text{inaczej} \end{cases}$$

### 2.4. Macierz incydencji kierunkowej
Dla 24 przejść kierunkowych, macierz $24 \times 8$ lub lista krawędzi skierowanych.

---

## 3. Hipoteza Przejść Elementarnych (HPE)

### 3.1. Sformułowanie – HPE-model (ograniczenie modelowe)

**HPE-model:** W generatorze $Q$ łańcucha Markowskiego w czasie ciągłym (CTMC) intensywności przejść między stanami o odległości Hamminga $d_H \geq 2$ są równe zero:

$$q_{ij} = 0 \quad \text{dla} \quad d_H(s_i, s_j) \geq 2$$

To oznacza, że **elementarne skoki** w czasie ciągłym zmieniają dokładnie jeden wymiar. HPE-model to **ograniczenie na strukturę generatora $Q$**, a nie twierdzenie o psychologicznej atomowości procesów.

### 3.2. HPE-empiryczna (hipoteza testowalna)

**HPE-empiryczna:** W danych EMA z gęstym próbkowaniem, odsetek obserwowanych zmian $d_H \geq 2$ między kolejnymi pomiarami jest istotnie mniejszy niż przewidywane przez model alternatywny dopuszczający bezpośrednie skoki wielobitowe (np. model z niezależnymi zmianami bitów lub model z błędami klasyfikacji).

To hipoteza empiryczna, która może zostać zafałszowana. HPE-empiryczna **nie** jest równoznaczna z HPE-model – nawet gdy generator $Q$ spełnia HPE-model ($q_{ij}=0$ dla $d_H \geq 2$), macierz przejścia $P(\Delta t) = \exp(Q\Delta t)$ dla $\Delta t > 0$ może mieć $p_{ij} > 0$ dla $d_H \geq 2$ (przejścia wieloetapowe w jednym interwale pomiarowym).

### 3.3. Modele alternatywne do testowania HPE

Do weryfikacji HPE-empirycznej porównujemy:

- **M1 (HPE-model):** $q_{ij}=0$ dla $d_H \geq 2$ (24 wolne parametry $q_{ij}$)
- **M2 (niezależne bity):** 6 niezależnych intensywności (po 2 na bit: 0→1, 1→0), $q_{ij}$ zależne tylko od zmieniającego się bitu
- **M3 (pełny generator):** 56 wolnych parametrów $q_{ij}$ (wszystkie pary $i \neq j$)
- **M4 (ciągły proces progowany):** zmienne ciągłe $W,C,N \in [0,1]$ z progowaniem na 8 stanów
- **M5 (błąd klasyfikacji):** HPE-model + model błędu pomiarowego/klasyfikacji stanów

Test HPE polega na porównaniu dopasowania M1 vs M2–M5 (LRT, AIC, BIC, walidacja krzyżowa).

### 3.4. Lista 24 przejść dopuszczalnych w HPE-model

| # | Start | Koniec | Zmieniony wymiar | Kierunek |
|---|-------|--------|------------------|----------|
| 1 | 000 | 100 | W | 0→1 |
| 2 | 100 | 000 | W | 1→0 |
| 3 | 001 | 101 | W | 0→1 |
| 4 | 101 | 001 | W | 1→0 |
| 5 | 010 | 110 | W | 0→1 |
| 6 | 110 | 010 | W | 1→0 |
| 7 | 011 | 111 | W | 0→1 |
| 8 | 111 | 011 | W | 1→0 |
| 9 | 000 | 010 | C | 0→1 |
| 10 | 010 | 000 | C | 1→0 |
| 11 | 001 | 011 | C | 0→1 |
| 12 | 011 | 001 | C | 1→0 |
| 13 | 100 | 110 | C | 0→1 |
| 14 | 110 | 100 | C | 1→0 |
| 15 | 101 | 111 | C | 0→1 |
| 16 | 111 | 101 | C | 1→0 |
| 17 | 000 | 001 | N | 0→1 |
| 18 | 001 | 000 | N | 1→0 |
| 19 | 010 | 011 | N | 0→1 |
| 20 | 011 | 010 | N | 1→0 |
| 21 | 100 | 101 | N | 0→1 |
| 22 | 101 | 100 | N | 1→0 |
| 23 | 110 | 111 | N | 0→1 |
| 24 | 111 | 110 | N | 1→0 |

### 3.5. Przejścia niedopuszczalne w HPE-model (wielobitowe)

Wszystkie pary stanów o $d_H \geq 2$:
- $d_H = 2$: 12 par (np. 000→011, 000→101, 000→110, ...)
- $d_H = 3$: 4 pary (000↔111, 001↔110, 010↔101, 011↔100)

**Interpretacja:** W HPE-model te przejścia mają $q_{ij}=0$. W danych obserwowanych mogą wystąpić jako: (a) sekwencje nieobserwowanych przejść jednobitowych w interwale $\Delta t$, (b) błędy pomiarowe/klasyfikacji, (c) dowody na fałszowanie HPE-model (jeśli $q_{ij} > 0$ dla $d_H \geq 2$ w estymowanym $Q$).

---

## 4. Modele Probabilistyczne Dynamiki

### 4.1. Dyskretny Łańcuch Markowa (DTMC)

Stan w czasie $t$: $X_t \in \mathcal{S}$

Macierz przejścia $P = [p_{ij}]_{8 \times 8}$ gdzie:
$$p_{ij} = \mathbb{P}(X_{t+1} = s_j | X_t = s_i)$$

**Ograniczenie HPE na $P$:**
$$p_{ij} > 0 \implies d_H(s_i, s_j) \leq 1$$
$$p_{ii} \geq 0 \text{ (pozostanie w stanie)}$$

Macierz $P$ ma strukturę:
- Przekątna: $p_{ii}$ (pozostanie)
- Sąsiedzi (d_H=1): $p_{ij} > 0$ możliwe
- Inne: $p_{ij} = 0$ (zgodnie z HPE)

Liczba wolnych parametrów: $8 \times 3 + 8 = 32$ (3 sąsiadów + sam węzeł) minus 8 normalizacji = 24 parametry przejść + 8 parametrów samoprzestania = 32, ale sumy wierszy = 1 → 24 wolne.

### 4.2. Łańcuch Markowa w Czasie Ciągłym (CTMC)

Macierz intensywności (generator) $Q = [q_{ij}]_{8 \times 8}$:
- $q_{ij} \geq 0$ dla $i \neq j$, $d_H(s_i, s_j) = 1$ (intensywność przejścia)
- $q_{ij} = 0$ dla $d_H(s_i, s_j) \geq 2$ (HPE na poziomie intensywności)
- $q_{ii} = -\sum_{j \neq i} q_{ij}$

**Kluczowe rozróżnienie:**
HPE nakładamy na **intensywności elementarne** $q_{ij}$ (procesy psychologiczne), a nie na prawdopodobieństwa $P(\Delta t)$ po czasie $\Delta t$.

Dlaczego? Bo $P(\Delta t) = \exp(Q \Delta t)$.
Nawet jeśli $q_{ij}=0$ dla $d_H \geq 2$, to $P(\Delta t)_{ij}$ może być $>0$ dla $\Delta t > 0$ (przejścia wieloetapowe w jednym interwale pomiarowym).

To rozwiązuje problem ograniczonej częstotliwości pomiarów (EMA).

### 4.3. Model Semi-Markowski (SMM)

Czas przebywania w stanie $s$ ma rozkład $F_s(t)$ (niekoniecznie wykładniczy).
Przejścia zgodne z HPE.

Przydatne gdy czasy przebywania w stanach nie są bezpamięciowe (np. stan 111 stabilny dłużej).

### 4.4. Model Stanów Ukrytych (HMM) / LTA

Stany $\mathcal{S}$ = stany latentne (ukryte).
Obserwacje: pomiary $W_{obs}, C_{obs}, N_{obs}$ (binarne lub ciągłe).

Macierz emisji: $\mathbb{P}(obs | state)$
Macierz przejść: $P$ (zgodna z HPE)

**Problem identyfikowalności:** 3 wskaźniki binarne → 8 wzorców odpowiedzi = 8 stanów = model nasycony (0 df). Wymaga:
- Wskaźników ciągłych (skale Likert dla W,C,N)
- Lub dodatkowych zmiennych obserwowanych (zachowanie, afekt, kontekst)
- Lub ograniczeń na macierzy emisji/przejść

### 4.5. Modele Przejść Latentnych (LTA)

Analiza przejść między klasami latentnymi w czasie.
$K=8$ klas (stanów), $T$ pomiarów.
Macierz przejść $P^{(t)}$ może zależeć od czasu / kowariancji.

---

## 5. Definicje Pochodne (do operacjonalizacji)

### 5.1. Intensywność przejścia
$q_{ij}$ (CTMC) lub $p_{ij}$ (DTMC) – parametry modelu, nie obserwowane bezpośrednio.

### 5.2. Stabilność stanu
- **DTMC:** $p_{ii}$ (prawdopodobieństwo pozostania w kroku)
- **CTMC:** $-q_{ii} = \sum_{j \neq i} q_{ij}$ (całkowita intensywność opuszczania stanu)
- **Czas oczekiwany w stanie (CTMC):** $\tau_i = 1 / (-q_{ii})$ (jeśli wykładniczy)

### 5.3. Czas przebywania (sojourn time)
Czas ciągły spędzony w stanie przed przejściem.
CTMC: rozkład wykładniczy $Exp(-q_{ii})$.
SMM: dowolny rozkład $F_i(t)$.

### 5.4. Prawdopodobieństwo osiągnięcia konfiguracji
Dla zbioru stanów docelowych $T \subseteq \mathcal{S}$:
$$h_i = \mathbb{P}(\text{dotrzeć do } T \text{ startując z } s_i)$$
Rozwiązuje układ równań (dla DTMC/ CTMC).

### 5.5. Koszt psychologiczny przejścia
Konstrukt teoretyczny (nieparametr modelu).
Można zdefiniować jako funkcję:
$$cost(i \to j) = f(\text{zmieniony wymiar}, \text{kierunek}, \text{stan początkowy}, \text{kontekst})$$

Przykłady hipotez:
- $cost(011 \to 111) < cost(001 \to 101)$ – dodanie W łatwiejsze przy C=1
- $cost(111 \to 011) > cost(111 \to 110)$ – utrata W trudniejsza niż utrata N
- $cost(101 \to 001)$ (rezygnacja z celu) = wysoki koszt emocjonalny

### 5.6. Trwałość zmiany
Prawdopodobieństwo, że po przejściu $i \to j$ system nie wróci do $i$ w czasie $\Delta t$.
Związane z głębią "doliny atrakcyjności" w metaforze systemów dynamicznych.

### 5.7. Zależność od historii (path dependence)
Czy $p_{ij}$ zależy od ścieżki do $i$?
- Model Markowski: nie (bezpamięciowy)
- Model rzędu wyższemi / semi-Markowski / ze zmiennymi latentnymi: tak

Przykłady w DMTRD:
- Przejście 000→100→110→111 (budowanie) vs 000→001→011→111 (internalizacja) → różna historia, ten sam stan 111
- Czy stabilność 111 zależy od ścieżki? (Hipoteza DMTRD: tak)

---

## 5. Status Epistemiczny i Zakres Modelu

### 5.1. Osiem stanów jako klasyfikacja logiczna, nie taksonomia psychologiczna

Osiem stanów $\mathcal{S} = \{0,1\}^3$ to **wyczerpujące zestawienie logicznych kombinacji** trzech ocen binarnych. Nie postulujemy, że odpowiadają one ośmiu jakościowo odrębnym, naturalnym stanom psychicznym. Nazwy stanów (np. „Gotowość autonomiczna”, „Obowiązek wykonalny bez autonomii”) to **etykiety interpretacyjne** ułatwiające komunikację, a nie nazwy odkrytych taksonów psychologicznych.

Różne osoby w tym samym kodzie (np. 111) mogą mieć odmienną intensywność W, różne źródła N (`N_source`), różną historię dojścia – co może implikować różną dynamikę przyszłą. Agregacja do 8 stanów to **kompresja informacji** ułatwiająca modelowanie, a nie odkrycie naturalnych kategorii.

### 5.2. Zakres modelu: regulacja refleksyjna (System 2)

Model DMTRD w wersji bazowej opisuje **regulację refleksywną (System 2)** – procesy świadome, celowe, wymagające uwagi. Nie modeluje:

- **Automatyzm/nawyki (System 1):** działanie bez aktualnej refleksji o chęci (Wood & Neal, 2007). Stan 010/011 (W=0, C=1) przy nawyku to normalne działanie, a nie „brak motywacji”.
- **Ambiwalencję:** współistnienie chęci i niechęci (W nie rozróżnia neutralności od awersji).
- **Patologie kliniczne:** depresję, anhedonię, uzależnienia – wymagają rozszerzeń.

Dla zjawisk System 1 wymagane jest rozszerzenie modelu (parametr H – siła nawyku, wersja ciągła W ∈ [-1,1]).

### 5.3. Stan motywacyjny ≠ zachowanie

Stan $(W,C,N)$ to **konfiguracja ocen motywacyjnych**, nie działanie ani intencja.

- Stan 110 („Gotowość autonomiczna”) ≠ wykonane działanie.
- Stan 101 (W=1, N=1, C=0) – silna motywacja zablokowana barierami; może prowadzić do *działań przygotowawczych* (szukanie zasobów, lobbyowanie), ale nie do wykonania celu głównego.
- Zachowanie (wykonanie celu) to osobna zmienna wynikowa $A \in \{0,1\}$, modelowana jako funkcja stanu, kontekstu, volicji (Kuhl), nawyków i okazji.

### 5.4. Zmienna pomocnicza: Źródło obowiązku ($N_{source}$)

Bit $N$ informuje tylko o **obecności/braku poczucia zobowiązania**. Źródło i jakość regulacji to osobna zmienna kategoryczna:

$$N_{source} \in \{\text{external}, \text{introjected}, \text{identified}, \text{integrated}, \text{moral}, \text{role}, \text{legal}\}$$

Internalizacja normy to proces zmiany $N_{source}$ (np. external → identified), a **nie** koniecznie zmiana $N$ z 1 na 0. Stan 110 (W=1, C=1, N=0) może oznaczać: brak poczucia „powinienem” LUB zinternalizowany obowiązek (N=1) który nie jest doświadczany jako „powinienem” (bo zinternalizowany). Rozdzielenie $N$ i $N_{source}$ rozwiązuje sprzeczność między rozdz. 8.4 a 8.5 w dokumentacji pierwotnej.

### 5.5. Path Dependence jako rozszerzenie, nie cecha modelu bazowego

Model bazowy (CTMC/DTMC) jest **bezpamięciowy (Markowski)**: przyszłość zależy tylko od aktualnego stanu $(W,C,N)$. Zależność od historii (path dependence – np. różna stabilność 111 w zależności od drogi dojścia) to **rozszerzenie modelu** (model rzędu wyższego, zmienne latentne historii, CTMC z kowariancjami zależnymi od czasu), nie cecha modelu bazowego. W modelu bazowym: $P(X_{t+1} | X_t, X_{t-1}, ...) = P(X_{t+1} | X_t)$.

---

## 6. Rozszerzenia Modelu (do rozważenia)

### 6.1. Zmienne ciągłe zamiast binarnych
$W, C, N \in [0,1]$ (lub skala Likert 1-7).
Stan = punkt w sześcianie $[0,1]^3$.
8 stanów = 8 oktaantów (przedziały).
Przejścia = ruch między oktaantami (przecinanie płaszczyzn $W=0.5$, $C=0.5$, $N=0.5$).

Zalety: naturalniejsze, więcej informacji, identyfikowalne w LTA.
Wady: utrata prostej topologii Q3, trudniejsza interpretacja.

### 6.2. Czwarty wymiar: Intencja (I)
$I \in \{0,1\}$ lub $[0,1]$.
Przestrzeń: $Q_4$ (16 stanów).
Intencja jako pośrednik między (W,C,N) a działaniem.

### 6.3. Piąty wymiar: Działanie (A)
$A \in \{0,1\}$ – czy działanie faktycznie nastąpiło.
Rozdzielenie stanu motywacyjnego od zachowania.

### 6.4. Kontekst / Zmienne ekzogennne
Zmienne $X_t$ wpływające na $Q$ lub $P$:
- Zasoby obiektywne
- Presja społeczna
- Stan afektywny
- Nawyk (siła asocjacji kontekst-reakcja)
- Historia przejść (path dependence)

Model: $Q(X_t)$ lub $P(X_t)$ – łańcuch Markowa z kowariancjami.

---

## 8. Model Pomiarowy i Identyfikowalność (Specyfikacja G3)

### 8.1. Wybór modelu bazowego

**Model bazowy do estymacji:** **CTMC z obserwowanymi stanami ciągłymi** ($W,C,N \in [1,7]$ Likert).

- Stany obserwowane bezpośrednio (brak klas latentnych) → unika problemu identyfikowalności LTA/HMM z 3 wskaźnikami binarnymi.
- Wersja ciągła zachowuje informację o natężeniu; dyskretyzacja na 8 stanów (oktaanty, próg 4) tylko do interpretacji i wizualizacji.
- Estymacja generatora $Q$ z danych panelowych EMA (pakiety `msm`/`ctmcm` w R, `ctmcm` w Python).

### 8.2. Wersja binarna (uproszczenie)

Wersja binarna ($W,C,N \in \{0,1\}$) to **uproszczenie do interpretacji i wizualizacji** (graf Q3, 8 stanów). Nie jest modelem bazowym do estymacji, ponieważ:
- 3 wskaźniki binarne → 8 wzorców odpowiedzi = model nasycony (0 df) w pojedynczym pomiarze LTA.
- Traci informację o natężeniu i gradacji (self-efficacy, typy regulacji, kategorie norm).
- Progowanie (próg 4) jest arbitralne i generuje błędy klasyfikacji u osób blisko granicy.

### 8.3. Specyfikacja modelu pomiarowego (wersja ciągła)

**Zmienne obserwowane (wskaźniki stanu):**
- $W_{it} \in [1,7]$ – skala Likert: „W jakim stopniu chcesz wykonać to działanie?”
- $C_{it} \in [1,7]$ – skala Likert: „W jakim stopniu uważasz, że jesteś w stanie to zrealizować (posiadasz kompetencje, czas, zasoby)?”
- $N_{it} \in [1,7]$ – skala Likert: „W jakim stopniu uważasz, że powinieneś to zrobić ze względu na swoje cele?”

**Zmienne eksogenne (predyktory przejść / moderatory):**
- $AutonomySupport_{it}$ – wsparcie autonomii (mPAS)
- $Resources_{it}$ – dostępne zasoby, czas, wsparcie
- $RoleAmbiguity_{it}$, $RoleConflict_{it}$ – ambiguitet/konflikt ról
- $HabitStrength_{it}$ – siła nawyku (SRHI, opcjonalnie)
- $N_{source,it}$ – źródło obowiązku (kategoryczna)

**Zmienne wynikowe (outcomes):**
- $Behavior_{it} \in \{0,1\}$ – wykonanie celu w oknie $[t, t+\Delta]$
- $Affect_{it}$ – PANAS (pozytywny/negatywny afekt)
- $Burnout_{it}$ – MBI (wypalenie, skala czasu: tygodnie)
- $MoralDistress_{it}$ – MDS (moral distress, kontekst moralny)

**Rola zmiennych w modelu:**
| Zmienna | Rola | Uwagi |
|---------|------|-------|
| $W,C,N$ | Stan (obserwowany) | Definiują stan w CTMC; nie zawierają zachowania |
| $X_{exog}$ | Predyktory $Q$ / moderatory | Wpływają na intensywności $q_{ij}$ |
| $Y_{outcome}$ | Wyniki (outcomes) | Przewidywane ze stanu; **nie** wskaźniki emisji |

**Kluczowa zasada:** Zachowanie, afekt, wypalenie, moral distress to **zmienne wynikowe (outcomes)** przewidywane ze stanu $(W,C,N)$, a **nie** wskaźniki emisji definiujące stan. To unika zanieczyszczenia kryterium (criterion contamination).

### 8.4. Model dynamiczny: CTMC z kowariancjami

Generator $Q$ zależny od kowariancji:

$$q_{ij}(X_t) = q_{ij}^0 \cdot \exp(\beta_{ij}^T X_t) \quad \text{dla} \quad d_H(i,j)=1$$

Gdzie $X_t$ to wektor kowariancji (AutonomySupport, Resources, itd.). Dla $d_H \geq 2$: $q_{ij}=0$ (HPE-model).

Estymacja: pakiet `msm` (R) lub `ctmcm` (Python) z danymi panelowymi EMA.

### 8.5. Wersje alternatywne (do porównania w walidacji)

| Model | Opis | Użycie |
|-------|------|--------|
| **M_full** | CTMC z 56 wolnymi $q_{ij}$ (bez HPE) | Test HPE (LRT vs M_HPE) |
| **M_indep** | 6 niezależnych intensywności (po 2 na bit) | Test zależności $q$ od konfiguracji |
| **M_cont** | Procesy ciągłe $W,C,N \in [0,1]$ z progowaniem | Test wersji ciągłej vs dyskretnej |
| **M_meas** | HPE-model + błąd klasyfikacji stanów | Test wrażliwości na błędy pomiarowe |

---

## 9. Identyfikowalność i Estymacja

### 9.1. Dane panelowe / EMA
$N$ osób, $T$ pomiarów, zmienne $W_{it}, C_{it}, N_{it}$ (ciągłe Likert 1–7).

### 9.2. Modele do estymacji
1. **CTMC z obserwowanymi stanami ciągłymi** – estymacja $Q$ z danych panelowych EMA (pakiety `msm`/`ctmcm` w R, `ctmcm` w Python). Model bazowy.
2. **CTMC z HPE-model** – $q_{ij}=0$ dla $d_H \geq 2$ (24 wolne parametry). Test HPE: LRT vs model pełny.
3. **Model niezależnych bitów** – 6 intensywności bazowych (po 2 na bit). Test zależności $q$ od konfiguracji.
4. **DSEM (Dynamic SEM)** – modele wielopoziomowe z opóźnieniami (alternatywa dla CTMC).

### 9.3. Moc statystyczna
Symulacje Monte Carlo (1000 replikacji) do ustalenia:
- Minimalne $N$ i $T$ do wykrycia asymetrii przejść (np. $q_{011\to111} \neq q_{111\to011}$) przy mocy > 0.80.
- Wpływ błędu pomiarowego/klasyfikacji na odrzucenie HPE-model.
- Moc testu LRT: HPE-model (24 parametry) vs model pełny (56 parametrów) vs model niezależnych bitów (6 parametrów).
- Precyzja estymacji rzadkich przejść (np. 000→001, 111→110).

---

*Dokument wersja robocza. Wymaga uzupełnienia o konkretne wzory, symulacje ilustracyjne i plan estymacji.*