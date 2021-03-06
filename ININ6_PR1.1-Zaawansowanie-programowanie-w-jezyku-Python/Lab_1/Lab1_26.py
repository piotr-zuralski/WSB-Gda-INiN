names = ["Bolesław Prus", "Henryk Sienkiewicz", "Adam Mickiewicz", "Władysław Reymont", "Juliusz Słowacki",
         "Cyprian Kamil Norwid", "Stefan Żeromski", "Halina Auderska", "Flora Bieńkowska"]

print(sorted(names, reverse=True, key=lambda y: y.split(" ")[-1]))
