#!/usr/bin/python3

stopword = ''
stri = ''
try:
    for line in iter(input, stopword):
        stri += line + '\n'
except EOFError:
   pass
stri = stri[0:-1]

spa = num = let = oth = 0
for i in stri:
    if i == ' ':
        spa += 1
    elif i.isdigit():
        num += 1
    elif i.isalpha():
        let += 1
    else:
        oth += 1
print("{} spaces, {} numbers, {} letters, {} other characters.".format(spa, num, let, oth))

