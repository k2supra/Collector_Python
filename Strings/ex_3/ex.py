def hg(t):
    res = text.count(".") + text.count("?") + text.count("/") + text.count(",") + text.count(" ") + text.count("-") + text.count("_")
    print(res)

try:
    print("Enter text")
    text = input("->")

    def main():
        hg(text)

    main()

except Exception as ex:
    print(f"Error", {ex})