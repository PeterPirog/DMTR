# Hipotezy Badawcze DMTRD

## Status: Specyfikacja do weryfikacji empirycznej (Etap 1)

---

## 1. Hipotezy ogólne (HG)

| Nr | Hipoteza | Zmienne | Metoda | Kryterium falsyfikacji |
|----|----------|---------|--------|------------------------|
| HG1 | Model 8-stanowy DMTRD lepiej dopasowuje dane EMA niż modele bez stanów (TPB, SDT, COM-B) | Dopasowanie modelu (AIC, BIC, log-likelihood) w LTA | LTA (Mplus/R) z 8 klasami, wskaźnikami ciągłymi | ΔAIC > 10 na korzyść modelu prostszego |
| HG2 | Hipoteza jednego bitu (HPE) jest empirycznie poparta – większość obserwowanych zmian w EMA to d_H=1; d_H≥2 są rzadkie lub wyjaśniane przez odstępy pomiarowe | Odsetek zmian d_H=1 vs d_H≥2 w sekwencjach EMA | Analiza sekwencji, test dwumianowy | Odsetek d_H≥2 > 15% przy gęstym EMA (co 30 min) |
| HG3 | Asymetria przejść odwrotnych jest istotna statystycznie – qᵢⱼ ≠ qⱼᵢ dla co najmniej 50% par | Intensywności przejść qᵢⱼ (CTMC) | Estymacja Q (CTMC), test LRT (H₀: qᵢⱼ = qⱼᵢ) | p > 0.05 dla >50% par po korekcie FDR |
| HG4 | Stan 101 operacjonalizuje moral distress – silna korelacja z istniejącymi skalami (MDS, Corley) i predykcja wypalenia/odejścia | Korelacja stan 101 (EMA) z MDS; HR dla wypalenia/odejścia | Walidacja kryterialna (korelacja), Cox regression | r < 0.3 z MDS; HR n.s. |
| HG5 | Topologia Q3 ma wartość heurystyczną – generuje przewidywania niedostępne w modelach płaskich (specyficzność 101, asymetria 111→011 vs 111→110) | Moc predykcyjna out-of-sample dla H1–H24 vs modele płaskie | Porównanie R², RMSE w walidacji krzyżowej | Brak przewagi predykcyjnej DMTRD |

---

## 2. Hipotezy szczegółowe dla 24 przejść (H1–H24)

Każda hipoteza ma strukturę: **Przejście → Przewidywana zależność → Zmienne → Pomiar → Analiza → Czynniki zakłócające**

### H1: 000 → 100 (Pojawienie się motywacji / Inicjacja celu)
- **Przewidywanie:** Wzrost outcome expectancies (SCT) i self-efficacy (SCT/TPB) przewiduje przejście 000→100.
- **Zmienne:** W (binarna/ciągła), Outcome Expectancies (SCT, 1-7), Self-Efficacy (GSE, 1-7).
- **Pomiar:** EMA – itemy W + SCT/TPB skale referencyjne na początku i w trakcie.
- **Analiza:** Regresja logistyczna wielopoziomowa (przejście w następnym oknie czasowym ~ OE_t + SE_t).
- **Czynniki zakłócające:** Afekt pozytywny/negatywny, stres, kontekst sytuacyjny.

### H2: 100 → 000 (Utrata motywacji / Rezygnacja z celu)
- **Przewidywanie:** Niska self-efficacy i negatywne outcome expectancies przewidują rezygnację (100→000).
- **Zmienne:** W, Self-Efficacy, Outcome Expectancies, Goal Disengagement (Wrosch).
- **Pomiar:** EMA + kwestionariusz Wrosch na początku.
- **Analiza:** Analiza przeżycia (Cox regression) – czas do rezygnacji ~ SE + OE + GD.
- **Czynniki zakłócające:** Nowe cele, zdarzenia życiowe, depresja.

### H3: 001 → 101 (Internalizacja obowiązku / Przejęcie odpowiedzialności)
- **Przewidywanie:** Perceived Autonomy Support (SDT) mediuje przejście 001→101 (internalizacja N→W).
- **Zmienne:** W, N, Perceived Autonomy Support (mPAS, 1-7), Identified Regulation (SDT).
- **Pomiar:** EMA – itemy W,N + mPAS co 2-3 dni.
- **Analiza:** Mediacja wielopoziomowa (001→101 ~ PAS → Identified Regulation → W).
- **Czynniki zakłócające:** Presja kontrolująca, brak wsparcia, wypalenie.

