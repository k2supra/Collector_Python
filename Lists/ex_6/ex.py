import random
try:
    size = int(input("Size ->"))
    begin = int(input("Begin ->"))
    finish = int(input("Finish ->"))
    my_list = list()
    l_list = []
    m_list = []
    d_list = []

    for i in range(size):
        my_list.append(random.randint(begin, finish))
    my_list.sort()

    for item in my_list:
        print(item, end=" ")

    print()

    for item in my_list:
        print(f"Min element = {min(my_list)}, Max element = {max(my_list)}")
        break

    for item in my_list:
        if item < 0:
            l_list.append(item)
        if item > 0:
            m_list.append(item)
        if item == 0:
            d_list.append(item)
    print(f"Numbers < 0 = {len(l_list)}")
    print(f"Numbers > 0 = {len(m_list)}")
    print(f"Numbers = 0 = {len(d_list)}")
except Exception as ex:
    print(f"Error: {ex}")