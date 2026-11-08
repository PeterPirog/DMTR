# Informacja dla Recenzenta – DMTRD rev3.1

**Data:** 08.11.2026  
**Wersja:** 3.1 (kanoniczna)  
**Commit:** ac00b7037a5f607ddf876225a75aeebbcd9ef9cb  
**Gałąź:** research/dmtrd-rev3-canonical  
**PR:** #3 (base: research/dmtrd-rev1-critical)

---

## 1. Co to jest DMTRD?

**Dynamiczny Model Trójwymiarowej Regulacji Działania (DMTRD)** to propozycja teoretyczna opisująca stan motywacyjny człowieka względem **konkretnego działania** za pomocą trzech wymiarów binarnych:

| Wymiar | Skrót | Definicja kanoniczna |
|--------|-------|---------------------|
| **W** | CHCĘ | Chęć wykonania konkretnego działania |
| **C** | MOGĘ | Subiektywne przekonanie o możliwości wykonania działania |
| **N** | POWINIENEM | Racjonalne przekonanie o konieczności wykonania działania ze względu na własne cele |

Każdy wymiar przyjmuje wartość 0 (brak) lub 1 (obecność). Tworzy to **8 stanów** (000–111), ułożonych w strukturę trójwymiarowego hipersześcianu **Q3**.

---

## 2. Status naukowy modelu

| Aspekt | Status |
|--------|--------|
| **Etap badawczy** | Etap 1 – Koncepualizacja i recenzja |
| **Walidacja empiryczna** | **NIE** – model nie jest zwalidowany empirycznie |
| **Spójność wewnętrzna** | ✅ Zweryfikowana automatycznie (0 błędów) |
| **Zgodność z kaninem** | ✅ Pełna (model/DMTRD_KANON_KONCEPCYJNY.md) |
| **Gotowość do konsultacji** | ✅ Tak – do niezależnej oceny merytorycznej |

**To nie jest teoria potwierdzona.** To propozycja koncepcyjna do testowania w Etapach 2-6 (EMA, eksperymenty, rozszerzenia).

---

## 3. Kluczowe założenia

1. **HPE-model (Hipoteza Przejść Elementarnych):** W generatorze CTMC intensywności przejść między stanami o odległości Hamminga d_H ≥ 2 są równe zero (qᵢⱼ = 0). Dozwolone są tylko 24 przejścia kierunkowe (d_H = 1).
2. **Asymetria przejść odwrotnych:** Np. 011→111 (internalizacja) to inny proces niż 111→011 (utrata autonomii/wypalenie).
3. **Stan ≠ zachowanie:** Model opisuje stan motywacyjny, nie deterministycznie zachowanie.
4. **N ≠ emocjonalna wina/presja:** N to racjonalne przekonanie o konieczności, nie emocja.
5. **Binarny rdzeń:** Wersje ciągłe, CTMC, LTA, 4. wymiar (Intencja), 5. wymiar (Działanie/Nawyk) to **rozszerzenia**, nie rdzeń.

---

## 4. Ograniczenia znane (nie rozwiązane w rev3.1)

1. Binarność traci wariancję (typy motywacji, gradacja self-efficacy, kategorie norm)
2. Brak intencji i celu (luka względem TPB, Rubikon, Goal-Setting)
3. Pomijanie automatyzmu/nawyku (System 1 – 40-50% działań)
4. N miesza kategorie normatywnych (moralne, rolowe, społeczne, zinternalizowane, eksternalne)
5. Identyfikowalność statystyczna – wersja binarna: saturated model (0 df) w LTA
6. HPE to hipoteza, nie fakt
7. Stan 111 nie zawsze optymalny (jakość zależy od N_source)
8. Brak walidacji empirycznej – Etap 1 koncepcyjny

---

## 5. Pliki w pakiecie recenzenckim

| Plik | Opis |
|------|------|
| `DMTRD_koncepcja_rev3_1.docx` | Główny dokument naukowy (pełna treść, 20 rozdziałów) |
| `DMTRD_streszczenie_dla_recenzenta_rev3_1.docx` | Streszczenie dla recenzenta (8 pytań) |
| `PYTANIA_DO_RECENZENTA.md` | Zestaw 8 pytań do niezależnego recenzenta |
| `INFO_DLA_RECENZENTA.md` | Ten plik |

---

## 6. Co NIE jest w modelu (by uniknąć nieporozumień)

- ❌ Nie ma intencji ani celu (to TPB/Rubikon)
- ❌ Nie ma automatyzmu/nawyku (to System 1, parametr H jako rozszerzenie)
- ❌ Nie ma jakości motywacji (to SDT – jakość regulacji)
- ❌ Nie ma deterministycznego mechanizmu stan → zachowanie
- ❌ Nie ma empirycznej walidacji (Etap 1 = koncepualizacja)

---

## 7. Kontakt

Projekt: DMTRD – Etap 1  
Repozytorium: https://github.com/PeterPirog/DMTR  
Gałąź: research/dmtrd-rev3-canonical  
PR: #3

Prosimy o ocenę merytoryczną zgodnie z pytaniami w `PYTANIA_DO_RECENZENTA.md`.