### H4: 101 → 001 / 011 (Dezengażowanie przy obowiązku)
- **Przewidywanie:** Brak perceived control → 101→001 (rezygnacja z W); silne normy społeczne → 101→011 (compliance bez W).
- **Zmienne:** W, N, Perceived Control, Subjective Norms (TPB), Social Pressure.
- **Pomiar:** EMA – itemy W,N + PC + SN.
- **Analiza:** Regresja multinomialna (kategoria przejścia: 001 vs 011 vs inne ~ PC + SN).
- **Czynniki zakłócające:** Wypalenie, dostępność zasobów, alternatywy.

### H5: 010 → 110 (Aktywacja potencjału / Przejęcie inicjatywy)
- **Przewidywanie:** Motywacja intryntyczna (IMI) i Autonomy Support przewidują 010→110.
- **Zmienne:** W, C, Intrinsic Motivation (IMI Interest/Enjoyment), Autonomy Support.
- **Pomiar:** EMA – itemy W,C + IMI + AS.
- **Analiza:** SEM (010→110 ~ IM + AS → W).
- **Czynniki zakłócające:** Lęk przed odpowiedzialnością, perfekcjonizm, brak wyzwań.

### H6: 110 → 010 (Utrata autonomicznej motywacji / Wypalenie od pasji)
- **Przewidywanie:** Niskie Autonomy Support przewiduje 110→010.
- **Zmienne:** W, C, Autonomy Support, Burnout (MBI), Job Demands/Resources.
- **Pomiar:** EMA – itemy W,C + AS + MBI co tydzień.
- **Analiza:** Cox regression (czas do 110→010 ~ AS + Burnout + Demands).
- **Czynniki zakłócające:** Rutyna, brak rozwoju, toksyczne środowisko.

### H7: 011 → 111 (Internalizacja obowiązku / Autonomizacja compliance)
- **Przewidywanie:** Perceived Autonomy Support i Identified Regulation mediują 011→111.
- **Zmienne:** W, C, N, Autonomy Support, Identified Regulation (SDT).
- **Pomiar:** EMA – itemy W,C,N + AS + IR.
- **Analiza:** Mediacja longitudinalna (011→111 ~ AS → IR → W).
- **Czynniki zakłócające:** Presja kontrolująca, lęk, brak kompetencji.

### H8: 111 → 011 (Utrata autonomii przy obowiązku – Dezautonomizacja)
- **Przewidywanie:** 111→011 silniej predykuje wypalenie niż 111→110 (utrata W vs N).
- **Zmienne:** W, C, N, Burnout (MBI), Autonomy Support, Job Demands.
- **Pomiar:** EMA – itemy W,C,N + MBI co tydzień.
- **Analiza:** Analiza ryzyka proporcjonalnego (Cox) – wypalenie ~ typ przejścia (011 vs 110) + kontrolne.
- **Czynniki zakłócające:** Wypalenie bazowe, toksyczne środowisko, konflikt ról.

### H9: 000 → 010 (Pojawienie się możliwości / Pozyskanie zasobów)
- **Przewidywanie:** Mastery Experience (Bandura) przewiduje 000→010.
- **Zmienne:** C, Mastery Experience (SCT), Vicarious Experience, Verbal Persuasion.
- **Pomiar:** EMA – itemy C + ME (krótkie itemy po zadaniach).
- **Analiza:** Analiza sekwencji EMA – ME_t → C_{t+1} (regresja logistyczna).
- **Czynniki zakłócające:** Brak czasu, lęk przed nauką, brak wsparcia.

### H10: 010 → 000 (Utrata możliwości / Utrata zasobów)
- **Przewidywanie:** Utrata C bez W/N mniej stresogenna niż 110→100 lub 111→101.
- **Zmienne:** C, W, N, Afekt (PANAS), Stres (PSS).
- **Pomiar:** EMA – itemy C,W,N + PANAS + PSS.
- **Analiza:** Porównanie średnich PANAS/PSS w oknach po 010→000 vs 110→100 vs 111→101 (ANOVA/regresja).
- **Czynniki zakłócające:** Stres ogólny, zdarzenia życiowe.

### H11: 001 → 011 (Pozyskanie możliwości do obowiązku / Empowerment)
- **Przewidywanie:** Perceived Organizational Support (POS) przewiduje 001→011.
- **Zmienne:** C, N, POS (Eisenberger), Resources, Training Access.
- **Pomiar:** EMA – itemy C,N + POS co tydzień.
- **Analiza:** Cross-lagged panel model (POS_t → C_{t+1} przy N=1).
- **Czynniki zakłócające:** Złożoność zadań, brak czasu, biurokracja.

