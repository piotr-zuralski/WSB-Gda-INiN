# 8. (7 pkt) Podać medianę z danego zbioru liczb. Możemy używać funkcji sortującej.

print('Program podaję medianę z pobranego zbioru liczb')

ilosc_liczb = int(input('Proszę podać ilość liczb w zbiorze: '))
zbior_liczb = []

czy_parzysta_ilosc_liczb = (True, False)[ilosc_liczb % 2]
srodek_zbioru = int(ilosc_liczb/2)

mediana = 0

i = zbior_liczb.__len__()
while(i != ilosc_liczb):
    liczba = int(input('Proszę podać liczbę nr {:d}:'.format(i+1)))
    zbior_liczb.append(liczba)
    i = zbior_liczb.__len__()
    del liczba
del i, ilosc_liczb

# sortujemy zbior liczb
zbior_liczb.sort()

# wyliczamy mediane
if czy_parzysta_ilosc_liczb:
    mediana = (zbior_liczb[srodek_zbioru-1] + zbior_liczb[srodek_zbioru])/2
# znajdujemy mediane mediane
else:
    mediana = zbior_liczb[srodek_zbioru]
del srodek_zbioru

print('Zbiór liczb: "{}", mediana: "{}"'.format(zbior_liczb, mediana))
del zbior_liczb, mediana
