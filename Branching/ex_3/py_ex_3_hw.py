num = int(input('m->'))
base = int(input('1(mile),2(duim),3(iard) \znak->'))

if base == 1:
    part_1 = num / 1609
    print(part_1)
if base == 2:
    part_2 = num * 32.37
    print(part_2)
if base == 3:
    part_3 = num * 1.094
    print(part_3)