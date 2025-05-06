def min_sum(D):
    min = {}
    for i in D:
        if i == 1:
            min[i] = D[i]
        else:
            min[i] = D[i] + min[i-1]
    return min

def max_sum(D):
    max = {}
    for i in range(len(D), 0, -1):
        if i == len(D):
            max[i] = D[i]
        else:
            max[i] = D[i] + max[i + 1]
    return max

m = int(input())
score = input()
num = {}
for i in range(m):
    num[i+1] = list(map(int, score.split(' ')))[i]
L, R = map(int, input().split(' '))

min_num = min_sum(num)
max_num = max_sum(num)
t = 0
for k in num:
    if k == 1:
        continue
    if L <= min_num[k-1] <= R and L <= max_num[k] <= R:
        print(k)
        t = 1
        break
if t != 1:
    print("0")
