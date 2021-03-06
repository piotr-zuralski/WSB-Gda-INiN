#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. [1 punkt] MiniMax
Na wejście zostanie podany string - liczby rozdzielone spacjami.
Należy wypisać na ekran wartość minimalną oraz maksymalną z
wprowadzonego ciągu:
Przykładowe wejście:
1 2 -3 4 5
Przykładowe wyjście:
-3 5
"""


def podaj_liczby():
    return input('Podaj liczby, rozdzielając je spacjami: ').split(' ')


liczby = podaj_liczby()
while not len(liczby) >= 2:
    print('Podaj przynajmniej dwie liczby')
    liczby = podaj_liczby()

liczby = list(filter(lambda x: int(float(x)) or x.isdigit(), liczby))
min = min(liczby)
max = max(liczby)

print('{0} {1}'.format(min, max))
