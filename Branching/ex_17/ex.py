print("Введіть 1 число")
val1 = int(input("->"))

print("Введіть 2 число")
val2 = int(input("->"))

if val1 > val2:
    print(f"{val1} , {val2}")

elif val1 < val2:
    print(f"{val2} , {val1}")

else:
    print(f"{val1} = {val2}")