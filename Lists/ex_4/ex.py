def ty(tt):
    print(f"Somethings = {txt.count(sm)}")


try:

    print("Enter text")
    txt = input("->")
    print("Enter something")
    sm = input("->")

    def main():
        ty(txt)

    main()


except Exception as ex:
    print(f"Error, {ex}")