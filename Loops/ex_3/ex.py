print("Введіть 1 число")
n1 = int(input("->"))
print("Введіть 2 число")
n2 = int(input("->"))

for i in range(n1, n2+1):
    if i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")

else:
    print(n2 - n1)