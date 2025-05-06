
a = int(input())
str = []
for i in range(a):
    str.append(int(input()))

D = {}
for i in range(len(str)):
    if str[i] in D:
        print("True\n{}".format(i+1))
        break
    else:
        D[str[i]] = 1

if len(D.keys()) == a:
    print("False")