m, n, a, b, t = map(int, input().split())
color = []
for i in range(m):
    temp = list(map(int, input().split()))
    color.append(temp)
for i in range(m):
    for j in range(n):
        if a <= color[i][j] <= b:
            color[i][j] = t
        if j == n - 1:
            print("{:0>3}".format(color[i][j]))
        else:
            print("{:0>3}".format(color[i][j]), end = ' ')