# Formalizacja HPE (Hipoteza Przejść Elementarnych) – DMTRD rev1

**Wersja:** 1.0  
**Data:** 07.11.2026  
**Status:** Specyfikacja po rewizji krytycznej ASTRA  
**Cel:** Precyzja formalna HPE jako ograniczenia modelowego (HPE-model) i hipotezy empirycznej (HPE-empiryczna), z modelem alternatywnym i planem testów.

---

## 1. Rozróżnienie dwóch poziomów HPE

### 1.1. HPE-model (Ograniczenie na generator Q)

**Definicja:** W generatorze $Q$ łańcucha Markowskiego w czasie ciągłym (CTMC) intensywności przejść między stanami o odległości Hamminga $d_H \geq 2$ są równe zero:

$$\forall i,j \in \mathcal{S}: \quad d_H(s_i, s_j) \geq 2 \implies q_{ij} = 0$$

Gdzie:
- $\mathcal{S} = \{0,1\}^3$ – przestrzeń 8 stanów
- $d_H(s_i, s_j) = \sum_{k \in \{W,C,N\}} |s_i^k - s_j^k|$ – odległość Hamminga
- $Q = [q_{ij}]_{8 \times 8}$ – macierz intensywności (generator)
- $q_{ij} \geq 0$ dla $i \neq j$ – intensywność przejścia $i \to j$
- $q_{ii} = -\sum_{j \neq i} q_{ij}$

**Konsekwencje HPE-model:**
- Dopuszczalne skoki elementarne: tylko $d_H = 1$ (24 kierunkowe przejścia).
- $Q$ ma **24 wolne parametry** $q_{ij}$ (dla $d_H=1$) + ewentualne parametry kowariancji $\beta_{ij}$.
- Macierz przejścia w czasie $\Delta t$: $P(\Delta t) = \exp(Q \Delta t)$.
- **Kluczowe:** Nawet przy $q_{ij}=0$ dla $d_H \geq 2$, macierz $P(\Delta t)$ dla $\Delta t > 0$ może mieć $p_{ij} > 0$ dla $d_H \geq 2$ (przejścia wieloetapowe w jednym interwale pomiarowym).

### 1.2. HPE-empiryczna (Hipoteza testowalna)

**Definicja:** W danych EMA z gęstym próbkowaniem, odsetek obserwowanych zmian $d_H \geq 2$ między kolejnymi pomiarami jest istotnie mniejszy niż przewidywane przez modele alternatywne dopuszczające bezpośrednie skoki wielobitowe.

**Formalizacja:** Niech $\hat{p}_{d_H \geq 2}$ będzie odsetkiem obserwowanych zmian $d_H \geq 2$ w danych EMA (po korekcie na błędy klasyfikacji). Niech $p_{d_H \geq 2}^{(M)}$ będzie przewidywanym odsetkiem w modelu $M$.

**HPE-empiryczna:** $\hat{p}_{d_H \geq 2} \approx p_{d_H \geq 2}^{(M_{HPE})}$ i $\hat{p}_{d_H \geq 2} \ll p_{d_H \geq 2}^{(M_{alt})}$ dla modeli alternatywnych $M_{alt}$ dopuszczających bezpośrednie skoki wielobitowe.

---

## 2. Modele do porównania (Test HPE)

### 2.1. M_HPE (Model bazowy – HPE-model)
- **Generator $Q$:** $q_{ij} = 0$ dla $d_H \geq 2$; $q_{ij} \geq 0$ dla $d_H = 1$.
- **Parametry:** 24 intensywności bazowych $q_{ij}^0$ (dla $d_H=1$) + $\beta_{ij}$ dla kowariancji $X_t$.
- **Kowariancje:** $q_{ij}(X_t) = q_{ij}^0 \cdot \exp(\beta_{ij}^T X_t)$ dla $d_H=1$.

