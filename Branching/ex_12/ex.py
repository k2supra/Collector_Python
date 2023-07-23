print("Введіть розмір файлу (ГБ)")
gb = int(input("->"))

print("Введіть швидкість інтернету (Б)")
b = int(input("->"))

print("1 - год / 2 - хв / 3 - сек")
base = int(input("->"))

part = gb * 1073741824
partt = part / b

if base == 1 :
    res = partt * 3600
    print(f"{res} год")

elif base == 2 :
    res = partt * 60
    print(f"{res} хв")

if base == 3 :
    res = partt
    print(f"{res} сек")