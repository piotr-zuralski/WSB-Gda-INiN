# 12. (10 pkt) Wykonać mnożenie dwóch macierzy (reprezentowanych jako dowolne struktury dwuwymiarowe).

import random


def liczby_losowe_do_macierzy():
    return random.randint(1, 200)


print('Program wykonuje mnożenie dwóch macierzy: A i B: A[wa x ka] * B[wb x kb]')
print('Proszę podać wymiary macierzy A:')

wierszeA = int(input('Ilość wierszy macierzy A [wa]:'))
kolumnyA = int(input('Ilość kolumn macierzy A [ka]:'))

wierszeB = int(input('Ilość wierszy macierzy B [wb]:'))
kolumnyB = int(input('Ilość kolumn macierzy B [kb]:'))

print('Macierz A: wiesze="{:d}", kolumny="{:d}"'.format(wierszeA, kolumnyA))
print('Macierz B: wiesze="{:d}", kolumny="{:d}"'.format(wierszeB, kolumnyB))

if kolumnyA != wierszeB:
    print('Ilość kolumn macierzy A [ka] jest różna od ilości wierszy macierzy B [wb], nie można wykonać mnożenia macierzy')
    exit(1)

# tworzymy macierze o odpowiednich wymiarach
A = [0] * wierszeA
B = [0] * wierszeB
C = [0] * wierszeA

for wa in range(wierszeA):
    A[wa] = [0] * kolumnyA
    C[wa] = [0] * kolumnyB

    # wypełniamy macierz A liczbami
    for ka in range(kolumnyA):
        A[wa][ka] = liczby_losowe_do_macierzy()
    del wa, ka

for ka in range(kolumnyA):
    B[ka] = [0] * kolumnyB
    # wypełniamy macierz B liczbami
    for kb in range(kolumnyB):
        B[ka][kb] = liczby_losowe_do_macierzy()
del ka, kb

# mnożymy macierz A przez B i wynik umieszczamy w macierzy C
for wa in range(wierszeA):
    for kb in range(kolumnyB):
        wynik_mnozenia = 0
        for ka in range(kolumnyA):
            wynik_mnozenia += A[wa][ka] * B[ka][kb]
        C[wa][kb] = wynik_mnozenia
        del wynik_mnozenia, ka
del wa, kb

print('macierz A = "{}"'.format(A))
print('macierz B = "{}"'.format(B))
print('macierz C = "{}"'.format(C))