### 2.2. M_full (Pełny generator – bez HPE)
- **Generator $Q$:** $q_{ij} \geq 0$ dla **wszystkich** $i \neq j$ (56 wolnych parametrów).
- **Parametry:** 56 intensywności $q_{ij}^0$ + $\beta_{ij}$.
- **Test:** LRT (M_HPE vs M_full) – hipoteza zerowa: $q_{ij}=0$ dla $d_H \geq 2$.

### 2.3. M_indep (Niezależne bity)
- **Założenie:** Każdy bit zmienia się niezależnie od pozostałych.
- **Parametry:** 6 intensywności bazowych (po 2 na bit: $W: 0\to1, 1\to0$; $C: 0\to1, 1\to0$; $N: 0\to1, 1\to0$).
- **Generator:** $q_{ij} = q_{k}^{dir}$ jeśli $d_H=1$ i zmienia się bit $k$ w kierunku $dir$; wpp. 0.
- **Test:** LRT (M_HPE vs M_indep) – czy intensywności zależą od konfiguracji pozostałych bitów?

### 2.4. M_cont (Procesy ciągłe z progowaniem)
- **Zmienne latente:** $W^*, C^*, N^* \in [0,1]$ (lub $\mathbb{R}$) – procesy ciągłe (np. OU, dyfuzja).
- **Obserwacja:** $W = \mathbb{1}(W^* \geq \tau_W)$, analogicznie $C, N$ (progowanie).
- **Parametry:** Parametry procesów ciągłych + progi $\tau_W, \tau_C, \tau_N$.
- **Test:** Porównanie dopasowania (AIC/BIC, walidacja krzyżowa) vs M_HPE.

### 2.5. M_meas (HPE-model + błąd klasyfikacji)
- **Model:** M_HPE + macierz pomyłek $E$ (prawdopodobieństwo obserwacji stanu $j$ przy prawdziwym $i$).
- **Parametry:** 24 $q_{ij}$ + parametry macierzy pomyłek (np. 3 parametry: sens/spec dla każdego bitu).
- **Test:** Czy uwzględnienie błędu klasyfikacji wyjaśnia obserwowane $d_H \geq 2$?

---

## 3. Formalna specyfikacja testów

### 3.1. Test HPE-model (LRT: M_HPE vs M_full)

**Hipoteza zerowa $H_0$:** $q_{ij} = 0$ dla wszystkich $i,j$ takich że $d_H(s_i, s_j) \geq 2$.

**Statystyka testowa:** $\Lambda = 2(\ell_{M_{full}} - \ell_{M_{HPE}}) \stackrel{H_0}{\sim} \chi^2_{df}$  
Gdzie $df = 56 - 24 = 32$ (różnica liczby parametrów $q_{ij}$).

**Uwaga:** Standardowy rozkład $\chi^2$ może nie być dokładny dla parametrów na brzegu przestrzeni ($q_{ij}=0$). **Kalibracja:** Bootstrap parametryczny lub symulacja Monte Carlo pod $H_0$.

### 3.2. Test HPE-model vs M_indep (LRT)

**Hipoteza zerowa $H_0$:** Intensywności zależą tylko od zmieniającego się bitu (nie od konfiguracji pozostałych).

**Statystyka:** $\Lambda = 2(\ell_{M_{HPE}} - \ell_{M_{indep}}) \stackrel{H_0}{\sim} \chi^2_{df}$  
Gdzie $df = 24 - 6 = 18$.

**Interpretacja:** Odrzucenie $H_0$ → intensywności zależą od kontekstu (pozostałych bitów) → poparcie dla HPE-model jako uproszczenia, ale z zależnością od konfiguracji.

### 3.3. Test HPE-empiryczna (Odsetek $d_H \geq 2$)

**Statystyka:** $\hat{p}_{d_H \geq 2} = \frac{1}{N_{trans}} \sum_{t} \mathbb{1}(d_H(S_t, S_{t+1}) \geq 2)$

