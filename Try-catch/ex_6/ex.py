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
            sum += num;
        else:
            print('Sum = ', sum)
            break



except Exception as ex:
    print(f'Error', {ex})