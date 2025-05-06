import json

j = json.loads(input())
# a = eval(input()) 似乎能达到相同效果 -> 内存超限！
n = 0
ls = []
for i in j[0]:
    n += 1
    ls.append(i)
    if n == len(j[0]):
        print(i)
    else:
        print(i, end = ',')
for i in j:
    n = 0
    for t in ls:
        n += 1
        if n == len(ls):
            print(i[t])
        else:
            print(i[t], end = ',')