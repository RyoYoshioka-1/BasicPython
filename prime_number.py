a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

a = int(a)
b = int(b)

count = 0

for i in range(1, a+1):
    if a % i ==0:
        count += 1   

if count == 2:
    print("{} is prime number!".format(a))
else:
    print("{} is not prime number.".format(a))

for i in range(1, b+1):
    if b % i ==0:
        count += 1

if count == 2:
    print("{} is prime number!".format(b))
else:
    print("{} is not prime number.".format(b))