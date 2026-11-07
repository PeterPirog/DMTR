# Testowalność HPE – Plan Weryfikacji Empirycznej i Symulacyjnej (rev1)

**Wersja:** 1.0  
**Data:** 07.11.2026  
**Status:** Plan testów zgodny z formalizacją HPE rev1  
**Cel:** Konkretny plan weryfikacji HPE-model i HPE-empirycznej.

---

## 1. Strategia testowania HPE

### 1.1. Dwa poziomy testowania

| Poziom | Nazwa | Pytanie badawcze | Metoda |
|--------|-------|------------------|--------|
| **Modelowy** | HPE-model | Czy generator $Q$ ma $q_{ij}=0$ dla $d_H \geq 2$? | Estymacja CTMC → LRT (M_HPE vs M_full) |
| **Empiryczny** | HPE-empiryczna | Czy odsetek obserwowanych $d_H \geq 2$ w danych EMA jest zgodny z M_HPE? | Porównanie $\hat{p}_{d_H \geq 2}$ z predykcjami M_HPE vs M_alt |

### 1.2. Hierarchia dowodów

| Siła dowodu | Test | Interpretacja |
|-------------|------|---------------|
| **Najmocniejszy** | LRT (M_HPE vs M_full) na estymowanym $Q$ | Test HPE-model: $H_0: q_{ij}=0$ dla $d_H \geq 2$. **Istotny LRT ($p < 0.05$) = dowód PRZECIW HPE-model** (M_full dopasowuje lepiej). Brak istotności = brak dowodu przeciwko HPE-model. |
| **Mocny** | Porównanie AIC/BIC: M_HPE vs M_full vs M_indep vs M_cont | Selekcja modelu; HPE-model preferowany jeśli ΔAIC > 10 na korzyść M_HPE. |
| **Wspierający** | Predykcja out-of-sample: log-loss M_HPE vs M_full vs M_indep | Wartość predykcyjna HPE-model. |
| **Wspierający** | Odsetek $d_H \geq 2$ w danych vs predykcje modeli | Konsystencja obserwacji z M_HPE. |
| **Słaby** | Odsetek $d_H \geq 2$ w surowych danych (bez modelu) | Tylko opisowy; nie rozróżnia HPE od błędów pomiarowych. |

**Uwaga:** Standardowy test LRT zakłada parametry w wnętrzu przestrzeni parametrów. Dla $q_{ij}=0$ (brzeg przestrzeni) rozkład asymptotyczny LRT nie jest standardowym $\chi^2$. **Wymagana kalibracja bootstrap parametryczny** lub symulacja Monte Carlo pod $H_0$.

---

## 2. Symulacje Weryfikacyjne (Krok 0 – przed danymi)

### 2.1. Cel
Zweryfikować:
1. Czy LRT (M_HPE vs M_full) poprawnie kontroluje błąd I-go rodzaju (α = 0.05) gdy HPE-model jest prawdziwy.
2. Czy LRT ma moc > 0.80 do wykrycia naruszenia HPE (M_full) przy realistycznych parametrach.
3. Czy arbitralny próg 15% $d_H \geq 2$ jest bezużyteczny (kontrprzykład Astry).

### 2.2. Parametry symulacji

| Parametr | Wartości |
|----------|----------|
| **Generator prawdziwy** | M_HPE (HPE-model) / M_full (naruszenie) |
| **Intensywności bazowe $q_{ij}^0$** | 0.1, 0.5, 1.0, 2.0 na godzinę |
| **Kowariancje $\beta$** | 0 (brak), 0.5 (umiarkowane), 1.0 (silne) |
| **Liczba osób $N$** | 50, 100, 200, 500 |
| **Liczba pomiarów $T$** | 50, 100, 200 na osobę |
| **Odstępy $\Delta t$** | Stałe: 0.5h, 1h, 2h, 3h; Zmienne: Exp(mean=2h) |
| **Błąd klasyfikacji (próg 4)** | 0%, 5%, 10%, 20% |
| **Liczba replikacji** | 1000 na warunek |

### 2.3. Metryki wyjściowe

| Metryka | Cel |
|---------|-----|
| **Type I error rate** | Odsetek odrzuceń $H_0$ gdy HPE-model prawdziwy (cel: ≈ 0.05) |
| **Power (Moc)** | Odsetek odrzuceń $H_0$ gdy HPE-model fałszywy (cel: > 0.80) |
| **Bias estymacji $q_{ij}$** | Średnie odstępnienie estymowanych $q_{ij}$ od prawdziwych |
| **Precision (Precyzja)** | Średnia szerokość 95% CI dla $q_{ij}$ |
| **Odsetek $d_H \geq 2$** | Porównanie z arbitralnym progiem 15% |

