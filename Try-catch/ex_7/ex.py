try:
    sum = 0
    while True:
        print("Введіть число")
        num = int(input("->"))
        if num != 7:
            if num < 0:
                print("Number is negative")
            if num > 0:
                print("Number is positive")
            if num == 0:
                print("Number is equal to zero")
        else:
            print("Good bye!")
            break



except Exception as ex:
    print(f'Error', {ex})