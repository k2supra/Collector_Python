list = []
while True:
    try:
        print("Enter number")
        num = int(input("->"))

        if num != 0:
            list.append(num)
            print("Sum = " + str(sum(list)))

        else:

            break




    except Exception as ex:
        print(f"Error: {ex}")
print("Final sum = " + str(sum(list)))
print("AVG = ", sum(list) / len(list))