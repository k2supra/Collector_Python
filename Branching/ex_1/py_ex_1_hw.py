num_1 = int(input('1->'))
num_2 = int(input('2->'))
num_3 = int(input('3->'))
base = int(input('1(+),2(*) \znak->'))

if base == 1:
    part_1 = num_1 + num_2 + num_3
    print(part_1)
if base == 2:
    part_2 = num_1 * num_2 * num_3
    print(part_2)
