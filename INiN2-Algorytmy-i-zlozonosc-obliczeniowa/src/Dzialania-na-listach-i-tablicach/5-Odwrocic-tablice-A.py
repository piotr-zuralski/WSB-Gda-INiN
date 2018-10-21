# 5. (5 pkt) Odwrócić tablicę A.

print('Program odwraca tablicę A')
tablica = str(input('Podaj tablicę liczb oddzialając każdą z liczb przecinkiem (","):'))

# zamiana ciągu znaków na tablicę
tablica = tablica.replace(' ', '').strip(',').split(',')

if tablica.__len__() <= 1:
    print('Podana tablica liczb jest pusta')
    exit(1)

t = tablica.__len__()
tablica_odwrocona = [0] * t
ta = 0
for liczba in range(t):
    tablica_odwrocona[ta] = tablica[t-1]
    ta += 1
    t -= 1
del ta, t

print('tablica oryginalna: "{}", tablica odwrocona: "{}"'.format(tablica, tablica_odwrocona))
