"""
def cite(str):
    a = []
    for i in range(len(str)):
        if str[i] == '"':
            for j in range(len(str) - i - 1):
                if str[i+j+1] == ':' or str[i+j+1] == ',': #溢出风险
                    break
                elif str[i+j+1] == '"':
                    a.append(str[i+1:i+j+1])
                    break
    return a

ans = {}
str = input()
x = input()
s = str[1:-1]
a = cite(s)
for i in range(len(a)//2):
    ans[a[i*2]] = a[i*2+1]
print(ans[x])

"""

a = eval(input())
b = input()
print(a[b])