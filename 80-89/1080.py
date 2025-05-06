import json

def printf(ls):
    for i in range(len(ls)):
        if i == len(ls) - 1:
            print(ls[i])
        else:
            print(ls[i], end=',')

str = ''
stopword = ''
try:
    for line in iter(input, stopword):
        str += line
except:
    pass
s = json.loads(str)
title = []
info = []
for i in range(len(s)):
    temp = []
    for j in s[i]:
        if j not in title:
            title.append(j)
        temp.append(s[i][j])
    info.append(temp)
printf(title)
for i in info:
    printf(i)


