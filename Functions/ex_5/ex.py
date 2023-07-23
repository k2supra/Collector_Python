def numbr(number):
    if number >= 0:
        return 'True'

    else:
        return 'False'

try:
    print("Enter a number")
    n1 = int(input("->"))




except Exception as ex:
    print(f'Error', {ex})