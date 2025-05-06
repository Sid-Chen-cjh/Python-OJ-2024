import re

def to_rgb(s):
    a = re.findall(r'.', s)
    print(a)


def from_rgb(s):
    a = re.findall(r'\d', s)
    print(len(a))






str = []
stopword = ''
try:
    for line in iter(input, stopword):
        str.append(line)
except:
    pass
ans = []
for i in str:
    if '#' in i:
        to_rgb(i)

    elif 'rgb' in i:
        from_rgb(i)

print(ans)