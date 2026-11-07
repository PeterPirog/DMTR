# Analiza Oryginalności DMTRD – Wersja rev1 (po rewizji ASTRA)

**Wersja:** 1.0  
**Data:** 07.11.2026  
**Status:** Analiza po rewizji krytycznej ASTRA  
**Cel:** Uczciwa ocena oryginalności DMTRD po rewizji krytycznej.

---

## 1. Metodologia oceny

Oryginalność oceniana w trzech kategoriach:

| Kategoria | Kryterium |
|-----------|-----------|
| **ORYGINALNOŚĆ UDOKUMENTOWANA** | Istnieje dowód (literatura, formalizm, dane) na nowość; nie znaleziono precedensu w literaturze do 11.2026. |
| **ORYGINALNOŚĆ POTENCJALNA** | Koncepcja ma cechy nowatorskie, ale wymaga weryfikacji empirycznej / formalnej; nie znaleziono precedensu, ale nie udowodniono unikalności. |
| **BRAK PODSTAW DO TWIERDZENIA O ORYGINALNOŚCI** | Element jest renomowaniem / redukcją istniejących koncepcji; znaleziono precedensy w literaturze. |

---

## 2. Szczegółowa analiza elementów DMTRD

### 2.1. Trzy wymiary (W, C, N) jako klasyfikacja binarna

| Ocena | **BRAK PODSTAW DO TWIERDZENIA O ORYGINALNOŚCI** |
|-------|--------------------------------------------------|
| **Uzasadnienie** | Podział na trzy determinaty działania (motywacja, możliwość, norma) występuje w: TPB (postawa, norma subiektywna, PBC), SDT (autonomia, kompetencja, powiązanie – choć to potrzeby), COM-B (motivation, capability, opportunity), MOA (motivation, opportunity, ability), Rubikon (motywacja, wykonalność, norma niejawnie). Trzy filary to **wspólny mianownik** teorii motywacji, nie nowość DMTRD. |
| **Wniosek** | Trzy wymiary to **renomowanie/agregacja** istniejących konstruktów. Nowość nie leży w samym podziale. |

### 2.2. Osiem stanów (Q3) jako przestrzeń stanów

| Ocena | **BRAK PODSTAW DO TWIERDZENIA O ORYGINALNOŚCI** |
|-------|--------------------------------------------------|
| **Uzasadnienie** | Przestrzeń $\{0,1\}^3$ = 8 stanów to prosta kombinatoryka. Q3 (hipersześcian 3-wymiarowy) to standardowy obiekt matematyczny. Użycie Q3 jako topologii stanów motywacyjnych nie jest nowe – np. modele wielostanowe w psychologii (LTA, HMM) używają dyskretnych stanów; CTBN (Nodelman et al., 2002) formalnie to ten sam formalizm dla 3 zmiennych binarnych. |
| **Wniosek** | Q3 jako topologia to **standardowy formalizm**, nie nowość. |

### 2.3. Hipoteza Przejść Elementarnych (HPE-model)

| Ocena | **ORYGINALNOŚĆ POTENCJALNA** |
|-------|------------------------------|
| **Uzasadnienie** | HPE-model jako **ograniczenie na generator Q** ($q_{ij}=0$ dla $d_H \geq 2$) to matematycznie to samo co **Continuous Time Bayesian Networks (CTBN)** dla 3 zmiennych binarnych z lokalnymi zmianami (Nodelman, Shelton, Koller, UAI 2002). CTBN to ogólny formalizm; DMTRD to jego **specjalizacja psychologiczna** z konkretnymi zmiennymi (W,C,N) i interpretacją parametrów. **Nowość potencjalna** leży w: (a) psychologicznym doborze zmiennych (W,C,N), (b) interpretacji asymetrii $q_{ij}$ jako różnych procesów psychologicznych, (c) testowalnych przewidywaniach interwencyjnych. |
| **Wniosek** | Formalizm HPE-model = CTBN (znany). **Nowość potencjalna** w zastosowaniu psychologicznym i interpretacji. |

### 2.4. Asymetria przejść odwrotnych ($q_{ij} \neq q_{ji}$)

