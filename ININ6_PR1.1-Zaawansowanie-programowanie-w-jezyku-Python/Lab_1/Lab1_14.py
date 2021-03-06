ip = "10.120.24.23"
x = ip.split('.')
print(x)
print((type(x[0])))
y = []
for i in x:
    y.append(int(i))
print(y)
# list comprehension
z = [int(i) for i in x]
print(z)
z2 = [int(i) for i in x if int(i) % 2 == 0]
print(z2)
