"""
2. (2 pkt) Suma podawanych liczb:
• Pobrać od użytkownika liczbę przypadków (t).
• t-razy pobrać od użytkownika liczbę.
• Wypisać sumę podanych liczb.
• Wypisać średnią podanych liczb.
"""
t = int(input("Podaj liczbę przypadków: "))
tList = []
for i in range(0, t):
    j = int(input("Podaj liczbę dla przypadku {0:d}: ".format(i+1)))
    tList.append(j)

suma = sum(tList)
srednia = suma / t

print("Dla podanych {0:d} liczb, suma wynosi: {1:d} a średnia: {2:.2f}.".format(t, suma, srednia))
