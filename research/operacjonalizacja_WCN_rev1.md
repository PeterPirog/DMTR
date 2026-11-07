# Operacjonalizacja Wymiarów W, C, N – DMTRD rev1

**Wersja:** 1.0  
**Data:** 07.11.2026  
**Status:** Wersja po rewizji krytycznej (ASTRA review)  
**Cel:** Jednoznaczna definicja operacyjna trzech wymiarów DMTRD do zastosowania w badaniach empirycznych (EMA, kwestionariusze, wywiady).

---

## 1. Zasady ogólne

### 1.1. Definicje vs wskaźniki
- **Definicja teoretyczna (konstrukt):** Co mierzymy (np. "osobista akceptacja wartości celu").
- **Definicja operacyjna (wskaźnik):** Jak mierzymy (np. skala Likert 1–7, item "W jakim stopniu akceptujesz wartość tego celu?").
- **Kod stanu (W,C,N):** Wynik dyskretyzacji (próg 4) lub klasyfikacji w modelu dyskretnym. **Nie jest to definicja konstruktu.**

### 1.2. Wersje pomiarowe
| Wersja | Zastosowanie | Skala | Uwagi |
|--------|--------------|-------|-------|
| **Ciągła (bazowa)** | EMA, SEM, CTMC, regresje | Likert 1–7 | Zachowuje informację o natężeniu; domyślna w analizach |
| **Binarna (uproszczenie)** | Wizualizacja Q3, LTA z klasami latentnymi (z ograniczeniami) | 0/1 (próg 4) | Tylko do interpretacji/wizualizacji; traci informację |
| **Ciągła z ambiwalencją** | Badania nad ambiwalencją | [-1, 1] lub [1,7]×[1,7] | W = chęć - awersja; opcjonalne rozszerzenie |

---

## 2. Wymiar W – CHCĘ (Osobista akceptacja wartości celu)

### 2.1. Definicja teoretyczna
**W = Osobista akceptacja wartości celu / zgoda na realizację celu.**

- **To jest:** Pozytywna wertefukacja celu; zgoda na to, że cel jest wartościowy i godzien realizacji; "tak, chcę, by to się wydarzyło/doszło do tego".
- **To NIE jest:**
  - Chwilowa ochota / chęć (affect-driven desire) – to stan afektywny, chwilowy.
  - Pragnienie / silne pragnienie (craving/urge) – intensywność motywacji, nie jej znak.
  - Intencja (intention) – plan działania (TPB); W to ocena wartości, nie plan.
  - Motywacja intryntyczna (intrinsic motivation) – tylko jeden typ regulacji (SDT).
  - Autonomy (autonomia) – jakość regulacji (SDT), nie binarna akceptacja.
  - Preferencja (preference) – wybór między alternatywami.

### 2.2. Definicja operacyjna (wersja ciągła – bazowa)

**Item główny (EMA, skala 1–7):**
> "W jakim stopniu **osobiście akceptujesz wartość tego celu / zgadzasz się z jego realizacją**?"
> 1 – Wcale nie akceptuję / nie zgadzam się  
> 4 – Umiarkowanie / nie mam zdania  
> 7 – Pełnie akceptuję / w pełni zgadzam się

**Dodatkowe itemy (do wiarygodności i CFA):**
1. "Ten cel jest dla mnie wartościowy." (Value)
2. "Osobiście chcę, by ten cel został zrealizowany." (Personal endorsement)
3. "Zgadzam się z tym, że ten cel powinien zostać zrealizowany." (Agreement)

### 2.3. Kodowanie binarne (uproszczenie)
- **W = 1** jeśli średnia z itemów ≥ 4 (próg 4 na skali 1–7)
- **W = 0** jeśli średnia < 4
- *Uwaga:* Próg 4 jest arbitralny; wersja ciągła jest bazowa.

### 2.4. Przypadki brzegowe i kodowanie

| Sytuacja | W (ciągłe) | W (binarne) | Uwagi |
|----------|------------|-------------|-------|
| "Uznaję cel za wartościowy, ale nie mam siły/chęci teraz" | 5–6 | 1 | W=1 (akceptacja wartości ≠ chwilowa chęć) |
| "Silnie chcę nagrodę, ale cel mi nie pasuje (presja)" | 2–3 | 0 | W=0 (brak osobistej akceptacji celu) |
| "Pragnę rezultatu, ale nie zamierzam działać (brak intencji)" | 5–6 | 1 | W=1 (akceptacja ≠ intencja) |
| "Czuję awersję do celu (chcę, by się NIE wydarzył)" | 1–2 | 0 | W=0 (awersja = negatywna akceptacja) |
| Neutralność ("nie mam zdania") | 4 | 0 (próg) | Granica decyzyjna |

