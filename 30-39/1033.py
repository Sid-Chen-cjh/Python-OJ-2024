l = int(input())
a = []
for i in range(l):
    a.append(int(input()))

#迭代法
def fibo(n):
    fro = 1
    lat = 1
    #ans = 0
    if n == 0:
        return 1
    else:
        for i in range(n):
            #ans += fro
            fro, lat = lat, fro + lat
            #ans表示前n项和，fro指向第n项
    return fro

for i in range(l):
    print(fibo(a[i]))








"""
#无脑递归
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(l):
    print(fibo(a[i]))
"""


"""
#空间换时间
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141]
for i in range(l):
    m = a[i]
    print(b[m])
"""