import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.weights import entropy_weights
from pymcdm import normalizations 

samochody_matrix = np.array([
    [680, 1400000, 325, 3.6, 2023],
    [795, 1480000, 340, 2.9, 2019],
    [740, 1850000, 350, 3.0, 2019],
    [525, 1673567, 312, 3.2, 2025],
    [755, 1060000, 345, 3.0, 2019],
    [807, 449900, 320, 2.8, 2019],
    [420, 199000, 250, 5.0, 2007],
    [457, 229000, 250, 4.3, 2008],
    [570, 289000, 328, 2.9, 2012]
], dtype=float)

nazwy_alternatyw = ['Aston Martin DB12 coupe', 'Ferrari 812 Superfast', 'Lamborghini Aventador S',
                    'Porsche 911 GT3 RS', 'Chevrolet Corvette ZR1 C7', 'Dodge Challenger SRT Hellcat',
                    'BMW E92 M3', 'Mercede-Benz C63 AMG', 'Nissan GT-R Black Edition']

nazwy_kryteriow = ['Moc(KM)', 'Cena(zł)', 'Prędkość maksymalna(km/h)', 'Przyspieszenie 0-100(s)', 'Rok produkcji']

wagi_apriori = np.array([0.3, 0.3, 0.25, 0.1, 0.05])

oryginalne_typy_kryteriow_lista = [1, -1, 1, -1, 1]
oryginalne_typy_kryteriow_np_do_metod = np.array(oryginalne_typy_kryteriow_lista)

print("--- Dane początkowe ---")
print("Macierz decyzyjna (surowa):")
print(pd.DataFrame(samochody_matrix, columns=nazwy_kryteriow, index=nazwy_alternatyw))
print("\nWagi a priori (subiektywne):")
print(dict(zip(nazwy_kryteriow, wagi_apriori)))
print("\nOryginalne typy kryteriów (1:max, -1:min):")
print(dict(zip(nazwy_kryteriow, oryginalne_typy_kryteriow_lista)))

wagi_entropia = entropy_weights(samochody_matrix, oryginalne_typy_kryteriow_lista)
print("\nWagi wyznaczone metodą entropii (na surowych danych):")
print(dict(zip(nazwy_kryteriow, np.round(wagi_entropia, 4))))
print(f"Suma wag entropii: {np.sum(wagi_entropia):.4f}")

print("\n--- Demonstracja jawnej normalizacji ---")
samochody_znormalizowane_minmax = normalizations.minmax_normalization(samochody_matrix, oryginalne_typy_kryteriow_lista)
print("Macierz po normalizacji Min-Max (0-1, gdzie 1=najlepiej):")
print(pd.DataFrame(samochody_znormalizowane_minmax, columns=nazwy_kryteriow, index=nazwy_alternatyw).round(4))

typy_dla_danych_gdzie_1_to_lepiej_lista = [1] * samochody_matrix.shape[1]
typy_dla_danych_gdzie_1_to_lepiej_np_do_metod = np.array(typy_dla_danych_gdzie_1_to_lepiej_lista)

samochody_znormalizowane_vector = normalizations.vector_normalization(samochody_matrix, oryginalne_typy_kryteriow_lista)
print("\nMacierz po normalizacji Wektorowej:")
print(pd.DataFrame(samochody_znormalizowane_vector, columns=nazwy_kryteriow, index=nazwy_alternatyw).round(4))

def wyswietl_ranking(scenariusz, metoda_nazwa, ranking, preferencje, nazwy_alt, etykieta_wartosci="Preferencja"):
    print(f"\n--- {scenariusz} ---")
    print(f"Ranking {metoda_nazwa}:")
    posortowane = sorted(zip(ranking, preferencje, nazwy_alt), key=lambda x: x[0])
    for rank_val, pref_val, name_val in posortowane:
        print(f"Miejsce {int(rank_val)}: {name_val} ({etykieta_wartosci}: {pref_val:.5f})")

granice_spotis_surowe = np.zeros((samochody_matrix.shape[1], 2))
for j in range(samochody_matrix.shape[1]):
    kolumna = samochody_matrix[:, j]
    granice_spotis_surowe[j, :] = [np.min(kolumna), np.max(kolumna)] # ZAWSZE [min, max] z danych

print("\nGranice dla SPOTIS (surowe dane, zawsze [min, max] z kolumny):")
print(pd.DataFrame(granice_spotis_surowe, index=nazwy_kryteriow, columns=['Min w danych', 'Max w danych']))


print("\n\n===== SCENARIUSZ 1: WAGI A PRIORI, WBUDOWANA NORMALIZACJA (SUROWE DANE) =====")
# TOPSIS
topsis1 = TOPSIS()
pref_topsis1 = topsis1(samochody_matrix, wagi_apriori, oryginalne_typy_kryteriow_np_do_metod)
rank_topsis1 = topsis1.rank(pref_topsis1)
wyswietl_ranking("Scenariusz 1", "TOPSIS", rank_topsis1, pref_topsis1, nazwy_alternatyw)

# SPOTIS
spotis1 = SPOTIS(bounds=granice_spotis_surowe)
pref_spotis1 = spotis1(samochody_matrix, wagi_apriori, oryginalne_typy_kryteriow_np_do_metod)
rank_spotis1 = spotis1.rank(pref_spotis1)
wyswietl_ranking("Scenariusz 1", "SPOTIS", rank_spotis1, pref_spotis1, nazwy_alternatyw)

