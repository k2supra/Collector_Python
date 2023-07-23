print("1 число")
n1 = int(input("->"))
print("2 число")
n2 = int(input("->"))

for i in range(n1, n2+1):
    if i %2==0:
        print(i)

for i in range(n2+1, n1):
    if i %2==0:
        print(i)