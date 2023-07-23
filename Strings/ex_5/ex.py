try:
    print("Введіть символ для пошуку")
    sym = input("->")
    print("Введіть рядок")
    txt = input("->")


    def cont(tt):\
        print(txt.count(sym))

    def main():
        cont(sym)

    main()

except Exception as ex:
    print(f"Error", {ex})