try:
    print("Введіть 1 число діапазону")
    num1 = int(input("->"))
    print("Введіть 2 число діапазону")
    num2 = int(input("->"))

    for i in range(num1, num2 + 1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}", end="\t")
        print()

except Exception as ex:
    print(f'Error', {ex})