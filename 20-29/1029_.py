"""
#最精简的方法
import json

stopword = ''
a = []
try:
    for line in iter(input,stopword):
        a.append(line.split(","))
except EOFError:
    pass
b = []
for i in a[1:]:
    b.append(dict(sorted(zip(a[0],i))))
print(b)
print(json.dumps(b,indent = 4))
"""
"""
#仿写的较规范写法
import json
stopword = ''
csv_ls = []
try:
    for line in iter(input,stopword):
        temp = list(line.split(','))
        csv_ls.append(temp)
except EOFError:
    pass
D = []
for i in csv_ls[1:]:
    d = {}
    for j in range(len(i)):
        d[csv_ls[0][j]] = i[j]
    D.append(d)
print(json.dumps(D, sort_keys = True, indent = 4))
"""

"""
#比较低级但可行
import json

stopword = ''
csv_ls = []
try:
    for line in iter(input,stopword):
        csv_ls.append(line)
except EOFError:
    pass

def trans(ls):
    l = len(ls[0].split(','))
    key = []
    ans = []
    for i in range(l):
        key.append(ls[0].split(',')[i])
    for i in range(len(ls)):
        D = {}
        if ls[i] == ls[0]:
            continue
        for j in range(l):
            D[str(key[j])] = ls[i].split(",")[j]
        ans.append(D)
    print(json.dumps(ans, sort_keys = True, indent = 4))

trans(csv_ls)
"""

#重写
import json
data = []
try:
    for line in iter(input, ''):
        temp = list(line.split(','))
        data.append(temp)
except:
    pass
D  = []
for i in data[1:]:
    temp = {}
    for j in range(len(data[0])):
        temp[data[0][j]] = i[j]
    D.append(temp)
print(json.dumps(D, sort_keys = True, indent = 4))