### H12: 011 → 001 (Utrata możliwości przy obowiązku / Dezempowerment)
- **Przewidywanie:** 011→001 silniej predykuje intencję odejścia z pracy niż 011→010.
- **Zmienne:** C, N, Turnover Intention, POS, Resources.
- **Pomiar:** EMA – itemy C,N + Turnover Intention co tydzień.
- **Analiza:** Regresja logistyczna (Turnover Intention ~ typ przejścia 001 vs 010 + kontrolne).
- **Czynniki zakłócające:** Alternatywy rynkowe, wiek, staż.

### H13: 100 → 110 (Pozyskanie możliwości do celu / Przełamanie barier)
- **Przewidywanie:** Implementation Intentions (Gollwitzer) mediują 100→110 (planowanie → działanie).
- **Zmienne:** C, W, Implementation Intentions (II), Action Planning.
- **Pomiar:** EMA – itemy C,W + II (krótkie itemy "jeśli X to Y").
- **Analiza:** Mediacja (100→110 ~ II → C).
- **Czynniki zakłócające:** Bariery systemowe, brak kapitału, konkurencja.

### H14: 110 → 100 (Utrata możliwości przy autonomicznej motywacji / Blokada)
- **Przewidywanie:** 110→100 częściej prowadzi do persistencji (100→110) niż rezygnacji (100→000).
- **Zmienne:** C, W, Persistence, Goal Reengagement (Wrosch).
- **Pomiar:** EMA – sekwencje stanów 110→100→... (analiza trajektorii).
- **Analiza:** Analiza sekwencji stanów – odsetek 100→110 vs 100→000 po 110→100.
- **Czynniki zakłócające:** Ryzyko, niepewność, brak zasobów rezerwowych.

### H15: 101 → 111 (Rozwiązanie konfliktu / Przełamanie barier przy motywacji i obowiązku)
- **Przewidywanie:** Problem-focused Coping i Social Support przewidują 101→111.
- **Zmienne:** C, W, N, Coping (Brief COPE), Social Support (MSPSS).
- **Pomiar:** EMA – itemy C,W,N + COPE + MSPSS co tydzień.
- **Analiza:** SEM (101→111 ~ PFC + SS → C).
- **Czynniki zakłócające:** Bariery systemowe, wypalenie, brak wsparcia.

### H16: 111 → 101 (Utrata możliwości przy pełnej gotowości / Kryzys zasobów)
- **Przewidywanie:** 111→101 silniej predykuje ostre stresowe reakcje (PTSD, ostry stres) niż inne utraty C.
- **Zmienne:** C, W, N, Acute Stress (ASDS), PTSD (PCL-5), Burnout.
- **Pomiar:** EMA – itemy C,W,N + ASDS/PCL-5 po zdarzeniu kryzysowym.
- **Analiza:** Porównanie wskaźników stresu po 111→101 vs 111→110 vs 111→011 (ANOVA/regresja).
- **Czynniki zakłócające:** Historia traum, wsparcie społeczne, rezylencja.

### H17: 000 → 001 (Pojawienie się obowiązku / Przyjęcie odpowiedzialności)
- **Przewidywanie:** Internalizacja (→101) vs compliance (→011) rozróżnialne przez Autonomy Support.
- **Zmienne:** N, W, Autonomy Support, Internalization (Kelman).
- **Pomiar:** EMA – itemy N,W + AS + Internalization.
- **Analiza:** Regresja multinomialna z interakcją (001→101 vs 001→011 vs inne ~ AS × Internalization).
- **Czynniki zakłócające:** Ambiguitet roli, brak wsparcia, presja społeczna.

### H18: 001 → 000 (Utrata obowiązku / Odrzucenie roli)
- **Przewidywanie:** Role Ambiguity i niskie Role Commitment przewidują 001→000.
- **Zmienne:** N, Role Ambiguity, Role Commitment, Role Overload.
- **Pomiar:** EMA – itemy N + RA/RC/RO co tydzień.
- **Analiza:** Cox model (czas do 001→000 ~ RA + RC + RO).
- **Czynniki zakłócające:** Lojalność, strach przed wykluczeniem, alternatywy.

