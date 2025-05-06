
stopword = ''
num = []
try:
    for line in iter(input, stopword):
        num.append(int(line))
except EOFError:
    pass
for i in range(len(num)):
    if num[i] == 42:
        break
    else:
        print(num[i])