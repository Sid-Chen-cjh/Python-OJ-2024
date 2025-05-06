n = int(input())

for i in range(1, n+1, 2):
    for j in range((n-i)//2):
        print(" ", end = '')
    for i in range(i):
        print("*", end = '')
    for j in range((n-i)//2):
        print(" ", end = '')
    print("\n", end = '')
