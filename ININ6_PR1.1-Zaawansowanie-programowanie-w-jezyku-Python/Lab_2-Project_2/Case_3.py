#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3. [2 punkty] Sortowanie zbioru liczb
Na wejście zostanie podana lista liczb. Proszę dokonać sortowania, które
umieści liczby pierwsze na początku zbioru.
Liczba pierwsza to taka liczba, która dzieli się tylko przez 1 oraz samą siebie.
Wystarczy zaimplementować metodę naiwną:
https://pl.wikipedia.org/wiki/Test_pierwszo%C5%9Bci
Przykładowe wejście:
14, 8, 9, 12, 4, 10, 11, 7, 2
Przykładowe wyjście:
11, 7, 2, 14, 8, 9, 12, 4, 10
(Nie ma żadnych innych wymagań odnośnie kolejności na zbiorze).
"""


def is_liczba_pierwsza(liczba):
    liczba = int(liczba)
    try:
        return liczba % 1 == 0 and liczba % liczba == 0
    except ZeroDivisionError:
        return False


def podaj_liczby():
    return input('Podaj liczby, rozdzielając je przecinkiem: ').replace(' ', '').split(',')


liczby = podaj_liczby()
while not len(liczby) >= 2:
    print('Podaj przynajmniej dwie liczby')
    liczby = podaj_liczby()

for i in liczby:
    last = len(liczby) - 1
    index = liczby.index(i)
    if is_liczba_pierwsza(i):
        liczby.insert(0, i)
    else:
        liczby.insert(last, i)
    del liczby[index]

print(', '.join(liczby))
