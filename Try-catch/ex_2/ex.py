print("Enter a number")
num = int(input("->"))

try:
    f = 1
    for i in range(1, num + 1):
        f = f * i
    print(f)

except Exception as ex:
    print(f'Error', {ex})