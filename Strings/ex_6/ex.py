def ttxt(t):
    txxt = txt.replace(sym, chn)
    print(txxt)
try:
    print("Введіть рядок")
    txt = input("->")
    print("Введіть слово для пошуку")
    sym = input("->")
    print("Введіть слово для заміни")
    chn = input("->")


    def main():
        ttxt(txt)

    main()

except Exception as ex:
    print(f"Error", {ex})