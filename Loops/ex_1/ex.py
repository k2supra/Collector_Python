print("Введіть початок діапазону")
n1 = int(input("->"))
print("Введіть кінець діапазону")
n2 = int(input("->"))

for i in range(n1, n2 + 1):
        if i % 7 == 0:
            print(i)