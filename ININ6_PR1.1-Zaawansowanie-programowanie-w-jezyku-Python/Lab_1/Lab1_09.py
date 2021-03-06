# bool isEven(int number) {   .... return True}
def is_even(number: int, variable=10) -> bool:
    return number + variable % 2 == 0

print(is_even(10, variable=5))
print(is_even(7))
print(is_even(3))
print(is_even(2))

print("Heheszke1", end=".")
print("Heheszke2")
print("Heheszke3")
