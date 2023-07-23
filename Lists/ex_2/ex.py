import random
try:
    size = int(input("Size ->"))
    begin = int(input("Begin ->"))
    finish = int(input("Finish ->"))
    my_list = list()

    for i in range(size):
        my_list.append(random.randint(begin, finish))

    my_list.sort()

    for item in my_list:
        print(item, end=" ")

    res_list_even = list()
    res_list_odd = list()
    res_list_neg = list()
    res_list_pos = list()
    print()

    for it in my_list:
        if it % 2 == 0:
            res_list_even.append(it)

        if it % 2 != 0:
            res_list_odd.append(it)

        if it < 0:
            res_list_neg.append(it)

        if it > 0:
            res_list_pos.append(it)


    print(f"Even {res_list_even}", end=" ")
    print(f"\nOdd {res_list_odd}", end=" ")
    print(f"\nNeg {res_list_neg}", end=" ")
    print(f"\nNeg {res_list_pos}", end=" ")
except Exception as ex:
    print(f"Error: {ex}")