### H19: 010 → 011 (Narzucony obowiązek przy możliwości / Compliance enablement)
- **Przewidywanie:** 010→011 przy niskim Autonomy Support przewiduje 011→001 (rezygnacja z C), nie 011→111.
- **Zmienne:** N, C, Autonomy Support, Compliance.
- **Pomiar:** EMA – sekwencje 010→011→... (analiza trajektorii z moderacją AS).
- **Analiza:** Regresja logistyczna z interakcją (następny stan po 011 ~ AS × typ 010→011).
- **Czynniki zakłócające:** Autonomia, sens, kompetencja.

### H20: 011 → 010 / 001 (Utrata obowiązku przy możliwości / Deregulacja)
- **Przewidywanie:** Wysoka autonomia → 011→010 (wolność); niska autonomia → 011→001 (bezsilność).
- **Zmienne:** N, C, Autonomy, Empowerment.
- **Pomiar:** EMA – itemy N,C + Autonomy + Empowerment.
- **Analiza:** Regresja multinomialna z moderacją (następny stan ~ Autonomy).
- **Czynniki zakłócające:** Lęk przed odpowiedzialnością, brak alternatyw.

### H21: 100 → 101 (Pojawienie się obowiązku przy celu / Moralizacja celu)
- **Przewidywanie:** Personal Norm (Schwartz) → 101→111; Subjective Norms (TPB) → 101→001.
- **Zmienne:** N, W, Personal Norm (Schwartz), Subjective Norms (TPB), Moral Obligation (Ajzen).
- **Pomiar:** EMA – itemy N,W + PN + SN + MO.
- **Analiza:** Regresja multinomialna z moderacją (następny stan po 101 ~ PN vs SN).
- **Czynniki zakłócające:** Konflikt wartości, lęk, presja społeczna.

### H22: 101 → 100 (Utrata obowiązku przy motywacji / Sekularyzacja celu)
- **Przewidywanie:** Wysoka identyfikacja z celem (W) przy 101→100 zapobiega 100→000.
- **Zmienne:** N, W, Goal Identification, Goal Commitment.
- **Pomiar:** EMA – itemy N,W + GI + GC.
- **Analiza:** Regresja logistyczna z interakcją (100→000 po 101→100 ~ W × N change).
- **Czynniki zakłócające:** Lojalność, tradycja, presja normatywna.

### H23: 110 → 111 (Pojawienie się obowiązku przy autonomii / Odpowiedzialność społeczna)
- **Przewidywanie:** Organizational Identification i Prosocial Motivation przewidują 110→111 (OCB).
- **Zmienne:** N, W, C, Org Identification (Mael & Ashforth), Prosocial Motivation (Grant).
- **Pomiar:** EMA – itemy N,W,C + OI + PM co tydzień.
- **Analiza:** SEM (110→111 ~ OI + PM → N).
- **Czynniki zakłócające:** Konflikt wartości, lęk, presja grupowa.

### H24: 111 → 110 (Utrata obowiązku przy pełnej gotowości / Dezobowiązkowanie)
- **Przewidywanie:** Planowana sukcesja przy 111→110 nie predykuje wypalenia; 111→011 tak.
- **Zmienne:** N, W, C, Succession Planning, Burnout, Role Exit Quality.
- **Pomiar:** EMA – itemy N,W,C + SP + Burnout + REQ.
- **Analiza:** Porównanie trajektorii wypalenia po 111→110 (z SP) vs 111→011 (bez SP) – Cox/SEM.
- **Czynniki zakłócające:** Lojalność, tożsamość z rolą, nieplanowana utrata roli.

---

## 3. Specyfikacja metodologiczna wspólna

### Pomiar W, C, N (EMA)
- **Wersja binarna (dla LTA):** 3 itemy tak/nie na wymiar (np. "Czy osobiście chcę to zrobić? Tak/Nie").
- **Wersja ciągła (dla SEM/regresji/CTMC):** Skale Likert 1–7 dla każdego wymiaru (np. W: "W jakim stopniu osobiście chcę to zrobić? 1–7").
- **Czas wypełnienia:** < 30 sekund (12 itemów łącznie).
- **Losowa kolejność itemów.**

### Pomiar zachowania
- Samoraport: "Czy wykonałeś działanie od ostatniego pomiaru?" (tak/nie) + czas trwania/intensywność.
- Opcjonalnie obiektywne: akcelerometr (aktywność fizyczna), logi aplikacji (nauka), systemy CRM (praca).

