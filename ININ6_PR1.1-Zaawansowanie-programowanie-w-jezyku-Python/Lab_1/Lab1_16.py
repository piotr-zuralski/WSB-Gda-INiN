#x = dict()
animals = {"cat": ["stefan", "bubuś"],
           "dog": { "type": "pitbull",
                    "name": "azor"},
           "turtle": "tuptuś"}
for i in animals:
    print(i)
print("===")
for i in animals.keys():
    print(i)
print("===")
for i in animals.values():
    print(i)
print("===")
for key, value in animals.items():
    print("Klucz", key, "ma wartość", value)
