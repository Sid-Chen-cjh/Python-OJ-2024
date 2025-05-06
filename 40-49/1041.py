
a = list(map(int, input().split()))

def plus(n):
    ans = temp = 0
    for i in range(n):
        temp += 10 ** i
        ans += temp
    return ans

print("{}".format(plus(a[0]) * a[1]))


"""
#字符串拼接和转换操作会牺牲高昂的代价
def plus(n):
    ans = 0
    m = ""
    for i in range(n):
        m += str(1)
        ans += int(m)
    return ans
"""