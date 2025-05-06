#140925 2004 01 31 003 9

def judge(s):
    for i in range(17):
        if not s[i].isdigit():
            return False
    return True
def culculate(s):
    power = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    D = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    sum = 0
    for i in range(17):
        sum += int(s[i]) * power[i]
    sum %= 11
    return D[sum]

n = int(input())
id_num = []
for i in range(n):
    id_num.append(input())
r = 0
for i in id_num:
    if judge(i):
        if i[17] != culculate(i):
            r = 1
            print(i)
    else:
        r = 1
        print(i)
if r == 0:
    print("All passed")