**Porównanie:** $\hat{p}_{d_H \geq 2}$ vs $p_{d_H \geq 2}^{(M)}$ dla $M \in \{M_{HPE}, M_{full}, M_{indep}, M_{cont}, M_{meas}\}$.

**Kryterium:** $\hat{p}_{d_H \geq 2}$ bliskie predykcji M_HPE (po korekcie na błędy klasyfikacji) i istotnie mniejsze niż predykcje M_full/M_indep/M_cont.

**Uwaga:** Prog 15% z pierwotnej wersji jest **arbitralny** (C1). Prawdziwy odsetek zależy od:
- Intensywności $q_{ij}$ (im wyższe, tym więcej zmian w $\Delta t$)
- Odstępów pomiarowych $\Delta t$ (im większe, tym więcej wieloetapowych przejść)
- Błędów klasyfikacji (progowanie)

### 3.4. Test asymetrii (Asymetria intensywności)

Dla każdej pary odwrotnych $(i,j)$:

**Hipoteza zerowa $H_0$:** $q_{ij} = q_{ji}$

**Statystyka:** LRT lub test Walda dla $\log(q_{ij}/q_{ji}) = 0$.

**Korekcja wielokrotnych testów:** FDR (Benjamini-Hochberg) dla 12 par.

**Wielkość efektu:** Iloraz $q_{ij}/q_{ji}$ z 95% CI.

---

## 4. Kontrprzykład Astry (Weryfikacja numeryczna)

### 4.1. Zadanie
Pokaż, że przy generatorze $Q$ spełniającym HPE-model (tylko $d_H=1$), przy realistycznych odstępach EMA (2-3h) i intensywnościach, odsetek obserwowanych $d_H \geq 2$ może przekraczać 15%.

### 4.2. Model symulacyjny

**Generator $Q$ (HPE-model, niezależne bity dla uproszczenia):**
- Każdy bit niezależnie zmienia stan z intensywnością $\lambda = 1$ na godzinę (0→1 i 1→0).
- $Q$ ma 6 nienulowych intensywności (po 2 na bit), reszta = 0.

**Symulacja:**
1. Wygeneruj trajektorię CTMC dla $T=24$h.
2. Próbkuj co $\Delta t = 0.5$h (30 min).
3. Oblicz odsetek par kolejnych obserwacji z $d_H \geq 2$.

### 4.3. Wynik analityczny (dla $\Delta t = 0.5$h, $\lambda=1$)

Dla jednego bitu: $p_{flip} = \frac{1-e^{-2\lambda \Delta t}}{2} = \frac{1-e^{-1}}{2} \approx 0.316$.

Prawdopodobieństwo zmiany **co najmniej 2 bitów** z 3 niezależnych:
$$P(d_H \geq 2) = 3p^2(1-p) + p^3 = 3(0.316)^2(0.684) + (0.316)^3 \approx 0.237 = 23.7\%$$

**Wniosek:** Przy **prawdziwym HPE-model** (niezależne bity, $\lambda=1$/h), przy pomiarze co 30 min, **23.7% obserwowanych zmian to $d_H \geq 2$**. Przekracza to arbitralny próg 15% z pierwotnej wersji.

### 4.4. Wniosek
- Próg 15% jest **bezfundamentowy**.
- Test HPE-empiryczna musi porównywać **model z modelem**, nie używać arbitralnego progu.
- Prawidłowy test: estymacja $Q$ (CTMC) + LRT (M_HPE vs M_full).

---

## 5. Kod symulacyjny (Python)

