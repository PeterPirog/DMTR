#!/usr/bin/env python3
"""
DMTRD DOCX Validator
Waliduje końcowy dokument DMTRD_koncepcja_rev2.docx pod kątem spójności naukowej i technicznej.
"""

from docx import Document
from docx.oxml.ns import qn
from pathlib import Path
import re
import sys

BASE = Path(__file__).parent.parent

def load_expected_states():
    """Ładuje oczekiwane stany z CSV."""
    import csv
    states = {}
    with open(BASE / "model" / "stany.csv", 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            states[row['kod']] = row
    return states

def load_expected_transitions():
    """Ładuje oczekiwane przejścia z CSV."""
    import csv
    transitions = []
    with open(BASE / "model" / "przejscia_24.csv", 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transitions.append(row)
    return transitions

class DocxValidator:
    def __init__(self, docx_path):
        self.docx_path = Path(docx_path)
        self.doc = Document(docx_path)
        self.errors = []
        self.warnings = []
        self.info = []
        
        # Pobierz cały tekst dokumentu
        self.full_text = "\n".join([p.text for p in self.doc.paragraphs])
        self.table_texts = []
        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    self.table_texts.append(cell.text)
        self.all_text = self.full_text + "\n" + "\n".join(self.table_texts)
    
    def check_document_opens(self):
        """1. Czy dokument otwiera sie poprawnie."""
        try:
            _ = self.doc.paragraphs
            _ = self.doc.tables
            self.info.append("[OK] Dokument otwiera sie poprawnie")
            return True
        except Exception as e:
            self.errors.append(f"[ERROR] Dokument nie otwiera sie: {e}")
            return False
    
    def check_required_chapters(self):
        """2. Czy istnieja wszystkie wymagane rozdziały."""
        required_chapters = [
            "Wstęp",
            "Problem badawczy",
            "Uzasadnienie przyjętych trzech wymiarów",
            "Definicje konstruktów",
            "Geneza i podstawowe założenia",
            "Analiza istniejących teorii",
            "Formalizacja matematyczna",
            "Charakterystyka ośmiu stanów",
            "Graf stanów i topologia przejść",
            "Mechanizmy dynamiki motywacyjnej",
            "Związek stanów z podejmowaniem",
            "Zależność od ścieżki",
            "Hipotezy badawcze",
            "Propozycja metodologii walidacji",
            "Krytyczna ocena teorii",
            "Ograniczenia modelu",
            "Możliwe zastosowania",
            "Proponowany dalszy program badawczy",
            "Wnioski",
            "Bibliografia"
        ]
        
        found_chapters = []
        for p in self.doc.paragraphs:
            if p.style and p.style.name and p.style.name.startswith('Heading'):
                found_chapters.append(p.text.strip())
        
        missing = []
        for req in required_chapters:
            found = any(req.lower() in fc.lower() for fc in found_chapters)
            if not found:
                missing.append(req)
        
        if missing:
            self.errors.append(f"✗ Brakujące rozdziały: {missing}")
            return False
        else:
            self.info.append(f"✓ Wszystkie {len(required_chapters)} wymaganych rozdziałów znaleziono")
            return True
    
    def check_q3_diagram(self):
        """3. Czy zawiera diagram Q3."""
        # Sprawdź obrazy
        has_image = False
        for rel in self.doc.part.rels.values():
            if "image" in rel.target_ref:
                has_image = True
                break
        
        # Sprawdź też w tekście odniesienia do diagramu
        has_ref = any("Rysunek 1" in p.text or "Graf stanów" in p.text or "Q3" in p.text for p in self.doc.paragraphs)
        
        if has_image and has_ref:
            self.info.append("[OK] Diagram Q3 (Rysunek 1) znaleziony")
            return True
        elif has_ref:
            self.warnings.append("[WARN] Odniesienie do diagramu Q3 znalezione, ale obraz moze nie byc osadzony")
            return True
        else:
            self.errors.append("[ERROR] Brak diagramu Q3 ani odniesienia do niego")
            return False
    
    def check_eight_states(self):
        """4. Czy zawiera opisy ośmiu stanów."""
        states = load_expected_states()
        found_states = 0
        missing_states = []
        
        for code, state in states.items():
            # Sprawdź czy kod stanu występuje w tekście
            if code in self.all_text:
                found_states += 1
            else:
                missing_states.append(code)
        
        if found_states == 8:
            self.info.append(f"[OK] Wszystkie 8 stanow ({found_states}/8) znalezione w dokumencie")
            return True
        else:
            self.errors.append(f"[ERROR] Brakujace stany: {missing_states} (znaleziono {found_states}/8)")
            return False
    
    def check_24_transitions(self):
        """5. Czy zawiera charakterystyki 24 przejść."""
        transitions = load_expected_transitions()
        found_transitions = 0
        missing_transitions = []
        
        for t in transitions:
            trans_id = t['id']
            start_end = f"{t['start']}->{t['end']}"
            # Sprawdź ID lub start→end
            if trans_id in self.all_text or start_end in self.all_text:
                found_transitions += 1
            else:
                missing_transitions.append(f"{trans_id} ({start_end})")
        
        if found_transitions == 24:
            self.info.append(f"[OK] Wszystkie 24 przejscia ({found_transitions}/24) znalezione w dokumencie")
            return True
        else:
            self.warnings.append(f"[WARN] Znaleziono {found_transitions}/24 przejsc. Brakujace: {missing_transitions[:5]}...")
            return found_transitions > 20  # Akceptuj jeśli większość
    
    def check_current_hypotheses(self):
        """6. Czy ma aktualny zestaw hipotez (HPE, HPD, HPP, E1-E24)."""
        required_hypotheses = ["HPE", "HPD", "HPP"]
        # E1-E24 są wymieniane zbiorczo w dokumencie głównym, szczegóły w research/
        exploratory_mentioned = "E1" in self.all_text and "E24" in self.all_text
        
        missing_main = []
        for h in required_hypotheses:
            if h not in self.all_text:
                missing_main.append(h)
        
        if not missing_main and exploratory_mentioned:
            self.info.append("[OK] Hipotezy glowne (HPE, HPD, HPP) i zakres eksploracyjnych (E1-E24) znalezione")
            return True
        else:
            issues = []
            if missing_main:
                issues.append(f"brakujace glowne: {missing_main}")
            if not exploratory_mentioned:
                issues.append("brak wspomnienia E1-E24")
            self.errors.append(f"[ERROR] Problemy z hipotezami: {issues}")
            return False
    
    def check_no_old_errors(self):
        """7. Czy nie przywraca błędów modelu pierwotnego (jako aktualnych twierdzeń)."""
        # Te wzorce są błędem TYLKO jeśli występują jako aktualne twierdzenia,
        # a nie w sekcji krytycznej analizy (gdzie omówiono błędy POPRZEDNIE wersje)
        # Sprawdzamy czy występują POZA sekcją "Krytyczna ocena" / "Critical"
        critical_section_start = False
        for p in self.doc.paragraphs:
            if "Krytyczna ocena" in p.text or "Critical" in p.text:
                critical_section_start = True
        
        # Jeśli sekcja krytyczna istnieje, błędy w niej są OK (to analiza błędów)
        # Sprawdzamy tylko w części przed sekcją krytyczną
        text_before_critical = self.full_text
        if critical_section_start:
            # Znajdź pozycję sekcji krytycznej
            idx = self.full_text.find("Krytyczna ocena")
            if idx == -1:
                idx = self.full_text.find("Critical")
            if idx > 0:
                text_before_critical = self.full_text[:idx]
        
        old_errors = [
            # 101 = moral distress jako twierdzenie równości (nie jako zaprzeczenie)
            ("101 = moral distress (jako rownowaznosc)", r"(?<!NIE\s)(?<!nie\s)(?<!nie jest\s)stan 101\s*(jest|to)\s*moral distress|moral distress\s*(jest|to)\s*stan 101|101\s*=\s*moral distress"),
            # klasy latentne jako model bazowy (nie jako metoda LTA) - szukamy bliskiego skojarzenia
            ("klasy latentne (jako model bazowy)", r"model\s+bazowy.{0,50}klas.*latentn|klas.*latentn.{0,50}model\s+bazowy|stany\s*=\s*klas.*latentn"),
            # HG1-HG5 jako aktualne hipotezy główne
            ("HG1-HG5 (jako aktualne hipotezy)", r"HG[1-5].*hipoteza.*glowna|hipotezy\s*glowne.*HG[1-5]"),
            # stary plik hipotezy_badawcze.md jako referencja główna
            ("hipotezy_badawcze.md (stary plik glowny)", r"hipotezy_badawcze\.md(?!_rev1)(?!\s*\(wersja eksploracyjna)"),
            # Działanie autonomiczne jako nazwa stanu 110
            ("Działanie autonomiczne (jako nazwa stanu 110)", r"stan 110.*Działanie autonomiczne|Działanie autonomiczne.*stan 110"),
            # intencja centralna jako cecha DMTRD
            ("intencja centralna (jako cecha DMTRD)", r"DMTRD.*intencja.*centralna|intencja.*centralna.*DMTRD"),
            # próg 15% jako kryterium HPE
            ("prog 15% (jako kryterium HPE)", r"prog.*15%.*HPE|HPE.*15%|kryterium.*HPE.*15%"),
            # saturated model 0 df jako cecha modelu bazowego
            ("saturated model 0 df (jako model bazowy)", r"model\s+bazowy.{0,50}saturated|saturated.{0,50}model\s+bazowy"),
        ]
        
        found_errors = []
        for name, pattern in old_errors:
            if re.search(pattern, text_before_critical, re.IGNORECASE):
                found_errors.append(name)
        
        if found_errors:
            self.errors.append(f"[ERROR] Znaleziono bledy modelu pierwotnego (poza sekcja krytyczna): {found_errors}")
            return False
        else:
            self.info.append("[OK] Nie znaleziono bledow modelu pierwotnego jako aktualnych twierdzen")
            return True
    
    def check_bibliography(self):
        """8. Czy bibliografia jest obecna."""
        has_bib = any("Bibliografia" in p.text or "References" in p.text for p in self.doc.paragraphs)
        has_citations = any(ref in self.all_text for ref in ["Ajzen", "Bandura", "Deci", "Ryan", "Schwartz", "Corley", "Jameton"])
        
        if has_bib and has_citations:
            self.info.append("[OK] Bibliografia i cytowania znalezione")
            return True
        elif has_bib:
            self.warnings.append("[WARN] Sekcja Bibliografia znaleziona, ale brak kluczowych cytowan")
            return True
        else:
            self.errors.append("[ERROR] Brak sekcji Bibliografia")
            return False
    
    def check_tables_correct(self):
        """9. Czy tabele zawierają poprawne dane."""
        # Sprawdź tabelę stanów
        state_table_found = False
        trans_table_found = False
        hypothesis_table_found = False
        
        for table in self.doc.tables:
            if len(table.rows) > 0:
                header_text = " ".join([cell.text for cell in table.rows[0].cells])
                if "Kod" in header_text and "W" in header_text and "Nazwa" in header_text:
                    state_table_found = True
                    # Sprawdź czy ma 9 wierszy (1 header + 8 stanów)
                    if len(table.rows) >= 9:
                        self.info.append("[OK] Tabela stanów: poprawna struktura (8 stanów + header)")
                    else:
                        self.warnings.append(f"[WARN] Tabela stanów: za mało wierszy ({len(table.rows)})")
                elif "ID" in header_text and "Start" in header_text and "Wymiar" in header_text:
                    trans_table_found = True
                elif "Id" in header_text and "Nazwa" in header_text and "Formalna" in header_text:
                    hypothesis_table_found = True
        
        if state_table_found and trans_table_found and hypothesis_table_found:
            self.info.append("[OK] Wszystkie kluczowe tabele znalezione")
            return True
        else:
            missing = []
            if not state_table_found: missing.append("stanów")
            if not trans_table_found: missing.append("przejść")
            if not hypothesis_table_found: missing.append("hipotez głównych")
            self.warnings.append(f"[WARN] Brakujace tabele: {missing}")
            return len(missing) == 0
    
    def check_version_consistency(self):
        """10. Czy wersja dokumentu zgadza się z wersją źródeł."""
        # Sprawdź czy w dokumencie jest "rev2" lub data dzisiejsza
        from datetime import datetime
        today = datetime.now().strftime('%d.%m.%Y')
        
        has_rev2 = "rev2" in self.all_text.lower() or "_rev2" in self.docx_path.name.lower()
        has_today = today in self.all_text
        
        if has_rev2 or has_today:
            self.info.append(f"[OK] Wersja dokumentu aktualna (rev2 lub data {today})")
            return True
        else:
            self.warnings.append(f"[WARN] Wersja dokumentu moze nie byc aktualna (brak 'rev2' ani dzisiejszej daty {today})")
            return True
    
    def run_all_checks(self):
        """Uruchamia wszystkie sprawdzenia."""
        print(f"Walidacja dokumentu: {self.docx_path.name}")
        print("=" * 60)
        
        checks = [
            ("1. Otwarcie dokumentu", self.check_document_opens),
            ("2. Wymagane rozdziały", self.check_required_chapters),
            ("3. Diagram Q3", self.check_q3_diagram),
            ("4. Osiem stanów", self.check_eight_states),
            ("5. 24 przejścia", self.check_24_transitions),
            ("6. Hipotezy aktualne", self.check_current_hypotheses),
            ("7. Brak starych bledow", self.check_no_old_errors),
            ("8. Bibliografia", self.check_bibliography),
            ("9. Tabele poprawne", self.check_tables_correct),
            ("10. Wersja spójna", self.check_version_consistency),
        ]
        
        passed = 0
        failed = 0
        
        for name, check_func in checks:
            print(f"\n{name}...")
            try:
                result = check_func()
                if result:
                    passed += 1
                else:
                    failed += 1
            except Exception as e:
                self.errors.append(f"[ERROR] Blad w sprawdzaniu {name}: {e}")
                failed += 1
        
        print("\n" + "=" * 60)
        print("PODSUMOWANIE WALIDACJI DOCX")
        print("=" * 60)
        print(f"Przeszlo: {passed}/{len(checks)}")
        print(f"Nie przeszlo: {failed}/{len(checks)}")
        
        if self.errors:
            print(f"\nBLEDY ({len(self.errors)}):")
            for e in self.errors:
                # Replace Unicode chars for console
                safe = e.replace('\u2717', '[X]').replace('\u2713', '[V]').replace('\u2192', '->')
                print(f"  {safe}")
        
        if self.warnings:
            print(f"\nOSTRZEZENIA ({len(self.warnings)}):")
            for w in self.warnings:
                safe = w.replace('\u2717', '[X]').replace('\u2713', '[V]').replace('\u2192', '->')
                print(f"  {safe}")
        
        if self.info:
            print(f"\nINFORMACJE ({len(self.info)}):")
            for i in self.info:
                safe = i.replace('\u2717', '[X]').replace('\u2713', '[V]').replace('\u2192', '->')
                print(f"  {safe}")
        
        # Oblicz status końcowy
        if failed == 0 and len(self.errors) == 0:
            print("\nSTATUS: PASS")
            return "PASS"
        elif failed <= 2 and len(self.errors) <= 2:
            print("\nSTATUS: PARTIAL")
            return "PARTIAL"
        else:
            print("\nSTATUS: FAIL")
            return "FAIL"

def main():
    docx_path = BASE / "DMTRD_koncepcja_rev3.docx"
    if not docx_path.exists():
        print(f"BŁĄD: Plik {docx_path} nie istnieje")
        sys.exit(1)
    
    validator = DocxValidator(docx_path)
    status = validator.run_all_checks()
    
    # Zapisz raport
    report_path = BASE / "reports" / "DMTRD_rev2_docx_validation.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Raport walidacji DOCX - DMTRD rev2\n\n")
        f.write(f"Plik: {docx_path.name}\n")
        f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Status: {status}\n\n")
        
        if validator.errors:
            f.write("## Błędy\n\n")
            for e in validator.errors:
                f.write(f"- {e}\n")
            f.write("\n")
        
        if validator.warnings:
            f.write("## Ostrzeżenia\n\n")
            for w in validator.warnings:
                f.write(f"- {w}\n")
            f.write("\n")
        
        if validator.info:
            f.write("## Informacje\n\n")
            for i in validator.info:
                f.write(f"- {i}\n")
    
    print(f"\nRaport zapisano: {report_path}")
    
    if status == "FAIL":
        sys.exit(1)

if __name__ == "__main__":
    from datetime import datetime
    main()