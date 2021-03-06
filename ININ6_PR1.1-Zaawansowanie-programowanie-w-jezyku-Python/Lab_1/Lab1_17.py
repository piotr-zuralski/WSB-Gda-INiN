#x = dict()
animals = {"cat": ["stefan", "bubuś"],
           "dog": { "type": "pitbull",
                    "name": "azor"},
           "turtle": "tuptuś"}
#del animals["cat"]
if "cat" in animals: # animals.keys()
    print("Mamy koty")
else:
    print("Nie mamy kotów")
print("===")
print(animals["turtle"])
animals["hamster"] = "fifi"
for key, value in animals.items():
    print("Klucz", key, "ma wartość", value)
# print(animals["spider"])
print(animals.get("spider"))
print(animals.get("spider", "Brak klucza"))
print(animals.get("hamster"))
