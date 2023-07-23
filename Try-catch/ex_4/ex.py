print("1 number")
n1 = int(input("->"))
print("2 number")
n2 = int(input("->"))

try:
    f = 0
    for i in range(n1, n2+1):
        if i % 9 == 0:
            if i % 2 == 0:
                f = f + i
            print(f"Сума парних чисел {f}")

            if i % 2 == 1:
                f = f + i
            print(f"Сума непарних чисел {f}")
except Exception as ex:
    print("Error", ex)