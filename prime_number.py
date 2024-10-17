a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

if not isinstance(a or b, int):
    print("These numbers is not valid!")

else:
    a = int(a)
    b = int(b)

    def prime(n):
        count = 0

        for i in range(1, n+1):
            if n % i == 0:
               count += 1

        if count == 2:
            return True
        else:
            return False

    print(prime(a))
    print(prime(b))