### 2.4. Kod symulacyjny (`src/hpe_simulation.py`)

```python
# src/hpe_simulation.py
import numpy as np
from scipy.linalg import expm
from scipy.stats import chi2
import pandas as pd
from typing import Dict, List, Tuple
import json

STATES = ['000','001','010','011','100','101','110','111']
STATE_TO_IDX = {s:i for i,s in enumerate(STATES)}

def hamming(s1: str, s2: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def build_Q_hpe(rates: Dict[str, float]) -> np.ndarray:
    """Buduje generator Q spełniający HPE-model (tylko d_H=1)."""
    Q = np.zeros((8, 8))
    for i, s1 in enumerate(STATES):
        for j, s2 in enumerate(STATES):
            if i != j and hamming(s1, s2) == 1:
                # Określ zmieniony bit i kierunek
                diff_idx = [k for k, (a, b) in enumerate(zip(s1, s2)) if a != b][0]
                bit_name = 'WCN'[diff_idx]
                direction = f"{s1[diff_idx]}→{s2[diff_idx]}"
                key = f"{bit_name}_{direction}"
                Q[i, j] = rates.get(key, 0.0)
    # Diagonalna
    for i in range(8):
        Q[i, i] = -Q[i].sum()
    return Q

def build_Q_full(rates: Dict[str, float]) -> np.ndarray:
    """Buduje pełny generator Q (wszystkie pary i≠j)."""
    Q = np.zeros((8, 8))
    for i, s1 in enumerate(STATES):
        for j, s2 in enumerate(STATES):
            if i != j:
                # Uproszczenie: intensywność zależna od liczby zmienionych bitów
                dH = hamming(STATES[i], STATES[j])
                base_rate = 0.5  # bazowa intensywność
                Q[i, j] = base_rate * (0.5 ** (dH - 1))  # malejące z d_H
    for i in range(8):
        Q[i, i] = -Q[i].sum()
    return Q

def simulate_ctmc(Q: np.ndarray, T: float, dt_obs: float, 
                  state0: int = None) -> Tuple[List[int], List[float]]:
    """Symuluje CTMC z generatorem Q, zwraca stany w momentach obserwacji co dt_obs."""
    n_states = Q.shape[0]
    if state0 is None:
        state0 = np.random.choice(n_states)
    
    obs_times = np.arange(0, T + dt_obs/2, dt_obs)
    states_obs = []
    current_state = state0
    current_time = 0.0
    
    # Symulacja skoków
    jump_times = []
    jump_states = [state0]
    t = 0.0
    current = state0
    
    while t < T:
        rate = -Q[current, current]
        if rate <= 0:
            break
        tau = np.random.exponential(1/rate)
        t += tau
        if t >= T:
            break
        # Wybierz następny stan
        probs = Q[current].copy()
        probs[current] = 0
        probs = probs / probs.sum()
        next_state = np.random.choice(8, p=probs)
        jump_times.append(t)
        jump_states.append(next_state)
        current = next_state
    
    # Próbkowanie co dt_obs
    states_obs = []
    for obs_t in obs_times:
        # Znajdź ostatni stan przed lub w momencie obs_t
        idx = np.searchsorted(jump_times, obs_t, side='right') - 1
        if idx >= 0:
            states_obs.append(jump_states[idx])
        else:
            states_obs.append(state0)
    
    return states_obs, obs_times

def estimate_Q_from_data(states_seq: List[int], dt: float) -> np.ndarray:
    """Prosta estymacja Q z danych dyskretnych (MLE dla DTMC)."""
    n = 8
    counts = np.zeros((8, 8))
    for i in range(len(states_seq) - 1):
        counts[states_seq[i], states_seq[i+1]] += 1
    # MLE dla DTMC: P_ij = counts_ij / sum_j counts_ij
    P = np.zeros((8, 8))
    for i in range(8):
        row_sum = counts[i].sum()
        if row_sum > 0:
            P[i] = counts[i] / row_sum
    # Q z P = exp(Q*dt) -> Q = logm(P)/dt (uproszczone)
    # Uwaga: logm macierzy może dawać ujemne wartości na przekątnej
    # W praktyce używamy pakietu `msm` lub `ctmcm`
    return P  # Zwracamy P jako aproksymację

def run_simulation_study():
    """Główna funkcja symulacyjna."""
    results = []
    
    # Warunki eksperymentalne
    conditions = [
        {"name": "HPE_true_low", "model": "HPE", "rate": 0.5, "beta": 0.0},
        {"name": "HPE_true_med", "model": "HPE", "rate": 1.0, "beta": 0.0},
        {"name": "HPE_true_high", "model": "HPE", "rate": 2.0, "beta": 0.0},
        {"name": "HPE_false_low", "model": "FULL", "rate": 0.5, "beta": 0.0},
        {"name": "HPE_false_med", "model": "FULL", "rate": 1.0, "beta": 0.0},
    ]
    
    N_vals = [50, 100, 200]
    T_vals = [50, 100, 200]
    dt_vals = [0.5, 1.0, 2.0]
    n_rep = 1000
    
    for cond in conditions:
        for N in N_vals:
            for T in T_vals:
                for dt in dt_vals:
                    type1_errors = 0
                    power_count = 0
                    dH_ge_2_rates = []
                    
                    for rep in range(n_rep):
                        # Buduj Q
                        if cond["model"] == "HPE":
                            rates = {f"W_0→1": cond["rate"], "W_1→0": cond["rate"],
                                     "C_0→1": cond["rate"], "C_1→0": cond["rate"],
                                     "N_0→1": cond["rate"], "N_1→0": cond["rate"]}
                            Q = build_Q_hpe(rates)
                        else:
                            Q = build_Q_full({})
                        
                        # Symuluj dane dla N osób
                        all_states = []
                        for _ in range(N):
                            states_obs, _ = simulate_ctmc(Q, T, dt)
                            all_states.extend(states_obs)
                        
                        # Oblicz odsetek d_H >= 2
                        dH_ge_2 = sum(1 for i in range(len(all_states)-1) 
                                     if hamming(STATES[all_states[i]], STATES[all_states[i+1]]) >= 2)
                        total_trans = len(all_states) - 1
                        dH_ge_2_rates.append(dH_ge_2 / total_trans if total_trans > 0 else 0)
                        
                        # Estymacja Q (uproszczona - tu powinno być MLE przez msm/ctmcm)
                        # Tutaj placeholder - w rzeczywistości używamy pakietu msm/ctmcm
                        pass
                    
                    # Statystyki
                    mean_dH = np.mean(dH_ge_2_rates)
                    results.append({
                        "condition": cond["name"],
                        "N": N, "T": T, "dt": dt,
                        "mean_dH_ge_2": mean_dH,
                        "rate": cond["rate"],
                        "model": cond["model"]
                    })
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    # Test analityczny kontrprzykładu Astry
    print("=== Kontrprzykład Astry (analityczny) ===")
    for dt in [0.5, 1.0, 2.0, 3.0]:
        p = (1 - np.exp(-2 * 1.0 * dt)) / 2  # p dla jednego bitu
        p_dH_ge_2 = 3 * p**2 * (1 - p) + p**3
        print(f"dt={dt}h: P(d_H>=2) = {p_dH_ge_2:.3f} ({p_dH_ge_2*100:.1f}%)")
    
    print("\n=== Symulacja (placeholder) ===")
    print("Uruchomienie pełnej symulacji wymaga pakietu msm/ctmcm do estymacji Q.")
    print("Zobacz sekcję 'Kod symulacyjny' w model/HPE_formalizacja_rev1.md")
```

