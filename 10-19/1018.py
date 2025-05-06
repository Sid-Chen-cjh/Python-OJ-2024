stopword = ''
str = ''
try:
    for line in iter(input, stopword):
        str += line + ' '
except EOFError:
    pass
str = str[:-1]

D = {}
for i in str.split(' '):
    if i in D:
        D[i] += 1
    else:
        D[i] = 1
max = 1
for i in D:
    if D[i] > max:
        max = D[i]
print(max)


