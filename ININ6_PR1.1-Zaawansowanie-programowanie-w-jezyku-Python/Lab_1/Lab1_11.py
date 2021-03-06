x = ["Ala", "Marcin", "Zygmunt"]
print(len(x))
#x.append("Zbigniew")
print(len(x))
x.remove("Marcin")
for i in x:
    print(i)
print(x[1])
if "Zbigniew" in x:
    print("Jest z nami Zbigniew")
else:
    print("Nie ma z nami Zbigniewa bo pewnie jest w więzieniu")