### 2.5. Kryteria sukcesu symulacji

| Metryka | Próg sukcesu |
|---------|--------------|
| Type I error (HPE prawdziwy) | 0.04 – 0.06 (dla α=0.05) |
| Power (HPE fałszywy, efekt średni) | > 0.80 |
| Bias $q_{ij}$ | < 10% wartości prawdziwej |
| Pokrycie 95% CI | 0.94 – 0.96 |
| Odsetek $d_H \geq 2$ przy HPE-model | > 15% przy realistycznych parametrach (potwierdzenie błędu progu 15%) |

---

## 3. Badanie Empiryczne (EMA Pilotażowe)

### 3.1. Grupa docelowa i procedura

| Parametr | Wartość |
|----------|---------|
| **Populacja** | N = 100–150 (jedna populacja, np. studenci uczący się języka) |
| **Działanie** | Jedno, powtarzalne, z realną zmiennością W, C, N (np. nauka języka 15 min/dzień) |
| **Czas trwania** | 14 dni |
| **Częstotliwość EMA** | Losowe: 5×/dzień (9:00–21:00); Event-based: do 1h po działaniu |
| **Odstępy** | Zmienne (Exp(mean=2h)) – dopasowane w symulacjach |
| **Pomiar W,C,N** | Skale Likert 1–7 (wersja ciągła) + wersja binarna (próg 4) |
| **Kowariancje** | AutonomySupport, Resources, RoleAmbiguity, HabitStrength, $N_{source}$ |

### 3.2. Procedura estymacji

