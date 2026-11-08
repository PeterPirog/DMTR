# Pytania do Niezależnego Recenzenta – DMTRD rev3.1

**Wersja modelu:** 3.1 (kanoniczna)  
**Data:** 08.11.2026  
**Commit:** ac00b7037a5f607ddf876225a75aeebbcd9ef9cb

---

## Instrukcja

Prosimy o ocenę poniższych kwestii. **Nie sugerujemy oczekiwanej pozytywnej oceny.** Każda uwaga, krytyka lub sugestia jest cenną. Prosimy o wskazanie numeru pytania przy odpowiedzi.

---

## 1. Trafność rozróżnienia W, C, N

**Pytanie:** Czy trzy konstrukty (W – chęć, C – przekonanie o możliwości, N – racjonalne przekonanie o konieczności) są psychometrycznie odseparowywalne?

**Kontekst:** W literaturze motywacji te konstrukty często nachodzą na siebie (np. postawa w TPB, self-efficacy w SCT, normy subiektywne w TPB, regulacje w SDT). DMTRD postuluje ich niezależność binarną.

**Prosimy o ocenę:**
- Czy definicje kanoniczne (W = chęć, C = przekonanie o możliwości, N = racjonalne przekonanie o konieczności) są wystarczająco ostre?
- Czy binarna operacjonalizacja nie traci istotnej informacji (typy motywacji, gradacja self-efficacy, kategorie norm)?
- Czy wersja ciągła (oktaanty w [0,1]³) nie byłaby bardziej adekwatna jako model bazowy do estymacji?

---

## 2. Znaczenie binarności

**Pytanie:** Czy utrata wariancji wynikająca z binarności jest akceptowalna na etapie koncepcyjnym?

**Kontekst:** Wszystkie teorie referencyjne (TPB, SDT, SCT, Goal-Setting, COM-B) używają skal ciągłych. DMTRD rdzeń to 8 stanów binarnych.

**Prosimy o ocenę:**
- Czy redukcja do 8 stanów jest heurystycznie użyteczna (topologia Q3, HPE, asymetria)?
- Czy utrata informacji o natężeniu (typy motywacji, gradacja self-efficacy, kategorie norm) uniemożliwia sensowne przewidywania?
- Czy wersja ciągła powinna być modelem bazowym, a binarna uproszczeniem do interpretacji?

---

## 3. Interpretacja ośmiu stanów

**Pytanie:** Czy interpretacje stanów 001, 011, 101, 110, 111 są teoretycznie uzasadnione i empirycznie rozróżnialne?

**Kontekst:** Stan to konfiguracja (W,C,N), nie zachowanie ani emocja. Kluczowe stany:

| Stan | Kod | Opis kanoniczny |
|------|-----|-----------------|
| Tylko powinność | 001 | Przekonanie o konieczności bez chęci i możliwości |
| Działanie bez zgody | 011 | Możliwość + konieczność bez chęci |
| Silne napięcie | 101 | Chęć + konieczność bez możliwości |
| Gotowość z inicjatywy | 110 | Chęć + możliwość bez konieczności |
| Pełna gotowość | 111 | Chęć + możliwość + konieczność (nie zawsze optymalna) |

**Prosimy o ocenę:**
- Czy stan 011 ("działanie bez wewnętrznej zgody") jest odseparowywalny od "compliance" (SDT) i "przymusu"?
- Czy stan 101 ("silne napięcie motywacyjne") jest odseparowywalny od "moral distress" (hipoteza H_MD)?
- Czy stan 110 ("gotowość z inicjatywy") jest odseparowywalny od "motywacji autonomicznej" (SDT)?
- Czy stan 111 ("pełna gotowość") jest poprawnie oznaczony jako "nie zawsze optymalna" (jakość zależy od N_source)?
- Czy stan 000 ("spoczynek/brak przesłanek") jest odseparowywalny od apatii?

---

## 4. Przydatność 24 przejść i asymetria

**Pytanie:** Czy asymetria przejść odwrotnych generuje przewidywania różniące się od modeli płaskich (TPB, SDT, COM-B)?

**Kontekst:** Z 12 krawędzi nieskierowanych Q3 powstaje 24 przejścia kierunkowe (d_H = 1). Kluczowe pary:

| Para | Przejście A | Przejście B | Różnica |
|------|-------------|-------------|---------|
| 011↔111 | Internalizacja (jakość) | Dezautonomizacja (wypalenie) | Wzrost vs utrata W przy N=1 |
| 001↔101 | Autonomizacja (nadzieja) | Dezengażowanie (bezsilność) | Wzrost vs utrata W przy N=1 |
| 101↔111 | Rozwiązanie konfliktu (olga) | Kryzys zasobów (PTSD) | Wzrost vs utrata C przy W+N |
| 110↔111 | OCB (dumą, sens) | Dezobowiązkowanie (ulga) | Wzrost vs utrata N przy W+C |
| 111↔110 | Sukcesja (adaptacyjne) | Wypalenie (groźne) | Planowana utrata N vs utrata W |

