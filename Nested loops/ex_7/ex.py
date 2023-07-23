import sys
try:
    print("Введіть число (довжина)")
    num1 = int(input("->"))
    print("Введіть число (ширина)")
    num2 = int(input("->"))

    for i in range(0, num1):
        for j in range(0, num2):
            if i == 0 or j == 0 or i == num1 - 1 or i == num2 - 1 or j == num2 - 1:
                sys.stdout.write("* ")
            else:
                sys.stdout.write("  ")
        print(" ")

except Exception as ex:
    print(f'Error', {ex})