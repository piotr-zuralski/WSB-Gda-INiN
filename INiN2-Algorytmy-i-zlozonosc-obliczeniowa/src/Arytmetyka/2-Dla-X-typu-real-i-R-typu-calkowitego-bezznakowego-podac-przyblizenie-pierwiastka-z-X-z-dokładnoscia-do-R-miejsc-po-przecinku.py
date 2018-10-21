# 2. (10 pkt) Dla X typu real i R typu całkowitego bezznakowego podać przybliżenie pierwiastka z X z dokładnością do R miejsc po przecinku.

from math import fabs

print('Program podaje przybliżenie pierwiastka z X z dokładnością do R miejsc po przecinku')

X = float(input('Proszę podać liczbę X: '))
R = int(fabs(int(input('Proszę podać liczbę R: '))))

iteracja = '0.'
for i in range(R-1):
    iteracja += '0'
del i
iteracja += '1'

iteracja = float(iteracja)

wynik_tymczasowy = 0
while (wynik_tymczasowy * wynik_tymczasowy) < X:
    wynik_tymczasowy += iteracja

wynik = str(wynik_tymczasowy).split('.')[0]
wynik_tymczasowy_czesci_setne = str(wynik_tymczasowy).split('.')[1]
wynik += '.'
for i in range(R):
    wynik += str(wynik_tymczasowy_czesci_setne[i])

wynik = float(wynik)
print('Pierwiastek z X="{}" z dokładnością R="{}" wynosi "{}"'.format(X, R, wynik))
