l = int(input())
a = list(map(int,input().split()))
num = {5:0,0:0}
for i in a:
    if i == 5:
        num[5] += 1
    else:
        num[0] += 1

if num[0] == 0:
    print(-1)
else:
    for i in range(num[5]//9):
        print(555555555, end = '')
    if num[5]//9 == 0:
        print(0)
    else:
        for i in range(num[0]):
            print(0, end = '')