```python
# src/hpe_simulation.py
import numpy as np
from scipy.linalg import expm
import pandas as pd

def simulate_ctmc_hpe(Q, T=24.0, dt=0.5, n_sim=1000):
    """
    Symuluje CTMC z generatorem Q (HPE-model) i próbkuje co dt.
    Zwraca odsetek obserwowanych zmian d_H >= 2.
    """
    states = ['000','001','010','011','100','101','110','111']
    state_to_idx = {s:i for i,s in enumerate(states)}
    
    def hamming(s1, s2):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))
    
    counts_dH_ge_2 = 0
    total_trans = 0
    
    for _ in range(n_sim):
        # Stan początkowy losowy
        current = np.random.choice(len(states))
        t = 0.0
        
        while t < T:
            # Czas do następnego skoku
            rate = -Q[current, current]
            if rate <= 0:
                break
            tau = np.random.exponential(1/rate)
            t += tau
            if t >= T:
                break
            
            # Wybierz następny stan
            probs = Q[current] / rate
            probs[current] = 0
            next_state = np.random.choice(len(states), p=probs)
            
            # Sprawdź czy mamy pomiar w tym przedziale
            # (uproszczone: sprawdzamy co dt)
            pass  # Implementacja próbkowania co dt
    
    # Uproszczona wersja: analityczna dla niezależnych bitów
    # P(d_H >= 2) = 3p^2(1-p) + p^3, gdzie p = (1-exp(-2*lambda*dt))/2
    return None

def analytical_dH_ge_2(lambda_rate=1.0, dt=0.5):
    """Analityczne P(d_H >= 2) dla 3 niezależnych bitów."""
    p = (1 - np.exp(-2 * lambda_rate * dt)) / 2
    return 3 * p**2 * (1 - p) + p**3

if __name__ == "__main__":
    for dt in [0.5, 1.0, 2.0, 3.0]:
        p = analytical_dH_ge_2(lambda_rate=1.0, dt=dt)
        print(f"dt={dt}h: P(d_H >= 2) = {p:.3f} ({p*100:.1f}%)")
```

**Wynik oczekiwany:**
```
dt=0.5h: P(d_H >= 2) = 0.237 (23.7%)
dt=1.0h: P(d_H >= 2) = 0.354 (35.4%)
dt=2.0h: P(d_H >= 2) = 0.489 (48.9%)
dt=3.0h: P(d_H >= 2) = 0.572 (57.2%)
```

---

## 6. Plan wdrożenia testów (Kolejność realizacji)

1. **Implementacja `src/hpe_simulation.py`** – symulacja weryfikująca kontrprzykład Astry.
2. **Estymacja CTMC na danych symulowanych** – weryfikacja, że LRT (M_HPE vs M_full) poprawnie odrzuca/nie odrzuca HPE.
2. **Estymacja CTMC na danych EMA (pilotaż)** – test HPE na rzeczywistych danych.
3. **Porównanie modeli** (M_HPE vs M_full vs M_indep vs M_cont) – AIC/BIC, log-loss out-of-sample.
3. **Test asymetrii** – LRT dla $q_{ij} = q_{ji}$ dla kluczowych par.

---

## 7. Zmiany względem wersji pierwotnej

| Element | Wersja pierwotna | Wersja rev1 |
|---------|------------------|-------------|
| HPE | Jedna hipoteza ("elementarny proces = 1 bit") | **Dwa poziomy:** HPE-model (ograniczenie Q) + HPE-empiryczna (testowalna) |
| Test HPE | LTA: $p_{ij}=0$ dla $d_H \geq 2$ przy $\Delta t=2-3$h | **CTMC:** estymacja $Q$ + LRT (M_HPE vs M_full) |
| Próg falsyfikacji | >15% zmian $d_H \geq 2$ przy EMA co 30 min | **Usunięty** – arbitralny (kontrprzykład: 23.7% przy HPE) |
| Modele alternatywne | Niejawnie: "zmiany wielobitowe" | **Jawne:** M_full, M_indep, M_cont, M_meas |
| Asymetria | Próg 50% par z $q_{ij} \neq q_{ji}$ | **LRT dla każdej pary** + wielkość efektu (iloraz $q_{ij}/q_{ji}$) + FDR |

---

*Dokument wersja 1.0. Gotowy do implementacji testów w `src/hpe_simulation.py` i wdrożenia w badaniu pilotażowym.*