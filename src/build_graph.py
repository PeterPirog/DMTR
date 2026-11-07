#!/usr/bin/env python3
"""
DMTRD Graph Builder
Generuje pliki GraphML dla yEd Graph Editor:
- DMTRD_12_krawedzi.graphml (12 krawędzi nieskierowanych / 24 przejścia jako właściwości)
- DMTRD_24_przejscia.graphml (24 krawędzie skierowane jako odrębne obiekty)
"""

import csv
import uuid
from pathlib import Path
from lxml import etree

# Namespace GraphML + yFiles extensions
GRAPHML_NS = "http://graphml.graphdrawing.org/xmlns"
Y_NS = "http://www.yworks.com/xml/graphml"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"

NSMAP = {
    None: GRAPHML_NS,
    "y": Y_NS,
    "xsi": XSI_NS
}

ET = etree

# Kolory dla wymiarów
DIM_COLORS = {
    "W": "#E74C3C",  # Czerwony - CHCĘ
    "C": "#2ECC71",  # Zielony - MOGĘ
    "N": "#3498DB",  # Niebieski - POWINIENEM
}

DIM_LABELS = {
    "W": "CHCĘ",
    "C": "MOGĘ",
    "N": "POWINIENEM",
}

# Pozycje węzłów (układ hipersześcianu Q3)
# Używamy współrzędnych 3D rzutowanych na 2D
NODE_POSITIONS = {
    "000": (100, 400),
    "001": (100, 200),
    "010": (300, 400),
    "011": (300, 200),
    "100": (500, 400),
    "101": (500, 200),
    "110": (700, 400),
    "111": (700, 200),
}

def load_states(csv_path):
    """Wczytuje definicje stanów z CSV."""
    states = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            states[row['kod']] = row
    return states

def load_transitions(csv_path):
    """Wczytuje definicje przejść z CSV."""
    transitions = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transitions.append(row)
    return transitions

def create_graphml_root():
    """Tworzy element główny GraphML z definicjami kluczy."""
    root = ET.Element("graphml", nsmap=NSMAP)
    root.set(f"{{{XSI_NS}}}schemaLocation", 
             "http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd")
    
    # Definicje kluczy dla węzłów
    node_keys = [
        ("d0", "label", "string", "node"),
        ("d1", "description", "string", "node"),
        ("d2", "W", "string", "node"),
        ("d3", "C", "string", "node"),
        ("d4", "N", "string", "node"),
        ("d5", "psych_interpretation", "string", "node"),
        ("d6", "consequences", "string", "node"),
        ("d7", "allowed_transitions", "string", "node"),
        ("d8", "name", "string", "node"),
        # yFiles graphics
        ("d9", "graphics", "string", "node"),
    ]
    
    for key_id, attr_name, attr_type, for_type in node_keys:
        key = ET.SubElement(root, "key", id=key_id, **{"for": for_type},
                           attr_name=attr_name, attr_type=attr_type)
        if attr_name == "graphics":
            key.set("yfiles.type", "nodegraphics")
    
    # Definicje kluczy dla krawędzi
    edge_keys = [
        ("e0", "label", "string", "edge"),
        ("e1", "description", "string", "edge"),
        ("e2", "source", "string", "edge"),
        ("e3", "target", "string", "edge"),
        ("e4", "dimension", "string", "edge"),
        ("e5", "direction", "string", "edge"),
        ("e6", "process_name", "string", "edge"),
        ("e7", "psych_interpretation", "string", "edge"),
        ("e8", "mechanisms", "string", "edge"),
        ("e9", "empirical_status", "string", "edge"),
        ("e10", "graphics", "string", "edge"),
    ]
    
    for key_id, attr_name, attr_type, for_type in edge_keys:
        key = ET.SubElement(root, "key", id=key_id, **{"for": for_type},
                           attr_name=attr_name, attr_type=attr_type)
        if attr_name == "graphics":
            key.set("yfiles.type", "edgegraphics")
    
    return root

def create_node_graphics(state_code, x, y, color="#FFFFFF", border_color="#000000"):
    """Tworzy element graficzny yFiles dla węzła."""
    graphics = ET.Element(f"{{{Y_NS}}}ShapeNode")
    
    # Geometry
    geom = ET.SubElement(graphics, f"{{{Y_NS}}}Geometry")
    geom.set("x", str(x))
    geom.set("y", str(y))
    geom.set("width", "120")
    geom.set("height", "80")
    
    # Fill
    fill = ET.SubElement(graphics, f"{{{Y_NS}}}Fill")
    fill.set("color", color)
    fill.set("transparent", "false")
    
    # Border
    border = ET.SubElement(graphics, f"{{{Y_NS}}}BorderStyle")
    border.set("color", border_color)
    border.set("type", "line")
    border.set("width", "2.0")
    
    # Node Label
    node_label = ET.SubElement(graphics, f"{{{Y_NS}}}NodeLabel")
    node_label.set("alignment", "center")
    node_label.set("fontFamily", "Arial")
    node_label.set("fontSize", "14")
    node_label.set("fontStyle", "bold")
    node_label.set("textColor", "#000000")
    node_label.set("modelName", "internal")
    node_label.set("modelPosition", "c")
    node_label.text = state_code
    
    # Shape
    shape = ET.SubElement(graphics, f"{{{Y_NS}}}Shape")
    shape.set("type", "roundrectangle")
    
    return graphics

