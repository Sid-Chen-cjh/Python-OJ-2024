n = int(input())
num = []
for i in range(n):
    num.append(input())

def judge(s):
    l = len(s)
    s = int(s)
    a = s % pow(10,l//2)
    b = s // pow(10,l//2)
    m = a * b
    if m ==0:
        print("No")
    elif s % m ==0:
        print("Yes")
    else:
        print("No")

for i in num:
    judge(i)