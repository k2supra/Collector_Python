def cili(n1):
    if n1 % 1 == 0 and n1 % n1 == 0:
        print(f"{n1}, цілі")
    else:
        print("Не цілі")


try:
    print("Введіть число")
    n1 = int(input("->"))
    def cili(n1):
        if n1 % 1 == 0 and n1 % n1 == 0:
            print(f"{n1}, цілі")
        else:
            print("Не цілі")

    def main():
        cili(n1)

    main()



except Exception as ex:
    print(f'Error', {ex})