# SPRAWOZDANIE LAB 4 - wprowadzenie do biblioteki pymcdm 

## 1. Cel projektu 
Celem projektu było porównanie wybranych metod wielokryterialnego wspomagania decyzji (MCDM): **TOPSIS**, **SPOTIS** oraz opcjonalnie **VIKOR**. Wybranym kryterium przeze mnie był ranking samochodów sportowych z "wyższej półki" na podstawie macierzy decyzyjnej. Celem końcowym było określenie zgodności rankingów oraz wyciągnięcie wniosków odnośnie stabilności i różnic pomiędzy metodami.

## 2. Opis zastowowanych metod MCDM

### TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
TOPSIS zakłada istnienie punktu idealnego (najlepsze możliwe wartości kryteriów) i anty-idealnego (najgorsze możliwe wartości). Każda alternatywa (samochód) oceniana jest na podstawie odległości od obu punktów – im bliżej ideału i dalej od anty-ideału, tym wyższa preferencja.

### SPOTIS (Stable Preference Ordering Towards Ideal Solution)
SPOTIS to metoda oparta na stabilnej miarze odległości od ideału, ale zamiast względnych rankingów bazuje na absolutnych granicach (min, max) dla każdego kryterium. Preferencja obliczana jest jako ważona suma odchyleń od najlepszego punktu.

### VIKOR (VIseKriterijumska Optimizacija I Kompromisno Resenje)
VIKOR to metoda kompromisowa – oblicza tzw. wskaźnik Q, który uwzględnia zarówno "odległość sumaryczną" (S), jak i "maksymalną stratę" (R). Umożliwia wybór rozwiązania najbardziej kompromisowego.

## 3. Dane wejściowe i wstępna macierz decyzyjna oraz jej kryteria
W ramach ćwiczenia porównywane są **samochody sportowe klasy premium**, przy czym kluczowym założeniem projektu jest określenie, które z nich są najbardziej optymalne z punktu widzenia różnych kryteriów technicznych i ekonomicznych. Każdy z samochodów stanowi **alternatywę decyzyjną**, a ocena odbywa się na podstawie 5 kluczowych **kryteriów decyzyjnych**, które są typowe w analizie porównawczej pojazdów tego typu:

1. **Moc (KM)** – kryterium do maksymalizacji - waga apriori - 0.3
2. **Cena (zł)** – kryterium do minimalizacji - waga apriori - 0.3
3. **Prędkość maksymalna (km/h)** – kryterium do maksymalizacji - waga apriori - 0.25    
4. **Przyspieszenie 0–100 km/h (s)** – kryterium do minimalizacji - waga apriori - 0.1
5. **Rok produkcji** – kryterium do maksymalizacji - waga apriori - 0.05

Dane zostały zebrane w postaci macierzy decyzyjnej w następujący sposób:
                                Moc(KM)   Cena(zł)  Prędkość maksymalna(km/h)  Przyspieszenie 0-100(s)  Rok produkcji
Aston Martin DB12 coupe         680.0     1400000.0                      325.0                      3.6         2023.0
Ferrari 812 Superfast           795.0     1480000.0                      340.0                      2.9         2019.0
Lamborghini Aventador S         740.0     1850000.0                      350.0                      3.0         2019.0
Porsche 911 GT3 RS              525.0     1673567.0                      312.0                      3.2         2025.0
Chevrolet Corvette ZR1 C7       755.0     1060000.0                      345.0                      3.0         2019.0
Dodge Challenger SRT Hellcat    807.0     449900.0                       320.0                      2.8         2019.0
BMW E92 M3                      420.0     199000.0                       250.0                      5.0         2007.0
Mercede-Benz C63 AMG            457.0     229000.0                       250.0                      4.3         2008.0
Nissan GT-R Black Edition       570.0     289000.0                       328.0                      2.9         2012.0

Ogólnie głównym celem było wybranie egzemplarza, który jednocześnie w prostych słowach mówiąc **oferował jak najwięcej za najmniej**

## 4. Scenariusze
### 4.1 Scenariusz 1 - Równomierne podejście
### 🎯 Scenariusz 1: Równomierne podejście
- **Wagi:** [0.3, 0.3, 0.25, 0.1, 0.05]
- **Preferencje:** standardowy balans pomiędzy mocą, ceną i osiągami.
- **Wynik:**  
  - TOP 3 (stałe we wszystkich metodach):  
    1. **Dodge Challenger SRT Hellcat**  
    2. **Chevrolet Corvette ZR1**  
    3. **Ferrari 812 Superfast**  
- **Ocena:** Stabilny scenariusz — metody dają niemal identyczne wyniki.

---

### ⚡ Scenariusz 2: Priorytet dla osiągów (moc + przyspieszenie)
- **Wagi:** [0.4, 0.1, 0.3, 0.15, 0.05]
- **Cel:** promowanie samochodów o sportowym charakterze.
- **Wynik:**  
  - TOP 3:
    1. **Dodge Challenger**  
    2. **Chevrolet Corvette ZR1**  
    3. **Ferrari 812 Superfast / Lamborghini Aventador** (zależnie od metody)  
- **Ocena:** Ranking zmienia się tylko nieznacznie — metody są odporne na zmiany, gdy liderzy mają ekstremalne osiągi.

---

### 💰 Scenariusz 3: Minimalizacja kosztów
- **Wagi:** [0.2, 0.5, 0.1, 0.1, 0.1]
- **Cel:** maksymalizacja opłacalności zakupu.
- **Wynik:**  
  - TOP 3:
    1. **BMW E92 M3**  
    2. **Mercedes C63 AMG**  
    3. **Nissan GT-R Black Edition**  
- **Ocena:** Zmiana liderów — tańsze auta wysuwają się na prowadzenie. Metody pokazują wysoką czułość na koszt przy dużej wadze ceny.

---

### 🚀 Scenariusz 4: Maksymalne osiągi (bez uwzględniania ceny)
- **Wagi:** [0.35, 0.0, 0.35, 0.2, 0.1]
- **Cel:** wybrać najbardziej ekstremalny samochód bez oglądania się na koszt.
- **Wynik:**
  - TOP 3:
    1. **Lamborghini Aventador S**  
    2. **Ferrari 812 Superfast**  
    3. **Dodge Challenger SRT Hellcat**  
- **Ocena:** Droższe auta wskakują na podium, jeśli koszt nie ma znaczenia.

---

## 6. Wnioski ze scenariuszy

Analiza scenariuszowa pokazuje, że:

- **Dodge Challenger i Chevrolet Corvette ZR1** to najczęściej wybierane samochody w scenariuszach uwzględniających cenę.
- **Lamborghini i Ferrari** wygrywają w rankingach, gdy koszt nie ma znaczenia.
- **SPOTIS** zachowywał się najbardziej „neutralnie” i nie faworyzował skrajnych wartości, przez co wyniki były bardziej wyważone.
- **VIKOR** jako metoda kompromisowa lepiej różnicował pozycje środkowe i eksponował auta zbalansowane.