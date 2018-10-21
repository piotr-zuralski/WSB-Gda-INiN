# 2. (5 pkt) Usunąć N-ty element cyklicznej listy L.

print('Program usuwa N-ty element z cyklicznej listy L')
element_N = str(input('Podaj N-ty element: '))
lista_L = str(input('Podaj tablicę liczb L oddzialając każdą z liczb przecinkiem (","): '))
lista_L = lista_L.replace(' ', '').strip(',').split(',')

L_len = lista_L.__len__()
for i in range(1, L_len-1):
    if element_N >= i:
        lista_L[i] = lista_L[i + 1]
del i

print('Tablica L "{}" z usuniętym N-tym elementem "{:d}"'.format(lista_L, element_N))
