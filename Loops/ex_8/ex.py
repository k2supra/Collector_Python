print("Введіть 1 число")
n1 = int(input("->"))
print("Введіть 2 число")
n2 = int(input("->"))

if n1 < n2:
    for i in range(n1, n2 + 1):
        if i % 2 == 1:
            print(i)



elif n1 > n2:
    for i in range(n2, n1 + 1):
        if i % 2 == 1:
            print(i)