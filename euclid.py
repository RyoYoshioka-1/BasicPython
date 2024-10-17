a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a = int(a)
b = int(b)


def euclid(a, b):
    r = 1

    if a > b:
        while r !=0:
            r = a % b
            a = b
            b = r
        return "{}が最大公約数です。".format(a)
    elif a < b:
        while r != 0:
            r = b % a
            b = a
            a = r
        return "{}が最大公約数です。".format(b)

print(euclid(a, b))

def prime():
    if euclid(a, b) == "1が最大公約数です。":
        return "さらにこの二数は互いに素です"
    else:
        return "しかし、互いに素ではありません"

print(prime())



