"""
1. (2 pkt) Piąteczek:
• Pobrać od użytkownika słowo (dzień tygodnia)
• Jeśli to piątek to wypisać tekst "Piąteczek piątunio! :)"
• Jeśli to weekend to wypisać "weeeekend!!"
• W pozostałych przypadkach wypisać "Praca, praca..."
"""
dni_tygodnia = ("poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela")


def podaj_dzien_tygodnia():
    return input("Podaj dzień tygodnia ({0:s}): ".format("|".join(dni_tygodnia))).lower()


dzien_tygodnia = podaj_dzien_tygodnia()
while dzien_tygodnia not in dni_tygodnia:
    print("Nieprawidłowy dzień tygodnia, podaj prawidłowy")
    dzien_tygodnia = podaj_dzien_tygodnia()

if dzien_tygodnia == dni_tygodnia[4]:
    print("Piąteczek piątunio! :)")
elif dzien_tygodnia == dni_tygodnia[5] or dzien_tygodnia == dni_tygodnia[6]:
    print("weeeekend!!")
else:
    print("Praca, praca...")