**Prosimy o ocenę:**
- Czy asymetria (np. 011→111 vs 111→011) generuje testowalne przewidywania?
- Czy topologia Q3 ma wartość heurystyczną ponad estetykę?
- Czy HPE-model (qᵢⱼ = 0 dla d_H ≥ 2) jest sensownym ograniczeniem na strukturę generatora CTMC?

---

## 5. Mechanizm racjonalnej zmiany N (przejścia N:1→0)

**Pytanie:** Czy interpretacja przejść N:1→0 (001→000, 011→010, 101→100, 111→110) jako "ponownej racjonalnej oceny zasadności działania względem własnych celów" jest psychologicznie sensowna i odseparowywalna od redukcji stresu/ucieczki?

**Kontekst:** DMTRD odseparowuje:
- **Logikę bitową:** N zmienia się 1→0
- **Mechanizm psychologiczny:** ponowna racjonalna ocena konieczności (delegacja, sukcesja, sekularyzacja, deregulacja)
- **Konsekwencje:** mogą być adaptacyjne LUB nieadaptacyjne – zależy od kontekstu
- **NIE:** automatyczna redukcja stresu, ucieczka, uwolnienie emocjonalne

**Prosimy o ocenę:**
- Czy to rozróżnienie jest psychologicznie sensowne?
- Czy da się to zoperacjonalizować w badaniu EMA (np. pytania o przyczyny zmiany przekonania o konieczności)?
- Czy istnieje ryzyko, że badani będą interpretować utratę N jako "ucieczkę"?

---

## 6. Rozróżnienie motywacji (stanu) i zachowania

**Pytanie:** Czy model jasno oddziela stan motywacyjny (W,C,N) od faktycznego zachowania?

**Kontekst:** DMTRD opisuje stan motywacyjny, nie deterministycznie zachowanie. Związek jest prawdopodobieństwowy i zmodulowany przez volicję, kontekst, nawyki, zasoby.

**Prosimy o ocenę:**
- Czy rozróżnienie "stan ≠ zachowanie" jest wyraźnie komunikowane?
- Czy brak mechanizmu stan → zachowanie (intencja, volicja) to krytyczna luka teoretyczna?
- Czy dodanie 4. wymiaru I (Intencja) lub A (Działanie) jest konieczne lub wystarczy modelowanie probabilistyczne (CTMC/LTA)?

---

## 7. Ograniczenia modelu

**Pytanie:** Czy wskazane ograniczenia są kompletne i adekwatnie opisane?

**Lista ograniczeń (z dokumentu):**
1. Binarność traci wariancję
2. Brak intencji i celu
3. Pomijanie automatyzmu/nawyku (System 1)
4. N miesza kategorie normatywnych
5. Identyfikowalność statystyczna (saturated model w LTA)
6. HPE to hipoteza, nie fakt
7. Stan 111 nie zawsze optymalny
8. Brak walidacji empirycznej

**Prosimy o ocenę:**
- Czy lista jest kompletna?
- Czy opis ograniczeń jest rzetelny (nie zaniżany, nie przesadzany)?
- Czy wskazane kierunki rozszerzeń (wersja ciągła, 4. wymiar I, parametr H, podwymiary N) są właściwe?

---

## 8. Potencjalna wartość naukowa DMTRD

**Pytanie:** Czy DMTRD wnosi nową treść teoretyczną nad to, co zawarte w MOA, COM-B, TPB, SDT, Rubikon?

**Kandydaty na nowość:**
- Topologia Q3 (8 stanów, 12 krawędzi, 24 przejścia)
- HPE-model (qᵢⱼ = 0 dla d_H ≥ 2) jako ograniczenie na generator CTMC
- N jako niezależny wymiar binarny (nie redukowany do norm subiektywnych TPB)
- Stan 101 (W=1, C=0, N=1) – konfiguracja napięcia motywacyjnego
- Asymetria przejść odwrotnych jako generowana przez topologię
- Rozróżnienie warstwy logicznej (kody) od psychologicznej (mechanizmy)

**Prosimy o ocenę:**
- Gdzie model jest tylko redukcją/renomowaniem istniejących idei?
- Gdzie wnosi nową treść teoretyczną lub metodologiczną?
- Czy wartość heurystyczna topologii Q3 przewyższa koszt binarności?

---

## Jak oddać odpowiedź

Prosimy o przesłanie uwag w dowolnej formie (plik tekstowy, komentarze w dokumencie, e-mail) z wskazaniem numerów pytań.

**Termin:** Do uzgodnienia.

**Kontakt:** Zgodnie z informacjami w repozytorium.

---

*Dziękujemy za poświęcony czas i merytoryczną ocenę.*