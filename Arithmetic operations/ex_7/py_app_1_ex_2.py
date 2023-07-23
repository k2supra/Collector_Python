count = int(input('->'))
part_1 = int(count/100)
part_2 = int(count %100 / 10)
part_3 = int(count %10)
part_4 = part_1 + part_2 + part_3
print(part_1, "\n",  part_2, "\n", part_3, "\n", part_4)