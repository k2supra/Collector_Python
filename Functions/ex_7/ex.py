def tring(tt):
    for ky in text:
        res = text[::-1]
    print(res)


try:

    text = input("->")
    def tring(tt):
        for ky in text:
            res = text[::-1]
        print(res)

    def main():
        tring(text)

    main()


except Exception as ex:
    print(f'Error', {ex})