### 2.5. Wskaźniki referencyjne (do walidacji kryterialnej)
| Konstrukt referencyjny | Skala | Oczekiwana korelacja z W |
|------------------------|-------|---------------------------|
| Identified Regulation (SDT) | BRSQ / SRQ | **Wysoka (r > 0.6)** – najbliższy konstrukt |
| Integrated Regulation (SDT) | BRSQ | Wysoka |
| Intrinsic Motivation (IMI Interest/Enjoyment) | IMI | Umiarkowana (r ~ 0.4–0.5) |
| Attitude toward Behavior (TPB) | TPB questionnaire | Umiarkowana (r ~ 0.4–0.5) |
| Personal Norm (Schwartz) | PN scale | Umiarkowana (N_source=internal → korelacja z W) |
| External Regulation (SDT) | BRSQ | Niska/zerowa |

---

## 3. Wymiar C – MOGĘ (Subiektywnie oceniana wykonalność)

### 3.1. Definicja teoretyczna
**C = Subiektywnie oceniana wykonalność działania.**

- **To jest:** Przekonanie/ocena: "Jestem w stanie to zrealizować / widzę sposób na to, by to zrobić". Ocena *subiektywna* dostępności zasobów, kompetencji, czasu, okazji.
- **To NIE jest:**
  - Obiektywna możliwość / rzeczywista wykonalność – C to ocena, nie fakt.
  - Self-efficacy (Bandura) – wiara w *zdolność do organizacji/wykonania* konkretnych działań; C to szersza ocena wykonalności (w tym zasoby zewnętrzne).
  - Perceived Behavioral Control (Ajzen) – PBC = mieszanka self-efficacy i kontroli środowiskowej; C bliższe PBC, ale binarne/uproszczone.
  - Capability (COM-B) – tylko komponent wewnętrzny (psychologiczny/fizyczny); C zawiera też Opportunity.
  - Opportunity (COM-B) – tylko komponent zewnętrzny; C to synteza obu.

### 3.2. Definicja operacyjna (wersja ciągła – bazowa)

**Item główny (EMA, skala 1–7):**
> "W jakim stopniu uważasz, że **jesteś w stanie to zrealizować / widzisz sposób na to, by to zrobić** (posiadasz kompetencje, czas, zasoby, okazję)?"
> 1 – Wcale nie jestem w stanie / nie widzę sposobu  
> 4 – Częściowo / nie mam pewności  
> 7 – Pełnie jestem w stanie / jasno widzę sposób

**Dodatkowe itemy:**
1. "Posiadam potrzebne kompetencje/umiejętności." (Competence)
2. "Mam wystarczająco czasu i zasobów." (Resources/Opportunity)
3. "Nie ma przeszkód, których nie mogę przełamać." (Perceived barriers – odwrotnie)

### 3.4. Kodowanie binarne
- **C = 1** jeśli średnia ≥ 4
- **C = 0** jeśli średnia < 4

### 3.5. Przypadki brzegowe

| Sytuacja | C (ciągłe) | C (binarne) | Uwagi |
|----------|------------|-------------|-------|
| "Umiem, ale nie mam czasu" | 3–4 | 0/4 | C odzwierciedla *syntezę* – brak czasu obniża C |
| "Mam czas, ale nie umiem" | 3–4 | 0/4 | Brak kompetencji obniża C |
| "Mogę, ale boję się niepowodzenia (lęk)" | 4–5 | 1 | Lęk nie = brak wykonalności (choć może obniżać C) |
| "Obiektywnie niemożliwe, ale uważam, że dam radę" | 6–7 | 1 | C = subiektywna ocena (może być błędna) |
| "Obiektywnie możliwe, ale uważam, że nie dam rady" | 2–3 | 0 | C = subiektywna ocena (może być błędna) |

### 3.6. Wskaźniki referencyjne
| Konstrukt referencyjny | Skala | Oczekiwana korelacja z C |
|------------------------|-------|---------------------------|
| General Self-Efficacy (GSE) | Schwarzer & Jerusalem | Umiarkowana (r ~ 0.5) |
| Perceived Behavioral Control (TPB) | TPB items | Wysoka (r > 0.6) – najbliższy |
| Capability (COM-B/TDF) | TDF items | Umiarkowana (tylko część wewnętrzna) |
| Opportunity (COM-B/TDF) | TDF items | Umiarkowana (tylko część zewnętrzna) |
| Task-specific Self-Efficacy | Specyficzne itemy | Wysoka (dla konkretnego zadania) |

---

## 4. Wymiar N – POWINIENEM (Poczucie zobowiązania normatywnego)

### 4.1. Definicja teoretyczna
**N = Poczucie zobowiązania normatywnego wobec realizacji celu.**

