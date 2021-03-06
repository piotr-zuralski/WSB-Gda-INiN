dictionary = {"dog": "Bazyli"}
dictionary["cat"] = "Stefan"
try:
    print(dictionary["cat"])
except KeyError:
    print("Nie ma takiego klucza")
else:
    print("Wszystko działa - nie poleciał wyjątek")
finally:
    print("Mimo wszystko robię kolejne rzeczy")
