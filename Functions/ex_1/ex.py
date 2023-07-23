def fact(a):
    f = 1
    for i in range(1, a1 + 1):
        f = f * i
    print(f)


try:
    a1 = int(input("->"))


    def main():
        fact(a1)

    main()


except Exception as ex:
    print(f'Error', {ex})