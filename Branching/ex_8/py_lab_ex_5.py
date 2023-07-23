num_1 = int(input('1->'))
num_2 = int(input('2->'))
base = int(input('1(+), 2(-), 3(1/2), 4(*) \znak->'))

if base == 1:
    part_1 = num_1 + num_2
    print(part_1)
if base == 2:
    part_2 = num_1 - num_2
    print(part_2)
if base == 3:
    part_3 = (num_1 + num_2) / 2
    print(part_3)
if base == 4:
    part_4 = num_1 * num_2
    print(part_4)
