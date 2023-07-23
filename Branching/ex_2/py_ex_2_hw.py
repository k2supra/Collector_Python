num_1 = int(input('1->'))
num_2 = int(input('2->'))
num_3 = int(input('3->'))
base = int(input('1 (max),2 (min),3 (avg) \znak->'))
res = ''
if base == 1:
    if num_1 > num_2 and num_1 > num_3:
        res = num_1
elif num_2 > num_1 and num_2 > num_3:
    res = num_2
elif num_3 > num_1 and num_3 > num_2:
    res = num_3
else:
    res = 'equils'
print("max", res)

if base == 2:
    if num_1 < num_2 and num_1 < num_3:
        res1 = num_1
elif num_2 < num_1 and num_2 < num_3:
    res1 = num_2
elif num_1 > num_3 and num_3 < num_2:
    res1 = num_3
else:
    res1 = 'equals'
print("min", res1)
res2 = (num_1 + num_2 + num_3) / 3
print("avg", res2)
