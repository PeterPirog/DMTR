#!/usr/bin/env python3
"""
Generate SVG/PNG diagrams for DMTRD using matplotlib/networkx.
Fallback since yEd is not available.
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import networkx as nx
import csv
from pathlib import Path

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

# Node positions (Q3 cube layout)
POSITIONS = {
    "000": (0, 0, 0),
    "001": (0, 0, 1),
    "010": (0, 1, 0),
    "011": (0, 1, 1),
    "100": (1, 0, 0),
    "101": (1, 0, 1),
    "110": (1, 1, 0),
    "111": (1, 1, 1),
}

# Project 3D to 2D for visualization
def project_3d_to_2d(pos_3d):
    x, y, z = pos_3d
    # Isometric projection
    x2d = (x - y) * 1.5
    y2d = (x + y) * 0.8 - z * 1.2
    return (x2d, y2d)

POS_2D = {k: project_3d_to_2d(v) for k, v in POSITIONS.items()}

# Colors for dimensions
DIM_COLORS = {"W": "#E74C3C", "C": "#2ECC71", "N": "#3498DB"}
DIM_LABELS = {"W": "CHCĘ", "C": "MOGĘ", "N": "POWINIENEM"}

def draw_graph_12_edges(states, transitions, output_path):
    """Draw undirected graph with 12 edges (Q3 cube)."""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    G = nx.Graph()
    for code in states:
        G.add_node(code)
    
    # Add undirected edges (unique pairs)
    edge_set = set()
    for t in transitions:
        pair = tuple(sorted([t['start'], t['end']]))
        edge_set.add(pair)
    
    for u, v in edge_set:
        G.add_edge(u, v)
    
    # Node colors based on number of 1s
    node_colors = []
    for node in G.nodes():
        ones = sum(int(c) for c in node)
        if ones == 0:
            node_colors.append("#F5F5F5")
        elif ones == 1:
            node_colors.append("#FFF3E0")
        elif ones == 2:
            node_colors.append("#FFE0B2")
        else:
            node_colors.append("#FFCC80")
    
    # Draw
    nx.draw_networkx_nodes(G, POS_2D, node_color=node_colors, node_size=2000, 
                          edgecolors='black', linewidths=2, ax=ax)
    nx.draw_networkx_edges(G, POS_2D, edge_color='gray', width=2, ax=ax)
    nx.draw_networkx_labels(G, POS_2D, font_size=14, font_weight='bold', ax=ax)
    
    # Edge labels (dimension)
    edge_labels = {}
    for u, v in G.edges():
        # Find dimension
        for t in transitions:
            if (t['start'] == u and t['end'] == v) or (t['start'] == v and t['end'] == u):
                edge_labels[(u, v)] = DIM_LABELS[t['zmieniony_wymiar']]
                break
    
    nx.draw_networkx_edge_labels(G, POS_2D, edge_labels=edge_labels, font_size=10, ax=ax)
    
    ax.set_title("DMTRD: Graf stanów (12 krawędzi nieskierowanych / Q3)", fontsize=16, fontweight='bold')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")

def draw_graph_24_transitions(states, transitions, output_path):
    """Draw directed graph with 24 transitions."""
    fig, ax = plt.subplots(figsize=(14, 12))
    
    G = nx.DiGraph()
    for code in states:
        G.add_node(code)
    
    for t in transitions:
        G.add_edge(t['start'], t['end'], dim=t['zmieniony_wymiar'])
    
    # Node colors
    node_colors = []
    for node in G.nodes():
        ones = sum(int(c) for c in node)
        if ones == 0:
            node_colors.append("#F5F5F5")
        elif ones == 1:
            node_colors.append("#FFF3E0")
        elif ones == 2:
            node_colors.append("#FFE0B2")
        else:
            node_colors.append("#FFCC80")
    
    # Draw nodes
    nx.draw_networkx_nodes(G, POS_2D, node_color=node_colors, node_size=2500, 
                          edgecolors='black', linewidths=2, ax=ax)
    
    # Draw edges by dimension with different colors and styles
    for dim in ['W', 'C', 'N']:
        edges_dim = [(u, v) for u, v, d in G.edges(data=True) if d['dim'] == dim]
        color = DIM_COLORS[dim]
        nx.draw_networkx_edges(G, POS_2D, edgelist=edges_dim, edge_color=color, 
                              width=2, arrows=True, arrowsize=20, arrowstyle='->', 
                              connectionstyle='arc3,rad=0.1', ax=ax)
    
    # Labels
    nx.draw_networkx_labels(G, POS_2D, font_size=14, font_weight='bold', ax=ax)
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=DIM_COLORS['W'], label='W: CHCĘ'),
        Patch(facecolor=DIM_COLORS['C'], label='C: MOGĘ'),
        Patch(facecolor=DIM_COLORS['N'], label='N: POWINIENEM'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=12)
    
    ax.set_title("DMTRD: 24 przejścia kierunkowe (hipoteza jednego bitu)", fontsize=16, fontweight='bold')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")

def draw_state_table(states, output_path):
    """Draw a summary table of states."""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('off')
    
    # Table data
    headers = ['Kod', 'W', 'C', 'N', 'Nazwa naukowa', 'Interpretacja psychologiczna']
    rows = []
    for code in sorted(states.keys()):
        s = states[code]
        rows.append([
            code, s['W'], s['C'], s['N'], 
            s['nazwa_naukowa'],
            s['interpretacja_psychologiczna'][:80] + '...'
        ])
    
    table = ax.table(cellText=rows, colLabels=headers, loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Style header
    for i in range(len(headers)):
        table[(0, i)].set_facecolor('#4472C4')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternate row colors
    for i in range(1, len(rows) + 1):
        for j in range(len(headers)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#F2F2F2')
    
    ax.set_title("DMTRD: Osiem stanów motywacyjnych", fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")

def main():
    states = load_states()
    transitions = load_transitions()
    
    draw_graph_12_edges(states, transitions, DIAGRAMS_DIR / "DMTRD_diagram_12_edges.svg")
    draw_graph_12_edges(states, transitions, DIAGRAMS_DIR / "DMTRD_diagram_12_edges.png")
    
    draw_graph_24_transitions(states, transitions, DIAGRAMS_DIR / "DMTRD_diagram_24_transitions.svg")
    draw_graph_24_transitions(states, transitions, DIAGRAMS_DIR / "DMTRD_diagram_24_transitions.png")
    
    draw_state_table(states, DIAGRAMS_DIR / "DMTRD_states_table.svg")
    draw_state_table(states, DIAGRAMS_DIR / "DMTRD_states_table.png")
    
    print("\nAll diagrams generated successfully!")

if __name__ == "__main__":
    main()