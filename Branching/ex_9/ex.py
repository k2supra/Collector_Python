print("Введіть час (с)")
value = int(input("->"))
print("1 - год / 2 - хв / 3 - сек / 4 - год хв сек")
time = int(input("->"))
res = 86400 - value

if time == 1 :
    part_1 = res / 3600
    print(f"Залишилось {part_1} годин/и до кінця дня")

elif time == 2 :
    part_2 = res / 60
    print(f"Залишилось {part_2} хвилин/и до кінця дня")

elif time == 3 :
    part_3 = res
    print(f"Залишилось {part_3} секунд/и до кінця дня")

elif time == 4 :
    part_1 = res / 3600
    part_2 = res / 60
    part_3 = res
    print(f"Залишилось {part_1} годин/и до кінця дня")
    print(f"Залишилось {part_2} хвилин/и до кінця дня")
    print(f"Залишилось {part_3} хвилин/и до кінця дня")