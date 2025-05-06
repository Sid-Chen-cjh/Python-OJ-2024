a = input().split()
l = int(a[0])//2
if int(a[0])*2 >= l*4+1:
    l += 1
for i in range(l):
    for j in range(int(a[0])):
        print(a[1], end = '')
    print('')
