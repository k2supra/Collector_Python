print("Введіть число (ширина)")
num1 = int(input("->"))
print("Введіть число (висота)")
num2 = int(input("->"))

for i in range(0, num2):
    for j in range(0, num1):
        print('*', end=" ")
    print()