1. **Przygotowanie danych:** Agregacja do stanów binarnych (próg 4) + zachowanie wersji ciągłej.
2. **Estymacja CTMC:** Pakiet `msm` (R) lub `ctmcm` (Python) – estymacja $Q$ z danych panelowych z kowariancjami.
3. **Test HPE-model:** LRT (M_HPE vs M_full) na estymowanym $Q$.
4. **Test HPE-empiryczna:** Porównanie odsetka $d_H \geq 2$ w danych z predykcjami M_HPE, M_full, M_indep.
5. **Test asymetrii:** LRT dla $q_{ij} = q_{ji}$ dla 12 par (FDR korekcja).
6. **Porównanie modeli:** AIC/BIC dla M_HPE, M_full, M_indep, M_cont.

### 3.3. Kryteria sukcesu badania pilotażowego

| Test | Kryterium sukcesu |
|------|-------------------|
| LRT (M_HPE vs M_full) | $p > 0.05$ – brak istotnej poprawy dopasowania przez M_full (HPE-model nie odrzucane) |
| ΔAIC (M_HPE vs M_full) | > 10 na korzyść M_HPE |
| ΔAIC (M_HPE vs M_indep) | > 6 na korzyść M_HPE (zależność od konfiguracji) |
| Asymetria | Istotna ($p < 0.05$ po FDR) dla ≥ 3 kluczowych par (011↔111, 111↔011, 101↔111) |
| Predykcja out-of-sample | Log-loss M_HPE < M_full, M_indep, M_cont (test Diebold-Mariano $p < 0.05$) |

**Uwaga:** Istotny LRT ($p < 0.05$) oznacza, że M_full dopasowuje istotnie lepiej – to dowód **PRZECIW** HPE-model. Brak istotności ($p > 0.05$) nie dowodzi HPE-model, ale nie pozwala go odrzucić. Wymagana kalibracja bootstrap parametryczny ze względu na parametry na brzegu przestrzeni.

---

## 4. Analiza Mocy (Power Analysis) – Plan

### 4.1. Parametry do symulacji mocy

| Parametr | Wartości |
|----------|----------|
| $N$ | 100, 200, 300, 500 |
| $T$ (pomiarów/osobę) | 50, 100, 150, 200 |
| Intensywności $q_{ij}$ | Niskie (0.1/h), średnie (0.5/h), wysokie (1.0/h) |
| Efekty kowariancji $\beta$ | OR = 1.5, 2.5, 4.0 |
| Błąd klasyfikacji | 0%, 5%, 10%, 20% |

### 4.2. Testy do oceny mocy

1. **Test HPE (LRT M_HPE vs M_full)**
2. **Test asymetrii (LRT $q_{ij} = q_{ji}$)** dla kluczowych par
3. **Test mediacji** (np. E3, E7, E13, E15)
3. **Predykcja zachowania** (log-loss out-of-sample)

### 4.3. Decyzja
Na podstawie symulacji: ustalenie minimalnych $N$ i $T$ dla mocy > 0.80 przy efekcie średnim dla testów kluczowych.

---

## 5. Harmonogram Wdrożenia

| Tydzień | Zadanie |
|---------|---------|
| 1–2 | Implementacja `src/hpe_simulation.py` + uruchomienie symulacji weryfikacyjnych |
| 3–4 | Analiza wyników symulacji; ustalenie minimalnych N, T dla mocy > 0.80 |
| 5–6 | Przygotowanie protokołu EMA (itemy, aplikacja, rekrutacja) |
| 7–10 | Badanie pilotażowe (N=100, 14 dni) |
| 11–12 | Estymacja CTMC, testy HPE, asymetrii, porównanie modeli |
| 13 | Raport pilotażowy; decyzja o Etapie 4 (główne badanie) |

---

## 6. Zmiany względem wersji pierwotnej

| Element | Wersja pierwotna | Wersja rev1 |
|---------|------------------|-------------|
| Test HPE | LTA: $p_{ij}=0$ dla $d_H \geq 2$ | **CTMC:** LRT (M_HPE vs M_full) na estymowanym $Q$ |
| Próg falsyfikacji | >15% $d_H \geq 2$ przy EMA co 30 min | **Usunięty** – arbitralny (kontrprzykład: 23.7% przy HPE) |
| Model alternatywny | Niejawny | **Jawne:** M_full, M_indep, M_cont, M_meas |
| Test asymetrii | Próg 50% par | **LRT na poziomie $q_{ij}$** + wielkość efektu + FDR |
| Dane | Binarne (LTA) | **Ciągłe W,C,N (1–7)** + dyskretyzacja do 8 stanów |
| Estymacja | LTA (klasy latentne) | **CTMC z obserwowanymi stanami** (unikanie problemu identyfikowalności) |

---

*Dokument wersja 1.0. Gotowy do implementacji w `src/hpe_simulation.py` i wdrożenia w badaniu pilotażowym (Etap 3).*