- **To jest:** Doświadczenie "powinienem to zrobić" / "to moje zobowiązanie". Poczucie presji normatywnej (wewnętrznej lub zewnętrznej) do realizacji celu.
- **To NIE jest:**
  - Zakaz (prohibition) – N=0 to brak obowiązku, nie zabronienie.
  - Norma społeczna (social norm) – tylko jeden źródło N (TPB: subjective norms).
  - Norma moralna (moral norm) – tylko jeden typ N (Schwartz: personal norm).
  - Obowiązek rolowy (role obligation) – tylko jeden typ N (Role theory).
  - Internalizacja (internalization) – to proces/jakość regulacji (N_source), nie bit N.
  - Presja społeczna (social pressure) – tylko jedno źródło (external).

### 4.2. Zmienne pomocnicze: Źródło i Jakość Obowiązku

Bit $N$ informuje **tylko o obecności/braku poczucia "powinienem"**. Źródło obowiązku i jakość regulacji to **dwie osobne zmienne**:

**1. Źródło obowiązku ($N_{source}$) – skąd wynika "powinienem":**
$$N_{source} \in \{
\text{external (presja zewnętrzna, oczekiwania innych)},
\text{moral (przekonania moralne, sumienie)},
\text{role (obowiązek rolowy, stanowiskowy)},
\text{legal (przepisy, prawo, regulamin)}
\}$$

**2. Jakość regulacji ($N_{quality}$) – jak jest doświadczany obowiązek (według SDT/Kelman):**
$$N_{quality} \in \{
\text{external (compliance, tylko presja zewnętrzna)},
\text{introjected (wewnętrzna presja, winę, lęk)},
\text{identified (uznana wartość, osobista zgoda)},
\text{integrated (zintegrowane z tożsamością, autonomiczne)}
\}$$

**Kluczowa zasada:** Internalizacja normy to zmiana $N_{quality}$ (np. external → identified), a **nie** koniecznie zmiana $N$ z 1 na 0. Osoba może mieć $N=1$ z $N_{quality}=\text{identified}$ (dobrowolnie przyjęty obowiązek) LUB $N=1$ z $N_{quality}=\text{external}$ (presja zewnętrzna). Obie to $N=1$, ale różna jakość regulacji.

### 4.3. Definicja operacyjna (wersja ciągła – bazowa)

**Item główny (EMA, skala 1–7):**
> "W jakim stopniu czujesz, że **powinieneś to zrobić / to jest Twoje zobowiązanie**?"
> 1 – Wcale nie czuję zobowiązania  
> 4 – Częściowo / nie mam zdania  
> 7 – Czuję silne zobowiązanie / silne "powinienem"

**Item dodatkowy 1 (źródło – $N_{source}$, kategoryczny):**
> "Skąd wynika Twoje poczucie, że powinieneś to zrobić? (Wybierz jedno główne)"
> 1. Presja zewnętrzna / oczekiwania innych (external)
> 2. Moje przekonania moralne / sumienie (moral)
> 3. Moja rola / stanowisko / funkcja (role)
> 4. Przepisy / prawo / regulamin (legal)

**Item dodatkowy 2 (jakość regulacji – $N_{quality}$, kategoryczny):**
> "Jak doświadczasz tego obowiązku? (Wybierz jedno)"
> 1. Tylko dlatego, że inni oczekują / każą (external)
> 2. Czuję winę/lęk, jeśli nie zrobię (introjected)
> 3. Osobiście uważam, to jest wartościowe / słuszne (identified)
> 4. To część moich wartości i tożsamości (integrated)

### 4.4. Kodowanie binarne
- **N = 1** jeśli średnia itemu głównego ≥ 4
- **N = 0** jeśli średnia < 4

### 4.5. Przypadki brzegowe i kodowanie

| Sytuacja | N (binarne) | $N_{source}$ | $N_{quality}$ | Uwagi |
|----------|-------------|--------------|---------------|-------|
| "Muszę, bo szef kazał, ale nie chcę" | 1 | external | external | Compliance |
| "Czuję winę, jak nie zrobię, choć nikt nie każe" | 1 | external/moral | introjected | Presja wewnętrzna |
| "Uważam, że to jest dobre i warto, więc powinienem" | 1 | moral | identified | Zidentyfikowana regulacja |
| "To jest częścią moich wartości, to ja jestem" | 1 | moral/role | integrated | Zintegrowana regulacja |
| "Moje sumienie mi nakazuje / moja moralność" | 1 | moral | identified/integrated | Norma moralna |
| "To moja rola/funkcja, muszę to robić" | 1 | role | identified/integrated | Obowiązek rolowy |
| "Prawo/przepis mi nakazuje" | 1 | legal | external/identified | Obowiązek prawny |
| "Nikt nie każe, nie czuję, że powinienem" | 0 | (brak) | (brak) | Brak obowiązku |

### 4.6. Rozwiązanie sprzeczności 110 vs 111

