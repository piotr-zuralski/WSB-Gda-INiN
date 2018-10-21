# 7. (5 pkt) Podać ilość wystąpień znaku A w zbiorze znaków D

print('Program podaje ilość wystąpień znaku "A" w zbiorze znaków D')

A = 'A'
D = str(input('Podaj zbiór znaków D oddzialając każdy ze znaków przecinkiem (","):'))

# zamiana ciągu znaków na tablicę
D = D.replace(' ', '').strip(',').split(',')

if D.__len__() <= 1:
    print('Podana tablica liczb jest pusta')
    exit(1)

ilosc_znakow = 0
for i in range(D.__len__()):
    if D[i] == A:
        ilosc_znakow += 1
del i

print('Znaleziono "{:d}" znaków "{:s}" w zbiorze D "{}"'.format(ilosc_znakow, A, D))
