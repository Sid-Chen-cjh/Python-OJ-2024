def corr(s):
    for i in s:
        if i == "1":
            print("@", end = '')
        elif i == "l":
            print("L", end = '')
        elif i == "0":
            print("%", end = '')
        elif i == "O":
            print("o", end = '')
        else:
            print(i, end = '')

def tec(s):
    if '1' in s:
        return True
    elif 'l' in s:
        return True
    elif '0' in s:
        return True
    elif 'O' in s:
        return True
    else:
        return False

n = int(input())
k = []
v = []
for i in range(n):
    s = input().split()
    k.append(s[0])
    v.append(s[1])
    #if s[0] not in data:
    #    data[s[0]] = s[1]
    #if s[0] in data:
    #用字典的弊端：keys不能重复

time = 0
for i in v:
    if tec(i):
        time += 1
if time == 0 and n > 1:
    print("There are {} accounts and no account is modified".format(n))
elif time == 0 and n == 1:
    print("There is 1 account and no account is modified")
else:
    print(time)

for i in range(n):
    if tec(v[i]):
        print(k[i], end = ' ')
        corr(v[i])
        print('\n', end = '')