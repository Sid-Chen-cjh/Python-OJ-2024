n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
t = int(input())
search = []
for i in range(t):
    search.append(int(input()))
num = sorted(num)
for j in range(t):
    print(num[search[j]])