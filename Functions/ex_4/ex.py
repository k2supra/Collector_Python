try:
    print("Enter 1 number")
    val1 = int(input("->"))
    print("Enter 2 number")
    val2 = int(input("->"))

    def most(a, b):
        if val1 > val2:
            print(f"{val1} is more than {val2}")
        if val2 > val1:
            print(f"{val2} is more than {val1}")

        if val1 == val2:
            print(f"{val1} and {val2} are same")



    def main():
        most(val1, val2)


    main()

except Exception as ex:
    print(f'Error', {ex})