n = int(input("input number:\t"))
s = n
for i in range(n):
    for n in range(s):
        print("*", end=" ")
    print("")


n = int(input("input number:\t"))
for i in range(n+1):
    for s in range(i):
        print(s+1, end=" ")
    print("")
for i in range(n+1):
    for s in range(i):
        print("*", end=" ")
    print("")


n = input("input number:\t")
print(len(n))

start = int(input("Input the starting point:\t"))
end = int(input("input the ending point:\t"))
prime_numbers = []
for number in range(start, end):
    if number > 1:
        if number % 2 == 0:
            continue
        for i in range(3, (number//2)+3):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)

print(prime_numbers)


n = int(input("input number:\t"))
for i in range(n+1):
    for a in range(i):
        print("*", end=" ")
    print("")
    if i == n:
        for i in range(n-1,0,-1):
            for a in range(i,0,-1):
                print("*", end=" ")
            print("")


n = int(input("input number of words:\t")) # bareri qanaki nermucum
word = {}
answer = {}
for i in range(1,n+1):         # dictionary-i nermucum
    s = input(f"input {i} word:\t")
    word[i] = s
print(word)
for w in word:                 
    g = word[w]
    if g in answer:
        continue
    answer[g] = len(g)
print(answer)
