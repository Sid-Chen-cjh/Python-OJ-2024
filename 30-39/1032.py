a = int(input())
str = []
for i in range(a):
    str.append(input())

def sum(x):
    sum = 0
    t = {"MAX": 0, "MIN": 0, "Digit": 0, "Char": 0}
    for i in x:
        if i.isdigit():
            t["Digit"] += 1
        elif 65 < ord(i) < 91:
            t["MAX"] += 1
        elif 96 < ord(i) <123:
            t["MIN"] += 1
        else:
            t["Char"] += 1
    for i in t:
        if t[i] > 0:
            sum += 1
    return sum

def judge(s):
    if 8 <= len(s) <= 16 and sum(s) > 2:
        print("YES")
    else:
        print("NO")

for i in str:
    judge(i)
