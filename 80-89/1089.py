import math

def cakes(n):
    ans = math.ceil(n/10)
    return ans
a = int(input())
num = 0
stu = list(map(int, input().split()))
for i in range(a):
    num += cakes(stu[i])
print(num)

"""
提示：
使用 math 库中的函数，其中向上取整是 ceil，调用方法是 math.ceil(x) ；
向下取整是 floor，调用方法是 math.floor(x)；
其中 x 为一个浮点数。
"""