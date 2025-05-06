a = int(input().strip())
a4 = 0
a7 = 0
while a%4==0:
    a4 += 1
    a = a//4
while a%7==0 :
    a7 += 1
    a = a//7
print(a4, a7)