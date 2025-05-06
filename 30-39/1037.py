
def count(s):
    statistics = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n':0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            statistics[i] += 1
    return statistics

a = list(input().split(', '))
num = []
ans = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n':0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
same = []
for i in a:
    num.append(count(i))
for i in ans.keys():
    ans[i] = min(num[j][i] for j in range(len(num)))
    if ans[i] != 0:
        for j in range(ans[i]):
            same.append(i)

print('"', end = '')
for i in same:
    print(i, end = '')
print('"',end = '')