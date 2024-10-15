a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
r = 1
a = int(a)
b = int(b)

if a > b:
    while r !=0:
        r = a % b
        a = b
        b = r
    print("{}が最大公約数です。".format(a))
elif a < b:
    while r != 0:
        r = b % a
        b = a
        a = r
    print("{}が最大公約数です。".format(b))



