print("Введіть 1 число")
n1 = int(input("->"))
print("Введіть 2 число")
n2 = int(input("->"))

for i in range(n1, n2):
    print(i, end=",")

for i in range(n2, n1):
    print(i, end=",")