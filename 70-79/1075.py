import json

csv_ls = []
stopword = ''
try:
    for line in iter(input, stopword):
        temp = list(line.split(','))
        csv_ls.append(temp)
except EOFError:
    pass

ans = []
for i in csv_ls[1:]:
    d = {}
    for j in range(len(i)):
        d[csv_ls[0][j]] = i[j]
    if 'target' in d and d['target'] == '1':
        ans.append(d)
if len(ans) != 0:
    print(json.dumps(ans, indent = 4))
else:
    print("File is not OK!")