try:
    print("Enter sentence/s")
    string = input("->")

    print(f"********** \n{string.capitalize()}") #1

    t3 = ",.?!-/"
    t4 = "!"

    def cifri(ci): #2
        counter = 0
        for c in string:
            if c.isdigit():
                counter += 1


        print(f"********** \nNumbers = {counter}")


    def znaks(zn): #3
        counter = 0
        for b in string:
            if b in t3:
                counter += 1
        print(f"********** \nZnaks = {counter}")

    def ok(okl): #4
        counter = 0
        for a in string:
            if a in t4:
                counter += 1
        print(f"********** \nZnaks ! = {counter}")

    def main():
        cifri(string)

    main()

    def main():
        znaks(string)

    main()

    def main():
        ok(string)

    main()


except Exception as ex:
    print(f"Error", {ex})