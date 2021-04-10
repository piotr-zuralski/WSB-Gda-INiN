#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2. [1 punkt] Numer do cioci z ameryki
Na wejście zostanie podana lista dziesięciu cyfr. Należy z niej
złożyć numer w formacie:
(XXX) XXX-XXXX
I wypisać na ekran.
Przykładowe wejście:
1 2 3 4 5 6 7 8 9 0
Przykładowe wyjście:
(123) 456-7890
"""


def podaj_cyfry():
    _cyfry = input('Podaj listę 10 cyfr: ').replace(' ', '')
    _cyfry = list(filter(lambda x: int(float(x)) or x.isdigit(), _cyfry))
    return _cyfry


cyfry = podaj_cyfry()
while not len(cyfry) == 10:
    print("Nieprawidłowa ilość cyfr")
    cyfry = podaj_cyfry()

cyfry = ''.join(cyfry)
print("({0}) {1}-{2}".format(cyfry[0:3], cyfry[3:6], cyfry[6:10]))
