
def judge(x):
    if x == "*":
        return 1
    else:
        return 0

bomb = []
ans = []
n, m = map(int, input().split())
for i in range(n):
    bomb.append(input())
    ans.append([])
    for j in range(m):
        if bomb[i][j] == "*":
            ans[i].append("*")
        else:
            ans[i].append(0)
#角
if bomb[0][0] != "*":
    ans[0][0] +=(judge(bomb[0][1])+judge(bomb[1][1])+judge(bomb[1][0]))
if bomb[0][m-1] != "*":
    ans[0][m-1] +=(judge(bomb[0][m-2])+judge(bomb[1][m-2])+judge(bomb[1][m-1]))
if bomb[n-1][0] != "*":
    ans[n-1][0] +=(judge(bomb[n-2][0])+judge(bomb[n-2][1])+judge(bomb[n-1][1]))
if bomb[n-1][m-1] != "*":
    ans[n-1][m-1] +=(judge(bomb[n-2][m-2])+judge(bomb[n-2][m-1])+judge(bomb[n-1][m-2]))
#边
for i in range(1, n-1):
    if bomb[i][0] != "*":
        ans[i][0] +=judge(bomb[i-1][0])+judge(bomb[i-1][1])+judge(bomb[i][1])+judge(bomb[i+1][0])+judge(bomb[i+1][1])
    if bomb[i][m-1] != "*":
        ans[i][m-1] += judge(bomb[i - 1][m-1]) + judge(bomb[i - 1][m-2]) + judge(bomb[i][m-2]) + judge(bomb[i + 1][m-1]) + judge(bomb[i + 1][m-2])
for j in range(1,m-1):
    if bomb[0][j] != "*":
        ans[0][j] +=judge(bomb[0][j-1])+judge(bomb[1][j-1])+judge(bomb[1][j])+judge(bomb[1][j+1])+judge(bomb[0][j+1])
    if bomb[n-1][j] != "*":
        ans[n-1][j] += judge(bomb[n-1][j - 1]) + judge(bomb[n-2][j-1]) + judge(bomb[n-2][j]) + judge(bomb[n-2][j+1]) + judge(bomb[n-1][j + 1])
#内部
for i in range(1, n-1):
    for j in range(1, m-1):
        if bomb[i][j] != "*":
            ans[i][j] += judge(bomb[i-1][j-1])+judge(bomb[i-1][j])+judge(bomb[i-1][j+1])+judge(bomb[i][j-1])+judge(bomb[i][j+1])+judge(bomb[i+1][j-1])+judge(bomb[i+1][j])+judge(bomb[i+1][j+1])

for i in range(n):
    for j in range(m):
        print(ans[i][j], end = '')
    print('')