| Ocena | **ORYGINALNOŚĆ POTENCJALNA** |
|-------|------------------------------|
| **Uzasadnienie** | Asymetria intensywności ($q_{ij} \neq q_{ji}$) jest standardową cechą CTMC/CTBN. **Nowość potencjalna** leży w: (a) psychologicznej interpretacji asymetrii jako różnych procesów (np. internalizacja vs dezautonomizacja), (b) powiązaniu asymetrii z mierzalnymi moderatorami (autonomia, wsparcie, afekt), (c) testowalnych przewidywaniach o różnicach w afekcie, wypaleniu, trwałości zmian. |
| **Wniosek** | Asymetria jako taka = znana. **Nowość potencjalna** w interpretacji psychologicznej i testach interwencyjnych. |

### 2.5. Zależność od historii (Path Dependence)

| Ocena | **ORYGINALNOŚĆ POTENCJALNA** |
|-------|------------------------------|
| **Uzasadnienie** | Zależność od drogi dojścia (np. różna stabilność 111 w zależności od ścieżki: budowanie autonomii vs internalizacja normy) jest znana w modelach rzędu wyższego, HMM z historią, CTMC z kowariancjami zależnymi od czasu. **Nowość potencjalna** w: (a) jawnej formułowaniu hipotezy HPD dla DMTRD, (b) powiązaniu z konkretnymi ścieżkami w Q3 (np. 000→100→110→111 vs 000→001→011→111), (c) testowalnych przewidywaniach o różnicach w stabilności, afekcie, trwałości. |
| **Wniosek** | Path dependence = znana w modelowaniu. **Nowość potencjalna** w zastosowaniu do Q3 i testach. |

### 2.6. Trzy wymiary z rozróżnieniem $N_{source}$

| Ocena | **ORYGINALNOŚĆ POTENCJALNA** |
|-------|------------------------------|
| **Uzasadnienie** | Rozróżnienie bitu $N$ (obecność poczucia "powinienem") od zmiennej $N_{source}$ (źródło/jakość regulacji: external, introjected, identified, integrated, moral, role, legal) to **rozwiązanie problemu** wewnątrz DMTRD, nie nowość teoretyczna *per se*. SDT (Deci & Ryan) rozróżnia typy regulacji; Kelman (1958) rozróżnia compliance/identification/internalization; Schwartz (1977) – normy moralne; Role theory – obowiązki rolowe. **Nowość potencjalna** w: (a) integracji tych rozróżnień w **jedną zmienną kategoryczną $N_{source}$** zintegrowaną z modelem dynamicznym (moderator $q_{ij}$), (b) jawnej separacji bitu $N$ (obecność/braku poczucia) od jakości regulacji ($N_{source}$), co rozwiązuje sprzeczność 110 vs 111. |
| **Wniosek** | Rozdzielenie $N$ i $N_{source}$ = **rozwiązanie problemu wewnątrz DMTRD**, elementy składowe znane z literatury. |

### 2.7. Stan 101 jako formalizacja napięcia (nie moral distress)

| Ocena | **ORYGINALNOŚĆ POTENCJALNA** |
|-------|------------------------------|
| **Uzasadnienie** | Stan 101 (W=1, C=0, N=1) jako **konfiguracja trzech ocen** (silna motywacja + obowiązek + brak wykonalności) to nowa **klasyfikacja konfiguracji**. Utożsamienie z *moral distress* (Jameton, Corley) jest **nieuzasadnione** (B6) – moral distress wymaga specyficznych warunków (moralny charakter, cierpienie, blokada moralnie właściwego działania). **Nowość potencjalna** w: (a) jawnej klasyfikacji 101 jako "stan napięcia krytycznego / blocked motivated obligation", (b) hipotezie H_MD: w kontekście moralnym 101 predysponuje do moral distress, (c) testowalnych przewidywaniach o różnicy 101 w kontekście moralnym vs administracyjnym. |
| **Wniosek** | Stan 101 jako konfiguracja = nowa klasyfikacja. Równość z moral distress = **nieuzasadniona**. |

### 2.8. Separacja kodu przejścia od mechanizmów (etykieta neutralna + hipotezy mechanistyczne)

