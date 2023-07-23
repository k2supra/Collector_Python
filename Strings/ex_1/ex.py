def paloo(tt):
    for pa in pal:
        res = pal[::-1]
    print(res)
    if pal == res:
        print("True")
    else:
        print("NOPE")

try:
    print("Введіть паліндром")
    pal = input("->")

    def main():
        paloo(pal)

    main()

except Exception as ex:
    print(f"Error", {ex})