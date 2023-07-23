def ple(number):
    return number ** 3


try:
    print("Введіть число")
    num = int(input("->"))




    result = ple(num)
    print(f"result = {result}")

except Exception as ex:
    print(f'Error', {ex})