| Ocena | **ORYGINALNOŚĆ UDOKUMENTOWANA** |
|-------|----------------------------------|
| **Uzasadnienie** | Jawna separacja trzech warstw w opisie przejścia: (1) **kod przejścia** (co się zmieniło – wynikający z bitów), (2) **etykieta neutralna** (np. "Zmiana W: 0→1 przy C=1, N=1"), (3) **lista hipotez mechanistycznych** (alternatywne wyjaśnienia z odsyłaczami do literatury). W literaturze psychologicznej modele dynamiczne (CTMC, HMM, LTA) zazwyczaj **utożsamiają** kod przejścia z interpretacją mechanistyczną (np. "internalizacja" jako nazwa przejścia 011→111). Jawna separacja warstw i jawne wymienienie alternatywnych mechanizmów to **dobra praktyka metodologiczna**, rzadko stosowana w sposób systematyczny. |
| **Wniosek** | **Nowość metodologiczna** – systematyczna separacja kodu, etykiety i hipotez mechanistycznych dla wszystkich 24 przejść. |

### 2.9. Model pomiarowy: stany obserwowane ciągłe + CTMC z kowariancjami

| Ocena | **ORYGINALNOŚĆ POTENCJALNA** |
|-------|------------------------------|
| **Uzasadnienie** | Wybór **stanów obserwowanych ciągłych (W,C,N ∈ [1,7])** zamiast klas latentnych w LTA/HMM to **rozsądny wybór metodologiczny** unikający problemu identyfikowalności (C2). CTMC z kowariancjami ($q_{ij}(X_t)$) to standardowa metoda (`msm` w R). **Nowość potencjalna** w: (a) spójnym połączeniu wersji ciągłej (do estymacji) z wersją binarną (do interpretacji Q3), (b) jawnej separacji ról zmiennych: stan (W,C,N) / predyktory (kowariancje) / outcomes (zachowanie, afekt), (c) jawnej specyfikacji modeli alternatywnych do porównania (M_full, M_indep, M_cont, M_meas). |
| **Wniosek** | Dobór metodologiczny = rozsądny, elementy składowe znane. **Nowość potencjalna** w spójnym zintegrowaniu. |

### 2.10. Redukcja hipotez do 3 głównych (HPE, HPD, HPP)

| Ocena | **ORYGINALNOŚĆ UDOKUMENTOWANA** |
|-------|----------------------------------|
| **Uzasadnienie** | Radikalna redukcja z 24 hipotez szczegółowych + 5 ogólnych do **3 hipotez głównych (HPE, HPD, HPP)** z zamkniętymi kryteriami odrzucenia, a reszta jako hipotezy eksploracyjne – to **dobra praktyka naukowa** (confirmatory vs exploratory), rzadko stosowana w psychologii motywacji w tak radykalnym stopniu. Większość prac prezentuje listę hipotez bez rozróżnienia confirmatory/exploratory. |
| **Wniosek** | **Nowość metodologiczna** – radykalna separacja confirmatory vs exploratory z zamkniętymi kryteriami odrzucenia wersji core. |

---

## 3. Tabela podsumowująca

| Element DMTRD | Ocena oryginalności | Uzasadnienie w skrócie |
|---------------|---------------------|------------------------|
| Trzy wymiary (W,C,N) | **BRAK PODSTAW** | Redukcja TPB/SDT/COM-B/MOA |
| Osiem stanów (Q3) | **BRAK PODSTAW** | Standardowa kombinatoryka / CTBN |
| HPE-model (ograniczenie Q) | **POTENCJALNA** | = CTBN (Nodelman et al., 2002); nowość w zastosowaniu psychologicznym |
| Asymetria $q_{ij} \neq q_{ji}$ | **POTENCJALNA** | Znana w CTMC; nowość w interpretacji psychologicznej |
| Path Dependence (HPD) | **POTENCJALNA** | Znana w modelach rzędu wyższego; nowość w zastosowaniu do Q3 |
| Rozdzielenie $N$ i $N_{source}$ | **POTENCJALNA** | Rozwiązanie problemu wewnątrz DMTRD; elementy składowe znane |
| Stan 101 jako konfiguracja | **POTENCJALNA** | Nowa klasyfikacja; równość z moral distress = nieuzasadniona |
| Separacja kodów/mechanizmów | **UDOKUMENTOWANA** | Nowość metodologiczna: systematyczna separacja 3 warstw |
| Model pomiarowy (ciągły + CTMC) | **POTENCJALNA** | Rozsądny dobór; nowość w spójnym zintegrowaniu |
| 3 hipotezy główne (HPE, HPD, HPP) | **UDOKUMENTOWANA** | Nowość metodologiczna: radykalna separacja confirmatory/exploratory |

