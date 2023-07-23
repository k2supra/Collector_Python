print("Введіть початок діапазону")
n1 = nn1 = int(input("->"))
print("Введіть кінець діапазону")
n2 = nn2 = int(input("->"))
n = []

print(f"Всі числа діапазону {n1} , {n2}")
for i in range(n1, n2 + 1):
    print(i)

print(f"Всі числа діапазону {n1} , {n2} за спаданням")
while n1 <= n2:
    n.append(n2)
    n2 -= 1
    for i in n[::-1]:
        print(i)
        break

print(f"Усі числа діапазону {nn1} , {nn2} кратні 7")
for i in range(nn1, nn2 + 1):
        if i % 7 == 0:
            print(i)


print(f"Кількість чисел діапазона {nn1} , {nn2} що діляться на 5")
reb = (nn2 + 1) - nn1
lol = reb // 5
print(lol)