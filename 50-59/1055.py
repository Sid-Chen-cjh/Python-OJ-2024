a = input()
l = len(a)
a = int(a)
n = []
for i in range(l):
    n.append(a%10)
    a = a//10
n = sorted(n)

s = {}
for i in n:
    s[i] = s.get(i,0) + 1
for i in s:
    print("{}:{}".format(i,s[i]))