---

## 4. Wnioski

### 4.1. Czy DMTRD jest "nową teorią"?

**Nie.** DMTRD w wersji rev1 **nie jest nową teorią motywacji** w sensie odkrycia nowych konstruktów psychologicznych ani nowego formalizmu matematycznego. Jej elementy składowe (trzy wymiary, Q3, CTMC, asymetria, path dependence) są znane z literatury.

### 4.2. Jaki jest wkład DMTRD?

Wkład DMTRD rev1 to **spójna integracja** znanych elementów w **jedną spójną ramę badawczą** z:

1. **Precyzyjnymi definicjami operacyjnymi** W, C, N (rozróżniając co NIE są).
2. **Jawną separacją** kodu przejścia, etykiety neutralnej i hipotez mechanistycznych (nowość metodologiczna).
3. **Radikalną separacją** hipotez potwierdzających (3 główne) od eksploracyjnych (nowość metodologiczna).
3. **Rozwiązaniem problemu** $N$ vs $N_{source}$ (rozwiązanie sprzeczności 110 vs 111).
4. **Spójnym modelem pomiarowym** (ciągły + CTMC + kowariancje) unikającym problemów identyfikowalności.
4. **Zamkniętą wersją core** (HPE, HPD, HPP) z jawymi kryteriami odrzucenia.

### 4.3. Gdzie leży wartość naukowa DMTRD?

Wartość DMTRD **nie** leży w nowości poszczególnych elementów, ale w ich **spójnej integracji** tworzącej **narzędzie badawcze** do:

- Testowania HPE jako ograniczenia dynamiki (HPE-test).
- Badania path dependence w regulacji motywacyjnej (HPD).
- Oceny wartości predykcyjnej topologii Q3 nad modele płaskie (HPP).
- Generowania specyficznych, testowalnych przewidywań o asymetrii przejść, roli historii, interwencjach.

### 4.4. Rekomendacja

**Nie deklarować DMTRD jako "nową teorię".** Zaproponować jako: **"Spójna ramy badawcza (research framework) do badania dynamiki regulacji motywacyjnej, integrująca znane konstrukty w spójną topologię Q3 z testowalnymi ograniczeniami dynamicznymi (HPE), asymetrią i path dependence."**

---

## 5. Literatura kluczowa do precedensów

| Element | Precedens | Referencja |
|---------|-----------|------------|
| Trzy determinaty (M,O,A) | MOA | Ölander & Thøgersen (1995) |
| Trzy determinaty (Cap, Opp, Mot) | COM-B | Michie et al. (2011) |
| Trzy determinaty (Att, SN, PBC) | TPB | Ajzen (1991) |
| Autonomia, Kompetencja, Powiązanie | SDT | Deci & Ryan (2000) |
| CTBN (lokalne zmiany, Q zależny od konfiguracji) | Continuous Time Bayesian Networks | Nodelman, Shelton, Koller (UAI 2002) |
| CTMC z kowariancjami | Multi-state models / msm | Jackson (2011), Titman (2011) |
| Typy regulacji (external, introjected, identified, integrated) | SDT | Ryan & Deci (2000) |
| Compliance, Identification, Internalization | Kelman (1958) | Kelman (1958) |
| Normy moralne (Personal Norm) | Schwartz (1977) | Schwartz (1977) |
| Obowiązki rolowe | Role Theory | Kahn et al. (1964) |
| Moral Distress | Jameton (1984), Corley et al. (2001) | Jameton (1984), Corley et al. (2001) |
| Path dependence w modelach dynamicznych | Higher-order Markov, HMM with history | Berchtold (1999), Vermunt (2008) |
| Separacja confirmatory/exploratory | Wagenmakers et al. (2012) | Wagenmakers et al. (2012) |

---

*Dokument wersja 1.0. Gotowy do dołączenia do raportu rewizji.*