Str = input("input string:\t")
if len(Str) % 2 != 0:
    Str1 = (len(Str) - 3) // 2
    print(Str[Str1:-Str1])
else:
    print("the number of symbols in the word is even")


Str = input("input string:\t")
if len(Str) > 3:
    if Str[-1:-4:-1] == "gni":
        print(Str + "ly")
    else:
        print(Str + "ing")
else:
    print(Str)


Str = input("input string:\t")
if Str[:] == Str[::-1]:
    print("String is Palindrome")
else:
    print("String is not Palindrome")


Str = input("input string:\t")
n = int(input("input number for delete index"))
Str1, Str = Str[:n-1], Str[n:]
print(Str1 + Str)


Str = input("input string:\t")
print(Str.lower())