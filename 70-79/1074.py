
win = [[0, -1, 1, 1, -1], [1, 0, -1, 1, -1], [-1, 1, 0, -1, 1], [-1, -1, 1, 0, 1], [1, 1, -1, -1, 0]]
n, na, nb = map(int, input().split())
sa = sb = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    sa += win[a[i%na]][b[i%nb]]
    sb += win[b[i%nb]][a[i%na]]
print(sa,sb)
