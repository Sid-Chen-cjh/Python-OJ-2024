
def is_prime(x):
    if x == 1:return False
    else:
        for i in range(2, int(pow(x, 0.5))+1):
            if x % i == 0:
                return False
        return True

m = int(input())
a = []
s = 0
while s < 2:
    if is_prime(m):
        a.append(m)
        s += 1
    m -= 1
print(sorted(a))