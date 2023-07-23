nums = []
num1 = int(input("->"))
num2 = int(input("->"))

while num1 >= num2:
    nums.append(num1)
    num1 -= 1
    for i in nums[::-1]:
        print(i)
        break


while num1 <= num2:
    nums.append(num2)
    num2 -= 1
    for i in nums[::-1]:
        print(i)
        break