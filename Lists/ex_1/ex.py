import random
try:
    size = int(input("Size ->"))
    begin = int(input("Begin ->"))
    finish = int(input("Finish ->"))
    my_list = list()
    sum_list = []
    par_list = []
    unpar_list = []
    kthree_list = []

    for i in range(size):
        my_list.append(random.randint(begin, finish))

    my_list.sort()


    for item in my_list:
        print(item, end=" ")


    for itel in my_list:
        if itel < 0:
            sum_list.append(itel)
    print(f"\nLess ->{sum(sum_list)}" "\n**********")

    for par in my_list:
        if par % 2 == 0:
            par_list.append(par)
    print(f"Sum of pair numbers = {sum(par_list)}" "\n**********")

    for unpar in my_list:
        if unpar % 2 != 0:
            unpar_list.append(unpar)
    print(f"Sum of unpair numbers = {sum(unpar_list)}" "\n**********")

    mul = 1

    for kthree in range(0, len(my_list), 3):
        if kthree % 3 == 0:
            print(f"{mul} * {my_list[kthree]}[{kthree}] = ", end=" ")
            mul *= my_list[kthree]
            print(f"Mul = {mul}" "\n**********")


    for minmax in my_list:
        print(f"Mul of min & max = {min(my_list) * max(my_list)}" "\n**********")
        break

    for sumin in my_list:
        res = sum(my_list) - (min(my_list) + max(my_list))
        print(f"Res = {res}")
        break




except Exception as ex:
    print(f"Error: {ex}")