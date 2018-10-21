# 9. (10 pkt) Na dowolnej liście lub tablicy liczb wykonać sortowanie w porządku rosnącym.

import random

print('Program wykonuje sortowanie tablicy w porządku rosnącym')
tablica_dlugosc = random.randint(50, 200)
tablica = [0] * tablica_dlugosc

for i in range(tablica_dlugosc):
    tablica[i] = random.randint(-200, 2000)
del i

tablica_posortowana = tablica

for i in range(tablica_dlugosc):
    j = 1
    while j < tablica_dlugosc:
        tmp = 0
        if tablica_posortowana[j - 1] > tablica_posortowana[j]:
            tmp = tablica_posortowana[j]
            tablica_posortowana[j] = tablica_posortowana[j - 1]
            tablica_posortowana[j - 1] = tmp
        j += 1
    del tmp, j
del i

print('tablica oryginalna: "{}"'.format(tablica))
print('tablica po sortowaniu: "{}"'.format(tablica_posortowana))

