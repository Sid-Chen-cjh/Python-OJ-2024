"""
# 内存超限
n = int(input())
qlt = list(map(int, input().split()))
p = int(input())
gl = []
for i in range(p):
    gl.append(int(input()))
ans = set()
# 使用 set 来存储唯一的结果
for i in range(n):
    for j in range(i+1, n):
        ans.add(qlt[i] | qlt[j])
for i in range(p):
    if gl[i] in ans:
        print("YES")
    else:
        print("NO")
"""