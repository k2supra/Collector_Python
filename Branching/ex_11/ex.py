print("Введіть вартість пристаки")
m1 = int(input("->"))

print("Введіть їх кількість")
m2 = int(input("->"))

print("Введіть знижку %")
m3 = int(input("->"))

print("1 - сумма всіх приставок / 2 - вартість 1 приставки")
base = int(input("->"))

part = (m3 / 100) * m1
part_1 = (m1 - part) * m2
part_2 = part_1 / m2
if base == 1 :
    print(f"{part_1}")

if base == 2 :
    print(f"{part_2}")