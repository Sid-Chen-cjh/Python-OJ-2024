import math as m

def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(m.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

a = int(input())
multi = 1
for i in range(a//2):
    if is_prime(i) and is_prime(a - i) and i * (a - i) > multi:
        multi = i * (a - i)
print(multi)
