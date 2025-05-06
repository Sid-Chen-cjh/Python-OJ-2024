n = int(input())
age = []
while len(age) < n:
    temp = list(map(int, input().split()))
    #错误原因：样例中不全是用空格分隔的
    age += temp
age = sorted(age)

sta = {}
for i in age:
    if i not in sta:
        sta[i] = 1
    else:
        sta[i] += 1

for i in sta:
    print("{}:{}".format(i, sta[i]))
