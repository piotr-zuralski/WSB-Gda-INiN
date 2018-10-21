# 6. (5 pkt) Znaleźć średnią arytmetyczną z podanego zbioru liczb.

print('Program wylicza średnią artymetyczną z podanego zbioru liczb')
zbior_liczb = str(input('Podaj tablicę liczb oddzialając każdą z liczb przecinkiem (","):'))

# zamiana ciągu znaków na tablicę
zbior_liczb = zbior_liczb.replace(' ', '').strip(',').split(',')

if zbior_liczb.__len__() <= 1:
    print('Podana tablica liczb jest pusta')
    exit(1)

suma = 0
ilosc_liczb = zbior_liczb.__len__()
for i in range(ilosc_liczb):
    suma += int(zbior_liczb[i])
del i

srednia = suma/ilosc_liczb
print('Średnia artymetyczną wynosi "{}" z podanego zbioru liczbu liczb: "{}"'.format(srednia, zbior_liczb))

