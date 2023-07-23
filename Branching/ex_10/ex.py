print("Введіть діаметр")
di = int(input("->"))
print("1 - площа / 2 - периметр")
ch = int(input("->"))

if ch == 1 :
    res1 = (3.14 / 4) * (di * di)
    print(f"{res1}")

elif ch == 2 :
    res2 = 3.14 * di
    print(f"{res2}")