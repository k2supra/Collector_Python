try:
    print("Enter text")
    txt = input("->")

    def slova(tt):
        counter = 0
        for sym in txt:
            if sym.isdigit():
                counter += 1

        print(f"Nums = {counter}, letters = {len(txt) - counter}")

    def main():
        slova(txt)

    main()



except Exception as ex:
    print(f'Error', {ex})