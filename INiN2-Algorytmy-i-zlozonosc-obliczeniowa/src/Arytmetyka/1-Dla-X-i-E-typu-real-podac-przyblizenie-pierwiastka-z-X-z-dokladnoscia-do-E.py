# 1. (5 pkt) Dla X i E typu real podać przybliżenie pierwiastka z X z dokładnością do E.

print('Program podaje przybliżenie pierwiastka z X z dokładnością do E')

X = float(input('Proszę podać liczbę X: '))
E = float(input('Proszę podać liczbę E: '))
ilosc_znakow_po_przecniku = str(E).split('.')[1].__len__()

iteracja = '1'
if ilosc_znakow_po_przecniku > 1:
    iteracja = '0.'
    for i in range(ilosc_znakow_po_przecniku):
        iteracja += '0'
    del i
    iteracja += '1'

iteracja = float(iteracja)

wynik_tymczasowy = 0
while (wynik_tymczasowy * wynik_tymczasowy) < X:
    wynik_tymczasowy += iteracja

wynik_tymczasowy_czesci_setne = str(wynik_tymczasowy).split('.')[1]
if int(wynik_tymczasowy_czesci_setne) < int(ilosc_znakow_po_przecniku):
    ilosc_znakow_po_przecniku = wynik_tymczasowy_czesci_setne.__len__()

wynik = str(wynik_tymczasowy).split('.')[0]
wynik += '.'
for i in range(int(ilosc_znakow_po_przecniku)):
    wynik += str(wynik_tymczasowy_czesci_setne[i])

wynik = float(wynik)
print('Pierwiastek z X="{}" z dokładnością E="{}" wynosi "{}"'.format(X, E, wynik))
