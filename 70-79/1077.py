s = input().split()
s.reverse()
for i in s[0: -1]:
    print(i, end = ' ')
print(s[-1])