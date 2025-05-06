
def is_prime(n):
    if n == 1:return False
    else:
        for i in range(2,int(pow(n, 0.5))+1):
            if n % i == 0:
                return False
        return True

n = int(input())
m = int(input())
r = 0
for i in range(2, n+1):
    if is_prime(i) and is_prime(i+m):
        print(i, i+m)
        r = 1
if r == 0:
    print("Empty")


