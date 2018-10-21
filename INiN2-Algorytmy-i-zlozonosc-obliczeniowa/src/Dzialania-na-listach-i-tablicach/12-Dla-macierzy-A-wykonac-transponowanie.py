# 12. (10 pkt) Dla macierzy A (reprezentowanej przez dowolną wybraną dwuwymiarową strukturę), wykonać transponowanie.

import random


def liczby_losowe_do_wymiarow_macierzy():
    return random.randint(2, 5)


def liczby_losowe_do_macierzy():
    return random.randint(1, 200)


print('Program wykonuje transponowanie macierzy A')

# generowanie rozmiarów macierzy
# kolumny = 2
kolumny = liczby_losowe_do_wymiarow_macierzy()
# wiersze = 3
wiersze = liczby_losowe_do_wymiarow_macierzy()

A = [0] * kolumny
B = [0] * wiersze

# generowanie danych w macierzy
wiersz = [0] * wiersze
for k in range(kolumny):
    A[k] = [liczby_losowe_do_macierzy()]
    for w in range(wiersze):
        wiersz[w] = liczby_losowe_do_macierzy()
    A[k] = wiersz
    wiersz = [0] * wiersze
del wiersz, k, w

# A=[[127, 28, 96], [12, 89, 13]]
print('kolumny A ="{}", wiersze A ="{}", Macierz A = "{}"'.format(kolumny, wiersze, A))

# transpozycja macierzy
i = 0
for w in range(wiersze):
    i = 0
    B[w] = [0] * kolumny
    for k in range((kolumny-1), -1, -1):
        B[w][i] = A[k][w]
        i = i + 1
del k, w, i

print('kolumny B ="{}", wiersze B ="{}", Macierz B = AT = "{}"'.format(wiersze, kolumny, B))
del kolumny, wiersze, A, B