def create_edge_graphics(color="#000000", width="1.5", directed=True, label_text=""):
    """Tworzy element graficzny yFiles dla krawędzi."""
    graphics = ET.Element(f"{{{Y_NS}}}PolyLineEdge")
    
    # Line style
    line = ET.SubElement(graphics, f"{{{Y_NS}}}LineStyle")
    line.set("color", color)
    line.set("type", "line")
    line.set("width", width)
    
    # Arrows
    if directed:
        arrows = ET.SubElement(graphics, f"{{{Y_NS}}}Arrows")
        arrows.set("source", "none")
        arrows.set("target", "standard")
    
    # Edge label
    if label_text:
        edge_label = ET.SubElement(graphics, f"{{{Y_NS}}}EdgeLabel")
        edge_label.set("alignment", "center")
        edge_label.set("fontFamily", "Arial")
        edge_label.set("fontSize", "10")
        edge_label.set("fontStyle", "plain")
        edge_label.set("textColor", "#000000")
        edge_label.set("modelName", "six_pos")
        edge_label.set("modelPosition", "center")
        edge_label.set("preferredPlacement", "anywhere")
        edge_label.text = label_text
    
    # Bend style
    bend = ET.SubElement(graphics, f"{{{Y_NS}}}BendStyle")
    bend.set("smoothed", "false")
    
    return graphics

def build_12_edges_graphml(states, transitions, output_path):
    """Buduje GraphML z 12 krawędziami nieskierowanych (reprezentującymi pary sąsiedztwa)."""
    root = create_graphml_root()
    graph = ET.SubElement(root, "graph", id="DMTRD_12_edges", edgedefault="undirected")
    
    # Węzły
    for code, state in states.items():
        x, y = NODE_POSITIONS[code]
        node = ET.SubElement(graph, "node", id=code)
        
        # Data elements
        data_map = {
            "d0": code,
            "d1": state['interpretacja_psychologiczna'],
            "d2": state['W'],
            "d3": state['C'],
            "d4": state['N'],
            "d5": state['interpretacja_psychologiczna'],
            "d6": state['korzysci_adaptacyjne'] + "; " + state['koszty_psychologiczne'],
            "d7": state['przejscia_wychodzace'],
            "d8": state['nazwa_naukowa'],
        }
        
        for key_id, value in data_map.items():
            data = ET.SubElement(node, "data", key=key_id)
            data.text = value
        
        # Graphics
        # Kolor węzła zależny od profilu (liczba jedynek)
        ones = int(state['W']) + int(state['C']) + int(state['N'])
        if ones == 0:
            color = "#F5F5F5"  # Szary - 000
        elif ones == 1:
            color = "#FFF3E0"  # Pomarańczowy blady - 1 bit
        elif ones == 2:
            color = "#FFE0B2"  # Pomarańczowy średni - 2 bity
        else:
            color = "#FFCC80"  # Pomarańczowy ciemny - 111
        
        graphics = create_node_graphics(code, x, y, color)
        data_g = ET.SubElement(node, "data", key="d9")
        data_g.append(graphics)
    
    # Krawędzie nieskierowane (12 par sąsiedztwa)
    # Grupujemy przejścia w pary odwrotne
    edge_pairs = {}
    for t in transitions:
        key = tuple(sorted([t['start'], t['end']]))
        if key not in edge_pairs:
            edge_pairs[key] = []
        edge_pairs[key].append(t)
    
    edge_id = 0
    for (src, tgt), pair in edge_pairs.items():
        edge_id += 1
        eid = f"e{edge_id}"
        
        # Określ wymiar (ten sam dla obu kierunków)
        dim = pair[0]['zmieniony_wymiar']
        color = DIM_COLORS[dim]
        
        edge = ET.SubElement(graph, "edge", id=eid, source=src, target=tgt)
        
        # Dane krawędzi
        proc_names = [p['nazwa_procesu'] for p in pair]
        psych_interps = [p['interpretacja_psychologiczna'] for p in pair] if 'interpretacja_psychologiczna' in pair[0] else []
        
        data_map = {
            "e0": f"{src}↔{tgt} ({dim})",
            "e1": f"Przejścia: {'; '.join(proc_names)}",
            "e2": src,
            "e3": tgt,
            "e4": dim,
            "e5": "bidirectional",
            "e6": "; ".join(proc_names),
            "e7": "; ".join(psych_interps) if psych_interps else "",
            "e8": "",
            "e9": pair[0]['status_empiryczny'] if 'status_empiryczny' in pair[0] else "",
        }
        
        for key_id, value in data_map.items():
            data = ET.SubElement(edge, "data", key=key_id)
            data.text = value
        
        # Graphics
        graphics = create_edge_graphics(color=color, width="2.0", directed=False, 
                                        label_text=f"{DIM_LABELS[dim]}")
        data_g = ET.SubElement(edge, "data", key="e10")
        data_g.append(graphics)
    
    # Zapisz
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
    print(f"Zapisano: {output_path} ({len(states)} węzłów, {len(edge_pairs)} krawędzi)")

