"""
3. (2 pkt) Pobieranie wyrazów:
• Pobieraj od użytkownika wyrazy tak długo aż poda "koniec".
• Wyrazy odkładaj na listę
• Wypisz na ekran wyrazy w kolejności odwrotnej niż pobierana (ostatni jako
pierwszy). Nie wypisuj słowa "koniec".
"""
lista = []
while True:
    wyraz = input('Podaj wyraz do dodania (aby zakończyć, podaj "koniec"): ')
    if wyraz == 'koniec':
        break
    lista.append(wyraz)

print("Podane wyrazy w odwrotnej kolejności: {0:s}".format(", ".join(reversed(lista))))
