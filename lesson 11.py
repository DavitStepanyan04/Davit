def separation(num1, num2):
    try:
        S = num1 / num2
        return S
    except(ZeroDivisionError):
        return None


num1 = int(input("input first number:\t"))
num2 = int(input("input second number:\t"))
print(separation(num1, num2))


def Sum(L, S):
    try:
        for h in L:
            S += h
        return S
    except(TypeError):
        return None



L = [5, 8, "hello", 257, 777]
S = 0
print(Sum(L, S))


def Error(h):
    try:
        with open("text.txt", "r") as h:
            for i in h:
                print(i)
    except(FileNotFoundError):
        return None
h = open("text.txt", "a")
print(Error(h))


def IError(L):
    try:
        x1 = L[0]
        x2 = L[-1]
        H = x1 * x2
        return H
    except(IndexError,TypeError):
        return None




L = []
num = input("input quantity number")
L.append(num)
print(IError(L))