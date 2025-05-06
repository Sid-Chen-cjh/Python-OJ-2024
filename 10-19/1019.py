import math as m
def if_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(m.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

a = input()
if a.isalpha():
    print("invalid")
elif float(a) % 1 != 0:
    print("invalid")
elif int(a) < 0:
    print("invalid")
else:
    print(if_prime(int(a)))