def build_24_transitions_graphml(states, transitions, output_path):
    """Buduje GraphML z 24 krawędziami skierowanymi (każde przejście osobno)."""
    root = create_graphml_root()
    graph = ET.SubElement(root, "graph", id="DMTRD_24_transitions", edgedefault="directed")
    
    # Węzły (te same co wyżej)
    for code, state in states.items():
        x, y = NODE_POSITIONS[code]
        node = ET.SubElement(graph, "node", id=code)
        
        data_map = {
            "d0": code,
            "d1": state['interpretacja_psychologiczna'],
            "d2": state['W'],
            "d3": state['C'],
            "d4": state['N'],
            "d5": state['interpretacja_psychologiczna'],
            "d6": state['korzysci_adaptacyjne'] + "; " + state['koszty_psychologiczne'],
            "d7": state['przejscia_wychodzace'],
            "d8": state['nazwa_naukowa'],
        }
        
        for key_id, value in data_map.items():
            data = ET.SubElement(node, "data", key=key_id)
            data.text = value
        
        ones = int(state['W']) + int(state['C']) + int(state['N'])
        if ones == 0:
            color = "#F5F5F5"
        elif ones == 1:
            color = "#FFF3E0"
        elif ones == 2:
            color = "#FFE0B2"
        else:
            color = "#FFCC80"
        
        graphics = create_node_graphics(code, x, y, color)
        data_g = ET.SubElement(node, "data", key="d9")
        data_g.append(graphics)
    
    # 24 krawędzie skierowane
    for i, t in enumerate(transitions, 1):
        eid = f"t{i}"
        src = t['start']
        tgt = t['end']
        dim = t['zmieniony_wymiar']
        color = DIM_COLORS[dim]
        
        edge = ET.SubElement(graph, "edge", id=eid, source=src, target=tgt)
        
        data_map = {
            "e0": f"{src}→{tgt} ({dim} {t['kierunek']})",
            "e1": t['definicja_przejscia'],
            "e2": src,
            "e3": tgt,
            "e4": dim,
            "e5": t['kierunek'],
            "e6": t['nazwa_procesu'],
            "e7": t.get('interpretacja_psychologiczna', ''),
            "e8": t.get('mechanizmy_spoleczne', ''),
            "e9": t.get('status_empiryczny', ''),
        }
        
        for key_id, value in data_map.items():
            data = ET.SubElement(edge, "data", key=key_id)
            data.text = value
        
        # Graphics - etykieta z nazwą procesu
        label = f"{DIM_LABELS[dim]}: {t['kierunek']}"
        graphics = create_edge_graphics(color=color, width="1.5", directed=True, label_text=label)
        data_g = ET.SubElement(edge, "data", key="e10")
        data_g.append(graphics)
    
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
    print(f"Zapisano: {output_path} ({len(states)} węzłów, {len(transitions)} krawędzi skierowanych)")

def main():
    base = Path(__file__).parent.parent
    states = load_states(base / "model" / "stany.csv")
    transitions = load_transitions(base / "model" / "przejscia_24.csv")
    
    diagrams_dir = base / "diagrams"
    diagrams_dir.mkdir(exist_ok=True)
    
    build_12_edges_graphml(states, transitions, diagrams_dir / "DMTRD_12_krawedzi.graphml")
    build_24_transitions_graphml(states, transitions, diagrams_dir / "DMTRD_24_przejscia.graphml")
    
    print("\nGenerowanie SVG/PNG wymaga yEd lub ręcznego eksportu.")
    print("Otwórz pliki .graphml w yEd Graph Editor i wyeksportuj jako SVG/PNG.")

if __name__ == "__main__":
    main()