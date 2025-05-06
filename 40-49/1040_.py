"""
n = list(map(int, input().split()))

def trans_num(n, k):
    ans = []
    m = n
    while m // k != 0:
        temp = m % k
        if temp >= 10:
            temp = chr(temp - 10 + ord('A'))
        ans.append(temp)
        m = m // k
    ans.append(m)
    ans.reverse()
    return ans

ans = trans_num(n[0], n[1])
for i in range(len(ans)):
    print(ans[i], end = '')
"""

#重写

def trans(a, b):
    if b == 2:
        return bin(a)[2:]
    elif b == 8:
        return oct(a)[2:]
    elif b == 16:
        return hex(a)[2:]
    else:
        temp = ''
        t = a
        while a != 0:
            temp += str(a%b)#未考虑大于10！！！！
            a //= b
        return temp


a, b = map(int, input().split())
ans = trans(a, b)
for i in range(len(trans(a, b))-1, -1, -1):
    print(ans[i], end = '')