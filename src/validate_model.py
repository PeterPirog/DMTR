#!/usr/bin/env python3
"""
DMTRD Model Validator
Waliduje strukturę grafu Q3, stanów i przejść.
"""

import csv
import sys
from pathlib import Path
from lxml import etree
import networkx as nx

BASE = Path(__file__).parent.parent
MODEL_DIR = BASE / "model"
DIAGRAMS_DIR = BASE / "diagrams"

def load_states():
    states = {}
    with open(MODEL_DIR / "stany.csv", 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            states[row['kod']] = row
    return states

def load_transitions():
    transitions = []
    with open(MODEL_DIR / "przejscia_24.csv", 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transitions.append(row)
    return transitions

def hamming_distance(s1, s2):
    """Odległość Hamminga między dwoma kodami binarnymi."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def validate_states(states):
    """Waliduje stany."""
    errors = []
    warnings = []
    
    # 1. Dokładnie 8 stanów
    if len(states) != 8:
        errors.append(f"Liczba stanów: {len(states)} (oczekiwano 8)")
    
    # 2. Unikalność kodów
    codes = list(states.keys())
    if len(set(codes)) != len(codes):
        errors.append("Zduplikowane kody stanów")
    
    # 3. Wszystkie kody to 3-bity
    expected_codes = {"000", "001", "010", "011", "100", "101", "110", "111"}
    if set(codes) != expected_codes:
        errors.append(f"Kody stanów nie zgadzają się: {set(codes) ^ expected_codes}")
    
    # 4. Spójność W,C,N z kodem
    for code, state in states.items():
        if state['W'] != code[0] or state['C'] != code[1] or state['N'] != code[2]:
            errors.append(f"Stan {code}: niespójność W,C,N z kodem (W={state['W']},C={state['C']},N={state['N']})")
    
    # 5. Każdy stan ma 3 przejścia wychodzące (w danych)
    for code, state in states.items():
        out = state['przejscia_wychodzace'].split(', ')
        if len(out) != 3:
            warnings.append(f"Stan {code}: {len(out)} przejść wychodzących (oczekiwano 3): {out}")
    
    # 6. Każdy stan ma 3 przejścia przychodzące
    for code, state in states.items():
        inn = state['przejscia_przychodzace'].split(', ')
        if len(inn) != 3:
            warnings.append(f"Stan {code}: {len(inn)} przejść przychodzących (oczekiwano 3): {inn}")
    
    return errors, warnings

def validate_transitions(transitions, states):
    """Waliduje przejścia."""
    errors = []
    warnings = []
    
    # 1. Dokładnie 24 przejścia
    if len(transitions) != 24:
        errors.append(f"Liczba przejść: {len(transitions)} (oczekiwano 24)")
    
    # 2. Unikalność ID
    ids = [t['id'] for t in transitions]
    if len(set(ids)) != len(ids):
        errors.append("Zduplikowane ID przejść")
    
    # 3. Wszystkie przejścia mają d_H = 1
    for t in transitions:
        d = hamming_distance(t['start'], t['end'])
        if d != 1:
            errors.append(f"Przejście {t['id']}: {t['start']}→{t['end']} ma d_H={d} (oczekiwano 1)")
    
    # 4. Zmieniony wymiar zgadza się z różnicą bitów
    for t in transitions:
        start, end = t['start'], t['end']
        dim = t['zmieniony_wymiar']
        diff_idx = [i for i, (a, b) in enumerate(zip(start, end)) if a != b]
        if len(diff_idx) != 1:
            errors.append(f"Przejście {t['id']}: niejednoznaczna zmiana bitów")
            continue
        expected_dim = "WCN"[diff_idx[0]]
        if dim != expected_dim:
            errors.append(f"Przejście {t['id']}: zmieniony wymiar={dim}, oczekiwano={expected_dim}")
    
    # 5. Kierunek zmiany zgadza się
    for t in transitions:
        start, end = t['start'], t['end']
        dim = t['zmieniony_wymiar']
        idx = "WCN".index(dim)
        expected_dir = f"{start[idx]}→{end[idx]}"
        if t['kierunek'] != expected_dir:
            errors.append(f"Przejście {t['id']}: kierunek={t['kierunek']}, oczekiwano={expected_dir}")
    
    # 6. Istnienie przejścia odwrotnego
    trans_set = {(t['start'], t['end']) for t in transitions}
    for t in transitions:
        rev = (t['end'], t['start'])
        if rev not in trans_set:
            errors.append(f"Brak przejścia odwrotnego dla {t['id']}: {t['start']}→{t['end']}")
    
    # 7. Brak przejść wielobitowych (d_H >= 2) w liście
    for t in transitions:
        if hamming_distance(t['start'], t['end']) >= 2:
            errors.append(f"Przejście {t['id']} jest wielobitowe (d_H >= 2)")
    
    # 8. Spójność ze stanami (przejscia_wychodzace/przychodzace)
    for code, state in states.items():
        out_expected = set(state['przejscia_wychodzace'].split(', '))
        out_actual = {t['id'] for t in transitions if t['start'] == code}
        if out_expected != out_actual:
            warnings.append(f"Stan {code}: niespójność przejść wychodzących. CSV: {out_expected}, Trans: {out_actual}")
        
        in_expected = set(state['przejscia_przychodzace'].split(', '))
        in_actual = {t['id'] for t in transitions if t['end'] == code}
        if in_expected != in_actual:
            warnings.append(f"Stan {code}: niespójność przejść przychodzących. CSV: {in_expected}, Trans: {in_actual}")
    
    return errors, warnings

def validate_graphml_12(filepath):
    """Waliduje plik GraphML 12 krawędzi."""
    errors = []
    warnings = []
    
    try:
        tree = etree.parse(str(filepath))
        root = tree.getroot()
        
        # Namespace
        ns = {"g": "http://graphml.graphdrawing.org/xmlns"}
        
        # Liczba węzłów
        nodes = root.findall(".//g:node", ns)
        if len(nodes) != 8:
            errors.append(f"GraphML 12: liczba węzłów = {len(nodes)} (oczekiwano 8)")
        
        # Liczba krawędzi
        edges = root.findall(".//g:edge", ns)
        if len(edges) != 12:
            errors.append(f"GraphML 12: liczba krawędzi = {len(edges)} (oczekiwano 12)")
        
        # Sprawdź czy graf jest nieskierowany
        graph_elem = root.find(".//g:graph", ns)
        if graph_elem is not None:
            edgedefault = graph_elem.get("edgedefault")
            if edgedefault != "undirected":
                warnings.append(f"GraphML 12: edgedefault = {edgedefault} (oczekiwano undirected)")
        
    except Exception as e:
        errors.append(f"GraphML 12: błąd parsowania: {e}")
    
    return errors, warnings

def validate_graphml_24(filepath):
    """Waliduje plik GraphML 24 przejścia."""
    errors = []
    warnings = []
    
    try:
        tree = etree.parse(str(filepath))
        root = tree.getroot()
        
        ns = {"g": "http://graphml.graphdrawing.org/xmlns"}
        
        nodes = root.findall(".//g:node", ns)
        if len(nodes) != 8:
            errors.append(f"GraphML 24: liczba węzłów = {len(nodes)} (oczekiwano 8)")
        
        edges = root.findall(".//g:edge", ns)
        if len(edges) != 24:
            errors.append(f"GraphML 24: liczba krawędzi = {len(edges)} (oczekiwano 24)")
        
        graph_elem = root.find(".//g:graph", ns)
        if graph_elem is not None:
            edgedefault = graph_elem.get("edgedefault")
            if edgedefault != "directed":
                warnings.append(f"GraphML 24: edgedefault = {edgedefault} (oczekiwano directed)")
        
    except Exception as e:
        errors.append(f"GraphML 24: błąd parsowania: {e}")
    
    return errors, warnings

def validate_networkx_q3(states, transitions):
    """Waliduje strukturę Q3 używając NetworkX."""
    errors = []
    warnings = []
    
    G = nx.Graph()
    for code in states:
        G.add_node(code)
    
    for t in transitions:
        G.add_edge(t['start'], t['end'])
    
    # 1. Liczba węzłów
    if G.number_of_nodes() != 8:
        errors.append(f"NX: węzły = {G.number_of_nodes()}")
    
    # 2. Liczba krawędzi nieskierowanych (unikalne pary)
    if G.number_of_edges() != 12:
        errors.append(f"NX: krawędzie nieskierowane = {G.number_of_edges()} (oczekiwano 12)")
    
    # 3. Stopnie węzłów = 3
    for node in G.nodes():
        if G.degree(node) != 3:
            errors.append(f"NX: węzeł {node} ma stopień {G.degree(node)} (oczekiwano 3)")
    
    # 4. Spójność
    if not nx.is_connected(G):
        errors.append("NX: graf niespójny")
    
    # 5. Dwudzielność (Q3 jest bipartytny)
    if not nx.is_bipartite(G):
        errors.append("NX: graf nie jest dwudzielny (Q3 powinien być)")
    
    # 6. Średnica = 3
    try:
        diam = nx.diameter(G)
        if diam != 3:
            warnings.append(f"NX: średnica = {diam} (oczekiwano 3)")
    except:
        warnings.append("NX: nie można obliczyć średnicy")
    
    # 7. Liczba cykli 4 (kwadratów w Q3) = 6
    # Q3 ma 6 ścian (cykli 4)
    cycles_4 = 0
    for cycle in nx.simple_cycles(G.to_directed()):
        if len(cycle) == 4:
            cycles_4 += 1
    cycles_4 = cycles_4 // 8  # każdy cykl policzony 8 razy (4 rotacje * 2 kierunki)
    if cycles_4 != 6:
        warnings.append(f"NX: cykle 4-elementowe = {cycles_4} (oczekiwano 6)")
    
    return errors, warnings

def validate_csv_consistency(states, transitions):
    """Waliduje spójność danych CSV."""
    errors = []
    warnings = []
    
    # Sprawdź czy wszystkie stany w przejściach istnieją
    state_codes = set(states.keys())
    for t in transitions:
        if t['start'] not in state_codes:
            errors.append(f"Przejście {t['id']}: stan startowy {t['start']} nie istnieje")
        if t['end'] not in state_codes:
            errors.append(f"Przejście {t['id']}: stan końcowy {t['end']} nie istnieje")
    
    return errors, warnings

def main():
    print("=" * 60)
    print("DMTRD MODEL VALIDATION")
    print("=" * 60)
    
    states = load_states()
    transitions = load_transitions()
    
    all_errors = []
    all_warnings = []
    
    # Walidacje
    print("\n1. Walidacja stanów (stany.csv)...")
    e, w = validate_states(states)
    all_errors.extend(e)
    all_warnings.extend(w)
    print(f"   Błędy: {len(e)}, Ostrzeżenia: {len(w)}")
    
    print("\n2. Walidacja przejść (przejscia_24.csv)...")
    e, w = validate_transitions(transitions, states)
    all_errors.extend(e)
    all_warnings.extend(w)
    print(f"   Błędy: {len(e)}, Ostrzeżenia: {len(w)}")
    
    print("\n3. Walidacja spójności CSV...")
    e, w = validate_csv_consistency(states, transitions)
    all_errors.extend(e)
    all_warnings.extend(w)
    print(f"   Błędy: {len(e)}, Ostrzeżenia: {len(w)}")
    
    print("\n4. Walidacja GraphML 12 krawędzi...")
    e, w = validate_graphml_12(DIAGRAMS_DIR / "DMTRD_12_krawedzi.graphml")
    all_errors.extend(e)
    all_warnings.extend(w)
    print(f"   Błędy: {len(e)}, Ostrzeżenia: {len(w)}")
    
    print("\n5. Walidacja GraphML 24 przejścia...")
    e, w = validate_graphml_24(DIAGRAMS_DIR / "DMTRD_24_przejscia.graphml")
    all_errors.extend(e)
    all_warnings.extend(w)
    print(f"   Błędy: {len(e)}, Ostrzeżenia: {len(w)}")
    
    print("\n6. Walidacja topologii Q3 (NetworkX)...")
    e, w = validate_networkx_q3(states, transitions)
    all_errors.extend(e)
    all_warnings.extend(w)
    print(f"   Błędy: {len(e)}, Ostrzeżenia: {len(w)}")
    
    # Podsumowanie
    print("\n" + "=" * 60)
    print("PODSUMOWANIE")
    print("=" * 60)
    
    if all_errors:
        print(f"\nBLEDY ({len(all_errors)}):")
        for err in all_errors:
            print(f"  X {err}")
    else:
        print("\nV WSZYSTKIE TESTY PRZESZLY POMYSLNIE (0 bledow)")
    
    if all_warnings:
        print(f"\nOSTRZEZENIA ({len(all_warnings)}):")
        for warn in all_warnings:
            # Replace Unicode arrows for console output
            warn_safe = warn.replace('\u2192', '->').replace('\u2713', 'V').replace('\u2717', 'X')
            print(f"  ! {warn_safe}")
    
    # Kod wyjścia
    if all_errors:
        print("\nSTATUS: FAIL")
        sys.exit(1)
    else:
        print("\nSTATUS: PASS")
        sys.exit(0)

if __name__ == "__main__":
    main()