# VIKOR
vikor1 = VIKOR()
pref_vikor1 = vikor1(samochody_matrix, wagi_apriori, oryginalne_typy_kryteriow_np_do_metod)
rank_vikor1 = vikor1.rank(pref_vikor1)
wyswietl_ranking("Scenariusz 1", "VIKOR", rank_vikor1, pref_vikor1, nazwy_alternatyw, "Q")


print("\n\n===== SCENARIUSZ 2: WAGI ENTROPOWE, WBUDOWANA NORMALIZACJA (SUROWE DANE) =====")
# TOPSIS
topsis2 = TOPSIS()
pref_topsis2 = topsis2(samochody_matrix, wagi_entropia, oryginalne_typy_kryteriow_np_do_metod)
rank_topsis2 = topsis2.rank(pref_topsis2)
wyswietl_ranking("Scenariusz 2", "TOPSIS", rank_topsis2, pref_topsis2, nazwy_alternatyw)

# SPOTIS
spotis2 = SPOTIS(bounds=granice_spotis_surowe)
pref_spotis2 = spotis2(samochody_matrix, wagi_entropia, oryginalne_typy_kryteriow_np_do_metod)
rank_spotis2 = spotis2.rank(pref_spotis2)
wyswietl_ranking("Scenariusz 2", "SPOTIS", rank_spotis2, pref_spotis2, nazwy_alternatyw)

# VIKOR
vikor2 = VIKOR()
pref_vikor2 = vikor2(samochody_matrix, wagi_entropia, oryginalne_typy_kryteriow_np_do_metod)
rank_vikor2 = vikor2.rank(pref_vikor2)
wyswietl_ranking("Scenariusz 2", "VIKOR", rank_vikor2, pref_vikor2, nazwy_alternatyw, "Q")


print("\n\n===== SCENARIUSZ 3: WAGI A PRIORI, ZMIANA NORMALIZACJI W TOPSIS (SUROWE DANE) =====")
topsis3 = TOPSIS(normalization_function=normalizations.minmax_normalization)
pref_topsis3 = topsis3(samochody_matrix, wagi_apriori, oryginalne_typy_kryteriow_np_do_metod)
rank_topsis3 = topsis3.rank(pref_topsis3)
wyswietl_ranking("Scenariusz 3 (TOPSIS z MinMax Norm.)", "TOPSIS", rank_topsis3, pref_topsis3, nazwy_alternatyw)

vikor3 = VIKOR(normalization_function=normalizations.vector_normalization)
pref_vikor3 = vikor3(samochody_matrix, wagi_apriori, oryginalne_typy_kryteriow_np_do_metod)
rank_vikor3 = vikor3.rank(pref_vikor3)
wyswietl_ranking("Scenariusz 3 (VIKOR z Vector Norm.)", "VIKOR", rank_vikor3, pref_vikor3, nazwy_alternatyw, "Q")


print("\n\n===== SCENARIUSZ 4: WAGI A PRIORI, JAWNIE ZNORMALIZOWANE DANE (MinMax 0-1) =====")
#samochody_znormalizowane_minmax (gdzie 1=najlepiej, skala 0-1)

# TOPSIS
topsis4 = TOPSIS(normalization_function=normalizations.linear_normalization)
pref_topsis4 = topsis4(samochody_znormalizowane_minmax, wagi_apriori, typy_dla_danych_gdzie_1_to_lepiej_np_do_metod)
rank_topsis4 = topsis4.rank(pref_topsis4)
wyswietl_ranking("Scenariusz 4 (Dane już MinMax 0-1)", "TOPSIS", rank_topsis4, pref_topsis4, nazwy_alternatyw)

# SPOTIS z odpowiednimi granicami dla danych 0-1
# Dla danych znormalizowanych do [0,1], gdzie 1 jest zawsze lepiej,
granice_spotis_01 = np.array([[0, 1]] * samochody_matrix.shape[1], dtype=float)
print("\nGranice dla SPOTIS (dane znormalizowane 0-1):")
print(pd.DataFrame(granice_spotis_01, index=nazwy_kryteriow, columns=['Min (0)', 'Max (1)']))

spotis4 = SPOTIS(bounds=granice_spotis_01)
pref_spotis4 = spotis4(samochody_znormalizowane_minmax, wagi_apriori, typy_dla_danych_gdzie_1_to_lepiej_np_do_metod)
rank_spotis4 = spotis4.rank(pref_spotis4)
wyswietl_ranking("Scenariusz 4 (Dane już MinMax 0-1)", "SPOTIS", rank_spotis4, pref_spotis4, nazwy_alternatyw)

# VIKOR
vikor4 = VIKOR(normalization_function=normalizations.linear_normalization)
pref_vikor4 = vikor4(samochody_znormalizowane_minmax, wagi_apriori, typy_dla_danych_gdzie_1_to_lepiej_np_do_metod)
rank_vikor4 = vikor4.rank(pref_vikor4)
wyswietl_ranking("Scenariusz 4 (Dane już MinMax 0-1)", "VIKOR", rank_vikor4, pref_vikor4, nazwy_alternatyw, "Q")