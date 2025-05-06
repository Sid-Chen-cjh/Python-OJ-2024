"""
# 输出超限：输出超过限制，8%的样例输出比正确答案长了两倍
#!/usr/bin/python3
def select(s):
    t = s.split(',')
    l = len(t)
    for i in range(l):
        if 'target' in t[i]:
            return i
    return -1

stopword = ''
csv = []
try:
    for line in iter(input, stopword):
        csv.append(line)
except EOFError:
    pass

record = 0
aim = select(csv[0])
if aim != -1:
    for i in range(len(csv)):
        temp = csv[i].split(',')
        if temp[aim] == '1':
            print(csv[i])
        else:
            record += 1
if record == len(csv) or aim == -1:
    print("File is not OK!")
"""


# 内存超限：超出内存限制，数据可能需要压缩，检查内存是否有泄露
import json
csv_s = []
stopword = ''
try:
    for line in iter(input, stopword):
        csv_s.append(line)
except:
    pass
json_s = []
for i in csv_s[1:]:
    temp = {}
    for j in range(len(i.split(','))):
        temp[csv_s[0].split(',')[j]] = i.split(',')[j]
    json_s.append(temp)
json_s = eval(json.dumps(json_s))
for i in range(len(json_s)):
    if json_s[i]["target"] == '1':
        print(csv_s[i+1])







'''
  ▓█████░▒██  ▓██░ ▄████▄▄ ▒██ ▄█▀       ██████╗ ██╗   ██╗ ██████╗
  ▓██   ░▒██  ▓██░▒██▀ ▀█▓░ ██▄█▒        ██╔══██╗██║   ██║██╔════╝
  ▓████ ░▒██  ▒██░▒██    ▄ ░███▄░        ██████╔╝██║   ██║██║  ███╗
  ▒█▒   ░▒▓█  ░██░▒▓█▄ ▄██░░██ █▄        ██╔══██╗██║   ██║██║   ██║
  ▒█░    ▒▒████▒░ ▒ ▓███▀ ░▒██▒ █▄       ██████╔╝╚██████╔╝╚██████╔╝
   ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒       ╚═════╝  ╚═════╝  ╚═════╝
   ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
   ░ ░    ░░░ ░ ░ ░        ░ ░░ ░
            ░     ░ ░      ░  ░
'''