### Częstotliwość EMA
- Losowe: 5×/dzień (9:00–21:00), odstępy ~2–3h.
- Event-based: do 1h po działaniu (max 3/dzień).
- Całkowity czas: 14–21 dni.
- Łącznie ~100–150 pomiarów/osoba.

### Analiza statystyczna
1. **LTA (Mplus/R):** 8 klas, wskaźniki ciągłe, macierz przejść P. Test HPE: pᵢⱼ=0 dla d_H≥2.
2. **CTMC (msm/ctmcm w R):** Estymacja Q z danych panelowych. Test asymetrii: qᵢⱼ ≠ qⱼᵢ (LRT).
3. **Regresje logistyczne wielopoziomowe (lme4/brms):** Przewidywanie przejść (H1–H24).
4. **SEM (lavaan/Mplus):** Mediacje (H3, H7, H13, H15, H23).
5. **Analiza przeżycia (survival):** Cox regression (H2, H6, H8, H12, H18, H24).
5. **Analiza sekwencji / trajektorii:** TraMineR / seqHMM (H4, H14, H19, H24).

### Walidacja trafności konstruktu
- CFA: 3 czynniki (W,C,N) – CFI>0.95, RMSEA<0.06, SRMR<0.08.
- Dyskryminacyjna: AVE > kwadrat korelacji między czynnikami (Fornell-Larcker).
- Kryterialna: Korelacje ze skalami referencyjnymi (IMI, GSE, MDS, POS, MBI).

### Walidacja trafności predykcyjnej
- Przewidywanie zachowania (następny pomiar) ze stanu (bieżący pomiar).
- Porównanie z TPB (intencja→zachowanie), SDT (typy regulacji), COM-B (M,O,A), Rubikon (fazy).
- Kryteria: AIC, BIC, R², moc predykcyjna out-of-sample (walidacja krzyżowa).

### Analiza mocy
- Symulacja Monte Carlo (N=100–500, T=50–150, efekty małe/średnie/duże).
- Cel: moc > 0.80 dla testów HPE (d_H≥2), asymetrii (qᵢⱼ≠qⱼᵢ), mediacji (H3, H7).
- Plan: 1000 replikacji, raportowanie mocy dla różnych N, T, wielkości efektu.

---

## 4. Czynniki zakłócające (ogólne)

| Czynnik | Opis | Kontrola |
|---------|------|----------|
| Reaktywność pomiaru | EMA zmienia stan motywacyjny (self-monitoring effect) | Grupa kontrolna bez EMA / tylko event-based; analiza trendów w czasie |
| Selekcja próby | Uczestnicy zmotywowani do udziału w badaniu | Rekrutowanie różnorodne; analiza nierespondentów |
| Pamięć/retrospekcja | Błędy w samoraporcie zachowania | Event-based EMA (do 1h po działaniu); dane obiektywne gdzie możliwe |
| Kontekst sytuacyjny | Stres, afekt, zdarzenia życiowe modyfikują stany | Pomiar PANAS, PSS, zdarzeń życiowych w EMA; kontrola statystyczna |
| Nawyk/automatyzm | System 1 nie modelowany w DMTRD | Krótkie itemy nawyku (SRHI) w EMA; analiza podgrup (nawykowe vs nienawykowe) |
| Różnice indywidualne | Cechy osobowości, cechy demograficzne | Kontrola: Big Five, wiek, płeć, wykształcenie, staż |
| Sezonowość/tydzień | Wzorce cykliczne motywacji | Efekty losowe dla dnia tygodnia, tygodnia badania |

---

## 5. Plan symulacji mocy (do wykonania przed Etapem 3)

1. **Generowanie danych:** CTMC z Q (z literatury / eksperci) dla N=100, 200, 300, 500; T=50, 100, 150.
2. **Efekty:** Małe (OR=1.5), średnie (OR=2.5), duże (OR=4.0) dla przejść kluczowych (H1, H3, H7, H8, H15).
3. **Modele do testowania:** LTA (8 klas), CTMC (Q), Regresje logistyczne wielopoziomowe.
4. **Testy:** HPE (d_H≥2), Asymetria (qᵢⱼ≠qⱼᵢ), Mediacja (H3, H7), Predykcja zachowania.
5. **Replikacje:** 1000 per warunek.
6. **Output:** Tabele mocy dla każdego testu × N × T × wielkość efektu.
6. **Decyzja:** Minimalne N i T dla mocy >0.80 przy efekcie średnim.

---

*Dokument wersja 1.0. Wymaga weryfikacji przez recenzenta przed Etapem 2 (walidacja psychometryczna).*