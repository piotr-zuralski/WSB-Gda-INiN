"""
4. (2 pkt) Pomiędzy:
• Pobrać od użytkownika dwie liczby – a oraz b
• Należy wypisać na ekran liczby z przedziału <a; b> (a oraz b zawiera się w
przedziale).
• Proszę pamiętać że b może być większe od a lub odwrotnie a może być
większe od b.
"""
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

start = a
end = b
if end < start:
    start = b
    end = a

liczby = range(start, end+1, 1)
print("Liczby z przedziału <{0}; {1}>: {2:s}.".format(start, end, ", ".join(["{0:d}".format(l) for l in liczby])))
