#!/usr/bin/env python3
"""
Generate DMTRD_koncepcja.docx - Main scientific document.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
import csv
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent
MODEL_DIR = BASE / "model"
DIAGRAMS_DIR = BASE / "diagrams"
RESEARCH_DIR = BASE / "research"

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

def load_literature_review():
    with open(RESEARCH_DIR / "przeglad_literatury.md", 'r', encoding='utf-8') as f:
        return f.read()

def load_critical_analysis():
    with open(RESEARCH_DIR / "analiza_krytyczna.md", 'r', encoding='utf-8') as f:
        return f.read()

def add_heading_styled(doc, text, level):
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.color.rgb = RGBColor(0, 51, 102)
    return heading

def add_paragraph_styled(doc, text, style='Normal', bold=False, italic=False, size=11):
    p = doc.add_paragraph(text, style=style)
    for run in p.runs:
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(size)
    return p

def add_table_with_style(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Header
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.bold = True
                run.font.size = Pt(9)
    
    # Data rows
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = table.rows[r + 1].cells[c]
            cell.text = str(val)
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(9)
    
    if col_widths:
        for i, width in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(width)
    
    return table

def main():
    doc = Document()
    
    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    
    # ============================================================
    # 1. STRONA TYTULOWA
    # ============================================================
    for _ in range(4):
        doc.add_paragraph()
    
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("Dynamiczny Model Trójwymiarowej Regulacji Działania (DMTRD)")
    run.bold = True
    run.font.size = Pt(26)
    run.font.color.rgb = RGBColor(0, 51, 102)
    
    doc.add_paragraph()
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Koncepcja naukowa, formalizacja matematyczna i plan walidacji empirycznej\nEtap 1 – Analiza naukowa i przygotowanie dokumentacji do recenzji")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(80, 80, 80)
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = meta.add_run(f"Wersja robocza\n{datetime.now().strftime('%d.%m.%Y')}\nDla niezależnej recenzji naukowej")
    run.font.size = Pt(11)
    run.italic = True
    
    doc.add_page_break()
    
    # ============================================================
    # 2. STRESZCZENIE NAUKOWE
    # ============================================================
    add_heading_styled(doc, "Streszczenie naukowe", 1)
    
    abstract = (
        "Niniejsze opracowanie przedstawia Dynamiczny Model Trójwymiarowej Regulacji Działania (DMTRD) – "
        "propozycję teoretyczną opisującą stan motywacyjny człowieka względem konkretnego działania "
        "za pomocą trzech wymiarów binarnych: W (CHCĘ – osobista akceptacja i motywacja), "
        "C (MOGĘ – subiektywnie oceniana wykonalność) i N (POWINIENEM – poczucie zobowiązania normatywnego). "
        "Osiem możliwych stanów (000–111) tworzą wierzchołki trójwymiarowego hipersześcianu Q3, "
        "a hipoteza przejść elementarnych (HPE) zakłada, że pojedyncza zmiana motywacyjna modyfikuje "
        "dokładnie jeden wymiar (odległość Hamminga = 1). Model generuje 24 kierunkowe przejścia, "
        "którze są interpretowane jako odrębne procesy psychologiczne (np. internalizacja normy, utrata autonomii, "
        "moral distress, rezygnacja z celu). Przeprowadzono analizę porównawną z 10 głównymi teoriami motywacji "
        "(TPB, SDT, COM-B, Rubikon, SCT, Goal-Setting, samoregulacja, nawyki, MOA, modele dynamiczne), "
        "zidentyfikowano kluczowe różnice i podobieństwa, a także sformułowano 24 falsyfikowalne hipotezy badawcze "
        "oraz propozycję metodologii walidacji (EMA, LTA, CTMC). Krytyczna analiza wykazała istotne ograniczenia: "
        "binarność konstruktów, brak jawnej intencji i celu, pomijanie automatyzmu/nawyku, "
        "mieszanie kategorii normatywnych w wymiarze N oraz problemy identyfikowalności modelu. "
        "Mimo ograniczeń, DMTRD wnosi nową treść teoretyczną poprzez: formalną topologię stanów Q3, "
        "hipotezę jednego bitu, jawne modelowanie N jako niezależnego wymiaru, "
        "oraz identyfikację stanu 101 jako formalizacji moral distress."
    )
    add_paragraph_styled(doc, abstract)
    
    # Słowa kluczowe
    add_paragraph_styled(doc, "Słowa kluczowe:", bold=True)
    add_paragraph_styled(doc, "motywacja, samoregulacja, teoria planowanego zachowania, teoria autodeterminacji, "
                        "model COM-B, model Rubikonu, moral distress, modele Markowa, analiza przejść latentnych, "
                        "teoria grafów w psychologii")
    
    # Status epistemiczny
    add_heading_styled(doc, "Status epistemiczny opracowania", 2)
    add_paragraph_styled(doc, 
        "Niniejszy dokument ma charakter koncepcyjny i hipotetyczny. Wszystkie tezy oznaczone jako "
        "\"hipoteza DMTRD\" lub \"postulat DMTRD\" stanowią propozycje teoretyczne wymagające weryfikacji empirycznej. "
        "Przypisania do istniejących teorii opierają się na literaturze do listopada 2026 r. "
        "Nie twierdzi się, że model jest prawdziwy, nowatorski ani lepszy od istniejących teorii. "
        "Celem jest ustalenie spójności logicznej, podstaw literaturowych, falsyfikowalności i wartości heurystycznej.")
    
    doc.add_page_break()
    
    # ============================================================
    # 3. SPIS TREŚCI (zostanie wygenerowany w Word)
    # ============================================================
    add_heading_styled(doc, "Spis treści", 1)
    doc.add_paragraph("Spis treści zostanie wygenerowany automatycznie w Microsoft Word (Odkazy → Spis treści).")
    doc.add_page_break()
    
    # ============================================================
    # 4. WSTĘP
    # ============================================================
    add_heading_styled(doc, "1. Wstęp", 1)
    
    add_paragraph_styled(doc, 
        "Badania nad motywacją ludzkim działaniem mają długą tradycję, jednak większość istniejących teorji "
        "skupia się na predykcji inicjacji zachowania (np. Theory of Planned Behavior), jakości motywacji "
        "(Self-Determination Theory) lub fazach postępowania (Model Rubikonu). Mniej uwagi poświęca się "
        "dynamicznej strukturze stanów motywacyjnych i procesom przejścia między nimi w czasie rzeczywistym. "
        "Dynamiczny Model Trójwymiarowej Regulacji Działania (DMTRD) jest próbą wypełnienia tej luki "
        "poprzez zaproponowanie formalnej topologii stanów motywacyjnych i hipotez o ich dynamice.")
    
    add_paragraph_styled(doc, 
        "Model zakłada, że w dowolnym momencie stan motywacyjny יחס do konkretnego działania można opisać "
        "trzema wymiarami binarnymi: W (CHCĘ – osobista motywacja/akceptacja), C (MOGĘ – postrzegana wykonalność) "
        "i N (POWINIENEM – poczucie zobowiązania normatywnego). Tworzy to 8 stanów (000–111), które ułożone są "
        "w strukturę trójwymiarowego hipersześcianu Q3. Kluczowym postulate jest hipoteza przejść elementarnych: "
        "psychologiczna zmiana stanu następuje przez modyfikację jednego wymiaru (odległość Hamminga = 1).")
    
    add_paragraph_styled(doc, 
        "Opracowanie składa się z trzech głównych części: (1) analiza literatury i porównanie z istniejącymi teoriami, "
        "(2) formalizacja matematyczna (graf Q3, modele Markowa, analiza przejść), "
        "(3) krytyczna ocena, hipotezy badawcze i plan walidacji empirycznej.")
    
    # ============================================================
    # 5. PROBLEM BADAWCZY
    # ============================================================
    add_heading_styled(doc, "2. Problem badawczy", 1)
    
    add_paragraph_styled(doc, 
        "Główny problem badawczy: Czy stan motywacyjny względem konkretnego działania może być adäkwatnie "
        "opisany przez trzy wymiary binarne (W, C, N), a czy dynamika motywacji podlega regule pojedynczej zmiany "
        "wymiaru (hipoteza jednego bitu)?")
    
    add_paragraph_styled(doc, "Szczegółowe pytania badawcze:", bold=True)
    questions = [
        "Q1: Czy trzy wymiary (W, C, N) są psychometrycznie odseparowywalne konstruktami?",
        "Q2: Czy binarna operacjonalizacja nie traci istotnej informacji o natężeniu i jakości motywacji?",
        "Q3: Czy hipoteza jednego bitu (d_H = 1) opisuje elementarne procesy psychologiczne, czy jest artefaktem pomiarowym?",
        "Q4: Czy graf Q3 z 24 przejściami kierunkowymi generuje przewidywania różniące się od modeli konkurencyjnych (TPB, SDT, COM-B)?",
        "Q5: Jakie są koszty psychologiczne i korzyści adaptacyjne poszczególnych stanów i przejść?",
        "Q6: Czy model jest identyfikowalny statystycznie przy danych z pomiarów okresowych (EMA)?",
        "Q7: Czy stan 101 (W=1, C=0, N=1) operacjonalizuje zjawisko moral distress?",
        "Q8: Czy asymetria przejść odwrotnych (np. 011→111 vs 111→011) jest empirycznie potwierdzalna?"
    ]
    for q in questions:
        add_paragraph_styled(doc, q, style='List Bullet')
    
    # ============================================================
    # 6. UZASADNIENIE TRZECH WYMIARÓW
    # ============================================================
    add_heading_styled(doc, "3. Uzasadnienie przyjętych trzech wymiarów", 1)
    
    add_paragraph_styled(doc, 
        "Wybór trzech wymiarów nie jest arbitralny – odpowiada trzem fundamentalnym pytaniom, "
        "które człowiek zadaje sobie przed działaniem (por. Ajzen, 1991; Deci & Ryan, 2000; Michie et al., 2011):")
    
    dims = [
        ("W – CHCĘ (Osobista akceptacja i motywacja)", 
         "Odpowiada na pytanie: \"Czy chcę to zrobić? Czy zgadzam się z tym celem?\". "
         "W odróżnieniu od postawy (TPB) lub typów motywacji (SDT), W jest binarne – wyraża obecność "
         "lub brak osobistej zgody na realizację celu. Nie rozróżnia motywacji intryntycznej od zidentyfikowanej, "
         "co jest uproszczeniem wymagającym weryfikacji."),
        ("C – MOGĘ (Subiektywnie oceniana wykonalność)", 
         "Odpowiada na pytanie: \"Czy jestem w stanie to zrobić? Czy posiadam zasoby i kompetencje?\". "
         "Bliskie pojęciu self-efficacy (Bandura, 1997) i perceived behavioral control (Ajzen, 1991), "
         "ale w przeciwieństwie do nich jest binarne i nie rozdziela zdolności wewnętrznych od szans zewnętrznych "
         "(capability vs opportunity w COM-B)."),
        ("N – POWINIENEM (Poczucie zobowiązania normatywnego)", 
         "Odpowiada na pytanie: \"Czy powinienem to zrobić? Czy czuję się zobowiązany?\". "
         "Jest szersze niż normy subiektywne (TPB) – obejmuje normy moralne (Schwartz, 1977), "
         "obowiązki rolowe (Kahn et al., 1964), zinternalizowane normy (Kelman, 1958) "
         "oraz presję społeczną (Cialdini et al., 1990). To kluczowe rozróżnienie względem TPB i SDT.")
    ]
    
    for title, desc in dims:
        add_paragraph_styled(doc, title, bold=True)
        add_paragraph_styled(doc, desc)
    
    add_paragraph_styled(doc, 
        "Ważne rozróżnienia (co wymiar NIE oznacza):", bold=True)
    exclusions = [
        "W=0 ≠ silna niechęć (to oddzielny konstrukt aversji); W=0 = brak osobistej motywacji.",
        "C=0 ≠ obiektywna niemożność; C=0 = subiektywna ocena niewykonalności (może być błędna).",
        "N=0 ≠ zakaz; N=0 = brak poczucia obowiązku (może być neutralność, nie zabronienie).",
        "Stan (W,C,N) ≠ intencja (TPB) ani działanie; to stan motywacyjny, nie zachowanie.",
        "Stan 111 ≠ zawsze optymalny; N może być eksternalne, W perfekcjonistyczne, C przecenione."
    ]
    for e in exclusions:
        add_paragraph_styled(doc, e, style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 7. DEFINICJE KONSTRUKTÓW
    # ============================================================
    add_heading_styled(doc, "4. Definicje konstruktów", 1)
    
    add_paragraph_styled(doc, 
        "Poniżej przedstawiono definicje operacyjne trzech konstruktów DMTRD, z uwzględnieniem "
        "różnic względem bliższych pojęć z literatury.")
    
    constructs = [
        ("4.1. W – Osobista akceptacja i motywacja (CHCĘ)", 
         "Definicja: Stan wewnętrznej zgody na realizację konkretnego celu lub działania, "
         "objawiający się jako tendencja aproksymacyjna (chęć, pragnienie, zamiar). "
         "W=1 oznacza, że jednostka pozytywnie wertefikuje cel i czuje wewnętrzny napęd do jego realizacji. "
         "W=0 oznacza brak takiej zgody (neutralność, obojętność lub aversja – ale aversja nie jest modelowana).",
         "Różnice: TPB – attitude (ciągła, wielowymiarowa); SDT – autonomous motivation (typy regulacji); "
         "COM-B – reflective motivation (układa się z W) + automatic motivation (nie modelowane w DMTRD)."),
        ("4.2. C – Subiektywnie oceniana wykonalność (MOGĘ)", 
         "Definicja: Przekonanie jednostki o posiadaniu niezbędnych zasobów, kompetencji, czasu "
         "i szans środowiskowych do realizacji działania. C=1 = \"widzę sposób na to, by to zrobić\". "
         "C=0 = \"nie widzę jak to zrobić\" (bariera postrzegana jako nie do przełamania).",
         "Różnice: Bandura – self-efficacy (ciągła, specyficzna dziedzinowo, 4 źródła); "
         "Ajzen – PBC (mieszanka self-efficacy i kontroli środowiskowej); "
         "COM-B – capability (psychologiczna/fizyczna) + opportunity (społeczna/fizyczna) – rozdzielone; "
         "DMTRD scala to w jednym binarnym wymiarze."),
        ("4.3. N – Poczucie zobowiązania normatywnego (POWINIENEM)", 
         "Definicja: Stan doświadczania presji do działania wynikającej z zinternalizowanych lub zewnętrznych norm: "
         "moralnych (Schwartz), rolowych (Kahn), społecznych (Cialdini), prawnych lub organizacyjnych. "
         "N=1 = \"czuję, że to moja odpowiedzialność/obowiązek\". N=0 = brak takiego poczucia.",
         "Różnice: TPB – subjective norms (tylko presja społeczna, ciągła); "
         "SDT – introjected/identified regulation (typy motywacji, nie oddzielny wymiar); "
         "Kelman – compliance/identification/internalization (procesy, nie stan); "
         "Role theory – role expectations (kontekstowe, nie zawsze internalizowane).")
    ]
    
    for title, defn, diff in constructs:
        add_heading_styled(doc, title, 2)
        add_paragraph_styled(doc, defn)
        add_paragraph_styled(doc, "Różnice kluczowe:", bold=True)
        add_paragraph_styled(doc, diff)
    
    # ============================================================
    # 8. GENEZA I ZAŁOŻENIA DMTRD
    # ============================================================
    add_heading_styled(doc, "5. Geneza i podstawowe założenia DMTRD", 1)
    
    add_paragraph_styled(doc, 
        "Model powstał jako synteza trzech nurtów: (1) podejścia trzywymiarowych (MOA, COM-B, TPB), "
        "(2) teorii fazowych (Rubikon, HAPA) i (3) modelowania dynamicznego (systemy dynamiczne, sieci, "
        "modele Markowa). Kluczowe założenia:")
    
    assumptions = [
        ("A1 (Trzy wymiary)", "Stan motywacyjny = (W, C, N) ∈ {0,1}³. 8 stanów."),
        ("A2 (Hipersześcian Q3)", "Graf stanów = Q3. 8 węzłów, 12 krawędzi nieskierowanych, 24 przejścia kierunkowe."),
        ("A3 (Hipoteza jednego bitu – HPE)", "Elementarne przejście zmienia dokładnie 1 bit (d_H = 1). Przejścia wielobitowe = złożone lub artefakt pomiarowy."),
        ("A4 (Asymetria przejść)", "Przejścia odwrotne (np. 011→111 vs 111→011) to odrębne procesy psychologiczne o różnych kosztach/przyczynach."),
        ("A5 (Stan ≠ zachowanie)", "Model opisuje stan motywacyjny, nie deterministycznie zachowanie. Zachowanie zależy od dodatkowych czynników (volicja, kontekst, nawyk)."),
        ("A6 (Dynamiczny charakter)", "Motywacja = proces przechodzenia między stanami w czasie. Czas przebywania, sekwencja i historia mają znaczenie."),
        ("A7 (Falsyfikowalność)", "HPE, asymetria, specyficzne przewidywania dla stanów 101, 011, 110, 111 są testowalne.")
    ]
    
    for name, desc in assumptions:
        add_paragraph_styled(doc, f"{name}: {desc}", style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 9. ANALIZA ISTNIEJĄCYCH TEORII
    # ============================================================
    add_heading_styled(doc, "6. Analiza istniejących teorii motywacji i działania", 1)
    
    add_paragraph_styled(doc, 
        "Przeanalizowano 10 głównych teorii/ramowych podejść. Pełna analiza znajduje się w aneksie "
        "(plik: research/analiza_teorii_pokrewnych.md). Poniżej syntetyczne porównanie.")
    
    # Tabela porównawcza
    headers = ["Teoria", "W (motywacja)", "C (możliwość)", "N (norma)", "Dynamika", "Intencja", "Nawyk", "Główna różnica vs DMTRD"]
    rows = [
        ["TPB (Ajzen)", "Postawa (ciągła)", "PBC (ciągła)", "Normy subiektywne", "Statyczna", "Centralna", "Nie", "Brak topologii stanów, intencja mediuje"],
        ["SDT (Deci, Ryan)", "Typy regulacji (kat.)", "Kompetencja (potrzeba)", "Internalizacja (proces)", "Internalizacja", "Niejawna", "Nie", "Jakość motywacji, nie stan binarny"],
        ["COM-B (Michie et al.)", "Motywacja (2 systemy)", "Capability + Opportunity", "W Opportunity/Motivation", "Pętle zwrotne", "W Motivation", "Tak (automat.)", "Podział na psych/fiz, soc/fiz, ref/aut"],
        ["Rubikon (Heckhausen, Gollwitzer)", "Faza predecyzji", "Wykonalność", "Niejawne", "Fazy sekwencyjne", "Centralna (impl.)", "Nie", "Brak wymiaru N, intencja centralna"],
        ["SCT (Bandura)", "Outcome expectancies + cele", "Self-efficacy (ciągła)", "Niejawne", "Determinizm wzajemny", "Cele", "Nie", "Self-efficacy centralna, brak N"],
        ["Goal-Setting (Locke, Latham)", "Zangażowanie w cel", "Osiągalność", "Niejawne (normy grup.)", "Cykl cel-feedback", "Cel centralny", "Nie", "Cel jako organizator, brak stanów"],
        ["Carver & Scheier", "Cele 'do'", "Oczekiwana skuteczność", "Cele 'be/avoid'", "Cybernetyczna (ciągła)", "Hierarchia celów", "Nie", "Model ciągły, pętla zwrotna"],
        ["Teorie nawyku (Wood)", "Intencja (tylko nowe)", "Łatwość/automatyzacja", "Nieistotne", "Formowanie/łamanie", "Dualne", "Centralne", "System dwuprocesowy, automatyzm"],
        ["MOA (Ölander, Thøgersen)", "Motywacja (złożona)", "Ability + Opportunity", "W Motivation/Opportunity", "Predykcyjna", "W Motivation", "W Opportunity", "Bardzo bliskie DMTRD, zmienne ciągłe"],
        ["Modele dynamiczne (Vallacher, Borsboom)", "Sieci/atrakcje", "Sieci/atrakcje", "Sieci/atrakcje", "Ciągła/chaos", "Rozproszona", "Jako węzeł", "Brak dyskretnych stanów, ciągła dynamika"]
    ]
    add_table_with_style(doc, headers, rows, col_widths=[2.5, 2, 2, 2, 2, 1.5, 1.5, 3.5])
    
    add_paragraph_styled(doc, 
        "Tabela 1. Porównanie kluczowych wymiarów teorii motywacji z DMTRD (opracowanie własne).", 
        italic=True, size=9)
    
    add_heading_styled(doc, "6.1. Podobieństwa i różnice fundamentalne", 2)
    
    add_paragraph_styled(doc, 
        "Główne podobieństwo: Wszystkie teorie uznają, że motywacja, możliwość i norma/presja "
        "są kluczowe dla działania. DMTRD formalizuje to jako 3 bity i 8 stanów.")
    
    add_paragraph_styled(doc, 
        "Główne różnice:", bold=True)
    diffs = [
        "Binarność vs ciągłość: Wszystkie teorie referencyjne używają skal ciągłych lub kategorycznych z >2 poziomami.",
        "Brak intencji: TPB, Rubikon, HAPA, Goal-Setting traktują intencję jako centralną; DMTRD jej nie ma.",
        "Brak celu: Goal-Setting, Rubikon, Carver & Scheier – cel organizuje motywację; DMTRD stan jest bezcelowy.",
        "Brak nawyku/automatyzmu: COM-B, teorie nawyku, dual-process – większość działań automatycznych; DMTRD modeluje tylko procesy refleksywne.",
        "N miesza kategorie: TPB (normy subiektywne), SDT (internalizacja), Role theory (obowiązki rolowe), Moral norm (Schwartz) – DMTRD scala w jeden bit.",
        "C scala capability + opportunity: COM-B rozdziela; DMTRD nie."
    ]
    for d in diffs:
        add_paragraph_styled(doc, d, style='List Bullet')
    
    add_heading_styled(doc, "6.2. Ocena oryginalności propozycji DMTRD", 2)
    
    add_paragraph_styled(doc, 
        "Elementy potencjalnie nowatorskie DMTRD:", bold=True)
    novel = [
        "Formalna topologia stanów Q3 (8 stanów, 24 przejścia) – nie znaleziono w literaturze spójnego modelu z tą strukturą.",
        "Hipoteza jednego bitu (HPE) jako postulat o elementarności zmiany motywacyjnej – konkretna, falsyfikowalna.",
        "Jawne wyodrębnienie N jako niezależnego wymiaru (nie zredukowanego do motywacji ani norm subiektywnych).",
        "Stan 101 (W=1, C=0, N=1) jako formalizacja moral distress i niemożliwych celów z identyfikacją.",
        "Asymetria przejść odwrotnych jako hipoteza o różnych procesach psychologicznych (internalizacja vs utrata autonomii).",
        "Gotowość do modelowania Markowskiego (DTMC, CTMC, LTA) – naturalna struktura danych."
    ]
    for n in novel:
        add_paragraph_styled(doc, n, style='List Bullet')
    
    add_paragraph_styled(doc, 
        "Elementy redukcyjne (znane z literatury):", bold=True)
    reduc = [
        "Trzy filary (W, C, N) ≈ MOA, COM-B, TPB – brak nowości w samym podziale.",
        "Stan 011 ≈ motywacja kontrolowana / introjektowana regulacja (SDT).",
        "Stan 110 ≈ motywacja autonomiczna / zidentyfikowana regulacja (SDT).",
        "Stan 111 ≈ zintegrowana regulacja / wysokie TPB / wysokie COM-B.",
        "Przejścia ≈ zmiany w fazach Rubikonu, internalizacji (SDT), self-efficacy (SCT)."
    ]
    for r in reduc:
        add_paragraph_styled(doc, r, style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 10. FORMALIZACJA MATEMATYCZNA
    # ============================================================
    add_heading_styled(doc, "7. Formalizacja matematyczna", 1)
    
    add_heading_styled(doc, "7.1. Przestrzeń stanów i graf Q3", 2)
    
    add_paragraph_styled(doc, 
        "Niech W, C, N ∈ {0,1}. Przestrzeń stanów: 𝒮 = {0,1}³, |𝒮| = 8. "
        "Stan s = (W, C, N) zapisujemy jako kod binarny WCN (np. 101).")
    
    add_paragraph_styled(doc, 
        "Graf stanów G = (V, E) gdzie V = 𝒮, E = {{sᵢ, sⱼ} : d_H(sᵢ, sⱼ) = 1}. "
        "To trójwymiarowy hipersześcian Q3 o właściwościach:", bold=True)
    
    props = [
        "Węzły: 8 (po 3 sąsiadów każdy)",
        "Krawędzie nieskierowane: 12",
        "Przejścia kierunkowe: 24",
        "Stopień węzła: 3",
        "Średnica: 3",
        "Dwudzielność: tak (partycje: parzyste/nieparzyste liczba jedynek)",
        "Cyklowe: tak (cykle 4, 6, 8)",
        "Spójność: spójny"
    ]
    for p in props:
        add_paragraph_styled(doc, p, style='List Bullet')
    
    add_paragraph_styled(doc, 
        "Macierz sąsiedztwa A (8×8): Aᵢⱼ = 1 jeśli d_H(sᵢ, sⱼ) = 1, wpp. 0. "
        "Macierz incydencji kierunkowej B (24×8) opisuje 24 przejścia.")
    
    add_heading_styled(doc, "7.2. Hipoteza Przejść Elementarnych (HPE)", 2)
    
    add_paragraph_styled(doc, 
        "HPE: Elementarny proces psychologiczny zmiany stanu motywacyjnego modyfikuje dokładnie jeden wymiar. "
        "Formalnie: dopuszczalne przejścia to tylko te o d_H = 1. "
        "Lista 24 przejść (Tabela 2 w aneksie). "
        "Przejścia o d_H ≥ 2 (12 par d_H=2, 4 pary d_H=3) są złożone lub wynikają z ograniczonej rozdzielczości pomiaru.")
    
    add_heading_styled(doc, "7.3. Modele probabilistyczne dynamiki", 2)
    
    add_paragraph_styled(doc, 
        "Zależność od częstotliwości pomiaru: HPE nakładamy na intensywności elementarne, "
        "nie na obserwowane prawdopodobieństwa po czasie Δt.", bold=True)
    
    models = [
        ("DTMC (Dyskretny łańcuch Markowa)", 
         "Macierz przejścia P (8×8): pᵢⱼ > 0 tylko dla d_H ≤ 1. pᵢᵢ = pozostanie w stanie. "
         "24 wolne parametry przejść + 8 samoprzestania (sumy wierszy = 1)."),
        ("CTMC (Łańcuch Markowa w czasie ciągłym)", 
         "Macierz intensywności Q (8×8): qᵢⱼ ≥ 0 dla d_H = 1 (intensywność przejścia), "
         "qᵢⱼ = 0 dla d_H ≥ 2 (HPE na poziomie generatora). "
         "qᵢᵢ = -Σⱼ₌ᵢ qᵢⱼ. P(Δt) = exp(QΔt). "
         "To kluczowe: HPE dotyczy qᵢⱼ, a P(Δt) może mieć pᵢⱼ > 0 dla d_H ≥ 2 przy Δt > 0 "
         "(przejścia wieloetapowe w jednym interwale pomiarowym). Rozwiązuje problem EMA."),
        ("Semi-Markowski (SMM)", 
         "Czas przebywania w stanie ~ dowolny rozkład Fᵢ(t) (nie wykładniczy). "
         "Przydatne gdy stany mają charakterystyczne czasy trwania (np. 111 stabilny dłużej)."),
        ("HMM / LTA (Stanów ukrytych / Analiza przejść latentnych)", 
         "Stany 𝒮 = klasy latentne. Wskaźniki: pomiary W, C, N (binarne/ciągłe). "
         "Problem identyfikowalności: 3 wskaźniki binarne → 8 wzorców = model nasycony (0 df). "
         "Wymaga: wskaźników ciągłych (skale Likert), dodatkowych zmiennych (zachowanie, afekt, kontekst) "
         "lub ograniczeń na macierzach emisji/przejść.")
    ]
    
    for name, desc in models:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, desc)
    
    add_heading_styled(doc, "7.4. Definicje pochodne (do operacjonalizacji)", 2)
    
    derived = [
        ("Intensywność przejścia qᵢⱼ", "Parametr CTMC – siła tendencji do zmiany (nieobserwowana bezpośrednio)."),
        ("Stabilność stanu", "DTMC: pᵢᵢ; CTMC: -qᵢᵢ = Σ qᵢⱼ (całkowita intensywność opuszczania)."),
        ("Czas przebywania (sojourn time)", "CTMC: Exp(-qᵢᵢ); SMM: dowolny Fᵢ(t). Średni czas w stanie i: τᵢ = 1/(-qᵢᵢ)."),
        ("Prawdopodobieństwo osiągnięcia T ⊆ 𝒮", "hᵢ = ℙ(dotrzeć do T | start w sᵢ). Rozwiązuje układ równań liniowych."),
        ("Koszt psychologiczny przejścia", "Konstrukt teoretyczny: cost(i→j) = f(wymiar, kierunek, stan startowy, kontekst). "
         "Np. cost(011→111) < cost(001→101); cost(111→011) > cost(111→110)."),
        ("Trwałość zmiany", "ℙ(nie powrót do i w Δt | i→j). Związane z głębią 'doliny atrakcyjności'."),
        ("Zależność od historii (path dependence)", "Czy pᵢⱼ zależy od ścieżki do i? Model Markowski: nie. "
         "Modele rzędu wyższego / ze zmiennymi latentnymi: tak. "
         "Przykład: 111 osiągnięty przez 000→100→110→111 (budowanie) vs 000→001→011→111 (internalizacja) – różna historia.")
    ]
    
    for name, desc in derived:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, desc)
    
    add_heading_styled(doc, "7.5. Rozszerzenia modelu (do rozważenia)", 2)
    
    extensions = [
        "Zmienne ciągłe W,C,N ∈ [0,1] → stan = punkt w [0,1]³, 8 stanów = oktaanty.",
        "4. wymiar: Intencja (I) → Q₄ (16 stanów). Intencja jako pośrednik W,C,N → zachowanie.",
        "5. wymiar: Działanie (A) ∈ {0,1} – rozdzielenie stanu motywacyjnego od zachowania.",
        "Rozdzielenie C na Capability (wewnętrzne) i Opportunity (zewnętrzne) – jak COM-B.",
        "Rozdzielenie N na: normy społeczne, normy moralne, obowiązki rolowe.",
        "Parametr Nawyk/Automatyzm (H) – modyfikuje przejścia (np. 010→110 trudniejsze przy silnym nawyku).",
        "Kontekst/cele jako zmienne ekzogenne Xₜ wpływające na Q lub P."
    ]
    for e in extensions:
        add_paragraph_styled(doc, e, style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 11. CHARAKTERYSTYKA OŚMIU STANÓW
    # ============================================================
    add_heading_styled(doc, "8. Charakterystyka ośmiu stanów motywacyjnych", 1)
    
    add_paragraph_styled(doc, 
        "Każdy stan opisano według ujednoliconego schematu (kod, nazwa, definicja, interpretacje, "
        "procesy, emocje, zachowanie, mechanizmy, koszty/korzyści, przykłady, przejścia, hipotezy, powiązania, ograniczenia). "
        "Pełne opisy w aneksie (model/stany.csv). Poniżej syntetyczne zestawienie.")
    
    states = load_states()
    
    # Tabela stanów
    headers = ["Kod", "W", "C", "N", "Nazwa naukowa", "Kluczowa interpretacja"]
    rows = []
    for code in sorted(states.keys()):
        s = states[code]
        rows.append([code, s['W'], s['C'], s['N'], s['nazwa_naukowa'], 
                     s['interpretacja_psychologiczna'][:100] + "..."])
    add_table_with_style(doc, headers, rows, col_widths=[1, 0.8, 0.8, 0.8, 4, 8])
    
    add_paragraph_styled(doc, "Tabela 2. Osiem stanów motywacyjnych DMTRD (opracowanie własne).", italic=True, size=9)
    
    # Szczegóły kluczowych stanów
    add_heading_styled(doc, "8.1. Stan 001 – Obowiązek niewykonalny (N=1, W=0, C=0)", 2)
    add_paragraph_styled(doc, 
        "Napięcie między 'powinienem' a 'nie mogę' bez osobistej motywacji. Modeluje sytuacje "
        "przeciążenia roli bez zasobów (Kahn et al., 1964), moral distress w wersji 'bez identyfikacji'. "
        "Główne przejścia: 001→011 (pozyskanie C – empowerment), 001→101 (internalizacja N → W), 001→000 (rezygnacja z N). "
        "Hipoteza: presja do zmiany C lub W lub rezygnacji (N→0). Ryzyko depresji, wypalenia.")
    
    add_heading_styled(doc, "8.2. Stan 011 – Obowiązek wykonalny bez autonomii (W=0, C=1, N=1)", 2)
    add_paragraph_styled(doc, 
        "Compliance bez wewnętrznej zgody. Odpowiada motywacji kontrolowanej (SDT: introjektowana/eksternalna). "
        "Różni się od 111 brakiem autonomii (W=0). Główne przejścia: 011→111 (internalizacja – kluczowe dla jakości działania), "
        "011→001 (utrata C – dezempowerment), 011→010 (utrata N – deregulacja). "
        "Hipoteza: metastabilny – ryzyko wypalenia lub internalizacji.")
    
    add_heading_styled(doc, "8.3. Stan 101 – Motywacja i obowiązek bez możliwości (W=1, C=0, N=1)", 2)
    add_paragraph_styled(doc, 
        "Najbardziej napięty stan. Formalizuje moral distress (Jameton, 1984; Corley et al., 2001) – "
        "wiedza o właściwym działaniu + niemożność wykonania (bariery systemowe). "
        "Również: cel zidentyfikowany jako własny i normatywny, ale niemożliwy do osiągnięcia (Goal-Setting). "
        "Główne przejścia: 101→111 (rozwiązanie konfliktu – najbardziej pożądane), "
        "101→001 (rezygnacja z W – dezengażowanie), 101→100 (rezygnacja z N – sekularyzacja celu). "
        "Hipoteza: 'czasowa bomba' – wymaga szybkiej zmiany C lub rezygnacji.")
    
    add_heading_styled(doc, "8.4. Stan 110 – Działanie autonomiczne (W=1, C=1, N=0)", 2)
    add_paragraph_styled(doc, 
        "Motywacja autonomiczna z poczuciem sprawczości. Bliskie motywacji intryntycznej/zidentyfikowanej (SDT), "
        "wysokiej self-efficacy + outcome expectancy (SCT), Reflective Motivation + Capability (COM-B). "
        "N=0 nie oznacza brak norm – mogą być zinternalizowane (W=1) lub brak kontekstu normatywnego. "
        "Główne przejścia: 110→111 (dodanie N – odpowiedzialność społeczna/OCB), "
        "110→100 (utrata C – blokada), 110→010 (utrata W – wypalenie od pasji). "
        "Hipoteza: stabilny przy autonomii; ryzyko 110→010 przy narzuconych zadaniach.")
    
    add_heading_styled(doc, "8.5. Stan 111 – Zbieżność trzech wymiarów (W=1, C=1, N=1)", 2)
    add_paragraph_styled(doc, 
        "Pełna gotowość motywacyjna. Nie zawsze optymalny! N może być eksternalne (presja), "
        "W perfekcjonistyczne, C przecenione. Przy internalizowanym N: najwyższa jakość motywacji "
        "(zintegrowana regulacja SDT, wysokie TPB/COM-B, faza actional Rubikonu, role integration). "
        "Główne przejścia: 111→011 (utrata W – dezautonomizacja, groźne), "
        "111→101 (utrata C – kryzys zasobów, moral distress ostry), "
        "111→110 (utrata N – delegacja/dezobowiązkowanie, adaptacyjne przy planowanej sukcesji). "
        "Hipoteza: stabilny przy internalizowanym N; 111→011 silniej predykuje wypalenie niż 111→110.")
    
    doc.add_page_break()
    
    # ============================================================
    # 12. GRAF I TOPOLOGIA PRZEJŚĆ
    # ============================================================
    add_heading_styled(doc, "9. Graf stanów i topologia przejść", 1)
    
    add_paragraph_styled(doc, 
        "Graf Q3 (Rysunek 1) przedstawia 8 stanów jako wierzchołki i 12 krawędzi nieskierowanych "
        "jako dopuszczalne relacje sąsiedztwa (odległość Hamminga = 1). Każdy węzeł ma stopień 3. "
        "Graf jest dwudzielny, spójny, średnica 3.")
    
    # Wstaw diagram
    diagram_path = DIAGRAMS_DIR / "DMTRD_diagram.png"
    if diagram_path.exists():
        doc.add_picture(str(diagram_path), width=Inches(6.5))
        add_paragraph_styled(doc, "Rysunek 1. Graf stanów DMTRD – 24 przejścia kierunkowe (kolory: czerwony=W, zielony=C, niebieski=N).", 
                            italic=True, size=9, bold=False)
    
    add_paragraph_styled(doc, 
        "Tabela 3 (w aneksie: model/przejscia_24.csv) zawiera pełną charakterystykę 24 przejść kierunkowych: "
        "stan początkowy/końcowy, zmieniony wymiar, kierunek, nazwa procesu, definicja, przyczyny, "
        "mechanizmy, skutki emocjonalne, wpływ na zachowanie, czynniki sprzyjające/hamujące, "
        "interwencje, przykład, literatura, status empiryczny, hipoteza testowalna.")
    
    # Tabela przejść (skrócona)
    add_heading_styled(doc, "9.1. Zestawienie 24 przejść (skrócone)", 2)
    
    transitions = load_transitions()
    headers = ["ID", "Start→Koniec", "Wymiar", "Kierunek", "Nazwa procesu"]
    rows = []
    for t in transitions:
        rows.append([t['id'], f"{t['start']}→{t['end']}", t['zmieniony_wymiar'], t['kierunek'], t['nazwa_procesu'][:50]])
    add_table_with_style(doc, headers, rows, col_widths=[1, 2, 1.5, 1.5, 9])
    
    add_heading_styled(doc, "9.2. Asymetria przejść odwrotnych – kluczowe przykłady", 2)
    
    asym = [
        ("011 → 111 (Internalizacja)", "Dodanie W do obowiązku wykonalnego. Proces: identyfikacja z wartością zadania, autonomizacja. Koszt: niski (wzrost autonomii).", 
         "111 → 011 (Dezautonomizacja)", "Utrata W przy zachowaniu N i C. Proces: wypalenie, utrata sensu, mikromanagement. Koszt: wysoki (wypalenie, cynizm)."),
        ("001 → 101 (Przejęcie odpowiedzialności)", "Pojawienie się W przy N=1, C=0. Internalizacja normy, szukanie sensu. Koszt: umiarkowany (nadzieja).", 
         "101 → 001 (Dezengażowanie)", "Utrata W przy N=1, C=0. Wypalenie, utrata nadziei. Koszt: wysoki (bezsilność, depresja)."),
        ("101 → 111 (Rozwiązanie konfliktu)", "Pojawienie się C przy W=1, N=1. Przełamanie barier, moral distress resolution. Koszt: niski (olga, sens).", 
         "111 → 101 (Kryzys zasobów)", "Utrata C przy W=1, N=1. Szok, moral distress ostry. Koszt: bardzo wysoki (ryzyko PTSD)."),
        ("110 → 111 (Odpowiedzialność społeczna)", "Dodanie N do autonomii. Internalizacja normy prosocjalnej, OCB. Koszt: niski (dumą, sens).", 
         "111 → 110 (Dezobowiązkowanie)", "Utrata N przy W=1, C=1. Delegacja, sukcesja. Koszt: niski/umiarkowany (ulga, ewentualnie pustka)."),
        ("100 → 110 (Przełamanie barier)", "Pojawienie się C przy W=1. Planowanie, problem-solving, Rubikon. Koszt: umiarkowany (nadzieja).", 
         "110 → 100 (Blokada działania)", "Utrata C przy W=1. Frustracja, bezsilność. Koszt: wysoki (ryzyko rezygnacji).")
    ]
    
    for pair in asym:
        add_paragraph_styled(doc, f"{pair[0]} vs {pair[2]}:", bold=True)
        add_paragraph_styled(doc, f"  {pair[0]}: {pair[1]}")
        add_paragraph_styled(doc, f"  {pair[2]}: {pair[3]}")
    
    doc.add_page_break()
    
    # ============================================================
    # 13. MECHANIZMY DYNAMIKI MOTYWACYJNEJ
    # ============================================================
    add_heading_styled(doc, "10. Mechanizmy dynamiki motywacyjnej", 1)
    
    add_heading_styled(doc, "10.1. Procesy wewnątrzwymiarowe", 2)
    
    add_paragraph_styled(doc, 
        "Każdy wymiar ma własne mechanizmy zmiany 0↔1:", bold=True)
    
    mech = [
        ("W (CHCĘ): 0→1", "Pojawienie się motywacji: zmiana wartości celu, insight, modelowanie, perswazja, framing. "
         "1→0: Utrata motywacji: rozczarowanie, wypalenie, depresja, zmiana priorytetów, presja do rezygnacji."),
        ("C (MOGĘ): 0→1", "Pozyskanie możliwości: mastery experience (Bandura), szkolenie, delegacja, networking, innowacja, uproszczenie procedur. "
         "1→0: Utrata możliwości: utrata zasobów, awaria, zmiana regulacji, lęk, degradacja kompetencji."),
        ("N (POWINIENEM): 0→1", "Pojawienie się obowiązku: nowa rola, internalizacja normy (Kelman), aktywacja normy moralnej (Schwartz), presja społeczna. "
         "1→0: Utrata obowiązku: odrzucenie roli, deprecjacja normy, zmiana wartości, deregulacja, sekularyzacja.")
    ]
    
    for name, desc in mech:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, desc)
    
    add_heading_styled(doc, "10.2. Procesy międzywymiarowe (interakcje)", 2)
    
    add_paragraph_styled(doc, 
        "Zmiana jednego wymiaru modyfikuje kontekst dla pozostałych:", bold=True)
    
    inter = [
        "N=1 ułatwia W=0→1 (internalizacja normy → autonomia) – przejścia 001→101, 011→111.",
        "W=1 ułatwia C=0→1 (motywacja → problem-solving, szukanie dróg) – przejścia 100→110, 101→111.",
        "C=1 ułatwia W=0→1 (możliwość → aktywacja, 'mogę więc chcę spróbować') – przejścia 010→110, 011→111.",
        "C=0 utrudnia W=1 (frustracja celowa, ryzyko 100→000, 101→001).",
        "N=0 przy W=1, C=1 (stan 110) = autonomia bez presji – ryzyko 110→010 (wypalenie od braku sensu).",
        "W=0 przy N=1, C=1 (stan 011) = compliance – ryzyko 011→001 (wypalenie) lub 011→111 (internalizacja)."
    ]
    for i in inter:
        add_paragraph_styled(doc, i, style='List Bullet')
    
    add_heading_styled(doc, "10.3. Rola afektu w przejściach", 2)
    
    add_paragraph_styled(doc, 
        "Afekt jako sygnał i konsekwencja przejść (por. Carver & Scheier, 1998):", bold=True)
    
    affect = [
        "Pozytywny afekt (radość, nadzieja, olga, dumą): towarzyszy przejściom 'w górę' (0→1) przy W i C, "
        "oraz internalizacji N (011→111, 110→111). Wzmocni tendencję do utrzymania nowego stanu.",
        "Negatywny afekt (lęk, winę, frustracja, bezsilność, gniew, cynizm): towarzyszy przejściom 'w dół' (1→0), "
        "utracie możliwości (111→101, 110→100), moral distress (101), wypaleniu (110→010, 111→011). "
        "Może inicjować coping (problem-focused → 101→111) lub rezygnację (101→001).",
        "Afekt misto (ulga z winą: 011→010, 101→100; nadzieja z lękiem: 100→110, 001→101) – sygnalizuje ambiwalencję procesu."
    ]
    for a in affect:
        add_paragraph_styled(doc, a, style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 14. ZWIĄZEK STANÓW Z DZIAŁANIEM
    # ============================================================
    add_heading_styled(doc, "11. Związek stanów z podejmowaniem, kontynuowaniem i zaniechaniem działania", 1)
    
    add_paragraph_styled(doc, 
        "DMTRD opisuje stan motywacyjny, nie deterministycznie zachowanie. Związek ze zachowaniem jest prawdopodobieństwowy "
        "i zmodulowany przez volicję (Kuhl), kontekst, nawyki i zasoby.", bold=True)
    
    action = [
        ("Podejmowanie działania (inicjacja)", 
         "Najbardziej prawdopodobne ze stanów: 110 (autonomia + możliwość), 111 (pełna gotowość), 101 (motywacja + norma, szukanie C). "
         "Stan 100 (tylko W) → planowanie (przejscia 100→110). Stan 011 (compliance) → działanie bez zaangażowania. "
         "Stan 001, 010, 000 → działanie mało prawdopodobne bez zmiany stanu."),
        ("Kontynuowanie działania (persistencja)", 
         "Stan 111 (internalizowane N) > 110 (autonomia) > 011 (compliance) > 101 (blokada). "
         "Volicja (Kuhl) chroni działanie w 110/111. W 011 kontynuacja zależy od sankcji/norm. "
         "W 101 kontynuacja niemożliwa bez C – próby copingowe (101→111) lub rezygnacja."),
        ("Zaniechanie / rezygnacja (disengagement)", 
         "Przejścia do stanów z W=0: 111→011, 110→010, 101→001, 100→000. "
         "Adaptacyjne (Wrosch et al.): rezygnacja z niemożliwego celu (101→001/100) → reengagement. "
         "Niezadaptacyjne: wypalenie (110→010, 111→011), dezengażowanie przy zachowaniu N (101→001) → moral residue.")
    ]
    
    for name, desc in action:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, desc)
    
    add_heading_styled(doc, "11.1. Rola nawyków (System 1) – luka modelu", 2)
    
    add_paragraph_styled(doc, 
        "DMTRD modeluje procesy refleksywne (System 2). Dla działań nawykowych (System 1; Wood & Neal, 2007):", bold=True)
    
    habit = [
        "Stan 010/011 (C=1, W=0) to normalny stan działania nawykowego – NIE 'brak motywacji'.",
        "Przejście 010→110 = świadome przejęcie kontroli nad nawykem (kontrola wykonywcza).",
        "Przejście 110→010 = automatyzacja / utrata świadomej kontroli (może być adaptacyjne).",
        "Silny nawyk hamuje 010→110 (trudność przejęcia kontroli) i ułatwia 110→010.",
        "DMTRD wymaga rozszerzenia o parametr H (siła nawyku) modyfikującego przejścia."
    ]
    for h in habit:
        add_paragraph_styled(doc, h, style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 15. ZALEŻNOŚĆ OD ŚCIEŻKI I HISTORII
    # ============================================================
    add_heading_styled(doc, "12. Zależność od ścieżki i historii procesu (Path Dependence)", 1)
    
    add_paragraph_styled(doc, 
        "Model Markowski (bezpamięciowy) zakłada, że przyszłość zależy tylko od bieżącego stanu. "
        "Psychologicznie nieuzasadnione – historia ma znaczenie:", bold=True)
    
    path = [
        "Różne ścieżki do 111: 000→100→110→111 (budowanie autonomii) vs 000→001→011→111 (internalizacja normy). "
        "Czy stabilność 111 zależy od ścieżki? Hipoteza DMTRD: tak – internalizowana N (ścieżka B) daje wyższą stabilność.",
        "Stan 101 osiągnięty z 001 (internalizacja) vs z 100 (moralizacja celu) – różna prognaza.",
        "Liczba poprzednich cykli (np. wielokrotne 110→010→110) może budować odporność lub wrażliwość (sensytyzacja).",
        "Modelowanie: łańcuch Markowa rzędu wyższego, semi-Markowski ze zmiennymi latentnymi historii, "
        "lub CTMC z kowariancjami zależnymi od czasu/ścieżki."
    ]
    for p in path:
        add_paragraph_styled(doc, p, style='List Bullet')
    
    # ============================================================
    # 16. HIPOTEZY BADAWCZE
    # ============================================================
    add_heading_styled(doc, "13. Hipotezy badawcze DMTRD", 1)
    
    add_paragraph_styled(doc, 
        "Poniżej 24 hipotezy (H1–H24) odpowiadających 24 przejściom, plus hipotezy ogólne (HG1–HG5). "
        "Pełna specyfikacja (zmienne, pomiar, analiza, czynniki zakłócające) w aneksie (research/hipotezy_badawcze.md).")
    
    # Tabela hipotez (skrócona)
    headers = ["Nr", "Przejście", "Hipoteza (skrót)"]
    rows = []
    hypotheses = [
        ("H1", "000→100", "Wzrost outcome expectancies i self-efficacy przewiduje 000→100 (regresja logistyczna EMA)"),
        ("H2", "100→000", "Niska self-efficacy i negatywne outcome expectancies przewidują rezygnację (analiza przeżycia)"),
        ("H3", "001→101", "Perceived autonomy support mediuje internalizację obowiązku (mediacja panelowa)"),
        ("H4", "101→001/011", "Brak perceived control → 001; silne normy społeczne → 011 (multinomial logit)"),
        ("H5", "010→110", "Motywacja intryntyczna i autonomy support przewidują aktywację potencjału (SEM)"),
        ("H6", "110→010", "Niskie autonomy support przewiduje utratę autonomicznej motywacji (Cox regression)"),
        ("H7", "011→111", "Perceived autonomy support i identified regulation mediują internalizację (mediacja longitudinalna)"),
        ("H8", "111→011", "111→011 silniej predykuje wypalenie niż 111→110 (analiza ryzyka proporcjonalnego)"),
        ("H9", "000→010", "Mastery experience przewiduje pozyskanie możliwości (analiza sekwencji EMA)"),
        ("H10", "010→000", "Utrata C bez W/N mniej stresogenna niż 110→100 lub 111→101 (porównanie afektu EMA)"),
        ("H11", "001→011", "Perceived organizational support przewiduje empowerment w roli (cross-lagged panel)"),
        ("H12", "011→001", "011→001 silniej predykuje intencję odejścia niż 011→010 (regresja logistyczna)"),
        ("H13", "100→110", "Implementation intentions mediują przełamanie barier (mediacja Gollwitzer)"),
        ("H14", "110→100", "110→100 częściej prowadzi do persistencji (100→110) niż rezygnacji (sekwencje stanów)"),
        ("H15", "101→111", "Problem-focused coping i social support przewidują rozwiązanie konfliktu (SEM)"),
        ("H16", "111→101", "111→101 silniej predykuje ostre stresowe reakcje niż inne utraty C (porównanie wskaźników stresu)"),
        ("H17", "000→001", "Internalizacja (→101) vs compliance (→011) rozróżnialne przez autonomy support (interakcja)"),
        ("H18", "001→000", "Role ambiguity i niskie role commitment przewidują odrzucenie roli (Cox model)"),
        ("H19", "010→011", "Niskie autonomy support przy 010→011 przewiduje 011→001, nie 011→111 (sekwencje)"),
        ("H20", "011→010/001", "Wysoka autonomia → 010; niska → 001 (moderacja autonomy)"),
        ("H21", "100→101", "Personal norm (Schwartz) → 101→111; subjective norms (TPB) → 101→001 (moderacja)"),
        ("H22", "101→100", "Wysoka identyfikacja z celem (W) przy 101→100 zapobiega 100→000 (interakcja W×N)"),
        ("H23", "110→111", "Organizational identification i prosocial motivation przewidują OCB (SEM)"),
        ("H24", "111→110", "Planowana sukcesja przy 111→110 nie predykuje wypalenia; 111→011 tak (porównanie trajektorii)")
    ]
    
    for h in hypotheses:
        rows.append(list(h))
    add_table_with_style(doc, headers, rows, col_widths=[1, 2, 13])
    
    add_paragraph_styled(doc, "Tabela 4. Hipotezy badawcze DMTRD (H1–H24) – skrócone.", italic=True, size=9)
    
    add_heading_styled(doc, "13.1. Hipotezy ogólne (HG)", 2)
    
    hg = [
        "HG1: Model 8-stanowy DMTRD lepiej dopasowuje dane EMA niż modele bez stanów (np. TPB, SDT) – test: porównanie AIC/BIC w LTA.",
        "HG2: Hipoteza jednego bitu (d_H=1) jest empirycznie poparta – większość obserwowanych zmian w EMA to d_H=1; d_H≥2 są rzadkie lub wyjaśniane przez odstępy pomiarowe – test: analiza sekwencji.",
        "HG3: Asymetria przejść odwrotnych jest istotna statystycznie – qᵢⱼ ≠ qⱼᵢ dla co najmniej 50% par – test: test likelihodu w CTMC.",
        "HG4: Stan 101 operacjonalizuje moral distress – silna korelacja z istniejącymi skalami (MDS, Corley) i predykcja wypalenia/odejścia – test: walidacja kryterialna.",
        "HG5: Topologia Q3 ma wartość heurystyczną – generuje przewidywania niedostępne w modelach płaskich (np. specyficzność 101, asymetria 111→011 vs 111→110) – test: porównanie mocy predykcyjnej."
    ]
    for h in hg:
        add_paragraph_styled(doc, h, style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 17. PROPOZYCJA METODOLOGII WALIDACJI
    # ============================================================
    add_heading_styled(doc, "14. Propozycja metodologii walidacji empirycznej", 1)
    
    add_heading_styled(doc, "14.1. Operacjonalizacja W, C, N", 2)
    
    add_paragraph_styled(doc, 
        "Binarna operacjonalizacja (tak/nie) ma ograniczenia. Zalecane podejście hybrydowe:", bold=True)
    
    oper = [
        "Wersja binarna (dla LTA/Markov): 3 itemy tak/nie na każdy wymiar (np. 'Czy chcę to zrobić? Tak/Nie'). "
        "Problem: model nasycony (3 wskaźniki → 8 stanów = 0 df).",
        "Wersja ciągła (dla SEM/regresji): Skale Likert 1–7 dla każdego wymiaru (np. W: 'W jakim stopniu osobiście chcę to zrobić?'). "
        "Stan = oktaant w [1,7]³ (próg np. 4). Umożliwia testowanie HPE na poziomie ciągłym (przecinanie płaszczyzn).",
        "Istniejące skale do adaptacji:"
    ]
    for o in oper:
        add_paragraph_styled(doc, o, style='List Bullet')
    
    add_paragraph_styled(doc, "Istniejące skale do adaptacji:", bold=True)
    
    scales = [
        "W: Intrinsic Motivation Inventory (IMI) – Interest/Enjoyment; Identified Regulation (SDT); Attitude (TPB).",
        "C: General Self-Efficacy Scale (Schwarzer & Jerusalem); Perceived Behavioral Control (TPB); Capability items (TDF/COM-B).",
        "N: Moral Obligation Scale (Ajzen); Personal Norm (Schwartz); Role Overload/Conflict (Kahn); Internalization (Kelman)."
    ]
    for s in scales:
        add_paragraph_styled(doc, s, style='List Bullet 2')
    
    add_heading_styled(doc, "14.2. Projekt badania pilotażowego (EMA)", 2)
    
    pilot = [
        ("Cel", "Test HPE, asymetrii, stabilności stanów, przewidywania H1–H24."),
        ("Populacja", "Dorosli pracownicy (N=100–150) lub studenci (N=200) wykonujący konkretne, powtarzalne działanie (np. ćwiczenia, nauka, zadanie zawodowe)."),
        ("Kryteria doboru", "Wiek 18–65, zgoda na EMA, posiadanie smartfona, wykonywanie badanego działania min. 3×/tydzień."),
        ("Badanego działanie", "Np. regularna aktywność fizyczna, nauka języka, zadanie projektowe w pracy – zdefiniowane wspólnie z uczestnikiem."),
        ("Pomiar W, C, N", "3 itemy na wymiar (Likert 1–7) + 1 item binarny (tak/nie) – 12 itemów razem. "
         "Losowa kolejność. Czas wypełnienia < 30 sekund."),
        ("Pomiar zachowania", "Samoraport: 'Czy wykonałeś działanie od ostatniego pomiaru?' (tak/nie) + czas trwania/intensywność. "
         "Opcjonalnie: akcelerometr (dla aktywności fizycznej), logi aplikacji (dla nauki)."),
        ("Pomiary wielokrotne", "EMA: 5–8 pomiarów/dobę przez 14–21 dni (losowe + event-based po działaniu). "
         "Łącznie ~100–150 pomiarów/osoba."),
        ("Częstotliwość", "Losowe: 5×/dzień (9:00–21:00). Event-based: do 1h po działaniu. "
         "Rozdzielczość czasowa ~2–3h – kluczowe dla HPE (d_H=1 w interwale)."),
        ("Analiza statystyczna", "1. LTA (Mplus/R): 8 klas, wskaźniki ciągłe, macierz przejść P. Test HPE: pᵢⱼ=0 dla d_H≥2. "
         "2. CTMC (msm/ctmcm): estymacja Q z danych panelowych. Test asymetrii: qᵢⱼ ≠ qⱼᵢ. "
         "3. Regresje logistyczne wielopoziomowe: przewidywanie przejść (H1–H24). "
         "4. SEM (lavaan): mediacje (np. H3, H7, H13, H15)."),
        ("Walidacja trafności konstruktu", "CFA: 3 czynniki (W,C,N) – dopasowanie (CFI>0.95, RMSEA<0.06). "
         "Dyskryminacyjna: AVE > kwadrat korelacji między czynnikami. "
         "Kryterialna: korelacje ze skalami referencyjnymi (IMI, GSE, MDS)."),
        ("Walidacja trafności predykcyjnej", "Przewidywanie zachowania (następny pomiar) ze stanu (bieżący pomiar). "
         "Porównanie z TPB, SDT, COM-B (regresje zagnieżdżone)."),
        ("Porównanie z modelami konkurencyjnymi", "TPB (intencja → zachowanie), SDT (typy regulacji), COM-B (M,O,A), "
         "Model Rubikon (fazy), Model ciągły (Carver & Scheier). Kryteria: AIC, BIC, R², moc predykcyjna out-of-sample."),
        ("Analiza mocy", "Symulacja Monte Carlo (N=100, T=100, efekty małe/średnie) do wyznaczenia mocy dla: "
         "testu HPE (d_H≥2), asymetrii (qᵢⱼ≠qⱼᵢ), mediacji (H3, H7). Plan: 1000 replikacji."),
        ("Ograniczenia", "Selekcja próby (motywowani do udziału), reaktywność pomiaru (EMA zmienia stan), "
         "brak kontroli eksperymentalnej, ograniczone uogólnienie na inne działania/kultury."),
        ("Etyka i dane", "Zgoda KE, anonimizacja, prawo do wycofania, przechowywanie na serwerze UE (GDPR), "
         "brak danych wrażliwych, debriefing.")
    ]
    
    for name, desc in pilot:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, desc)
    
    doc.add_page_break()
    
    # ============================================================
    # 18. KRYTYCZNA OCENA TEORII
    # ============================================================
    add_heading_styled(doc, "15. Krytyczna ocena teorii DMTRD", 1)
    
    add_paragraph_styled(doc, 
        "Poniżej 20 kluczowych pytań krytycznych (zgodnie z zadaniem) z analizą problemu, "
        "znaczenia, konsekwencji, ewentualnej poprawki i wpływu na prostotę/oryginalność. "
        "Pełna analiza w aneksie (research/analiza_krytyczna.md).")
    
    # 5 najpoważniejszych argumentów
    add_heading_styled(doc, "15.1. Pięć najpoważniejszych argumentów przeciwko DMTRD", 2)
    
    critical = [
        ("ARG1: Binarność traci istotną wariancję", 
         "Problem: Wszystkie teorie referencyjne (TPB, SDT, SCT, Goal-Setting, COM-B) używają skal ciągłych. "
         "Binarne W traci typy motywacji (intryntyczna vs zidentyfikowana vs introjektowana); "
         "binarne C traci gradację self-efficacy; binarne N traci kategorie norm (moralne, rolowe, społeczne).",
         "Znaczenie: Redukcja siły wyjaśniającej, niemożność przewidywania natężenia zachowania/trwałości.",
         "Konsekwencje: Model może nie wyjaśniać wariancji, którą wyjaśniają modele ciągłe.",
         "Poprawka: Zmienne ciągłe W,C,N ∈ [0,1] lub Likert 1–7; stany = oktaanty. ",
         "Wpływ: utrata prostej topologii Q3, trudniejsza interpretacja, ale większa wierność psychologiczna."),
        ("ARG2: Brak intencji i celu – luka teoretyczna", 
         "Problem: TPB, Rubikon, HAPA, Goal-Setting, Carver & Scheier – intencja/cel centralne. "
         "DMTRD: stan (W,C,N) bez intencji ani celu. Stan 111 może oznaczać gotowość (preactional) lub działanie (actional).",
         "Znaczenie: Brak mechanizmu łączącego stan z działaniem; niejasność: czy 111 = intencja czy volicja?",
         "Konsekwencje: Trudność w przewidywaniu zachowania; niejasne rozróżnienie motywacji vs volicji.",
         "Poprawka: Dodać 4. wymiar I (Intencja) → Q₄ (16 stanów) lub modelować I jako funkcję (W,C,N). ",
         "Wpływ: podwojenie stanów, większa złożoność, ale zamknięcie luki teoretycznej."),
        ("ARG3: Pomijanie automatyzmu/nawyku – większość działań", 
         "Problem: Wood & Neal (2007) – 40–50% codziennych działań nawykowych (System 1). "
         "DMTRD: stan 010/011 interpretowany jako 'brak motywacji', a to normalny stan działania nawykowego. "
         "Przejścia 010↔110 nie oddają dynamiki nawyków (formowanie/łamanie).",
         "Znaczenie: Model nie dotyczy większości zachowań codziennych; ryzyko fałszywych wniosków.",
         "Konsekwencje: Niska walidacja ekologiczna; trudność w zastosowaniu do interwencji nawykowych.",
         "Poprawka: Dodać parametr H (siła nawyku) modyfikujący przejścia; rozdzielić System 1/2. ",
         "Wpływ: significantne ułożenie modelu, nowy wymiar złożoności."),
        ("ARG4: N miesza kategorie normatywnych – konstrukt niejednolity", 
         "Problem: N łączy normy opisowe (Cialdini), inskryptywne (Cialdini), moralne (Schwartz), "
         "rolowe (Kahn), zinternalizowane (Kelman), eksternalne (TPB). To różne psychologiczne mechanizmy "
         "z różnymi konsekwencjami (compliance vs internalizacja vs identyfikacja).",
         "Znaczenie: Stan 011 może być compliance (eksternalne N) lub introjektowana regulacja (wewnętrzne N) – "
         "DMTRD nie rozróżnia. Stan 111 z N eksternalnym ≠ 111 z N zinternalizowanym.",
         "Konsekwencje: Nieprecyzyjne przewidywania; utrata zdolności do rozróżnienia jakości zaangażowania.",
         "Poprawka: Rozdzielić N na: N_soc (normy społeczne), N_mor (normy moralne), N_rol (obowiązki rolowe). ",
         "Wpływ: 3 bity zamiast 1 → 5 wymiarów (32 stany) lub hierarchiczny model N."),
        ("ARG5: Identyfikowalność modelu – problem statystyczny", 
         "Problem: 3 wskaźniki binarne → 8 wzorców odpowiedzi = 8 klas latentnych = model nasycony (0 df). "
         "Nie da się testować dopasowania LTA/HMM bez dodatkowych założeń. "
         "CTMC wymaga wysokiej częstotliwości pomiarów (EMA), co jest kosztowne i reaktywne.",
         "Znaczenie: Trudność w empirycznej weryfikacji; ryzyko overfittingu; ograniczone wnioskowanie.",
         "Konsekwencje: Model może pozostać nienawiązany empirycznie przez długi czas.",
         "Poprawka: Wymagać wskaźników ciągłych (Likert) + dodatkowych zmiennych (zachowanie, afekt, kontekst) "
         "lub silnych ograniczeń (np. równość qᵢⱼ w grupach). ",
         "Wpływ: większe wymagania pomiarowe, ale identyfikowalność.")
    ]
    
    for name, prob, signif, conseq, fix, impact in critical:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, f"Problem: {prob}")
        add_paragraph_styled(doc, f"Znaczenie naukowe: {signif}")
        add_paragraph_styled(doc, f"Możliwe konsekwencje: {conseq}")
        add_paragraph_styled(doc, f"Ewentualna poprawka: {fix}")
        add_paragraph_styled(doc, f"Wpływ na prostotę/oryginalność: {impact}")
        doc.add_paragraph()
    
    add_heading_styled(doc, "15.2. Tabela 20 pytań krytycznych (skrócona)", 2)
    
    # Skrócona tabela
    headers = ["Nr", "Pytanie", "Ocena ryzyka", "Wymagana akcja"]
    critical_short = [
        ["1", "Czy W,C,N są niezależne konstrukty?", "Wysokie", "CFA, analiza dyskryminacyjna"],
        ["2", "Czy binarność nadmiernie upraszcza?", "Krytyczne", "Wersja ciągła, test utraty informacji"],
        ["3", "Czy 1 bit = elementarny proces?", "Wysokie", "Test HPE w EMA (d_H≥2)"],
        ["4", "Czy możliwe równoczesne zmiany?", "Średnie", "Analiza sekwencji, CTMC z qᵢⱼ dla d_H≥2"],
        ["5", "Czy model > klasycznych modeli?", "Nieznane", "Porównanie AIC/BIC, predykcja out-of-sample"],
        ["6", "Czy N nie łączy zbyt wielu kategorii?", "Krytyczne", "Rozdzielenie N na podwymiary"],
        ["7", "Czy C nie miesza self-efficacy z Opportunity?", "Wysokie", "Rozdzielenie C na Capability/Opportunity"],
        ["8", "Czy W = przyjemność/preferencja/intencja/autonomia?", "Wysokie", "Precyzyjna definicja, CFA z IMI/SDT"],
        ["9", "Czy model uwzględnia ambiwalencję?", "Średnie", "Dodać wymiar ambiwalencji lub wersję ciągłą"],
        ["10", "Czy wyjaśnia działanie bez świadomej W?", "Wysokie", "Dodać System 1 / parametr H (nawyk)"],
        ["11", "Czy wrażliwy na kontekst/kulturę?", "Średnie", "Badania cross-cultural, multiniveau"],
        ["12", "Czy historia zmienia dynamikę?", "Wysokie", "Modele z path dependence (rząd wyższego)"],
        ["13", "Czy założenia są falsyfikowalne?", "Tak", "H1–H24, HG1–HG5 – specyfikacja gotowa"],
        ["14", "Czy model identyfikowalny statystycznie?", "Krytyczne", "Wskaźniki ciągłe + dodatkowe zmienne"],
        ["15", "Czy prognostyczne dla zachowania?", "Nieznane", "Walidacja predykcyjna EMA vs TPB/SDT/COM-B"],
        ["16", "Czy ryzyko tautologii (stan=zachowanie)?", "Średnie", "Rozdzielenie stanu od zachowania (wymiar A)"],
        ["17", "Czy wymaga wymiaru Działania (A)?", "Wysokie", "Dodać A ∈ {0,1} → 16 stanów"],
        ["18", "Czy 8 stanów = najlepsza reprezentacja?", "Średnie", "Test wersji ciągłej (oktaanty) vs dyskretnej"],
        ["19", "Gdzie model wprowadza w błąd?", "Wysokie", "Mapowanie granic zastosowania (nawyki, ambiwalencja, kliniczne)"],
        ["20", "Czy DMTRD wnosi nową treść?", "Częściowo", "Q3, HPE, N niezależny, stan 101 – tak; 3 filary – nie"]
    ]
    
    for row in critical_short:
        rows.append(row)
    add_table_with_style(doc, headers, rows, col_widths=[0.8, 6, 2, 6])
    
    doc.add_page_break()
    
    # ============================================================
    # 19. OGRANICZENIA
    # ============================================================
    add_heading_styled(doc, "16. Ograniczenia modelu DMTRD", 1)
    
    limits = [
        "Teoretyczne: binarność, brak intencji/celu, brak nawyku/automatyzmu, mieszanie kategorii w N, "
        "skalowanie C (capability+opportunity), brak ambiwalencji, brak kontekstu kulturowego.",
        "Metodologiczne: identyfikowalność (3 wskaźniki binarne → saturated model), "
        "wymóg EMA (wysoka częstotliwość, reaktywność), brak danych longitudinalnych do kalibracji Q/ P.",
        "Zastosowawcze: model opisowy (nie interwencyjny jak BCW), trudny do zastosowania w praktyce bez narzędzi pomiarowych, "
        "ograniczone do działań refleksywnych (System 2), nie uwzględnia patologii klinicznych (np. depresja, OCD).",
        "Epistemologiczne: HPE to hipoteza, nie fakt; asymetria przejść to postulat; "
        "stan 111 nie zawsze optymalny; model nie roszczy się o uniwersalność."
    ]
    for l in limits:
        add_paragraph_styled(doc, l, style='List Bullet')
    
    # ============================================================
    # 20. MOŻLIWE ZASTOSOWANIA
    # ============================================================
    add_heading_styled(doc, "17. Możliwe zastosowania", 1)
    
    apps = [
        ("Psychologia zdrowia / medycyna", "Stan 101 = moral distress personelu medycznego; przewidywanie wypalenia, odejścia z pracy; "
         "interwencje: 101→111 (systemowe zmiany), 111→110 (delegacja/sukcesja)."),
        ("Zarządzanie i HR", "Diagnoza stanów motywacyjnych zespołów: 011 (compliance) vs 110 (autonomia) vs 111 (zaangażowanie). "
         "Job crafting: 010→110 (aktywacja), 100→110 (przełamanie barier). "
         "Sukcesja: 111→110 (planowane dezobowiązkowanie)."),
        ("Edukacja", "Stan 011 (uczenie się 'bo trzeba') vs 110 (pasja) vs 111 (zidentyfikowana regulacja). "
         "Internalizacja: 011→111 (wsparcie autonomii). Rezygnacja: 101→001 (moral distress studentów)."),
        ("Psychologia społeczna / polityczna", "Aktywizm: 100 (ideał bez możliwości) → 110 (mobilizacja) → 111 (instytucjonalizacja). "
         "Radikalizacja: 001→101 (internalizacja normy ekstremistycznej). "
         "Demobilizacja: 111→011 (wypalenie aktywistów)."),
        ("Badania nad nawykami / interwencjami", "Rozszerzenie o parametr H: modelowanie formowania/łamania nawyku. "
         "010 (nawyk) → 110 (świadoma kontrola) → 010 (automatyzacja nowego zachowania)."),
        ("Modelowanie symulacyjne / AI", "Agent-based modeling: agenci w stanach Q3, przejścia probabilistyczne. "
         "Symulacja dyfuzji innowacji, zmian norm, wypalenia w organizacjach.")
    ]
    
    for name, desc in apps:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, desc)
    
    doc.add_page_break()
    
    # ============================================================
    # 21. PROPONOWANY DALSZY PROGRAM BADAWCZY
    # ============================================================
    add_heading_styled(doc, "18. Proponowany dalszy program badawczy", 1)
    
    stages = [
        ("Etap 1 (bieżący) – Koncepualizacja i recenzja", 
         "Finalizacja niniejszego dokumentu, niezależna recenzja przez psychologów-metodologów, "
         "korekta definicji, operacjonalizacji i hipotez."),
        ("Etap 2 – Walidacja psychometryczna (N=300–500)", 
         "Przekrojowe badanie: skale Likert W,C,N + zachowanie + referencyjne (TPB, SDT, COM-B, MDS). "
         "CFA, walidacja konwergentna/dyskryminacyjna, test wersji ciągłej vs binarnej. "
         "Rozdzielenie N na podwymiary (moralne, rolowe, społeczne)."),
        ("Etap 3 – Badanie EMA pilotażowe (N=100, T=14 dni)", 
         "Test HPE, asymetrii, stabilności stanów, hipotez H1–H24. "
         "Estymacja P (DTMC) i Q (CTMC). Porównanie z modelami konkurencyjnymi. "
         "Analiza mocy dla głównego badania."),
        ("Etap 4 – Badanie EMA główne (N=300–500, T=21 dni)", 
         "Pełna walidacja predykcyjna, analiza path dependence, mediacji, moderacji. "
         "Test wersji z intencją (I) i nawykiem (H). Cross-cultural replication."),
        ("Etap 5 – Eksperymenty laboratoryjne i polowe", 
         "Manipulacja W (framing, autonomy support), C (mastery experience, resource provision), "
         "N (internalizacja normy, role induction). Test przyczynowy przejść. "
         "Interwencje: 011→111 (autonomy support), 101→111 (resource allocation), 111→110 (delegation training)."),
        ("Etap 6 – Rozszerzenia teoretyczne", 
         "Wersja ciągła (oktaanty), 4-wymiarowa (I), 5-wymiarowa (A/H), "
         "modele hybrydowe (DMTRD + dual-process), zastosowania kliniczne (depresja, OCD, uzależnienia).")
    ]
    
    for name, desc in stages:
        add_paragraph_styled(doc, name, bold=True)
        add_paragraph_styled(doc, desc)
    
    doc.add_page_break()
    
    # ============================================================
    # 22. WNIOSKI
    # ============================================================
    add_heading_styled(doc, "19. Wnioski", 1)
    
    conclusions = [
        "DMTRD to propozycja teoretyczna opisująca stan motywacyjny przez trzy wymiary binarne (W, C, N) "
        "tworzące 8 stanów ułożonych w graf Q3 z 24 przejściami kierunkowymi.",
        "Kluczowy postulat – Hipoteza Przejść Elementarnych (HPE) – zakłada, że elementarna zmiana motywacyjna "
        "modyfikuje jeden wymiar (d_H=1). To falsyfikowalna hipoteza, nie potwierdzone prawo.",
        "Model wnosi nową treść teoretyczną poprzez: formalną topologię Q3, jawne wyodrębnienie N jako "
        "niezależnego wymiaru, identyfikację stanu 101 z moral distress, oraz asymetrię przejść odwrotnych.",
        "Krytyczna analiza wykazała istotne ograniczenia: binarność konstruktów, brak intencji i celu, "
        "pomijanie automatyzmu/nawyku, mieszanie kategorii normatywnych w N, problemy identyfikowalności. "
        "Te ograniczenia nie unieważniają modelu, ale wskazują kierunki koniecznych rozszerzeń.",
        "Sformułowano 24 hipotezy badawcze (H1–H24) i 5 hipotez ogólnych (HG1–HG5), "
        "zaproponowano metodologię walidacji (EMA, LTA, CTMC, SEM) oraz program badawczy 6 etapów.",
        "DMTRD nie ma ambicji bycia 'lepszym' od TPB, SDT, COM-B czy Rubikonu – ma być "
        "komplementarną perspektywą dynamiczną, uzupełniającą modele statyczne i fazowe o topologię stanów "
        "i hipotezę o elementarności zmiany. Wartość modelu ostatecznie zależy od wyników weryfikacji empirycznej."
    ]
    
    for c in conclusions:
        add_paragraph_styled(doc, c, style='List Bullet')
    
    doc.add_page_break()
    
    # ============================================================
    # 23. BIBLIOGRAFIA
    # ============================================================
    add_heading_styled(doc, "Bibliografia", 1)
    
    refs = [
        "Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50(2), 179–211. https://doi.org/10.1016/0749-5978(91)90020-T",
        "Bandura, A. (1997). Self-efficacy: The exercise of control. Freeman.",
        "Carver, C. S., & Scheier, M. F. (1998). On the self-regulation of behavior. Cambridge University Press.",
        "Cialdini, R. B., Reno, R. R., & Kallgren, C. A. (1990). A focus theory of normative conduct. Journal of Personality and Social Psychology, 58(6), 1015–1026. https://doi.org/10.1037/0022-3514.58.6.1015",
        "Corley, M. C., Elswick, R. K., Gorman, M., & Clor, T. (2001). Development and evaluation of a moral distress scale. Journal of Advanced Nursing, 33(2), 250–256. https://doi.org/10.1046/j.1365-2648.2001.01659.x",
        "Deci, E. L., & Ryan, R. M. (2000). The \"what\" and \"why\" of goal pursuits: Human needs and the self-determination of behavior. Psychological Inquiry, 11(4), 227–268. https://doi.org/10.1207/S15327965PLI1104_01",
        "Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans. American Psychologist, 54(7), 493–503. https://doi.org/10.1037/0003-066X.54.7.493",
        "Heckhausen, H., & Gollwitzer, P. M. (1987). Thought contents and cognitive functioning in motivational versus volitional states. Motivation and Emotion, 11(2), 101–120. https://doi.org/10.1007/BF00992338",
        "Jameton, A. (1984). Nursing practice: The ethical issues. Prentice-Hall.",
        "Kahn, R. L., Wolfe, D. M., Quinn, R. P., Snoek, J. D., & Rosenthal, R. A. (1964). Organizational stress: Studies in role conflict and ambiguity. Wiley.",
        "Kelman, H. C. (1958). Compliance, identification, and internalization: Three processes of attitude change. Journal of Conflict Resolution, 2(1), 51–60. https://doi.org/10.1177/002200275800200106",
        "Locke, E. A., & Latham, G. P. (2002). Building a practically useful theory of goal setting and task motivation. American Psychologist, 57(9), 705–717. https://doi.org/10.1037/0003-066X.57.9.705",
        "Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. Implementation Science, 6, 42. https://doi.org/10.1186/1748-5908-6-42",
        "Ölander, F., & Thøgersen, J. (1995). Understanding of consumer behaviour as a prerequisite for environmental protection. Journal of Consumer Policy, 18(4), 345–385. https://doi.org/10.1007/BF01024160",
        "Schwartz, S. H. (1977). Normative influences on altruism. In L. Berkowitz (Ed.), Advances in Experimental Social Psychology (Vol. 10, pp. 221–279). Academic Press. https://doi.org/10.1016/S0065-2601(08)60358-5",
        "Sheeran, P., Maki, A., Montanaro, E., Bryan, A., Klein, W. M., Miles, E., & Rothman, A. J. (2016). The impact of changing attitudes, norms, and self-efficacy on health-related intentions and behavior: A meta-analysis. Health Psychology, 35(11), 1178–1188. https://doi.org/10.1037/hea0000387",
        "Stryker, S. (1980). Symbolic interactionism: A social structural version. Benjamin-Cummings.",
        "Vallacher, R. R., & Nowak, A. (1997). Dynamical social psychology. Guilford Press.",
        "Wood, W., & Neal, D. T. (2007). A new look at habits and the habit-goal interface. Psychological Review, 114(4), 843–863. https://doi.org/10.1037/0033-295X.114.4.843",
        "Wrosch, C., Scheier, M. F., Miller, G. E., Schulz, R., & Carver, C. S. (2003). Adaptive self-regulation of unattainable goals: Goal disengagement, goal reengagement, and subjective well-being. Personality and Social Psychology Bulletin, 29(12), 1494–1508. https://doi.org/10.1177/0146167203256921"
    ]
    
    for ref in refs:
        add_paragraph_styled(doc, ref, style='List Bullet', size=10)
    
    doc.add_page_break()
    
    # ============================================================
    # 24. ANEKSY
    # ============================================================
    add_heading_styled(doc, "Aneks A: Pełna charakterystyka 24 przejść", 1)
    add_paragraph_styled(doc, "Zobacz plik: model/przejscia_24.csv (zawartość w tabeli 3 dokumentu).")
    
    add_heading_styled(doc, "Aneks B: Dane stanów (model/stany.csv)", 1)
    add_paragraph_styled(doc, "Pełne dane 8 stanów w formacie CSV do importu do R/Python.")
    
    add_heading_styled(doc, "Aneks C: Pliki GraphML do yEd", 1)
    add_paragraph_styled(doc, 
        "DMTRD_12_krawedzi.graphml – 12 krawędzi nieskierowanych (sąsiedztwo). "
        "DMTRD_24_przejscia.graphml – 24 krawędzie skierowane (przejścia). "
        "Oba pliki zawierają Custom Properties z opisami, interpretacjami i statusem empirycznym.")
    
    add_heading_styled(doc, "Aneks D: Analiza literatury (research/przeglad_literatury.md)", 1)
    add_paragraph_styled(doc, "Szczegółowa analiza 10 teorii referencyjnych z mapowaniem konstruktów.")
    
    add_heading_styled(doc, "Aneks E: Analiza teorii pokrewnych (research/analiza_teorii_pokrewnych.md)", 1)
    add_paragraph_styled(doc, "Tabela porównawcza, ocena oryginalności, modele bardzo podobne do DMTRD.")
    
    add_heading_styled(doc, "Aneks F: Analiza krytyczna (research/analiza_krytyczna.md)", 1)
    add_paragraph_styled(doc, "20 pytań krytycznych, 5 najpoważniejszych argumentów, propozycje poprawek.")
    
    add_heading_styled(doc, "Aneks G: Hipotezy badawcze (research/hipotezy_badawcze.md)", 1)
    add_paragraph_styled(doc, "Pełna specyfikacja H1–H24, HG1–HG5: zmienne, pomiar, analiza, czynniki zakłócające.")
    
    # Save
    output_path = BASE / "DMTRD_koncepcja.docx"
    doc.save(output_path)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()