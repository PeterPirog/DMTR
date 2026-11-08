#!/usr/bin/env python3
"""
Generate DMTRD_streszczenie_dla_recenzenta.docx - Reviewer summary document.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent.parent

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

def main():
    doc = Document()
    
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    
    # Title page
    for _ in range(3):
        doc.add_paragraph()
    
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("DMTRD – Streszczenie dla recenzenta")
    run.bold = True
    run.font.size = Pt(22)
    run.font.color.rgb = RGBColor(0, 51, 102)
    
    doc.add_paragraph()
    
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("Dynamiczny Model Trójwymiarowej Regulacji Działania\nWersja koncepcyjna do niezależnej oceny merytorycznej")
    run.font.size = Pt(13)
    run.font.color.rgb = RGBColor(80, 80, 80)
    
    doc.add_paragraph()
    
    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = meta.add_run(f"Data: {datetime.now().strftime('%d.%m.%Y')}\nProjekt: DMTRD – Etap 1\nDokument główny: DMTRD_koncepcja_rev3_1.docx")
    run.font.size = Pt(11)
    run.italic = True
    
    doc.add_page_break()
    
    # 1. Istota modelu
    add_heading_styled(doc, "1. Istota modelu DMTRD", 1)
    
    add_paragraph_styled(doc, 
        "Dynamiczny Model Trójwymiarowej Regulacji Działania (DMTRD) jest propozycją teoretyczną "
        "opisującą stan motywacyjny człowieka względem konkretnego działania za pomocą trzech "
        "wymiarów binarnych:")
    
    dims = [
        ("W – CHCĘ", "Chęć wykonania konkretnego działania."),
        ("C – MOGĘ", "Przekonanie o możliwości wykonania działania."),
        ("N – POWINIENEM", "Racjonalne przekonanie o konieczności wykonania działania ze względu na własne cele. Źródło i jakość regulacji (N_source, N_quality) to osobne zmienne.")
    ]
    
    for name, desc in dims:
        add_paragraph_styled(doc, f"{name}: {desc}", style='List Bullet')
    
    add_paragraph_styled(doc, 
        "Każdy wymiar przyjmuje wartość 0 (brak) lub 1 (obecność). Tworzy to 8 możliwych stanów "
        "(000, 001, 010, 011, 100, 101, 110, 111), które odpowiadają wierzchołkom trójwymiarowego "
        "hipersześcianu Q3.")
    
    # 2. Wyjaśnienie trzech wymiarów
    add_heading_styled(doc, "2. Wyjaśnienie trzech wymiarów", 1)
    
    add_paragraph_styled(doc, 
        "Wymiary odpowiadają trzem fundamentalnym pytaniom, jakie jednostka zadaje sobie przed działaniem:", bold=True)
    
    q = [
        "W: \"Czy chcę to zrobić?\" (Chęć)",
        "C: \"Czy jestem w stanie to zrobić? Czy widzę sposób na realizację?\" (Przekonanie o możliwości)",
        "N: \"Czy powinienem to zrobić ze względu na swoje cele?\" (Racjonalne przekonanie o konieczności)"
    ]
    for qq in q:
        add_paragraph_styled(doc, qq, style='List Bullet')
    
    add_paragraph_styled(doc, 
        "Ważne rozróżnienia: W=0 to nie silna niechęć (to brak motywacji); C=0 to nie obiektywna niemożność "
        "(to subiektywna ocena); N=0 to nie zakaz (to brak obowiązku). Stan (W,C,N) to stan motywacyjny, "
        "nie intencja (TPB) ani działanie.")
    
    # 3. Struktura ośmiu stanów
    add_heading_styled(doc, "3. Struktura ośmiu stanów", 1)
    
    states = [
        ("000", "Spoczynek / Brak przesłanek", "W=0, C=0, N=0 – brak chęci, możliwości i powinności"),
        ("001", "Tylko powinność", "N=1, W=0, C=0 – przekonanie o konieczności bez chęci i możliwości"),
        ("010", "Tylko możliwość", "C=1, W=0, N=0 – przekonanie o możliwości bez chęci i powinności"),
        ("011", "Możliwość + powinność (bez chęci)", "C=1, N=1, W=0 – działanie bez wewnętrznej zgody"),
        ("100", "Tylko chęć", "W=1, C=0, N=0 – chęć bez przekonania o możliwości i powinności"),
        ("101", "Chęć + powinność (bez możliwości)", "W=1, N=1, C=0 – silne napięcie motywacyjne: chęć i przekonanie o konieczności bez możliwości"),
        ("110", "Chęć + możliwość (bez powinności)", "W=1, C=1, N=0 – gotowość do działania z inicjatywy, sprawczość"),
        ("111", "Pełna zbieżność trzech przesłanek", "W=1, C=1, N=1 – pełna gotowość (nie zawsze optymalna)")
    ]
    
    for code, name, desc in states:
        add_paragraph_styled(doc, f"{code} – {name}: {desc}", style='List Bullet')
    
    add_paragraph_styled(doc, 
        "Stan 101 (W=1, C=0, N=1) jest kluczowy – konfiguracja silnego napięcia motywacyjnego (chęć + przekonanie o konieczności bez przekonania o możliwości). "
        "W kontekście moralnym hipoteza H_MD przewiduje, że 101 predysponuje do moral distress (Jameton, Corley). "
        "Również: niemożliwe cele z identyfikacją (Goal-Setting). Stan 011 to działanie bez wewnętrznej zgody "
        "(motywacja kontrolowana w SDT). Stan 110 to gotowość do działania z inicjatywy (SDT, SCT). "
        "Stan 111 przy zinternalizowanym przekonaniu o konieczności to najwyższa jakość motywacji; przy N eksternalnym – ryzyko wypalenia.")
    
    # 4. Najważniejsze założenie: HPE
    add_heading_styled(doc, "4. Najważniejsze założenie: Hipoteza Przejść Elementarnych (HPE)", 1)
    
    add_paragraph_styled(doc, 
        "HPE-model: W generatorze Q (CTMC) intensywności przejść między stanami o odległości Hamminga d_H ≥ 2 są równe zero: "
        "qᵢⱼ = 0 dla d_H ≥ 2. To ograniczenie na strukturę generatora, a nie twierdzenie o psychologicznej atomowości. "
        "Z 8 stanów powstaje 24 dopuszczalne przejścia kierunkowe (d_H = 1).")
    
    add_paragraph_styled(doc, 
        "HPE-empiryczna (hipoteza testowalna): W danych EMA z gęstym próbkowaniem, odsetek obserwowanych zmian "
        "d_H ≥ 2 jest istotnie mniejszy niż przewidywane przez model alternatywny (np. niezależne zmiany bitów z błędami). "
        "Ważne: Nawet gdy Q spełnia HPE-model, macierz P(Δt) = exp(QΔt) dla Δt > 0 może mieć pᵢⱼ > 0 dla d_H ≥ 2 "
        "(przejścia wieloetapowe w jednym interwale pomiarowym). Rozwiązuje problem EMA.")
    
    add_paragraph_styled(doc, 
        "Graf stanów to Q3 (hipersześcian): 8 węzłów, 12 krawędzi nieskierowanych, 24 przejścia kierunkowe. "
        "Każdy węzeł ma stopień 3. Graf jest dwudzielny, spójny, średnica 3.", bold=True)
    
    add_paragraph_styled(doc, 
        "Kluczowa cecha: Asymetria przejść odwrotnych. Np. 011→111 (internalizacja, dodanie W) to inny proces "
        "niż 111→011 (utrata autonomii, wypalenie). 101→111 (rozwiązanie konfliktu) to inny proces niż "
        "111→101 (kryzys zasobów, napięcie krytyczne ostre). To generuje specyficzne, testowalne przewidywania.")
    
    # 5. Potencjalne powiązania z teoriami
    add_heading_styled(doc, "5. Potencjalne powiązania z istniejącymi teoriami", 1)
    
    theories = [
        ("TPB (Ajzen)", "W ≈ postawa, C ≈ PBC, N ≈ normy subiektywne. Różnice: TPB ma intencję, zmienne ciągłe, brak N jako moralnych/rolowych, brak dynamiki stanów."),
        ("SDT (Deci, Ryan)", "W=1 ≈ motywacja autonomiczna; 011 ≈ motywacja kontrolowana (introjektowana); 110 ≈ zidentyfikowana; 111 ≈ zintegrowana. Różnice: SDT ma jakość motywacji (typy regulacji), brak binarnego N, potrzeba autonomii/kompetencji/powiązania."),
        ("COM-B (Michie et al.)", "W ≈ Reflective Motivation, C ≈ Capability+Opportunity, N ⊂ Opportunity/Motivation. Różnice: COM-B dzieli na psych/fiz, soc/fiz, ref/aut; ma Automatic Motivation (nawyki); ma BCW do interwencji."),
        ("Rubikon (Heckhausen, Gollwitzer)", "Fazy Rubikonu ≈ sekwencje stanów DMTRD. Różnice: Rubikon ma intencję implementacyjną, volicję, brak N, fazy sekwencyjne (nie graf)."),
        ("SCT (Bandura)", "C ≈ self-efficacy (ale binarne vs ciągłe). W ≈ outcome expectancies + cele. Różnice: self-efficacy centralna, specyficzna dziedzinowo, 4 źródła; brak N."),
        ("Goal-Setting (Locke, Latham)", "W ≈ zangażowanie w cel, C ≈ osiągalność. Różnice: cel centralny, feedback, rezygnacja/reengagement; brak stanów."),
        ("Samoregulacja (Carver, Scheier)", "Model cybernetyczny (ciągły) vs graf stanów (dyskretny). Różnice: pętla zwrotna, hierarchia celów, afekt jako sygnał; brak N."),
        ("Teorie nawyku (Wood, Neal)", "DMTRD modeluje System 2; nawyki = System 1 (stan 010/011 to normalne działanie, nie 'brak chęci'). Luka modelu."),
        ("MOA (Ölander, Thøgersen)", "Bardzo bliskie: M≈W, O≈C (zewn.), A≈C (wewn.). Różnice: MOA ciągłe, predykcyjne, rozdziela O i A; DMTRD binarne, dynamiczne, scala C."),
        ("Modele dynamiczne (Vallacher, Borsboom)", "DMTRD = dyskretna aproksymacja Q3. Różnice: modele dynamiczne ciągłe, atrakcje, bifurkacje, sieci; brak dyskretnych stanów.")
    ]
    
    for name, rel in theories:
        add_paragraph_styled(doc, f"{name}: {rel}", style='List Bullet')
    
    # 6. Możliwe zastosowania
    add_heading_styled(doc, "6. Możliwe zastosowania", 1)
    
    apps = [
        "Psychologia zdrowia/medycyna: stan 101 (silne napięcie motywacyjne) – ryzyko moral distress personelu; przewidywanie wypalenia, interwencje 101→111 (systemowe zmiany), 111→110 (delegacja/sukcesja).",
        "Zarządzanie/HR: diagnoza stanów zespołów (011 działanie bez zgody vs 110 gotowość z inicjatywy vs 111 zaangażowanie); job crafting (010→110, 100→110); sukcesja (111→110).",
        "Edukacja: internalizacja 011→111 (wsparcie autonomii); rezygnacja 101→001 (silne napięcie motywacyjne studentów).",
        "Psychologia społeczna/polityczna: aktywizm (100→110→111), radikalizacja (001→101), demobilizacja (111→011).",
        "Badania nad nawykami: rozszerzenie o parametr H (siła nawyku) – modelowanie 010↔110.",
        "Modelowanie symulacyjne/AI: agent-based modeling na Q3."
    ]
    for a in apps:
        add_paragraph_styled(doc, a, style='List Bullet')
    
    # 7. Najważniejsze wątpliwości naukowe
    add_heading_styled(doc, "7. Najważniejsze wątpliwości naukowe", 1)
    
    doubts = [
        ("Binarność konstruktów", "Wszystkie teorie referencyjne używają skal ciągłych. Binarne W traci typy motywacji (intryntyczna vs introjektowana); binarne C traci gradację self-efficacy; binarne N traci kategorie norm (moralne, rolowe, społeczne). Czy utrata informacji jest akceptowalna?"),
        ("Brak intencji i celu", "TPB, Rubikon, Goal-Setting, Carver & Scheier – intencja/cel centralne. DMTRD stan (W,C,N) nie ma intencji ani celu. Stan 111 = gotowość (preactional) czy działanie (actional)? Brak mechanizmu stan→zachowanie."),
        ("Pomijanie automatyzmu/nawyku", "40–50% działań to nawyki (System 1). DMTRD modeluje tylko System 2. Stan 010/011 to normalne działanie nawykowe, a nie 'brak chęci'. Przejścia 010↔110 nie oddają dynamiki nawyków."),
        ("N miesza kategorie norm", "N łączy normy opisowe, inskryptywne, moralne, rolowe, zinternalizowane, eksternalne. To różne mechanizmy (działanie bez zgody vs internalizacja). Stan 011 może być działanie bez zgody LUB introjektowana regulacja – DMTRD nie rozróżnia."),
        ("Identyfikowalność statystyczna", "3 wskaźniki binarne → 8 wzorców = 8 klas latentnych = model nasycony (0 df). LTA/HMM nie testowalne bez wskaźników ciągłych lub dodatkowych zmiennych. CTMC wymaga gęstego EMA."),
        ("Hipoteza jednego bitu (HPE)", "Czy elementarny proces psychologiczny = 1 bit? Równoczesne zmiany możliwe (bifurkacje, ambiwalencja). Ograniczona częstotliwość EMA może maskować zmiany wielobitowe. HPE to hipoteza, nie fakt."),
        ("Stan 111 nie zawsze optymalny", "N może być eksternalne (presja), W perfekcjonistyczne, C przecenione. Model nie rozróżnia jakości 111 w zależności od pochodzenia N.")
    ]
    
    for name, desc in doubts:
        add_paragraph_styled(doc, f"{name}: {desc}", style='List Bullet')
    
    # 8. Pytania do recenzenta
    add_heading_styled(doc, "8. Pytania do recenzenta", 1)
    
    add_paragraph_styled(doc, 
        "Proszę o ocenę poniższych kwestii (nie sugerujemy oczekiwanej pozytywnej oceny):", bold=True)
    
    questions = [
        "1. Zasadność wyodrębnienia trzech wymiarów (W, C, N): Czy te trzy konstrukty są psychometrycznie odseparowywalne? Czy binarna operacjonalizacja nie traci istotnej informacji (typy motywacji, gradacja self-efficacy, kategorie norm)? Czy wersja ciągła (oktaanty w [0,1]³) nie byłaby bardziej adekwatna?",
        "2. Poprawność interpretacji stanów: Czy interpretacje stanów 001, 011, 101, 110, 111 są teoretycznie uzasadnione i empirycznie rozróżnialne? Czy stan 101 (konfiguracja napięcia motywacyjnego) w kontekście moralnym predysponuje do moral distress (hipoteza H_MD)? Czy stan 111 przy N eksternalnym nie powinien być klasyfikowany inaczej?",
        "3. Wiarygodność reguły jednego bitu (HPE): Czy elementarny proces psychologiczny zmiany motywacji realnie modyfikuje jeden wymiar? Czy równoczesne zmiany (d_H ≥ 2) są możliwe psychologicznie (ambiwalencja, bifurkacje) lub tylko artefaktem pomiarowym? Jak to zweryfikować w EMA?",
        "4. Wartość poznawcza dynamiki przejść: Czy asymetria przejść odwrotnych (np. 011→111 vs 111→011) generuje przewidywania różniące się od modeli płaskich (TPB, SDT, COM-B)? Czy topologia Q3 ma wartość heurystyczną ponad estetykę?",
        "5. Potencjalne problemy operacjonalizacji: Jak zmierzyć W, C, N w EMA (binarne vs Likert)? Jak rozdzielić N na podkategorie (moralne, rolowe, społeczne)? Jak uwzględnić nawyk/automatyzm (System 1)? Czy model jest identyfikowalny przy dostępnych danych?",
        "6. Możliwości empirycznej walidacji: Czy zaproponowana metodologia (EMA + LTA/CTMC/SEM) jest wykonalna i wystarczająca? Jakie N i T są potrzebne do mocy >0.80 dla testów HPE, asymetrii, mediacji? Czy porównanie z modelami konkurencyjnymi (TPB, SDT, COM-B) jest sensowne?",
        "7. Rzeczywista oryginalność propozycji: Czy DMTRD wnosi nową treść teoretyczną (Q3, HPE, N niezależny, stan 101, asymetria) nad to, co zawarte w MOA, COM-B, TPB, SDT, Rubikon? Gdzie model jest tylko redukcją/renomowaniem istniejących idei?",
        "8. Granice zastosowań i ryzyka: W jakich kontekstach model może wprowadzać w błąd (nawyki, ambiwalencja, patologie kliniczne, różnice kulturowe)? Czy model ma wartość interwencyjną (jak BCW) czy tylko opisową?"
    ]
    
    for q in questions:
        add_paragraph_styled(doc, q, style='List Number')
    
    # Save
    output_path = BASE / "DMTRD_streszczenie_dla_recenzenta_rev3_1.docx"
    doc.save(str(output_path))
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()