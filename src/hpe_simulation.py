#!/usr/bin/env python3
"""
HPE Simulation Module for DMTRD
Symulacja CTMC do weryfikacji HPE-model i testów mocy.
"""

import numpy as np
from scipy.linalg import expm
from scipy.stats import chi2
import pandas as pd
from typing import Dict, List, Tuple, Optional
import json
import warnings

# Ustawienie ziarna dla odtwarzalności
np.random.seed(42)

STATES = ['000', '001', '010', '011', '100', '101', '110', '111']
STATE_TO_IDX = {s: i for i, s in enumerate(STATES)}
IDX_TO_STATE = {i: s for i, s in enumerate(STATES)}


def hamming(s1: str, s2: str) -> int:
    """Odległość Hamminga między dwoma stanami."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def build_Q_hpe(rates: Dict[str, float]) -> np.ndarray:
    """
    Buduje generator Q spełniający HPE-model (tylko d_H=1).
    
    Parametry rates: słownik z kluczami typu 'W_0→1', 'W_1→0', 'C_0→1', itd.
    """
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


def build_Q_indep(rates: Dict[str, float]) -> np.ndarray:
    """
    Buduje generator Q dla modelu niezależnych bitów (M_indep).
    Intensywność zależy tylko od zmieniającego się bitu, nie od konfiguracji.
    """
    Q = np.zeros((8, 8))
    for i, s1 in enumerate(STATES):
        for j, s2 in enumerate(STATES):
            if i != j and hamming(s1, s2) == 1:
                diff_idx = [k for k, (a, b) in enumerate(zip(s1, s2)) if a != b][0]
                bit_name = 'WCN'[diff_idx]
                direction = f"{s1[diff_idx]}→{s2[diff_idx]}"
                key = f"{bit_name}_{direction}"
                Q[i, j] = rates.get(key, 0.0)
    for i in range(8):
        Q[i, i] = -Q[i].sum()
    return Q


def build_Q_full(rates: Dict[str, float]) -> np.ndarray:
    """
    Buduje pełny generator Q (M_full) - wszystkie przejścia i≠j dozwolone.
    Dla uproszczenia: intensywność maleje wykładniczo z d_H.
    """
    Q = np.zeros((8, 8))
    base_rate = 0.5
    for i, s1 in enumerate(STATES):
        for j, s2 in enumerate(STATES):
            if i != j:
                dH = hamming(STATES[i], STATES[j])
                Q[i, j] = base_rate * (0.5 ** (dH - 1))
    for i in range(8):
        Q[i, i] = -Q[i].sum()
    return Q


def simulate_ctmc(Q: np.ndarray, T: float, dt_obs: float, 
                  state0: Optional[int] = None) -> Tuple[List[int], np.ndarray]:
    """
    Symuluje CTMC z generatorem Q, zwraca stany w momentach obserwacji co dt_obs.
    
    Returns:
        states_obs: lista stanów w momentach obserwacji
        obs_times: czasy obserwacji
    
    Uwaga: Naprawiono błąd indeksowania (CR-01 z recenzji GPT-6).
    jump_states[0] = stan początkowy, jump_states[k] = stan po k-tym skoku.
    jump_times zawiera czasy skoków (bez czasu 0).
    Dla obserwacji w czasie obs_t, stan = jump_states[k] gdzie k = liczba skoków przed obs_t.
    """
    if state0 is None:
        state0 = np.random.choice(8)
    
    obs_times = np.arange(0, T + dt_obs/2, dt_obs)
    
    # Symulacja skoków
    jump_times = []
    jump_states = [state0]  # jump_states[0] = stan początkowy (przed pierwszym skokiem)
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
        if probs.sum() == 0:
            break
        probs = probs / probs.sum()
        next_state = np.random.choice(8, p=probs)
        jump_times.append(t)
        jump_states.append(next_state)  # stan PO skoku
        current = next_state
    
    # Próbkowanie co dt_obs
    # jump_states[0] = stan przed pierwszym skokiem (czas 0)
    # jump_states[k] = stan po k-tym skoku (dla k >= 1)
    # Liczba skoków przed czasem obs_t = np.searchsorted(jump_times, obs_t, side='right')
    states_obs = []
    for obs_t in obs_times:
        k = np.searchsorted(jump_times, obs_t, side='right')  # liczba skoków przed obs_t
        states_obs.append(jump_states[k])
    
    return states_obs, obs_times


def estimate_P_from_data(states_seq: List[int]) -> np.ndarray:
    """Estymuje macierz przejścia P z sekwencji stanów (MLE dla DTMC)."""
    n = 8
    counts = np.zeros((8, 8))
    for i in range(len(states_seq) - 1):
        counts[states_seq[i], states_seq[i+1]] += 1
    P = np.zeros((8, 8))
    for i in range(8):
        row_sum = counts[i].sum()
        if row_sum > 0:
            P[i] = counts[i] / row_sum
    return P


def estimate_Q_from_P(P: np.ndarray, dt: float) -> np.ndarray:
    """
    Estymuje Q z P = exp(Q*dt) używając logarytmu macierzowego.
    Uwaga: logm może dawać ujemne wartości na przekątnej dla macierzy nieodwracalnych.
    W praktyce używamy pakietu `msm` lub `ctmcm` do estymacji Q z danych panelowych.
    """
    try:
        from scipy.linalg import logm
        Q = logm(P) / dt
        # Wymuś nieujemne wartości poza przekątną
        np.fill_diagonal(Q, 0)
        Q = np.maximum(Q, 0)
        # Popraw przekątną
        for i in range(8):
            Q[i, i] = -Q[i].sum()
        return Q
    except Exception:
        # Fallback: aproksymacja dla małych dt
        Q = (P - np.eye(8)) / dt
        np.fill_diagonal(Q, 0)
        Q = np.maximum(Q, 0)
        for i in range(8):
            Q[i, i] = -Q[i].sum()
        return Q


def lrt_test(Q_hpe: np.ndarray, Q_full: np.ndarray, dt: float, 
             n_obs: int) -> Tuple[float, float]:
    """
    Test LRT: M_HPE vs M_full.
    H0: q_ij = 0 dla d_H >= 2 (M_HPE)
    H1: q_ij >= 0 dla wszystkich i≠j (M_full)
    
    Uwaga: Standardowy chi-kwadrat może nie być poprawny dla parametrów na brzegu.
    W praktyce: bootstrap parametryczny.
    
    NOT IMPLEMENTED: This is a placeholder. Full implementation requires:
    - Estimation of Q_hpe and Q_full from data using msm/ctmcm
    - Parametric bootstrap for correct null distribution (parameters on boundary)
    - Proper log-likelihood computation for CTMC
    
    Returns:
        (test_statistic, p_value) - currently returns placeholder
    
    Raises:
        NotImplementedError: This function is not yet implemented.
    """
    raise NotImplementedError(
        "lrt_test() is not implemented. "
        "Requires msm/ctmcm for Q estimation and parametric bootstrap for valid p-values. "
        "See model/HPE_formalizacja_rev1.md for details."
    )


def analytical_dH_ge_2(lambda_rate: float = 1.0, dt: float = 0.5) -> float:
    """Analityczne P(d_H >= 2) dla 3 niezależnych bitów."""
    p = (1 - np.exp(-2 * lambda_rate * dt)) / 2
    return 3 * p**2 * (1 - p) + p**3


def run_conterexample_astra():
    """Weryfikacja kontrprzykladu Astry: przy HPE-model odsetek d_H>=2 moze > 15%."""
    print("=== Kontrprzyklad Astry (analityczny) ===")
    for dt in [0.5, 1.0, 2.0, 3.0]:
        p = analytical_dH_ge_2(lambda_rate=1.0, dt=dt)
        print(f"dt={dt}h: P(d_H >= 2) = {p:.3f} ({p*100:.1f}%)")
    
    print("\nWniosek: Prog 15% jest bezuzyteczny - przy HPE-model i lambda=1/h,")
    print("przy pomiarach co 30 min odsetek d_H>=2 wynosi 23.7% > 15%.")


def run_simulation_demo(n_sim: int = 1000, dt: float = 0.5, T: float = 24.0) -> dict:
    """
    Demonstracyjna symulacja: porównanie M_HPE vs M_full.
    """
    # Parametry: niezależne bity, λ=1/h
    rates = {
        'W_0→1': 1.0, 'W_1→0': 1.0,
        'C_0→1': 1.0, 'C_1→0': 1.0,
        'N_0→1': 1.0, 'N_1→0': 1.0
    }
    
    Q_hpe = build_Q_hpe(rates)
    
    # M_full: dodatkowe przejścia d_H=2,3 z intensywnością 0.1
    Q_full = build_Q_hpe(rates)
    for i, s1 in enumerate(STATES):
        for j, s2 in enumerate(STATES):
            if i != j and hamming(STATES[i], STATES[j]) >= 2:
                Q_full[i, j] = 0.1
    for i in range(8):
        Q_full[i, i] = -Q_full[i].sum()
    
    results = {'hpe': [], 'full': []}
    
    for model_name, Q in [('hpe', Q_hpe), ('full', Q_full)]:
        dH_ge_2_counts = []
        for _ in range(n_sim):
            states_obs, _ = simulate_ctmc(Q, T=24.0, dt_obs=0.5)
            dH_ge_2 = sum(1 for i in range(len(states_obs)-1) 
                         if hamming(STATES[states_obs[i]], STATES[states_obs[i+1]]) >= 2)
            total = len(states_obs) - 1
            if total > 0:
                results[model_name].append(dH_ge_2 / total)
    
    return {
        'hpe_mean': np.mean(results['hpe']),
        'full_mean': np.mean(results['full']),
        'hpe_std': np.std(results['hpe']),
        'full_std': np.std(results['full'])
    }


def run_power_simulation(n_rep: int = 500, N: int = 100, T: int = 100, 
                         dt: float = 1.0, lambda_rate: float = 1.0) -> dict:
    """
    Symulacja mocy testu LRT (M_HPE vs M_full).
    Uproszczona wersja - w praktyce wymaga estymacji Q przez msm/ctmcm.
    """
    print(f"Running power simulation: N={N}, T={T}, dt={dt}, reps={n_rep}")
    print("Uwaga: Pełna symulacja mocy wymaga pakietu msm/ctmcm do estymacji Q.")
    print("Ta funkcja jest demonstracyjna.")
    
    return {
        'note': 'Placeholder - requires msm/ctmcm for actual Q estimation',
        'params': {'N': N, 'T': T, 'dt': dt, 'reps': n_rep}
    }


def test_simulate_ctmc_deterministic():
    """
    Test deterministyczny dla simulate_ctmc (CR-01).
    Weryfikuje poprawność indeksowania stanów przy znanym harmonogramie skoków.
    """
    print("\n=== Test deterministyczny simulate_ctmc (CR-01) ===")
    
    # Prosty Q: 000 -> 001 -> 011 z intensywnością 1.0
    # Stan 0 (000) -> stan 1 (001) -> stan 3 (011)
    Q = np.zeros((8, 8))
    Q[0, 1] = 1.0  # 000 -> 001
    Q[1, 3] = 1.0  # 001 -> 011
    Q[0, 0] = -1.0
    Q[1, 1] = -1.0
    Q[3, 3] = 0.0  # stan chłonny dla testu
    
    # Symulacja z deterministycznymi skokami (używamy seed)
    np.random.seed(12345)
    
    # Test 1: Sprawdź czy stan w czasie 0.0 to stan początkowy (0)
    states_obs, obs_times = simulate_ctmc(Q, T=1.0, dt_obs=0.5, state0=0)
    print(f"Czasy obserwacji: {obs_times}")
    print(f"Stany obserwowane: {[STATES[s] for s in states_obs]}")
    
    # Test 2: Znany harmonogram skoków - test indeksowania
    # Używamy Q z bardzo wysoką intensywnością, by wymusić szybkie skoki
    Q_fast = np.zeros((8, 8))
    Q_fast[0, 1] = 1000.0  # 000 -> 001 niemal natychmiast
    Q_fast[1, 3] = 1000.0  # 001 -> 011 niemal natychmiast
    Q_fast[0, 0] = -1000.0
    Q_fast[1, 1] = -1000.0
    Q_fast[3, 3] = 0.0
    
    np.random.seed(42)
    states_obs2, obs_times2 = simulate_ctmc(Q_fast, T=1.0, dt_obs=0.5, state0=0)
    print(f"\nTest szybkich skoków (Q_fast):")
    print(f"Czasy: {obs_times2}")
    print(f"Stany: {[STATES[s] for s in states_obs2]}")
    print(f"Oczekiwane: 000 -> 001 -> 011 (bo skoki niemal natychmiastowe)")
    
    # Test 3: Weryfikacja zgodności z exp(Q*dt) dla prostego Q
    print("\n=== Test zgodności z exp(Q*dt) ===")
    Q_test = np.zeros((8, 8))
    Q_test[0, 1] = 1.0
    Q_test[0, 0] = -1.0
    Q_test[1, 1] = 0.0  # chłonny
    
    from scipy.linalg import expm
    dt = 0.5
    P_exact = expm(Q_test * dt)
    print(f"P_exact[0,0] (pozostanie w 000) = {P_exact[0,0]:.4f}")
    print(f"P_exact[0,1] (przejście 000->001) = {P_exact[0,1]:.4f}")
    
    # Monte Carlo
    n_mc = 10000
    count_00 = 0
    count_01 = 0
    for _ in range(n_mc):
        states_obs, _ = simulate_ctmc(Q_test, T=dt, dt_obs=dt, state0=0)
        if states_obs[1] == 0:
            count_00 += 1
        elif states_obs[1] == 1:
            count_01 += 1
    
    print(f"MC: P(000->000) = {count_00/n_mc:.4f}, P(000->001) = {count_01/n_mc:.4f}")
    print(f"Różnica: {abs(count_00/n_mc - P_exact[0,0]):.4f}, {abs(count_01/n_mc - P_exact[0,1]):.4f}")
    
    if abs(count_00/n_mc - P_exact[0,0]) < 0.02 and abs(count_01/n_mc - P_exact[0,1]) < 0.02:
        print("[OK] TEST PRZESZEDL: Symulacja zgodna z teoria (exp(Q*dt))")
        return True
    else:
        print("[BLAD] TEST NIE PRZESZEDL: Symulacja NIEGODNA z teoria")
        return False


if __name__ == "__main__":
    print("=== DMTRD HPE Simulation Module ===\n")
    
    # 1. Test deterministyczny (CR-01)
    test_passed = test_simulate_ctmc_deterministic()
    
    # 2. Kontrprzykład Astry
    print("\n=== Kontrprzykład Astry (analityczny) ===")
    run_conterexample_astra()
    
    # 3. Demonstracyjna symulacja
    print("\n=== Demonstracyjna symulacja (M_HPE vs M_full) ===")
    demo_results = run_simulation_demo(n_sim=500)
    print(f"M_HPE: mean d_H>=2 = {demo_results['hpe_mean']:.3f} ± {demo_results['hpe_std']:.3f}")
    print(f"M_full: mean d_H>=2 = {demo_results['full_mean']:.3f} ± {demo_results['full_std']:.3f}")
    
    # 4. Test mocy (placeholder)
    print("\n=== Test mocy (placeholder) ===")
    run_power_simulation()
    
    print("\n=== Uwaga ===")
    print("Pełna symulacja mocy i testy LRT wymagają pakietu msm (R) lub ctmcm (Python)")
    print("do estymacji Q z danych panelowych. Ten moduł dostarcza narzędzia do")
    print("generowania danych i weryfikacji kontrprzykładu Astry.")
    print(f"\nTest CR-01: {'PRZESZŁ' if test_passed else 'NIE PRZESZŁ'}")