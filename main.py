quantity = int(input("import numbers count:\t"))
L = []
for i in range(quantity):
    number = int(input(f"input {i} number:\t"))
    L.append(number)
print(L)
M = []
for n in L:
    n *= n
    M.append(n)
print(M)


number = int(input("import numbers count:\t"))
L = []
for i in range(number):
    s = int(input(f"input {i} number:\t"))
    L.append(s)
print(L)
sum = 0
for n in L:
    sum += n
print(sum)


number = int(input("import numbers count:\t"))
L = []
for i in range(number):
    s = int(input(f"input {i} number:\t"))
    L.append(s)
print(L)
sum = 1
for n in L:
    sum *= n
print(sum)


number = int(input("import numbers count:\t"))
L = []
for i in  range(number):
    n = int(input(f"input {i} number:\t"))
    L.append(n)
print(L)
for index in range(len(L)):
    if L[index] == 20:
        L[index] = 200
        break
    else:
        print("The number 20 was not found in the list")
print(L)