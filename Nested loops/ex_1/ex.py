try:
    nums = []
    print("Введіть 1 число діапазону")
    num1 = int(input("->"))
    print("Введіть 2 число діапазону")
    num2 = int(input("->"))

    for i in range(num1, num2):
        for j in range(2, int(num1//2+1)):
            if num1 % j == 0:
                break

        else:
            nums.append(num1)
        num1 += 1
    for k in nums:
        if k < 2:
            nums.remove(k)
        print(nums)

except Exception as ex:
    print(f'Error', {ex})