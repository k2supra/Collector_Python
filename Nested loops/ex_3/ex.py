while True:
    try:
        print("Введіть 1 для старту")
        num = int(input("->"))

        if num == 1:
            for i in range(1, 11):
                for j in range(1, 11):
                    print(f"{i} * {j} = {i * j}", end="\t")
                print()
            break
        else:
            print("ВВЕДІТЬ 1 ДЛЯ ПОЧАТКУ")

    except Exception as ex:
        print(f'Error', {ex})