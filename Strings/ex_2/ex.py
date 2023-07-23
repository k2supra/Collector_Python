def gh(h):
    words = wordd.split()
    print(words)
    for word in words:
        if text.count(word) > 0:
            temp = word[0].upper() + word[1:]

            t1 = text.replace(wordd, temp)
    print(t1)

try:
    print("Enter a text")
    text = input("->")
    print("Enter a word/s")
    wordd = input("->")

    def main():
        gh(text)

    main()

except Exception as ex:
    print(f"Error", {ex})