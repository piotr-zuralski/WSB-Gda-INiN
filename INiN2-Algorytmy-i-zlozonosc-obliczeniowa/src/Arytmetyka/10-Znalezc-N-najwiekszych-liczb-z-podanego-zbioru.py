# 10. (10 pkt) Znaleźć N największych liczb z podanego zbioru.

print('Program znajduje N największych liczb z podanego zbioru')

N = int(input('N (ilość największych liczb): '))
zbior_liczb = str(input('Podaj zbiór liczb oddzialając każdą z liczb przecinkiem (","):'))

# zamiana ciągu znaków na tablicę
zbior_liczb = zbior_liczb.replace(' ', '').strip(',').split(',')

# zamiana ciągu znaków na liczby
for i in range(zbior_liczb.__len__()):
    zbior_liczb[i] = int(zbior_liczb[i])

print('Zbiór liczb="{}"'.format(zbior_liczb))

if N > zbior_liczb.__len__():
    print('N jest większe od ilości licz w zbiorze (N="{:d}", zbior_zlicz.length="{:d}")'.format(N, zbior_liczb.__len__()))
    exit(1)

for i in range(zbior_liczb.__len__()):
    j = 1
    while j < zbior_liczb.__len__():
        tmp = 0
        if zbior_liczb[j - 1] < zbior_liczb[j]:
            tmp = zbior_liczb[j]
            zbior_liczb[j] = zbior_liczb[j - 1]
            zbior_liczb[j - 1] = tmp
        j += 1
    del tmp, j
del i


print('{} (N) największych liczb: '.format(N))

for i in range(0, N):
    print('{:d}'.format(zbior_liczb[i]), end=', ')
del N, zbior_liczb, i
