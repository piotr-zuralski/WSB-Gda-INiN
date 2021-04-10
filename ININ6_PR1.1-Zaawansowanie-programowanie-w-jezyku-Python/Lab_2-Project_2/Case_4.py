#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
4. [3 punkty] Sprawdzenie poprawności adresu IP
W zagadnieniach sieciowych jednym z elementarnych
zagadnień jest adres IP. W protokole IP w wersji czwartej są to 4
liczby rozdzielone kropkami, gdzie każda liczba mieści się w
przedziale 0 - 255. Np 10.13.0.255.
a. Na początku zostanie podana ilość przypadków testowych (‘i’).
Dla każdego ‘ i’:
b. Wczytaj adres IP ze standardowego wejścia
c. Dla każdego adresu wypisz “TAK” gdy adres jest poprawny,
bądź “NIE” gdy nie jest poprawny.
Przykładowe wejście:
5
abc.def.ghi.jkl
12.255.56.1
123.456.789.0
123.045.067.089
12.34.56 .1
Przykładowe wyjście:
NIE
TAK
NIE
NIE
NIE
Proszę nie używać funkcji do sprawdzania IP z bibliotek sieciowych!
"""


def podaj_ilosc():
    return int(input('Podaj ilość przypadków testowych: '))


def podaj_ip():
    return input('')


def waliduj_ip(ip):
    parts = ip.split('.')
    valid = True
    for i in parts:
        if not i.isdigit() or str(i)[0] == 0 or len(i) <= 2:
            valid = False
    return valid


ilosc = podaj_ilosc()
while not int(ilosc) >= 1:
    print('Nieprawidłowa ilość przypadkow, podaj przynajmniej 1')
    ilosc = podaj_ilosc()

lista = []
for i in range(1, ilosc + 1):
    ip = podaj_ip()
    while not len(ip) >= 1:
        print('Nieprawidłowe dane, podaj przynamniej jeden znak')
        ip = podaj_ip()
    lista.insert(i, ip)


for i in lista:
    if waliduj_ip(i):
        print('TAK')
    else:
        print('NIE')
