# Definicje Matematyczne i Formalne – DMTRD

## 1. Przestrzeń Stanów

### 1.1. Wymiarowe przestrzenie
Niech:
- $W \in \{0,1\}$ – CHCĘ (osobista akceptacja i motywacja do realizacji celu)
- $C \in \{0,1\}$ – MOGĘ (subiektywnie oceniana wykonalność działania)
- $N \in \{0,1\}$ – POWINIENEM (poczucie zobowiązania normatywnego)

Przestrzeń stanów: $\mathcal{S} = \{0,1\}^3$

### 1.2. Reprezentacja stanu
Stan $s \in \mathcal{S}$ reprezentujemy jako trójkę uporządkowaną:
$$s = (W, C, N)$$

Kod binarny: $s_{bin} = WCN$ (np. $101 = (1,0,1)$)

Liczba stanów: $|\mathcal{S}| = 2^3 = 8$

### 1.3. Wartościowanie (interpretacja) bitów
| Bit | Wartość 0 | Wartość 1 |
|-----|-----------|-----------|
| W | Brak osobistej motywacji/akceptacji | Obecność osobistej motywacji/akceptacji |
| C | Postrzegana niewykonalność | Postrzegana wykonalność |
| N | Brak poczucia zobowiązania | Poczucie zobowiązania normatywnego |

**Uwaga:** Wartość 0 **nie** oznacza:
- Dla W: silną niechęć (to oddzielny konstrukt)
- Dla C: obiektywną niemożność (to subiektywna ocena)
- Dla N: zakaz (to brak obowiązku, nie zabronienie)

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

### 3.1. Sformułowanie
**HPE:** Elementarny proces psychologiczny zmiany stanu motywacyjnego zmienia dokładnie jeden z trzech wymiarów (W, C lub N).

Formalnie: dopuszczalne przejścia elementarne to tylko te, dla których $d_H(s_{start}, s_{end}) = 1$.

### 3.2. Lista 24 przejść dopuszczalnych

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

### 3.3. Przejścia niedopuszczalne (wielobitowe)
Wszystkie pary stanów o $d_H \geq 2$:
- $d_H = 2$: 12 par (np. 000→011, 000→101, 000→110, ...)
- $d_H = 3$: 4 pary (000↔111, 001↔110, 010↔101, 011↔100)

**Interpretacja HPE:** Przejścia $d_H \geq 2$ są złożone (składają się z 2 lub 3 przejść elementarnych) lub wynikają z ograniczonej rozdzielczości pomiarowej.

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

## 7. Identyfikowalność i Estymacja

### 7.1. Dane panelowe / EMA
$N$ osób, $T$ pomiarów, zmienne $W_{it}, C_{it}, N_{it}$ (binarne/ciągłe).

### 7.2. Modele do estymacji
1. **LTA (Latent Transition Analysis)** – stany latentne = 8 klas, wskaźniki = W,C,N
   - Problem: 3 wskaźniki binarne → saturated
   - Rozwiązanie: wskaźniki ciągłe, lub więcej wskaźników, lub ograniczenia
2. **Markov Model z obserwowanymi stanami** – jeśli W,C,N pomiarowe bez błędu
   - Proste: liczenie przejść, estymacja $P$ (MLE)
   - Wymaga: wysokiej częstotliwości pomiarów (HPE na poziomie obserwacji)
3. **CTMC z EMA** – estymacja $Q$ z danych panelowych (np. pakiet `msm` w R, `ctmcm` w Python)
4. **DSEM (Dynamic SEM)** – modele wielopoziomowe z opóźnieniami

### 7.3. Moc statystyczna
Symulacje potrzebne do ustalenia:
- Minimalne $N$ i $T$ do wykrycia asymetrii przejść (np. $p_{011\to111} \neq p_{111\to011}$)
- Wpływ błędu pomiarowego na odrzucenie HPE
- Moc testu $d_H \geq 2$ przejść (czy obserwujemy skoki wielobitowe?)

---

*Dokument wersja robocza. Wymaga uzupełnienia o konkretne wzory, symulacje ilustracyjne i plan estymacji.*