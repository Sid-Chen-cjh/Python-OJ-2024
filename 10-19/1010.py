a = int(input())
b = []
c = 0
for i in range(a):
    b.append(int(input()))
    c += b[i]

d = c/a
print(f"{c} {d:.5f}")
print(c,end = ' ')
print(f"{d:.5f}")

"""
列表.append()
print( 变量， end=' ')
格式化字符串: f"{变量/表达式}"
"""