| Stan | W | C | N | Interpretacja $N_{source}$ / $N_{quality}$ |
|------|---|---|---|----------------------------|
| 110 | 1 | 1 | 0 | Brak poczucia "powinienem" LUB zinternalizowany obowiązek ($N_{quality}$=identified/integrated) który nie jest doświadczany jako "powinienem" (bo zinternalizowany = "chcę", nie "powinienem") |
| 111 | 1 | 1 | 1 | Poczucie "powinienem" obecne ($N_{source}$ dowolne, $N_{quality}$ dowolne) |

**Klucz:** $N=0$ w 110 **nie** oznacza "brak internalizacji". Może oznaczać: (a) brak kontekstu normatywnego, (b) zinternalizowany obowiązek który nie generuje poczucia "powinienem" (bo "chcę" zastępuje "powinienem").

### 4.7. Wskaźniki referencyjne
| Konstrukt referencyjny | Skala | Relacja z N / $N_{quality}$ |
|------------------------|-------|-----------------------------|
| Personal Norm (Schwartz) | PN scale | Korelacja z N przy $N_{source}$=moral |
| Subjective Norms (TPB) | SN scale | Korelacja z N przy $N_{source}$=external |
| Role Overload/Conflict (Kahn) | RCS | Korelacja z N przy $N_{source}$=role |
| Internalization (Kelman) | Kelman scale | Predyktor $N_{quality}$ (identified/integrated) |
| Moral Obligation (Ajzen) | MO scale | Korelacja z N przy $N_{source}$=moral |

---

## 5. Podsumowanie: Macierz operacjonalizacji

| Wymiar | Konstrukt (teoria) | Item główny (1–7) | Próg binarny | Wersja bazowa | Co NIE jest |
|--------|-------------------|-------------------|--------------|---------------|-------------|
| **W** | Osobista akceptacja wartości celu | "Akceptujesz wartość celu / zgadzasz się z realizacją?" | ≥4 → 1 | Ciągła 1–7 | Chęć, pragnienie, intencja, autonomia, motywacja intryntyczna |
| **C** | Subiektywnie oceniana wykonalność | "Jesteś w stanie to zrealizować / widzisz sposób?" | ≥4 → 1 | Ciągła 1–7 | Obiektywna możliwość, self-efficacy (tylko część), capability/opportunity (tylko części) |
| **N** | Poczucie zobowiązania normatywnego | "Czujesz, że powinieneś to zrobić / to Twoje zobowiązanie?" | ≥4 → 1 | Ciągła 1–7 | Zakaz, norma społeczna (tylko część), internalizacja (to $N_{source}$) |

**Zmienna pomocnicza:** $N_{source}$ (kategoryczna, 7 kategorii) – źródło/jakość obowiązku, niezależna od bitu $N$.

---

## 6. Wskazówki do pomiaru w EMA

1. **Losowa kolejność itemów** W, C, N w każdym pomiarze.
2. **Skala 1–7** z etykietami tylko na krańcach (1, 4, 7) – unikanie tendencji centralnej.
3. **Czas wypełnienia:** < 30 sekund (3 itemy główne + opcjonalnie $N_{source}$ co kilka pomiarów).
4. **Losowa kolejność pytań** W, C, N w każdym oknie pomiarowym.
5. **Event-based EMA:** Itemy W, C, N *przed* oknem zachowania (predyktory); pomiar po działaniu = skutek (wzrost C po sukcesie, spadek N po spełnieniu obowiązku).
6. **Wywiady poznawcze (cognitive interviewing)** na etapie pilotażu – weryfikacja zrozumienia itemów.

---

## 7. Zmiany względem wersji pierwotnej (rev1)

| Zmiana | Uzasadnienie |
|--------|--------------|
| W: "osobista akceptacja i motywacja" → "osobista akceptacja wartości celu" | Usunięcie utożsamienia z chęcią, pragnieniem, intencją, autonomią (B1) |
| C: "subiektywnie oceniana wykonalność" (bez zmian definicji, ale doprecyzowanie) | Jawne rozróżnienie: C ≠ obiektywna możliwość, C ≠ capability/opportunity COM-B (B3) |
| N: dodanie $N_{source}$ jako zmiennej pomocniczej; definicja N = "poczucie zobowiązania" (bez "internalizowanej") | Rozwiązanie sprzeczności 110 vs 111; internalizacja to $N_{source}$, nie bit N (B2) |
| Wersja ciągła (1–7) jako bazowa; binarna jako uproszczenie | Progowanie traci informację, generuje błędy klasyfikacji (C3) |
| Dodanie $N_{source}$ jako zmiennej pomocniczej (nie bitu) | Rozdzielenie kodu stanu od jakości regulacji (B2) |

---

*Dokument wersja 1.0. Gotowy do zastosowania w badaniu pilotażowym (Etap 2).*