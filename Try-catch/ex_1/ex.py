print("1 number")
n1 = int(input("->"))
print("2 number")
n2 = int(input("->"))

try:
    f = 0

    for i in range(n1, n2+1):
        f = f + i
    print(f)

    for m in range(n1, n2+1):
        ges = f / i
        print(ges)
        break

except Exception as ex:
    print('Error:', ex)