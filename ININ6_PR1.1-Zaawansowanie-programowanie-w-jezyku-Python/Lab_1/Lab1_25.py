x = [1, 5, 2, 4]  # x.sort
print(sorted(x))
print(sorted(x, reverse=True))
print(sorted(x, reverse=True, key=lambda y: y % 2 == 0))
