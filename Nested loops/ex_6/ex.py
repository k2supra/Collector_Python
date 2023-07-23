import sys
try:
    print("Введіть число")
    num = int(input("->"))

    for i in range(0, num):
        for j in range(0, num):
            if i == 0 or j == 0 or i == num - 1 or j == num - 1:
                sys.stdout.write("* ")
            else:
                sys.stdout.write("  ")
        print(" ")

except Exception as ex:
    print(f'Error', {ex})