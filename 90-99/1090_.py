n = int(input())
a, b, c = map(int, input().split())
m = max(a, b, c)
# 题干描述不清晰，不明确为什么不能取0
if n < m or a == 0 or b == 0 or c == 0:
    print("Error!")
else:
    print(n//m)