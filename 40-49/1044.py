
def trans(s):    # s为一个4位字符串
    ans = 0
    for i in s:
        ans += pow(256, 3-s.index(i)) *ord(i)###~~~!!!!!!
    return ans

n = int(input())
all = []
for i in range(n):
    all.append(list(input().split()))
ans = []
for i in range(n):
    ans.append(trans(all[i][0]) + trans(all[i][1]))###~~~!!!!!!
print(ans)
